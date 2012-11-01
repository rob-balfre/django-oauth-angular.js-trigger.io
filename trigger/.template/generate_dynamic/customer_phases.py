"Tasks that might be run on the customers's machine"

from os import path
from time import gmtime
from calendar import timegm

# where the customer code exists inside the apps
locations = {
	'android': 'development/android/assets/src',
	'ios': 'development/ios/*/assets/src',
	'chrome': 'development/chrome/src',
	'firefox': 'development/firefox/resources/f/data/src',
	'safari': 'development/forge.safariextension/src',
	'ie': 'development/ie/src',
	'web': 'development/web/src',
	'wp': 'development/wp/assets/src',
	'reload': 'development/reload/src',
}

def validate_user_source(src='src'):
	'''Check for any issues with the user source, i.e. no where to include all.js'''
	return [
		{'do': {'check_index_html': (src,)}}
	]

def copy_user_source_to_tempdir(ignore_patterns=None, tempdir=None):
	return [
		{'do': {'copy_files': {'from': 'src', 'to': tempdir, 'ignore_patterns': ignore_patterns}}},
	]

def delete_tempdir(tempdir=None):
	return [
		{'do': {'remove_files': tempdir}},
	]

def run_hook(hook=None, dir=None):
	return [
		{'do': {'run_hook': {'hook': hook, 'dir': dir}}},
	]

def copy_user_source_to_template(ignore_patterns=None, src='src'):
	return [
		{'when': {'platform_is': 'android'}, 'do': {'copy_files': { 'from': src, 'to': locations["android"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'ios'}, 'do': {'copy_files': { 'from': src, 'to': locations["ios"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'chrome'}, 'do': {'copy_files': { 'from': src, 'to': locations["chrome"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'firefox'}, 'do': {'copy_files': { 'from': src, 'to': locations["firefox"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'safari'}, 'do': {'copy_files': { 'from': src, 'to': locations["safari"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'ie'}, 'do': {'copy_files': { 'from': src, 'to': locations["ie"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'web'}, 'do': {'copy_files': { 'from': src, 'to': locations["web"], 'ignore_patterns': ignore_patterns }}},
		{'when': {'platform_is': 'wp'}, 'do': {'copy_files': { 'from': src, 'to': locations["wp"], 'ignore_patterns': ignore_patterns }}},
		{'do': {'copy_files': { 'from': src, 'to': locations["reload"], 'ignore_patterns': ignore_patterns }}},
	]
	
def include_platform_in_html(server=False):
	return [
		{'when': {'platform_is': 'android'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["android"],
			"find": "<head>",
			"replace": "<head><script src='/forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["ios"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["firefox"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'chrome'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["chrome"],
			"find": "<head>",
			"replace": "<head><script src='/forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["safari"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["ie"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'web'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["web"],
			"find": "<head>",
			"replace": "<head><script src='/_forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["wp"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace_in_dir': {
			"root_dir": locations["wp"],
			"find": "<head>",
			"replace": """<head>
				<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
				<script>
					function window$forge$_receive(result) {
						try {
							window.forge._receive(JSON.parse(result));
						} catch (e) {
							forge.logging.error("window$forge$_receive -> " + e);
						}
					}
				</script>"""
		}}},
		{'do': {'find_and_replace_in_dir': {
			"root_dir": locations["reload"],
			"find": "<head>",
			"replace": "<head><script src='%{back_to_parent}%forge/all.js'></script>"
		}}},
		{'do': {'find_and_replace_in_dir': {
			"root_dir": locations["reload"],
			"find": "<head>",
			"replace": """<head>
				<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
				<script>
				function window$forge$_receive(result) {
					try {
						window.forge._receive(JSON.parse(result));
					} catch (e) {
						forge.logging.error("window$forge$_receive -> " + e);
					}
				}
			</script>"""
		}}},
	]

def include_name():
	return [
		{'do': {'populate_xml_safe_name': ()}},
		{'do': {'populate_json_safe_name': ()}},
		{'when': {'platform_is': 'android'}, 'do': {'set_element_value_xml': {
			"file": 'development/android/res/values/strings.xml',
			"element": "string/[@name='app_name']",
			"value": "${xml_safe_name}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'set_in_biplist': {
			"filename": 'development/ios/*/Info.plist',
			"key": "CFBundleName",
			"value": "${name}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'set_in_biplist': {
			"filename": 'development/ios/*/Info.plist',
			"key": "CFBundleDisplayName",
			"value": "${name}"
		}}},
		{'when': {'platform_is': 'chrome'}, 'do': {'find_and_replace': {
			"in": ('development/chrome/manifest.json',),
			"find": "APP_NAME_HERE", "replace": "${json_safe_name}"
		}}},
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace': {
			"in": ('development/firefox/install.rdf',),
			"find": "APP_NAME_HERE", "replace": "${xml_safe_name}"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace': {
			"in": ('development/forge.safariextension/Info.plist',),
			"find": "APP_NAME_HERE", "replace": "${xml_safe_name}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/manifest.json',
				'development/ie/dist/setup-x86.nsi',
				'development/ie/dist/setup-x64.nsi',
			), "find": "APP_NAME_HERE", "replace": "${json_safe_name}"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace': {
			"in": ('development/wp/Properties/WMAppManifest.xml',),
			"find": "APP_NAME_HERE", "replace": "${xml_safe_name}"
		}}},
	]

def include_uuid():
	return [
		{'do': {'populate_package_names': ()}},
		{'when': {'platform_is': 'android'}, 'do': {'find_and_replace': {
			"in": ('development/android/AndroidManifest.xml',),
			"find": "io.trigger.forge.android.template", "replace": "${modules.package_names.android}"
		}}},
		{'when': {'platform_is': 'android'}, 'do': {'find_and_replace': {
			"in": ('development/android/res/values/strings.xml',),
			"find": "UUID_HERE", "replace": "${uuid}"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace': {
			"in": ('development/wp/Properties/manifest.json',),
			"find": "UUID_HERE", "replace": "${uuid}"
		}}},
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace': {
			"in": ('development/firefox/install.rdf','development/firefox/harness-options.json',),
			"find": "PACKAGE_NAME_HERE", "replace": "${modules.package_names.firefox}"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace': {
			"in": ('development/forge.safariextension/Info.plist',),
			"find": "PACKAGE_NAME_HERE", "replace": "${modules.package_names.safari}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'set_in_biplist': {
			"filename": 'development/ios/*/Info.plist',
			"key": "CFBundleIdentifier", "value": "${modules.package_names.ios}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'find_and_replace': {
			"in": ( 'development/ios/*/app_config.json',),
			"find": "UUID_HERE", "replace": "${uuid}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/manifest.json', 'development/ie/forge/all.js', 'development/ie/forge/all-priv.js',
				   'development/ie/dist/setup-x86.nsi','development/ie/dist/setup-x64.nsi',),
			"find": "UUID_HERE", "replace": "${uuid}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/dist/setup-x86.nsi','development/ie/dist/setup-x64.nsi',),
			"find": "MS_CLSID_HERE", "replace": "${modules.package_names.ie}"
		}}},
	]

def include_author():
	return [
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace': {
			"in": ('development/firefox/install.rdf','development/firefox/harness-options.json',),
			"find": "AUTHOR_HERE", "replace": "${author}"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace': {
			"in": ('development/forge.safariextension/Info.plist',),
			"find": "AUTHOR_HERE", "replace": "${author}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/manifest.json','development/ie/dist/setup-x86.nsi','development/ie/dist/setup-x64.nsi',),
			"find": "AUTHOR_HERE", "replace": "${author}"
		}}},
	]

def include_description():
	return [
		{'when': {'platform_is': 'chrome'}, 'do': {'find_and_replace': {
			"in": ('development/chrome/manifest.json',),
			"find": "DESCRIPTION_HERE", "replace": "${description}"
		}}},
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace': {
			"in": ('development/firefox/install.rdf','development/firefox/harness-options.json',),
			"find": "DESCRIPTION_HERE", "replace": "${description}"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace': {
			"in": ('development/forge.safariextension/Info.plist',),
			"find": "DESCRIPTION_HERE", "replace": "${description}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/manifest.json','development/ie/dist/setup-x86.nsi','development/ie/dist/setup-x64.nsi',),
			"find": "DESCRIPTION_HERE", "replace": "${description}"
		}}},
	]

def include_version():
	return [
		{'when': {'platform_is': 'chrome'}, 'do': {'find_and_replace': {
			"in": ('development/chrome/manifest.json',),
			"find": "VERSION_HERE", "replace": "${version}"
		}}},
		{'when': {'platform_is': 'firefox'}, 'do': {'find_and_replace': {
			"in": ('development/firefox/install.rdf','development/firefox/harness-options.json',),
			"find": "VERSION_HERE", "replace": "${version}"
		}}},
		{'when': {'platform_is': 'safari'}, 'do': {'find_and_replace': {
			"in": ('development/forge.safariextension/Info.plist',),
			"find": "VERSION_HERE", "replace": "${version}"
		}}},
		{'when': {'platform_is': 'ie'}, 'do': {'find_and_replace': {
			"in": ('development/ie/manifest.json',
				'development/ie/dist/setup-x86.nsi','development/ie/dist/setup-x64.nsi',),
			"find": "VERSION_HERE", "replace": "${version}"
		}}},
		{'when': {'platform_is': 'android'}, 'do': {'set_attribute_value_xml': {
			"file": 'development/android/AndroidManifest.xml',
			"attribute": "android:versionCode",
			"value": str(int(timegm(gmtime())))
		}}},
		{'when': {'platform_is': 'android'}, 'do': {'set_attribute_value_xml': {
			"file": 'development/android/AndroidManifest.xml',
			"attribute": "android:versionName",
			"value": "${version}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'set_in_biplist': {
			"filename": 'development/ios/*/Info.plist',
			"key": "CFBundleVersion", "value": str(int(timegm(gmtime())))
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'set_in_biplist': {
			"filename": 'development/ios/*/Info.plist',
			"key": "CFBundleShortVersionString", "value": "${version}"
		}}},
	]

def include_reload():
	return [
		{'do': {'populate_trigger_domain': ()}},
		{'when': {'platform_is': 'android'}, 'do': {'find_and_replace': {
			"in": ('development/android/res/values/strings.xml',),
			"find": "CONFIG_HASH_HERE", "replace": "${config_hash}"
		}}},
		{'when': {'platform_is': 'android'}, 'do': {'find_and_replace': {
			"in": ('development/android/res/values/strings.xml',),
			"find": "TRIGGER_DOMAIN_HERE", "replace": "${trigger_domain}"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace': {
			"in": ('development/wp/Properties/manifest.json',),
			"find": "CONFIG_HASH_HERE", "replace": "${config_hash}"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace': {
			"in": ('development/wp/Properties/manifest.json',),
			"find": "TRIGGER_DOMAIN_HERE", "replace": "${trigger_domain}"
		}}},
		{'when': {'platform_is': 'wp'}, 'do': {'find_and_replace': {
			"in": ('development/wp/Properties/manifest.json',),
			"find": "VERSION_CODE_HERE", "replace": str(int(timegm(gmtime())))
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'find_and_replace': {
			"in": ('development/ios/*/app_config.json',),
			"find": "CONFIG_HASH_HERE", "replace": "${config_hash}"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'find_and_replace': {
			"in": ('development/ios/*/app_config.json',),
			"find": "TRIGGER_DOMAIN_HERE", "replace": "${trigger_domain}"
		}}},
	]

def resolve_urls():
	return [
		{'do': {'resolve_urls': (
			'modules.activations.[].scripts.[]',
			'modules.activations.[].styles.[]',
			'modules.icons.*',
			'modules.launchimage.*',
			'modules.button.default_icon',
			'modules.button.default_popup',
			'modules.button.default_icons.*'
		)}},
	]

def run_android_phase(build_type_dir, sdk, device, interactive, purge=False):
	return [
		{'when': {'platform_is': 'android'}, 'do': {'run_android': (build_type_dir, sdk, device, interactive, purge)}},
	]

def run_ios_phase(device):
	return [
		{'when': {'platform_is': 'ios'}, 'do': {'run_ios': (device,)}},
	]

def run_firefox_phase(build_type_dir):
	return [
		{'when': {'platform_is': 'firefox'}, 'do': {'run_firefox': (build_type_dir,)}},
	]
	
def run_web_phase():
	return [
		{'when': {'platform_is': 'web'}, 'do': {'run_web': ()}},
	]

def run_wp_phase(device):
	return [
		{'when': {'platform_is': 'wp'}, 'do': {'run_wp': (device,)}},
	]

def run_chrome_phase():
	return [
		{'when': {'platform_is': 'chrome'}, 'do': {'run_chrome': ()}},
	]

def package(build_type_dir):
	return [
		{'when': {'platform_is': 'android'}, 'do': {'package_android': ()}},
		{'when': {'platform_is': 'ios'}, 'do': {'package_ios': ()}},
		{'when': {'platform_is': 'web'}, 'do': {'package_web': ()}},
		{'when': {'platform_is': 'wp'}, 'do': {'package_wp': ()}},
		{'when': {'platform_is': 'chrome'}, 'do': {'package_chrome': ()}},
	]

def make_installers():
	return [
		{'when': {'platform_is': 'ie'}, 'do': {'package_ie': ()}},
	]

def check_javascript():
	return [
		{'do': {'lint_javascript': ()}},
	]

def check_local_config_schema():
	return [
		{'do': {'check_local_config_schema': ()}},
	]

def migrate_config():
	return [
		{'do': {'migrate_config': ()}},
	]

def clean_phase():
	return [
		{'when': {'platform_is': 'android'}, 'do': {'clean_android': ()}},
		{'when': {'platform_is': 'firefox'}, 'do': {'clean_firefox': 'development'}},
		{'when': {'platform_is': 'web'}, 'do': {'clean_web': ()}},
		{'when': {'platform_is': 'wp'}, 'do': {'clean_wp': ()}},
	]
