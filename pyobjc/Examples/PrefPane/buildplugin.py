from PyObjCTools.pluginbuilder import buildplugin

buildplugin(
    name = "SimplePreferencePane",
    mainmodule = "main.py",
    nibname = "SimplePreferencePane",
    principalClass = "SimplePreferencePane",
    resources = ["SimplePreferencePane.nib"],
    bundlesuffix = ".prefPane",
)
