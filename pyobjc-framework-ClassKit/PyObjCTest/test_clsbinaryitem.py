from PyObjCTools.TestSupport import TestCase

import ClassKit


class TestCLSBinaryItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ClassKit.CLSBinaryValueType)

    def test_constants(self):
        self.assertEqual(ClassKit.CLSBinaryValueTypeTrueFalse, 0)
        self.assertEqual(ClassKit.CLSBinaryValueTypePassFail, 1)
        self.assertEqual(ClassKit.CLSBinaryValueTypeYesNo, 2)
        self.assertEqual(ClassKit.CLSBinaryValueTypeCorrectIncorrect, 3)

    def test_methods(self):
        self.assertResultIsBOOL(ClassKit.CLSBinaryItem.value)
        self.assertArgIsBOOL(ClassKit.CLSBinaryItem.setValue_, 0)
