# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#

from bundlebuilder import buildapp 
    
buildapp(
    mainprogram = "CurrencyConverter.py",
    resources = ["English.lproj" ],
    nibname = "MainMenu",
)   

