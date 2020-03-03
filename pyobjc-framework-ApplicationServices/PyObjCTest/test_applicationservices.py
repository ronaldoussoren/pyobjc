import ApplicationServices
from PyObjCTools.TestSupport import TestCase


class TestApplicationServices(TestCase):
    def testTrivial(self):
        ApplicationServices.kAXErrorSuccess
