====================================================
API Description for :mod:`PyObjCTools.AppCategories`
====================================================

.. module:: PyObjCTools.AppCategories
   :synopsis: Useful categories on classes from AppKit


Introduction
------------

The module :mod:`PyObjCTools.AppCategories` defines a number of categories on
classes from the *AppKit* framework. These categories introduce
new methods that aren't present in that framework.

To use these new methods use the following code somewhere in your program:

  .. sourcecode:: python

     import PyObjCTools.AppCategories


Additional methods on ``NSGraphicsContext``
-------------------------------------------

This module defines a method for ``NSGraphicsContext``:

.. method:: NSGraphicsContext.savedGraphicsState

   This is a Python context-manager for use with the ``with`` statement.

   Usage:

   .. sourcecode:: python

      with NSGraphicsContext.savedGraphicsState():
          pass

   This is equivalent to:

   .. sourcecode:: python

      NSGraphicsContext.saveGraphicsState()
      try:
      	  pass
      finally:
	  NSGraphicsContext.restoreGraphicsState()


Context-manager for ``NSAnimationContext``
------------------------------------------

Class :c:type:`NSAnimationContext` can be used as the context for a ``with`` 
statement:

    .. sourcecode:: python

	with NSAnimationContext:
		pass

This is equivalent to:

    .. sourcecode:: python

	NSAnimationContext.beginGrouping()
	try:
		pass
	finally:
		NSAnimationContext.endGrouping()
