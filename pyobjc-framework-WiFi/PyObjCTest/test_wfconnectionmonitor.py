import sys
from PyObjCTest import *

if sys.maxsize > 2 ** 32:
    import WiFi

    class TestWFConnectionMonitor (TestCase):
        @min_os_level('10.15')
        def test_methods(self):
            self.assertResultIsBlock(WiFi.WFConnectionMonitor.invalidationHandler, b'v')
            self.assertArgIsBlock(WiFi.WFConnectionMonitor.setInvalidationHandler_, 0, b'v')

            self.assertResultIsBlock(WiFi.WFConnectionMonitor.connectionStatusHandler, b'v@')
            self.assertArgIsBlock(WiFi.WFConnectionMonitor.setConnectionStatusHandler_, 0, b'v@')
