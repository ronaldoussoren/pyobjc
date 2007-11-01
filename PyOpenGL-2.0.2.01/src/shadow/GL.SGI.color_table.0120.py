# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _color_table

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


__version__ = _color_table.__version__
__date__ = _color_table.__date__
__api_version__ = _color_table.__api_version__
__author__ = _color_table.__author__
__doc__ = _color_table.__doc__

glColorTableSGI = _color_table.glColorTableSGI

glColorTableubSGI = _color_table.glColorTableubSGI

glColorTablebSGI = _color_table.glColorTablebSGI

glColorTableusSGI = _color_table.glColorTableusSGI

glColorTablesSGI = _color_table.glColorTablesSGI

glColorTableuiSGI = _color_table.glColorTableuiSGI

glColorTableiSGI = _color_table.glColorTableiSGI

glColorTablefSGI = _color_table.glColorTablefSGI

glCopyColorTableSGI = _color_table.glCopyColorTableSGI

glColorTableParameterivSGI = _color_table.glColorTableParameterivSGI

glColorTableParameterfvSGI = _color_table.glColorTableParameterfvSGI

glGetColorTableParameterivSGI = _color_table.glGetColorTableParameterivSGI

glGetColorTableParameterfvSGI = _color_table.glGetColorTableParameterfvSGI

glGetColorTableSGI = _color_table.glGetColorTableSGI

glGetColorTableubSGI = _color_table.glGetColorTableubSGI

glGetColorTablebSGI = _color_table.glGetColorTablebSGI

glGetColorTableusSGI = _color_table.glGetColorTableusSGI

glGetColorTablesSGI = _color_table.glGetColorTablesSGI

glGetColorTableuiSGI = _color_table.glGetColorTableuiSGI

glGetColorTableiSGI = _color_table.glGetColorTableiSGI

glGetColorTablefSGI = _color_table.glGetColorTablefSGI

glInitColorTableSGI = _color_table.glInitColorTableSGI

__info = _color_table.__info
GL_COLOR_TABLE_SGI = _color_table.GL_COLOR_TABLE_SGI
GL_POST_CONVOLUTION_COLOR_TABLE_SGI = _color_table.GL_POST_CONVOLUTION_COLOR_TABLE_SGI
GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI = _color_table.GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI
GL_PROXY_COLOR_TABLE_SGI = _color_table.GL_PROXY_COLOR_TABLE_SGI
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI = _color_table.GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI = _color_table.GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI
GL_COLOR_TABLE_SCALE_SGI = _color_table.GL_COLOR_TABLE_SCALE_SGI
GL_COLOR_TABLE_BIAS_SGI = _color_table.GL_COLOR_TABLE_BIAS_SGI
GL_COLOR_TABLE_FORMAT_SGI = _color_table.GL_COLOR_TABLE_FORMAT_SGI
GL_COLOR_TABLE_WIDTH_SGI = _color_table.GL_COLOR_TABLE_WIDTH_SGI
GL_COLOR_TABLE_RED_SIZE_SGI = _color_table.GL_COLOR_TABLE_RED_SIZE_SGI
GL_COLOR_TABLE_GREEN_SIZE_SGI = _color_table.GL_COLOR_TABLE_GREEN_SIZE_SGI
GL_COLOR_TABLE_BLUE_SIZE_SGI = _color_table.GL_COLOR_TABLE_BLUE_SIZE_SGI
GL_COLOR_TABLE_ALPHA_SIZE_SGI = _color_table.GL_COLOR_TABLE_ALPHA_SIZE_SGI
GL_COLOR_TABLE_LUMINANCE_SIZE_SGI = _color_table.GL_COLOR_TABLE_LUMINANCE_SIZE_SGI
GL_COLOR_TABLE_INTENSITY_SIZE_SGI = _color_table.GL_COLOR_TABLE_INTENSITY_SIZE_SGI

