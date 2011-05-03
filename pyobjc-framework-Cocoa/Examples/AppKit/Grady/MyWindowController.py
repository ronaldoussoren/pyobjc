from Cocoa import *

class MyWindowController (NSWindowController):
    rectGradientView = objc.IBOutlet()
    bezierGradientView = objc.IBOutlet()
    
    startColorWell = objc.IBOutlet()
    endColorWell = objc.IBOutlet()
    angle = objc.IBOutlet()
    angleSlider = objc.IBOutlet()
    
    radialCheck = objc.IBOutlet()
    radialExplainText = objc.IBOutlet()


    def initWithPath_(self, newPath):
        return super(MyWindowController, self).initWithWindowNibName_("TestWindow")

    def awakeFromNib(self):
        # make sure our angle text input keep the right format
        formatter = NSNumberFormatter.alloc().init()
        formatter.setNumberStyle_(NSNumberFormatterDecimalStyle)
        self.angle.cell().setFormatter_(formatter)
        
        # setup the initial start color
        self.rectGradientView.setStartColor_(NSColor.orangeColor())
        self.bezierGradientView.setStartColor_(NSColor.orangeColor())
        self.startColorWell.setColor_(NSColor.orangeColor())
        
        # setup the initial end color
        self.rectGradientView.setEndColor_(NSColor.blueColor())
        self.bezierGradientView.setEndColor_(NSColor.blueColor())
        self.endColorWell.setColor_(NSColor.blueColor())
        
        # setup the initial angle value
        self.rectGradientView.setAngle_(90.0)
        self.bezierGradientView.setAngle_(90.0)
        self.angle.setStringValue_("90.0")
        self.angleSlider.setFloatValue_(90.0)

    @objc.IBAction
    def swapColors_(self, sender):
        startColor = self.startColorWell.color()
        endColor = self.endColorWell.color()
        
        # change all our view's start and end colors
        self.rectGradientView.setStartColor_(endColor)
        self.rectGradientView.setEndColor_(startColor)
        
        self.bezierGradientView.setStartColor_(endColor)
        self.bezierGradientView.setEndColor_(startColor)
        
        # fix our color wells
        self.startColorWell.setColor_(endColor)
        self.endColorWell.setColor_(startColor)

    @objc.IBAction
    def startColor_(self, sender):
        newColor = sender.color()
        self.rectGradientView.setStartColor_(newColor)
        self.bezierGradientView.setStartColor_(newColor)

    @objc.IBAction
    def endColor_(self, sender):
        newColor = sender.color()
        self.rectGradientView.setEndColor_(newColor)
        self.bezierGradientView.setEndColor_(newColor)

    def controlTextDidEndEditing_(self, notification):
        theAngle = self.angle.floatValue()
        self.rectGradientView.setAngle_(theAngle)
        self.bezierGradientView.setAngle_(theAngle)
        
        theAngleDougle = self.angle.doubleValue()
        self.angleSlider.setDoubleValue_(theAngleDougle)
        self.angleSlider.setNeedsDisplay_(True)

    @objc.IBAction
    def angleSliderChange_(self, sender):
        angleValue = sender.floatValue()
        self.rectGradientView.setAngle_(angleValue)
        self.bezierGradientView.setAngle_(angleValue)
        self.angle.setDoubleValue_(angleValue)

    @objc.IBAction
    def radialDraw_(self, sender):
        self.rectGradientView.setRadialDraw_(sender.selectedCell().state())
        self.bezierGradientView.setRadialDraw_(sender.selectedCell().state())
        
        # angle factor does not relate to radial draws
        self.angleSlider.setEnabled_(not sender.selectedCell().state())
        self.angle.setEnabled_(not sender.selectedCell().state())
        
        # hide/show the explain text for radial gradients
        self.radialExplainText.setHidden_(not sender.selectedCell().state())
