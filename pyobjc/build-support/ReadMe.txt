TestSupport scripts
===================

This directory contains a number of scripts and related files that make it
easier to thorougly test PyObjC with a number of different Python release and
build flavours.

All scripts are python3 scripts.

* build_frameworks.py:
  This script creates a couple of framework
  builds of Python for various Python
  releases:

  - 32-bit (i386, ppc), 3-way (i386, ppc, x86_64) and intel (i386, x86)
  - 2.6, 2.7, 3.1 and 3.2

  All builds are with '--with-pydebug' and
  are installed using an alternate framework
  name to avoid messing with an already existing
  install.

* run_tests.py

  Uses the frameworks installed by build_frameworks.py
  to run all PyObjC tests with all supported Python
  variants.


Both scripts have arguments to select what gets build or
tested:

* ``--help``

  Show the support command-line options

* ``--archs=3-way,32-bit``

  Select the architecture variants

* ``--versions=2.6,2.7``

  Select the python versions

* ``--only-setup``

  For run_tests: don't actually run the tests, just do
  the initial setup of pyobjc-core, pyobjc-framework-Cocoa
  and pyobjc-framework-Quartz

* ``--skip-quartz``

  For run_tests: do not run the tests for pyobjc-framework-Quartz
  (this makes it possible to run most of the testsuite in the
  background, the Quartz tests mess up the display while running)

* ``--index=index.html``

  For run_tests: select the filename for the report file that 
  gets generated, defaults to "index.html"

Managment tools
---------------

* ``set-version.py``

  This script has a single argument: a version number. The script updates
  the pyobjc version number to that version throught the project.

Support files
-------------

* ``checkout``

  This directory gets created by the scripts and contains checkouts of
  python releases.

* ``distribute-0.6.12-patched``

  A slightly patched version of distribute-0.6.12 that enables running with
  a older alpha of python 3.2

* ``templates``

  Contains Jinja2 template files for the run_tests script.

* ``testresults``

  This directory gets created by the run_tests script and contains the 
  raw results as well as the HTML summary report.

* ``topsort.py``

  An implementation of a topological sort function.

* ``virtualenv-src``, ``virtualenv3-src``

  Checkouts of virtualenv for python2 and python3, slightly patched to
  work better.

* ``virtualenvs``

  Contains the virtualenvs used during testing.
