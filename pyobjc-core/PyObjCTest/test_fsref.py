from PyObjCTools.TestSupport import *
import objc

from PyObjCTest.fsref import *

"""
@interface OC_TestFSRefHelper : NSObject
{
        }

-(FSRef)fsrefForPath:(NSString*)path;
-(NSString*)pathForFSRef:(in FSRef *)fsref;
-(void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path;
-(NSString*)stringForFSRef:(FSRef)fsref;



@end
"""



class TestFSRef (TestCase):
    def testBasicInterface(self):
        self.assertArgIsIn(OC_TestFSRefHelper.pathForFSRef_, 0)
        self.assertArgIsOut(OC_TestFSRefHelper.getFSRef_forPath_, 0)

    def testResult(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.assertIsInstance(ref, objc.FSRef)

        self.assertIsInstance(ref.data, bytes)
        self.assertIsInstance(ref.as_pathname(), unicode)

        try:
            from Carbon.File import FSRef

        except ImportError:
            pass

        else:
            self.assertIsInstance(ref.as_carbon(), FSRef)

    def testArg(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, u"/Library")

    def testInput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.assertIsInstance(ref, objc.FSRef)

        p = o.pathForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, u"/Library")

    def testOutput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.getFSRef_forPath_(None, u"/Library")
        self.assertIsInstance(ref, objc.FSRef)

        # Verify the fsref contents:
        p = o.stringForFSRef_(ref)
        self.assertIsInstance(p, unicode)
        self.assertEqual(p, u"/Library")


if __name__ == "__main__":
    main()
