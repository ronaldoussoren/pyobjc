# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _matrix_palette

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


__version__ = _matrix_palette.__version__
__date__ = _matrix_palette.__date__
__api_version__ = _matrix_palette.__api_version__
__author__ = _matrix_palette.__author__
__doc__ = _matrix_palette.__doc__

glMatrixIndexbvARB = _matrix_palette.glMatrixIndexbvARB

glMatrixIndexubvARB = _matrix_palette.glMatrixIndexubvARB

glMatrixIndexsvARB = _matrix_palette.glMatrixIndexsvARB

glMatrixIndexusvARB = _matrix_palette.glMatrixIndexusvARB

glMatrixIndexivARB = _matrix_palette.glMatrixIndexivARB

glMatrixIndexuivARB = _matrix_palette.glMatrixIndexuivARB

glMatrixIndexfvARB = _matrix_palette.glMatrixIndexfvARB

glMatrixIndexdvARB = _matrix_palette.glMatrixIndexdvARB

glMatrixIndexPointerARB = _matrix_palette.glMatrixIndexPointerARB

glMatrixIndexPointerubARB = _matrix_palette.glMatrixIndexPointerubARB

glMatrixIndexPointerbARB = _matrix_palette.glMatrixIndexPointerbARB

glMatrixIndexPointerusARB = _matrix_palette.glMatrixIndexPointerusARB

glMatrixIndexPointersARB = _matrix_palette.glMatrixIndexPointersARB

glMatrixIndexPointeruiARB = _matrix_palette.glMatrixIndexPointeruiARB

glMatrixIndexPointeriARB = _matrix_palette.glMatrixIndexPointeriARB

glMatrixIndexPointerfARB = _matrix_palette.glMatrixIndexPointerfARB

glMatrixIndexPointerdARB = _matrix_palette.glMatrixIndexPointerdARB

glCurrentPaletteMatrixARB = _matrix_palette.glCurrentPaletteMatrixARB

glInitMatrixPaletteARB = _matrix_palette.glInitMatrixPaletteARB

__info = _matrix_palette.__info
GL_MATRIX_PALETTE_ARB = _matrix_palette.GL_MATRIX_PALETTE_ARB
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB = _matrix_palette.GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB
GL_MAX_PALETTE_MATRICES_ARB = _matrix_palette.GL_MAX_PALETTE_MATRICES_ARB
GL_CURRENT_PALETTE_MATRIX_ARB = _matrix_palette.GL_CURRENT_PALETTE_MATRIX_ARB
GL_MATRIX_INDEX_ARRAY_ARB = _matrix_palette.GL_MATRIX_INDEX_ARRAY_ARB
GL_CURRENT_MATRIX_INDEX_ARB = _matrix_palette.GL_CURRENT_MATRIX_INDEX_ARB
GL_MATRIX_INDEX_ARRAY_SIZE_ARB = _matrix_palette.GL_MATRIX_INDEX_ARRAY_SIZE_ARB
GL_MATRIX_INDEX_ARRAY_TYPE_ARB = _matrix_palette.GL_MATRIX_INDEX_ARRAY_TYPE_ARB
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB = _matrix_palette.GL_MATRIX_INDEX_ARRAY_STRIDE_ARB
GL_MATRIX_INDEX_ARRAY_POINTER_ARB = _matrix_palette.GL_MATRIX_INDEX_ARRAY_POINTER_ARB

