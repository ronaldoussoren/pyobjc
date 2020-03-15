import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSClassDescription(TestCase):
    def testConstants(self):
        self.assertIsInstance(
            Foundation.NSClassDescriptionNeededForClassNotification, str
        )
