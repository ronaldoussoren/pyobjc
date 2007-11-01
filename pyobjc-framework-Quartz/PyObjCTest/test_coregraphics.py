'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
from Quartz import CoreGraphics

class TestCoreGraphics (unittest.TestCase):
    def testClasses(self):
        pass
        # self.assert_( hasattr(CoreGraphics, 'CLASSNAME') )
        # self.assert_( isinstance(CoreGraphics.CLASSNAME, objc.objc_class) )
        # Tollfree CF-type:
        # self.assert_( hasattr(CoreGraphics, 'CLASSNAMERef') )
        # self.assert_( CoreGraphics.CLASSNAMERef is CoreGraphics.CLASSNAME )

        # Not-tollfree CF-type:
        # self.assert_( hasattr(CoreGraphics, 'CLASSNAMERef') )
        # self.assert_( issubclass(CoreGraphics.CLASSNAMERef, objc.lookUpClass('NSCFType')) )
        # self.assert_( CoreGraphics.CLASSNAMERef is not objc.lookUpClass('NSCFType') )

    def testValues(self):
        # Integer values:
        self.assert_( hasattr(CoreGraphics, 'kCGNullWindowID') )
        self.assert_( isinstance(CoreGraphics.kCGNullWindowID, (int, long)) )
        self.assertEquals(CoreGraphics.kCGNullWindowID, 0)

        self.assert_( hasattr(CoreGraphics, 'kCGCaptureNoFill') )
        self.assert_( isinstance(CoreGraphics.kCGCaptureNoFill, (int, long)) )
        self.assertEquals(CoreGraphics.kCGCaptureNoFill, 1)

        self.assert_( hasattr(CoreGraphics, 'kCGErrorFailure') )
        self.assert_( isinstance(CoreGraphics.kCGErrorFailure, (int, long)) )
        self.assertEquals(CoreGraphics.kCGErrorFailure, 1000)
        
        self.assert_( hasattr(CoreGraphics, 'kCGEventFlagMaskControl') )
        self.assert_( isinstance(CoreGraphics.kCGEventFlagMaskControl, (int, long)) )
        
        self.assert_( hasattr(CoreGraphics, 'kCGAnyInputEventType') )
        self.assert_( isinstance(CoreGraphics.kCGAnyInputEventType, (int, long)) )

        self.assert_( hasattr(CoreGraphics, 'CGRectMaxXEdge') )
        self.assert_( isinstance(CoreGraphics.CGRectMaxXEdge, (int, long)) )

        self.assert_( hasattr(CoreGraphics, 'kCGBitmapByteOrder16Host') )
        self.assert_( isinstance(CoreGraphics.kCGBitmapByteOrder16Host, (int, long)) )

        self.assert_( hasattr(CoreGraphics, 'kCGEventFilterMaskPermitAllEvents') )
        self.assert_( isinstance(CoreGraphics.kCGEventFilterMaskPermitAllEvents, (int, long)) )

        self.assert_( hasattr(CoreGraphics, 'kCGMaxDisplayReservationInterval') )
        self.assert_( isinstance(CoreGraphics.kCGMaxDisplayReservationInterval, float) )
        self.assertEquals(CoreGraphics.kCGMaxDisplayReservationInterval, 15.0)


        # This is a "constant" that actually expands into a function call. It is unclear to me if
        # the return value of that function is constant over the live of the program, but it most likely
        # isn't.
        self.assert_( not hasattr(CoreGraphics, 'kCGDirectMainDisplay') )
        self.assert_( not hasattr(CoreGraphics, 'kCGDockWindowLevel') )

        # String values:
        self.assert_( hasattr(CoreGraphics, 'kCGDisplayHeight') )
        self.assert_( isinstance(CoreGraphics.kCGDisplayHeight, (str, unicode)) )
        self.assertEquals(CoreGraphics.kCGDisplayHeight, u'Height')

        self.assert_( hasattr(CoreGraphics, 'kCGNotifyEventTapAdded') )
        self.assert_( isinstance(CoreGraphics.kCGNotifyEventTapAdded, (str, unicode)) )
        self.assertEquals(CoreGraphics.kCGNotifyEventTapAdded, 'com.apple.coregraphics.eventTapAdded')


    def testVariables(self):
        self.assert_( hasattr(CoreGraphics, 'kCGColorSpaceGenericGray') )
        self.assert_( isinstance(CoreGraphics.kCGColorSpaceGenericGray, unicode) )

        self.assert_( hasattr(CoreGraphics, 'CGAffineTransform') )
        tf = CoreGraphics.CGAffineTransform
        self.assert_( hasattr(CoreGraphics, 'CGAffineTransformIdentity') )
        self.assert_( isinstance(CoreGraphics.CGAffineTransformIdentity, tf) )

    def testFunctions(self):
        self.assert_( hasattr(CoreGraphics, 'CGPointApplyAffineTransform') )
        self.assert_( hasattr(CoreGraphics, 'CGBitmapContextCreate') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(CoreGraphics, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(CoreGraphics, 'protocols') )

        # self.assert_( hasattr(CoreGraphics.protocols, 'PROTOCOL') )

    def testFunctions(self):
        self.assert_( hasattr(CoreGraphics, 'CGPointMake') )
        self.assert_( hasattr(CoreGraphics, 'CGRectIntersectsRect') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(CoreGraphics, 'OPAQUE') )

    def testProtocols(self):
        # Use this to test if informal protocols  are present
        pass

        # self.assert_( hasattr(CoreGraphics, 'protocols') )

        # self.assert_( hasattr(CoreGraphics.protocols, 'PROTOCOL') )
        # self.assert_( isinstance(CoreGraphics.protocols.PROTOCOL, objc.informal_protocol) )

    def test_structs(self):
        # Use this to test struct wrappers
        pass

        self.assert_( hasattr(CoreGraphics, 'CGSize') )
        o = CoreGraphics.CGSize()
        self.assert_( hasattr(o, 'width') )

        self.assert_( hasattr(CoreGraphics, 'CGSizeZero') )
        self.assert_( isinstance(CoreGraphics.CGSizeZero, CoreGraphics.CGSize) )



if __name__ == "__main__":
    unittest.main()

