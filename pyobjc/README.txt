This is a "pseudo-package". Its only goal in life is to make it
easier to install the rest of PyObjC.

That is, "python setup.py install" of "easy_install pyobjc" will install
this package and as a side effect will also install the rest of PyObjC
(pyobjc-core and the various framework wrappers).

This package does not contain code of itself.
