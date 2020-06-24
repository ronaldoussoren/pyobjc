from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import ModelIO  # noqa: F401


class TestMDLAnimation(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("MDLJointAnimation")
