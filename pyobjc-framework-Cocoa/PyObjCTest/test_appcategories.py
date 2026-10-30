import Cocoa
import PyObjCTools.AppCategories  # noqa: F401
from PyObjCTools.TestSupport import TestCase, skipUnless


class TestAppKitCategories(TestCase):
    # Note: These tests don't actually test anything beyond asserting that
    # the code doesn't crash...

    def test_saved_graphics_state(self):
        with Cocoa.NSGraphicsContext.savedGraphicsState():
            pass

    @skipUnless(
        hasattr(Cocoa, "NSAnimationContext"), "Test for NSAnimationContext category"
    )
    def test_animation_context(self):
        with Cocoa.NSAnimationContext:
            pass
