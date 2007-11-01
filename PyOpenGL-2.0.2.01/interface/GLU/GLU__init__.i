/*
# BUILD api_versions [0x100, 0x101, 0x102, 0x103]
# BUILD macro_template 'defined(GLU_VERSION_%(api_version_underscore)s)'
# BUILD shadow 1
*/

%module GLU__init__

#define __version__ "$Revision: 1.1.4.3 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057www.opengl.org\057developers\057documentation\057glx.html"

%{
/**
 *
 * GLU Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/

/* License from SGI's OpenGL® Sample Implementation */

/*
# License Applicability. Except to the extent portions of this file are
# made subject to an alternative license as permitted in the SGI Free
# Software License B, Version 1.1 (the "License"), the contents of this
# file are subject only to the provisions of the License. You may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at Silicon Graphics, Inc., attn: Legal Services, 1600
# Amphitheatre Parkway, Mountain View, CA 94043-1351, or at:
#
# http://oss.sgi.com/projects/FreeB
#
# Note that, as provided in the License, the Software is distributed on an
# "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS
# DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND
# CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A
# PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
#
# Original Code. The Original Code is: OpenGL Sample Implementation,
# Version 1.2.1, released January 26, 2000, developed by Silicon Graphics,
# Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc.
# Copyright in any portions created by third parties is as indicated
# elsewhere herein. All Rights Reserved.
#
# Additional Notice Provisions: The application programming interfaces
# established by SGI in conjunction with the Original Code are The
# OpenGL(R) Graphics System: A Specification (Version 1.2.1), released
# April 1, 1999; The OpenGL(R) Graphics System Utility Library (Version
# 1.3), released November 4, 1998; and OpenGL(R) Graphics with the X
# Window System(R) (Version 1.3), released October 19, 1998. This software
# was created using the OpenGL(R) version 1.2.1 Sample Implementation
# published by SGI, but has not been independently verified as being
# compliant with the OpenGL(R) version 1.2.1 Specification.
*/
%}


%include util.inc

%init %{
PyDict_SetItemString(d, "GLUerror", GLUerror);
%}
%{
void __ignoreDeletionCall(PyObject * tess ) {
}
%}



%shadow %{
#-------------- SHADOW WRAPPERS ------------------
%}


%{
typedef void (CALLBACK *callback)();
%}


/* yes we need this, GLU often doesn't clear GL errors */
%include gl_exception_handler.inc


/*
# gluErrorString
# 
# Python binding unchanged from spec.
*/

const GLubyte* gluErrorString(GLenum errCode);
DOC(gluErrorString, "gluErrorString(errCode) -> string")

/* this isn't working right now! */
/*const wchar_t* gluErrorUnicodeStringEXT(GLenum errCode); */
/*DOC(gluErrorUnicodeStringEXT, "gluErrorUnicodeStringEXT(errCode) -> string") */


/*
# gluGetString
# 
# Python binding unchanged from spec.
*/

#if API_VERSION >= 257
const GLubyte* gluGetString(GLenum name);
DOC(gluGetString, "gluGetString(name) -> string")
#endif


/*
# gluCheckExtension
# 
# Python binding unchanged from spec.
*/

#if API_VERSION >= 259 /* GLU 1.3 */
GLboolean gluCheckExtension( const char *extName, const char *extString );
DOC(gluCheckExtension, "gluCheckExtension(extName, extString) -> bool")
#endif


/*
# gluOrtho2D
# 
# Python binding unchanged from spec.
*/

void gluOrtho2D(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top);
DOC(gluOrtho2D, "gluOrtho2D(left, right, bottom, top) -> None")


/*
# gluPerspective
# 
# Python binding unchanged from spec.
*/

void gluPerspective(GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar);
DOC(gluPerspective, "gluPerspective(fovy, aspect, zNear, zFar) -> None")


/*
# gluPickMatrix
# 
# Python binding unchanged from spec, except "viewport" parameter is a keyword
*/

%{
void __gluPickMatrix(GLdouble x, GLdouble y, GLdouble width, GLdouble height, const GLint *viewport)
{
	GLint _viewport[4];

	if (!viewport)
	{
		glGetIntegerv(GL_VIEWPORT, _viewport);
		viewport = _viewport;
	}
	
	gluPickMatrix(x, y, width, height, (GLint*)viewport);
}
%}

void __gluPickMatrix(GLdouble x, GLdouble y, GLdouble width, GLdouble height, const GLint *viewport);


%shadow %{
def gluPickMatrix(x, y, width, height, viewport = None):
    'gluPickMatrix(x, y, width, height, viewport = None) -> None'
    return __gluPickMatrix(x, y, width, height, viewport)
%}


/*
# gluLookAt
# 
# Python binding unchanged from spec.
*/

void gluLookAt(GLdouble eyex, GLdouble eyey, GLdouble eyez, GLdouble centerx, GLdouble centery, GLdouble centerz,
               GLdouble upx, GLdouble upy, GLdouble upz);
DOC(gluLookAt, "gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz) -> None")


/*
# gluProject
# 
# Python binding unchanged from spec, except "modelMatrix", "projMatrix", and "viewport"
# parameters are keywords.
*/

%{
PyObject* __gluProject(GLdouble objx, GLdouble objy, GLdouble objz, const GLdouble *modelMatrix, const GLdouble *projMatrix, const GLint *viewport)
{
	GLdouble win[3], _modelMatrix[16], _projMatrix[16];
	GLint _viewport[4];

	if (!modelMatrix)
	{
		glGetDoublev(GL_MODELVIEW_MATRIX, _modelMatrix);
		modelMatrix = _modelMatrix;
	}
	
	if (!projMatrix)
	{
		glGetDoublev(GL_PROJECTION_MATRIX, _projMatrix);
		projMatrix = _projMatrix;
	}
	
	if (!viewport)
	{
		glGetIntegerv(GL_VIEWPORT, _viewport);
		viewport = _viewport;
	}

	if (gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport, win, win + 1, win + 2))
	{
		return _PyTuple_FromDoubleArray(3, win);
	}
	PyErr_SetGLUerror( GL_INVALID_VALUE );
	return NULL;
}
%}

PyObject* __gluProject(GLdouble objx, GLdouble objy, GLdouble objz, const GLdouble *modelMatrix, const GLdouble *projMatrix, const GLint *viewport);


%shadow %{
def gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluProject(objx, objy, objz, modelMatrix = None, projMatrix = None, viewport = None) -> (winx, winy, winz)'
    return __gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport)
%}



/*
# gluUnProject
# 
# Python binding unchanged from spec, except "modelMatrix", "projMatrix", and "viewport"
# parameters are keywords.
*/

%{
PyObject* __gluUnProject(GLdouble winx, GLdouble winy, GLdouble winz, const GLdouble *modelMatrix, const GLdouble *projMatrix, const GLint *viewport)
{
	GLdouble obj[3], _modelMatrix[16], _projMatrix[16];
	GLint _viewport[4];

	if (!modelMatrix)
	{
		glGetDoublev(GL_MODELVIEW_MATRIX, _modelMatrix);
		modelMatrix = _modelMatrix;
	}
	
	if (!projMatrix)
	{
		glGetDoublev(GL_PROJECTION_MATRIX, _projMatrix);
		projMatrix = _projMatrix;
	}
	
	if (!viewport)
	{
		glGetIntegerv(GL_VIEWPORT, _viewport);
		viewport = _viewport;
	}

	if (gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport, obj, obj + 1, obj + 2))
	{
		return _PyTuple_FromDoubleArray(3, obj);
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject* __gluUnProject(GLdouble winx, GLdouble winy, GLdouble winz, const GLdouble *modelMatrix, const GLdouble *projMatrix,
                 const GLint *viewport);

%shadow %{
def gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None):
    'gluUnProject(winx, winy, winz, modelMatrix = None, projMatrix = None, viewport = None) -> (objx, objy, objz)'
    return __gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport)
%}



/*
# gluUnProject4
# 
# Python binding unchanged from spec, except "modelMatrix", "projMatrix", "viewport",
# "near", and "far" parameters are keywords.
*/

#if API_VERSION >= 259
%{
PyObject* __gluUnProject4(GLdouble winx, GLdouble winy, GLdouble winz, GLdouble clipW, const GLdouble *modelMatrix, const GLdouble *projMatrix, const GLint *viewport, GLclampd near, GLclampd far)
{
	GLdouble obj[4], _modelMatrix[16], _projMatrix[16];
	GLint _viewport[4];

	if (!modelMatrix)
	{
		glGetDoublev(GL_MODELVIEW_MATRIX, _modelMatrix);
		modelMatrix = _modelMatrix;
	}
	
	if (!projMatrix)
	{
		glGetDoublev(GL_PROJECTION_MATRIX, _projMatrix);
		projMatrix = _projMatrix;
	}
	
	if (!viewport)
	{
		glGetIntegerv(GL_VIEWPORT, _viewport);
		viewport = _viewport;
	}

	if (gluUnProject4(winx, winy, winz, clipW, modelMatrix, projMatrix, viewport, near, far, obj, obj + 1, obj + 2, obj + 3))
	{
		return _PyTuple_FromDoubleArray(4, obj);
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject* __gluUnProject4(GLdouble winx, GLdouble winy, GLdouble winz, GLdouble clipW, const GLdouble *modelMatrix, const GLdouble *projMatrix,
                 const GLint *viewport, GLclampd near, GLclampd far);


%shadow %{
def gluUnProject4(winx, winy, winz, clipW, modelMatrix = None, projMatrix = None, viewport = None, near = 0.0, far = 1.0):
    'gluUnProject4(winx, winy, winz, clipW, modelMatrix = None, projMatrix = None, viewport = None, near = 0.0, far = 1.0) -> (objx, objy, objz, objw)'
    return __gluUnProject4(winx, winy, winz, clipW, modelMatrix, projMatrix, viewport, near, far)
%}


#endif


/*
# gluScaleImage
# 
# Python binding unchanged from spec with the addition of the decorated variants which omit all width, height or type
# parameters and ignore pixel storage settings.
*/

%{
PyObject* _gluScaleImage(GLenum format, GLint widthin, GLint heightin, GLenum typein, const void *datain, GLint widthout,
                  GLint heightout, GLenum typeout)
{
	PyObject* result;
	int code, dims[2];
	int size;
	void* dataout;
	
	dims[0] = widthout;
	dims[1] = heightout;
	
	dataout = SetupRawPixelRead(format, typeout, 2, dims, &size);
	if (!dataout) return NULL;

	code = gluScaleImage(format, widthin, heightin, typein, datain, widthout, heightout, typeout, dataout);

	if (code)
	{
		PyMem_Del(dataout);
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	result = PyString_FromStringAndSize((const char*)dataout, size);
	PyMem_Del(dataout);

	return result;
}

PyObject* __gluScaleImage(GLenum format, GLint widthin, GLint heightin, GLenum type, const void *datain, GLint widthout, GLint heightout)
{
	int dims[3], code;
	void *dataout;

	SetupPixelWrite(2);

	dims[0] = widthout;
	dims[1] = heightout;
	
	dataout = SetupPixelRead(2, format, type, dims);
	if (!dataout) return NULL;
	
	code = gluScaleImage(format, widthin, heightin, type, datain, widthout, heightout, type, dataout);

	if (code)
	{
		PyMem_Del(dataout);
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	return _PyObject_FromArray(type, (dims[2] == 1) ? 2 : 3, dims, dataout, 1);
}
%}

%name(gluScaleImage) PyObject* _gluScaleImage(GLenum format, GLint widthin, GLint heightin, GLenum typein, PyObject *datain, GLint widthout,
                  GLint heightout, GLenum typeout);
DOC(gluScaleImage, "gluScaleImage(format, widthin, heightin, typein, datain, widthout, heightout, typeout) -> dataout")

%name(gluScaleImageb) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_BYTE, const GLbyte* datain, GLint widthout, GLint heightout);
DOC(gluScaleImageb, "gluScaleImageb(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImageub) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_UNSIGNED_BYTE, const GLubyte* datain, GLint widthout, GLint heightout);
DOC(gluScaleImageub, "gluScaleImageub(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImages) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_SHORT, const GLshort* datain, GLint widthout, GLint heightout);
DOC(gluScaleImages, "gluScaleImages(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImageus) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_UNSIGNED_SHORT, const GLushort* datain, GLint widthout, GLint heightout);
DOC(gluScaleImageus, "gluScaleImageus(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImagei) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_INT, const GLint* datain, GLint widthout, GLint heightout);
DOC(gluScaleImagei, "gluScaleImagei(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImageui) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_UNSIGNED_INT, const GLuint* datain, GLint widthout, GLint heightout);
DOC(gluScaleImageui, "gluScaleImageui(format, datain, widthout, heightout) -> dataout")

%name(gluScaleImagef) PyObject *__gluScaleImage(GLenum format, GLint d_4_1, GLint d_4_0, GLenum type_FLOAT, const GLfloat* datain, GLint widthout, GLint heightout);
DOC(gluScaleImagef, "gluScaleImagef(format, datain, widthout, heightout) -> dataout")


/*
# gluBuild1DMipmaps
# 
# Python binding unchanged from spec with the addition of the decorated variants which omit all width, height or type
# parameters and ignore pixel storage settings.
*/

%{
PyObject* _gluBuild1DMipmaps(GLenum target, GLint components, GLint width, GLenum format, GLenum type, const void *buffer)
{
	int code;

	code = gluBuild1DMipmaps(target, components, width, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild1DMipmaps) PyObject* _gluBuild1DMipmaps(GLenum target, GLint components, GLint width, GLenum format, GLenum type, const void *buffer);
DOC(gluBuild1DMipmaps, "gluBuild1DMipmaps(target, components, width, format, type, data) -> None")

%{
PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint width, GLenum format, GLenum type, const void *buffer)
{
	int code;

	SetupPixelWrite(1);
	code = gluBuild1DMipmaps(target, components, width, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild1DMipmapsb) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_BYTE, const GLbyte *buffer);
DOC(gluBuild1DMipmapsb, "gluBuild1DMipmapsb(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapsub) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *buffer);
DOC(gluBuild1DMipmapsub, "gluBuild1DMipmapsub(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapss) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_SHORT, const GLshort *buffer);
DOC(gluBuild1DMipmapss, "gluBuild1DMipmapss(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapsus) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *buffer);
DOC(gluBuild1DMipmapsus, "gluBuild1DMipmapsus(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapsi) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_INT, const GLint *buffer);
DOC(gluBuild1DMipmapsi, "gluBuild1DMipmapsi(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapsui) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *buffer);
DOC(gluBuild1DMipmapsui, "gluBuild1DMipmapsui(target, components, format, pixels) -> None")

%name(gluBuild1DMipmapsf) PyObject *__gluBuild1DMipmaps(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_FLOAT, const GLshort *buffer);
DOC(gluBuild1DMipmapsf, "gluBuild1DMipmapsf(target, components, format, pixels) -> None")


/*
# gluBuild2DMipmaps
# 
# Python binding unchanged from spec with the addition of the decorated variants which omit all width, height or type
# parameters and ignore pixel storage settings.
*/

%{
PyObject* _gluBuild2DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, const void *buffer)
{
	int code;
	
	code = gluBuild2DMipmaps(target, components, width, height, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild2DMipmaps) PyObject* _gluBuild2DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, const void *buffer);
DOC(gluBuild2DMipmaps, "gluBuild2DMipmaps(target, components, width, height, format, type, data) -> None")

%{
PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, const void *buffer)
{
	int code;

	SetupPixelWrite(2);
	code = gluBuild2DMipmaps(target, components, width, height, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild2DMipmapsb) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_BYTE, const GLbyte *buffer);
DOC(gluBuild2DMipmapsb, "gluBuild2DMipmapsb(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapsub) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *buffer);
DOC(gluBuild2DMipmapsub, "gluBuild2DMipmapsub(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapss) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_SHORT, const GLshort *buffer);
DOC(gluBuild2DMipmapss, "gluBuild2DMipmapss(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapsus) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *buffer);
DOC(gluBuild2DMipmapsus, "gluBuild2DMipmapsus(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapsi) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_INT, const GLint *buffer);
DOC(gluBuild2DMipmapsi, "gluBuild2DMipmapsi(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapsui) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *buffer);
DOC(gluBuild2DMipmapsui, "gluBuild2DMipmapsui(target, components, format, pixels) -> None")

%name(gluBuild2DMipmapsf) PyObject *__gluBuild2DMipmaps(GLenum target, GLint components, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_FLOAT, const GLshort *buffer);
DOC(gluBuild2DMipmapsf, "gluBuild2DMipmapsf(target, components, format, pixels) -> None")


/*
# gluBuild3DMipmaps
# 
# Python binding unchanged from spec with the addition of the decorated variants which omit all width, height or type
# parameters and ignore pixel storage settings.
*/

#if API_VERSION >= 259
%{
PyObject* _gluBuild3DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, const void *buffer)
{
	int code;
	
	code = gluBuild3DMipmaps(target, components, width, height, depth, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild3DMipmaps) PyObject* _gluBuild3DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, const void *buffer);
DOC(gluBuild3DMipmaps, "gluBuild3DMipmaps(target, components, width, height, depth, format, type, data) -> None")

%{
PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, const void *buffer)
{
	int code;

	SetupPixelWrite(2);
	code = gluBuild3DMipmaps(target, components, width, height, depth, format, type, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild3DMipmapsb) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_BYTE, const GLbyte *buffer);
DOC(gluBuild3DMipmapsb, "gluBuild3DMipmapsb(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapsub) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *buffer);
DOC(gluBuild3DMipmapsub, "gluBuild3DMipmapsub(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapss) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_SHORT, const GLshort *buffer);
DOC(gluBuild3DMipmapss, "gluBuild3DMipmapss(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapsus) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *buffer);
DOC(gluBuild3DMipmapsus, "gluBuild3DMipmapsus(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapsi) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_INT, const GLint *buffer);
DOC(gluBuild3DMipmapsi, "gluBuild3DMipmapsi(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapsui) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *buffer);
DOC(gluBuild3DMipmapsui, "gluBuild3DMipmapsui(target, components, format, pixels) -> None")

%name(gluBuild3DMipmapsf) PyObject *__gluBuild3DMipmaps(GLenum target, GLint components, GLint d_6_2, GLint d_6_1, GLint d_6_0, GLenum format, GLenum type_FLOAT, const GLshort *buffer);
DOC(gluBuild3DMipmapsf, "gluBuild3DMipmapsf(target, components, format, pixels) -> None")


/*int gluBuild1DMipmapLevels(GLenum target, GLint components, GLint width, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *data); */
%{
PyObject* _gluBuild1DMipmapLevels(GLenum target, GLint components, GLint width, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;

	code = gluBuild1DMipmapLevels(target, components, width, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild1DMipmapLevels) PyObject* _gluBuild1DMipmapLevels(GLenum target, GLint components, GLint width, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer);
DOC(gluBuild1DMipmapLevels, "gluBuild1DMipmapLevels(target, components, width, format, type, level, base, max, data) -> None")

%{
PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint width, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;

	SetupPixelWrite(1);
	code = gluBuild1DMipmapLevels(target, components, width, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild1DMipmapLevelsb) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_BYTE, GLint level, GLint base, GLint max, const GLbyte *buffer);
DOC(gluBuild1DMipmapLevelsb, "gluBuild1DMipmapLevelsb(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelsub) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_BYTE, GLint level, GLint base, GLint max, const GLubyte *buffer);
DOC(gluBuild1DMipmapLevelsub, "gluBuild1DMipmapLevelsub(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelss) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_SHORT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild1DMipmapLevelss, "gluBuild1DMipmapLevelss(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelsus) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_SHORT, GLint level, GLint base, GLint max, const GLushort *buffer);
DOC(gluBuild1DMipmapLevelsus, "gluBuild1DMipmapLevelsus(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelsi) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_INT, GLint level, GLint base, GLint max, const GLint *buffer);
DOC(gluBuild1DMipmapLevelsi, "gluBuild1DMipmapLevelsi(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelsui) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_UNSIGNED_INT, GLint level, GLint base, GLint max, const GLuint *buffer);
DOC(gluBuild1DMipmapLevelsui, "gluBuild1DMipmapLevelsui(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild1DMipmapLevelsf) PyObject *__gluBuild1DMipmapLevels(GLenum target, GLint components, GLint d_5_0, GLenum format, GLenum type_FLOAT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild1DMipmapLevelsf, "gluBuild1DMipmapLevelsf(target, components, format, level, base, max, pixels) -> None")

/*int gluBuild2DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *data); */
%{
PyObject* _gluBuild2DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;
	
	code = gluBuild2DMipmapLevels(target, components, width, height, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild2DMipmapLevels) PyObject* _gluBuild2DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer);
DOC(gluBuild2DMipmapLevels, "gluBuild2DMipmapLevels(target, components, width, height, format, type, level, base, max, data) -> None")

%{
PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;

	SetupPixelWrite(2);
	code = gluBuild2DMipmapLevels(target, components, width, height, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild2DMipmapLevelsb) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_BYTE, GLint level, GLint base, GLint max, const GLbyte *buffer);
DOC(gluBuild2DMipmapLevelsb, "gluBuild2DMipmapLevelsb(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelsub) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_BYTE, GLint level, GLint base, GLint max, const GLubyte *buffer);
DOC(gluBuild2DMipmapLevelsub, "gluBuild2DMipmapLevelsub(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelss) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_SHORT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild2DMipmapLevelss, "gluBuild2DMipmapLevelss(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelsus) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_SHORT, GLint level, GLint base, GLint max, const GLushort *buffer);
DOC(gluBuild2DMipmapLevelsus, "gluBuild2DMipmapLevelsus(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelsi) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_INT, GLint level, GLint base, GLint max, const GLint *buffer);
DOC(gluBuild2DMipmapLevelsi, "gluBuild2DMipmapLevelsi(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelsui) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_INT, GLint level, GLint base, GLint max, const GLuint *buffer);
DOC(gluBuild2DMipmapLevelsui, "gluBuild2DMipmapLevelsui(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild2DMipmapLevelsf) PyObject *__gluBuild2DMipmapLevels(GLenum target, GLint components, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_FLOAT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild2DMipmapLevelsf, "gluBuild2DMipmapLevelsf(target, components, format, level, base, max, pixels) -> None")


/*int gluBuild3DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *data); */
%{
PyObject* _gluBuild3DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;
	
	code = gluBuild3DMipmapLevels(target, components, width, height, depth, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild3DMipmapLevels) PyObject* _gluBuild3DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer);
DOC(gluBuild3DMipmapLevels, "gluBuild3DMipmapLevels(target, components, width, height, depth, format, type, level, base, max, data) -> None")

%{
PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint width, GLint height, GLint depth, GLenum format, GLenum type, GLint level, GLint base, GLint max, const void *buffer)
{
	int code;

	SetupPixelWrite(2);
	code = gluBuild3DMipmapLevels(target, components, width, height, depth, format, type, level, base, max, buffer);
	
	if (code)
	{
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(gluBuild3DMipmapLevelsb) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_BYTE, GLint level, GLint base, GLint max, const GLbyte *buffer);
DOC(gluBuild3DMipmapLevelsb, "gluBuild3DMipmapLevelsb(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelsub) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_BYTE, GLint level, GLint base, GLint max, const GLubyte *buffer);
DOC(gluBuild3DMipmapLevelsub, "gluBuild3DMipmapLevelsub(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelss) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_SHORT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild3DMipmapLevelss, "gluBuild3DMipmapLevelss(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelsus) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_SHORT, GLint level, GLint base, GLint max, const GLushort *buffer);
DOC(gluBuild3DMipmapLevelsus, "gluBuild3DMipmapLevelsus(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelsi) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_INT, GLint level, GLint base, GLint max, const GLint *buffer);
DOC(gluBuild3DMipmapLevelsi, "gluBuild3DMipmapLevelsi(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelsui) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_UNSIGNED_INT, GLint level, GLint base, GLint max, const GLuint *buffer);
DOC(gluBuild3DMipmapLevelsui, "gluBuild3DMipmapLevelsui(target, components, format, level, base, max, pixels) -> None")

%name(gluBuild3DMipmapLevelsf) PyObject *__gluBuild3DMipmapLevels(GLenum target, GLint components, GLint d_9_2, GLint d_9_1, GLint d_9_0, GLenum format, GLenum type_FLOAT, GLint level, GLint base, GLint max, const GLshort *buffer);
DOC(gluBuild3DMipmapLevelsf, "gluBuild3DMipmapLevelsf(target, components, format, level, base, max, pixels) -> None")


#endif


%{
void CALLBACK throwGLUerror(GLenum code)
{
	PyErr_SetGLUerror(code);
}
%}


%{

typedef struct
{
	PyObject_HEAD
	GLUquadric *obj;
	PyObject *begin, *beginData, *edgeFlag, *edgeFlagData, *vertex, *vertexData;
	PyObject *end, *endData, *combine, *combineData;
} PyGLUquadric;


PyGLUquadric *currentQuadric = NULL;

static void PyGLUquadric_Del(PyObject *self)
{
	gluDeleteQuadric(((PyGLUquadric*)self)->obj);

    PyObject_Del(self);
}


PyTypeObject PyGLUquadric_Type =
{
    PyObject_HEAD_INIT(0)
    0,							/* ob_size */
    "GLUquadric",			/* tp_name */
    sizeof(PyGLUquadric),	/* tp_basicsize */
    0,							/* tp_itemsize */
    PyGLUquadric_Del,		/* tp_dealloc */
};

#define PYOBJ(x) ((x) ? (PyObject*)x : Py_None)


PyGLUquadric* _gluNewQuadric()
{
	PyGLUquadric *self = PyObject_NEW(PyGLUquadric, &PyGLUquadric_Type);
	
	if (!(self->obj = gluNewQuadric()))
	{
		PyErr_SetGLUerror(GLU_OUT_OF_MEMORY);
		return NULL;
	}
	
	gluQuadricCallback(self->obj, GLU_ERROR, throwGLUerror);

	return self;
}

PyObject* _gluQuadricCallback(PyGLUquadric* self, GLenum which, PyObject* pyfunc)
{
	PyErr_SetString(PyExc_Exception, "Can't set that callback.");
	return NULL;
}

%}


%typemap(python,in) PyGLUquadric*
{
	if ($input->ob_type != &PyGLUquadric_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUquadric object.");
		return NULL;
	}
	$1 = currentQuadric = (PyGLUquadric*)$input;
}

%typemap(python,freearg) PyGLUquadric*, GLUquadric*
{
	currentQuadric = NULL;
	if (PyErr_Occurred()) return NULL;
}

%typemap(python,out) PyGLUquadric*
{
	$result = (PyObject*)$1;
}

%typemap(python,in) GLUquadric*
{
	if ($input->ob_type != &PyGLUquadric_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUquadric object.");
		return NULL;
	}
	currentQuadric = (PyGLUquadric*)$input;
	$1 = currentQuadric->obj;
}

/*GLUquadric* gluNewQuadric (void); */
%name(gluNewQuadric) PyGLUquadric* _gluNewQuadric();
DOC(gluNewQuadric, "gluNewQuadric() -> GLUquadric")

%name(gluDeleteQuadric) void __ignoreDeletionCall(PyObject *quadObject);
DOC(gluDeleteQuadric, "gluDeleteQuadric(quadObject) -> (null function, use del nobj instead)")

void gluQuadricNormals(GLUquadric *quadObject, GLenum normals);
DOC(gluQuadricNormals, "gluQuadricNormals(quadObject, normals) -> None")

void gluQuadricTexture(GLUquadric *quadObject, GLboolean textureCoords);
DOC(gluQuadricTexture, "gluQuadricTexture(quadObject, textureCoords) -> None")

void gluQuadricOrientation(GLUquadric *quadObject, GLenum orientation);
DOC(gluQuadricOrientation, "gluQuadricOrientation(quadObject, orientation) -> None")

void gluQuadricDrawStyle(GLUquadric *quadObject, GLenum drawStyle);
DOC(gluQuadricDrawStyle, "gluQuadricDrawStyle(quadObject, drawStyle) -> None")

void gluCylinder(GLUquadric *qobj, GLdouble baseRadius, GLdouble topRadius, GLdouble height, GLint slices, GLint stacks);
DOC(gluCylinder, "gluCylinder(qobj, baseRadius, topRadius, height, slices, stacks) -> None")

void gluDisk(GLUquadric *qobj, GLdouble innerRadius, GLdouble outerRadius, GLint slices, GLint loops);
DOC(gluDisk, "gluDisk(qobj, innerRadius, outerRadius, slices, loops) -> None")

void gluPartialDisk(GLUquadric *qobj, GLdouble innerRadius, GLdouble outerRadius, GLint slices, GLint loops, GLdouble startAngle, GLdouble sweepAngle);
DOC(gluPartialDisk, "gluPartialDisk(qobj, innerRadius, outerRadius, slices, loops, startAngle, sweepAngle) -> None")

void gluSphere(GLUquadric *qobj, GLdouble radius, GLint slices, GLint stacks);
DOC(gluSphere, "gluSphere(qobj, radius, slices, stacks) -> None")

/*void gluQuadricCallback(GLUquadric *qobj, GLenum which, void (CALLBACK* pyfunc)()); */
%name(gluQuadricCallback) PyObject* _gluQuadricCallback(PyGLUquadric* self, GLenum which, PyObject* pyfunc);
DOC(gluQuadricCallback, "gluQuadricCallback(qobj, which, func)")

%{

#ifndef GLU_VERSION_1_2
#define GLU_TESS_BEGIN 100100
#define GLU_TESS_VERTEX 100101
#define GLU_TESS_END 100102
#define GLU_TESS_ERROR 100103
#define GLU_TESS_EDGE_FLAG 100104
#define GLU_TESS_COMBINE 100105
#define GLU_TESS_BEGIN_DATA 100106
#define GLU_TESS_VERTEX_DATA 100107
#define GLU_TESS_END_DATA 100108
#define GLU_TESS_ERROR_DATA 100109
#define GLU_TESS_EDGE_FLAG_DATA 100110
#define GLU_TESS_COMBINE_DATA 100111
#endif

typedef struct
{
	PyObject_HEAD
	GLUtesselator *obj;
	PyObject *lockedObjects;
	PyObject *callbacks;
	PyObject *currentData;
} PyGLUtesselator;


static void PyGLUtesselator_Del(PyObject *self)
{
	gluDeleteTess(((PyGLUtesselator*)self)->obj);

	Py_DECREF(((PyGLUtesselator*)self)->lockedObjects);
	Py_DECREF(((PyGLUtesselator*)self)->callbacks);
	if (((PyGLUtesselator*)self)->currentData) {
		Py_DECREF(((PyGLUtesselator*)self)->currentData);
	}

    PyObject_Del(self);
}


PyTypeObject PyGLUtesselator_Type =
{
    PyObject_HEAD_INIT(0)
    0,							/* ob_size */
    "GLUtesselator",			/* tp_name */
    sizeof(PyGLUtesselator),	/* tp_basicsize */
    0,							/* tp_itemsize */
    PyGLUtesselator_Del,		/* tp_dealloc */
};

#define PYOBJ(x) ((x) ? (PyObject*)x : Py_None)

PyObject *GetTessCallback( void * currentTessellator, char *name)
{
	if (currentTessellator) {
		PyGLUtesselator * tess = (PyGLUtesselator *) ((PyObject *) currentTessellator);
		{

			PyObject *this_callback = PyDict_GetItemString(tess->callbacks, name);
			if (this_callback != Py_None) return this_callback;
		}
	}
	return NULL;
}
PyObject *GetTessData( void * currentTessellator)
{
	if (currentTessellator) {
		PyGLUtesselator * tess = (PyGLUtesselator *) ((PyObject *) currentTessellator);
		return tess->currentData;
	}
	return NULL;
}

void _PyPrint_ToStderr( char * message ) {
	/* message must be a null-terminated C-style string */
	PyObject * sysModule;
	PyObject * sysModuleStdErr;
	PyObject * result;
	sysModule = NULL;
	sysModuleStdErr = NULL;
	sysModule = PyImport_ImportModule( "sys" );
	if (sysModule) {
		sysModuleStdErr = PyObject_GetAttrString( sysModule, "stderr" );
		if (sysModuleStdErr) {
			result = PyObject_CallMethod( sysModuleStdErr, "write", "s", message );
		}
	}
	Py_XDECREF(sysModule);
	Py_XDECREF(sysModuleStdErr);
	Py_XDECREF(result);
}

void CALLBACK PyGLUtesselator_begin(GLenum type, void *polygon_data)
{
	/* callback when Python code has only specified begin */
	PyObject *this_callback = GetTessCallback( polygon_data, "begin");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "l", (long)type);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation begin callback\n" );
		}
	}
}

void CALLBACK PyGLUtesselator_beginData(GLenum type, void *polygon_data)
{
	/* callback when Python code has only specified begindata */
	PyObject *this_callback = GetTessCallback( polygon_data, "beginData");
	if (this_callback)
	{
		PyObject * data = GetTessData( polygon_data );
		PyObject *result = PyObject_CallFunction(this_callback, "lO", (long)type, data);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation begin data callback\n" );
		}
	}
}

void CALLBACK PyGLUtesselator_edgeFlag(GLboolean flag, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "edgeFlag");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "l", (long)flag);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation edge flag callback\n" );
		}
	}
}
void CALLBACK PyGLUtesselator_edgeFlagData(GLboolean flag, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "edgeFlagData");
	if (this_callback)
	{
		PyObject * data = GetTessData( polygon_data );
		PyObject *result = PyObject_CallFunction(this_callback, "lO", (long)flag, data);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation edge flag data callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_vertex(void *vertex_data, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "vertex");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(O)", PYOBJ(vertex_data));
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr("Exception during GLU Tessellation vertex callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_vertexData(void *vertex_data, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "vertexData");
	if (this_callback)
	{
		PyObject * data = GetTessData( polygon_data );
		PyObject *result = PyObject_CallFunction(this_callback, "OO", PYOBJ(vertex_data), data);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation vertex data callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_end(void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "end");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, NULL);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation end callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_endData(void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "endData");
	if (this_callback)
	{
		PyObject * data = GetTessData( polygon_data );
		PyObject *result = PyObject_CallFunction(this_callback, "(O)", data);
		Py_XDECREF(result);
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation end data callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_combine(GLdouble coords[3], void *vertex_data[4], GLfloat weight[4], void **outData, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "combine");
	if (this_callback)
	{
		PyObject *result = NULL;
		result = PyObject_CallFunction(this_callback,
		            	"(ddd)(OOOO)(ffff)",
		                                         coords[0], coords[1], coords[2],
		                                         PYOBJ(vertex_data[0]), PYOBJ(vertex_data[1]), PYOBJ(vertex_data[2]), PYOBJ(vertex_data[3]),
		                                         weight[0], weight[1], weight[2], weight[3]);

		if (result)
		{
			PyList_Append(
				((PyGLUtesselator *) ((PyObject *) polygon_data))->lockedObjects,
				result
			);
			*outData = (void*)result;
			Py_DECREF(result);
		}
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation combine callback\n" );
		}
	}
}


void CALLBACK PyGLUtesselator_combineData(GLdouble coords[3], void *vertex_data[4], GLfloat weight[4], void **outData, void *polygon_data)
{
	PyObject *this_callback = GetTessCallback( polygon_data, "combineData");
	if (this_callback)
	{
		PyObject * data = GetTessData( polygon_data );
		PyObject *result = PyObject_CallFunction(this_callback,
		            	"(ddd)(OOOO)(ffff)O",
		                                         coords[0], coords[1], coords[2],
		                                         PYOBJ(vertex_data[0]), PYOBJ(vertex_data[1]), PYOBJ(vertex_data[2]), PYOBJ(vertex_data[3]),
		                                         weight[0], weight[1], weight[2], weight[3],
		                                         data);
		if (result)
		{
			PyList_Append(
				((PyGLUtesselator *) ((PyObject *) polygon_data))->lockedObjects,
				result
			);
			*outData = (void*)result;
			Py_DECREF(result);
		}
		if (PyErr_Occurred()){
			PyErr_Print();
			_PyPrint_ToStderr( "Exception during GLU Tessellation combine data callback\n" );
		}
	}
}


void CALLBACK tess_throwGLUerror(GLenum code, void *polygon_data)
{
	PyErr_SetObject(GLUerror, Py_BuildValue("isO", code, gluErrorString(code), PYOBJ(polygon_data)));
}


PyGLUtesselator* _gluNewTess()
{
	PyGLUtesselator *self = PyObject_NEW(PyGLUtesselator, &PyGLUtesselator_Type);
	
	if (!(self->obj = gluNewTess()))
	{
		PyErr_SetGLUerror(GLU_OUT_OF_MEMORY);
		return NULL;
	}
	
	gluTessCallback(self->obj, GLU_TESS_ERROR_DATA, tess_throwGLUerror);

	self->lockedObjects = PyList_New(0);
	self->callbacks = PyDict_New();
	self->currentData = Py_None;
	Py_INCREF( self->currentData );

	return self;
}

#define SET_TESS_CALLBACK(NAME,TYPE)\
PyDict_SetItemString(self->callbacks, #NAME, pyfunc);\
gluTessCallback(self->obj, TYPE, (pyfunc == Py_None) ? NULL : (callback)PyGLUtesselator_##NAME);

PyObject* _gluTessCallback(PyGLUtesselator* self, GLenum which, PyObject* pyfunc)
{
	switch (which)
	{
	case GLU_TESS_BEGIN:
		SET_TESS_CALLBACK(begin,GLU_TESS_BEGIN_DATA)
		break;
	case GLU_TESS_BEGIN_DATA:
		SET_TESS_CALLBACK(beginData,GLU_TESS_BEGIN_DATA)
		break;
	case GLU_TESS_EDGE_FLAG:
		SET_TESS_CALLBACK(edgeFlag,GLU_TESS_EDGE_FLAG_DATA)
		break;
	case GLU_TESS_EDGE_FLAG_DATA:
		SET_TESS_CALLBACK(edgeFlagData,GLU_TESS_EDGE_FLAG_DATA)
		break;
	case GLU_TESS_VERTEX:
		SET_TESS_CALLBACK(vertex,GLU_TESS_VERTEX_DATA)
		break;
	case GLU_TESS_VERTEX_DATA:
		SET_TESS_CALLBACK(vertexData,GLU_TESS_VERTEX_DATA)
		break;
	case GLU_TESS_END:
		SET_TESS_CALLBACK(end,GLU_TESS_END_DATA)
		break;
	case GLU_TESS_END_DATA:
		SET_TESS_CALLBACK(endData,GLU_TESS_END_DATA)
		break;
	case GLU_TESS_COMBINE:
		SET_TESS_CALLBACK(combine,GLU_TESS_COMBINE_DATA)
		break;
	case GLU_TESS_COMBINE_DATA:
		SET_TESS_CALLBACK(combineData,GLU_TESS_COMBINE_DATA)
		break;
	case GLU_TESS_ERROR:
	case GLU_TESS_ERROR_DATA:
		PyErr_SetString(PyExc_Exception, "Can't set that callback.");
		return NULL;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown callback code.");
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}

%}


%typemap(python,in) PyGLUtesselator*
{
	if ($input->ob_type != &PyGLUtesselator_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUtesselator object.");
		return NULL;
	}
	$1 = (PyGLUtesselator*)$input;
}

%typemap(python,freearg) PyGLUtesselator*, GLUtesselator*
{
	/*currentTesselator = NULL;*/
	if (PyErr_Occurred()) return NULL;
}

%typemap(python,out) PyGLUtesselator*
{
	$result = (PyObject*)$1;
}

%typemap(python,in) GLUtesselator*
{
	if ($input->ob_type != &PyGLUtesselator_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUtesselator object.");
		return NULL;
	}
	/*currentTesselator = (PyGLUtesselator*)$input;*/
	$1 = ((PyGLUtesselator*)$input)->obj;
}


/*GLUtesselator* gluNewTess(); */
%name(gluNewTess) PyGLUtesselator* _gluNewTess();
DOC(gluNewTess, "gluNewTess() -> GLUtesselator")

/*void gluDeleteTess(GLUtesselator *tess); */
%name(gluDeleteTess) void __ignoreDeletionCall(PyObject *tess);
DOC(gluDeleteTess, "gluDeleteTess(tess) -> (null function, use del tess instead)")

#if API_VERSION >= 258
%{
void _gluTessBeginPolygon(PyGLUtesselator *self, PyObject *polygon_data)
{
	PyList_Append(self->lockedObjects, polygon_data);
	if (self->currentData) {
		Py_DECREF( self->currentData);
	}
	self->currentData = polygon_data;
	Py_INCREF( polygon_data );
	gluTessBeginPolygon(self->obj, (void*)self);
}
%}

%name(gluTessBeginPolygon) void _gluTessBeginPolygon(PyGLUtesselator *self, PyObject *polygon_data);
DOC(gluTessBeginPolygon, "gluTessBeginPolygon(tess, polygon_data) -> None")
#endif

void gluBeginPolygon(GLUtesselator *tess);
DOC(gluBeginPolygon, "gluBeginPolygon(tess) -> None")

#if API_VERSION >= 258
void gluTessBeginContour(GLUtesselator *tess);
DOC(gluTessBeginContour, "gluTessBeginContour(tess) -> None")
#endif

%{
void _gluTessVertex(PyGLUtesselator *self, const GLdouble *coords, PyObject *data)
{
	PyList_Append(self->lockedObjects, data);
	gluTessVertex(self->obj, (GLdouble*)coords, (void*)data);
}
%}

%name(gluTessVertex) void _gluTessVertex(PyGLUtesselator *tess, const GLdouble *coords, PyObject *data);
DOC(gluTessVertex, "gluTessVertex(tess, coords, data) -> None")

/* Backwards compatibility for old tesselator */

#if API_VERSION >= 258
void gluTessEndContour(GLUtesselator *tess);
DOC(gluTessEndContour, "gluTessEndContour(tess) -> None")
#endif

void gluNextContour(GLUtesselator *tess, GLenum type);
DOC(gluNextContour, "gluNextContour(tess, type) -> None")

#if API_VERSION >= 258
%{
void _gluTessEndPolygon(PyGLUtesselator *self)
{
	gluTessEndPolygon(self->obj);
	PySequence_DelSlice(self->lockedObjects, 0, -1);
}
%}

%name(gluTessEndPolygon) void _gluTessEndPolygon(PyGLUtesselator *self);
DOC(gluTessEndPolygon, "gluTessEndPolygon(tess) -> None")
#endif

void gluEndPolygon(GLUtesselator *tess);
DOC(gluEndPolygon, "gluEndPolygon(tess) -> None")

#if API_VERSION >= 258
void gluTessProperty(GLUtesselator *tess, GLenum which, GLdouble value);
DOC(gluTessProperty, "gluTessProperty(tess, which, value) -> None")
#endif

#if API_VERSION >= 258 
void gluTessNormal(GLUtesselator *tess, GLdouble x, GLdouble y, GLdouble z);
DOC(gluTessNormal, "gluTessNormal(tess, x, y, z) -> None")
#endif

/*void gluTessCallback(GLUtesselator *tess, GLenum which, void (CALLBACK *pyfunc)()); */
%name(gluTessCallback) PyObject* _gluTessCallback(PyGLUtesselator* self, GLenum which, PyObject* pyfunc);
DOC(gluTessCallback, "gluTessCallback(tess, which, pyfunc) -> None\n\
\n\
The error callbacks GLU_TESS_ERROR and GLU_TESS_ERROR_BEGIN cannot be set by\n\
gluTessCallback, instead an exception is thrown when an error occurs with the\n\
exception value set to a tuple (errno, polygon_data)")

#if API_VERSION >= 258
void gluGetTessProperty(GLUtesselator *tess, GLenum which, GLdouble value[1]);
DOC(gluGetTessProperty, "gluGetTessProperty(tess, which) -> value")
#endif 

%{

#ifndef GLU_VERSION_1_3
#define GLU_NURBS_MODE             100160

#define GLU_NURBS_TESSELLATOR      100161
#define GLU_NURBS_RENDERER         100162

#define GLU_NURBS_BEGIN	               100164
#define GLU_NURBS_VERTEX                   100165
#define GLU_NURBS_NORMAL                   100166
#define GLU_NURBS_COLOR                    100167
#define GLU_NURBS_TEXTURE_COORD            100168
#define GLU_NURBS_END                      100169

#define GLU_NURBS_BEGIN_DATA	       100170
#define GLU_NURBS_VERTEX_DATA              100171
#define GLU_NURBS_NORMAL_DATA              100172
#define GLU_NURBS_COLOR_DATA               100173
#define GLU_NURBS_TEXTURE_COORD_DATA       100174
#define GLU_NURBS_END_DATA                 100175
#endif

typedef struct
{
	PyObject_HEAD
	GLUnurbs *obj;
	PyObject *data;
	PyObject *callbacks;
} PyGLUnurbs;


PyGLUnurbs *currentNurbs = NULL;

static void PyGLUnurbs_Del(PyObject *self)
{
	gluDeleteNurbsRenderer(((PyGLUnurbs*)self)->obj);

	Py_DECREF(((PyGLUnurbs*)self)->data);
	Py_DECREF(((PyGLUtesselator*)self)->callbacks);

    PyObject_Del(self);
}


PyTypeObject PyGLUnurbs_Type =
{
    PyObject_HEAD_INIT(0)
    0,							/* ob_size */
    "GLUnurbs",			/* tp_name */
    sizeof(PyGLUnurbs),	/* tp_basicsize */
    0,							/* tp_itemsize */
    PyGLUnurbs_Del,		/* tp_dealloc */
};

#define PYOBJ(x) ((x) ? (PyObject*)x : Py_None)

PyObject *GetNurbsCallback(char *name)
{
	if (currentNurbs)
	{
		PyObject *this_callback = PyDict_GetItemString(currentNurbs->callbacks, name);
		if (this_callback != Py_None) return this_callback;
	}
	return NULL;
}

PyGLUnurbs* _gluNewNurbsRenderer()
{
	PyGLUnurbs *self = PyObject_NEW(PyGLUnurbs, &PyGLUnurbs_Type);
	
	if (!(self->obj = gluNewNurbsRenderer()))
	{
		PyErr_SetGLUerror(GLU_OUT_OF_MEMORY);
		return NULL;
	}
	
	gluNurbsCallback(self->obj, GLU_ERROR, throwGLUerror);
	Py_INCREF(self->data = Py_None);
	self->callbacks = PyDict_New();

	return self;
}

void CALLBACK PyGLUnurbs_begin(GLenum type)
{
	PyObject *this_callback = GetNurbsCallback("begin");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "l", (long)type);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_beginData(GLenum type, void *userData)
{
	PyObject *this_callback = GetNurbsCallback("beginData");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "lO", (long)type, PYOBJ(userData));
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_vertex(GLfloat *vertex)
{
	PyObject *this_callback = GetNurbsCallback("vertex");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(fff)", vertex[0], vertex[1], vertex[2]);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_vertexData(GLfloat *vertex, void *userData)
{
	PyObject *this_callback = GetNurbsCallback("vertexData");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(fff)O", vertex[0], vertex[1], vertex[2], PYOBJ(userData));
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_normal(GLfloat *normal)
{
	PyObject *this_callback = GetNurbsCallback("normal");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(fff)", normal[0], normal[1], normal[2]);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_normalData(GLfloat *normal, void *userData)
{
	PyObject *this_callback = GetNurbsCallback("normalData");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(fff)O", normal[0], normal[1], normal[2], PYOBJ(userData));
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_color(GLfloat *color)
{
	PyObject *this_callback = GetNurbsCallback("color");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(ffff)", color[0], color[1], color[2], color[3]);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_colorData(GLfloat *color, void *userData)
{
	PyObject *this_callback = GetNurbsCallback("colorData");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "(ffff)O", color[0], color[1], color[2], color[3], PYOBJ(userData));
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_texCoord(GLfloat *texCoord)
{
	PyObject *this_callback = GetNurbsCallback("texCoord");
	if (this_callback)
	{
		PyObject *result = NULL;
		
		if (glIsEnabled(GL_MAP1_TEXTURE_COORD_1) || glIsEnabled(GL_MAP2_TEXTURE_COORD_1))
		{
			result = PyObject_CallFunction(this_callback, "((f))", texCoord[0]);
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_2) || glIsEnabled(GL_MAP2_TEXTURE_COORD_2))
		{
			result = PyObject_CallFunction(this_callback, "(ff)", texCoord[0], texCoord[1]);
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_3) || glIsEnabled(GL_MAP2_TEXTURE_COORD_3))
		{
			result = PyObject_CallFunction(this_callback, "(fff)", texCoord[0], texCoord[1], texCoord[2]);
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_4) || glIsEnabled(GL_MAP2_TEXTURE_COORD_4))
		{
			result = PyObject_CallFunction(this_callback, "(ffff)", texCoord[0], texCoord[1], texCoord[2], texCoord[3]);
		}
		
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_texCoordData(GLfloat *texCoord, void *userData)
{
	PyObject *this_callback = GetNurbsCallback("texCoordData");
	if (this_callback)
	{
		PyObject *result = NULL;
		
		if (glIsEnabled(GL_MAP1_TEXTURE_COORD_1) || glIsEnabled(GL_MAP2_TEXTURE_COORD_1))
		{
			result = PyObject_CallFunction(this_callback, "(f)O", texCoord[0], PYOBJ(userData));
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_2) || glIsEnabled(GL_MAP2_TEXTURE_COORD_2))
		{
			result = PyObject_CallFunction(this_callback, "(ff)O", texCoord[0], texCoord[1], PYOBJ(userData));
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_3) || glIsEnabled(GL_MAP2_TEXTURE_COORD_3))
		{
			result = PyObject_CallFunction(this_callback, "(fff)O", texCoord[0], texCoord[1], texCoord[2], PYOBJ(userData));
		}
		else if (glIsEnabled(GL_MAP1_TEXTURE_COORD_4) || glIsEnabled(GL_MAP2_TEXTURE_COORD_4))
		{
			result = PyObject_CallFunction(this_callback, "(ffff)O", texCoord[0], texCoord[1], texCoord[2], texCoord[3], PYOBJ(userData));
		}
		
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_end()
{
	PyObject *this_callback = GetNurbsCallback("end");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, NULL);
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


void CALLBACK PyGLUnurbs_endData(void *userData)
{
	PyObject *this_callback = GetNurbsCallback("endData");
	if (this_callback)
	{
		PyObject *result = PyObject_CallFunction(this_callback, "O", PYOBJ(userData));
		Py_XDECREF(result);
		PyErr_XPrint();
	}
}


#define SET_NURBS_CALLBACK(NAME)\
PyDict_SetItemString(self->callbacks, #NAME, pyfunc);\
gluNurbsCallback(self->obj, which, (pyfunc == Py_None) ? NULL : (callback)PyGLUnurbs_##NAME);

PyObject* _gluNurbsCallback(PyGLUnurbs* self, GLenum which, PyObject* pyfunc)
{
	switch (which)
	{
	case GLU_NURBS_BEGIN:
		SET_NURBS_CALLBACK(begin)
		break;
	case GLU_NURBS_BEGIN_DATA:
		SET_NURBS_CALLBACK(beginData)
		break;
	case GLU_NURBS_VERTEX:
		SET_NURBS_CALLBACK(vertex)
		break;
	case GLU_NURBS_VERTEX_DATA:
		SET_NURBS_CALLBACK(vertexData)
		break;
	case GLU_NURBS_NORMAL:
		SET_NURBS_CALLBACK(normal)
		break;
	case GLU_NURBS_NORMAL_DATA:
		SET_NURBS_CALLBACK(normalData)
		break;
	case GLU_NURBS_COLOR:
		SET_NURBS_CALLBACK(color)
		break;
	case GLU_NURBS_COLOR_DATA:
		SET_NURBS_CALLBACK(colorData)
		break;
	case GLU_NURBS_TEXTURE_COORD:
		SET_NURBS_CALLBACK(texCoord)
		break;
	case GLU_NURBS_TEXTURE_COORD_DATA:
		SET_NURBS_CALLBACK(texCoordData)
		break;
	case GLU_NURBS_END:
		SET_NURBS_CALLBACK(end)
		break;
	case GLU_NURBS_END_DATA:
		SET_NURBS_CALLBACK(endData)
		break;
	case GLU_ERROR:
		PyErr_SetString(PyExc_Exception, "Can't set that callback.");
		return NULL;
	default:
		PyErr_SetString(PyExc_Exception, "Unknown callback code.");
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}

%}

%typemap(python,in) PyGLUnurbs*
{
	if ($input->ob_type != &PyGLUnurbs_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUnurbs object.");
		return NULL;
	}
	$1 = currentNurbs = (PyGLUnurbs*)$input;
}

%typemap(python,freearg) PyGLUnurbs*, GLUnurbs*
{
	currentNurbs = NULL;
	if (PyErr_Occurred()) return NULL;
}

%typemap(python,out) PyGLUnurbs*
{
	$result = (PyObject*)$1;
}

%typemap(python,in) GLUnurbs*
{
	if ($input->ob_type != &PyGLUnurbs_Type)
	{
		PyErr_SetString(PyExc_Exception, "Not a GLUnurbs object.");
		return NULL;
	}
	currentNurbs = (PyGLUnurbs*)$input;
	$1 = currentNurbs->obj;
}

/*GLUnurbs* gluNewNurbsRenderer(); */
%name(gluNewNurbsRenderer) PyGLUnurbs* _gluNewNurbsRenderer();
DOC(gluNewNurbsRenderer, "gluNewNurbsRenderer() -> GLUnurbs")

%name(gluDeleteNurbsRenderer) void __ignoreDeletionCall(PyObject *tess);
DOC(gluDeleteNurbsRenderer, "gluDeleteNurbsRenderer(nobj) -> None (null function, use del nobj instead)")

void gluBeginSurface(GLUnurbs *nobj);
DOC(gluBeginSurface, "gluBeginSurface(nobj) -> None")

void gluBeginCurve(GLUnurbs *nobj);
DOC(gluBeginCurve, "gluBeginCurve(nobj) -> None")

void gluEndCurve(GLUnurbs *nobj);
DOC(gluEndCurve, "gluEndCurve(nobj) -> None")

void gluEndSurface(GLUnurbs *nobj);
DOC(gluEndSurface, "gluEndSurface(nobj) -> None")

void gluBeginTrim(GLUnurbs *nobj);
DOC(gluBeginTrim, "gluBeginTrim(nobj) -> None")

void gluEndTrim(GLUnurbs *nobj);
DOC(gluEndTrim, "gluEndTrim(nobj) -> None")

%{
#define _gluPwlCurve(nobj, count, array, stride, type) \
gluPwlCurve(nobj, count, (GLfloat*)array, stride, type)
%}

%name(gluPwlCurve) void _gluPwlCurve(
	GLUnurbs *nobj, GLint d_1_0, 
	const GLfloat *array, 
	GLint d_1_1, GLenum type
);
DOC(gluPwlCurve, "gluPwlCurve(nobj, array, type) -> None")

%{
#define _gluNurbsCurve(nobj, n_2, knot, d_5_0, d_5_1, ctlarray, type) \
gluNurbsCurve(nobj, n_2, (GLfloat*)knot, d_5_1, (GLfloat*)ctlarray, n_2 - d_5_0, type)
%}

%name(gluNurbsCurve) void _gluNurbsCurve(GLUnurbs *nobj, GLint n_2, const GLfloat *knot, GLint d_5_0, GLint d_5_1, const GLfloat *ctlarray, GLenum type);
DOC(gluNurbsCurve, "gluNurbsCurve(nobj, knot, ctlarray, type) -> None")

%{
#define _gluNurbsSurface(nobj, sknot_len, sknot, tknot_len, tknot, d_0, d_1, d_2, ctlarray, type)\
gluNurbsSurface(\
	nobj, sknot_len, (GLfloat*)sknot, tknot_len, (GLfloat*)tknot, \
	d_1*d_2, d_2, (GLfloat*)ctlarray, sknot_len-d_0, tknot_len-d_1, type \
)
%}

/* I (Mike) have _no_ idea why this requires d_6_* instead of d_4_* :( */
%name(gluNurbsSurface) void _gluNurbsSurface(GLUnurbs *nobj, GLint n_2, const GLfloat *sknot, GLint n_3, const GLfloat *tknot, GLint d_6_0, GLint d_6_1, GLint d_6_2,
                     const GLfloat *ctlarray, GLenum type);
DOC(gluNurbsSurface, "gluNurbsSurface(nobj, sknot, tknot, ctlarray, type) -> None")

void gluLoadSamplingMatrices(GLUnurbs *nobj, const GLfloat *modelMatrix, const GLfloat *projMatrix, const GLint *viewport);
DOC(gluLoadSamplingMatrices, "gluLoadSamplingMatrices(nobj, modelMatrix, projMatrix, viewport) -> None")

void gluNurbsProperty(GLUnurbs *nobj, GLenum property, GLfloat value);
DOC(gluNurbsProperty, "gluNurbsProperty(nobj, property, value) -> None")

void gluGetNurbsProperty(GLUnurbs *nobj, GLenum property, GLfloat value[1]);
DOC(gluGetNurbsProperty, "gluGetNurbsProperty(nobj, property) -> value")

/*void gluNurbsCallback(GLUnurbs *nobj, GLenum which, void (CALLBACK* pyfunc)() ); */
%name(gluNurbsCallback) PyObject* _gluNurbsCallback(PyGLUnurbs* self, GLenum which, PyObject* pyfunc);
DOC(gluNurbsCallback, "gluNurbsCallback(qobj, which, func)")

#if API_VERSION >= 259 /* GLU 1.3 */
%{
void _gluNurbsCallbackData(PyGLUnurbs *self, PyObject *data)
{
	Py_DECREF(self->data);
	Py_INCREF(self->data = data);
	gluNurbsCallbackData(self->obj, (void*)data);
}
%}

%name(gluNurbsCallbackData) void _gluNurbsCallbackData(PyGLUnurbs *nobj, PyObject *data);
DOC(gluNurbsCallbackData, "gluNurbsCallbackData(nobj, data) -> None")
#endif

/* turn the exception handler on for GLU_EXT_nurbs_tessellator */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GLU_EXT_nurbs_tessellator)
DECLARE_VOID_EXT(gluNurbsCallbackDataEXT, \
	(GLUnurbs* theNurb, void* userData),\
	(theNurb, userData))
#endif

#define __gluNurbsCallbackDataEXT(nobj, data) gluNurbsCallbackDataEXT(nobj, (void*)data)
%}

void __gluNurbsCallbackDataEXT(GLUnurbs *nobj, PyObject *data);
DOC(__gluNurbsCallbackDataEXT, "gluNurbsCallbackDataEXT(nobj, data) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GLU_EXT_nurbs_tessellator)
	"gluNurbsCallbackDataEXT",
#endif
	NULL
};

#define __gluInitNurbsTessellatorEXT() InitExtension("GLU_EXT_nurbs_tessellator", proc_names)
%}

int __gluInitNurbsTessellatorEXT();
DOC(__gluInitNurbsTessellatorEXT, "gluInitNurbsTessellatorEXT() -> bool")

/* revert to the normal exception handler */
%include gl_exception_handler.inc

/* Generic constants */

/* Version */
#if API_VERSION >= 257
#define GLU_VERSION_1_1 1
#endif

#if API_VERSION >= 258
#define GLU_VERSION_1_2 1
#endif

#if API_VERSION >= 259
#define GLU_VERSION_1_3 1
#endif

/* Errors: (return value 0 = no error) */
#define GLU_INVALID_ENUM 100900
#define GLU_INVALID_VALUE 100901
#define GLU_OUT_OF_MEMORY 100902
#define GLU_INCOMPATIBLE_GL_VERSION 100903

#if API_VERSION >= 257
/* StringName */
#define GLU_VERSION 100800
#define GLU_EXTENSIONS 100801
#endif

/* Boolean */
#define GLU_TRUE GL_TRUE
#define GLU_FALSE GL_FALSE


/* Quadric constants */

/* QuadricNormal */
#define GLU_SMOOTH 100000
#define GLU_FLAT 100001
#define GLU_NONE 100002

/* QuadricDrawStyle  */
#define GLU_POINT 100010
#define GLU_LINE 100011
#define GLU_FILL 100012
#define GLU_SILHOUETTE 100013

/* QuadricOrientation */
#define GLU_OUTSIDE 100020
#define GLU_INSIDE 100021

/* Callback types:  */
/* GLU_ERROR 100103  */


/* Tesselation constants */

#define GLU_TESS_MAX_COORD 1.0e150

/* TessProperty  */
#define GLU_TESS_WINDING_RULE 100140
#define GLU_TESS_BOUNDARY_ONLY 100141
#define GLU_TESS_TOLERANCE 100142

/* TessWinding */
#define GLU_TESS_WINDING_ODD 100130
#define GLU_TESS_WINDING_NONZERO 100131
#define GLU_TESS_WINDING_POSITIVE 100132
#define GLU_TESS_WINDING_NEGATIVE 100133
#define GLU_TESS_WINDING_ABS_GEQ_TWO 100134

/* TessCallback  */
#define GLU_TESS_BEGIN 100100
#define GLU_TESS_VERTEX 100101
#define GLU_TESS_END 100102
#define GLU_TESS_ERROR 100103
#define GLU_TESS_EDGE_FLAG 100104
#define GLU_TESS_COMBINE 100105
#define GLU_TESS_BEGIN_DATA 100106
#define GLU_TESS_VERTEX_DATA 100107
#define GLU_TESS_END_DATA 100108
#define GLU_TESS_ERROR_DATA 100109
#define GLU_TESS_EDGE_FLAG_DATA 100110
#define GLU_TESS_COMBINE_DATA 100111

/* TessError  */
#define GLU_TESS_ERROR1 100151
#define GLU_TESS_ERROR2 100152
#define GLU_TESS_ERROR3 100153
#define GLU_TESS_ERROR4 100154
#define GLU_TESS_ERROR5 100155
#define GLU_TESS_ERROR6 100156
#define GLU_TESS_ERROR7 100157
#define GLU_TESS_ERROR8 100158

#define GLU_TESS_MISSING_BEGIN_POLYGON GLU_TESS_ERROR1
#define GLU_TESS_MISSING_BEGIN_CONTOUR GLU_TESS_ERROR2
#define GLU_TESS_MISSING_END_POLYGON GLU_TESS_ERROR3
#define GLU_TESS_MISSING_END_CONTOUR GLU_TESS_ERROR4
#define GLU_TESS_COORD_TOO_LARGE GLU_TESS_ERROR5
#define GLU_TESS_NEED_COMBINE_CALLBACK GLU_TESS_ERROR6

/* NURBS constants */

/* NurbsProperty */
#define GLU_AUTO_LOAD_MATRIX 100200
#define GLU_CULLING 100201
#define GLU_SAMPLING_TOLERANCE 100203
#define GLU_DISPLAY_MODE 100204
#if API_VERSION > 257
#define GLU_PARAMETRIC_TOLERANCE 100202
#define GLU_SAMPLING_METHOD 100205
#define GLU_U_STEP 100206
#define GLU_V_STEP 100207
#endif

/* NurbsSampling */
#define GLU_PATH_LENGTH 100215
#define GLU_PARAMETRIC_ERROR 100216
#define GLU_DOMAIN_DISTANCE 100217


/* NurbsTrim */
#define GLU_MAP1_TRIM_2 100210
#define GLU_MAP1_TRIM_3 100211

/* NurbsDisplay */
#define GLU_OUTLINE_POLYGON 100240
#define GLU_OUTLINE_PATCH 100241

/* NurbsErrors */
#define GLU_NURBS_ERROR1 100251
#define GLU_NURBS_ERROR2 100252
#define GLU_NURBS_ERROR3 100253
#define GLU_NURBS_ERROR4 100254
#define GLU_NURBS_ERROR5 100255
#define GLU_NURBS_ERROR6 100256
#define GLU_NURBS_ERROR7 100257
#define GLU_NURBS_ERROR8 100258
#define GLU_NURBS_ERROR9 100259
#define GLU_NURBS_ERROR10 100260
#define GLU_NURBS_ERROR11 100261
#define GLU_NURBS_ERROR12 100262
#define GLU_NURBS_ERROR13 100263
#define GLU_NURBS_ERROR14 100264
#define GLU_NURBS_ERROR15 100265
#define GLU_NURBS_ERROR16 100266
#define GLU_NURBS_ERROR17 100267
#define GLU_NURBS_ERROR18 100268
#define GLU_NURBS_ERROR19 100269
#define GLU_NURBS_ERROR20 100270
#define GLU_NURBS_ERROR21 100271
#define GLU_NURBS_ERROR22 100272
#define GLU_NURBS_ERROR23 100273
#define GLU_NURBS_ERROR24 100274
#define GLU_NURBS_ERROR25 100275
#define GLU_NURBS_ERROR26 100276
#define GLU_NURBS_ERROR27 100277
#define GLU_NURBS_ERROR28 100278
#define GLU_NURBS_ERROR29 100279
#define GLU_NURBS_ERROR30 100280
#define GLU_NURBS_ERROR31 100281
#define GLU_NURBS_ERROR32 100282
#define GLU_NURBS_ERROR33 100283
#define GLU_NURBS_ERROR34 100284
#define GLU_NURBS_ERROR35 100285
#define GLU_NURBS_ERROR36 100286
#define GLU_NURBS_ERROR37 100287

/* Contours types -- obsolete! */
#define GLU_CW 100120
#define GLU_CCW 100121
#define GLU_INTERIOR 100122
#define GLU_EXTERIOR 100123
#define GLU_UNKNOWN 100124

/* Names without "TESS_" prefix */
#define GLU_BEGIN GLU_TESS_BEGIN
#define GLU_VERTEX GLU_TESS_VERTEX
#define GLU_END GLU_TESS_END
#define GLU_ERROR GLU_TESS_ERROR
#define GLU_EDGE_FLAG GLU_TESS_EDGE_FLAG



#if API_VERSION >= 259

/* Nurbs tesselator */
#define GLU_NURBS_MODE             100160

#define GLU_NURBS_TESSELLATOR      100161
#define GLU_NURBS_RENDERER         100162

#define GLU_NURBS_BEGIN	               100164
#define GLU_NURBS_VERTEX                   100165
#define GLU_NURBS_NORMAL                   100166
#define GLU_NURBS_COLOR                    100167
#define GLU_NURBS_TEXTURE_COORD            100168
#define GLU_NURBS_END                      100169

#define GLU_NURBS_BEGIN_DATA	       100170
#define GLU_NURBS_VERTEX_DATA              100171
#define GLU_NURBS_NORMAL_DATA              100172
#define GLU_NURBS_COLOR_DATA               100173
#define GLU_NURBS_TEXTURE_COORD_DATA       100174
#define GLU_NURBS_END_DATA                 100175

/* Object space tess */
#define GLU_OBJECT_PARAMETRIC_ERROR 100208 
#define GLU_OBJECT_PATH_LENGTH 100209

#endif

/*
FIXME: why do we need import string here?
*/
%shadow %{
def __info():
    import string
    return [('GLU_VERSION', GLU_VERSION, 'su'),
    ('GLU_EXTENSIONS', GLU_EXTENSIONS, 'eu')]

%}


%shadow %{
GLUerror = _GLU__init__.GLUerror

__api_version__ = _GLU__init__.__api_version__
__author__ = _GLU__init__.__author__
__date__ = _GLU__init__.__date__
__doc__ = _GLU__init__.__doc__
__version__ = _GLU__init__.__version__

%}


