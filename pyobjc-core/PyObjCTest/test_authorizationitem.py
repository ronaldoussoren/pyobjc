import objc
from PyObjCTools.TestSupport import TestCase
from .authorizationitem import OC_Authorization

authorization_typestr = b"{_AuthorizationItem=^cL^vI}"
objc.registerMetaDataForSelector(
    b"OC_Authorization",
    b"dictWithAuthorizationItem:",
    {
        "arguments": {
            2 + 0: {"type_modifier": objc._C_IN, "type": b"^" + authorization_typestr}
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_Authorization",
    b"getAuthorizationItem:kind:",
    {
        "arguments": {
            2 + 0: {"type_modifier": objc._C_OUT, "type": b"^" + authorization_typestr}
        }
    },
)


class TestAuthorizationItemStruct(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.AuthorizationItem = objc.createStructType(
            "Security.AuthorizationItem",
            authorization_typestr,
            ["name", "valueLength", "value", "flags"],
        )

    @classmethod
    def tearDownClass(self):
        objc._dropStructType(authorization_typestr.decode())

        # This will always fail, added to trigger the exception...
        try:
            objc._dropStructType(authorization_typestr)
        except KeyError:
            pass

    def test_struct(self):
        x = self.AuthorizationItem(b"username", 6, b"ronald", 0)
        self.assertEqual(x.name, b"username")
        self.assertEqual(x.value, b"ronald")
        self.assertEqual(x.valueLength, 6)
        self.assertEqual(x.flags, 0)

    def test_methods(self):
        self.assertArgHasType(
            OC_Authorization.dictWithAuthorizationItem_,
            0,
            b"n^{_AuthorizationItem=^cL^vI}",
        )

    def test_to_objc_struct(self):
        x = self.AuthorizationItem(b"username", 6, b"ronaldo", 0)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], "username")
        self.assertEqual(r["value"], b"ronald")
        self.assertEqual(r["flags"], 0)

        x = self.AuthorizationItem(b"username", 42, None, 99)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], "username")
        self.assertEqual(r["value"], None)
        self.assertEqual(r["valueLength"], 42)
        self.assertEqual(r["flags"], 99)

        x = self.AuthorizationItem(None, 6, b"ronaldo", 0)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], None)
        self.assertEqual(r["value"], b"ronald")
        self.assertEqual(r["flags"], 0)

        x = self.AuthorizationItem("username", 6, b"ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.name should be a byte string, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", 6, "ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.value should be a byte string, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", 10, b"ronaldo", 0)
        with self.assertRaisesRegex(
            ValueError,
            "AuthorizationItem.value too small; expecting at least 10 bytes, got 7",
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", "6", b"ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.valueLength should be an integer, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", 6, b"ronaldo", "0")
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.flags should be an integer, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", 2**65, b"ronaldo", 0)
        with self.assertRaises(OverflowError):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = self.AuthorizationItem(b"username", 6, b"ronaldo", 2**65)
        with self.assertRaises(OverflowError):
            OC_Authorization.dictWithAuthorizationItem_(x)

    def test_from_objc(self):
        self.assertArgIsOut(OC_Authorization.getAuthorizationItem_kind_, 0)
        x = OC_Authorization.getAuthorizationItem_kind_(None, 0)
        self.assertEqual(x.name, None)
        self.assertEqual(x.value, None)
        self.assertEqual(x.valueLength, 32)
        self.assertEqual(x.flags, 0)

        x = OC_Authorization.getAuthorizationItem_kind_(None, 1)
        self.assertEqual(x.name, b"name-value")
        self.assertEqual(x.value, b"value buffer")
        self.assertEqual(x.valueLength, 12)
        self.assertEqual(x.flags, 14356)


class TestAuthorizationItemTuple(TestCase):
    def test_to_objc_tuple(self):
        x = (b"username", 6, b"ronaldo", 0)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], "username")
        self.assertEqual(r["value"], b"ronald")
        self.assertEqual(r["flags"], 0)

        x = (b"username", 42, None, 99)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], "username")
        self.assertEqual(r["value"], None)
        self.assertEqual(r["valueLength"], 42)
        self.assertEqual(r["flags"], 99)

        x = (None, 6, b"ronaldo", 0)
        r = OC_Authorization.dictWithAuthorizationItem_(x)
        self.assertEqual(r["name"], None)
        self.assertEqual(r["value"], b"ronald")
        self.assertEqual(r["flags"], 0)

        x = ("username", 6, b"ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.name should be a byte string, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 6, "ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.value should be a byte string, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 10, b"ronaldo", 0)
        with self.assertRaisesRegex(
            ValueError,
            "AuthorizationItem.value too small; expecting at least 10 bytes, got 7",
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", "6", b"ronaldo", 0)
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.valueLength should be an integer, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 6, b"ronaldo", "0")
        with self.assertRaisesRegex(
            TypeError, "AuthorizationItem.flags should be an integer, not str"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 2**65, b"ronaldo", 0)
        with self.assertRaises(OverflowError):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 6, b"ronaldo", 2**65)
        with self.assertRaises(OverflowError):
            OC_Authorization.dictWithAuthorizationItem_(x)

        x = (b"username", 6, b"ronaldo", 0, 10)
        with self.assertRaisesRegex(
            ValueError, "depythonifying struct of 4 members, got tuple of 5"
        ):
            OC_Authorization.dictWithAuthorizationItem_(x)

        with self.assertRaisesRegex(
            TypeError, "depythonifying struct, got no sequence"
        ):
            OC_Authorization.dictWithAuthorizationItem_(object())

    def test_from_objc(self):
        self.assertArgIsOut(OC_Authorization.getAuthorizationItem_kind_, 0)
        x = OC_Authorization.getAuthorizationItem_kind_(None, 0)
        self.assertEqual(x, (None, 32, None, 0))

        x = OC_Authorization.getAuthorizationItem_kind_(None, 1)
        self.assertEqual(x, (b"name-value", 12, b"value buffer", 14356))
