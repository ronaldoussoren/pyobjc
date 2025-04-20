.. module:: CoreWLAN
   :platform: macOS
   :synopsis: Bindings for the CoreWLAN framework

API notes: CoreWLAN framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/corewlan?preferredLanguage=occ

These bindings are accessed through the ``CoreWLAN`` package (that is, ``import CoreWLAN``).

API Notes
---------

Code only gets access to privacy relevant when the binary is signed
properly (not using an ad-hoc signature). This is a security feature in macOS.
