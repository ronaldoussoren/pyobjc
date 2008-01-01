#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

#include <OpenGL/gl.h>

static PyObject*
call_NSOpenGLPixelFormat_initWithAttributes_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject *result;
	struct objc_super super;
	GLuint *attribs;
	PyObject *seq;
	NSOpenGLPixelFormat *pixelFormat;
	int i, count;

	if (!PyArg_ParseTuple(arguments, "O", &seq)) {
		return NULL;
	}

	seq = PySequence_Fast(seq, "attributes must be a sequence");
	if (seq == NULL) {
		return NULL;
	}
	count = PySequence_Fast_GET_SIZE(seq);

	attribs = PyMem_New(GLuint, count+1);
	if (attribs == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}
    
	for (i=0; i<count; ++i) {
		PyObjC_PythonToObjC(
			@encode(GLuint), 
			PySequence_Fast_GET_ITEM(seq, i),
			attribs + i);
	}
	attribs[count] = 0;
	Py_DECREF(seq);

	if (PyErr_Occurred()) {
		PyMem_Del(attribs);
		PyErr_Clear();
		PyErr_SetString(PyExc_ValueError, "attributes must be GLuint");
		return NULL;
	}
    
	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		pixelFormat = objc_msgSendSuper(&super,
			PyObjCSelector_GetSelector(method),
			attribs);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		pixelFormat = nil;
	PyObjC_ENDHANDLER

	if (pixelFormat == nil && PyErr_Occurred()) return NULL;

	result = PyObjC_IdToPython(pixelFormat);

	NSLog(@"result: %@", pixelFormat);
    
	PyMem_Del(attribs);
	return result;
}


static PyObject*
call_NSOpenGLContext_setValues_forParameter_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	long* values;
	PyObject* pyValues;
	PyObject* pyParam;
	PyObject* seq;
	NSOpenGLContextParameter param;
	Py_ssize_t count, i;


	if (!PyArg_ParseTuple(arguments, "OO", &pyValues, &pyParam)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSOpenGLContextParameter),
			pyParam, &param) == -1) {
		return NULL;
	}

	seq = PySequence_Fast(pyValues, "attributes must be a sequence");
	if (seq == NULL) {
		return NULL;
	}

	count = PySequence_Fast_GET_SIZE(seq);
#if 1
	if (param == NSOpenGLCPSwapRectangle) {
		if (count != 4) {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
				"param needs 4 integers, "
				"not %" PY_FORMAT_SIZE_T "d", count);
			return NULL;
		}
	} else if (
			(param == NSOpenGLCPSwapRectangleEnable)
		||	(param == NSOpenGLCPRasterizationEnable)
		||	(param == NSOpenGLCPSwapInterval)
		||	(param == NSOpenGLCPSurfaceOrder)
		||	(param == NSOpenGLCPSurfaceOpacity)
		||	(param == NSOpenGLCPStateValidation)
	) {
		if (count != 1)  {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
				"param needs 1 integer, "
				"not %" PY_FORMAT_SIZE_T "d", count);
			return NULL;
		}
	}
	/* else: lets hope the user knows what he's doing... */
#endif

	values = malloc(sizeof(long) * count);
	if (values == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		if (PyObjC_PythonToObjC(
			@encode(long),
			PySequence_Fast_GET_ITEM(seq, i),
			values + i) == -1) {

			PyErr_SetString(PyExc_ValueError,
					"attribute values must be integers");

			Py_DECREF(seq);
			free(values);
			return NULL;
		}
	}
	Py_DECREF(seq);

	PyObjC_DURING
                if (PyObjCIMP_Check(method)) {
			((void(*)(id, SEL, long*, NSOpenGLContextParameter))
			 PyObjCIMP_GetIMP(method))(
				 PyObjCObject_GetObject(self),
				 PyObjCIMP_GetSelector(method),
				 values,
				 param);
		} else {
			PyObjC_InitSuper(
				&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));
		
			objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				values, param);
		}

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	free(values);
	if (PyErr_Occurred()) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
call_NSOpenGLContext_getValues_forParameter_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	long* values;
	PyObject* pyParam;
	PyObject* seq;
	NSOpenGLContextParameter param;
	Py_ssize_t count, i;


	if (!PyArg_ParseTuple(arguments, "O", &pyParam)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSOpenGLContextParameter),
			pyParam, &param) == -1) {
		return NULL;
	}

	if (param == NSOpenGLCPSwapRectangle) {
		count = 4;
		
	} else if (
			(param == NSOpenGLCPSwapRectangleEnable)
		||	(param == NSOpenGLCPRasterizationEnable)
		||	(param == NSOpenGLCPSwapInterval)
		||	(param == NSOpenGLCPSurfaceOrder)
		||	(param == NSOpenGLCPSurfaceOpacity)
		||	(param == NSOpenGLCPStateValidation)
	) {
		count = 1;
	} else {
		PyErr_SetString(PyExc_ValueError, "Don't know how many values to allocate");
		return NULL;
	}

	values = malloc(sizeof(long) * count);
	if (values == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
                if (PyObjCIMP_Check(method)) {
			((void(*)(id, SEL, long*, NSOpenGLContextParameter))
			 PyObjCIMP_GetIMP(method))(
				 PyObjCObject_GetObject(self),
				 PyObjCIMP_GetSelector(method),
				 values,
				 param);
		} else {
			PyObjC_InitSuper(
				&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));
		
			objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				values, param);
		}

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	seq = PyTuple_New(count);
	for (i = 0; i < count; i++) {
		PyObject* v = PyObjC_ObjCToPython(@encode(long), values+i);
		if (v == NULL) {
			free(values);
			Py_DECREF(seq);
			return NULL;
		}
	}

	free(values);
	return seq;
}



static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_nsopengl(void);
void init_nsopengl(void)
{
	PyObject* m = Py_InitModule4("_nsopengl", mod_methods, "", NULL,
			PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

#if 0
	Class classNSOpenGLPixelFormat = objc_lookUpClass("NSOpenGLPixelFormat");

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLPixelFormat,
		@selector(initWithAttributes:),
		call_NSOpenGLPixelFormat_initWithAttributes_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}
#endif

	Class classNSOpenGLContext = objc_lookUpClass("NSOpenGLContext");


	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(getValues:forParameter:),
		call_NSOpenGLContext_getValues_forParameter_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(setValues:forParameter:),
		call_NSOpenGLContext_setValues_forParameter_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	return;
}
