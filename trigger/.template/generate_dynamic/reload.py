import lib
import logging
import os
import re
import hashlib
import json
from zipfile import ZipFile
from StringIO import StringIO

remote = None

LOG = logging.getLogger(__name__)

class ReloadError(lib.BASE_EXCEPTION):
	pass
	
def run_command(build, args):
	global remote
	from forge import build_config
	import forge
	from forge.remote import Remote

	config = build_config.load()
	remote = Remote(config)
	remote._authenticate()

	if len(args) == 0:
		raise ReloadError("Expecting command to after 'forge reload'")
	if args[0] == 'list':
		if len(args) != 1:
			raise ReloadError("Invalid number of arguments passed to 'forge reload list'")
		list_streams(build)
	elif args[0] == 'create':
		if len(args) != 2:
			raise ReloadError("Invalid number of arguments passed to 'forge reload create'")
		create_stream(build, args[1])
	elif args[0] == 'push':
		if len(args) != 2:
			raise ReloadError("Invalid number of arguments passed to 'forge reload push'")
		push_stream(build, args[1])
	else:
		raise ReloadError("Unknown command 'forge reload %s'" % args[0])

def list_streams(build):
	LOG.info("List of streams from website:")
	streams = remote._api_get('reload/%s/streams' % build.config['uuid'])
	if streams['result'] != 'ok':
		raise ReloadError("Fetching remote streams failed")
		
	for stream in streams['streams']:
		LOG.info('%s' % stream['name'])

def create_stream(build, stream_id):
	# Validate id
	if not re.match("^[a-z0-9_-]+$", stream_id):
		raise ReloadError("Invalid stream id, must only contain lowercase a-z, 0-9, - and _.")

	LOG.info("Create stream with website")
	created = remote._api_post('reload/%s/streams' % build.config['uuid'], data={'name': stream_id})
	if created['result'] != 'ok':
		raise ReloadError("Remote stream creation failed")

	LOG.info("Stream created, use 'forge reload push %s' to push a snapshot" % stream_id);

def push_stream(build, stream_id):
	from forge import build_config
	manifest = dict()
	file_for_hash = dict()

	# TODO: Some kind of partial build (insert all.js references)
	
	src = os.path.join('development', 'reload', 'src')
	for root, dirs, files in os.walk(src):
		for filename in files:
				filename = os.path.join(root, filename)
				with open(filename, 'rb') as file:
					hash = hashlib.sha1(file.read()).hexdigest()
					manifest[filename[len(src)+1:].replace('\\','/')] = hash
					file_for_hash[hash] = filename

	remote_hashes = remote._api_post('reload/snapshots/filter', files={'manifest': StringIO(json.dumps(manifest))})
	if remote_hashes['result'] != 'ok':
		raise ReloadError("Remote hash filter failed")
	hashes_to_upload = set(remote_hashes['manifest'].values())

	with lib.temp_file() as zip_file_path:
		with ZipFile(zip_file_path, 'w') as zip_file:
			for hash in hashes_to_upload:
				zip_file.write(file_for_hash[hash], hash)

		with open(zip_file_path, 'rb') as zip_file:
			created = remote._api_post('reload/snapshots/%s/%s' % (build.config['uuid'], stream_id), files={'config': StringIO(json.dumps(build_config.load_app())), 'manifest': StringIO(json.dumps(manifest)), 'forge-deploy': zip_file})
			if created['result'] != 'ok':
				raise ReloadError("Remote snapshot creation failed")
	LOG.info("Pushed snapshot to stream '%s'" % stream_id)