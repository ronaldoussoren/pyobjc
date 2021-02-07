from PyObjCTools.TestSupport import TestCase

import UniformTypeIdentifiers


class TestUTAdditions(TestCase):
    def test_methods(self):
        UniformTypeIdentifiers.NSString.stringByAppendingPathComponent_conformingToType_
