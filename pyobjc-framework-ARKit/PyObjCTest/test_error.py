from PyObjCTools.TestSupport import TestCase

import ARKit


class TestError(TestCase):
    def test_types(self):
        # This is not a concrete type in ObjC:
        # self.assertIsSubclass(ARKit.ar_error_t, objc.objc_object)
        pass

    def test_constants(self):
        self.assertIsInstance(ARKit.ar_error_domain, str)

    def test_functions(self):
        ARKit.ar_error_get_error_code
        self.assertResultIsCFRetained(ARKit.ar_error_copy_cf_error)
