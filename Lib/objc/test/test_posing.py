import unittest
import objc

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

class TestPosing(unittest.TestCase):
    def testPosing(self):
        class Level1Class(NSObject):
            def description(self):
                return "<<subdescrip>> " + super.description()

        Level1Class.poseAsClass_(NSObject)
        
        obj = NSObject.new()

        print obj.description


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPosing))
    return suite

if __name__ == '__main__':
    unittest.main()
