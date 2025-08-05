from PyObjCTools.TestSupport import TestCase

import ARKit


class TestAnchor(TestCase):
    def test_types(self):
        # Hidden types (ObjC typedef is a NSObjecT<...>)
        # self.assertIsSubclass(ARKit.ar_anchor_t, objc.objc_object)
        # self.assertIsSubclass(ARKit.ar_trackable_anchor_t, objc.objc_object)
        pass

    def test_functions(self):
        # SIMD types
        # ARKit.ar_anchor_get_origin_from_anchor_transform
        self.assertArgIsOut(ARKit.ar_anchor_get_identifier, 1)
        ARKit.ar_anchor_get_timestamp
        ARKit.ar_trackable_anchor_is_tracked
