
from PyObjCTools.TestSupport import *
from QTKit import *
import sys

try:
    unicode
except NameError:
    unicode = str

class TestQTMovieHelper (NSObject):
    def movie_linkToURL_(self, m, u):
        return True

    def movieShouldLoadData_(self, d):
        return True

    def movieShouldTask_(self, m):
        return True

    def externalMovie_(self, d):
        return True

    def movie_shouldContinueOperation_withPhase_atPercent_withAttributes_(self, m, o, ph, per, at):
        return True




class TestQTMovie (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTMoviePasteboardType, unicode)
        self.assertIsInstance(QTMovieEditabilityDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieEditedNotification, unicode)
        self.assertIsInstance(QTMovieLoadStateDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieLoopModeDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieMessageStringPostedNotification, unicode)
        self.assertIsInstance(QTMovieRateDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieSelectionDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieSizeDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieStatusStringPostedNotification, unicode)
        self.assertIsInstance(QTMovieTimeDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieVolumeDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieDidEndNotification, unicode)
        self.assertIsInstance(QTMovieChapterDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieChapterListDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieEnterFullScreenRequestNotification, unicode)
        self.assertIsInstance(QTMovieExitFullScreenRequestNotification, unicode)
        self.assertIsInstance(QTMovieCloseWindowRequestNotification, unicode)
        self.assertIsInstance(QTMovieApertureModeDidChangeNotification, unicode)
        self.assertIsInstance(QTMovieMessageNotificationParameter, unicode)
        self.assertIsInstance(QTMovieRateDidChangeNotificationParameter, unicode)
        self.assertIsInstance(QTMovieStatusFlagsNotificationParameter, unicode)
        self.assertIsInstance(QTMovieStatusCodeNotificationParameter, unicode)
        self.assertIsInstance(QTMovieStatusStringNotificationParameter, unicode)
        self.assertIsInstance(QTMovieTargetIDNotificationParameter, unicode)
        self.assertIsInstance(QTMovieTargetNameNotificationParameter, unicode)
        self.assertIsInstance(QTMovieExport, unicode)
        self.assertIsInstance(QTMovieExportType, unicode)
        self.assertIsInstance(QTMovieFlatten, unicode)
        self.assertIsInstance(QTMovieExportSettings, unicode)
        self.assertIsInstance(QTMovieExportManufacturer, unicode)
        self.assertIsInstance(QTAddImageCodecType, unicode)
        self.assertIsInstance(QTAddImageCodecQuality, unicode)
        self.assertIsInstance(QTMovieDataReferenceAttribute, unicode)
        self.assertIsInstance(QTMoviePasteboardAttribute, unicode)
        self.assertIsInstance(QTMovieDataAttribute, unicode)
        self.assertIsInstance(QTMovieFileOffsetAttribute, unicode)
        self.assertIsInstance(QTMovieResolveDataRefsAttribute, unicode)
        self.assertIsInstance(QTMovieAskUnresolvedDataRefsAttribute, unicode)
        self.assertIsInstance(QTMovieOpenAsyncOKAttribute, unicode)
        self.assertIsInstance(QTMovieApertureModeAttribute, unicode)
        self.assertIsInstance(QTMovieActiveSegmentAttribute, unicode)
        self.assertIsInstance(QTMovieAutoAlternatesAttribute, unicode)
        self.assertIsInstance(QTMovieCopyrightAttribute, unicode)
        self.assertIsInstance(QTMovieCreationTimeAttribute, unicode)
        self.assertIsInstance(QTMovieCurrentSizeAttribute, unicode)
        self.assertIsInstance(QTMovieCurrentTimeAttribute, unicode)
        self.assertIsInstance(QTMovieDataSizeAttribute, unicode)
        self.assertIsInstance(QTMovieDelegateAttribute, unicode)
        self.assertIsInstance(QTMovieDisplayNameAttribute, unicode)
        self.assertIsInstance(QTMovieDontInteractWithUserAttribute, unicode)
        self.assertIsInstance(QTMovieDurationAttribute, unicode)
        self.assertIsInstance(QTMovieEditableAttribute, unicode)
        self.assertIsInstance(QTMovieFileNameAttribute, unicode)
        self.assertIsInstance(QTMovieHasApertureModeDimensionsAttribute, unicode)
        self.assertIsInstance(QTMovieHasAudioAttribute, unicode)
        self.assertIsInstance(QTMovieHasDurationAttribute, unicode)
        self.assertIsInstance(QTMovieHasVideoAttribute, unicode)
        self.assertIsInstance(QTMovieIsActiveAttribute, unicode)
        self.assertIsInstance(QTMovieIsInteractiveAttribute, unicode)
        self.assertIsInstance(QTMovieIsLinearAttribute, unicode)
        self.assertIsInstance(QTMovieIsSteppableAttribute, unicode)
        self.assertIsInstance(QTMovieLoadStateAttribute, unicode)
        self.assertIsInstance(QTMovieLoopsAttribute, unicode)
        self.assertIsInstance(QTMovieLoopsBackAndForthAttribute, unicode)
        self.assertIsInstance(QTMovieModificationTimeAttribute, unicode)
        self.assertIsInstance(QTMovieMutedAttribute, unicode)
        self.assertIsInstance(QTMovieNaturalSizeAttribute, unicode)
        self.assertIsInstance(QTMoviePlaysAllFramesAttribute, unicode)
        self.assertIsInstance(QTMoviePlaysSelectionOnlyAttribute, unicode)
        self.assertIsInstance(QTMoviePosterTimeAttribute, unicode)
        self.assertIsInstance(QTMoviePreferredMutedAttribute, unicode)
        self.assertIsInstance(QTMoviePreferredRateAttribute, unicode)
        self.assertIsInstance(QTMoviePreferredVolumeAttribute, unicode)
        self.assertIsInstance(QTMoviePreviewModeAttribute, unicode)
        self.assertIsInstance(QTMoviePreviewRangeAttribute, unicode)
        self.assertIsInstance(QTMovieRateAttribute, unicode)
        self.assertIsInstance(QTMovieSelectionAttribute, unicode)
        self.assertIsInstance(QTMovieTimeScaleAttribute, unicode)
        self.assertIsInstance(QTMovieURLAttribute, unicode)
        self.assertIsInstance(QTMovieVolumeAttribute, unicode)
        self.assertIsInstance(QTMovieRateChangesPreservePitchAttribute, unicode)
        self.assertIsInstance(QTMovieUneditableException, unicode)

        self.assertEqual(QTIncludeStillImageTypes, 1 << 0)
        self.assertEqual(QTIncludeTranslatableTypes, 1 << 1)
        self.assertEqual(QTIncludeAggressiveTypes, 1 << 2)
        self.assertEqual(QTIncludeDynamicTypes, 1 << 3)
        self.assertEqual(QTIncludeCommonTypes, 0)
        self.assertEqual(QTIncludeAllTypes, 0xffff)
        self.assertEqual(QTMovieOperationBeginPhase, 0)
        self.assertEqual(QTMovieOperationUpdatePercentPhase, 1)
        self.assertEqual(QTMovieOperationEndPhase, 2)

        self.assertEqual(QTMovieLoadStateError, -1)
        self.assertEqual(QTMovieLoadStateLoading, 1000)
        self.assertEqual(QTMovieLoadStateLoaded, 2000)
        self.assertEqual(QTMovieLoadStatePlayable, 10000)
        self.assertEqual(QTMovieLoadStatePlaythroughOK, 20000)
        self.assertEqual(QTMovieLoadStateComplete, 100000)



    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(QTMovieApertureModeClassic, unicode)
        self.assertIsInstance(QTMovieApertureModeClean, unicode)
        self.assertIsInstance(QTMovieApertureModeProduction, unicode)
        self.assertIsInstance(QTMovieApertureModeEncodedPixels, unicode)
        self.assertIsInstance(QTMovieFrameImageSize, unicode)
        self.assertIsInstance(QTMovieFrameImageType, unicode)
        self.assertIsInstance(QTMovieFrameImageTypeNSImage, unicode)
        self.assertIsInstance(QTMovieFrameImageTypeCGImageRef, unicode)
        self.assertIsInstance(QTMovieFrameImageTypeCIImage, unicode)
        self.assertIsInstance(QTMovieFrameImageTypeCVPixelBufferRef, unicode)
        self.assertIsInstance(QTMovieFrameImageTypeCVOpenGLTextureRef, unicode)
        self.assertIsInstance(QTMovieFrameImageOpenGLContext, unicode)
        self.assertIsInstance(QTMovieFrameImagePixelFormat, unicode)
        self.assertIsInstance(QTMovieFrameImageRepresentationsType, unicode)
        self.assertIsInstance(QTMovieFrameImageDeinterlaceFields, unicode)
        self.assertIsInstance(QTMovieFrameImageHighQuality, unicode)
        self.assertIsInstance(QTMovieFrameImageSingleField, unicode)
        self.assertIsInstance(QTMovieChapterName, unicode)
        self.assertIsInstance(QTMovieChapterStartTime, unicode)
        self.assertIsInstance(QTMovieChapterTargetTrackAttribute, unicode)

    def testInformalProtocols(self):
        self.assertIsInstance(protocols.QTMovie_Delegate, objc.informal_protocol)
        self.assertResultIsBOOL(TestQTMovieHelper.movie_linkToURL_)
        self.assertResultIsBOOL(TestQTMovieHelper.movieShouldLoadData_)
        self.assertResultIsBOOL(TestQTMovieHelper.movieShouldTask_)
        self.assertResultIsBOOL(TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_)
        self.assertArgHasType(TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_, 2, objc._C_INT)

    @onlyOn32Bit
    def testMethods32(self):
        self.assertArgIsBOOL(QTMovie.movieWithQuickTimeMovie_disposeWhenDone_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithQuickTimeMovie_disposeWhenDone_error_, 2)
        self.assertArgIsBOOL(QTMovie.initWithQuickTimeMovie_disposeWhenDone_error_, 1)
        self.assertArgIsOut(QTMovie.initWithQuickTimeMovie_disposeWhenDone_error_, 2)

    @onlyOn32Bit
    def testCarbonQuickTimeIntegration(self):
        #FIXME: Should test integration with the Carbon.Qt module here
        pass
        #- (Movie)quickTimeMovie;
        #- (MovieController)quickTimeMovieController;


    def testMethods(self):
        self.assertResultIsBOOL(QTMovie.canInitWithPasteboard_)
        self.assertResultIsBOOL(QTMovie.canInitWithFile_)
        self.assertResultIsBOOL(QTMovie.canInitWithURL_)
        self.assertResultIsBOOL(QTMovie.canInitWithDataReference_)
        self.assertResultIsBOOL(QTMovie.muted)


        self.assertArgIsOut(QTMovie.movieWithFile_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithURL_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithDataReference_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithPasteboard_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithData_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithAttributes_error_, 1)
        self.assertArgIsOut(QTMovie.movieNamed_error_, 1)
        self.assertArgIsOut(QTMovie.initWithFile_error_, 1)
        self.assertArgIsOut(QTMovie.initWithURL_error_, 1)
        self.assertArgIsOut(QTMovie.initWithDataReference_error_, 1)
        self.assertArgIsOut(QTMovie.initWithPasteboard_error_, 1)
        self.assertArgIsOut(QTMovie.initWithData_error_, 1)
        self.assertArgHasType(QTMovie.initWithMovie_timeRange_error_, 1, QTTimeRange.__typestr__) #b'{_QTTimeRange={_QTTime=qll}{_QTTime=qll}}')
        self.assertArgIsOut(QTMovie.initWithMovie_timeRange_error_, 2)
        self.assertArgIsOut(QTMovie.initWithAttributes_error_, 1)
        self.assertArgIsOut(QTMovie.movieWithTimeRange_error_, 1)
        self.assertArgIsOut(QTMovie.initToWritableFile_error_, 1)
        self.assertArgIsOut(QTMovie.initToWritableData_error_, 1)
        self.assertArgIsOut(QTMovie.initToWritableDataReference_error_, 1)

        self.assertArgIsOut(QTMovie.frameImageAtTime_withAttributes_error_, 2)
        self.assertResultIsBOOL(QTMovie.writeToFile_withAttributes_)
        self.assertResultIsBOOL(QTMovie.writeToFile_withAttributes_error_)
        self.assertArgIsOut(QTMovie.writeToFile_withAttributes_error_, 2)
        self.assertResultIsBOOL(QTMovie.canUpdateMovieFile)
        self.assertResultIsBOOL(QTMovie.updateMovieFile)
        self.assertArgIsBOOL(QTMovie.setMuted_, 0)
        self.assertResultIsBOOL(QTMovie.attachToCurrentThread)
        self.assertResultIsBOOL(QTMovie.detachFromCurrentThread)
        self.assertArgIsBOOL(QTMovie.setIdling_, 0)
        self.assertResultIsBOOL(QTMovie.isIdling)
        self.assertResultIsBOOL(QTMovie.hasChapters)
        self.assertResultIsBOOL(QTMovie.removeChapters)




if __name__ == "__main__":
    main()
