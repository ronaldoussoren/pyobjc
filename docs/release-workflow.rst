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

6. Create a GitHub release

7. Update the PyObjC website

8. Upload the new release

9. Update the version in the repository

10. Announce the new release

Ensure that PyObjC works
------------------------

Run ``development-support/run-testsuite`` on the build machine running the latest release
of macOS and check the report at the end for errors. When you do get errors: fix the problems
and start over.

Before the first release supporting a new major release of macOS also run the test suite
on a number of older versions of macOS.


Update version number for release
---------------------------------

Run ``development-support/set-pyobjc-version VERSION`` where *VERSION* is the version number for the
upcoming release, and commit the changes.

Create distribution artifacts
-----------------------------

The machines used to create the distribution archives are two VMs running macOS 10.13 and 10.14 with
the following additional software:

* up to date version of Xcode

* up to date versions of the supported Python versions

  All of these are installed using the python.org binary installer (universal)
  and during installation only the framework itself is installed (nothing in /usr/local,
  no GUI tools)

The script "development-support/collect-dist-archives" creates all distribution archives, but
is not called directly.

Tag the release
---------------

Create a tag in the pyobjc repository. The tag name is "vVERSION" (with *VERSION* replaced by
the correct version).

Push to GitHub.

Create a GitHub release
-----------------------

Create a GitHub release using the newly pushed tag and the changelog for
the current version.

The release artefacts created by GitHub are *not* used in the release process.

Update the PyObjC website
-------------------------

The PyObjC website is automatically updated after push to GitHub.

Upload the new release
----------------------

Use "twine" to upload the source and wheel archives created earlier to PyPI.

Check the website
-----------------

Check that https://pyobjc.readthedocs.io/en/latest/ contains the release notes for the current release

Send out announcement
---------------------

1) Create a blog entry on my blog describing the new release

2) Mention the blog entry on X/Twitter/Mastondon.
