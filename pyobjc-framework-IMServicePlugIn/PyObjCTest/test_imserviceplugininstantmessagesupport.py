import IMServicePlugIn
import objc
from PyObjCTools.TestSupport import *


class TestIMServicePlugInInstantMessageSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInInstantMessagingSupport")
        objc.protocolNamed("IMServiceApplicationInstantMessagingSupport")


if __name__ == "__main__":
    main()
