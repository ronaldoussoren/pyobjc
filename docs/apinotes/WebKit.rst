API Notes: WebKit framework
===========================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/webkit/?preferredLanguage=occ

These bindings are accessed through the ``WebKit`` package (that is, ``import WebKit``).

API Notes
---------

* Carbon integration functions are not supported.

  The relevant functions are: ``HIWebViewCreate``, ``HIWebViewCreateWithClass``
  and ``HIWebViewGetWebView``.

* Java plugins (informal protocol ``WebJavaPlugIn``) are not supported.

* The NPAPI interface of WebKit is not supported
