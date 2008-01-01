# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _polynomial_ffd

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


__version__ = _polynomial_ffd.__version__
__date__ = _polynomial_ffd.__date__
__api_version__ = _polynomial_ffd.__api_version__
__author__ = _polynomial_ffd.__author__
__doc__ = _polynomial_ffd.__doc__

glDeformationMap3dSGIX = _polynomial_ffd.glDeformationMap3dSGIX

glDeformationMap3fSGIX = _polynomial_ffd.glDeformationMap3fSGIX

glDeformSGIX = _polynomial_ffd.glDeformSGIX

glLoadIdentityDeformationMapSGIX = _polynomial_ffd.glLoadIdentityDeformationMapSGIX
GL_GEOMETRY_DEFORMATION_SGIX = _polynomial_ffd.GL_GEOMETRY_DEFORMATION_SGIX
GL_TEXTURE_DEFORMATION_SGIX = _polynomial_ffd.GL_TEXTURE_DEFORMATION_SGIX
GL_DEFORMATIONS_MASK_SGIX = _polynomial_ffd.GL_DEFORMATIONS_MASK_SGIX
GL_MAX_DEFORMATION_ORDER_SGIX = _polynomial_ffd.GL_MAX_DEFORMATION_ORDER_SGIX

glInitPolynomialFfdSGIX = _polynomial_ffd.glInitPolynomialFfdSGIX

__info = _polynomial_ffd.__info

