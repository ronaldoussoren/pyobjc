import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestMath64(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("S64Max")
        self.assert_not_wrapped("S64Min")
        self.assert_not_wrapped("S64Add")
        self.assert_not_wrapped("S64Subtract")
        self.assert_not_wrapped("extern SInt64 ")
        self.assert_not_wrapped("S64Absolute")
        self.assert_not_wrapped("S64Multiply")
        self.assert_not_wrapped("S64Mod")
        self.assert_not_wrapped("S64Divide")
        self.assert_not_wrapped("S64Div")
        self.assert_not_wrapped("S64Set")
        self.assert_not_wrapped("S64SetU")
        self.assert_not_wrapped("S32Set")
        self.assert_not_wrapped("S64And")
        self.assert_not_wrapped("S64Or")
        self.assert_not_wrapped("S64Eor")
        self.assert_not_wrapped("S64Not")
        self.assert_not_wrapped("S64Compare")
        self.assert_not_wrapped("S64BitwiseAnd")
        self.assert_not_wrapped("S64BitwiseOr")
        self.assert_not_wrapped("S64BitwiseEor")
        self.assert_not_wrapped("S64BitwiseNot")
        self.assert_not_wrapped("S64ShiftRight")
        self.assert_not_wrapped("S64ShiftLeft")
        self.assert_not_wrapped("SInt64ToLongDouble")
        self.assert_not_wrapped("LongDoubleToSInt64")
        self.assert_not_wrapped("U64Max")
        self.assert_not_wrapped("U64Add")
        self.assert_not_wrapped("U64Subtract")
        self.assert_not_wrapped("U64Multiply")
        self.assert_not_wrapped("U64Mod")
        self.assert_not_wrapped("U64Divide")
        self.assert_not_wrapped("U64Div")
        self.assert_not_wrapped("U64Set")
        self.assert_not_wrapped("U64SetU")
        self.assert_not_wrapped("U32SetU")
        self.assert_not_wrapped("U64And")
        self.assert_not_wrapped("U64Or")
        self.assert_not_wrapped("U64Eor")
        self.assert_not_wrapped("U64Not")
        self.assert_not_wrapped("U64Compare")
        self.assert_not_wrapped("U64BitwiseAnd")
        self.assert_not_wrapped("U64BitwiseOr")
        self.assert_not_wrapped("U64BitwiseEor")
        self.assert_not_wrapped("U64BitwiseNot")
        self.assert_not_wrapped("U64ShiftRight")
        self.assert_not_wrapped("U64ShiftLeft")
        self.assert_not_wrapped("UInt64ToLongDouble")
        self.assert_not_wrapped("LongDoubleToUInt64")
        self.assert_not_wrapped("UInt64ToSInt64")
        self.assert_not_wrapped("SInt64ToUInt64")
        self.assert_not_wrapped("SInt64ToWide")
        self.assert_not_wrapped("WideToSInt64")
        self.assert_not_wrapped("UInt64ToUnsignedWide")
        self.assert_not_wrapped("UnsignedWideToUInt64")
        self.assert_not_wrapped("SInt64ToWide")
        self.assert_not_wrapped("WideToSInt64")
        self.assert_not_wrapped("UInt64ToUnsignedWide")
        self.assert_not_wrapped("UnsignedWideToUInt64")
        self.assert_not_wrapped("_SInt64ToWideLL")
        self.assert_not_wrapped("_WideToSInt64LL")
        self.assert_not_wrapped("_UInt64ToUnsignedWide")
        self.assert_not_wrapped("_UnsignedWideToUInt64")
        self.assert_not_wrapped("SInt64ToWide")
        self.assert_not_wrapped("WideToSInt64")
        self.assert_not_wrapped("UInt64ToUnsignedWide")
        self.assert_not_wrapped("UnsignedWideToUInt64")
        self.assert_not_wrapped("SInt64ToWide")
        self.assert_not_wrapped("WideToSInt64")
        self.assert_not_wrapped("UInt64ToUnsignedWide")
        self.assert_not_wrapped("UnsignedWideToUInt64")
