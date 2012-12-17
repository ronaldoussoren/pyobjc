from Cocoa import *
from Quartz import *

import objc

_hazeRemovalKernel = None

class MyHazeFilter (CIFilter):
    inputImage      = objc.ivar()
    inputColor      = objc.ivar()
    inputDistance   = objc.ivar()
    inputSlope      = objc.ivar()


    @classmethod
    def initialize(cls):
        CIFilter.registerFilterName_constructor_classAttributes_(
                "MyHazeRemover",  cls, {
                    kCIAttributeFilterDisplayName: "Haze Remover" ,
                    kCIAttributeFilterCategories: [
                        kCICategoryColorAdjustment, kCICategoryVideo,
                        kCICategoryStillImage, kCICategoryInterlaced,
                        kCICategoryNonSquarePixels,
                    ],
                    "inputDistance": {
                        kCIAttributeMin: 0.0,
                        kCIAttributeMax: 1.0,
                        kCIAttributeSliderMin: 0.0,
                        kCIAttributeSliderMax: 0.7,
                        kCIAttributeDefault: 0.2,
                        kCIAttributeIdentity: 0.0,
                        kCIAttributeType: kCIAttributeTypeScalar,
                    },

                    "inputSlope": {
                        kCIAttributeSliderMin: -0.01,
                        kCIAttributeSliderMax: 0.01,
                        kCIAttributeDefault: 0.0,
                        kCIAttributeIdentity: 0.0,
                        kCIAttributeType: kCIAttributeTypeScalar,
                    },

                    "inputColor": {
                        kCIAttributeDefault: CIColor.colorWithRed_green_blue_alpha_(
                            1.0, 1.0, 1.0, 1.0),
                    },
                })

    @classmethod
    def filterWithName_(cls, name):
        filter = cls.alloc().init()
        return filter

    def init(self):
        global _hazeRemovalKernel

        if _hazeRemovalKernel is None:
            bundle = NSBundle.bundleForClass_(type(self))
            code = open(bundle.pathForResource_ofType_(
                "MyHazeRemoval", "cikernel"), 'rb').read()
            kernels = CIKernel.kernelsWithString_(code)
            _hazeRemovalKernel = kernels[0]

        return super(MyHazeFilter, self).init()

    def outputImage(self):
        src = CISampler.samplerWithImage_(self.inputImage)

        return self.apply_arguments_options_(_hazeRemovalKernel,
                (src, self.inputColor, self.inputDistance, self.inputSlope),
                { "definition": src.definition() })
