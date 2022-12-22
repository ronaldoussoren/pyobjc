from PyObjCTools.TestSupport import TestCase

from objc import simd
import objc


def calc_xyzw():
    result = set(BASE_ATTR)

    for idx in range(4):
        for n in range(2, 5):
            result.add("".join(BASE_ATTR[idx : idx + n]))

    return result


BASE_ATTR = ("x", "y", "z", "w")
XYZW_ATTR = calc_xyzw()


class TestSIMDVectorTypes(TestCase):
    def assert_has_xyzw(self, value, nelem):
        """
        Assert that the correct "xyzw" properties
        are presesnt for a SIMD type with 'nelem'
        elements.
        """
        if nelem > 4:
            missing = XYZW_ATTR
            expected = set()

        else:
            missing = {x for x in XYZW_ATTR if any(y in x for y in BASE_ATTR[nelem:])}
            expected = XYZW_ATTR - missing

        for n in missing:
            self.assertNotHasAttr(value, n)

        for n in expected:
            self.assertHasAttr(value, n)

    def assert_vector_type(self, vtype, etype, nelem, is_signed, typestr):
        a = vtype()
        self.assertEqual(len(a), nelem)
        self.assertTrue(all(a[i] == etype() for i in range(nelem)))
        self.assert_has_xyzw(a, nelem)

        a = vtype(etype(42))
        self.assertEqual(len(a), nelem)
        self.assertTrue(all(a[i] == etype(42) for i in range(nelem)))
        self.assertTrue(all(isinstance(a[i], etype) for i in range(nelem)))

        if nelem != 2:
            with self.assertRaises(ValueError):
                vtype(*range(nelem - 1))

        with self.assertRaises(ValueError):
            vtype(*range(nelem + 1))

        a = vtype(*(etype(n) for n in range(nelem)))
        self.assertTrue(all(a[i] == etype(i) for i in range(nelem)))

        a[0] = a[1]
        self.assertEqual(a[0], a[1])

        a[0] = 42
        self.assertEqual(a[0], etype(42))
        self.assertIsInstance(a[0], etype)

        a = vtype(*(etype(n) for n in range(nelem)))
        self.assertEqual(a.x, etype(0))
        self.assertEqual(a.y, etype(1))
        self.assertEqual(a.xy.as_tuple(), (etype(0), etype(1)))

        if nelem >= 3:
            self.assertEqual(a.z, etype(2))
            self.assertEqual(a.yz.as_tuple(), (etype(1), etype(2)))
            self.assertEqual(a.xyz.as_tuple(), (etype(0), etype(1), etype(2)))

        if nelem == 4:
            self.assertEqual(a.w, etype(3))
            self.assertEqual(a.zw.as_tuple(), (etype(2), etype(3)))
            self.assertEqual(a.yzw.as_tuple(), (etype(1), etype(2), etype(3)))
            self.assertEqual(
                a.xyzw.as_tuple(), (etype(0), etype(1), etype(2), etype(3))
            )
            self.assertIsNot(a.xyzw, a)

        self.assertEqual(abs(a), abs(a))
        if is_signed:
            b = vtype(*(-e for e in a.as_tuple()))
            self.assertNotEqual(a, b)
            self.assertEqual(a, abs(b))

            c = -a
            self.assertEqual(b, c)

            c = +a
            self.assertEqual(c, a)
            self.assertIsNot(c, a)

        else:
            with self.assertRaises(TypeError):
                -a

            with self.assertRaises(TypeError):
                +a

        a = vtype(*range(1, nelem + 1))
        b = vtype(*(2 * n for n in range(1, nelem + 1)))

        c = a * b
        self.assertIsInstance(c, vtype)
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] * b[i])

        c = a * 3
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] * 3)

        c = 3 * a
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] * 3)

        c = a + b
        self.assertIsInstance(c, vtype)
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] + b[i])

        c = a + 3
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] + 3)

        c = 3 + a
        for i in range(len(c)):
            self.assertEqual(c[i], a[i] + 3)

        c = a @ b
        self.assertEqual(c, sum(n * m for n, m in zip(a.as_tuple(), b.as_tuple())))

        with self.assertRaises(TypeError):
            c = a @ 1

        with self.assertRaises(TypeError):
            c = 1 @ a

        a1 = vtype(*range(1, nelem + 1))
        a2 = vtype(*range(1, nelem + 1))
        b1 = vtype(*(2 * n for n in range(1, nelem + 1)))

        self.assertTrue(a1 == a2)
        self.assertFalse(a1 == b1)

        self.assertFalse(a1 != a2)
        self.assertTrue(a1 != b1)

        self.assertFalse(a1 < a2)
        self.assertTrue(a1 < b1)

        self.assertTrue(a1 <= a2)
        self.assertFalse(b1 <= a2)

        self.assertFalse(a1 > a2)
        self.assertTrue(b1 > a1)

        self.assertTrue(a1 >= a2)
        self.assertFalse(a1 >= b1)

        a = vtype(*range(nelem))
        b = vtype(*range(nelem))
        b[nelem - 1] = 0

        self.assertFalse(a == b)
        self.assertTrue(a != b)
        self.assertTrue(a > b)
        self.assertTrue(a >= b)
        self.assertFalse(b > a)
        self.assertFalse(b >= a)
        self.assertTrue(b < a)
        self.assertTrue(b <= a)
        self.assertFalse(a < b)
        self.assertFalse(a <= b)

        self.assertEqual(
            vtype.__typestr__,
            b"".join([objc._C_VECTOR_B, b"%d" % (nelem,), typestr, objc._C_VECTOR_E]),
        )

        with self.assertRaises(TypeError):
            a["a"] = 3

        with self.assertRaises(TypeError):
            a + "a"

        with self.assertRaises(TypeError):
            "a" + a

        with self.assertRaises(TypeError):
            a - "a"

        with self.assertRaises(TypeError):
            "a" - a

        with self.assertRaises(TypeError):
            a * "a"

        with self.assertRaises(TypeError):
            "a" * a

        with self.assertRaises(TypeError):
            a / "a"

        with self.assertRaises(TypeError):
            "a" / a

        with self.assertRaises(TypeError):
            "a" < a  # noqa: B015

        with self.assertRaises(TypeError):
            a < "a"  # noqa: B015

        with self.assertRaises(TypeError):
            "a" <= a  # noqa: B015

        with self.assertRaises(TypeError):
            a <= "a"  # noqa: B015

        with self.assertRaises(TypeError):
            "a" > a  # noqa: B015

        with self.assertRaises(TypeError):
            a > "a"  # noqa: B015

        with self.assertRaises(TypeError):
            "a" >= a  # noqa: B015

        with self.assertRaises(TypeError):
            a >= "a"  # noqa: B015

        self.assertFalse(a == "a")
        self.assertTrue(a != "a")

    def test_vector_uchar16(self):
        a = simd.vector_uchar16()
        self.assertEqual(len(a), 16)
        self.assertTrue(all(a[i] == 0 for i in range(16)))

        a = simd.vector_uchar16(42)
        self.assertEqual(len(a), 16)
        self.assertTrue(all(a[i] == 42 for i in range(16)))

        with self.assertRaises(ValueError):
            simd.vector_uchar16(1, 2, 3, 4)

        with self.assertRaises(ValueError):
            simd.vector_uchar16(*range(17))

        a = simd.vector_uchar16(*range(16))
        self.assertTrue(all(a[i] == i for i in range(16)))

        self.assert_has_xyzw(a, 16)

        a[0] = 4
        self.assertEqual(a[0], 4)

        with self.assertRaises(TypeError):
            a[0] = 4.5

        self.assertEqual(
            simd.vector_uchar16.__typestr__,
            b"".join([objc._C_VECTOR_B, b"16", objc._C_UCHR, objc._C_VECTOR_E]),
        )

    def test_vector_short2(self):
        self.assert_vector_type(simd.vector_short2, int, 2, True, objc._C_SHT)

    def test_vector_ushort2(self):
        self.assert_vector_type(simd.vector_ushort2, int, 2, False, objc._C_USHT)

    def test_vector_ushort4(self):
        self.assert_vector_type(simd.vector_ushort4, int, 4, False, objc._C_USHT)

    def test_vector_int2(self):
        self.assert_vector_type(simd.vector_int2, int, 2, True, objc._C_INT)

    def test_vector_uint3(self):
        self.assert_vector_type(simd.vector_uint3, int, 3, False, objc._C_UINT)

    def test_vector_float2(self):
        self.assert_vector_type(simd.vector_float2, float, 2, True, objc._C_FLT)

    def test_vector_float3(self):
        self.assert_vector_type(simd.vector_float3, float, 3, True, objc._C_FLT)

    def test_vector_float4(self):
        self.assert_vector_type(simd.vector_float4, float, 4, True, objc._C_FLT)

    def test_vector_double2(self):
        self.assert_vector_type(simd.vector_double2, float, 2, True, objc._C_DBL)

        v = simd.vector_double2(1.0, 2.0)
        v.xy = simd.vector_double2(2.5, 3.5)
        self.assertEqual(v, simd.vector_double2(2.5, 3.5))

        with self.assertRaises(TypeError):
            v.xy = 42

    def test_vector_double3(self):
        self.assert_vector_type(simd.vector_double3, float, 3, True, objc._C_DBL)

        v = simd.vector_double3(1.0, 2.0, 3.0)
        v.xyz = simd.vector_double3(2.5, 3.5, 4.5)
        self.assertEqual(v, simd.vector_double3(2.5, 3.5, 4.5))

        with self.assertRaises(TypeError):
            v.xyz = 42

    def test_vector_double4(self):
        self.assert_vector_type(simd.vector_double4, float, 4, True, objc._C_DBL)

        v = simd.vector_double4(4.0, simd.vector_double2(6.0, 8.0), 9.0)
        self.assertIsInstance(v, simd.vector_double4)
        self.assertEqual(v, simd.vector_double4(4.0, 6.0, 8.0, 9.0))

        v = simd.vector_double4(simd.vector_double3(4.0, 6.0, 8.0), 9.0)
        self.assertIsInstance(v, simd.vector_double4)
        self.assertEqual(v, simd.vector_double4(4.0, 6.0, 8.0, 9.0))

        self.assertEqual(repr(v), "objc.simd.vector_double4(4.0, 6.0, 8.0, 9.0)")
        self.assertEqual(v._objc_literal(), "(vector_double4){4.0, 6.0, 8.0, 9.0}")

        v.x += 0.5
        v.y += 0.6
        v.z += 0.7
        v.w += 0.8
        self.assertEqual(v, simd.vector_double4(4.5, 6.6, 8.7, 9.8))

        v.xy = simd.vector_double2(1.0, 2.0)
        self.assertEqual(v, simd.vector_double4(1.0, 2.0, 8.7, 9.8))

        with self.assertRaises(TypeError):
            v.xy = 42

        v.yz = simd.vector_double2(8.0, 9.0)
        self.assertEqual(v, simd.vector_double4(1.0, 8.0, 9.0, 9.8))

        with self.assertRaises(TypeError):
            v.yz = 42

        v.zw = simd.vector_double2(10.0, 11.0)
        self.assertEqual(v, simd.vector_double4(1.0, 8.0, 10.0, 11.0))

        with self.assertRaises(TypeError):
            v.zw = 42

        v.xyz = simd.vector_double3(-1.0, -2.0, -3.0)
        self.assertEqual(v, simd.vector_double4(-1.0, -2.0, -3.0, 11.0))

        with self.assertRaises(TypeError):
            v.xyz = 42

        v.yzw = simd.vector_double3(-1.5, -2.5, -3.5)
        self.assertEqual(v, simd.vector_double4(-1.0, -1.5, -2.5, -3.5))

        with self.assertRaises(TypeError):
            v.yzw = 42

        v.xyzw = simd.vector_double4(-1.5, -2.5, -3.5, -5.5)
        self.assertEqual(v, simd.vector_double4(-1.5, -2.5, -3.5, -5.5))

        with self.assertRaises(TypeError):
            v.xyzw = 42


class TestSIMDMatrixTypes(TestCase):
    pass


class TestSIMDQuadTypes(TestCase):
    pass
