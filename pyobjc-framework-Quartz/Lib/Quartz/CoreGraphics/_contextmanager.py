"""
This module defines a number of context managers. These are meant to be used
in the context of the with statement (introduced in Python 2.5).
"""

__all__ = ("CGSavedGState", "CGTransparencyLayer", "CGContextPage")
import Quartz


class CGSavedGState:
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with  CGSavedGState(context):
            statement

    This is equivalent to:
        CGContextSaveGState(context)
        try:
            statement

        finally:
            CGContextRestoreGState(context)
    """

    def __init__(self, context):
        self.context = context

    def __enter__(self):
        Quartz.CGContextSaveGState(self.context)
        return self

    def __exit__(self, exc_type, exc_value, exc_tp):
        Quartz.CGContextRestoreGState(self.context)
        return False


class CGTransparencyLayer:
    """
    Context manager for working in a transparancylayer.

    Usage::

        with CGTransparencyLayer(context, info [, rect]):
            statement

    This is equivalent to:
        CGContextBeginTransparencyLayer(context, info)
        try:
            statement

        finally:
            CGContextEndTransparencyLayer(context)
    """

    def __init__(self, context, info, rect=None):
        self.context = context
        self.info = info
        self.rect = rect

    def __enter__(self):
        if self.rect is None:
            result = Quartz.CGContextBeginTransparencyLayer(self.context, self.info)
        else:
            result = Quartz.CGContextBeginTransparencyLayerWithRect(
                self.context, self.rect, self.info
            )
        return result

    def __exit__(self, exc_type, exc_value, exc_tp):
        Quartz.CGContextEndTransparencyLayer(self.context)
        return False


class CGContextPage:
    """
    Context manager for saving and restoring the graphics state.

    Usage::

        with CGContextPage(context) as mediaRect:
            statement

    This is equivalent to:
        mediaRect = CGContextBeginPage(context, None)
        try:
            statement

        finally:
            CGContextEndPage(context)
    """

    def __init__(self, context, mediaBox=None):
        self.context = context
        self.mediaBox = mediaBox

    def __enter__(self):
        mediaRect = Quartz.CGContextBeginPage(self.context, self.mediaBox)
        return mediaRect

    def __exit__(self, exc_type, exc_value, exc_tp):
        Quartz.CGContextEndPage(self.context)
        return False
