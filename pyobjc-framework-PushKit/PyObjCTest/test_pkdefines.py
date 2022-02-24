from PyObjCTools.TestSupport import TestCase

import PushKit


class TestPKDefines(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(PushKit.PKPushType, str)
