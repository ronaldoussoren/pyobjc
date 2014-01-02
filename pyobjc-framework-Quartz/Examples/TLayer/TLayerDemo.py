import Cocoa
import Quartz
import objc
from objc import super

import ShadowOffsetView


class TLayerDemo (Cocoa.NSObject):
    colorWell = objc.IBOutlet()
    shadowOffsetView = objc.IBOutlet()
    shadowRadiusSlider = objc.IBOutlet()
    tlayerView = objc.IBOutlet()
    transparencyLayerButton = objc.IBOutlet()


    @classmethod
    def initialize(self):
        Cocoa.NSColorPanel.sharedColorPanel().setShowsAlpha_(True)

    def init(self):
        self = super(TLayerDemo, self).init()
        if self is None:
            return None

        if not Cocoa.NSBundle.loadNibNamed_owner_("TLayerDemo", self):
            Cocoa.NSLog("Failed to load TLayerDemo.nib")
            return nil

        self.shadowOffsetView.setScale_(40)
        self.shadowOffsetView.setOffset_(Quartz.CGSizeMake(-30, -30))
        self.tlayerView.setShadowOffset_(Quartz.CGSizeMake(-30, -30))

        self.shadowRadiusChanged_(self.shadowRadiusSlider)

        # Better to do this as a subclass of NSControl....
        Cocoa.NSNotificationCenter.defaultCenter(
                ).addObserver_selector_name_object_(
                        self, b'shadowOffsetChanged:',
                        ShadowOffsetView.ShadowOffsetChanged, None)
        return self

    def dealloc(self):
        Cocoa.NSNotificationCenter.defaultCenter().removeObserver_(self)
        super(TLayerDemo, self).dealloc()

    def window(self):
        return self.tlayerView.window()

    @objc.IBAction
    def shadowRadiusChanged_(self, sender):
        self.tlayerView.setShadowRadius_(self.shadowRadiusSlider.floatValue())

    @objc.IBAction
    def toggleTransparencyLayers_(self, sender):
        self.tlayerView.setUsesTransparencyLayers_(self.transparencyLayerButton.state())

    def shadowOffsetChanged_(self, notification):
        offset = notification.object().offset()
        self.tlayerView.setShadowOffset_(offset)
