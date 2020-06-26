from PyObjCTools.TestSupport import TestCase

import ClassKit


class TestCLSDeeplinks(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ClassKit.NSUserActivity.isClassKitDeepLink)
