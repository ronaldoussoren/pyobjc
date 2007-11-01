# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _half_float

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


__version__ = _half_float.__version__
__date__ = _half_float.__date__
__api_version__ = _half_float.__api_version__
__author__ = _half_float.__author__
__doc__ = _half_float.__doc__

glVertex2hNV = _half_float.glVertex2hNV

glVertex2hvNV = _half_float.glVertex2hvNV

glVertex3hNV = _half_float.glVertex3hNV

glVertex3hvNV = _half_float.glVertex3hvNV

glVertex4hNV = _half_float.glVertex4hNV

glVertex4hvNV = _half_float.glVertex4hvNV

glNormal3hNV = _half_float.glNormal3hNV

glNormal3hvNV = _half_float.glNormal3hvNV

glColor3hNV = _half_float.glColor3hNV

glColor3hvNV = _half_float.glColor3hvNV

glColor4hNV = _half_float.glColor4hNV

glColor4hvNV = _half_float.glColor4hvNV

glTexCoord1hNV = _half_float.glTexCoord1hNV

glTexCoord1hvNV = _half_float.glTexCoord1hvNV

glTexCoord2hNV = _half_float.glTexCoord2hNV

glTexCoord2hvNV = _half_float.glTexCoord2hvNV

glTexCoord3hNV = _half_float.glTexCoord3hNV

glTexCoord3hvNV = _half_float.glTexCoord3hvNV

glTexCoord4hNV = _half_float.glTexCoord4hNV

glTexCoord4hvNV = _half_float.glTexCoord4hvNV

glMultiTexCoord1hNV = _half_float.glMultiTexCoord1hNV

glMultiTexCoord1hvNV = _half_float.glMultiTexCoord1hvNV

glMultiTexCoord2hNV = _half_float.glMultiTexCoord2hNV

glMultiTexCoord2hvNV = _half_float.glMultiTexCoord2hvNV

glMultiTexCoord3hNV = _half_float.glMultiTexCoord3hNV

glMultiTexCoord3hvNV = _half_float.glMultiTexCoord3hvNV

glMultiTexCoord4hNV = _half_float.glMultiTexCoord4hNV

glMultiTexCoord4hvNV = _half_float.glMultiTexCoord4hvNV

glFogCoordhNV = _half_float.glFogCoordhNV

glFogCoordhvNV = _half_float.glFogCoordhvNV

glSecondaryColor3hNV = _half_float.glSecondaryColor3hNV

glSecondaryColor3hvNV = _half_float.glSecondaryColor3hvNV

glVertexWeighthNV = _half_float.glVertexWeighthNV

glVertexWeighthvNV = _half_float.glVertexWeighthvNV

glVertexAttrib1hNV = _half_float.glVertexAttrib1hNV

glVertexAttrib1hvNV = _half_float.glVertexAttrib1hvNV

glVertexAttrib2hNV = _half_float.glVertexAttrib2hNV

glVertexAttrib2hvNV = _half_float.glVertexAttrib2hvNV

glVertexAttrib3hNV = _half_float.glVertexAttrib3hNV

glVertexAttrib3hvNV = _half_float.glVertexAttrib3hvNV

glVertexAttrib4hNV = _half_float.glVertexAttrib4hNV

glVertexAttrib4hvNV = _half_float.glVertexAttrib4hvNV

glVertexAttribs1hvNV = _half_float.glVertexAttribs1hvNV

glVertexAttribs2hvNV = _half_float.glVertexAttribs2hvNV

glVertexAttribs3hvNV = _half_float.glVertexAttribs3hvNV

glVertexAttribs4hvNV = _half_float.glVertexAttribs4hvNV
GL_HALF_FLOAT_NV = _half_float.GL_HALF_FLOAT_NV

glInitHalfFloatNV = _half_float.glInitHalfFloatNV

__info = _half_float.__info

