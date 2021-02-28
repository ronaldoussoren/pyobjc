API Notes: FSEvents framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices/carbon_core/carbon_core_functions?preferredLanguage=occ

These bindings are accessed through the ``FSEvents`` package (that is, ``import FSEvents``).


API Notes
---------

The FSEvents package contains wrappers for the FSEvents API's, which are
part of Carbon and not a standalone framework.

The FSEventsRef type is an opaque pointer, unlike what the name suggests this
is not a CoreFounation based types. As a side-effect of that the programmer
is responsibly for managing the retain-count of objects of this type.

This means you have to call ``FSEventStreamRelease`` when you're done with
a stream. You must not use the stream after that, it will then refer to an
invalid stream.
