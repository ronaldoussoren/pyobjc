#
#  ÇPROJECTNAMEASIDENTIFIERÈPlugIn.py
#  ÇPROJECTNAMEASIDENTIFIERÈ
#
#
"""
This loads all of your Objective-C classes and exposes them to Python
in a ÇPROJECTNAMEASIDENTIFIERÈ module.
"""

def _load(name, g):
    from Foundation import NSBundle
    import objc
    bundle_path = NSBundle.mainBundle().pathForResource_ofType_(unicode(name), u'bundle')
    objc.loadBundle(name, g, bundle_path=bundle_path)

_load(__name__,  globals())
