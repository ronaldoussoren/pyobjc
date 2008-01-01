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

glColorTableEXT = _color_table.glColorTableEXT

glColorTableubEXT = _color_table.glColorTableubEXT

glColorTablebEXT = _color_table.glColorTablebEXT

glColorTableusEXT = _color_table.glColorTableusEXT

glColorTablesEXT = _color_table.glColorTablesEXT

glColorTableuiEXT = _color_table.glColorTableuiEXT

glColorTableiEXT = _color_table.glColorTableiEXT

glColorTablefEXT = _color_table.glColorTablefEXT

glCopyColorTableEXT = _color_table.glCopyColorTableEXT

glColorTableParameterivEXT = _color_table.glColorTableParameterivEXT

glColorTableParameterfvEXT = _color_table.glColorTableParameterfvEXT

glGetColorTableParameterivEXT = _color_table.glGetColorTableParameterivEXT

glGetColorTableParameterfvEXT = _color_table.glGetColorTableParameterfvEXT

glGetColorTableEXT = _color_table.glGetColorTableEXT

glGetColorTableubEXT = _color_table.glGetColorTableubEXT

glGetColorTablebEXT = _color_table.glGetColorTablebEXT

glGetColorTableusEXT = _color_table.glGetColorTableusEXT

glGetColorTablesEXT = _color_table.glGetColorTablesEXT

glGetColorTableuiEXT = _color_table.glGetColorTableuiEXT

glGetColorTableiEXT = _color_table.glGetColorTableiEXT

glGetColorTablefEXT = _color_table.glGetColorTablefEXT

glInitColorTableEXT = _color_table.glInitColorTableEXT

__info = _color_table.__info
GL_COLOR_TABLE_EXT = _color_table.GL_COLOR_TABLE_EXT
GL_POST_CONVOLUTION_COLOR_TABLE_EXT = _color_table.GL_POST_CONVOLUTION_COLOR_TABLE_EXT
GL_POST_COLOR_MATRIX_COLOR_TABLE_EXT = _color_table.GL_POST_COLOR_MATRIX_COLOR_TABLE_EXT
GL_PROXY_COLOR_TABLE_EXT = _color_table.GL_PROXY_COLOR_TABLE_EXT
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_EXT = _color_table.GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_EXT
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_EXT = _color_table.GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_EXT
GL_COLOR_TABLE_SCALE_EXT = _color_table.GL_COLOR_TABLE_SCALE_EXT
GL_COLOR_TABLE_BIAS_EXT = _color_table.GL_COLOR_TABLE_BIAS_EXT
GL_COLOR_TABLE_FORMAT_EXT = _color_table.GL_COLOR_TABLE_FORMAT_EXT
GL_COLOR_TABLE_WIDTH_EXT = _color_table.GL_COLOR_TABLE_WIDTH_EXT
GL_COLOR_TABLE_RED_SIZE_EXT = _color_table.GL_COLOR_TABLE_RED_SIZE_EXT
GL_COLOR_TABLE_GREEN_SIZE_EXT = _color_table.GL_COLOR_TABLE_GREEN_SIZE_EXT
GL_COLOR_TABLE_BLUE_SIZE_EXT = _color_table.GL_COLOR_TABLE_BLUE_SIZE_EXT
GL_COLOR_TABLE_ALPHA_SIZE_EXT = _color_table.GL_COLOR_TABLE_ALPHA_SIZE_EXT
GL_COLOR_TABLE_LUMINANCE_SIZE_EXT = _color_table.GL_COLOR_TABLE_LUMINANCE_SIZE_EXT
GL_COLOR_TABLE_INTENSITY_SIZE_EXT = _color_table.GL_COLOR_TABLE_INTENSITY_SIZE_EXT

