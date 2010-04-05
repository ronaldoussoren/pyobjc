This directory contains a number of scripts
that help in testing PyObjC on a number 
of platforms.

All scripts are python3 scripts, but are currently
simple enough that they probably run with python2.6
as well.

WARNING: The scripts are a work-in-progress and don't 
work right now.

* build_frameworks.py:
  This script creates a couple of framework
  builds of Python for various Python
  releases:

  - 32-bit (i386, ppc) and intel (i386, x86)
  - 2.6, 2.7, 3.1 and 3.2

  All builds are with '--with-pydebug' and
  are installed using an alternate framework
  name to avoid messing with an already existing
  install.

  TODO: also install distribute and virtualenv

* run_tests.py

  Uses the frameworks installed by build_frameworks.py
  to run all PyObjC tests with all supported Python
  variants.

  TODO:
  - create virtual env and install PyObjC dependencies
  - install pyobjc-core, pyobjc-framework-Cocoa and
    pyobjc-framework-Quartz
  - run tests for pyobjc-core and all framework wrappers
  - collect the results and create an HTML page with
    the summary and details.
  - send e-mail with the result to an e-mail address

* TODO: run_distributed_tests.py

  This script will do something simular to run_tests,
  but builds on a 10.6 machine and runs the tests on
  a number of different machines (10.4, 10.5)
