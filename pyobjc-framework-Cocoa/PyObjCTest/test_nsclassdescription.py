import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSClassDescription(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            Foundation.NSClassDescriptionNeededForClassNotification, str
        )
