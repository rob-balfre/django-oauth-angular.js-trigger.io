def create_all_js(build):
	return [
		{'when': {'module_enabled': 'reload'}, 'do': {'add_to_all_js': 'common-v2/modules/reload/default.js'}},
		{'when': {'module_disabled': 'reload'}, 'do': {'add_to_all_js': 'common-v2/modules/reload/disabled.js'}},
	]
	
def platform_specific_templating(build):
	return [
		{'when': {'platform_is': 'android', 'module_enabled': 'reload'}, 'do': {'add_element_to_xml': {
			"file": 'android/ForgeTemplate/res/values/strings.xml',
			"tag": "item",
			"text": "io.trigger.forge.android.modules.reload",
			"to": "string-array/[@name='modules']"
		}}},
		{'when': {'platform_is': 'ios', 'module_enabled': 'reload'}, 'do': {'add_to_json_array': {
			"filename": 'ios/ForgeTemplate/ForgeTemplate/app_config.json',
			"key": "modules",
			"value": "reload"
		}}},
		{'when': {'platform_is': 'wp', 'module_enabled': 'reload'}, 'do': {'add_to_json_array': {
			"filename": 'wp/Properties/manifest.json',
			"key": "modules",
			"value": "reload"
		}}},
	]

def customer_phase(build):
	return [
		{'when': {'platform_is': 'android'}, 'do': {'generate_sha1_manifest': {
			"input_folder": "development/android/assets/src",
			"output_file": "development/android/assets/hash_to_file.json"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'generate_sha1_manifest': {
			"input_folder": "development/ios/device-ios.app/assets/src",
			"output_file": "development/ios/device-ios.app/assets/hash_to_file.json"
		}}},
		{'when': {'platform_is': 'ios'}, 'do': {'generate_sha1_manifest': {
			"input_folder": "development/ios/simulator-ios.app/assets/src",
			"output_file": "development/ios/simulator-ios.app/assets/hash_to_file.json"
		}}},
	]