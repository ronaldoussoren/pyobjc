/*
# BUILD api_versions [0x104]
*/

%module register_combiners

#define __version__ "$Revision: 1.20.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057NV\057register_combiners.txt"

%{
/**
 *
 * GL.NV.register_combiners Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_register_combiners)
DECLARE_VOID_EXT(glCombinerParameterfvNV, (GLenum pname, const GLfloat *params), (pname, params))
DECLARE_VOID_EXT(glCombinerParameterivNV, (GLenum pname, const GLint *params), (pname, params))
DECLARE_VOID_EXT(glCombinerParameterfNV, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glCombinerParameteriNV, (GLenum pname, GLint param), (pname, param))
DECLARE_VOID_EXT(glCombinerInputNV,\
	(GLenum stage, GLenum portion, GLenum variable, GLenum input, GLenum mapping, GLenum componentUsage),\
	(stage, portion, variable, input, mapping, componentUsage))
DECLARE_VOID_EXT(glCombinerOutputNV,\
	(GLenum stage, GLenum portion, GLenum abOutput, GLenum cdOutput, GLenum sumOutput, GLenum scale, GLenum bias, GLboolean abDotProduct, GLboolean cdDotProduct, GLboolean muxSum),\
	(stage, portion, abOutput, cdOutput, sumOutput, scale, bias, abDotProduct, cdDotProduct, muxSum))
DECLARE_VOID_EXT(glFinalCombinerInputNV,\
	(GLenum variable, GLenum input, GLenum mapping, GLenum componentUsage),\
	(variable, input, mapping, componentUsage))
DECLARE_VOID_EXT(glGetCombinerInputParameterfvNV,\
	(GLenum stage, GLenum portion, GLenum variable, GLenum pname, GLfloat *params),\
	(stage, portion, variable, pname, params))
DECLARE_VOID_EXT(glGetCombinerInputParameterivNV,\
	(GLenum stage, GLenum portion, GLenum variable, GLenum pname, GLint *params),\
	(stage, portion, variable, pname, params))
DECLARE_VOID_EXT(glGetCombinerOutputParameterfvNV,\
	(GLenum stage, GLenum portion, GLenum pname, GLfloat *params),\
	(stage, portion, pname, params))
DECLARE_VOID_EXT(glGetCombinerOutputParameterivNV,\
	(GLenum stage, GLenum portion, GLenum pname, GLint *params),\
	(stage, portion, pname, params))
DECLARE_VOID_EXT(glGetFinalCombinerInputParameterfvNV,\
	(GLenum variable, GLenum pname, GLfloat *params),\
	(variable, pname, params))
DECLARE_VOID_EXT(glGetFinalCombinerInputParameterivNV,\
	(GLenum variable, GLenum pname, GLint *params),\
	(variable, pname, params))
#endif
%}

void glCombinerParameterfvNV(GLenum pname, const GLfloat *params);
DOC(glCombinerParameterfvNV, "glCombinerParameterfvNV(pname, params) -> None")

void glCombinerParameterivNV(GLenum pname, const GLint *params);
DOC(glCombinerParameterivNV, "glCombinerParameterivNV(pname, params) -> None")

void glCombinerParameterfNV(GLenum pname, GLfloat param);
DOC(glCombinerParameterfNV, "glCombinerParameterfNV(pname, param) -> None")

void glCombinerParameteriNV(GLenum pname, GLint param);
DOC(glCombinerParameteriNV, "glCombinerParameteriNV(pname, param) -> None")

void glCombinerInputNV(GLenum stage, GLenum portion, GLenum variable, GLenum input, GLenum mapping, GLenum componentUsage);
DOC(glCombinerInputNV, "glCombinerInputNV(stage, portion, variable, input, mapping, componentUsage) -> None")

void glCombinerOutputNV(GLenum stage, GLenum portion, GLenum abOutput, GLenum cdOutput, GLenum sumOutput, GLenum scale, GLenum bias, GLboolean abDotProduct, GLboolean cdDotProduct, GLboolean muxSum);
DOC(glCombinerOutputNV, "glCombinerOutputNV(stage, portion, abOutput, cdOutput, sumOutput, scale, bias, abDotProduct, cdDotProduct, muxSum) -> None")

void glFinalCombinerInputNV(GLenum variable, GLenum input, GLenum mapping, GLenum componentUsage);
DOC(glFinalCombinerInputNV, "glFinalCombinerInputNV(variable, input, mapping, componentUsage) -> None")

void glGetCombinerInputParameterfvNV(GLenum stage, GLenum portion, GLenum variable, GLenum pname, GLfloat params[4]);
DOC(glGetCombinerInputParameterfvNV, "glGetCombinerInputParameterfvNV(stage, portion, variable, pname) -> params")

void glGetCombinerInputParameterivNV(GLenum stage, GLenum portion, GLenum variable, GLenum pname, GLint params[4]);
DOC(glGetCombinerInputParameterivNV, "glGetCombinerInputParameterivNV(stage, portion, variable, pname) -> params")

void glGetCombinerOutputParameterfvNV(GLenum stage, GLenum portion, GLenum pname, GLfloat params[4]);
DOC(glGetCombinerOutputParameterfvNV, "glGetCombinerOutputParameterfvNV(stage, portion, pname) -> params")

void glGetCombinerOutputParameterivNV(GLenum stage, GLenum portion, GLenum pname, GLint params[4]);
DOC(glGetCombinerOutputParameterivNV, "glGetCombinerOutputParameterivNV(stage, portion, pname) -> params")

void glGetFinalCombinerInputParameterfvNV(GLenum variable, GLenum pname, GLfloat params[4]);
DOC(glGetFinalCombinerInputParameterfvNV, "glGetFinalCombinerInputParameterfvNV(variable, pname) -> params")

void glGetFinalCombinerInputParameterivNV(GLenum variable, GLenum pname, GLint params[4]);
DOC(glGetFinalCombinerInputParameterivNV, "glGetFinalCombinerInputParameterivNV(variable, pname) -> params")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_register_combiners)
	"glCombinerParameterfvNV",
	"glCombinerParameterivNV",
	"glCombinerParameterfNV",
	"glCombinerParameteriNV",
	"glCombinerInputNV",
	"glCombinerOutputNV",
	"glFinalCombinerInputNV",
	"glGetCombinerInputParameterfvNV",
	"glGetCombinerInputParameterivNV",
	"glGetCombinerOutputParameterfvNV",
	"glGetCombinerOutputParameterivNV",
	"glGetFinalCombinerInputParameterfvNV",
	"glGetFinalCombinerInputParameterivNV",
#endif
	NULL
};

#define glInitRegisterCombinersNV() InitExtension("GL_NV_register_combiners", proc_names)
%}

int glInitRegisterCombinersNV();
DOC(glInitRegisterCombinersNV, "glInitRegisterCombinersNV() -> bool")


%{
#ifndef GL_NV_register_combiners
#define GL_MAX_GENERAL_COMBINERS_NV           0x854D
#endif

PyObject *__info()
{
	if (glInitRegisterCombinersNV())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_GENERAL_COMBINERS_NV", GL_MAX_GENERAL_COMBINERS_NV, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_ALL_COMPLETED_NV                   0x84F2

#define GL_REGISTER_COMBINERS_NV              0x8522

#define GL_COMBINER0_NV                       0x8550
#define GL_COMBINER1_NV                       0x8551
#define GL_COMBINER2_NV                       0x8552
#define GL_COMBINER3_NV                       0x8553
#define GL_COMBINER4_NV                       0x8554
#define GL_COMBINER5_NV                       0x8555
#define GL_COMBINER6_NV                       0x8556
#define GL_COMBINER7_NV                       0x8557

#define GL_VARIABLE_A_NV                      0x8523
#define GL_VARIABLE_B_NV                      0x8524
#define GL_VARIABLE_C_NV                      0x8525
#define GL_VARIABLE_D_NV                      0x8526
#define GL_VARIABLE_E_NV                      0x8527
#define GL_VARIABLE_F_NV                      0x8528
#define GL_VARIABLE_G_NV                      0x8529

#define GL_CONSTANT_COLOR0_NV                 0x852A
#define GL_CONSTANT_COLOR1_NV                 0x852B
#define GL_PRIMARY_COLOR_NV                   0x852C
#define GL_SECONDARY_COLOR_NV                 0x852D
#define GL_SPARE0_NV                          0x852E
#define GL_SPARE1_NV                          0x852F

#define GL_UNSIGNED_IDENTITY_NV               0x8536
#define GL_UNSIGNED_INVERT_NV                 0x8537
#define GL_EXPAND_NORMAL_NV                   0x8538
#define GL_EXPAND_NEGATE_NV                   0x8539
#define GL_HALF_BIAS_NORMAL_NV                0x853A
#define GL_HALF_BIAS_NEGATE_NV                0x853B
#define GL_SIGNED_IDENTITY_NV                 0x853C
#define GL_SIGNED_NEGATE_NV                   0x853D

#define GL_E_TIMES_F_NV                       0x8531
#define GL_SPARE0_PLUS_SECONDARY_COLOR_NV     0x8532

#define GL_SCALE_BY_TWO_NV                    0x853E
#define GL_SCALE_BY_FOUR_NV                   0x853F
#define GL_SCALE_BY_ONE_HALF_NV               0x8540

#define GL_BIAS_BY_NEGATIVE_ONE_HALF_NV       0x8541

#define GL_DISCARD_NV                         0x8530

#define GL_COMBINER_INPUT_NV                  0x8542
#define GL_COMBINER_MAPPING_NV                0x8543
#define GL_COMBINER_COMPONENT_USAGE_NV        0x8544

#define GL_COMBINER_AB_DOT_PRODUCT_NV         0x8545
#define GL_COMBINER_CD_DOT_PRODUCT_NV         0x8546
#define GL_COMBINER_MUX_SUM_NV                0x8547
#define GL_COMBINER_SCALE_NV                  0x8548
#define GL_COMBINER_BIAS_NV                   0x8549
#define GL_COMBINER_AB_OUTPUT_NV              0x854A
#define GL_COMBINER_CD_OUTPUT_NV              0x854B
#define GL_COMBINER_SUM_OUTPUT_NV             0x854C

#define GL_NUM_GENERAL_COMBINERS_NV           0x854E
#define GL_COLOR_SUM_CLAMP_NV                 0x854F

#define GL_MAX_GENERAL_COMBINERS_NV           0x854D
