# TODO: Put this somewhere shared
locations = {
	'android': 'development/android/assets/src',
	'ios': 'development/ios/*/assets/src',
	'chrome': 'development/chrome/src',
	'firefox': 'development/firefox/resources/f/data/src',
	'safari': 'development/forge.safariextension/src',
	'ie': 'development/ie/src',
	'web': 'development/web/src',
	'wp': 'development/wp/assets/src',
}

def customer_phase(build):
	return [
		{'when': {'platform_is': 'firefox'}, 'do': {'wrap_activations': locations["firefox"]}},
		{'when': {'platform_is': 'safari'}, 'do': {'wrap_activations': locations["safari"]}},
	]