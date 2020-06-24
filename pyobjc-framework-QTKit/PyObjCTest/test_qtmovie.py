from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit
import objc


class TestQTMovieHelper(QTKit.NSObject):
    def movie_linkToURL_(self, m, u):
        return True

    def movieShouldLoadData_(self, d):
        return True

    def movieShouldTask_(self, m):
        return True

    def externalMovie_(self, d):
        return True

    def movie_shouldContinueOperation_withPhase_atPercent_withAttributes_(
        self, m, o, ph, per, at
    ):
        return True


class TestQTMovie(TestCase):
    def testConstants(self):
        self.assertIsInstance(QTKit.QTMoviePasteboardType, str)
        self.assertIsInstance(QTKit.QTMovieEditabilityDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieEditedNotification, str)
        self.assertIsInstance(QTKit.QTMovieLoadStateDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieLoopModeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieMessageStringPostedNotification, str)
        self.assertIsInstance(QTKit.QTMovieRateDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieSelectionDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieSizeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieStatusStringPostedNotification, str)
        self.assertIsInstance(QTKit.QTMovieTimeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieVolumeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieDidEndNotification, str)
        self.assertIsInstance(QTKit.QTMovieChapterDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieChapterListDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieEnterFullScreenRequestNotification, str)
        self.assertIsInstance(QTKit.QTMovieExitFullScreenRequestNotification, str)
        self.assertIsInstance(QTKit.QTMovieCloseWindowRequestNotification, str)
        self.assertIsInstance(QTKit.QTMovieApertureModeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieMessageNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieRateDidChangeNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieStatusFlagsNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieStatusCodeNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieStatusStringNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieTargetIDNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieTargetNameNotificationParameter, str)
        self.assertIsInstance(QTKit.QTMovieExport, str)
        self.assertIsInstance(QTKit.QTMovieExportType, str)
        self.assertIsInstance(QTKit.QTMovieFlatten, str)
        self.assertIsInstance(QTKit.QTMovieExportSettings, str)
        self.assertIsInstance(QTKit.QTMovieExportManufacturer, str)
        self.assertIsInstance(QTKit.QTAddImageCodecType, str)
        self.assertIsInstance(QTKit.QTAddImageCodecQuality, str)
        self.assertIsInstance(QTKit.QTMovieDataReferenceAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePasteboardAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDataAttribute, str)
        self.assertIsInstance(QTKit.QTMovieFileOffsetAttribute, str)
        self.assertIsInstance(QTKit.QTMovieResolveDataRefsAttribute, str)
        self.assertIsInstance(QTKit.QTMovieAskUnresolvedDataRefsAttribute, str)
        self.assertIsInstance(QTKit.QTMovieOpenAsyncOKAttribute, str)
        self.assertIsInstance(QTKit.QTMovieApertureModeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieActiveSegmentAttribute, str)
        self.assertIsInstance(QTKit.QTMovieAutoAlternatesAttribute, str)
        self.assertIsInstance(QTKit.QTMovieCopyrightAttribute, str)
        self.assertIsInstance(QTKit.QTMovieCreationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieCurrentSizeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieCurrentTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDataSizeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDelegateAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDisplayNameAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDontInteractWithUserAttribute, str)
        self.assertIsInstance(QTKit.QTMovieDurationAttribute, str)
        self.assertIsInstance(QTKit.QTMovieEditableAttribute, str)
        self.assertIsInstance(QTKit.QTMovieFileNameAttribute, str)
        self.assertIsInstance(QTKit.QTMovieHasApertureModeDimensionsAttribute, str)
        self.assertIsInstance(QTKit.QTMovieHasAudioAttribute, str)
        self.assertIsInstance(QTKit.QTMovieHasDurationAttribute, str)
        self.assertIsInstance(QTKit.QTMovieHasVideoAttribute, str)
        self.assertIsInstance(QTKit.QTMovieIsActiveAttribute, str)
        self.assertIsInstance(QTKit.QTMovieIsInteractiveAttribute, str)
        self.assertIsInstance(QTKit.QTMovieIsLinearAttribute, str)
        self.assertIsInstance(QTKit.QTMovieIsSteppableAttribute, str)
        self.assertIsInstance(QTKit.QTMovieLoadStateAttribute, str)
        self.assertIsInstance(QTKit.QTMovieLoopsAttribute, str)
        self.assertIsInstance(QTKit.QTMovieLoopsBackAndForthAttribute, str)
        self.assertIsInstance(QTKit.QTMovieModificationTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieMutedAttribute, str)
        self.assertIsInstance(QTKit.QTMovieNaturalSizeAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePlaysAllFramesAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePlaysSelectionOnlyAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePosterTimeAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePreferredMutedAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePreferredRateAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePreferredVolumeAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePreviewModeAttribute, str)
        self.assertIsInstance(QTKit.QTMoviePreviewRangeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieRateAttribute, str)
        self.assertIsInstance(QTKit.QTMovieSelectionAttribute, str)
        self.assertIsInstance(QTKit.QTMovieTimeScaleAttribute, str)
        self.assertIsInstance(QTKit.QTMovieURLAttribute, str)
        self.assertIsInstance(QTKit.QTMovieVolumeAttribute, str)
        self.assertIsInstance(QTKit.QTMovieRateChangesPreservePitchAttribute, str)
        self.assertIsInstance(QTKit.QTMovieUneditableException, str)

        self.assertEqual(QTKit.QTIncludeStillImageTypes, 1 << 0)
        self.assertEqual(QTKit.QTIncludeTranslatableTypes, 1 << 1)
        self.assertEqual(QTKit.QTIncludeAggressiveTypes, 1 << 2)
        self.assertEqual(QTKit.QTIncludeDynamicTypes, 1 << 3)
        self.assertEqual(QTKit.QTIncludeCommonTypes, 0)
        self.assertEqual(QTKit.QTIncludeAllTypes, 0xFFFF)
        self.assertEqual(QTKit.QTMovieOperationBeginPhase, 0)
        self.assertEqual(QTKit.QTMovieOperationUpdatePercentPhase, 1)
        self.assertEqual(QTKit.QTMovieOperationEndPhase, 2)

        self.assertEqual(QTKit.QTMovieLoadStateError, -1)
        self.assertEqual(QTKit.QTMovieLoadStateLoading, 1000)
        self.assertEqual(QTKit.QTMovieLoadStateLoaded, 2000)
        self.assertEqual(QTKit.QTMovieLoadStatePlayable, 10000)
        self.assertEqual(QTKit.QTMovieLoadStatePlaythroughOK, 20000)
        self.assertEqual(QTKit.QTMovieLoadStateComplete, 100_000)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(QTKit.QTMovieApertureModeClassic, str)
        self.assertIsInstance(QTKit.QTMovieApertureModeClean, str)
        self.assertIsInstance(QTKit.QTMovieApertureModeProduction, str)
        self.assertIsInstance(QTKit.QTMovieApertureModeEncodedPixels, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageSize, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageType, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageTypeNSImage, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageTypeCGImageRef, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageTypeCIImage, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageTypeCVPixelBufferRef, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageTypeCVOpenGLTextureRef, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageOpenGLContext, str)
        self.assertIsInstance(QTKit.QTMovieFrameImagePixelFormat, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageRepresentationsType, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageDeinterlaceFields, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageHighQuality, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageSingleField, str)
        self.assertIsInstance(QTKit.QTMovieChapterName, str)
        self.assertIsInstance(QTKit.QTMovieChapterStartTime, str)
        self.assertIsInstance(QTKit.QTMovieChapterTargetTrackAttribute, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(QTKit.QTMovieNaturalSizeDidChangeNotification, str)
        self.assertIsInstance(QTKit.QTMovieOpenAsyncRequiredAttribute, str)
        self.assertIsInstance(QTKit.QTMovieOpenForPlaybackAttribute, str)
        self.assertIsInstance(QTKit.QTMovieLoadStateErrorAttribute, str)
        self.assertIsInstance(QTKit.QTMovieFrameImageSessionMode, str)
        self.assertIsInstance(QTKit.QTDisallowedForInitializationPurposeException, str)

    def testInformalProtocols(self):
        # self.assertIsInstance(protocols.QTMovie_Delegate, objc.informal_protocol)
        self.assertResultIsBOOL(TestQTMovieHelper.movie_linkToURL_)
        self.assertResultIsBOOL(TestQTMovieHelper.movieShouldLoadData_)
        self.assertResultIsBOOL(TestQTMovieHelper.movieShouldTask_)
        self.assertResultIsBOOL(
            TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_
        )
        self.assertArgHasType(
            TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_,
            2,
            objc._C_INT,
        )

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTMovie.canInitWithPasteboard_)
        self.assertResultIsBOOL(QTKit.QTMovie.canInitWithFile_)
        self.assertResultIsBOOL(QTKit.QTMovie.canInitWithURL_)
        self.assertResultIsBOOL(QTKit.QTMovie.canInitWithDataReference_)
        self.assertResultIsBOOL(QTKit.QTMovie.muted)

        self.assertArgIsOut(QTKit.QTMovie.movieWithFile_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithURL_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithDataReference_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithPasteboard_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithData_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithAttributes_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieNamed_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initWithFile_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initWithURL_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initWithDataReference_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initWithPasteboard_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initWithData_error_, 1)
        self.assertArgHasType(
            QTKit.QTMovie.initWithMovie_timeRange_error_,
            1,
            QTKit.QTTimeRange.__typestr__,
        )  # b'{_QTTimeRange={_QTTime=qll}{_QTTime=qll}}')
        self.assertArgIsOut(QTKit.QTMovie.initWithMovie_timeRange_error_, 2)
        self.assertArgIsOut(QTKit.QTMovie.initWithAttributes_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.movieWithTimeRange_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initToWritableFile_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initToWritableData_error_, 1)
        self.assertArgIsOut(QTKit.QTMovie.initToWritableDataReference_error_, 1)

        self.assertArgIsOut(QTKit.QTMovie.frameImageAtTime_withAttributes_error_, 2)
        self.assertResultIsBOOL(QTKit.QTMovie.writeToFile_withAttributes_)
        self.assertResultIsBOOL(QTKit.QTMovie.writeToFile_withAttributes_error_)
        self.assertArgIsOut(QTKit.QTMovie.writeToFile_withAttributes_error_, 2)
        self.assertResultIsBOOL(QTKit.QTMovie.canUpdateMovieFile)
        self.assertResultIsBOOL(QTKit.QTMovie.updateMovieFile)
        self.assertArgIsBOOL(QTKit.QTMovie.setMuted_, 0)
        self.assertResultIsBOOL(QTKit.QTMovie.attachToCurrentThread)
        self.assertResultIsBOOL(QTKit.QTMovie.detachFromCurrentThread)
        self.assertArgIsBOOL(QTKit.QTMovie.setIdling_, 0)
        self.assertResultIsBOOL(QTKit.QTMovie.isIdling)
        self.assertResultIsBOOL(QTKit.QTMovie.hasChapters)
        self.assertResultIsBOOL(QTKit.QTMovie.removeChapters)
