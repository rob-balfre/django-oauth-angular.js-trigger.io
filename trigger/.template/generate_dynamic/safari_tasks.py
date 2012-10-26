def _generate_package_name(build):
	if "package_names" not in build.config["modules"]:
		build.config["modules"]["package_names"] = {}
	if "safari" not in build.config["modules"]["package_names"]:
		build.config["modules"]["package_names"]["safari"] = "forge.safari.{package_name}".format(package_name=build.config["package_name"])
	return build.config["modules"]["package_names"]["safari"]
