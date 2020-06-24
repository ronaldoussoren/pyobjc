import sys
from PyObjCTools.TestSupport import TestCase
import Photos


class TestPhotosTypes(TestCase):
    def test_constants(self):

        self.assertEqual(Photos.PHAssetMediaTypeUnknown, 0)
        self.assertEqual(Photos.PHAssetMediaTypeImage, 1)
        self.assertEqual(Photos.PHAssetMediaTypeVideo, 2)
        self.assertEqual(Photos.PHAssetMediaTypeAudio, 3)

        self.assertEqual(Photos.PHAssetMediaSubtypeNone, 0)

        self.assertEqual(Photos.PHAssetMediaSubtypePhotoPanorama, (1 << 0))
        self.assertEqual(Photos.PHAssetMediaSubtypePhotoHDR, (1 << 1))
        self.assertEqual(Photos.PHAssetMediaSubtypePhotoScreenshot, (1 << 2))
        self.assertEqual(Photos.PHAssetMediaSubtypePhotoLive, (1 << 3))
        self.assertEqual(Photos.PHAssetMediaSubtypePhotoDepthEffect, (1 << 4))

        self.assertEqual(Photos.PHAssetMediaSubtypeVideoStreamed, (1 << 16))
        self.assertEqual(Photos.PHAssetMediaSubtypeVideoHighFrameRate, (1 << 17))
        self.assertEqual(Photos.PHAssetMediaSubtypeVideoTimelapse, (1 << 18))

        self.assertEqual(Photos.PHImageContentModeAspectFit, 0)
        self.assertEqual(Photos.PHImageContentModeAspectFill, 1)
        self.assertEqual(Photos.PHImageContentModeDefault, 0)

        self.assertEqual(Photos.PHCollectionListTypeMomentList, 1)
        self.assertEqual(Photos.PHCollectionListTypeFolder, 2)
        self.assertEqual(Photos.PHCollectionListTypeSmartFolder, 3)

        self.assertEqual(Photos.PHCollectionListSubtypeMomentListCluster, 1)
        self.assertEqual(Photos.PHCollectionListSubtypeMomentListYear, 2)
        self.assertEqual(Photos.PHCollectionListSubtypeRegularFolder, 100)
        self.assertEqual(Photos.PHCollectionListSubtypeSmartFolderEvents, 200)
        self.assertEqual(Photos.PHCollectionListSubtypeSmartFolderFaces, 201)

        self.assertEqual(Photos.PHCollectionEditOperationDeleteContent, 1)
        self.assertEqual(Photos.PHCollectionEditOperationRemoveContent, 2)
        self.assertEqual(Photos.PHCollectionEditOperationAddContent, 3)
        self.assertEqual(Photos.PHCollectionEditOperationCreateContent, 4)
        self.assertEqual(Photos.PHCollectionEditOperationRearrangeContent, 5)
        self.assertEqual(Photos.PHCollectionEditOperationDelete, 6)
        self.assertEqual(Photos.PHCollectionEditOperationRename, 7)

        self.assertEqual(Photos.PHAssetCollectionTypeAlbum, 1)
        self.assertEqual(Photos.PHAssetCollectionTypeSmartAlbum, 2)
        self.assertEqual(Photos.PHAssetCollectionTypeMoment, 3)

        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumRegular, 2)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumSyncedEvent, 3)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumSyncedFaces, 4)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumSyncedAlbum, 5)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumImported, 6)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumMyPhotoStream, 100)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAlbumCloudShared, 101)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumGeneric, 200)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumPanoramas, 201)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumVideos, 202)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumFavorites, 203)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumTimelapses, 204)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumAllHidden, 205)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumRecentlyAdded, 206)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumBursts, 207)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumSlomoVideos, 208)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumUserLibrary, 209)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumSelfPortraits, 210)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumScreenshots, 211)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumDepthEffect, 212)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumLivePhotos, 213)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumAnimated, 214)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumLongExposures, 215)
        self.assertEqual(Photos.PHAssetCollectionSubtypeSmartAlbumUnableToUpload, 216)
        self.assertEqual(Photos.PHAssetCollectionSubtypeAny, sys.maxsize)

        self.assertEqual(Photos.PHAssetEditOperationDelete, 1)
        self.assertEqual(Photos.PHAssetEditOperationContent, 2)
        self.assertEqual(Photos.PHAssetEditOperationProperties, 3)

        self.assertEqual(Photos.PHAssetBurstSelectionTypeNone, 0)
        self.assertEqual(Photos.PHAssetBurstSelectionTypeAutoPick, 1 << 0)
        self.assertEqual(Photos.PHAssetBurstSelectionTypeUserPick, 1 << 1)

        self.assertEqual(Photos.PHAssetSourceTypeNone, 0)
        self.assertEqual(Photos.PHAssetSourceTypeUserLibrary, 1 << 0)
        self.assertEqual(Photos.PHAssetSourceTypeCloudShared, 1 << 1)
        self.assertEqual(Photos.PHAssetSourceTypeiTunesSynced, 1 << 2)

        self.assertEqual(Photos.PHAssetResourceTypePhoto, 1)
        self.assertEqual(Photos.PHAssetResourceTypeVideo, 2)
        self.assertEqual(Photos.PHAssetResourceTypeAudio, 3)
        self.assertEqual(Photos.PHAssetResourceTypeAlternatePhoto, 4)
        self.assertEqual(Photos.PHAssetResourceTypeFullSizePhoto, 5)
        self.assertEqual(Photos.PHAssetResourceTypeFullSizeVideo, 6)
        self.assertEqual(Photos.PHAssetResourceTypeAdjustmentData, 7)
        self.assertEqual(Photos.PHAssetResourceTypeAdjustmentBasePhoto, 8)
        self.assertEqual(Photos.PHAssetResourceTypePairedVideo, 9)
        self.assertEqual(Photos.PHAssetResourceTypeFullSizePairedVideo, 10)
        self.assertEqual(Photos.PHAssetResourceTypeAdjustmentBasePairedVideo, 11)
        self.assertEqual(Photos.PHAssetResourceTypeAdjustmentBaseVideo, 12)

        self.assertEqual(Photos.PHAssetPlaybackStyleUnsupported, 0)
        self.assertEqual(Photos.PHAssetPlaybackStyleImage, 1)
        self.assertEqual(Photos.PHAssetPlaybackStyleImageAnimated, 2)
        self.assertEqual(Photos.PHAssetPlaybackStyleLivePhoto, 3)
        self.assertEqual(Photos.PHAssetPlaybackStyleVideo, 4)
        self.assertEqual(Photos.PHAssetPlaybackStyleVideoLooping, 5)
