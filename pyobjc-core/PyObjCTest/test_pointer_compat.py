from PyObjCTools.TestSupport import *
import objc
import ctypes


class TestProxySupport (TestCase):
    def test_cobject_roundtrip(self):
        arr = objc.lookUpClass('NSArray').array()

        p = arr.__cobject__()
        self.assertEqual(type(p).__name__, "PyCapsule")
        self.assertIn("objc.__object__", repr(p))
        # Note: 

        v = objc.objc_object(cobject=p)
        self.assertIs(v, arr)

    def test_voidp_roundtrip(self):
        arr = objc.lookUpClass('NSArray').array()

        p = arr.__c_void_p__()
        self.assertIsInstance(p, ctypes.c_void_p)
        self.assertEqual(p.value, objc.pyobjc_id(arr))

        v = objc.objc_object(c_void_p=p)
        self.assertIs(v, arr)

    @expectedFailure
    def test_missing(self):
        # Add tests simular to the ones above, but
        # with objects created outside of PyObjC
        self.fail()

if __name__ == "__main__":
    main()
