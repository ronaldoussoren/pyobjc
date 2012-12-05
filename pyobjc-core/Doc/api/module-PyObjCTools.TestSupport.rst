=================================================
:mod:`PyObjCTools.TestSupport` -- Testing helpers
=================================================

.. module:: PyObjCTools.TestSupport
   :synopsis: Testing helpers

This module provides classes and functions that are
usefull for testing PyObjC itself including the framework
wrappers.

.. warning::

   This module is primarily used for testing PyObjC 
   and the API isn't fully stable.


.. function:: sdkForPython()

   Returns the SDK version used to compile Python,
   or :data:`None` when no version can be calculated.

   The SDK version is a tupel with the major
   and minor versions of Mac OS X (for example ``(10, 8)``).

.. function:: fourcc(value)

   Returns the integer value of a four character code
   "literal".

   The *value* is a byte string of length 4 and contains
   the contents of the :c:type:`char` C literal with 
   the four character code, for example ``b"abcd"``.

.. function:: cast_int(value)

   Return *value* as if it were a 4 byte integer (using
   the overflow behavior of most CPUs)

.. function:: cast_longlong(value)

   Return *value* as if it were a 8 byte integer (using
   the overflow behavior of most CPUs)


.. function:: cast_uint(value)

   Return *value* as if it were a 4 byte unsigned integer (
   using the overflow behavior of C)

.. function:: cast_ulonglong(value)

   Return *value* as if it were a 8 byte unsigned integer (using
   the overflow behavior of C)

.. function:: os_release()

   Returns the major release of Mac OS X on the current machine,
   for example "10.5" on all systems running a version 
   of Leopard.

.. function:: is32Bit()

   Returns :data:`True` if the proces is in 32-bit mode.

.. function:: onlyIf(expr, message)

   Decorator for enabling tests only when an expression is true. This is
   the same as :func:`skipUnless <unittest.skipUnless>` in Python 2.7 or later.

.. function:: onlyPython2

   Decorator for enabling a test only when using Python 2.x.

   This is basicly ``onlyIf(sys.version_info[0] == 2)``.

.. function:: onlyPython3

   Decorator for enabling a test only when using Python 3.x.

   This is basicly ``onlyIf(sys.version_info[0] == 3)``.

.. function:: onlyOn32Bit

   Decorator for enabling a test only when the process is running in 32-bit mode.

.. function:: onlyOn64Bit

   Decorator for enabling a test only when the process is running in 64-bit mode.

.. function:: min_os_level(version)

   Decorator for enabling a test only when running on a recent enough release
   of Mac OS X.


.. function:: max_os_level(version)

   Decorator for enabling a test only when running on a old enough release
   of Mac OS X.

.. class:: filterWarnings(kind, category)

   A with-statement context that adds a filter to the warnings module
   while the body of the statement is running.

   This is similar to :class:`warnings.catch_warnings`.

.. class:: TestCase

   A subclass of :class:`unittest.TestCase` with some addition functionality. The
   most important addition is that each test gets run with a fresh autorelease pool.

   .. method:: assertItemsEqual(seq1, seq2[, message])

      Asserts that sequences *seq1* and *seq2* have the same members (in any order).

   .. method:: assertGreaterThan(value, test[, message])

      Asserts that *value* is greater than *test*.

   .. method:: assertGreaterThanOrEquals(value, test[, message])

      Asserts that *value* is greater than or equal to *test*.

   .. method:: assertLessThan(value, test[, message])

      Asserts that *value* is less than *test*.

   .. method:: assertLessThanOrEquals(value, test[, message])

      Asserts that *value* is less than or equal to *test*.

   .. method:: assertIs(value, test[, message])

      Asserts that *value* is the same object as *test*

   .. method:: assertIsNot(value, test[, message])

      Asserts that *value* is not the same object as *test*

   .. method:: assertIsNone(value[, message])

      Asserts that *value* is the same object as :data:`None`

   .. method:: assertIsNotNone(value[, message])

      Asserts that *value* is the not same object as :data:`None`

   .. method:: assertSstartswith(self, value, check[, message])

      Assert that *value* is a string that starts with *check*.

   .. method:: assertHasAttr(self, value, key[, message])

      Assert that *value* has an attribute named *key*.

   .. method:: assertNotHasAttr(self, value, key[, message])

      Assert that *value* does not have an attribute named *key*.

   .. method:: assertIsInstance(self, value, types[, message])

      Assert that *value* is an instance of *types*.

   .. method:: assertIsNotInstance(self, value, types[, message])

      Assert that *value* is not an instance of *types*.

   .. method:: assertAlmostEquals(val1, val2[, message)

      Assert that *val1* is almost equal to *val2* (that is,
      the difference between the two values is less that 1e-5)

   .. method:: assertIn(self, value, seq[, message])

      Assert that *value* is a member of *seq*.

   .. method:: assertNotIn(self, value, seq[, message])

      Assert that *value* is not a member of *seq*.

   .. method:: assertIsCFType(tp[, message])

      Asserts that *tp* is a wrapper class for a CoreFoundation type.

   .. method:: assertIsOpaquePointer(tp[, message)

      Asserts that *tp* is a wrapper class for an opaque pointer ("handle")

   .. method:: assertIsNullTerminated(method[, message])

      Asserts that the callable has metadata that indicates that the 
      callable is variadic function where the argument list is terminated by
      a null value.

   .. method:: assertResultIsNullTerminated(method[, message])

      Asserts that the callable has metadata that indicates that the result
      is a null terminated array.

   .. method:: assertArgIsNullTerminated(method, argno[, message])

      Asserts that the callable has metadata that indicates that the argument
      *argno* is a null terminated array.


   .. method:: assertResultIsVariableSize(method[, message])

      Asserts that the callable has metadata that indicates that the result
      is an array with an unspecified size.

   .. method:: assertArgIsVariableSize(method, argno[, message])

      Asserts that the callable has metadata that indicates that the argument
      *argno* is an array with an unspecified size.

   .. method:: assertArgSizeInResult(method, argno[, message)
      Asserts that the callable has metadata that indicates that the argument
      *argno* is an array where the size of the array is specified in the return value.

   .. method:: assertArgIsPrintf(method, argno[, message])

      Assert that the callable has metadata that specifies that it is a
      variadic function with a printf-format string in argument *argno*.

   .. method:: assertResultIsCFRetained(method[, message])

      Assert that the callable has metadata that specifies that the
      retain count of the result is increased by the function (that
      is, the caller owns the value after the call).

   .. method:: assertResultIsNotCFRetained(method[, message])

      Assert that the callable has metadata that specifies that the
      retain count of the result is not increased by the function.

   .. method:: assertArgIsCFRetained(method, argno[, message])

      Assert that the callable has metadata that specifies that the
      retain count of argument *argno* is increased by the function (that
      is, the caller owns the value after the call).

      .. note:: used to check the behavior of output arguments.

   .. method:: assertArgIsNotCFRetained(method, argno[, message])

      Assert that the callable has metadata that specifies that the
      retain count of argument *argno* is not increased by the function.

      .. note:: used to check the behavior of output arguments.

   .. method:: assertResultIsRetained(method[, message])

      Assert that the callable has metadata that specifies that the
      retain count of the result is increased by the function (that
      is, the caller owns the value after the call).

   .. method:: assertResultIsNotRetained(method[, message])

      Assert that the callable has metadata that specifies that the
      retain count of the result is not increased by the function.

   .. method:: assertArgIsRetained(method, argno[, message])

      Assert that the callable has metadata that specifies that the
      retain count of argument *argno* is increased by the function (that
      is, the caller owns the value after the call).

      .. note:: used to check the behavior of output arguments.

   .. method:: assertArgIsNotRetained(method, argno[, message])

      Assert that the callable has metadata that specifies that the
      retain count of argument *argno* is not increased by the function.

      .. note:: used to check the behavior of output arguments.

   .. method:: assertResultHasType(method, tp[, message])

      Assert that the result has a specific type encoding.

   .. method:: assertResultIsBOOL(method[, message])

      Assert that the result has type :c:type:`BOOL`.

   .. method:: assertArgHasType(method, argno, tp[, message])

      Assert that the argument *argno* has a specific type encoding.

   .. method:: assertArgIsBOOL(method, argno[, message])

      Assert that the argument *argno* has type :c:type:`BOOL`.

   .. method:: assertArgIsFunction(method, argno, sel_type, retained[, message])

      Assert that argument *argno* is a function with a specific type signature.
      If *retained* is true the function stores the function reference beyond
      the end of the function call.

   .. method:: assertResultIsBlock(method, sel_type[, message])

      Assert that the result is a block with a specific type signature.

   .. method:: assertArgIsBlock(method, argno, sel_type[, message])

      Assert that argument *argno* is a block with a specific type signature.

   .. method:: assertArgIsSEL(method, argno, sel_type[, message])

      Assert that argument *argno* is a SEL value for a method with
      a specific type signature

   .. method:: assertArgIsFixedSize(method, argno, count[, message])

      Assert that argument *argno* is an array of *count* elements.

   .. method:: assertResultSizeInArg(method, count[, message])

      Assert that the result is an array of where the size
      of the array is specified in argument *count*.

   .. method:: assertArgSizeInArg(method, argno, count[, message])

      Assert that argument *argno* is an array of where the size
      of the array is specified in argument *count*.

      *count* can also be an tuple of two elements: the first elements
      specifies the size before the call, the second the size
      after the call. 

   .. method:: assertArgIsOut(method, argno[, message])

      Assert that argument *argno* is a pass-by-reference output parameter.

   .. method:: assertArgIsIn(method, argno[, message])

      Assert that argument *argno* is a pass-by-reference input parameter.

   .. method:: assertArgIsInOut(method, argno[, message])

      Assert that argument *argno* is a pass-by-reference input and output parameter.

   .. note::

      There are also a number of deprecated aliases for the methods above, those
      are intentionally not documented.
