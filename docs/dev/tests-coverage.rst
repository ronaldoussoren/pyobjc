Test coverage information
=========================

This file is very much a work in progress...

The documentation in this file is focused on pyobjc-core, I'll add
information about framework bindings once I'm happy with code coverage
for the core bridge as most interesting code is in the bridge itself.


General
-------

Tooling for measuring test coverage helps deterimining if there are
gaps in test coverage. When adding new tests to fill in gaps make sure
to add tests that cover functionality, not just tests that cover
particular lines in the source code.

The longer term goal is to reach close to 100% test coverage through
functional tests.


Test coverage for C code in pyobjc-core
---------------------------------------

For internal APIs in pyobjc-core it can be useful to add tests for these APIs
as well, especially to cover error cases that should never occur in real code.
Add such tests to ``pyobjc-core/Modules/objc/ctests.m``.

The Makefile target "c-coverage" runs the test suite
while collecting coverage information. This requires having
`lcov <https://https://github.com/linux-test-project/lcov>`_ on the system
running the tests, and currently requires an arm64 system.

It is possible to mark lines as unreachable for coverage reporting, use
only in the following cases (and after double checking that the excludede
code is correct):

1. Failure cases in internal state assertions that should never fail

2. Memory allocation failure handling

Use ``LOCV_EXC_LINE`` in a comment to exclude a specific line.

Use ``LCOV_EXC_START`` and ``EXC_EXC_STOP`` in comments to exclude a block
of code.


Test coverage for Python code in pyobjc-core
--------------------------------------------

To collect coverage information first install `coverage <https://coverage.readthedocs.io/>`,
then run:

.. sourcecode:: shell

   $ python3 -mcoverage run --branch setup.py test --verbosity=3
   $ python3 -mcoverage html --omit='PyObjCTest/*,setup.py'
   $ open htmlcov/index.html

Alternatively use the "coverage" target in the Makefile

As with coverage for C code use coverage pragma's sparingly.
