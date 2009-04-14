from Cocoa import *
from PyObjCTools import NibClassBuilder
from Quartz import *
import objc

import ShadowOffsetView


class TLayerDemo (NSObject:
    colorWell = objc.IBOutlet()
    shadowOffsetView = objc.IBOutlet()
    shadowRadiusSlider = objc.IBOutlet()
    tlayerView = objc.IBOutlet()
    transparencyLayerButton = objc.IBOutlet()


    @classmethod
    def initialize(self):
        NSColorPanel.sharedColorPanel().setShowsAlpha_(True)

    def init(self):
        self = super(TLayerDemo, self).init()
        if self is None:
            return None

        if not NSBundle.loadNibNamed_owner_("TLayerDemo", self):
            NSLog("Failed to load TLayerDemo.nib")
	    return nil

        self.shadowOffsetView.setScale_(40)
        self.shadowOffsetView.setOffset_(CGSizeMake(-30, -30))
        self.tlayerView.setShadowOffset_(CGSizeMake(-30, -30))

        self.shadowRadiusChanged_(self.shadowRadiusSlider)

        # Better to do this as a subclass of NSControl.... 
        NSNotificationCenter.defaultCenter(
                ).addObserver_selector_name_object_(
                        self, 'shadowOffsetChanged:',
                        ShadowOffsetView.ShadowOffsetChanged, None)
        return self

    def dealloc(self):
        NSNotificationCenter.defaultCenter().removeObserver_(self)
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
