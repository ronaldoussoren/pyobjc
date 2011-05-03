Development
===========

.. _`subversion`: http://subversion.tigris.org/



Repository
----------

The PyObjC repository is a `subversion` repository at <http://svn.red-bean.com/pyobjc>.

Martin Ott maintains an easy to install Subversion package for Mac OS X 10.3. It can be downloaded from `his site`__. Note
that recent versions of OSX already ship with a subversion client.

.. __: http://www.codingmonkeys.de/mbo/

You can fetch a snapshot of the current development tree using a WebDAV connection to <http://svn.red-bean.com/pyobjc/trunk/>
or <https://svn.red-bean.com/pyobjc/trunk/>, just copy the ``pyobjc`` folder to a local disk.

Bug tracker and older files
---------------------------

PyObjC has a file download service and bug tracker hosted on SourceForge, they can be found here:

 * Bug tracker: http://sourceforge.net/tracker/?group_id=14534&atid=114534

 * Files:  http://sourceforge.net/project/showfiles.php?group_id=14534


Testing PyObjC
--------------

PyObjC includes a large number of unittests. These can be started using
a ``test`` command in ``setup.py``::
   
   $ python setup.py test

Contributing to PyObjC
----------------------

The best way too contribute to PyObjC is by sending patches or (links to)
examples to the list. Soon enough someone will get bored with applying
your changes and you'll get access to the repository :-).

We're currently short on good documentation and well sample code for
several frameworks, those are a good way to contribute without diving into
the rather hairy code of the actual bridge.
