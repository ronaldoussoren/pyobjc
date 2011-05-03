=========================================
Using WebKit's nightly builds with PyObjC
=========================================

The WebKit developers make regular binary builds of WebKit. These can be
downloaded from http://nightly.webkit.org/builds/. With some effort you
can use these snapshots to create a version of PyObjC that makes use of
the frameworks in those snapshots.

Instructions
------------

1. Download the nightly snapshot and place ``WebKit.app`` into
   this directory


2. Run ``python rewriteHeaders.py`` from this directory to extract
   the frameworks

3. Apply the patch to setup.py in this directory

4. Rebuild (and reinstall) PyObjC.


Todo
----

The updated frameworks might include new global functions or constants,
those are not yet made available to python code. We'd need a patch to
``Scripts/CodeGenerators`` to make that possible.
