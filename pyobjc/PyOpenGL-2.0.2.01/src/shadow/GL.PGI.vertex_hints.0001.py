# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_hints

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


__version__ = _vertex_hints.__version__
__date__ = _vertex_hints.__date__
__api_version__ = _vertex_hints.__api_version__
__author__ = _vertex_hints.__author__
__doc__ = _vertex_hints.__doc__
GL_VERTEX_DATA_HINT_PGI = _vertex_hints.GL_VERTEX_DATA_HINT_PGI
GL_VERTEX_CONSISTENT_HINT_PGI = _vertex_hints.GL_VERTEX_CONSISTENT_HINT_PGI
GL_MATERIAL_SIDE_HINT_PGI = _vertex_hints.GL_MATERIAL_SIDE_HINT_PGI
GL_MAX_VERTEX_HINT_PGI = _vertex_hints.GL_MAX_VERTEX_HINT_PGI
GL_COLOR3_BIT_PGI = _vertex_hints.GL_COLOR3_BIT_PGI
GL_COLOR4_BIT_PGI = _vertex_hints.GL_COLOR4_BIT_PGI
GL_EDGEFLAG_BIT_PGI = _vertex_hints.GL_EDGEFLAG_BIT_PGI
GL_INDEX_BIT_PGI = _vertex_hints.GL_INDEX_BIT_PGI
GL_MAT_AMBIENT_BIT_PGI = _vertex_hints.GL_MAT_AMBIENT_BIT_PGI
GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI = _vertex_hints.GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI
GL_MAT_DIFFUSE_BIT_PGI = _vertex_hints.GL_MAT_DIFFUSE_BIT_PGI
GL_MAT_EMISSION_BIT_PGI = _vertex_hints.GL_MAT_EMISSION_BIT_PGI
GL_MAT_COLOR_INDEXES_BIT_PGI = _vertex_hints.GL_MAT_COLOR_INDEXES_BIT_PGI
GL_MAT_SHININESS_BIT_PGI = _vertex_hints.GL_MAT_SHININESS_BIT_PGI
GL_MAT_SPECULAR_BIT_PGI = _vertex_hints.GL_MAT_SPECULAR_BIT_PGI
GL_NORMAL_BIT_PGI = _vertex_hints.GL_NORMAL_BIT_PGI
GL_TEXCOORD1_BIT_PGI = _vertex_hints.GL_TEXCOORD1_BIT_PGI
GL_TEXCOORD2_BIT_PGI = _vertex_hints.GL_TEXCOORD2_BIT_PGI
GL_TEXCOORD3_BIT_PGI = _vertex_hints.GL_TEXCOORD3_BIT_PGI
GL_TEXCOORD4_BIT_PGI = _vertex_hints.GL_TEXCOORD4_BIT_PGI
GL_VERTEX23_BIT_PGI = _vertex_hints.GL_VERTEX23_BIT_PGI
GL_VERTEX4_BIT_PGI = _vertex_hints.GL_VERTEX4_BIT_PGI

glInitVertexHintsPGI = _vertex_hints.glInitVertexHintsPGI

__info = _vertex_hints.__info

