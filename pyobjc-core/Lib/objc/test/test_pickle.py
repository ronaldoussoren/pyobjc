from objc.test.fnd import NSNumber
import objc.test
from objc._pythonify import OC_PythonInt, OC_PythonFloat, OC_PythonLong
import pickle
import cPickle
import sys

class TestPickleNumber (objc.test.TestCase):

    def testPickleInt(self):
        v = NSNumber.numberWithInt_(42)
        self.assert_(isinstance(v, OC_PythonInt))

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonInt))
        self.assert_(isinstance(v2, int))

        # Then C pickle
        s = cPickle.dumps(v)
        v2 = cPickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonInt))
        self.assert_(isinstance(v2, int))

    def testPickleFloat(self):
        v = NSNumber.numberWithFloat_(42)
        self.assert_(isinstance(v, OC_PythonFloat))

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonFloat))
        self.assert_(isinstance(v2, float))

        # Then C pickle
        s = cPickle.dumps(v)
        v2 = cPickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonFloat))
        self.assert_(isinstance(v2, float))

    def testPickleLongLong(self):
        if sys.maxint > 2 ** 32:
            return

        v = NSNumber.numberWithLongLong_(sys.maxint + 3)
        self.assert_(isinstance(v, OC_PythonLong))

        # First python pickle
        s = pickle.dumps(v)
        v2 = pickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonLong))
        self.assert_(isinstance(v2, long))

        # Then C pickle
        s = cPickle.dumps(v)
        v2 = cPickle.loads(s)
        self.assertEquals(v2, v)
        self.assert_(not isinstance(v2, OC_PythonLong))
        self.assert_(isinstance(v2, long))




if __name__ == "__main__":
    objc.test.main()
