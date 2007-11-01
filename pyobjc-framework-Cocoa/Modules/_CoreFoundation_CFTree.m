#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static const void* 
mod_CFTreeRetainCallback(const void* info) 
{
	return [(NSObject*)info retain];
}

static void
mod_CFTreeReleaseCallback(const void* info)
{
	[(NSObject*)info release];
}

static CFStringRef
mod_CFTreeCopyDescriptionCallback(const void* info)
{
	NSString* result = [(NSObject*)info description];
	[result retain];
	return (CFStringRef)result;
}

static CFTreeContext mod_CFTreeContext = {
	0,		
	NULL,
	mod_CFTreeRetainCallback,
	mod_CFTreeReleaseCallback,
	mod_CFTreeCopyDescriptionCallback
};

static PyObject*
mod_CFTreeGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_tree;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_tree, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFTreeRef), py_tree, &tree) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFTreeGetContext(tree, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
		return NULL;
	}

	if (context.retain != mod_CFTreeRetainCallback) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
		return NULL;
	}

	return PyObjC_ObjCToPython(@encode(id), &context.info);
}

static PyObject*
mod_CFTreeSetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_tree;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;
	NSObject* info;

	if (!PyArg_ParseTuple(args, "O|O", &py_tree, &py_context)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFTreeRef), py_tree, &tree) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(id), py_context, &info) < 0) {
		return NULL;
	}

	context = mod_CFTreeContext;
	context.info = info;

	PyObjC_DURING
		CFTreeSetContext(tree, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}


static PyObject*
mod_CFTreeCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;
	CFAllocatorRef allocator;
	NSObject* info;

	if (!PyArg_ParseTuple(args, "O|O", &py_allocator, &py_context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(id), py_context, &info) < 0) {
		return NULL;
	}

	context = mod_CFTreeContext;
	context.info = info;


	tree = NULL;

	PyObjC_DURING
		tree = CFTreeCreate(allocator, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (tree == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* py_tree = PyObjC_ObjCToPython(@encode(CFTreeRef), &tree);
	CFRelease(tree); /* we're donated a reference */

	return py_tree;
}


static PyMethodDef mod_methods[] = {
        {
		"CFTreeCreate",
		(PyCFunction)mod_CFTreeCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFTreeGetContext",
		(PyCFunction)mod_CFTreeGetContext,
		METH_VARARGS,
		NULL
	},
        {
		"CFTreeSetContext",
		(PyCFunction)mod_CFTreeSetContext,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFTree(void);
void init_CFTree(void)
{
	PyObject* m = Py_InitModule4("_CFTree", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
