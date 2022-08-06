API Notes: SpriteKit framework
===============================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/spritekit/?preferredLanguage=occ

These bindings are accessed through the ``SpriteKit`` package (that is, ``import SpriteKit``).

API Notes
---------

* ``SK_VERSION``: This constant is not exposed as it changes with the SDK used.

* ``+[SKFieldNode customFieldWithEvaluationBlock:]``

  This method is not supported yet (requires changes to the core bridge)

.. note::

   This framework is only available on macOS 10.9 and later.
