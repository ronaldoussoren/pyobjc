import objc
from PyObjCTest.properties import OCPropertyDefinitions
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestPropertiesForClass(TestCase):
    @min_os_level("10.6")
    def testBasic(self):
        props = objc.propertiesForClass(OCPropertyDefinitions)
        self.assertIsInstance(props, list)

        p = self.get_prop(props, "prop1")
        self.assertEqual(p["name"], "prop1")
        self.assertIsInstance(p["raw_attr"], bytes)
        self.assertEqual(p["typestr"], objc._C_INT)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop2")
        self.assertEqual(p["name"], "prop2")
        self.assertEqual(p["typestr"], objc._C_FLT)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop3")
        self.assertEqual(p["name"], "prop3")
        self.assertEqual(p["typestr"], b"{s=ic}")
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop4")
        self.assertEqual(p["name"], "prop4")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop5")
        self.assertEqual(p["name"], "prop5")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertTrue(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop6")
        self.assertEqual(p["name"], "prop6")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop7")
        self.assertEqual(p["name"], "prop7")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop8")
        self.assertEqual(p["name"], "prop8")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertTrue(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop9")
        self.assertEqual(p["name"], "prop9")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertTrue(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertFalse(p.get("dynamic", False))

        p = self.get_prop(props, "prop10")
        self.assertEqual(p["name"], "prop10")
        self.assertEqual(p["typestr"], b"{s=ic}")
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("dynamic", False))

        # This seems to be a bug in the objc runtime:
        # self.assertTrue(p.get('nonatomic', False))

        p = self.get_prop(props, "prop11")
        self.assertEqual(p["name"], "prop11")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertFalse(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertFalse(p.get("nonatomic", False))
        self.assertEqual(p.get("setter"), b"propSetter:")
        self.assertEqual(p.get("getter"), b"propGetter")
        self.assertFalse(p.get("dynamic", False))

        # p = self.get_prop(props, "prop12")
        # self.assertEqual(p['name'], "prop12")
        # self.assertEqual(p['typestr'], objc._C_ID)
        # self.assertFalse(p.get('readonly', False))
        # self.assertFalse(p.get('copy', False))
        # self.assertTrue(p.get('retain', False))
        # self.assertTrue(p.get('nonatomic', False))
        # self.assertFalse(p.get('dynamic', False))

        p = self.get_prop(props, "prop13")
        self.assertEqual(p["name"], "prop13")
        self.assertEqual(p["typestr"], objc._C_ID)
        self.assertFalse(p.get("readonly", False))
        self.assertTrue(p.get("copy", False))
        self.assertFalse(p.get("retain", False))
        self.assertTrue(p.get("dynamic", False))

    def get_prop(self, lst, name):
        for item in lst:
            if item["name"] == name:
                return item
        self.fail(f"property not found: {name}")
