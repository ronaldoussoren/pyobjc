from PyObjCTools.TestSupport import TestCase

import UniformTypeIdentifiers


class TestUTTagClass(TestCase):
    def test_constants(self):
        self.assertIsInstance(UniformTypeIdentifiers.UTTagClassFilenameExtension, str)
        self.assertIsInstance(UniformTypeIdentifiers.UTTagClassMIMEType, str)
