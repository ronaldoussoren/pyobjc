The release workflow for PyObjC
===============================

This is a description of the workflow for pushing out a new release of PyObjC.

.. note::

   This document is a work in progress.

The release workflow consists of a number of steps, each of which will be described
below.

1. Ensure that PyObjC works on all supported platforms.

2. Update version number for release

3. Create distributions artifacts with smoke test

5. Tag the release

6. Update the PyObjC website

7. Upload the new release

8. Update the version in the repository

Ensure that PyObjC works on all supported platform
--------------------------------------------------

This steps needs to be automated and is currently manual labor...

On every supported platform start of with a clean installation of Python 2.7, 3.4 and 3.5 using
the installers on www.python.org.

Run ``development-support/run-testsuite`` and check the report at the end for errors. When you
do get errors: fix the problems and start over.

Update version number for release
---------------------------------

Run ``development-support/set-pyobjc-version VERSION`` where *VERSION* is the version number for the
upcoming release, and commit the changes.

Create distribution artifacts
-----------------------------

The machine used to create the distribution archives is a VM running OSX 10.12 with the following
additional software:

* up to date version of Xcode

* up to date versions of Python 2.7, 3.4, 3.5 and 3.6

  All of these are installed using the python.org binary installer for OSX 10.6 or later,
  and during installation only the framework itself is installed (nothing in /usr/local,
  no GUI tools)

* up to date python and python3 from Homebrew


Update the dependencies needed for the final tests and creating the distribution archive:

* ``$ development-support/update-system-dependencies``

  This will install or upgrade pip, setuptools, virtualenv and wheel.

Then build the archives:

* ``$ development-support/collection-dist-archives``

  This will create the "sdist" and "wheel" archives in "distribution-dir". That directory
  build also contain a file "build-info.txt" with information about the build environment.

* ``$ development-support/test-wheels``

  This will perform a smoke-test of the generated wheels on the current machine.

  For major releases also run this on other OSX releases (after transporting "distribution-dir"
  to those machines).


Tag the release
---------------

Create a tag in the pyobjc repository. The tag name is "pyobjc-VERSION" (with *VERSION* replaced by
the correct version).

Push to bitbucket.

Update the PyObjC website
-------------------------

In the pyobjc-website project directory:

.. sourcecode:: sh

  $ make collect
  $ make html
  $ make show

Check the contents of the website.

Then upload:

.. sourcecode:: sh

  $ make upload


Upload the new release
----------------------

Use "twine" to upload the source and wheel archives created earlier to PyPI.


Update the version in the repository
------------------------------------

If this is a new feature release (3.2 to 3.3):

* Create a branch for future bugfix release in this feature release

* Close the branch for the previous feature release

* In the new branch: update the version of the first patch release with "b1" as a suffix.

* In the default branch: update the version to the next feature release with "a1" as a suffix


If this is a new bugfix release:

* Update the version number in the bugfix branch, the version number if the version number for the
  next release followed by "b1" (e.g. "3.2.2b1" if you just released "3.2.1").

Push the update to bitbucket.
