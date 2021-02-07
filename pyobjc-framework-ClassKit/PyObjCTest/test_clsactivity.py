from PyObjCTools.TestSupport import TestCase

import ClassKit


class TestCLSActivity(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ClassKit.CLSActivity.isStarted)
