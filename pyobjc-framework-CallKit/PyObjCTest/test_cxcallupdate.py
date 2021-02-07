from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXCallUpdate(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXCallUpdate.supportsHolding)
        self.assertArgIsBOOL(CallKit.CXCallUpdate.setSupportsHolding_, 0)
        self.assertResultIsBOOL(CallKit.CXCallUpdate.supportsGrouping)
        self.assertArgIsBOOL(CallKit.CXCallUpdate.setSupportsGrouping_, 0)
        self.assertResultIsBOOL(CallKit.CXCallUpdate.supportsUngrouping)
        self.assertArgIsBOOL(CallKit.CXCallUpdate.setSupportsUngrouping_, 0)
        self.assertResultIsBOOL(CallKit.CXCallUpdate.supportsDTMF)
        self.assertArgIsBOOL(CallKit.CXCallUpdate.setSupportsDTMF_, 0)
        self.assertResultIsBOOL(CallKit.CXCallUpdate.hasVideo)
        self.assertArgIsBOOL(CallKit.CXCallUpdate.setHasVideo_, 0)
