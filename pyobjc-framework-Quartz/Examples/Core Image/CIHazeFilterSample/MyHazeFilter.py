import objc
from objc import super
import Cocoa
import Quartz

_hazeRemovalKernel = None

class MyHazeFilter (Quartz.CIFilter):
    inputImage      = objc.ivar()
    inputColor      = objc.ivar()
    inputDistance   = objc.ivar()
    inputSlope      = objc.ivar()


    @classmethod
    def initialize(cls):
        Quartz.CIFilter.registerFilterName_constructor_classAttributes_(
                "MyHazeRemover",  cls, {
                    Quartz.kCIAttributeFilterDisplayName: "Haze Remover" ,
                    Quartz.kCIAttributeFilterCategories: [
                        Quartz.kCICategoryColorAdjustment, Quartz.kCICategoryVideo,
                        Quartz.kCICategoryStillImage, Quartz.kCICategoryInterlaced,
                        Quartz.kCICategoryNonSquarePixels,
                    ],
                    "inputDistance": {
                        Quartz.kCIAttributeMin: 0.0,
                        Quartz.kCIAttributeMax: 1.0,
                        Quartz.kCIAttributeSliderMin: 0.0,
                        Quartz.kCIAttributeSliderMax: 0.7,
                        Quartz.kCIAttributeDefault: 0.2,
                        Quartz.kCIAttributeIdentity: 0.0,
                        Quartz.kCIAttributeType: Quartz.kCIAttributeTypeScalar,
                    },

                    "inputSlope": {
                        Quartz.kCIAttributeSliderMin: -0.01,
                        Quartz.kCIAttributeSliderMax: 0.01,
                        Quartz.kCIAttributeDefault: 0.0,
                        Quartz.kCIAttributeIdentity: 0.0,
                        Quartz.kCIAttributeType: Quartz.kCIAttributeTypeScalar,
                    },

                    "inputColor": {
                        Quartz.kCIAttributeDefault: Quartz.CIColor.colorWithRed_green_blue_alpha_(
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
            bundle = Cocoa.NSBundle.bundleForClass_(type(self))
            with open(bundle.pathForResource_ofType_(
                "MyHazeRemoval", "cikernel"), 'r') as fp:
                code = fp.read()
            kernels = Quartz.CIKernel.kernelsWithString_(code)
            _hazeRemovalKernel = kernels[0]

        return super(MyHazeFilter, self).init()

    def outputImage(self):
        src = Quartz.CISampler.samplerWithImage_(self.inputImage)

        return self.apply_arguments_options_(_hazeRemovalKernel,
                (src, self.inputColor, self.inputDistance, self.inputSlope),
                { "definition": src.definition() })
