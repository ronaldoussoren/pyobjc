import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSScriptCoercionHandler(TestCase):
    def test_methods(self):
        self.assertArgIsSEL(
            Foundation.NSScriptCoercionHandler.registerCoercer_selector_toConvertFromClass_toClass_,  # noqa: B950
            1,
            b"@@:@#",
        )
