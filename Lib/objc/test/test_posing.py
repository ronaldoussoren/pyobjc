import unittest
import objc

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

class TestPosing(unittest.TestCase):
    def testPosing(self):
        class PoseClass(NSObject):
            __slots__ = ()  # Don't add instance variables, not even __dict__
            def description(self):
                return "<<subdescrip>> " + super.description()

        PoseClass.poseAsClass_(NSObject)
        
        obj = NSObject.new()

if __name__ == '__main__':
    unittest.main()
