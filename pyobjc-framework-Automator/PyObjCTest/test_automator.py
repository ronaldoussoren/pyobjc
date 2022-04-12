import Automator
import objc
from PyObjCTools.TestSupport import TestCase


class TestAutomator(TestCase):
    def testClasses(self):
        self.assertHasAttr(Automator, "AMAction")
        self.assertIsInstance(Automator.AMAction, objc.objc_class)

        self.assertHasAttr(Automator, "AMAppleScriptAction")
        self.assertIsInstance(Automator.AMAppleScriptAction, objc.objc_class)

    def testInformalProtocols(self):
        self.assertNotHasAttr(Automator, "protocols")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(
            Automator,
            exclude_attrs={
                (
                    "NSObject",
                    "copyRenderedTextureForCGLContext_pixelFormat_bounds_isFlipped_",
                )
            },
        )
