from PyObjCTools.pluginbuilder import buildplugin

buildplugin(
    name = "SillyBalls",
    mainmodule = "SillyBalls.py",
    nibname = "SillyBalls",
    principalClass = "SillyBalls",
    resources = ["English.lproj"],
    bundlesuffix = ".saver",
)
