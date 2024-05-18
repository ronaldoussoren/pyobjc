import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level

CMTagCollectionTagFilterFunction = b"Z" + CoreMedia.CMTag.__typestr__ + b"^v"
CMTagCollectionApplierFunction = b"v" + CoreMedia.CMTag.__typestr__ + b"^v"


class TestCMTagCollection(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreMedia.CMTagCollectionError)
        self.assertEqual(CoreMedia.kCMTagCollectionError_ParamErr, -15740)
        self.assertEqual(CoreMedia.kCMTagCollectionError_AllocationFailed, -15741)
        self.assertEqual(CoreMedia.kCMTagCollectionError_InternalError, -15742)
        self.assertEqual(CoreMedia.kCMTagCollectionError_InvalidTag, -15743)
        self.assertEqual(
            CoreMedia.kCMTagCollectionError_InvalidTagCollectionDictionary, -15744
        )
        self.assertEqual(
            CoreMedia.kCMTagCollectionError_InvalidTagCollectionData, -15745
        )
        self.assertEqual(CoreMedia.kCMTagCollectionError_TagNotFound, -15746)
        self.assertEqual(
            CoreMedia.kCMTagCollectionError_InvalidTagCollectionDataVersion, -15747
        )
        self.assertEqual(CoreMedia.kCMTagCollectionError_ExhaustedBufferSize, -15748)
        self.assertEqual(CoreMedia.kCMTagCollectionError_NotYetImplemented, -15749)

    @min_os_level("14.0")
    def test_consetants14_0(self):
        self.assertIsInstance(CoreMedia.kCMTagCollectionTagsArrayKey, str)

    @min_os_level("14.0")
    def test_types(self):
        self.assertIsCFType(CoreMedia.CMTagCollectionRef)
        self.assertIsCFType(CoreMedia.CMMutableTagCollectionRef)

    @min_os_level("14.0")
    def test_functions(self):
        CoreMedia.CMTagCollectionGetTypeID

        self.assertArgIsIn(CoreMedia.CMTagCollectionCreate, 1)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionCreate, 1, 2)
        self.assertArgIsOut(CoreMedia.CMTagCollectionCreate, 3)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreate, 3)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateMutable, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateMutable, 2)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateCopy, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateCopy, 2)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateMutableCopy, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateMutableCopy, 2)

        self.assertResultIsCFRetained(CoreMedia.CMTagCollectionCopyDescription)

        self.assertResultIsBOOL(CoreMedia.CMTagCollectionContainsTagsOfCollection)

        self.assertResultIsBOOL(CoreMedia.CMTagCollectionContainsSpecifiedTags)
        self.assertArgIsIn(CoreMedia.CMTagCollectionContainsSpecifiedTags, 1)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionContainsSpecifiedTags, 1, 2)

        self.assertResultIsBOOL(CoreMedia.CMTagCollectionContainsCategory)

        CoreMedia.CMTagCollectionGetCountOfCategory

        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTags, 1)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionGetTags, 1, (2, 3))
        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTags, 3)

        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTagsWithCategory, 2)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionGetTagsWithCategory, 2, (3, 4))
        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTagsWithCategory, 4)

        self.assertArgIsFunction(
            CoreMedia.CMTagCollectionCountTagsWithFilterFunction,
            1,
            CMTagCollectionTagFilterFunction,
            False,
        )

        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTagsWithFilterFunction, 1)
        self.assertArgSizeInArg(
            CoreMedia.CMTagCollectionGetTagsWithFilterFunction, 1, (2, 3)
        )
        self.assertArgIsOut(CoreMedia.CMTagCollectionGetTagsWithFilterFunction, 3)
        self.assertArgIsFunction(
            CoreMedia.CMTagCollectionGetTagsWithFilterFunction,
            4,
            CMTagCollectionTagFilterFunction,
            False,
        )

        self.assertArgIsIn(CoreMedia.CMTagCollectionCopyTagsOfCategories, 2)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionCopyTagsOfCategories, 2, 3)
        self.assertArgIsOut(CoreMedia.CMTagCollectionCopyTagsOfCategories, 4)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCopyTagsOfCategories, 4)

        self.assertArgIsFunction(
            CoreMedia.CMTagCollectionApply, 1, CMTagCollectionApplierFunction, False
        )

        self.assertArgIsFunction(
            CoreMedia.CMTagCollectionApplyUntil,
            1,
            CMTagCollectionTagFilterFunction,
            False,
        )

        self.assertResultIsBOOL(CoreMedia.CMTagCollectionIsEmpty)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateIntersection, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateIntersection, 2)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateUnion, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateUnion, 2)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateDifference, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateDifference, 2)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateExclusiveOr, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateExclusiveOr, 2)

        CoreMedia.CMTagCollectionAddTag

        CoreMedia.CMTagCollectionRemoveTag

        CoreMedia.CMTagCollectionRemoveAllTags

        CoreMedia.CMTagCollectionRemoveAllTagsOfCategory

        CoreMedia.CMTagCollectionAddTagsFromCollection

        self.assertArgIsIn(CoreMedia.CMTagCollectionAddTagsFromArray, 1)
        self.assertArgSizeInArg(CoreMedia.CMTagCollectionAddTagsFromArray, 1, 2)

        self.assertResultIsCFRetained(CoreMedia.CMTagCollectionCopyAsDictionary)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateFromDictionary, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateFromDictionary, 2)

        self.assertResultIsCFRetained(CoreMedia.CMTagCollectionCopyAsData)

        self.assertArgIsOut(CoreMedia.CMTagCollectionCreateFromData, 2)
        self.assertArgIsCFRetained(CoreMedia.CMTagCollectionCreateFromData, 2)
