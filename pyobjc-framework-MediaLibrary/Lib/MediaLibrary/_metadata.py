# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:14:16 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$MLApertureAllPhotosTypeIdentifier$MLApertureAllProjectsTypeIdentifier$MLApertureFacebookAlbumTypeIdentifier$MLApertureFacebookGroupTypeIdentifier$MLApertureFacesAlbumTypeIdentifier$MLApertureFlaggedTypeIdentifier$MLApertureFlickrAlbumTypeIdentifier$MLApertureFlickrGroupTypeIdentifier$MLApertureFolderAlbumTypeIdentifier$MLApertureLastImportAlbumTypeIdentifier$MLApertureLastNMonthsAlbumTypeIdentifier$MLApertureLastViewedEventAlbumTypeIdentifier$MLApertureLightTableTypeIdentifier$MLAperturePhotoStreamAlbumTypeIdentifier$MLAperturePlacesAlbumTypeIdentifier$MLAperturePlacesCityAlbumTypeIdentifier$MLAperturePlacesCountryAlbumTypeIdentifier$MLAperturePlacesPointOfInterestAlbumTypeIdentifier$MLAperturePlacesProvinceAlbumTypeIdentifier$MLApertureProjectAlbumTypeIdentifier$MLApertureProjectFolderAlbumTypeIdentifier$MLApertureRootGroupTypeIdentifier$MLApertureSlideShowTypeIdentifier$MLApertureSmugMugAlbumTypeIdentifier$MLApertureSmugMugGroupTypeIdentifier$MLApertureUserAlbumTypeIdentifier$MLApertureUserSmartAlbumTypeIdentifier$MLFinalCutEventCalendarGroupTypeIdentifier$MLFinalCutEventGroupTypeIdentifier$MLFinalCutEventLibraryGroupTypeIdentifier$MLFinalCutFolderGroupTypeIdentifier$MLFinalCutProjectGroupTypeIdentifier$MLFinalCutRootGroupTypeIdentifier$MLFolderGroupTypeIdentifier$MLFolderRootGroupTypeIdentifier$MLGarageBandFolderGroupTypeIdentifier$MLGarageBandRootGroupTypeIdentifier$MLLogicBouncesGroupTypeIdentifier$MLLogicProjectTypeIdentifier$MLLogicProjectsGroupTypeIdentifier$MLLogicRootGroupTypeIdentifier$MLMediaLoadAppFoldersKey$MLMediaLoadAppleLoops$MLMediaLoadExcludeSourcesKey$MLMediaLoadFoldersKey$MLMediaLoadIncludeSourcesKey$MLMediaLoadMoviesFolder$MLMediaLoadSourceTypesKey$MLMediaObjectAlbumKey$MLMediaObjectArtistKey$MLMediaObjectBitRateKey$MLMediaObjectChannelCountKey$MLMediaObjectCommentsKey$MLMediaObjectDurationKey$MLMediaObjectGenreKey$MLMediaObjectKeywordsKey$MLMediaObjectKindKey$MLMediaObjectProtectedKey$MLMediaObjectResolutionStringKey$MLMediaObjectSampleRateKey$MLMediaObjectTrackNumberKey$MLMediaSourceApertureIdentifier$MLMediaSourceAppDefinedFoldersIdentifier$MLMediaSourceCustomFoldersIdentifier$MLMediaSourceFinalCutIdentifier$MLMediaSourceGarageBandIdentifier$MLMediaSourceLogicIdentifier$MLMediaSourceMoviesFolderIdentifier$MLMediaSourcePhotoBoothIdentifier$MLMediaSourcePhotosIdentifier$MLMediaSourceiMovieIdentifier$MLMediaSourceiPhotoIdentifier$MLMediaSourceiTunesIdentifier$MLPhotosAlbumTypeIdentifier$MLPhotosAlbumsGroupTypeIdentifier$MLPhotosAllCollectionsGroupTypeIdentifier$MLPhotosAllMomentsGroupTypeIdentifier$MLPhotosAllPhotosAlbumTypeIdentifier$MLPhotosAllYearsGroupTypeIdentifier$MLPhotosAnimatedGroupTypeIdentifier$MLPhotosBurstGroupTypeIdentifier$MLPhotosCollectionGroupTypeIdentifier$MLPhotosDepthEffectGroupTypeIdentifier$MLPhotosFacesAlbumTypeIdentifier$MLPhotosFavoritesGroupTypeIdentifier$MLPhotosFolderTypeIdentifier$MLPhotosFrontCameraGroupTypeIdentifier$MLPhotosLastImportGroupTypeIdentifier$MLPhotosLivePhotosGroupTypeIdentifier$MLPhotosLongExposureGroupTypeIdentifier$MLPhotosMomentGroupTypeIdentifier$MLPhotosMyPhotoStreamTypeIdentifier$MLPhotosPanoramasGroupTypeIdentifier$MLPhotosPublishedAlbumTypeIdentifier$MLPhotosRootGroupTypeIdentifier$MLPhotosScreenshotGroupTypeIdentifier$MLPhotosSharedGroupTypeIdentifier$MLPhotosSharedPhotoStreamTypeIdentifier$MLPhotosSloMoGroupTypeIdentifier$MLPhotosSmartAlbumTypeIdentifier$MLPhotosTimelapseGroupTypeIdentifier$MLPhotosVideosGroupTypeIdentifier$MLPhotosYearGroupTypeIdentifier$MLiMovieEventCalendarGroupTypeIdentifier$MLiMovieEventGroupTypeIdentifier$MLiMovieEventLibraryGroupTypeIdentifier$MLiMovieFolderGroupTypeIdentifier$MLiMovieProjectGroupTypeIdentifier$MLiMovieRootGroupTypeIdentifier$MLiPhotoAlbumTypeIdentifier$MLiPhotoEventAlbumTypeIdentifier$MLiPhotoEventsFolderTypeIdentifier$MLiPhotoFacebookAlbumTypeIdentifier$MLiPhotoFacebookGroupTypeIdentifier$MLiPhotoFacesAlbumTypeIdentifier$MLiPhotoFlaggedAlbumTypeIdentifier$MLiPhotoFlickrAlbumTypeIdentifier$MLiPhotoFlickrGroupTypeIdentifier$MLiPhotoFolderAlbumTypeIdentifier$MLiPhotoLastImportAlbumTypeIdentifier$MLiPhotoLastNMonthsAlbumTypeIdentifier$MLiPhotoLastViewedEventAlbumTypeIdentifier$MLiPhotoLibraryAlbumTypeIdentifier$MLiPhotoPhotoStreamAlbumTypeIdentifier$MLiPhotoPlacesAlbumTypeIdentifier$MLiPhotoPlacesCityAlbumTypeIdentifier$MLiPhotoPlacesCountryAlbumTypeIdentifier$MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier$MLiPhotoPlacesProvinceAlbumTypeIdentifier$MLiPhotoRootGroupTypeIdentifier$MLiPhotoSlideShowAlbumTypeIdentifier$MLiPhotoSmartAlbumTypeIdentifier$MLiPhotoSubscribedAlbumTypeIdentifier$MLiTunesAudioBooksPlaylistTypeIdentifier$MLiTunesFolderPlaylistTypeIdentifier$MLiTunesGeniusPlaylistTypeIdentifier$MLiTunesMoviesPlaylistTypeIdentifier$MLiTunesMusicPlaylistTypeIdentifier$MLiTunesMusicVideosPlaylistTypeIdentifier$MLiTunesPlaylistTypeIdentifier$MLiTunesPodcastPlaylistTypeIdentifier$MLiTunesPurchasedPlaylistTypeIdentifier$MLiTunesRootGroupTypeIdentifier$MLiTunesSavedGeniusPlaylistTypeIdentifier$MLiTunesSmartPlaylistTypeIdentifier$MLiTunesTVShowsPlaylistTypeIdentifier$MLiTunesVideoPlaylistTypeIdentifier$MLiTunesiTunesUPlaylistTypeIdentifier$"""
enums = """$MLMediaSourceTypeAudio@1$MLMediaSourceTypeImage@2$MLMediaSourceTypeMovie@4$MLMediaTypeAudio@1$MLMediaTypeImage@2$MLMediaTypeMovie@4$"""
misc.update(
    {
        "MLMediaType": NewType("MLMediaType", int),
        "MLMediaSourceType": NewType("MLMediaSourceType", int),
    }
)
misc.update({})
misc.update({})

objc.registerNewKeywordsFromSelector("MLMediaLibrary", b"initWithOptions:")
expressions = {}

# END OF FILE
