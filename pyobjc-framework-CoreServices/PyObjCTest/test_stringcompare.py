import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestStringCompoare(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("systemCurLang")
        self.assert_not_wrapped("systemDefLang")
        self.assert_not_wrapped("currentCurLang")
        self.assert_not_wrapped("currentDefLang")
        self.assert_not_wrapped("scriptCurLang")
        self.assert_not_wrapped("scriptDefLang")
        self.assert_not_wrapped("iuSystemCurLang")
        self.assert_not_wrapped("iuSystemDefLang")
        self.assert_not_wrapped("iuCurrentCurLang")
        self.assert_not_wrapped("iuCurrentDefLang")
        self.assert_not_wrapped("iuScriptCurLang")
        self.assert_not_wrapped("iuScriptDefLang")
        self.assert_not_wrapped("ReplaceText")
        self.assert_not_wrapped("MacReplaceText")
        self.assert_not_wrapped("ScriptOrder")
        self.assert_not_wrapped("CompareString")
        self.assert_not_wrapped("MacCompareString")
        self.assert_not_wrapped("IdenticalString")
        self.assert_not_wrapped("StringOrder")
        self.assert_not_wrapped("CompareText")
        self.assert_not_wrapped("IdenticalText")
        self.assert_not_wrapped("TextOrder")
        self.assert_not_wrapped("LanguageOrder")
        self.assert_not_wrapped("CompareString")
        self.assert_not_wrapped("CompareText")
        self.assert_not_wrapped("IdenticalString")
        self.assert_not_wrapped("IdenticalText")
        self.assert_not_wrapped("StringOrder")
        self.assert_not_wrapped("TextOrder")
        self.assert_not_wrapped("LanguageOrder")
        self.assert_not_wrapped("RelString")
        self.assert_not_wrapped("EqualString")
        self.assert_not_wrapped("relstring")
