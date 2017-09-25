Introduction
============

The PyObjC project aims to provide a bridge between the Python and Objective-C
programming languages. The bridge is intended to be fully bidirectional, allowing
the Python programmer to take full advantage of the power provided by various
Objective-C based toolkits and the Objective-C programmer transparent access
to Python based functionality.

The most important usage of this is writing Cocoa GUI applications on Mac OS X
in pure Python. See our tutorial for an example of this.

Release information
-------------------

.. raw:: html

   <p>PyObjC <span id="release_version">4.0</span> was released on <span id="release_date">2017-09-25</span>.
   See the <a href="changelog.html">changelog</a> for more information.
   <script type="text/javascript">
      $.getJSON('https://pypi.python.org/pypi/pyobjc/json?callback=?', function(data) {
         $('#release_version').text(data.info.version);

         $.each(data.urls, function(idx, info) {
                $('#release_date').text(info.upload_time.substring(0, 10));
         });
      });
   </script>


General documentation
=====================

.. toctree::
   :maxdepth: 1

   install
   changelog
   core/intro
   core/protocols
   core/blocks
   core/typemapping
   core/fsref-fsspec
   core/type-wrapper
   core/introspecting
   core/serializing
   core/kvo
   core/objc-gc
   metadata/index
   tutorials/index
   notes/quartz-vs-coregraphics
   examples/index
   notes/framework-wrappers.rst
   apinotes
   team
   release-workflow
   xcode


API documentation
=================

.. toctree::
   :maxdepth: 2

   api/index
   api/coregraphics-context-managers
   api/threading-helpers
   api/module-PyObjCTools.AppCategories
   api/module-PyObjCTools.FndCategories



PyObjC Developement
===================

PyObjC development is hosted at bickbucket, in particular at <https://bitbucket.org/ronaldoussoren/pyobjc/>.

Important resources:

* `Issue tracker <https://bitbucket.org/ronaldoussoren/pyobjc/issues>`_

* `PyObjC-dev mailing list <https://lists.sourceforge.net/lists/listinfo/pyobjc-dev>`_

  A low-volume mailinglist for PyObjC development.

* `Mailing list for the PythonMac SIG <https://www.python.org/community/sigs/current/pythonmac-sig/>`_

  A mailing list for anyone developing with Python on Mac OS X.

* `Repository browser <https://bitbucket.org/ronaldoussoren/pyobjc/src>`_

* Creating a checkout of the respository:

  .. sourcecode:: sh

     $ hg clone https://bitbucket.org/ronaldoussoren/pyobjc pyobjc

  You can then use the "install.py" at the root of the checkout to
  install this version of PyObjC.

.. toctree::
   :maxdepth: 1
   :glob:

   dev/*


Indices and tables
==================

* :ref:`modindex`
* :ref:`search`

