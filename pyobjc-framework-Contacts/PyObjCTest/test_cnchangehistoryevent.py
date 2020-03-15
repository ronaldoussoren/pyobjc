import sys

import objc

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import TestCase, min_os_level
    import Contacts  # noqa: F401

    class TestCNChangeHistoryEvent(TestCase):
        @min_os_level("10.15")
        def testProtocols(self):
            objc.protocolNamed("CNChangeHistoryEventVisitor")
