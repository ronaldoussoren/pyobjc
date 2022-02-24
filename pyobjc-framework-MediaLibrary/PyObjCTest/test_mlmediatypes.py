from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaLibrary


class TestMLMediaTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MediaLibrary.MLMediaSourceType)
        self.assertIsEnumType(MediaLibrary.MLMediaType)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(MediaLibrary.MLMediaSourceTypeAudio, 1)
        self.assertEqual(MediaLibrary.MLMediaSourceTypeImage, 2)
        self.assertEqual(MediaLibrary.MLMediaSourceTypeMovie, 4)

        self.assertEqual(MediaLibrary.MLMediaTypeAudio, 1)
        self.assertEqual(MediaLibrary.MLMediaTypeImage, 2)
        self.assertEqual(MediaLibrary.MLMediaTypeMovie, 4)

        self.assertIsInstance(MediaLibrary.MLFolderRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLFolderGroupTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLiTunesRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesPurchasedPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesPodcastPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesSmartPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesFolderPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesMoviesPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesTVShowsPlaylistTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiTunesAudioBooksPlaylistTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiTunesMusicPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiTunesGeniusPlaylistTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiTunesSavedGeniusPlaylistTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiTunesiTunesUPlaylistTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLiPhotoRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoLibraryAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoEventsFolderTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoSmartAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoEventAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoLastImportAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoLastNMonthsAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFlaggedAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFolderAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoSubscribedAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFacesAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoPlacesAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiPhotoPlacesCountryAlbumTypeIdentifier, str
        )
        self.assertIsInstance(
            MediaLibrary.MLiPhotoPlacesProvinceAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiPhotoPlacesCityAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiPhotoFacebookAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFlickrAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFacebookGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoFlickrGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiPhotoSlideShowAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiPhotoLastViewedEventAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiPhotoPhotoStreamAlbumTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLApertureRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureUserAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureUserSmartAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureProjectAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFolderAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLApertureProjectFolderAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLApertureLightTableTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFlickrGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFlickrAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFacebookGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFacebookAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureSmugMugGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureSmugMugAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureSlideShowTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureAllPhotosTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFlaggedTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureAllProjectsTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLApertureFacesAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLAperturePlacesAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLAperturePlacesCountryAlbumTypeIdentifier, str
        )
        self.assertIsInstance(
            MediaLibrary.MLAperturePlacesProvinceAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLAperturePlacesCityAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLAperturePlacesPointOfInterestAlbumTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLApertureLastImportAlbumTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLApertureLastNMonthsAlbumTypeIdentifier, str
        )
        self.assertIsInstance(
            MediaLibrary.MLApertureLastViewedEventAlbumTypeIdentifier, str
        )
        self.assertIsInstance(
            MediaLibrary.MLAperturePhotoStreamAlbumTypeIdentifier, str
        )

        self.assertIsInstance(MediaLibrary.MLGarageBandRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLGarageBandFolderGroupTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLLogicRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLLogicBouncesGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLLogicProjectsGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLLogicProjectTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLiMovieRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiMovieEventGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiMovieProjectGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLiMovieEventLibraryGroupTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLiMovieEventCalendarGroupTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiMovieFolderGroupTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLFinalCutRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLFinalCutEventGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLFinalCutProjectGroupTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLFinalCutEventLibraryGroupTypeIdentifier, str
        )
        self.assertIsInstance(
            MediaLibrary.MLFinalCutEventCalendarGroupTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLFinalCutFolderGroupTypeIdentifier, str)

        self.assertIsInstance(MediaLibrary.MLMediaObjectDurationKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectArtistKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectAlbumKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectGenreKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectKindKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectTrackNumberKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectBitRateKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectSampleRateKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectChannelCountKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectResolutionStringKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectCommentsKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectKeywordsKey, str)
        self.assertIsInstance(MediaLibrary.MLMediaObjectProtectedKey, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            MediaLibrary.MLiTunesMusicVideosPlaylistTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLiTunesVideoPlaylistTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosRootGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosSharedGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAlbumsGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosFolderTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosSmartAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosPublishedAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAllMomentsGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosMomentGroupTypeIdentifier, str)
        self.assertIsInstance(
            MediaLibrary.MLPhotosAllCollectionsGroupTypeIdentifier, str
        )
        self.assertIsInstance(MediaLibrary.MLPhotosCollectionGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAllYearsGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosYearGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosLastImportGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosMyPhotoStreamTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosSharedPhotoStreamTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosFavoritesGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosPanoramasGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosVideosGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosSloMoGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosTimelapseGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosBurstGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosFacesAlbumTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAllPhotosAlbumTypeIdentifier, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(MediaLibrary.MLPhotosFrontCameraGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosScreenshotGroupTypeIdentifier, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(MediaLibrary.MLPhotosDepthEffectGroupTypeIdentifier, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(MediaLibrary.MLPhotosLivePhotosGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosLongExposureGroupTypeIdentifier, str)
        self.assertIsInstance(MediaLibrary.MLPhotosAnimatedGroupTypeIdentifier, str)
