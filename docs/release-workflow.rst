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

9. Announce the new release

Ensure that PyObjC works on all supported platform
--------------------------------------------------

This steps needs to be automated and is currently manual labor...

On every supported platform start of with a clean installation of Python 3.6, 3.7 and 3.8 using
the installers on www.python.org.

Run ``development-support/run-testsuite`` and check the report at the end for errors. When you
do get errors: fix the problems and start over.

Update version number for release
---------------------------------

Run ``development-support/set-pyobjc-version VERSION`` where *VERSION* is the version number for the
upcoming release, and commit the changes.

Create distribution artifacts
-----------------------------

The machines used to create the distribution archives are two VMs running macOS 10.13 and 10.14 with
the following additional software:

* up to date version of Xcode

* up to date versions of Python 3.6, 3.7 and 3.8

  All of these are installed using the python.org binary installer for x86-64
  and during installation only the framework itself is installed (nothing in /usr/local,
  no GUI tools)

The script "development-support/collect-dist-archives" creates all distribution archives, but
is not called directly.

The script "development-support/collect-all-dist-archives" creates the distribution archives on
both build machines and moves them to a common location.

Tag the release
---------------

Create a tag in the pyobjc repository. The tag name is "vVERSION" (with *VERSION* replaced by
the correct version).

Push to GitHub.

Update the PyObjC website
-------------------------

The PyObjC website is automatically updated after push to GitHub.

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

Push the update to GitHub.

Check the website
-----------------

Check that https://pyobjc.readthedocs.io/en/latest/ contains the release notes for the current release

Send out announcement
---------------------

1) Create a blog entry on my blog describing the new release

2) Send e-mail to pythonmac-sig and pyobjc-dev with the same description
