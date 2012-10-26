from os import path

_icon_path_for_customer = {
	"android": "development/android/res/",
	"safari": "development/forge.safariextension/",
	"firefox": "development/firefox/",
	"ios": "development/ios/*.app/",
	"wp": "development/wp/dist/"
}

def customer_phase(build):
	icon_path = _icon_path_for_customer
	def icon(platform, sub_path):
		return path.join(icon_path[platform], sub_path)

	return [
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["iphone"]}',
			'to': icon("ios", "Default~iphone.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["iphone-retina"]}',
			'to': icon("ios", "Default@2x~iphone.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["iphone-retina4"]}',
			'to': icon("ios", "Default-568h@2x~iphone.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["ipad"]}',
			'to': icon("ios", "Default-Portrait~ipad.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["ipad-landscape"]}',
			'to': icon("ios", "Default-Landscape~ipad.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["ipad-retina"]}',
			'to': icon("ios", "Default-Portrait@2x~ipad.png")
		}}},
		{'when': {'platform_is': 'ios', 'have_ios_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["ipad-landscape-retina"]}',
			'to': icon("ios", "Default-Landscape@2x~ipad.png")
		}}},
	]
		
def platform_specific_templating(build):
	return [
		{'when': {'platform_is': 'android', 'have_android_launch': ()}, 'do': {'find_and_replace': {
			"in": ('android/ForgeTemplate/res/values/strings.xml',),
			"find": "SPLASH_IMAGE_HERE",
			"replace": "${modules.launchimage.android}"
		}}},
		{'when': {'platform_is': 'android', 'have_android_launch': ()}, 'do': {'find_and_replace': {
			"in": ('android/ForgeTemplate/res/values/strings.xml',),
			"find": "SPLASH_IMAGE_LANDSCAPE_HERE",
			"replace": "${modules.launchimage['android-landscape']}"
		}}},
	]