from PyObjCTools.TestSupport import TestCase

import UniformTypeIdentifiers


class TestUTCoreTypes(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeContent, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCompositeContent, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeDiskImage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeData, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeDirectory, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeResolvable, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSymbolicLink, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeExecutable, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMountPoint, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAliasFile, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeURLBookmarkData, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeURL, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeFileURL, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePlainText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUTF8PlainText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUTF16ExternalPlainText,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUTF16PlainText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeDelimitedText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCommaSeparatedText,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeTabSeparatedText, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUTF8TabSeparatedText,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeRTF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeHTML, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeXML, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeYAML, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSourceCode, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAssemblyLanguageSource,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCSource, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeObjectiveCSource, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSwiftSource, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCPlusPlusSource, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeObjectiveCPlusPlusSource,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCHeader, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCPlusPlusHeader, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAppleScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeOSAScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeOSAScriptBundle, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeJavaScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeShellScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePerlScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePythonScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeRubyScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePHPScript, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeJSON, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePropertyList, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeXMLPropertyList, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeBinaryPropertyList,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePDF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeRTFD, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeFlatRTFD, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeWebArchive, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeImage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeJPEG, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeTIFF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeGIF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePNG, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeICNS, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeBMP, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeICO, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeRAWImage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSVG, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeLivePhoto, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeHEIF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeHEIC, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeWebP, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTType3DContent, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUSD, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUSDZ, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeRealityFile, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSceneKitScene, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeARReferenceObject,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAudiovisualContent,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMovie, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeVideo, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAudio, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeQuickTimeMovie, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMPEG, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMPEG2Video, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMPEG2TransportStream,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMP3, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMPEG4Movie, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMPEG4Audio, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAppleProtectedMPEG4Audio,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAppleProtectedMPEG4Video,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAVI, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeAIFF, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeWAV, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMIDI, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePlaylist, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeM3UPlaylist, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeFolder, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeVolume, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePackage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeBundle, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePluginBundle, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSpotlightImporter,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeQuickLookGenerator,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeXPCService, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeFramework, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeApplication, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeApplicationBundle,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeApplicationExtension,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeUnixExecutable, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeEXE, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSystemPreferencesPane,
            UniformTypeIdentifiers.UTType,
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeArchive, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeGZIP, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeBZ2, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeZIP, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeSpreadsheet, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePresentation, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeDatabase, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeMessage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeContact, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeVCard, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeToDoItem, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeCalendarEvent, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeEmailMessage, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeInternetLocation, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeInternetShortcut, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeFont, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeBookmark, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypePKCS12, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeX509Certificate, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeEPUB, UniformTypeIdentifiers.UTType
        )
        self.assertIsInstance(
            UniformTypeIdentifiers.UTTypeLog, UniformTypeIdentifiers.UTType
        )
