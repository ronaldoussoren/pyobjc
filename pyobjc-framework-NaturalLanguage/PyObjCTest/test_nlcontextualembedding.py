from PyObjCTools.TestSupport import TestCase, min_os_level
import NaturalLanguage


class TestNLContextualEmbedding(TestCase):
    @min_os_level("14.0")
    def test_constants(self):
        self.assertIsTypedEnum(NaturalLanguage.NLContextualEmbeddingKey, str)

        self.assertIsInstance(NaturalLanguage.NLContextualEmbeddingKeyLanguages, str)
        self.assertIsInstance(NaturalLanguage.NLContextualEmbeddingKeyScripts, str)
        self.assertIsInstance(NaturalLanguage.NLContextualEmbeddingKeyRevision, str)

        self.assertIsEnumType(NaturalLanguage.NLContextualEmbeddingAssetsResult)
        self.assertEqual(NaturalLanguage.NLContextualEmbeddingAssetsResultAvailable, 0)
        self.assertEqual(
            NaturalLanguage.NLContextualEmbeddingAssetsResultNotAvailable, 1
        )
        self.assertEqual(NaturalLanguage.NLContextualEmbeddingAssetsResultError, 2)

    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(NaturalLanguage.NLContextualEmbedding.loadWithError_)
        self.assertArgIsOut(NaturalLanguage.NLContextualEmbedding.loadWithError_, 0)

        self.assertArgIsOut(
            NaturalLanguage.NLContextualEmbedding.embeddingResultForString_language_error_,
            2,
        )

        self.assertResultIsBOOL(
            NaturalLanguage.NLContextualEmbedding.hasAvailableAssets
        )

        self.assertArgIsBlock(
            NaturalLanguage.NLContextualEmbeddingResult.enumerateTokenVectorsInRange_usingBlock_,
            1,
            b"v@" + NaturalLanguage.NSRange.__typestr__ + b"o^Z",
        )
