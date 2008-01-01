# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _subtexture

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


__version__ = _subtexture.__version__
__date__ = _subtexture.__date__
__api_version__ = _subtexture.__api_version__
__author__ = _subtexture.__author__
__doc__ = _subtexture.__doc__

glTexSubImage1DEXT = _subtexture.glTexSubImage1DEXT

glTexSubImage1DubEXT = _subtexture.glTexSubImage1DubEXT

glTexSubImage1DbEXT = _subtexture.glTexSubImage1DbEXT

glTexSubImage1DusEXT = _subtexture.glTexSubImage1DusEXT

glTexSubImage1DsEXT = _subtexture.glTexSubImage1DsEXT

glTexSubImage1DuiEXT = _subtexture.glTexSubImage1DuiEXT

glTexSubImage1DiEXT = _subtexture.glTexSubImage1DiEXT

glTexSubImage1DfEXT = _subtexture.glTexSubImage1DfEXT

glTexSubImage2DEXT = _subtexture.glTexSubImage2DEXT

glTexSubImage2DubEXT = _subtexture.glTexSubImage2DubEXT

glTexSubImage2DbEXT = _subtexture.glTexSubImage2DbEXT

glTexSubImage2DusEXT = _subtexture.glTexSubImage2DusEXT

glTexSubImage2DsEXT = _subtexture.glTexSubImage2DsEXT

glTexSubImage2DuiEXT = _subtexture.glTexSubImage2DuiEXT

glTexSubImage2DiEXT = _subtexture.glTexSubImage2DiEXT

glTexSubImage2DfEXT = _subtexture.glTexSubImage2DfEXT

glTexSubImage3DEXT = _subtexture.glTexSubImage3DEXT

glTexSubImage3DubEXT = _subtexture.glTexSubImage3DubEXT

glTexSubImage3DbEXT = _subtexture.glTexSubImage3DbEXT

glTexSubImage3DusEXT = _subtexture.glTexSubImage3DusEXT

glTexSubImage3DsEXT = _subtexture.glTexSubImage3DsEXT

glTexSubImage3DuiEXT = _subtexture.glTexSubImage3DuiEXT

glTexSubImage3DiEXT = _subtexture.glTexSubImage3DiEXT

glTexSubImage3DfEXT = _subtexture.glTexSubImage3DfEXT

glInitSubtextureEXT = _subtexture.glInitSubtextureEXT

glInitSubTexEXT = _subtexture.glInitSubTexEXT

__info = _subtexture.__info

