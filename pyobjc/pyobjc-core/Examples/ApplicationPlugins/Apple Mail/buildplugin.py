from PyObjCTools.pluginbuilder import buildplugin

buildplugin(
    name = "ToyMailBundle2",
    mainmodule = "main.py",
    nibname = "ToyMailBundle2",
    principalClass = "ToyMailBundle2",
    resources = [],
    bundlesuffix = ".mailbundle",
)
