import unittest
import objc

# Most useful systems will at least have 'NSObject'.
#NSObject = objc.lookUpClass('NSObject')

# Use a class that isn't used in the rest of the testsuite,
# should write a native class for this!
BaseClass = objc.lookUpClass('NSPortCoder')

class TestPosing(unittest.TestCase):
    def testPosing(self):
        class PoseClass(BaseClass):
            __slots__ = ()  # Don't add instance variables, not even __dict__
            def description(self):
                return "<<subdescrip>> " + super.description()

        PoseClass.poseAsClass_(BaseClass)
        
        obj = BaseClass.new()

if __name__ == '__main__':
    unittest.main()
