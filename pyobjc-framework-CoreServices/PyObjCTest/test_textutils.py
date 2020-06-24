import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestTextUtils(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("ScriptRunStatus")
        self.assert_not_wrapped("BreakTable")
        self.assert_not_wrapped("NBreakTable")
        self.assert_not_wrapped("Munger")
        self.assert_not_wrapped("NewString")
        self.assert_not_wrapped("SetString")
        self.assert_not_wrapped("GetString")
        self.assert_not_wrapped("GetIndString")
        self.assert_not_wrapped("FindWordBreaks")
        self.assert_not_wrapped("LowercaseText")
        self.assert_not_wrapped("UppercaseText")
        self.assert_not_wrapped("StripDiacritics")
        self.assert_not_wrapped("UppercaseStripDiacritics")
        self.assert_not_wrapped("FindScriptRun")
        self.assert_not_wrapped("UpperString")
        self.assert_not_wrapped("upperstring")
        self.assert_not_wrapped("UprString")
        self.assert_not_wrapped("c2pstrcpy")
        self.assert_not_wrapped("p2cstrcpy")
        self.assert_not_wrapped("CopyPascalStringToC")
        self.assert_not_wrapped("CopyCStringToPascal")
        self.assert_not_wrapped("c2pstr")
        self.assert_not_wrapped("C2PStr")
        self.assert_not_wrapped("p2cst")
        self.assert_not_wrapped("P2CStr")
        self.assert_not_wrapped("p2cstr")
        self.assert_not_wrapped("c2pstr")
        self.assert_not_wrapped("C2PStr")
        self.assert_not_wrapped("P2CStr")
