from lib import predicate

@predicate
def is_external(build):
	return bool(build.external)

@predicate
def do_package(build):
	return getattr(build, "package", False)

@predicate
def icon_available(build, platform, size):
	return "icons" in build.config["modules"] and \
		(size in build.config["modules"]["icons"] or \
		size in build.config["modules"]["icons"].get(platform, {}))

@predicate
def have_ios_launch(build):
	return "launchimage" in build.config["modules"] and \
		"iphone" in build.config["modules"]["launchimage"] and \
		"iphone-retina" in build.config["modules"]["launchimage"] and \
		"ipad" in build.config["modules"]["launchimage"] and \
		"ipad-landscape" in build.config["modules"]["launchimage"] and \
		"ipad-retina" in build.config["modules"]["launchimage"] and \
		"ipad-landscape-retina" in build.config["modules"]["launchimage"]

@predicate
def have_android_launch(build):
	return "launchimage" in build.config["modules"] and \
		"android" in build.config["modules"]["launchimage"] and \
		"android-landscape" in build.config["modules"]["launchimage"]

@predicate
def have_wp_launch(build):
	return "launchimage" in build.config["modules"] and \
		"wp" in build.config["modules"]["launchimage"] and \
		"wp-landscape" in build.config["modules"]["launchimage"]

@predicate
def module_enabled(build, module):
	return module in build.config["modules"]
	
@predicate
def module_disabled(build, module):
	return not module_enabled(build, module)
	
@predicate
def partner_enabled(build, partner):
	return "partners" in build.config and \
		partner in build.config["partners"]

@predicate
def partner_disabled(build, partner):
	return not partner_enabled(build, partner)
	
@predicate
def orientation_disabled(build, device, orientation):
	if module_disabled(build, 'display'):
		return False
	
	if not "orientations" in build.config["modules"]['display']:
		return False
	
	if device in build.config["modules"]['display']['orientations']:
		return not build.config["modules"]['display']['orientations'][device] == orientation and not build.config["modules"]['display']['orientations'][device] == 'any'
	elif 'default' in build.config["modules"]['display']['orientations']:
		return not build.config["modules"]['display']['orientations']['default'] == orientation and not build.config["modules"]['display']['orientations']['default'] == 'any'
	else:
		return False

@predicate
def config_property_exists(build, property):
	properties = property.split('.')
	at = build.config
	for x in properties:
		if x in at:
			at = at[x]
		else:
			return False
	return True
@predicate
def config_property_does_not_exist(build, property):
	return not config_property_exists(build, property)

@predicate
def config_property_true(build, property):
	properties = property.split('.')
	at = build.config
	for x in properties:
		if x in at:
			at = at[x]
		else:
			return False
	return at == True

@predicate
def config_property_equals(build, property, value):
	properties = property.split('.')
	at = build.config
	for x in properties:
		if x in at:
			at = at[x]
		else:
			return False
	return at == value
	
@predicate
def platform_is(build, platform):
	return platform == 'all' or (set(platform.split(',')) & set(build.enabled_platforms))

@predicate
def module_reload_enabled(build):
	return "reload" in build.config["modules"]

@predicate
def module_reload_disabled(build):
	return not module_reload_enabled(build)
