import unittest
import objc

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

class TestPosing(unittest.TestCase):
    def testPosing(self):
        class Level1Class(NSObject):
            __slots__ = ()  # Don't add instance variables, not even __dict__
            def description(self):
                return "<<subdescrip>> " + super.description()

        Level1Class.poseAsClass_(NSObject)
        
        obj = NSObject.new()



def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPosing))
    return suite

if __name__ == '__main__':
    unittest.main()
