# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex

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


__version__ = _vertex.__version__
__date__ = _vertex.__date__
__api_version__ = _vertex.__api_version__
__author__ = _vertex.__author__
__doc__ = _vertex.__doc__

glColor4ubVertex2fSUN = _vertex.glColor4ubVertex2fSUN

glColor4ubVertex2fvSUN = _vertex.glColor4ubVertex2fvSUN

glColor4ubVertex3fSUN = _vertex.glColor4ubVertex3fSUN

glColor4ubVertex3fvSUN = _vertex.glColor4ubVertex3fvSUN

glColor3fVertex3fSUN = _vertex.glColor3fVertex3fSUN

glColor3fVertex3fvSUN = _vertex.glColor3fVertex3fvSUN

glNormal3fVertex3fSUN = _vertex.glNormal3fVertex3fSUN

glNormal3fVertex3fvSUN = _vertex.glNormal3fVertex3fvSUN

glColor4fNormal3fVertex3fSUN = _vertex.glColor4fNormal3fVertex3fSUN

glColor4fNormal3fVertex3fvSUN = _vertex.glColor4fNormal3fVertex3fvSUN

glTexCoord2fVertex3fSUN = _vertex.glTexCoord2fVertex3fSUN

glTexCoord2fVertex3fvSUN = _vertex.glTexCoord2fVertex3fvSUN

glTexCoord4fVertex4fSUN = _vertex.glTexCoord4fVertex4fSUN

glTexCoord4fVertex4fvSUN = _vertex.glTexCoord4fVertex4fvSUN

glTexCoord2fColor4ubVertex3fSUN = _vertex.glTexCoord2fColor4ubVertex3fSUN

glTexCoord2fColor4ubVertex3fvSUN = _vertex.glTexCoord2fColor4ubVertex3fvSUN

glTexCoord2fColor3fVertex3fSUN = _vertex.glTexCoord2fColor3fVertex3fSUN

glTexCoord2fColor3fVertex3fvSUN = _vertex.glTexCoord2fColor3fVertex3fvSUN

glTexCoord2fNormal3fVertex3fSUN = _vertex.glTexCoord2fNormal3fVertex3fSUN

glTexCoord2fNormal3fVertex3fvSUN = _vertex.glTexCoord2fNormal3fVertex3fvSUN

glTexCoord2fColor4fNormal3fVertex3fSUN = _vertex.glTexCoord2fColor4fNormal3fVertex3fSUN

glTexCoord2fColor4fNormal3fVertex3fvSUN = _vertex.glTexCoord2fColor4fNormal3fVertex3fvSUN

glTexCoord4fColor4fNormal3fVertex4fSUN = _vertex.glTexCoord4fColor4fNormal3fVertex4fSUN

glTexCoord4fColor4fNormal3fVertex4fvSUN = _vertex.glTexCoord4fColor4fNormal3fVertex4fvSUN

glReplacementCodeuiVertex3fSUN = _vertex.glReplacementCodeuiVertex3fSUN

glReplacementCodeuiVertex3fvSUN = _vertex.glReplacementCodeuiVertex3fvSUN

glReplacementCodeuiColor4ubVertex3fSUN = _vertex.glReplacementCodeuiColor4ubVertex3fSUN

glReplacementCodeuiColor4ubVertex3fvSUN = _vertex.glReplacementCodeuiColor4ubVertex3fvSUN

glReplacementCodeuiColor3fVertex3fSUN = _vertex.glReplacementCodeuiColor3fVertex3fSUN

glReplacementCodeuiColor3fVertex3fvSUN = _vertex.glReplacementCodeuiColor3fVertex3fvSUN

glReplacementCodeuiNormal3fVertex3fSUN = _vertex.glReplacementCodeuiNormal3fVertex3fSUN

glReplacementCodeuiNormal3fVertex3fvSUN = _vertex.glReplacementCodeuiNormal3fVertex3fvSUN

glReplacementCodeuiColor4fNormal3fVertex3fSUN = _vertex.glReplacementCodeuiColor4fNormal3fVertex3fSUN

glReplacementCodeuiColor4fNormal3fVertex3fvSUN = _vertex.glReplacementCodeuiColor4fNormal3fVertex3fvSUN

glReplacementCodeuiTexCoord2fVertex3fSUN = _vertex.glReplacementCodeuiTexCoord2fVertex3fSUN

glReplacementCodeuiTexCoord2fVertex3fvSUN = _vertex.glReplacementCodeuiTexCoord2fVertex3fvSUN

glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN = _vertex.glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN

glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN = _vertex.glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN

glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN = _vertex.glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN

glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN = _vertex.glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN

glInitVertexSUN = _vertex.glInitVertexSUN

__info = _vertex.__info

