# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _facet_normal

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


__version__ = _facet_normal.__version__
__date__ = _facet_normal.__date__
__api_version__ = _facet_normal.__api_version__
__author__ = _facet_normal.__author__
__doc__ = _facet_normal.__doc__

glFacetNormal3b = _facet_normal.glFacetNormal3b

glFacetNormal3d = _facet_normal.glFacetNormal3d

glFacetNormal3f = _facet_normal.glFacetNormal3f

glFacetNormal3i = _facet_normal.glFacetNormal3i

glFacetNormal3s = _facet_normal.glFacetNormal3s

glFacetNormal3bv = _facet_normal.glFacetNormal3bv

glFacetNormal3dv = _facet_normal.glFacetNormal3dv

glFacetNormal3fv = _facet_normal.glFacetNormal3fv

glFacetNormal3iv = _facet_normal.glFacetNormal3iv

glFacetNormal3sv = _facet_normal.glFacetNormal3sv

glInitFacetNormalAutodesk = _facet_normal.glInitFacetNormalAutodesk

__info = _facet_normal.__info
GL_FACET_NORMAL = _facet_normal.GL_FACET_NORMAL

