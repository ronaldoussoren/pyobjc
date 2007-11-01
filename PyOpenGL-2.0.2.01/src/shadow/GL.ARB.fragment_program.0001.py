# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fragment_program

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


__version__ = _fragment_program.__version__
__date__ = _fragment_program.__date__
__api_version__ = _fragment_program.__api_version__
__author__ = _fragment_program.__author__
__doc__ = _fragment_program.__doc__
GL_FRAGMENT_PROGRAM_ARB = _fragment_program.GL_FRAGMENT_PROGRAM_ARB
GL_PROGRAM_ALU_INSTRUCTIONS_ARB = _fragment_program.GL_PROGRAM_ALU_INSTRUCTIONS_ARB
GL_PROGRAM_TEX_INSTRUCTIONS_ARB = _fragment_program.GL_PROGRAM_TEX_INSTRUCTIONS_ARB
GL_PROGRAM_TEX_INDIRECTIONS_ARB = _fragment_program.GL_PROGRAM_TEX_INDIRECTIONS_ARB
GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = _fragment_program.GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB
GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = _fragment_program.GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB
GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = _fragment_program.GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB
GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB
GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = _fragment_program.GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB
GL_MAX_TEXTURE_COORDS_ARB = _fragment_program.GL_MAX_TEXTURE_COORDS_ARB
GL_MAX_TEXTURE_IMAGE_UNITS_ARB = _fragment_program.GL_MAX_TEXTURE_IMAGE_UNITS_ARB

glInitFragmentProgramARB = _fragment_program.glInitFragmentProgramARB

__info = _fragment_program.__info

