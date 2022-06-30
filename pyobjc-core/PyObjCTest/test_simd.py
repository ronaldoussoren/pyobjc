from PyObjCTools.TestSupport import TestCase

from objc import simd


def calc_xyzw():
    result = set(BASE_ATTR)

    for idx in range(4):
        for n in range(2, 5):
            result.add("".join(BASE_ATTR[idx : idx + n]))

    return result


BASE_ATTR = ("x", "y", "z", "w")
XYZW_ATTR = calc_xyzw()


class TestSIMDVectorTypes(TestCase):
    # XXX:
    # - Tests for various operators
    # - Tests that handle out of range values (including operators)

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

    def assert_vector_type(self, vtype, etype, nelem, is_signed):
        a = vtype()
        self.assertEqual(len(a), nelem)
        self.assertTrue(all(a[i] == etype() for i in range(nelem)))
        self.assert_has_xyzw(a, nelem)

        a = vtype(etype(42))
        self.assertEqual(len(a), nelem)
        self.assertTrue(all(a[i] == etype(42) for i in range(nelem)))

        if nelem != 2:
            with self.assertRaises(ValueError):
                vtype(*range(nelem - 1))

        with self.assertRaises(ValueError):
            vtype(*range(nelem + 1))

        a = vtype(*(etype(n) for n in range(nelem)))
        self.assertTrue(all(a[i] == etype(i) for i in range(nelem)))

        a[0] = a[1]
        self.assertEqual(a[0], a[1])

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

    def test_vector_short2(self):
        self.assert_vector_type(simd.vector_short2, int, 2, True)

    def test_vector_ushort2(self):
        self.assert_vector_type(simd.vector_ushort2, int, 2, False)

    def test_vector_ushort4(self):
        self.assert_vector_type(simd.vector_ushort4, int, 4, False)

    def test_vector_int2(self):
        self.assert_vector_type(simd.vector_int2, int, 2, True)

    def test_vector_uint3(self):
        self.assert_vector_type(simd.vector_uint3, int, 3, False)

    def test_vector_float2(self):
        self.assert_vector_type(simd.vector_float2, float, 2, True)

    def test_vector_float3(self):
        self.assert_vector_type(simd.vector_float3, float, 3, True)

    def test_vector_float4(self):
        self.assert_vector_type(simd.vector_float4, float, 4, True)

    def test_vector_double2(self):
        self.assert_vector_type(simd.vector_double2, float, 2, True)

    def test_vector_double3(self):
        self.assert_vector_type(simd.vector_double3, float, 3, True)

    def test_vector_double4(self):
        self.assert_vector_type(simd.vector_double4, float, 4, True)


class TestSIMDMatrixTypes(TestCase):
    pass


class TestSIMDQuadTypes(TestCase):
    pass
