=================================
Context Managers for CoreGraphics
=================================

The CoreGraphics bindings for PyObjC introduce a couple of context manager
for use with the ``with`` statement. These are simple wrappers around the
basic CoreGraphics/Quartz API's that make using the API more convenient and
allow you to write easier to understand code.

Note that you'll have to use ``from __future__ import with_statement`` to
use the ``with``-statement in Python 2.5.

* ``CGSavedGState(context)``

  This wraps a block of code between ``CGContextSaveGState`` and
  ``CGContextRestoreGState``.

  Usage::

      with CGSavedGState(context):
         # Change context and use changed context
         pass

      # Context is restored to before the with-statement at this point.

* ``CGTransparencyLayer(context, info, rect=None)``

  This wraps a block of code between ``CGContextBeginTransparencyLayer``
  (or ``CGContextBeginTransparencyLayerWithRect`` if ``rect`` is not ``None``) 
  and ``CGContextEndTransparencyLayer``.

  Usage::

      with CGTransparancyLayer(context, None):
         pass

  Or::

      with CGTransparancyLayer(context, None, myRect):
         pass

* ``CGContextPage``

 This wraps a block of code between calls to ``CGContextBeginPage`` and
 ``CGContextEndPage``).

 Usage::

      with CGContextPage(context [, mediaBox]):
         pass

  __all__ = ('CGSavedGState', 'CGTransparencyLayer',  'CGContextPage')

