import sys
from PyObjCTest.fnd import NSNumber
from PyObjCTools.TestSupport import *
from objc._pythonify import OC_PythonLong, OC_PythonFloat
if sys.version_info[0] == 2:
    from objc._pythonify import OC_PythonInt
import pickle

try:
    import cPickle
except ImportError:
    cPickle = None

try:
    long
except NameError:
    # Python 3.x
    long = int

class TestPickleNumber (TestCase):

    def testPickleInt(self):
        if sys.version_info[0] == 2:
            number_type = OC_PythonInt
        else:
            number_type = OC_PythonLong
        v = NSNumber.numberWithInt_(42)
        self.assertIsInstance(v, number_type)

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEqual(v2, v)
        self.assertIsNotInstance(v2, number_type)
        self.assertIsInstance(v2, int)

        if cPickle is not None:
            # Then C pickle
            s = cPickle.dumps(v)
            v2 = cPickle.loads(s)
            self.assertEqual(v2, v)
            self.assertIsNotInstance(v2, number_type)
            self.assertIsInstance(v2, int)

    def testPickleFloat(self):
        v = NSNumber.numberWithFloat_(42)
        self.assertIsInstance(v, OC_PythonFloat)

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEqual(v2, v)
        self.assertIsNotInstance(v2, OC_PythonFloat)
        self.assertIsInstance(v2, float)

        if cPickle is not None:
            # Then C pickle
            s = cPickle.dumps(v)
            v2 = cPickle.loads(s)
            self.assertEqual(v2, v)
            self.assertIsNotInstance(v2, OC_PythonFloat)
            self.assertIsInstance(v2, float)

    @onlyOn32Bit
    def testPickleLongLong(self):
        v = NSNumber.numberWithLongLong_(sys.maxsize + 3)
        self.assertIsInstance(v, OC_PythonLong)

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEqual(v2, v)
        self.assertIsNotInstance(v2, OC_PythonLong)
        self.assertIsInstance(v2, long)

        if cPickle is not None:
            # Then C pickle
            s = cPickle.dumps(v)
            v2 = cPickle.loads(s)
            self.assertEqual(v2, v)
            self.assertIsNotInstance(v2, OC_PythonLong)
            self.assertIsInstance(v2, long)




if __name__ == "__main__":
    main()
