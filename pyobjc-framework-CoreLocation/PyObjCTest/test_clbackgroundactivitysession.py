import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLBackgroundActivitySession(TestCase):
    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.authorizationDenied
        )
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.authorizationDeniedGlobally
        )
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.authorizationRestricted
        )
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.insufficientlyInUse
        )
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.serviceSessionRequired
        )
        self.assertResultIsBOOL(
            CoreLocation.CLBackgroundActivitySessionDiagnostic.authorizationRequestInProgress
        )

        self.assertArgIsBlock(
            CoreLocation.CLBackgroundActivitySession.backgroundActivitySessionWithQueue_handler_,
            1,
            b"v@",
        )
