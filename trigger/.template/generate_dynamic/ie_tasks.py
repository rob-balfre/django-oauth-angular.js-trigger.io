import os
from os import path
import shutil, glob
import uuid
import hashlib
from subprocess import PIPE, STDOUT

import lib
from lib import CouldNotLocate, task

class IEError(Exception):
	pass

@task
def package_ie(build, **kw):
	'Run NSIS'
	
	nsis_check = lib.PopenWithoutNewConsole('makensis -VERSION', shell=True, stdout=PIPE, stderr=STDOUT)
	stdout, stderr = nsis_check.communicate()
	
	if nsis_check.returncode != 0:
		raise CouldNotLocate("Make sure the 'makensis' executable is in your path")
	
	# JCB: need to check nsis version in stdout here?
	
	development_dir = path.join("development", "ie")
	release_dir = path.join("release", "ie")
	if not path.isdir(release_dir):
		os.makedirs(release_dir)

	for arch in ('x86', 'x64'):
		nsi_filename = "setup-{arch}.nsi".format(arch=arch)
		
		package = lib.PopenWithoutNewConsole('makensis {nsi}'.format(
			nsi=path.join(development_dir, "dist", nsi_filename)),
			stdout=PIPE, stderr=STDOUT, shell=True
		)
	
		out, err = package.communicate()
	
		if package.returncode != 0:
			raise IEError("problem running {arch} IE build: {stdout}".format(arch=arch, stdout=out))
		
		# move output to release directory of IE directory
		for exe in glob.glob(development_dir+"/dist/*.exe"):
			shutil.move(exe,
				path.join(release_dir, "{name}-{version}-{arch}.exe".format(
					name=build.config.get('name', 'Forge App'),
					version=build.config.get('version', '0.1'),
					arch=arch
				))
			)

def _generate_package_name(build):
	if "package_names" not in build.config["modules"]:
		build.config["modules"]["package_names"] = {}
	build.config["modules"]["package_names"]["ie"] =  _uuid_to_ms_clsid(build)
	return build.config["modules"]["package_names"]["ie"]

def _uuid_to_ms_clsid(build):
	md5   = hashlib.md5(build.config['uuid'])
	guid  = uuid.UUID(md5.hexdigest())
	clsid = uuid.UUID(guid.bytes_le.encode('hex'))
	return "{" + str(clsid).upper() + "}"
