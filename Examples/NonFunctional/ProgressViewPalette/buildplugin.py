from PyObjCTools.pluginbuilder import buildplugin
from plistlib import Plist, Dict

infoPlist = Plist(
    CFBundleName='ProgressViewPalette',
    CFBundleExecutable='ProgressViewPalette',
    CFBundleIdentifier="net.sf.pyobjc.ProgressViewPalette",
    #CFBundleIconFile='ShellEnv.icns',
    CFBundleGetInfoString='Shell Environment Panel',
    CFBundleVersion='0.1',
    CFBundleShortVersionString = '0.1',
)

buildplugin(
    name = "ProgressViewPalette",
    mainmodule = "ProgressViewPalette.py",
    nibname = "ProgressViewPalette",
    principalClass = "ProgressViewPalette",
    resources = [ 'English.lproj', 'ProgressCell.py',
            'ProgressView.py', 'ProgressViewInspector.py',
            'ProgressViewPalette.py', 'palette.table', ],
    bundlesuffix = ".palette",
    plist = infoPlist,
)
