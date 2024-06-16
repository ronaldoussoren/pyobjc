from PyObjCTools.TestSupport import TestCase

import MediaExtension


class TestMEError(TestCase):
    def test_enum(self):
        self.assertIsEnumType(MediaExtension.MEError)
        self.assertEqual(MediaExtension.MEErrorUnsupportedFeature, -19320)
        self.assertEqual(MediaExtension.MEErrorAllocationFailure, -19321)
        self.assertEqual(MediaExtension.MEErrorInvalidParameter, -19322)
        self.assertEqual(MediaExtension.MEErrorParsingFailure, -19323)
        self.assertEqual(MediaExtension.MEErrorInternalFailure, -19324)
        self.assertEqual(MediaExtension.MEErrorPropertyNotSupported, -19325)
        self.assertEqual(MediaExtension.MEErrorNoSuchEdit, -19326)
        self.assertEqual(MediaExtension.MEErrorNoSamples, -19327)
        self.assertEqual(MediaExtension.MEErrorLocationNotAvailable, -19328)
        self.assertEqual(MediaExtension.MEErrorEndOfStream, -19329)
        self.assertEqual(MediaExtension.MEErrorPermissionDenied, -19330)
        self.assertEqual(MediaExtension.MEErrorReferenceMissing, -19331)
