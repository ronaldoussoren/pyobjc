:mod:`objc.simd` -- SIMD support for PyObjC
===========================================

.. module:: objc.simd
   :platform: macOS
   :synopsis: SIMD support for PyObjC

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>


Introduction
------------

The module :mod:`objc.simd` provides types that are used
to support SIMD types in PyObjC.

The module contains two groups of types:

1. Vector types

   These types behave like numbers and support
   the usual numerical operators, as well as
   matrix multiplication.

2. Matrix types

   These are structs containing an array of
   vector types and don't support numerical operators.

.. note::

   This module only defines the SIMD types either used in
   Cocoa frameworks as wrapped by PyObjC, or needed to
   fully implement those types.

   This means that there obvious holes in the types
   described below. That is intentional.

Vector types
............

Only the first vector types is fully described. The other
types follow the same pattern, dropping fields as needed
(that is, a 4 element vector has attributes named *x*,
*y*, *z*, *w* to represent elements, a 2 element vector
only has *x* and *y*).

The exception to the rule is ``vector_uchar16``: This type
does not support the complicated ``__init__`` signature and
does not support named accessors to elements.

.. class:: vector_double4

   A vector of 4 floating point values. In C these values
   are C *double* values.


   .. method:: __init__(self, x: float)

      Initialize all elements of the vector to the same value

   .. method:: __init__(self, x: float, y: float, z: float, w: float)
      :noindex:

      Initialize the 4 elements of the vector

   .. method:: __init__(self, xy: vector_float2, z: float, w: float)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, x: float, yz: vector_float2, w: float)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, x: float, y: float, zw: vector_float2)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, xy: vector_float2, zw: vector_float2)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, x: float, yzw: vector_float3)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, xyz: vector_float3, w: float)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. method:: __init__(self, xxyz: vector_float4)
      :noindex:

      Initialize the 4 elements of the vector after
      unpacking the vector argument.

   .. data:: x: float

      First element of the vector

   .. data:: y: float

      Second element of the vector

   .. data:: z: float

      Third element of the vector

   .. data:: w: float

      Fourth element of the vector

   .. data:: xy

      A :class:`vector_double2` with the first and second
      elements.

   .. data:: yz

      A :class:`vector_double2` with the second and third
      elements.

   .. data:: zw

      A :class:`vector_double2` with the third and fourth
      elements.

   .. data:: xyz

      A :class:`vector_double3` with the first,  second and third
      elements.

   .. data:: yzw

      A :class:`vector_double3` with the second, third and fourth
      elements.

   .. data:: xyzw

      A copy of the vector.

   .. method:: __getitem__(index: int) -> float

      Return the ``index``th element, for
      ``idx`` in the range 1 to 4 (inclusive).

   .. method:: __setitem__(index: int, value: float)

      Replace element at *indx* with *value*.

   .. method:: __add__(self, other: vector_double4) -> vector_double4

      Return a :class:`vector_double4` with the pairwise
      addition of *self* and *other*.

   .. method:: __add__(self, other: float|int) -> vector_double4
      :noindex:

      Return a :class:`vector_double4` with *other*
      added to all elements of *self*.

   .. method:: __mul__(self, other: vector_double4) -> vector_double4

      Return a :class:`vector_double4` with the pairwise
      multiplication of *self* and *other*.

   .. method:: __mul__(self, other: float|int) -> vector_double4
      :noindex:

      Return a :class:`vector_double4` with all
      elements of *self* multiplied by *other*.

   .. method:: __div__(self, other: vector_double4) -> vector_double4

      Return a :class:`vector_double4` with the pairwise
      division of *self* and *other*.

   .. method:: __div__(self, other: float|int) -> vector_double4
      :noindex:

      Return a :class:`vector_double4` with all
      elements of *self* divided by *other*.

   .. method:: __matmul__(self, other: vector_double4) -> float

      Return the inner product of *self* and *other*

   .. method:: __abs__(self) -> vector_double4

      Return a :class:`vector_double4` with the absolute
      value of all elements of *self*.

   .. method:: __neg__(self) -> vector_double4

      Return a :class:`vector_double4` with the negated
      value of all elements of *self*

   .. method:: __pos__(self) -> vector_double4

      Return a copy of *self*.

   .. method:: __eq__(self, other)

      Return True if *self* and *other* are equal
      after casting *other* to :class:`vector_double4`

   .. method:: __ne__(self, other)

      Return False if *self* and *other* are equal
      after casting *other* to :class:`vector_double4`

   .. method:: __lt__(self, other)

      Return True if *self* is less than *other*
      after casting *other* to :class:`vector_double4`

   .. method:: __le__(self, other)

      Return True if *self* is less than or equal to *other*
      after casting *other* to :class:`vector_double4`

   .. method:: __gt__(self, other)

      Return True if *self* is greater than *other*
      after casting *other* to :class:`vector_double4`

   .. method:: __ge__(self, other)

      Return True if *self* is greater than or equal to *other*
      after casting *other* to :class:`vector_double4`

   .. versionadded: 9.0

.. class:: vector_double2

   A vector of 2 floating point values. In C these values
   are C *double* values.

   .. versionadded: 9.0

.. class:: vector_double3

   A vector of 3 floating point values. In C these values
   are C *double* values.

   .. versionadded: 9.0

.. class:: vector_float2

   A vector of 2 floating point values. In C these values
   are C *float* values.

   .. versionadded: 9.0

.. class:: vector_float3

   A vector of 3 floating point values. In C these values
   are C *float* values.

   .. versionadded: 9.0

.. class:: vector_float4

   A vector of 4 floating point values. In C these values
   are C *float* values.

   .. versionadded: 9.0

.. class:: vector_short2

   A vector of 2 integer values. In C these values
   are C *short* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *short*.

   .. versionadded: 9.0

.. class:: vector_ushort2

   A vector of 2 integer values. In C these values
   are C *unsigned short* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned short*.

   .. versionadded: 9.0

.. class:: vector_ushort3

   A vector of 3 integer values. In C these values
   are C *unsigned short* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned short*.

   .. versionadded: 9.0

.. class:: vector_ushort4

   A vector of 4 integer values. In C these values
   are C *unsigned short* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned short*.

   .. versionadded: 9.0

.. class:: vector_int2

   A vector of 2 integer values. In C these values
   are C *int* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *int*.

   .. versionadded: 9.0

.. class:: vector_int3

   A vector of 3 integer values. In C these values
   are C *int* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *int*.

   .. versionadded: 9.0

.. class:: vector_int4

   A vector of 4 integer values. In C these values
   are C *int* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *int*.

   .. versionadded: 9.0

.. class:: vector_uint2

   A vector of 2 integer values. In C these values
   are C *unsigned int* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned int*.

   .. versionadded: 9.0

.. class:: vector_uint3

   A vector of 3 integer values. In C these values
   are C *unsigned int* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned int*.

   .. versionadded: 9.0

.. class:: vector_uchar16

   A vector of 16 integer values. In C these values
   are C *unsigned char* values.

   The values of elements of the vector are automatically
   restricted to the range of a C *unsigned char*.

   .. versionadded: 9.0

Vector aliases
..............

All types documented in the previous section are also available
with the prefix ``simd_`` instead of ``vector_``.

In particular:

.. class:: simd_int2

   Alias for vector_int2

.. class:: simd_uint2

   Alias for vector_uint2

.. class:: simd_uint3

   Alias for vector_uint3

.. class:: simd_double2

   Alias for vector_double2

.. class:: simd_double3

   Alias for vector_double3

.. class:: simd_double4

   Alias for vector_double4

.. class:: simd_float2

   Alias for vector_float2

.. class:: simd_float3

   Alias for vector_float3

.. class:: simd_float4

   Alias for vector_float4

.. class:: simd_short2

   Alias for vector_short2

.. class:: simd_ushort2

   Alias for vector_ushort

.. class:: simd_ushort3

   Alias for vector_ushort3

.. class:: simd_ushort4

   Alias for vector_ushort4

.. class:: simd_uchar16

   Alias for vector_uchar16

Matrix types
............

.. class:: matrix_float2x2

   A 2 by 2 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_float2`
   with the row values.

   .. data:: columns

      The columns of the matrix.

.. class:: matrix_float3x3

   A 3 by 3 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_float3`
   with the row values.

   .. data:: columns

      The columns of the matrix.

.. class:: matrix_float4x3

   A 4 by 3 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_float3`
   with the row values.

   .. data:: columns

      The columns of the matrix.

.. class:: matrix_float4x4

   A 4 by 4 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_float4`
   with the row values.

   .. data:: columns

      The columns of the matrix.

.. class:: simd_float4x4

   A 4 by 4 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_float4`
   with the row values.

   .. data:: columns

      The columns of the matrix.

.. class:: matrix_double4x4

   A 4 by 4 matrix of floats,
   represented as an array of columns where each
   element of the array is a :class:`vector_double4`
   with the row values.

   .. data:: columns

      The columns of the matrix.

Quaternions
...........

.. class:: simd_quatf

   A struct wrapping a :class:`vector_float4`

   .. data:: vector

      The wrapped value

.. class:: simd_quatd

   A struct wrapping a :class:`vector_doulbe4`

   .. data:: vector

      The wrapped value
