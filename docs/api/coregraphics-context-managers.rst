=================================
Context Managers for CoreGraphics
=================================

.. currentmodule:: Quartz

The CoreGraphics bindings for PyObjC introduce a couple of context manager
for use with the ``with`` statement. These are simple wrappers around the
basic CoreGraphics/Quartz API's that make using the API more convenient and
allow you to write easier to understand code.

.. function:: CGSavedGState(context)

   Context manager that  wraps a block of code between :func:`CGContextSaveGState` and
   :func:`CGContextRestoreGState`.

   Usage:

   .. sourcecode:: python

      with CGSavedGState(context):
         # Change context and use changed context
         pass

      # Context is restored to before the with-statement at this point.

   :param CGContextRef context: CoreGraphics context value.

.. function:: CGTransparencyLayer(context, info, rect=None)

   Context manager that  wraps a block of code between :func:`CGContextBeginTransparencyLayer`
   (or :func:`CGContextBeginTransparencyLayerWithRect` if *rect* is not :data:`None`)
   and :func:`CGContextEndTransparencyLayer`.

   Usage:

   .. sourcecode:: python

      with CGTransparancyLayer(context, None):
          pass

   Or:

   .. sourcecode:: python

      with CGTransparancyLayer(context, None, myRect):
         pass

   :param CGContexRef context: A CoreGraphics context.
   :param dict|None info: A directory with additional information, or :data:`None`.
   :param CGRect rect: Bounds for the transparent layer.

.. function:: GContextPage(context, mediaBox=None)

   Context manager that  wraps a block of code between calls to :func:`CGContextBeginPage` and
   :func:`CGContextEndPage`).

   Usage:

   .. sourcecode:: python

      with CGContextPage(context):
          pass

   :param CGContextRef context: A CoreGraphics context.
   :param CGRect|None mediaBox: Optional rectangle defining the bounds of the page.
                                Defaults to the media box for *context*.
