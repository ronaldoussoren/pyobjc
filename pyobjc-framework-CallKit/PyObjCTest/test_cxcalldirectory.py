from PyObjCTools.TestSupport import TestCase
import CallKit
import sys


class TestCXCallDirectory(TestCase):
    def test_constants(self):
        self.assertEqual(CallKit.CXCallDirectoryPhoneNumberMax, sys.maxsize - 1)
