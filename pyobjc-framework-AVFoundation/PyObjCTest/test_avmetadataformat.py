import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMetadataFormat(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceCommon, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyTitle, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCreator, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySubject, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyDescription, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyPublisher, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyContributor, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCreationDate, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLastModifiedDate, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyType, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyFormat, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyIdentifier, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySource, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLanguage, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyRelation, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyLocation, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyCopyrights, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyAlbumName, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyAuthor, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyArtist, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyArtwork, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyMake, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeyModel, str)
        self.assertIsInstance(AVFoundation.AVMetadataCommonKeySoftware, str)
        self.assertIsInstance(AVFoundation.AVMetadataFormatQuickTimeUserData, str)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceQuickTimeUserData, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyAlbum, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyArranger, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyArtist, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyAuthor, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyChapter, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyComment, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyComposer, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyCopyright, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyCreationDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyDescription, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyDirector, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyDisclaimer, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyEncodedBy, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyFullName, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyGenre, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyHostComputer, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyInformation, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyKeywords, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyMake, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyModel, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalFormat, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyOriginalSource, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyPerformers, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyProducer, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyPublisher, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyProduct, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeySoftware, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeySpecialPlaybackRequirements, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyTrack, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyWarning, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyWriter, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyURLLink, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyLocationISO6709, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyTrackName, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeUserDataKeyCredits, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyPhonogramRights, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataISOUserDataKeyCopyright, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyCopyright, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyAuthor, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyPerformer, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyGenre, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyRecordingYear, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyLocation, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyTitle, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyDescription, str)
        self.assertIsInstance(AVFoundation.AVMetadataFormatQuickTimeMetadata, str)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceQuickTimeMetadata, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyAuthor, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyComment, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyCopyright, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCreationDate, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyDirector, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDisplayName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyInformation, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyKeywords, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyProducer, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyPublisher, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyAlbum, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyArtist, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyArtwork, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDescription, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeySoftware, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyYear, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyGenre, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyiXML, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationISO6709, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyMake, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyModel, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyArranger, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyEncodedBy, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyOriginalArtist, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyPerformer, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyComposer, str)
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyCredits, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyPhonogramRights, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCameraIdentifier, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataQuickTimeMetadataKeyTitle, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyCollectionUser, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyRatingUser, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationBody, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationNote, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationRole, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyLocationDate, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDirectionFacing, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyDirectionMotion, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataFormatiTunesMetadata, str)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceiTunes, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAlbum, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArtist, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyUserComment, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyCoverArt, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyCopyright, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyReleaseDate, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyEncodedBy, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPredefinedGenre, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyUserGenre, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySongName, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyTrackSubTitle, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyEncodingTool, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyComposer, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAlbumArtist, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAccountKind, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAppleID, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArtistID, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySongID, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyDiscCompilation, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyDiscNumber, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyGenreID, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyGrouping, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyPlaylistID, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyContentRating, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyBeatsPerMin, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyTrackNumber, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArtDirector, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyArranger, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyAuthor, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyLyrics, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyAcknowledgement, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyConductor, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyDescription, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyDirector, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyEQ, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyLinerNotes, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyRecordCompany, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyOriginalArtist, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeyPhonogramRights, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyProducer, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyPerformer, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyPublisher, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataiTunesMetadataKeySoundEngineer, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeySoloist, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyCredits, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyThanks, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyOnlineExtras, str)
        self.assertIsInstance(AVFoundation.AVMetadataiTunesMetadataKeyExecProducer, str)
        self.assertIsInstance(AVFoundation.AVMetadataFormatID3Metadata, str)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceID3, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyAudioEncryption, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyAttachedPicture, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyAudioSeekPointIndex, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyComments, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCommerical, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncryption, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEqualization, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEqualization2, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyEventTimingCodes, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyGeneralEncapsulatedObject, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyGroupIdentifier, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInvolvedPeopleList_v23, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLink, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMusicCDIdentifier, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMPEGLocationLookupTable, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyOwnership, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPrivate, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPlayCounter, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPopularimeter, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPositionSynchronization, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRecommendedBufferSize, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRelativeVolumeAdjustment, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyRelativeVolumeAdjustment2, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyReverb, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySeek, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySignature, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeySynchronizedLyric, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeySynchronizedTempoCodes, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyAlbumTitle, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyBeatsPerMinute, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyComposer, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyContentType, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCopyright, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyDate, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncodingTime, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPlaylistDelay, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalReleaseTime, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyRecordingTime, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyReleaseTime, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTaggingTime, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncodedBy, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLyricist, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyFileType, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTime, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInvolvedPeopleList_v24, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyContentGroupDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyTitleDescription, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySubTitle, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyInitialKey, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLanguage, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLength, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyMusicianCreditsList, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyMediaType, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyMood, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalAlbumTitle, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalFilename, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalLyricist, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyOriginalArtist, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOriginalReleaseYear, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyFileOwner, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyLeadPerformer, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyBand, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyConductor, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyModifiedBy, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPartOfASet, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyProducedNotice, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPublisher, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTrackNumber, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyRecordingDates, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternetRadioStationName, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternetRadioStationOwner, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySize, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyAlbumSortOrder, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyPerformerSortOrder, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTitleSortOrder, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyInternationalStandardRecordingCode, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyEncodedWith, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeySetSubtitle, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyYear, str)
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyUserText, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyUniqueFileIdentifier, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyTermsOfUse, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyUnsynchronizedLyric, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyCommercialInformation, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyCopyrightInformation, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialAudioFileWebpage, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialArtistWebpage, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialAudioSourceWebpage, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialInternetRadioStationHomepage,
            str,
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyPayment, str)
        self.assertIsInstance(
            AVFoundation.AVMetadataID3MetadataKeyOfficialPublisherWebpage, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyUserURL, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyTaggedCharacteristic, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVMetadataFormatISOUserData, str)
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceISOUserData, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyCollection, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyUserRating, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyThumbnail, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyAlbumAndTrack, str)
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyKeywordList, str)
        self.assertIsInstance(
            AVFoundation.AVMetadata3GPUserDataKeyMediaClassification, str
        )
        self.assertIsInstance(AVFoundation.AVMetadata3GPUserDataKeyMediaRating, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataISOUserDataKeyTaggedCharacteristic, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceIcy, str)
        self.assertIsInstance(AVFoundation.AVMetadataIcyMetadataKeyStreamTitle, str)
        self.assertIsInstance(AVFoundation.AVMetadataIcyMetadataKeyStreamURL, str)
        self.assertIsInstance(AVFoundation.AVMetadataFormatHLSMetadata, str)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeValueURIKey, str)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeBaseURIKey, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyContentIdentifier, str
        )
        self.assertIsInstance(AVFoundation.AVMetadataID3MetadataKeyCommercial, str)
        self.assertIsInstance(AVFoundation.AVMetadataExtraAttributeInfoKey, str)

    @min_os_level("10.11.3")
    def testConstants10_11_3(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceHLSDateRange, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVMetadataISOUserDataKeyDate, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVMetadataKeySpaceAudioFile, str)
        self.assertIsInstance(AVFoundation.AVMetadataFormatUnknown, str)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonKeyAccessibilityDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeUserDataKeyAccessibilityDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataISOUserDataKeyAccessibilityDescription, str
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataQuickTimeMetadataKeyAccessibilityDescription, str
        )
