from PyObjCTools.TestSupport import TestCase, min_os_level
import NaturalLanguage


class TestNLEmbedding(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NaturalLanguage.NLDistanceType)

    def test_constants(self):
        self.assertEqual(NaturalLanguage.NLDistanceTypeCosine, 0)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(NaturalLanguage.NLEmbedding.containsString_)

        self.assertArgIsBlock(
            NaturalLanguage.NLEmbedding.enumerateNeighborsForString_maximumCount_distanceType_usingBlock_,
            3,
            b"v@do^Z",
        )
        self.assertArgIsBlock(
            NaturalLanguage.NLEmbedding.enumerateNeighborsForString_maximumCount_maximumDistance_distanceType_usingBlock_,
            4,
            b"v@do^Z",
        )

        self.assertResultIsBOOL(NaturalLanguage.NLEmbedding.getVector_forString_)
        self.assertArgIsOut(NaturalLanguage.NLEmbedding.getVector_forString_, 0)
        self.assertArgIsVariableSize(
            NaturalLanguage.NLEmbedding.getVector_forString_, 0
        )

        self.assertArgIsBlock(
            NaturalLanguage.NLEmbedding.enumerateNeighborsForVector_maximumCount_distanceType_usingBlock_,
            3,
            b"v@do^Z",
        )
        self.assertArgIsBlock(
            NaturalLanguage.NLEmbedding.enumerateNeighborsForVector_maximumCount_maximumDistance_distanceType_usingBlock_,
            4,
            b"v@do^Z",
        )

        self.assertResultIsBOOL(
            NaturalLanguage.NLEmbedding.writeEmbeddingForDictionary_language_revision_toURL_error_
        )
        self.assertArgIsOut(
            NaturalLanguage.NLEmbedding.writeEmbeddingForDictionary_language_revision_toURL_error_,
            4,
        )
