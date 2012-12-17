from Cocoa import *
from Quartz import *

import math

TRANSITION_COUNT=9

class TransitionSelectorView (NSView):
    _sourceImage = objc.ivar()
    _targetImage = objc.ivar()
    _shadingImage = objc.ivar()
    _blankImage = objc.ivar()
    _maskImage = objc.ivar()
    transitions = objc.ivar() # Array

    base = objc.ivar(type=objc._C_DBL)

    thumbnailWidth = objc.ivar(type=objc._C_FLT)
    thumbnailHeight = objc.ivar(type=objc._C_FLT)
    thumbnailGap = objc.ivar(type=objc._C_FLT)


    def awakeFromNib(self):
        self.thumbnailWidth  = 340.0
        self.thumbnailHeight = 240.0
        self.thumbnailGap    = 20.0


        url = NSURL.fileURLWithPath_(
            NSBundle.mainBundle().pathForResource_ofType_("Rose", "jpg"))
        self.setSourceImage_(CIImage.imageWithContentsOfURL_(url))


        url = NSURL.fileURLWithPath_(
            NSBundle.mainBundle().pathForResource_ofType_("Frog", "jpg"))
        self.setTargetImage_(CIImage.imageWithContentsOfURL_(url))


        timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                1.0/30.0, self, 'timerFired:', None, True)

        self.base = NSDate.pyobjc_classMethods.timeIntervalSinceReferenceDate()
        NSRunLoop.currentRunLoop().addTimer_forMode_(timer, NSDefaultRunLoopMode)
        NSRunLoop.currentRunLoop().addTimer_forMode_(timer, NSEventTrackingRunLoopMode)

    def setSourceImage_(self, source):
        self._sourceImage = source

    def setTargetImage_(self, target):
        self._targetImage = target

    def shadingImage(self):
        if self._shadingImage is None:
            url = NSURL.fileURLWithPath_(
                NSBundle.mainBundle().pathForResource_ofType_("Shading", "tiff"))
            self._shadingImage = CIImage.alloc().initWithContentsOfURL_(url)

        return self._shadingImage

    def blankImage(self):
        if self._blankImage is None:
            url = NSURL.fileURLWithPath_(
                NSBundle.mainBundle().pathForResource_ofType_("Blank", "jpg"))
            self._blankImage = CIImage.alloc().initWithContentsOfURL_(url)

        return self._blankImage

    def maskImage(self):
        if self._maskImage is None:
            url = NSURL.fileURLWithPath_(
                NSBundle.mainBundle().pathForResource_ofType_("Mask", "jpg"))
            self._maskImage = CIImage.alloc().initWithContentsOfURL_(url)

        return self._maskImage

    def timerFired_(self, sender):
        self.setNeedsDisplay_(True)


    def imageForTransition_atTime_(self, transitionNumber, t):
        transition = self.transitions[transitionNumber]

        if t % 2.0 < 1.0:
            transition.setValue_forKey_(self._sourceImage, "inputImage")
            transition.setValue_forKey_(self._targetImage, "inputTargetImage")
        else:
            transition.setValue_forKey_(self._targetImage, "inputImage")
            transition.setValue_forKey_(self._sourceImage, "inputTargetImage")

        transition._.inputTime = t % 1.0

        crop = CIFilter.filterWithName_("CICrop")
        crop._.inputImage = transition._.outputImage
        crop._.inputRectangle = CIVector.vectorWithX_Y_Z_W_(
                0, 0, self.thumbnailWidth, self.thumbnailHeight)
        return crop._.outputImage

    def drawRect_(self, rectangle):
        thumbFrame = CGRectMake(0, 0, self.thumbnailWidth, self.thumbnailHeight)
        t = 0.4*(NSDate.pyobjc_classMethods.timeIntervalSinceReferenceDate() - self.base)

        context = NSGraphicsContext.currentContext().CIContext()

        if self.transitions is None:
            self.transitions = [None] * TRANSITION_COUNT
            self.setupTransitions()

        w = int(math.ceil(math.sqrt(TRANSITION_COUNT)))
        origin = CGPoint()

        for i in xrange(TRANSITION_COUNT):
            origin.x = (i % w) * (self.thumbnailWidth  + self.thumbnailGap)
            origin.y = (i / w) * (self.thumbnailHeight + self.thumbnailGap)

            if context is not None:
                context.drawImage_atPoint_fromRect_(
                    self.imageForTransition_atTime_(i, t + 0.1 * i), origin, thumbFrame)


    def setupTransitions(self):
        w = self.thumbnailWidth
        h = self.thumbnailHeight

        extent = CIVector.vectorWithX_Y_Z_W_(0, 0, w, h)

        self.transitions[0] = CIFilter.filterWithName_("CISwipeTransition")
        self.transitions[0]._.inputExtent = extent
        self.transitions[0]._.inputColor = CIColor.colorWithRed_green_blue_alpha_(0, 0, 0, 0)
        self.transitions[0]._.inputAngle = 0.3 * math.pi
        self.transitions[0]._.inputWidth = 80.0
        self.transitions[0]._.inputOpacity = 0.0

        self.transitions[1] = CIFilter.filterWithName_("CIDissolveTransition")

        self.transitions[2] = CIFilter.filterWithName_("CISwipeTransition")                     # dupe
        self.transitions[2]._.inputExtent = extent
        self.transitions[2]._.inputColor = CIColor.colorWithRed_green_blue_alpha_(0, 0, 0, 0)
        self.transitions[2]._.inputAngle = math.pi
        self.transitions[2]._.inputWidth = 2.0
        self.transitions[2]._.inputOpacity = 0.2

        self.transitions[3] = CIFilter.filterWithName_("CIModTransition")
        self.transitions[3]._.inputCenter = CIVector.vectorWithX_Y_(0.5*w, 0.5*h)
        self.transitions[3]._.inputAngle =  math.pi*0.1
        self.transitions[3]._.inputRadius = 30.0
        self.transitions[3]._.inputCompression = 10.0

        self.transitions[4] = CIFilter.filterWithName_("CIFlashTransition")
        self.transitions[4]._.inputExtent = extent
        self.transitions[4]._.inputCenter = CIVector.vectorWithX_Y_(0.3*w, 0.7*h)
        self.transitions[4]._.inputColor = CIColor.colorWithRed_green_blue_alpha_(1, 0.8, 0.6, 1)
        self.transitions[4]._.inputMaxStriationRadius = 2.5
        self.transitions[4]._.inputStriationStrength = 0.5
        self.transitions[4]._.inputStriationContrast = 1.37
        self.transitions[4]._.inputFadeThreshold = 0.85

        self.transitions[5] = CIFilter.filterWithName_("CIDisintegrateWithMaskTransition")
        self.transitions[5]._.inputMaskImage = self.maskImage()
        self.transitions[5]._.inputShadowRadius = 10.0
        self.transitions[5]._.inputShadowDensity = 0.7
        self.transitions[5]._.inputShadowOffset = CIVector.vectorWithX_Y_(0.0, -0.05*h)

        self.transitions[6] = CIFilter.filterWithName_("CIRippleTransition")
        self.transitions[6]._.inputExtent = extent
        self.transitions[6]._.inputShadingImage = self.shadingImage()
        self.transitions[6]._.inputCenter = CIVector.vectorWithX_Y_(0.5*w, 0.5*h)
        self.transitions[6]._.inputWidth = 80.0
        self.transitions[6]._.inputScale = 30.0

        self.transitions[7] = CIFilter.filterWithName_("CICopyMachineTransition")
        self.transitions[7]._.inputExtent = extent
        self.transitions[7]._.inputColor = CIColor.colorWithRed_green_blue_alpha_(0.6, 1, 0.8, 1)
        self.transitions[7]._.inputAngle = 0
        self.transitions[7]._.inputWidth = 40
        self.transitions[7]._.inputOpacity = 1.0

        self.transitions[8] = CIFilter.filterWithName_("CIPageCurlTransition")
        self.transitions[8]._.inputExtent = extent
        self.transitions[8]._.inputShadingImage = self.shadingImage()
        self.transitions[8]._.inputBacksideImage = self.blankImage()
        self.transitions[8]._.inputAngle = -0.2 * math.pi
        self.transitions[8]._.inputRadius = 70.0
