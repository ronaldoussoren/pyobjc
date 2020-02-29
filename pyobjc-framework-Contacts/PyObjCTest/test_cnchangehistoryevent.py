import sys

import objc
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Contacts

    class TestCNChangeHistoryEvent(TestCase):
        @min_os_level("10.15")
        def testProtocols(self):
            objc.protocolNamed("CNChangeHistoryEventVisitor")


if __name__ == "__main__":
    main()
