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
		{'when': {'platform_is': 'android'}, 'do': {'populate_icons': ("android", [36, 48, 72])}},
		{'when': {'platform_is': 'chrome'}, 'do': {'populate_icons': ("chrome", [16, 48, 128])}},
		{'when': {'platform_is': 'firefox'}, 'do': {'populate_icons': ("firefox", [32, 64])}},
		{'when': {'platform_is': 'ios'}, 'do': {'populate_icons': ("ios", [57, 72, 114, 144])}},
		{'when': {'platform_is': 'safari'}, 'do': {'populate_icons': ("safari", [32, 48, 64])}},
		{'when': {'platform_is': 'wp'}, 'do': {'populate_icons': ("wp", [62, 99, 173])}},

		{'when': {'platform_is': 'android', 'icon_available': ('android', '36')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["android"]["36"]}',
			'to': icon("android", 'drawable-ldpi/icon.png')
		}}},
		{'when': {'platform_is': 'android', 'icon_available': ('android', '48')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["android"]["48"]}',
			'to': icon("android", 'drawable-mdpi/icon.png')
		}}},
		{'when': {'platform_is': 'android', 'icon_available': ('android', '72')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["android"]["72"]}',
			'to': icon("android", "drawable-hdpi/icon.png")
		}}},
		
		{'when': {'platform_is': 'safari', 'icon_available': ('safari', '32')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["safari"]["32"]}',
			'to': icon("safari", 'icon-32.png')
		}}},
		{'when': {'platform_is': 'safari', 'icon_available': ('safari', '48')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["safari"]["48"]}',
			'to': icon("safari", 'icon-48.png')
		}}},
		{'when': {'platform_is': 'safari', 'icon_available': ('safari', '64')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["safari"]["64"]}',
			'to': icon("safari", 'icon-64.png')
		}}},
		
		{'when': {'platform_is': 'firefox', 'icon_available': ('firefox', '32')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["firefox"]["32"]}',
			'to': icon("firefox", 'icon.png')
		}}},
		{'when': {'platform_is': 'firefox', 'icon_available': ('firefox', '64')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["firefox"]["64"]}',
			'to': icon("firefox", 'icon64.png')
		}}},

		{'when': {'platform_is': 'ios', 'icon_available': ('ios', '57')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["ios"]["57"]}',
			'to': icon("ios", 'normal.png')
		}}},
		{'when': {'platform_is': 'ios', 'icon_available': ('ios', '72')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["ios"]["72"]}',
			'to': icon("ios", 'ipad.png')
		}}},
		{'when': {'platform_is': 'ios', 'icon_available': ('ios', '114')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["ios"]["114"]}',
			'to': icon("ios", 'retina.png')
		}}},
		{'when': {'platform_is': 'ios', 'icon_available': ('ios', '144')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["ios"]["144"]}',
			'to': icon("ios", 'ipad-retina.png')
		}}},

		{'when': {'platform_is': 'wp', 'icon_available': ('wp', '64')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["wp"]["62"]}',
			'to': icon("wp", 'ApplicationIcon.png')
		}}},
		{'when': {'platform_is': 'wp', 'icon_available': ('wp', '99')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["wp"]["99"]}',
			'to': icon("wp", 'Marketplace.png')
		}}},
		{'when': {'platform_is': 'wp', 'icon_available': ('wp', '173')}, 'do': {'copy_files': {
			'from': '${modules["icons"]["wp"]["173"]}',
			'to': icon("wp", 'Background.png')
		}}},

		{'when': {'platform_is': 'wp', 'have_wp_launch': ()}, 'do': {'copy_files': {
			'from': '${modules["launchimage"]["wp-landscape"]}',
			'to': icon("wp", "SplashScreenImage.jpg")
		}}},
		
		{'when': {'platform_is': 'ios', 'config_property_true': 'modules.icons.ios.prerendered'}, 'do': {
			'set_in_biplist': {
				"filename": 'development/ios/*/Info.plist',
				"key": "UIPrerenderedIcon",
				"value": True
			},
		}},
		{'when': {'platform_is': 'ios', 'config_property_true': 'modules.icons.ios.prerendered'}, 'do': {
			'set_in_biplist': {
				"filename": 'development/ios/*/Info.plist',
				"key": "CFBundleIcons.CFBundlePrimaryIcon.UIPrerenderedIcon",
				"value": True
			},
		}},
	]
