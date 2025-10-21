from PyObjCTools.TestSupport import TestCase

import ARKit  # noqa: F401


class TestStringsCollection(TestCase):
    def test_types(self):
        # Not a concrete type in ObjC:
        # self.assertIsSubclass(ARKit.ar_strings_t, objc.objc_object)
        pass
