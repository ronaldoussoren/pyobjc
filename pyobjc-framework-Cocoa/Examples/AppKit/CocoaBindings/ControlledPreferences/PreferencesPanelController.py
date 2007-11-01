#
#  PreferencesPanelController.py
#  ControlledPreferences
#
#  Converted by u.fiedler on 04.02.05.
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html


from FontNameToDisplayNameTransformer import FontNameToDisplayNameTransformer
from Foundation import *
from AppKit import *
from PyObjCTools.KeyValueCoding import *
from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses("MainMenu")

class PreferencesPanelController(NibClassBuilder.AutoBaseClass):
    # NSWindowController
        
    def changeTextFont_(self, sender):
        "The user changed the current font selection, so update the default font"
        
        # Get font name and size from user defaults
        defaults = NSUserDefaultsController.sharedUserDefaultsController().values()
        fontName = getKey(defaults, u'FontName')
        fontSize = getKey(defaults, u'FontSize')
        
        # Create font from name and size; initialize font panel
        font = NSFont.fontWithName_size_(fontName, fontSize)
        if font is None:
            font = NSFont.systemFontOfSize_(NSFont.systemFontSize())
        NSFontManager.sharedFontManager().setSelectedFont_isMultiple_(font, False)
        NSFontManager.sharedFontManager().orderFrontFontPanel_(self)
        
        # Set window as firstResponder so we get changeFont: messages
        self.window().makeFirstResponder_(self.window())
    
		
    def changeFont_(self, sender):
        "This is the message the font panel sends when a new font is selected"
        # Get selected font
        fontManager = NSFontManager.sharedFontManager()
        selectedFont = fontManager.selectedFont()
        if selectedFont is None:
            selectedFont = NSFont.systemFontOfSize_(NSFont.systemFontSize())
        panelFont = fontManager.convertFont_(selectedFont)
        
        # Get and store details of selected font
        # Note: use fontName, not displayName.  The font name identifies the font to
        # the system, we use a value transformer to show the user the display name
        fontSize = panelFont.pointSize()
        
        defaults = NSUserDefaultsController.sharedUserDefaultsController().values()
        defaults.setValue_forKey_(panelFont.fontName(), u"FontName")
        defaults.setValue_forKey_(fontSize, u"FontSize")


"""
Set up initial values for defaults:
Create dictionary with keys and values for WordOfTheDay, FontName,
FontSize, and FavoriteColor.  Mostly straightforward, but:

Store the fontName of the font as the default; the textfield displays
the font's displayName using a value transformer.

The color must be archived -- you can't store NSColors directly in NSUserDefaults.
"""

dictionary = {}
dictionary[u'WordOfTheDay'] = u'Today'
systemFont = NSFont.systemFontOfSize_(NSFont.systemFontSize())
dictionary[u"FontName"] = systemFont.fontName()
dictionary[u"FontSize"] = systemFont.pointSize()
archivedColor = NSArchiver.archivedDataWithRootObject_(NSColor.greenColor())
dictionary[u'FavoriteColor'] = archivedColor
NSUserDefaultsController.sharedUserDefaultsController().setInitialValues_(dictionary)

# Create and register font name value transformer
transformer = FontNameToDisplayNameTransformer.alloc().init()
NSValueTransformer.setValueTransformer_forName_(transformer, u'FontNameToDisplayNameTransformer')
