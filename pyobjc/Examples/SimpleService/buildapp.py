from bundlebuilder import buildapp
from plistlib import Plist, Dict

plist = Plist(
    CFBundleIdentifier = u'net.sf.pyobjc.PyObjCSimpleService',
    LSBackgroundOnly = 1,
    NSServices = [
        Dict(
            NSKeyEquivalent = Dict(
                default = u'F',
            ),
            NSMenuItem = Dict(
                default = u'Open File',
            ),
            NSMessage = u'doOpenFileService',
            NSPortName = u'PyObjCSimpleService',
            NSSendTypes = [
                u'NSStringPboardType',
            ],
        ),
        Dict(
            NSMenuItem = Dict(
                default = u'Capitalize String',
            ),
            NSMessage = u'doCapitalizeService',
            NSPortName = u'PyObjCSimpleService',
            NSReturnTypes = [
                u'NSStringPboardType',
            ],
            NSSendTypes = [
                u'NSStringPboardType',
            ],
        ),
    ],
)


buildapp(
	mainprogram = "SimpleService_main.py",
    name = 'PyObjCSimpleService',
    resources = ['ServiceTest.py'],
    plist = plist,
)
