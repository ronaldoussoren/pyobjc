Code Signing and Notarizing
===========================

Applications using PyObjC can be signed and notarized
in the usual way, but you do need to make sure that
the signature contains the right entitlements.

PyObjC uses a limited form of dynamic code generation
to create executable stubs that are used to call from
(Objective-)C code into Python. This requires an
exception from the Hardened Runtime configuration.

In particular, enable "Allow Execution of JIT-compiled code"
in the Hardened Runtime configuration. If that doesn't work
enable "Allowed Unsigned Executable Memory" instead.
