import IMServicePlugIn
import objc
from PyObjCTools.TestSupport import *


class TestIMServicePlugInPresenceSupport(TestCase):
    def testProtocols(self):
        objc.protocolNamed("IMServicePlugInPresenceSupport")


if __name__ == "__main__":
    main()
