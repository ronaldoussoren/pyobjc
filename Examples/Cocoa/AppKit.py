import pyobjc
from Cocoa import Foundation


def LoadBundle( path ):
        bundle = Foundation.NSBundle.bundleWithPath_( path )
        bundle.load()
        return bundle


# load AppKit so those classes are available for inspection
AppKitBundle = LoadBundle( '/System/Library/Frameworks/AppKit.framework')

__AppKit__ = globals()
for _name in dir(pyobjc.runtime):
    if _name[0] <> '_' and _name not in dir(Foundation)+Foundation.__skip__:
		__AppKit__[_name] = pyobjc.lookup_class(_name)

del _name



