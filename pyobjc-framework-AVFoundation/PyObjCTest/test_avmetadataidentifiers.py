import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMetadataIdentifiers(TestCase):
    @min_os_level("10.10")
    def testConstants10(self):
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierTitle, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierCreator, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierSubject, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierDescription, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierPublisher, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierContributor, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierCreationDate, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierLastModifiedDate, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierType, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierFormat, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierAssetIdentifier, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierSource, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierLanguage, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierRelation, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierLocation, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierCopyrights, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierAlbumName, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierAuthor, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierArtist, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierArtwork, str
        )  # noqa: B950
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierMake, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierModel, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierSoftware, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataAlbum, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataArranger, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataAuthor, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataChapter, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataComment, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataComposer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCreationDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDirector, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDisclaimer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataEncodedBy, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataFullName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataGenre, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataHostComputer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataInformation, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataKeywords, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataMake, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataModel, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalArtist,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalFormat,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalSource,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPerformers, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataProducer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPublisher, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataProduct, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataSoftware, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataSpecialPlaybackRequirements,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTrack, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataWarning, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataWriter, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataURLLink, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataLocationISO6709,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTrackName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCredits, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPhonogramRights,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTaggedCharacteristic,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierISOUserDataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierISOUserDataTaggedCharacteristic,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataAuthor, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataPerformer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataGenre, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataRecordingYear, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataLocation, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataTitle, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataCollection, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataUserRating, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataThumbnail, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataAlbumAndTrack, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataKeywordList, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataMediaClassification, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataMediaRating, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataAuthor, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataComment, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCreationDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirector, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDisplayName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataInformation, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataKeywords, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataProducer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPublisher, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataAlbum, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArtwork, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataSoftware, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataYear, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataGenre, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataiXML, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationISO6709,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataMake, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataModel, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArranger, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataEncodedBy, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataOriginalArtist,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPerformer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataComposer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCredits, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPhonogramRights,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCameraIdentifier,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCollectionUser,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataRatingUser, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationBody, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationNote, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationRole, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirectionFacing,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirectionMotion,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPreferredAffineTransform,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAlbum, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataUserComment, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCoverArt, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataReleaseDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEncodedBy, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPredefinedGenre, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataUserGenre, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSongName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataTrackSubTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEncodingTool, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataComposer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAlbumArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAccountKind, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAppleID, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtistID, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSongID, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDiscCompilation, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDiscNumber, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataGenreID, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataGrouping, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPlaylistID, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataContentRating, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataBeatsPerMin, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataTrackNumber, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtDirector, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArranger, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAuthor, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataLyrics, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAcknowledgement, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataConductor, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDirector, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEQ, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataLinerNotes, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataRecordCompany, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataOriginalArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPhonogramRights, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataProducer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPerformer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPublisher, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSoundEngineer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSoloist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCredits, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataThanks, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataOnlineExtras, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataExecProducer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAudioEncryption, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAttachedPicture, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAudioSeekPointIndex, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataComments, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncryption, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEqualization, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEqualization2, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEventTimingCodes, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataGeneralEncapsulatedObject,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataGroupIdentifier, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInvolvedPeopleList_v23,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLink, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMusicCDIdentifier, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMPEGLocationLookupTable,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOwnership, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPrivate, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPlayCounter, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPopularimeter, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPositionSynchronization,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecommendedBufferSize,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment2,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataReverb, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSeek, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSignature, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSynchronizedLyric, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSynchronizedTempoCodes,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAlbumTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataBeatsPerMinute, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataComposer, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataContentType, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCopyright, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataDate, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodingTime, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPlaylistDelay, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalReleaseTime, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecordingTime, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataReleaseTime, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTaggingTime, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodedBy, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLyricist, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataFileType, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTime, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInvolvedPeopleList_v24,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataContentGroupDescription,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTitleDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSubTitle, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInitialKey, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLanguage, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLength, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMusicianCreditsList, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMediaType, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMood, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalAlbumTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalFilename, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalLyricist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalReleaseYear, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataFileOwner, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLeadPerformer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataBand, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataConductor, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataModifiedBy, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPartOfASet, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataProducedNotice, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPublisher, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTrackNumber, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecordingDates, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternetRadioStationName,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternetRadioStationOwner,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSize, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAlbumSortOrder, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPerformerSortOrder, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTitleSortOrder, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternationalStandardRecordingCode,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodedWith, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSetSubtitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataYear, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUserText, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUniqueFileIdentifier,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTermsOfUse, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUnsynchronizedLyric, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommercialInformation,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCopyrightInformation,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialAudioFileWebpage,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialArtistWebpage,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialAudioSourceWebpage,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPayment, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialPublisherWebpage,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUserURL, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierIcyMetadataStreamTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierIcyMetadataStreamURL, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedFace, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataVideoOrientation,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataContentIdentifier,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommercial, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommerical, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierISOUserDataDate, str
        )  # noqa: B950

    @min_os_level("10.15")
    def testConstants10_15(self):
        with self.subTest("humanbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedHumanBody,
                str,  # noqa: B950
            )

        with self.subTest("catbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedCatBody,
                str,  # noqa: B950
            )
        with self.subTest("dogbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedDogBody,
                str,  # noqa: B950
            )
        with self.subTest("salientobject"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedSalientObject,  # noqa: B950
                str,
            )
        with self.subTest("livephoto"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataAutoLivePhoto,
                str,  # noqa: B950
            )
        with self.subTest("vitalityscore"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataLivePhotoVitalityScore,  # noqa: B950
                str,
            )
        with self.subTest("vitalityscoringversion"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataLivePhotoVitalityScoringVersion,  # noqa: B950
                str,
            )
        with self.subTest("qualityscore"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataSpatialOverCaptureQualityScore,  # noqa: B950
                str,
            )
        with self.subTest("qaulityscoringversion"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataSpatialOverCaptureQualityScoringVersion,  # noqa: B950
                str,
            )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierAccessibilityDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataAccessibilityDescription,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataAccessibilityDescription,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationHorizontalAccuracyInMeters,
            str,
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataIsMontage, str
        )
