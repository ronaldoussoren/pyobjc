import Foundation  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestNSURLAuthenticationChallenge(TestCase):
    def testProtocols(self):
        objc.protocolNamed("NSURLAuthenticationChallengeSender")
