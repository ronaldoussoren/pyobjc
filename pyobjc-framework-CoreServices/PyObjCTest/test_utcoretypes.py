import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestUTCoreTypes(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kUTTypeItem, str)
        self.assertIsInstance(CoreServices.kUTTypeContent, str)
        self.assertIsInstance(CoreServices.kUTTypeCompositeContent, str)
        self.assertIsInstance(CoreServices.kUTTypeApplication, str)
        self.assertIsInstance(CoreServices.kUTTypeMessage, str)
        self.assertIsInstance(CoreServices.kUTTypeContact, str)
        self.assertIsInstance(CoreServices.kUTTypeArchive, str)
        self.assertIsInstance(CoreServices.kUTTypeDiskImage, str)
        self.assertIsInstance(CoreServices.kUTTypeData, str)
        self.assertIsInstance(CoreServices.kUTTypeDirectory, str)
        self.assertIsInstance(CoreServices.kUTTypeResolvable, str)
        self.assertIsInstance(CoreServices.kUTTypeSymLink, str)
        self.assertIsInstance(CoreServices.kUTTypeMountPoint, str)
        self.assertIsInstance(CoreServices.kUTTypeAliasFile, str)
        self.assertIsInstance(CoreServices.kUTTypeAliasRecord, str)
        self.assertIsInstance(CoreServices.kUTTypeURL, str)
        self.assertIsInstance(CoreServices.kUTTypeFileURL, str)
        self.assertIsInstance(CoreServices.kUTTypeText, str)
        self.assertIsInstance(CoreServices.kUTTypePlainText, str)
        self.assertIsInstance(CoreServices.kUTTypeUTF8PlainText, str)
        self.assertIsInstance(CoreServices.kUTTypeUTF16ExternalPlainText, str)
        self.assertIsInstance(CoreServices.kUTTypeUTF16PlainText, str)
        self.assertIsInstance(CoreServices.kUTTypeRTF, str)
        self.assertIsInstance(CoreServices.kUTTypeHTML, str)
        self.assertIsInstance(CoreServices.kUTTypeXML, str)
        self.assertIsInstance(CoreServices.kUTTypeSourceCode, str)
        self.assertIsInstance(CoreServices.kUTTypeCSource, str)
        self.assertIsInstance(CoreServices.kUTTypeObjectiveCSource, str)
        self.assertIsInstance(CoreServices.kUTTypeCPlusPlusSource, str)
        self.assertIsInstance(CoreServices.kUTTypeObjectiveCPlusPlusSource, str)
        self.assertIsInstance(CoreServices.kUTTypeCHeader, str)
        self.assertIsInstance(CoreServices.kUTTypeCPlusPlusHeader, str)
        self.assertIsInstance(CoreServices.kUTTypeJavaSource, str)
        self.assertIsInstance(CoreServices.kUTTypePDF, str)
        self.assertIsInstance(CoreServices.kUTTypeRTFD, str)
        self.assertIsInstance(CoreServices.kUTTypeFlatRTFD, str)
        self.assertIsInstance(CoreServices.kUTTypeTXNTextAndMultimediaData, str)
        self.assertIsInstance(CoreServices.kUTTypeWebArchive, str)
        self.assertIsInstance(CoreServices.kUTTypeImage, str)
        self.assertIsInstance(CoreServices.kUTTypeJPEG, str)
        self.assertIsInstance(CoreServices.kUTTypeJPEG2000, str)
        self.assertIsInstance(CoreServices.kUTTypeTIFF, str)
        self.assertIsInstance(CoreServices.kUTTypePICT, str)
        self.assertIsInstance(CoreServices.kUTTypeGIF, str)
        self.assertIsInstance(CoreServices.kUTTypePNG, str)
        self.assertIsInstance(CoreServices.kUTTypeQuickTimeImage, str)
        self.assertIsInstance(CoreServices.kUTTypeAppleICNS, str)
        self.assertIsInstance(CoreServices.kUTTypeBMP, str)
        self.assertIsInstance(CoreServices.kUTTypeICO, str)
        self.assertIsInstance(CoreServices.kUTTypeAudiovisualContent, str)
        self.assertIsInstance(CoreServices.kUTTypeMovie, str)
        self.assertIsInstance(CoreServices.kUTTypeVideo, str)
        self.assertIsInstance(CoreServices.kUTTypeAudio, str)
        self.assertIsInstance(CoreServices.kUTTypeQuickTimeMovie, str)
        self.assertIsInstance(CoreServices.kUTTypeMPEG, str)
        self.assertIsInstance(CoreServices.kUTTypeMPEG4, str)
        self.assertIsInstance(CoreServices.kUTTypeMP3, str)
        self.assertIsInstance(CoreServices.kUTTypeMPEG4Audio, str)
        self.assertIsInstance(CoreServices.kUTTypeAppleProtectedMPEG4Audio, str)
        self.assertIsInstance(CoreServices.kUTTypeFolder, str)
        self.assertIsInstance(CoreServices.kUTTypeVolume, str)
        self.assertIsInstance(CoreServices.kUTTypePackage, str)
        self.assertIsInstance(CoreServices.kUTTypeBundle, str)
        self.assertIsInstance(CoreServices.kUTTypeFramework, str)
        self.assertIsInstance(CoreServices.kUTTypeApplicationBundle, str)
        self.assertIsInstance(CoreServices.kUTTypeApplicationFile, str)
        self.assertIsInstance(CoreServices.kUTTypeVCard, str)
        self.assertIsInstance(CoreServices.kUTTypeInkText, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CoreServices.kUTTypeURLBookmarkData, str)
        self.assertIsInstance(CoreServices.kUTTypeDelimitedText, str)
        self.assertIsInstance(CoreServices.kUTTypeCommaSeparatedText, str)
        self.assertIsInstance(CoreServices.kUTTypeTabSeparatedText, str)
        self.assertIsInstance(CoreServices.kUTTypeUTF8TabSeparatedText, str)
        self.assertIsInstance(CoreServices.kUTTypeAssemblyLanguageSource, str)
        self.assertIsInstance(CoreServices.kUTTypeScript, str)
        self.assertIsInstance(CoreServices.kUTTypeAppleScript, str)
        self.assertIsInstance(CoreServices.kUTTypeOSAScript, str)
        self.assertIsInstance(CoreServices.kUTTypeOSAScriptBundle, str)
        self.assertIsInstance(CoreServices.kUTTypeJavaScript, str)
        self.assertIsInstance(CoreServices.kUTTypeShellScript, str)
        self.assertIsInstance(CoreServices.kUTTypePerlScript, str)
        self.assertIsInstance(CoreServices.kUTTypePythonScript, str)
        self.assertIsInstance(CoreServices.kUTTypeRubyScript, str)
        self.assertIsInstance(CoreServices.kUTTypePHPScript, str)
        self.assertIsInstance(CoreServices.kUTTypeJSON, str)
        self.assertIsInstance(CoreServices.kUTTypePropertyList, str)
        self.assertIsInstance(CoreServices.kUTTypeXMLPropertyList, str)
        self.assertIsInstance(CoreServices.kUTTypeBinaryPropertyList, str)
        self.assertIsInstance(CoreServices.kUTTypeRawImage, str)
        self.assertIsInstance(CoreServices.kUTTypeScalableVectorGraphics, str)
        self.assertIsInstance(CoreServices.kUTTypeMPEG2Video, str)
        self.assertIsInstance(CoreServices.kUTTypeMPEG2TransportStream, str)
        self.assertIsInstance(CoreServices.kUTTypeAppleProtectedMPEG4Video, str)
        self.assertIsInstance(CoreServices.kUTTypeAVIMovie, str)
        self.assertIsInstance(CoreServices.kUTTypeAudioInterchangeFileFormat, str)
        self.assertIsInstance(CoreServices.kUTTypeWaveformAudio, str)
        self.assertIsInstance(CoreServices.kUTTypeMIDIAudio, str)
        self.assertIsInstance(CoreServices.kUTTypePlaylist, str)
        self.assertIsInstance(CoreServices.kUTTypeM3UPlaylist, str)
        self.assertIsInstance(CoreServices.kUTTypePluginBundle, str)
        self.assertIsInstance(CoreServices.kUTTypeSpotlightImporter, str)
        self.assertIsInstance(CoreServices.kUTTypeQuickLookGenerator, str)
        self.assertIsInstance(CoreServices.kUTTypeXPCService, str)
        self.assertIsInstance(CoreServices.kUTTypeUnixExecutable, str)
        self.assertIsInstance(CoreServices.kUTTypeWindowsExecutable, str)
        self.assertIsInstance(CoreServices.kUTTypeJavaClass, str)
        self.assertIsInstance(CoreServices.kUTTypeJavaArchive, str)
        self.assertIsInstance(CoreServices.kUTTypeSystemPreferencesPane, str)
        self.assertIsInstance(CoreServices.kUTTypeGNUZipArchive, str)
        self.assertIsInstance(CoreServices.kUTTypeBzip2Archive, str)
        self.assertIsInstance(CoreServices.kUTTypeZipArchive, str)
        self.assertIsInstance(CoreServices.kUTTypeSpreadsheet, str)
        self.assertIsInstance(CoreServices.kUTTypePresentation, str)
        self.assertIsInstance(CoreServices.kUTTypeToDoItem, str)
        self.assertIsInstance(CoreServices.kUTTypeCalendarEvent, str)
        self.assertIsInstance(CoreServices.kUTTypeEmailMessage, str)
        self.assertIsInstance(CoreServices.kUTTypeInternetLocation, str)
        self.assertIsInstance(CoreServices.kUTTypeFont, str)
        self.assertIsInstance(CoreServices.kUTTypeBookmark, str)
        self.assertIsInstance(CoreServices.kUTType3DContent, str)
        self.assertIsInstance(CoreServices.kUTTypePKCS12, str)
        self.assertIsInstance(CoreServices.kUTTypeX509Certificate, str)
        self.assertIsInstance(CoreServices.kUTTypeElectronicPublication, str)
        self.assertIsInstance(CoreServices.kUTTypeLog, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(CoreServices.kUTTypeSwiftSource, str)
