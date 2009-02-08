
from PyObjCTools.TestSupport import *
from QTKit import *

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
        self.failUnlessIsInstance(QTMoviePasteboardType, unicode)
        self.failUnlessIsInstance(QTMovieEditabilityDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieEditedNotification, unicode)
        self.failUnlessIsInstance(QTMovieLoadStateDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieLoopModeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieMessageStringPostedNotification, unicode)
        self.failUnlessIsInstance(QTMovieRateDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieSizeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieStatusStringPostedNotification, unicode)
        self.failUnlessIsInstance(QTMovieTimeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieVolumeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieDidEndNotification, unicode)
        self.failUnlessIsInstance(QTMovieChapterDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieChapterListDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieEnterFullScreenRequestNotification, unicode)
        self.failUnlessIsInstance(QTMovieExitFullScreenRequestNotification, unicode)
        self.failUnlessIsInstance(QTMovieCloseWindowRequestNotification, unicode)
        self.failUnlessIsInstance(QTMovieApertureModeDidChangeNotification, unicode)
        self.failUnlessIsInstance(QTMovieMessageNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieRateDidChangeNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieStatusFlagsNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieStatusCodeNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieStatusStringNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieTargetIDNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieTargetNameNotificationParameter, unicode)
        self.failUnlessIsInstance(QTMovieExport, unicode)
        self.failUnlessIsInstance(QTMovieExportType, unicode)
        self.failUnlessIsInstance(QTMovieFlatten, unicode)
        self.failUnlessIsInstance(QTMovieExportSettings, unicode)
        self.failUnlessIsInstance(QTMovieExportManufacturer, unicode)
        self.failUnlessIsInstance(QTAddImageCodecType, unicode)
        self.failUnlessIsInstance(QTAddImageCodecQuality, unicode)
        self.failUnlessIsInstance(QTMovieDataReferenceAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePasteboardAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDataAttribute, unicode)
        self.failUnlessIsInstance(QTMovieFileOffsetAttribute, unicode)
        self.failUnlessIsInstance(QTMovieResolveDataRefsAttribute, unicode)
        self.failUnlessIsInstance(QTMovieAskUnresolvedDataRefsAttribute, unicode)
        self.failUnlessIsInstance(QTMovieOpenAsyncOKAttribute, unicode)
        self.failUnlessIsInstance(QTMovieApertureModeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieActiveSegmentAttribute, unicode)
        self.failUnlessIsInstance(QTMovieAutoAlternatesAttribute, unicode)
        self.failUnlessIsInstance(QTMovieCopyrightAttribute, unicode)
        self.failUnlessIsInstance(QTMovieCreationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieCurrentSizeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieCurrentTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDataSizeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDelegateAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDisplayNameAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDontInteractWithUserAttribute, unicode)
        self.failUnlessIsInstance(QTMovieDurationAttribute, unicode)
        self.failUnlessIsInstance(QTMovieEditableAttribute, unicode)
        self.failUnlessIsInstance(QTMovieFileNameAttribute, unicode)
        self.failUnlessIsInstance(QTMovieHasApertureModeDimensionsAttribute, unicode)
        self.failUnlessIsInstance(QTMovieHasAudioAttribute, unicode)
        self.failUnlessIsInstance(QTMovieHasDurationAttribute, unicode)
        self.failUnlessIsInstance(QTMovieHasVideoAttribute, unicode)
        self.failUnlessIsInstance(QTMovieIsActiveAttribute, unicode)
        self.failUnlessIsInstance(QTMovieIsInteractiveAttribute, unicode)
        self.failUnlessIsInstance(QTMovieIsLinearAttribute, unicode)
        self.failUnlessIsInstance(QTMovieIsSteppableAttribute, unicode)
        self.failUnlessIsInstance(QTMovieLoadStateAttribute, unicode)
        self.failUnlessIsInstance(QTMovieLoopsAttribute, unicode)
        self.failUnlessIsInstance(QTMovieLoopsBackAndForthAttribute, unicode)
        self.failUnlessIsInstance(QTMovieModificationTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieMutedAttribute, unicode)
        self.failUnlessIsInstance(QTMovieNaturalSizeAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePlaysAllFramesAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePlaysSelectionOnlyAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePosterTimeAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePreferredMutedAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePreferredRateAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePreferredVolumeAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePreviewModeAttribute, unicode)
        self.failUnlessIsInstance(QTMoviePreviewRangeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieRateAttribute, unicode)
        self.failUnlessIsInstance(QTMovieSelectionAttribute, unicode)
        self.failUnlessIsInstance(QTMovieTimeScaleAttribute, unicode)
        self.failUnlessIsInstance(QTMovieURLAttribute, unicode)
        self.failUnlessIsInstance(QTMovieVolumeAttribute, unicode)
        self.failUnlessIsInstance(QTMovieRateChangesPreservePitchAttribute, unicode)
        self.failUnlessIsInstance(QTMovieUneditableException, unicode)

        self.failUnlessEqual(QTIncludeStillImageTypes, 1 << 0)
        self.failUnlessEqual(QTIncludeTranslatableTypes, 1 << 1)
        self.failUnlessEqual(QTIncludeAggressiveTypes, 1 << 2)
        self.failUnlessEqual(QTIncludeDynamicTypes, 1 << 3)
        self.failUnlessEqual(QTIncludeCommonTypes, 0)
        self.failUnlessEqual(QTIncludeAllTypes, 0xffff)
        self.failUnlessEqual(QTMovieOperationBeginPhase, 0)
        self.failUnlessEqual(QTMovieOperationUpdatePercentPhase, 1)
        self.failUnlessEqual(QTMovieOperationEndPhase, 2)

        self.failUnlessEqual(QTMovieLoadStateError, -1)
        self.failUnlessEqual(QTMovieLoadStateLoading, 1000)
        self.failUnlessEqual(QTMovieLoadStateLoaded, 2000)
        self.failUnlessEqual(QTMovieLoadStatePlayable, 10000)
        self.failUnlessEqual(QTMovieLoadStatePlaythroughOK, 20000)
        self.failUnlessEqual(QTMovieLoadStateComplete, 100000)



    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(QTMovieApertureModeClassic, unicode)
        self.failUnlessIsInstance(QTMovieApertureModeClean, unicode)
        self.failUnlessIsInstance(QTMovieApertureModeProduction, unicode)
        self.failUnlessIsInstance(QTMovieApertureModeEncodedPixels, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageSize, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageType, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageTypeNSImage, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageTypeCGImageRef, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageTypeCIImage, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageTypeCVPixelBufferRef, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageTypeCVOpenGLTextureRef, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageOpenGLContext, unicode)
        self.failUnlessIsInstance(QTMovieFrameImagePixelFormat, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageRepresentationsType, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageDeinterlaceFields, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageHighQuality, unicode)
        self.failUnlessIsInstance(QTMovieFrameImageSingleField, unicode)
        self.failUnlessIsInstance(QTMovieChapterName, unicode)
        self.failUnlessIsInstance(QTMovieChapterStartTime, unicode)
        self.failUnlessIsInstance(QTMovieChapterTargetTrackAttribute, unicode)

    def testInformalProtocols(self):
        self.failUnlessIsInstance(protocols.QTMovieDelegate, objc.informal_protocol)
        self.failUnlessResultIsBOOL(TestQTMovieHelper.movie_linkToURL_)
        self.failUnlessResultIsBOOL(TestQTMovieHelper.movieShouldLoadData_)
        self.failUnlessResultIsBOOL(TestQTMovieHelper.movieShouldTask_)
        self.failUnlessResultIsBOOL(TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_)
        self.failUnlessArgHasType(TestQTMovieHelper.movie_shouldContinueOperation_withPhase_atPercent_withAttributes_, 2, objc._C_INT)

    @onlyOn32Bit
    def testMethods32(self):
        self.failUnlessArgIsBOOL(QTMovie.movieWithQuickTimeMovie_disposeWhenDone_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithQuickTimeMovie_disposeWhenDone_error_, 2)
        self.failUnlessArgIsBOOL(QTMovie.initWithQuickTimeMovie_disposeWhenDone_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithQuickTimeMovie_disposeWhenDone_error_, 2)

    @onlyOn32Bit
    def testCarbonQuickTimeIntegration(self):
        #FIXME: Should test integration with the Carbon.Qt module here
        pass
        #- (Movie)quickTimeMovie;
        #- (MovieController)quickTimeMovieController;


    def testMethods(self):
        self.failUnlessResultIsBOOL(QTMovie.canInitWithPasteboard_)
        self.failUnlessResultIsBOOL(QTMovie.canInitWithFile_)
        self.failUnlessResultIsBOOL(QTMovie.canInitWithURL_)
        self.failUnlessResultIsBOOL(QTMovie.canInitWithDataReference_)
        self.failUnlessResultIsBOOL(QTMovie.muted)


        self.failUnlessArgIsOut(QTMovie.movieWithFile_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithURL_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithDataReference_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithPasteboard_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithData_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithAttributes_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieNamed_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithFile_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithURL_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithDataReference_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithPasteboard_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initWithData_error_, 1)
        self.failUnlessArgHasType(QTMovie.initWithMovie_timeRange_error_, 1, '{?={?=qll}{?=qll}}')
        self.failUnlessArgIsOut(QTMovie.initWithMovie_timeRange_error_, 2)
        self.failUnlessArgIsOut(QTMovie.initWithAttributes_error_, 1)
        self.failUnlessArgIsOut(QTMovie.movieWithTimeRange_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initToWritableFile_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initToWritableData_error_, 1)
        self.failUnlessArgIsOut(QTMovie.initToWritableDataReference_error_, 1)

        self.failUnlessArgIsOut(QTMovie.frameImageAtTime_withAttributes_error_, 2)
        self.failUnlessResultIsBOOL(QTMovie.writeToFile_withAttributes_)
        self.failUnlessResultIsBOOL(QTMovie.writeToFile_withAttributes_error_)
        self.failUnlessArgIsOut(QTMovie.writeToFile_withAttributes_error_, 2)
        self.failUnlessResultIsBOOL(QTMovie.canUpdateMovieFile)
        self.failUnlessResultIsBOOL(QTMovie.updateMovieFile)
        self.failUnlessArgIsBOOL(QTMovie.setMuted_, 0)
        self.failUnlessResultIsBOOL(QTMovie.attachToCurrentThread)
        self.failUnlessResultIsBOOL(QTMovie.detachFromCurrentThread)
        self.failUnlessArgIsBOOL(QTMovie.setIdling_, 0)
        self.failUnlessResultIsBOOL(QTMovie.isIdling)
        self.failUnlessResultIsBOOL(QTMovie.hasChapters)
        self.failUnlessResultIsBOOL(QTMovie.removeChapters)




if __name__ == "__main__":
    main()
