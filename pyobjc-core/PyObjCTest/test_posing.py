from __future__ import unicode_literals
from PyObjCTools.TestSupport import *
import objc
import sys

# Most useful systems will at least have 'NSObject'.
#NSObject = objc.lookUpClass('NSObject')

# Use a class that isn't used in the rest of the testsuite,
# should write a native class for this!
BaseName = 'NSAttributedString'
BaseClass = objc.lookUpClass(BaseName)

if sys.maxsize >= 2 ** 32:
    # -poseAsClass: is not supported in 64-bit mode (the functionality is
    # not present in the 64-bit runtime and will never be because it
    # conflicts with new functionality such as non-fragile class layouts)
    pass

else:
    class TestPosing(TestCase):
        def testPosing(self):

            class PoseClass(BaseClass):
                __slots__ = ()  # Don't add instance variables, not even __dict__
                def testPosingMethod(self):
                    return "<PoseClass instance>"


            PoseClass.poseAsClass_(BaseClass)

            # BaseClass still refers to the old class, if we look it up again
            # we get to see the new value. There's not much we can do about that.
            obj = objc.lookUpClass(BaseName).new()
            self.assertEqual(obj.testPosingMethod(), "<PoseClass instance>")

            # XXX: next assertion fails because the runtime seems to copy the
            # original class.
            #self.assertIsInstance(obj, PoseClass)
            self.assertNotEqual(BaseClass.__name__, BaseName)
            self.assertEqual(PoseClass.__name__, BaseName)
            del obj



if __name__ == '__main__':
    main()
