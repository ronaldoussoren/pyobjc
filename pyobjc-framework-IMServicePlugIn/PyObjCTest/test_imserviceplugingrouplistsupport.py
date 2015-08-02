from PyObjCTools.TestSupport import *
import IMServicePlugIn
import objc

class TestIMServicePlugInGroupListSupport (TestCase):
    def testProtocols(self):
        objc.protocolNamed('IMServicePlugInGroupListSupport')
        objc.protocolNamed('IMServicePlugInGroupListEditingSupport')
        objc.protocolNamed('IMServicePlugInGroupListOrderingSupport')
        objc.protocolNamed('IMServicePlugInGroupListAuthorizationSupport')
        objc.protocolNamed('IMServicePlugInGroupListHandlePictureSupport')
        objc.protocolNamed('IMServiceApplicationGroupListSupport')
        objc.protocolNamed('IMServiceApplicationGroupListAuthorizationSupport')

if __name__ == "__main__":
    main()
