# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _vertex_program

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


__version__ = _vertex_program.__version__
__date__ = _vertex_program.__date__
__api_version__ = _vertex_program.__api_version__
__author__ = _vertex_program.__author__
__doc__ = _vertex_program.__doc__

glVertexAttrib1dARB = _vertex_program.glVertexAttrib1dARB

glVertexAttrib1dvARB = _vertex_program.glVertexAttrib1dvARB

glVertexAttrib1fARB = _vertex_program.glVertexAttrib1fARB

glVertexAttrib1fvARB = _vertex_program.glVertexAttrib1fvARB

glVertexAttrib1sARB = _vertex_program.glVertexAttrib1sARB

glVertexAttrib1svARB = _vertex_program.glVertexAttrib1svARB

glVertexAttrib2dARB = _vertex_program.glVertexAttrib2dARB

glVertexAttrib2dvARB = _vertex_program.glVertexAttrib2dvARB

glVertexAttrib2fARB = _vertex_program.glVertexAttrib2fARB

glVertexAttrib2fvARB = _vertex_program.glVertexAttrib2fvARB

glVertexAttrib2sARB = _vertex_program.glVertexAttrib2sARB

glVertexAttrib2svARB = _vertex_program.glVertexAttrib2svARB

glVertexAttrib3dARB = _vertex_program.glVertexAttrib3dARB

glVertexAttrib3dvARB = _vertex_program.glVertexAttrib3dvARB

glVertexAttrib3fARB = _vertex_program.glVertexAttrib3fARB

glVertexAttrib3fvARB = _vertex_program.glVertexAttrib3fvARB

glVertexAttrib3sARB = _vertex_program.glVertexAttrib3sARB

glVertexAttrib3svARB = _vertex_program.glVertexAttrib3svARB

glVertexAttrib4NbvARB = _vertex_program.glVertexAttrib4NbvARB

glVertexAttrib4NivARB = _vertex_program.glVertexAttrib4NivARB

glVertexAttrib4NsvARB = _vertex_program.glVertexAttrib4NsvARB

glVertexAttrib4NubARB = _vertex_program.glVertexAttrib4NubARB

glVertexAttrib4NubvARB = _vertex_program.glVertexAttrib4NubvARB

glVertexAttrib4NuivARB = _vertex_program.glVertexAttrib4NuivARB

glVertexAttrib4NusvARB = _vertex_program.glVertexAttrib4NusvARB

glVertexAttrib4bvARB = _vertex_program.glVertexAttrib4bvARB

glVertexAttrib4dARB = _vertex_program.glVertexAttrib4dARB

glVertexAttrib4dvARB = _vertex_program.glVertexAttrib4dvARB

glVertexAttrib4fARB = _vertex_program.glVertexAttrib4fARB

glVertexAttrib4fvARB = _vertex_program.glVertexAttrib4fvARB

glVertexAttrib4ivARB = _vertex_program.glVertexAttrib4ivARB

glVertexAttrib4sARB = _vertex_program.glVertexAttrib4sARB

glVertexAttrib4svARB = _vertex_program.glVertexAttrib4svARB

glVertexAttrib4ubvARB = _vertex_program.glVertexAttrib4ubvARB

glVertexAttrib4uivARB = _vertex_program.glVertexAttrib4uivARB

glVertexAttrib4usvARB = _vertex_program.glVertexAttrib4usvARB

glVertexAttribPointerARB = _vertex_program.glVertexAttribPointerARB

glEnableVertexAttribArrayARB = _vertex_program.glEnableVertexAttribArrayARB

glDisableVertexAttribArrayARB = _vertex_program.glDisableVertexAttribArrayARB

glProgramStringARB = _vertex_program.glProgramStringARB

glBindProgramARB = _vertex_program.glBindProgramARB

glDeleteProgramsARB = _vertex_program.glDeleteProgramsARB

glGenProgramsARB = _vertex_program.glGenProgramsARB

glProgramEnvParameter4dARB = _vertex_program.glProgramEnvParameter4dARB

glProgramEnvParameter4dvARB = _vertex_program.glProgramEnvParameter4dvARB

glProgramEnvParameter4fARB = _vertex_program.glProgramEnvParameter4fARB

glProgramEnvParameter4fvARB = _vertex_program.glProgramEnvParameter4fvARB

glProgramLocalParameter4dARB = _vertex_program.glProgramLocalParameter4dARB

glProgramLocalParameter4dvARB = _vertex_program.glProgramLocalParameter4dvARB

glProgramLocalParameter4fARB = _vertex_program.glProgramLocalParameter4fARB

glProgramLocalParameter4fvARB = _vertex_program.glProgramLocalParameter4fvARB

glGetProgramEnvParameterdvARB = _vertex_program.glGetProgramEnvParameterdvARB

glGetProgramEnvParameterfvARB = _vertex_program.glGetProgramEnvParameterfvARB

glGetProgramLocalParameterdvARB = _vertex_program.glGetProgramLocalParameterdvARB

glGetProgramLocalParameterfvARB = _vertex_program.glGetProgramLocalParameterfvARB

glGetProgramivARB = _vertex_program.glGetProgramivARB

glGetProgramStringARB = _vertex_program.glGetProgramStringARB

glGetVertexAttribdvARB = _vertex_program.glGetVertexAttribdvARB

glGetVertexAttribfvARB = _vertex_program.glGetVertexAttribfvARB

glGetVertexAttribivARB = _vertex_program.glGetVertexAttribivARB

glGetVertexAttribPointervARB = _vertex_program.glGetVertexAttribPointervARB

glIsProgramARB = _vertex_program.glIsProgramARB
GL_COLOR_SUM_ARB = _vertex_program.GL_COLOR_SUM_ARB
GL_VERTEX_PROGRAM_ARB = _vertex_program.GL_VERTEX_PROGRAM_ARB
GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB
GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB
GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB
GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB
GL_CURRENT_VERTEX_ATTRIB_ARB = _vertex_program.GL_CURRENT_VERTEX_ATTRIB_ARB
GL_PROGRAM_LENGTH_ARB = _vertex_program.GL_PROGRAM_LENGTH_ARB
GL_PROGRAM_STRING_ARB = _vertex_program.GL_PROGRAM_STRING_ARB
GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB = _vertex_program.GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB
GL_MAX_PROGRAM_MATRICES_ARB = _vertex_program.GL_MAX_PROGRAM_MATRICES_ARB
GL_CURRENT_MATRIX_STACK_DEPTH_ARB = _vertex_program.GL_CURRENT_MATRIX_STACK_DEPTH_ARB
GL_CURRENT_MATRIX_ARB = _vertex_program.GL_CURRENT_MATRIX_ARB
GL_VERTEX_PROGRAM_POINT_SIZE_ARB = _vertex_program.GL_VERTEX_PROGRAM_POINT_SIZE_ARB
GL_VERTEX_PROGRAM_TWO_SIDE_ARB = _vertex_program.GL_VERTEX_PROGRAM_TWO_SIDE_ARB
GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB
GL_PROGRAM_ERROR_POSITION_ARB = _vertex_program.GL_PROGRAM_ERROR_POSITION_ARB
GL_PROGRAM_BINDING_ARB = _vertex_program.GL_PROGRAM_BINDING_ARB
GL_MAX_VERTEX_ATTRIBS_ARB = _vertex_program.GL_MAX_VERTEX_ATTRIBS_ARB
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = _vertex_program.GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB
GL_PROGRAM_ERROR_STRING_ARB = _vertex_program.GL_PROGRAM_ERROR_STRING_ARB
GL_PROGRAM_FORMAT_ASCII_ARB = _vertex_program.GL_PROGRAM_FORMAT_ASCII_ARB
GL_PROGRAM_FORMAT_ARB = _vertex_program.GL_PROGRAM_FORMAT_ARB
GL_PROGRAM_INSTRUCTIONS_ARB = _vertex_program.GL_PROGRAM_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_INSTRUCTIONS_ARB = _vertex_program.GL_MAX_PROGRAM_INSTRUCTIONS_ARB
GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB = _vertex_program.GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB
GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB = _vertex_program.GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB
GL_PROGRAM_TEMPORARIES_ARB = _vertex_program.GL_PROGRAM_TEMPORARIES_ARB
GL_MAX_PROGRAM_TEMPORARIES_ARB = _vertex_program.GL_MAX_PROGRAM_TEMPORARIES_ARB
GL_PROGRAM_NATIVE_TEMPORARIES_ARB = _vertex_program.GL_PROGRAM_NATIVE_TEMPORARIES_ARB
GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB = _vertex_program.GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB
GL_PROGRAM_PARAMETERS_ARB = _vertex_program.GL_PROGRAM_PARAMETERS_ARB
GL_MAX_PROGRAM_PARAMETERS_ARB = _vertex_program.GL_MAX_PROGRAM_PARAMETERS_ARB
GL_PROGRAM_NATIVE_PARAMETERS_ARB = _vertex_program.GL_PROGRAM_NATIVE_PARAMETERS_ARB
GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB = _vertex_program.GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB
GL_PROGRAM_ATTRIBS_ARB = _vertex_program.GL_PROGRAM_ATTRIBS_ARB
GL_MAX_PROGRAM_ATTRIBS_ARB = _vertex_program.GL_MAX_PROGRAM_ATTRIBS_ARB
GL_PROGRAM_NATIVE_ATTRIBS_ARB = _vertex_program.GL_PROGRAM_NATIVE_ATTRIBS_ARB
GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB = _vertex_program.GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB
GL_PROGRAM_ADDRESS_REGISTERS_ARB = _vertex_program.GL_PROGRAM_ADDRESS_REGISTERS_ARB
GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB = _vertex_program.GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB
GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = _vertex_program.GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB
GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = _vertex_program.GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB
GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB = _vertex_program.GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB
GL_MAX_PROGRAM_ENV_PARAMETERS_ARB = _vertex_program.GL_MAX_PROGRAM_ENV_PARAMETERS_ARB
GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB = _vertex_program.GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB
GL_TRANSPOSE_CURRENT_MATRIX_ARB = _vertex_program.GL_TRANSPOSE_CURRENT_MATRIX_ARB
GL_MATRIX0_ARB = _vertex_program.GL_MATRIX0_ARB
GL_MATRIX1_ARB = _vertex_program.GL_MATRIX1_ARB
GL_MATRIX2_ARB = _vertex_program.GL_MATRIX2_ARB
GL_MATRIX3_ARB = _vertex_program.GL_MATRIX3_ARB
GL_MATRIX4_ARB = _vertex_program.GL_MATRIX4_ARB
GL_MATRIX5_ARB = _vertex_program.GL_MATRIX5_ARB
GL_MATRIX6_ARB = _vertex_program.GL_MATRIX6_ARB
GL_MATRIX7_ARB = _vertex_program.GL_MATRIX7_ARB
GL_MATRIX8_ARB = _vertex_program.GL_MATRIX8_ARB
GL_MATRIX9_ARB = _vertex_program.GL_MATRIX9_ARB
GL_MATRIX10_ARB = _vertex_program.GL_MATRIX10_ARB
GL_MATRIX11_ARB = _vertex_program.GL_MATRIX11_ARB
GL_MATRIX12_ARB = _vertex_program.GL_MATRIX12_ARB
GL_MATRIX13_ARB = _vertex_program.GL_MATRIX13_ARB
GL_MATRIX14_ARB = _vertex_program.GL_MATRIX14_ARB
GL_MATRIX15_ARB = _vertex_program.GL_MATRIX15_ARB
GL_MATRIX16_ARB = _vertex_program.GL_MATRIX16_ARB
GL_MATRIX17_ARB = _vertex_program.GL_MATRIX17_ARB
GL_MATRIX18_ARB = _vertex_program.GL_MATRIX18_ARB
GL_MATRIX19_ARB = _vertex_program.GL_MATRIX19_ARB
GL_MATRIX20_ARB = _vertex_program.GL_MATRIX20_ARB
GL_MATRIX21_ARB = _vertex_program.GL_MATRIX21_ARB
GL_MATRIX22_ARB = _vertex_program.GL_MATRIX22_ARB
GL_MATRIX23_ARB = _vertex_program.GL_MATRIX23_ARB
GL_MATRIX24_ARB = _vertex_program.GL_MATRIX24_ARB
GL_MATRIX25_ARB = _vertex_program.GL_MATRIX25_ARB
GL_MATRIX26_ARB = _vertex_program.GL_MATRIX26_ARB
GL_MATRIX27_ARB = _vertex_program.GL_MATRIX27_ARB
GL_MATRIX28_ARB = _vertex_program.GL_MATRIX28_ARB
GL_MATRIX29_ARB = _vertex_program.GL_MATRIX29_ARB
GL_MATRIX30_ARB = _vertex_program.GL_MATRIX30_ARB
GL_MATRIX31_ARB = _vertex_program.GL_MATRIX31_ARB

glInitVertexProgramARB = _vertex_program.glInitVertexProgramARB

__info = _vertex_program.__info

