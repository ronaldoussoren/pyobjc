import objc as _objc
from _Foundation import *

NSClassFromString = _objc.lookUpClass

# Do something smart to collect Foundation classes...

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        'Foundation',
        globals(),
        bundle_identifier=u'com.apple.Foundation',
    )
else:
    _objc.loadBundle(
        'Foundation',
        globals(),
        bundle_path=_objc.pathForFramework(
            u'/System/Library/Frameworks/Foundation.framework',
        ),
    )

def _initialize():
    import sys, os
    if 'PYOBJCFRAMEWORKS' in os.environ:
        paths = os.environ['PYOBJCFRAMEWORKS'].split(":")
        count = 0
        for path in paths:
            bundle = NSBundle.bundleWithPath_(path)
            bundle.principalClass()
            sys.path.insert(count, str(bundle.resourcePath()))
            count = count + 1

            initPath = bundle.pathForResource_ofType_( "Init", "py")
            if initPath:
                execfile(initPath, globals(), locals())

    try:
        NSDecimal
    except NameError:
        pass
    else:
        NSClassFromString('OC_PythonObject').depythonifyTable().append(
            (NSDecimal, NSDecimalNumber.decimalNumberWithDecimal_)
        )

_initialize()

import protocols  # no need to export these, just register with PyObjC

#
# (informal) protocols eported for b/w compatibility
#
from protocols import NSConnectionDelegateMethods, \
                      NSDistantObjectRequestMethods, \
                      NSCopyLinkMoveHandler, NSKeyedArchiverDelegate, \
                      NSKeyedUnarchiverDelegate, NSNetServiceDelegateMethods, \
                      NSNetServiceBrowserDelegateMethods, NSPortDelegateMethods
