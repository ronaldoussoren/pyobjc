import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSProxyHelper(Foundation.NSObject):
    def allowsWeakReference(self):
        return 0

    def retainWeakReference(self):
        return 0


class TestNSProxy(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSProxy.respondsToSelector_)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSProxyHelper.allowsWeakReference)
        self.assertResultIsBOOL(TestNSProxyHelper.retainWeakReference)
