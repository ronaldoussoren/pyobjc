import HIServices
from PyObjCTools.TestSupport import TestCase


class TestTranslationServices(TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.badTranslationRefErr, -3031)

        self.assertEqual(HIServices.kTranslationDataTranslation, 1 << 0)
        self.assertEqual(HIServices.kTranslationFileTranslation, 1 << 1)

    def testFunctions(self):
        self.assertIsInstance(HIServices.TranslationGetTypeID(), int)

        self.assertArgIsOut(HIServices.TranslationCreate, 3)
        self.assertArgIsCFRetained(HIServices.TranslationCreate, 3)

        self.assertArgIsOut(HIServices.TranslationCreateWithSourceArray, 2)
        self.assertArgIsCFRetained(HIServices.TranslationCreateWithSourceArray, 2)
        self.assertArgIsOut(HIServices.TranslationCreateWithSourceArray, 3)
        self.assertArgIsCFRetained(HIServices.TranslationCreateWithSourceArray, 3)

        self.assertArgIsOut(HIServices.TranslationPerformForData, 2)
        self.assertArgIsCFRetained(HIServices.TranslationPerformForData, 2)

        self.assertArgIsIn(HIServices.TranslationPerformForFile, 1)
        self.assertArgIsIn(HIServices.TranslationPerformForFile, 2)
        self.assertArgIsOut(HIServices.TranslationPerformForFile, 4)

        self.assertArgIsOut(HIServices.TranslationPerformForURL, 3)
        self.assertArgIsCFRetained(HIServices.TranslationPerformForURL, 3)

        self.assertArgIsOut(HIServices.TranslationCopySourceType, 1)
        self.assertArgIsCFRetained(HIServices.TranslationCopySourceType, 1)

        self.assertArgIsOut(HIServices.TranslationCopyDestinationType, 1)
        self.assertArgIsCFRetained(HIServices.TranslationCopyDestinationType, 1)

        self.assertArgIsOut(HIServices.TranslationGetTranslationFlags, 1)
