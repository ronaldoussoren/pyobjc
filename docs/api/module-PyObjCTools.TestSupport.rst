=================================================
:mod:`PyObjCTools.TestSupport` -- Testing helpers
=================================================

.. module:: PyObjCTools.TestSupport
   :synopsis: Testing helpers

This module provides classes and functions that are
useful for testing PyObjC itself including the framework
wrappers.

.. warning::

   This module is primarily used for testing PyObjC
   and the API isn't fully stable.

.. function:: expectedFailureIf(condition)

   Decorator that marks a test as an expected failure
   if *condition* is true.

.. function:: no_autorelease_pool

   Decorator that disables the autorelease pool that's
   used for specific tests.

   .. versionadded: 8.2


.. function:: pyobjc_options(\**kwds)

   Contextmanager that sets attributes of :data:`objc.options`
   to the given values while running the body of the
   block.

.. function:: sdkForPython()

   Returns the SDK version used to compile Python,
   or :data:`None` when no version can be calculated.

   The SDK version is a tuple with the major
   and minor versions of macOS (for example ``(10, 8)``).

.. function:: fourcc(value)

   Returns the integer value of a four character code
   "literal".

   The *value* is a byte string of length 4 and contains
   the contents of the *char* C literal with
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

   Returns the release of macOS on the current machine.

   .. note::

      Before PyObjC 4.0.1 this returned the major release and
      left out the patch level.

.. function:: os_level_key(release)

   Return a value for *release* that can be used to compare
   two versions with the "<" and ">" operators.

.. function:: min_sdk_level(version)

   Decorator for enabling a test only when running with a build of PyObjC
   that was done with a recent enough SDK for macOS.

.. function:: max_sdk_level(version)

   Decorator for enabling a test only when running with a build of PyObjC
   that was done with an old enough SDK for macOS.

.. function:: min_os_level(version)

   Decorator for enabling a test only when running on a recent enough release
   of macOS.


.. function:: max_os_level(version)

   Decorator for enabling a test only when running on a old enough release
   of macOS.


.. _`leaks(1)`: https://www.manpagez.com/man/1/leaks/

.. class:: TestCase

   A subclass of :class:`unittest.TestCase` with some addition functionality. The
   most important addition is that each test gets run with a fresh autorelease pool.

   .. method:: run()

      Calls :meth:`unitest.TestCase.run`, but ensures that there is a fresh
      autorelease pool for every test. This makes is less likely that two
      tests accidentally influence each other.

      There will not be a fresh autorelease pool when :envvar:`PYOBJC_NO_AUTORELEASE`
      is in the shell environment.


      .. versionchanged:: 2.5
         Removed support for using the `leaks(1)`_ tool to check for memory leaks because
         that support was broken (cause test hangs) and didn't properly report leaks. This
         used to environment variable :envvar:`PyOBJC_USE_LEAKS` as a trigger to enable the
         functionality.

   .. method:: assertStartswith(self, value, check[, message])

      Assert that *value* is a string that starts with *check*.

   .. method:: assertHasAttr(self, value, key[, message])

      Assert that *value* has an attribute named *key*.

   .. method:: assertNotHasAttr(self, value, key[, message])

      Assert that *value* does not have an attribute named *key*.

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

   .. method:: assertArgIsIDLike(method, argno[, message])

      Asserts that the type of argument *argno* is ``_C_ID``, or a known
      CoreFoundation type encoding.

   .. method:: resultArgIsIDLike(method[, message])

      Asserts that the type of the return value is ``_C_ID``, or a known
      CoreFoundation type encoding.

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

      Assert that the result has type *BOOL*.

   .. method:: assertArgHasType(method, argno, tp[, message])

      Assert that the argument *argno* has a specific type encoding.

   .. method:: assertArgIsBOOL(method, argno[, message])

      Assert that the argument *argno* has type *BOOL*.

   .. method:: assertArgIsFunction(method, argno, sel_type, retained[, message])

      Assert that argument *argno* is a function with a specific type signature.
      If *retained* is true the function stores the function reference beyond
      the end of the function call.

   .. method:: assertResultsFunction(method, sel_type, [, message])

      Assert that the result is a function with a specific type signature.

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

   .. method:: assertPickleRoundTrips(value)

      Assert that *value* can be pickled, and roundtrips back to an equal
      value of the same type.

   .. note::

      There are also a number of deprecated aliases for the methods above, those
      are intentionally not documented.
