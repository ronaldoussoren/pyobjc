API Notes: LatentSemanticMapping framework
==========================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/latentsemanticmapping/?preferredLanguage=occ

These bindings are accessed through the ``LatentSemanticMapping`` package (that is, ``import LatentSemanticMapping``).


API Notes
---------

All functions in this framework are mapped, however the unittests
for this framework wrapper cause crashes in the Python interpreter.

I'm pretty sure that is due to misuse of the API, sadly enough
I haven't found good documentation or examples for the problematic
functions yet. For this reason a large subset of the framework
interface is not tested at the moment.
