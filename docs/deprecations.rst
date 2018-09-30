Dealing with API deprecations
=============================

Apple's system APIs evolve like any other, new APIs
are introduced and old ones are deprecated (and sometimes
removed).

PyObjC has machinery to help you deal with API deprecations
by providing Python level warnings for these API deprecations.

To enable warnings you need to do two things. First enable
logging warnings for API deprecations:

.. sourcecode:: python

   import warnings
   warnings.simplefilter("always", objc.ApiDeprecationWarning)

Then tell the bridge which API deprecations you want to get
warnings about:


.. sourcecode:: python

   import objc

   objc.options.deprecation_warnings = 1013

This fragment causes the bridge to emit a warning when you
use an API that was deprecated in macOS 10.13 or earlier (but
won't warn about APIs deprecated in macOS 10.14 or later).

.. warning::

   The machinery is already implemented, the metadata needed
   to emit the correct warnings is not present yet. This will
   change in future version of PyObjC.

Example
-------

The following script demonstrates the use of API deprecation warnings:

.. sourcecode:: python
   :name: demoscript.py
   :linenos:

   import objc
   import warnings
   warnings.simplefilter("always", objc.ApiDeprecationWarning)
   objc.options.deprecation_warnings = 1014

   import Contacts
   Contacts.CNPhoneNumber.alloc().init()

When you run this script it logs the following information:


.. sourcecode:: none

    demoscript.py:7: ApiDeprecationWarning: -[CNPhoneNumber init] is a deprecated API (macOS 10.13)
      Contacts.CNPhoneNumber.alloc().init()
