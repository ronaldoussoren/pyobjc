import unittest
import objc

# Most useful systems will at least have 'NSObject'.
#NSObject = objc.lookUpClass('NSObject')

# Use a class that isn't used in the rest of the testsuite,
# should write a native class for this! NSPortCoder
BaseName = 'NSPortCoder'
BaseClass = objc.lookUpClass(BaseName)

class TestPosing(unittest.TestCase):
    def testPosing(self):
        class PoseClass(BaseClass):
            __slots__ = ()  # Don't add instance variables, not even __dict__
            def testPosingMethod(self):
                return "<PoseClass instance>"

        PoseClass.poseAsClass_(BaseClass)
       
        # Whoops, this is a problem: We keep referencing the old class!
        #obj = objc.lookUpClass(BaseName).new()
        obj = objc.runtime.__getattr__(BaseName).alloc().init()
        self.assert_(isinstance(obj, PoseClass))
        self.assertEquals(obj.testPosingMethod(), "<PoseClass instance>")
        del obj



if __name__ == '__main__':
    unittest.main()
