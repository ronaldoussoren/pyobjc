from PyObjCTools.pluginbuilder import buildplugin
from plistlib import Plist, Dict

infoPlist = Plist(
    CFBundleName='Shell Environment',
    #CFBundleIconFile='ShellEnv.icns',
    CFBundleGetInfoString='Shell Environment Panel',
    CFBundleVersion='0.1',
    CFBundleShortVersionString = '0.1',
    NSPrefPaneIconLabel='Shell Environment',
    NSPrefPaneIconFile='ShellEnv.icns',
)

buildplugin(
    name = "EnvironmentPane",
    mainmodule = "main.py",
    nibname = "EnvironmentPane",
    principalClass = "EnvironmentPane",
    resources = ["English.lproj", "ShellEnv.icns"],
    bundlesuffix = ".prefPane",
    plist = infoPlist,
)
