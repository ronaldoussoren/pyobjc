'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import Foundation
import os

class TestFoundation (TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(Foundation, 'CLASSNAME') )
        # self.assert_( isinstance(Foundation.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(Foundation, 'CLASSNAMERef') )
        # self.assert_( Foundation.CLASSNAMERef is Foundation.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(Foundation, 'CLASSNAMERef') )
        # self.assert_( issubclass(Foundation.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( Foundation.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        self.assert_( hasattr(Foundation, 'NSTimeIntervalSince1970') )
        self.assert_( isinstance(Foundation.NSTimeIntervalSince1970, float) )
        self.assertEquals(Foundation.NSTimeIntervalSince1970, 978307200.0)

	if os.uname()[2] < '9.':
		self.assert_( hasattr(Foundation, 'NSMaximumStringLength') )
		self.assert_( isinstance(Foundation.NSMaximumStringLength, (int, long)) )
        self.assert_( hasattr(Foundation, 'NSURLResponseUnknownLength') )
        self.assert_( isinstance(Foundation.NSURLResponseUnknownLength, (int, long)) )

    def testVariables(self):
        # Use this to test for global variables, (NSString*'s and the like)
        pass

        # self.assert_( hasattr(Foundation, 'CONSTANT') )
        # self.assert_( isinstance(Foundation.CONSTANT, unicode) )

    def testFunctions(self):
        self.assert_( hasattr(Foundation, 'NSStringFromSelector') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(Foundation, 'OPAQUE') )

    def testProtocols(self):
        self.assert_( hasattr(Foundation, 'protocols') )

        for nm in [
                'NSArchiverCallback',
                'NSClassDescriptionPrimitives',
                'NSComparisonMethods',
                'NSConnectionDelegateMethods',
                'NSCopyLinkMoveHandler',
                'NSDelayedPerforming',
                'NSDistantObjectRequestMethods',
                'NSDistributedObjects',
                'NSErrorRecoveryAttempting',
                'NSKeyValueCoding',
                'NSKeyValueObserverNotification',
                'NSKeyValueObserverRegistration',
                'NSKeyValueObserving',
                'NSKeyValueObservingCustomization',
                'NSKeyedArchiverDelegate',
                'NSKeyedArchiverObjectSubstitution',
            ]:

            self.assert_( hasattr(Foundation.protocols, nm), 'protocol %s'%(nm,))
            self.assert_( isinstance(getattr(Foundation.protocols, nm), objc.informal_protocol) )

    def test_structs(self):
        self.assert_( hasattr(Foundation, 'NSPoint') )
        o = Foundation.NSPoint()
        self.assert_( hasattr(o, 'x') )
        self.assert_( hasattr(o, 'y') )

        self.assert_( hasattr(Foundation, 'NSSize') )
        o = Foundation.NSSize()
        self.assert_( hasattr(o, 'width') )
        self.assert_( hasattr(o, 'height') )

        self.assert_( hasattr(Foundation, 'NSRange') )
        o = Foundation.NSRange()
        self.assert_( hasattr(o, 'location') )
        self.assert_( hasattr(o, 'length') )

        self.assert_( hasattr(Foundation, 'NSRect') )
        o = Foundation.NSRect()
        self.assert_( hasattr(o, 'origin') )
        self.assert_( hasattr(o, 'size') )
        self.assert_( isinstance(o.origin, Foundation.NSPoint) )
        self.assert_( isinstance(o.size, Foundation.NSSize) )

        self.assert_( hasattr(Foundation, 'NSAffineTransformStruct') )
        o = Foundation.NSAffineTransformStruct()
        self.assert_( hasattr(o, 'm11') )
        self.assert_( hasattr(o, 'm12') )
        self.assert_( hasattr(o, 'm21') )
        self.assert_( hasattr(o, 'm22') )
        self.assert_( hasattr(o, 'tX') )
        self.assert_( hasattr(o, 'tY') )


if __name__ == "__main__":
    main()

