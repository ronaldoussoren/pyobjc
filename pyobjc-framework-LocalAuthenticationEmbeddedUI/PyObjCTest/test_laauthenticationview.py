from PyObjCTools.TestSupport import TestCase
import LocalAuthenticationEmbeddedUI


class TestLAAuthenticationView(TestCase):
    def test_classes(self):
        LocalAuthenticationEmbeddedUI.LAAuthenticationView

    def test_methods(self):
        # XXX: unavailable: initWithFrame_, initWithCoder_
        pass
