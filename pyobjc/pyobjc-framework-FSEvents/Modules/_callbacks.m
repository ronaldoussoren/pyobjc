/*
 * Support for callback functions/structs in the FSEvents frameework.
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <CoreServices/CoreServices.h>

static const void*
m_retain_python(const void* value)
{
	PyGILState_STATE   state = PyGILState_Ensure();

	Py_XINCREF((PyObject*)value);

        PyGILState_Release(state);

	return value;
}

static void
m_release_python(const void* value)
{
	PyGILState_STATE   state = PyGILState_Ensure();

	Py_XDECREF((PyObject*)value);

        PyGILState_Release(state);
}

static CFStringRef
m_copyDescription_python(const void* value)
{
	CFStringRef result;
	PyObject* description;
	int r;

	PyGILState_STATE   state = PyGILState_Ensure();

	description = PyObject_Repr((PyObject*)value);
	if (description == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	r = PyObjC_PythonToObjC(@encode(CFStringRef), description, &result);
	Py_DECREF(description);
	if (r == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	/* description is autoreleased, we should donate a reference to
	 * our caller 
	 */
	CFRetain(result);

        PyGILState_Release(state);
	return result;
}

static FSEventStreamContext m_python_context_template = {
	0,
	NULL,
	m_retain_python,
	m_release_python,
	m_copyDescription_python
};

static void
m_FSEVentStreamCallback(
	ConstFSEventStreamRef streamRef,
	void* clientCallbackInfo,
	size_t numEvents,
	void* eventPaths,
	const FSEventStreamEventFlags eventFlags[],
	const FSEventStreamEventId eventIds[])
{
	PyGILState_STATE   state = PyGILState_Ensure();
	FSEventStreamCreateFlags flags;
	PyObject* callback;
	PyObject* info;
	PyObject* v;
	PyObject* paths;	

	v = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 0);
	if (PyObjC_PythonToObjC(
			@encode(FSEventStreamCreateFlags), v, &flags) < 0) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	info = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 1);
	callback = PyTuple_GET_ITEM((PyObject*)clientCallbackInfo, 2);

	if (flags & kFSEventStreamCreateFlagUseCFTypes) {
		/* The evenPaths are an CFArray */
		paths = PyObjC_ObjCToPython(@encode(CFArrayRef), &eventPaths);
		if (paths == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
	} else {
		/* The evenPaths are a CArray of C strings */
		paths = PyObjC_CArrayToPython(@encode(char*), 
				eventPaths, numEvents);
		if (paths == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
	}

	PyObject* py_streamRef = PyObjC_ObjCToPython(
			@encode(ConstFSEventStreamRef), 
			&streamRef);
	if (py_streamRef == NULL) {
		Py_DECREF(paths);
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_eventFlags = PyObjC_CArrayToPython(
			@encode(FSEventStreamCreateFlags), 
			(void*)eventFlags, numEvents);
	if (py_eventFlags == NULL) {
		Py_DECREF(paths);
		Py_DECREF(py_streamRef);
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_eventIds = PyObjC_CArrayToPython(
			@encode(FSEventStreamEventId), 
			(void*)eventIds, numEvents);
	if (py_eventIds == NULL) {
		Py_DECREF(paths);
		Py_DECREF(py_streamRef);
		Py_DECREF(py_eventFlags);
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* result = PyObject_CallFunction(callback,
			"OO" Py_ARG_SIZE_T "OOO",
			py_streamRef, info, numEvents, paths,
			py_eventFlags,
			py_eventIds);
	Py_DECREF(paths);
	Py_DECREF(py_streamRef);
	Py_DECREF(py_eventFlags);
	Py_DECREF(py_eventIds);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);

        PyGILState_Release(state);
}

PyDoc_STRVAR(m_FSEventStreamCreate_doc,
	"FSEventStreamCreate(allocator, callback, callback_info, \n"
	"	pathsToWatch, sinceWhen, latency, flags) -> stream\n"
	"\n"
	"NOTE: the callback info is passed directly, it is not a structure as\n"
	"it is in C");
static PyObject*
m_FSEventStreamCreate(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_callback;
	PyObject* py_callback_info;
	PyObject* py_pathsToWatch;
	PyObject* py_sinceWhen;
	PyObject* py_latency;
	PyObject* py_flags;

	if (!PyArg_ParseTuple(args, "OOOOOOO",
		&py_allocator, &py_callback, &py_callback_info,
		&py_pathsToWatch, &py_sinceWhen, &py_latency, &py_flags)) {

		return NULL;
	}
	
	CFAllocatorRef allocator;
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	CFArrayRef pathsToWatch;
	if (PyObjC_PythonToObjC(@encode(CFArrayRef), py_pathsToWatch, &pathsToWatch) < 0) {
		return NULL;
	}

	FSEventStreamEventId sinceWhen;
	if (PyObjC_PythonToObjC(@encode(FSEventStreamEventId), py_sinceWhen, &sinceWhen) < 0) {
		return NULL;
	}

	CFTimeInterval latency;
	if (PyObjC_PythonToObjC(@encode(CFTimeInterval), py_latency, &latency) < 0) {
		return NULL;
	}

	FSEventStreamCreateFlags flags;
	if (PyObjC_PythonToObjC(@encode(FSEventStreamCreateFlags), py_flags, &flags) < 0) {
		return NULL;
	}

	/*
	 * Build the actual callback info, which includes the flags because
	 * the arguments passed to the callback vary based on the value of
	 * flags.
	 */
	PyObject* info = Py_BuildValue("OOO",
			py_flags, py_callback_info, py_callback);
	if (info == NULL) {
		return NULL;
	}

	FSEventStreamContext context = m_python_context_template;
	context.info = info;

	FSEventStreamRef stream = NULL;

	PyObjC_DURING
		stream = FSEventStreamCreate(
				allocator,
				m_FSEVentStreamCallback,
				&context,
				pathsToWatch,
				sinceWhen,
				latency,
				flags);

	PyObjC_HANDLER
		stream = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(info);

	if (stream == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (stream == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(FSEventStreamRef), &stream);
	// FSEventStreamRef is not a CF type (AFAIK), hence the user is 
	// responsible for maintaining the refcount.
	//FSEventStreamRelease(stream);
	return result;
}


PyDoc_STRVAR(m_FSEventStreamCreateRelativeToDevice_doc,
	"FSEventStreamCreate(allocator, callback, callback_info, \n"
	"	deviceToWatch, pathsToWatchRelativeToDevice, sinceWhen, \n"
	"	latency, flags) -> stream\n"
	"\n"
	"NOTE: the callback info is passed directly, it is not a structure as\n"
	"it is in C");
static PyObject*
m_FSEventStreamCreateRelativeToDevice(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_callback;
	PyObject* py_callback_info;
	PyObject* py_pathsToWatch;
	PyObject* py_sinceWhen;
	PyObject* py_latency;
	PyObject* py_flags;
	PyObject* py_deviceToWatch;

	if (!PyArg_ParseTuple(args, "OOOOOOO",
		&py_allocator, &py_callback, &py_callback_info, 
		&py_deviceToWatch, &py_pathsToWatch, &py_sinceWhen, 
		&py_latency, &py_flags)) {

		return NULL;
	}
	
	CFAllocatorRef allocator;
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	dev_t deviceToWatch;
	if (PyObjC_PythonToObjC(@encode(dev_t), py_deviceToWatch, &deviceToWatch) < 0) {
		return NULL;
	}

	CFArrayRef pathsToWatch;
	if (PyObjC_PythonToObjC(@encode(CFArrayRef), py_pathsToWatch, &pathsToWatch) < 0) {
		return NULL;
	}

	FSEventStreamEventId sinceWhen;
	if (PyObjC_PythonToObjC(@encode(FSEventStreamEventId), py_sinceWhen, &sinceWhen) < 0) {
		return NULL;
	}

	CFTimeInterval latency;
	if (PyObjC_PythonToObjC(@encode(CFTimeInterval), py_latency, &latency) < 0) {
		return NULL;
	}

	FSEventStreamCreateFlags flags;
	if (PyObjC_PythonToObjC(@encode(FSEventStreamCreateFlags), py_flags, &flags) < 0) {
		return NULL;
	}

	/*
	 * Build the actual callback info, which includes the flags because
	 * the arguments passed to the callback vary based on the value of
	 * flags.
	 */
	PyObject* info = Py_BuildValue("OOO",
			py_flags, py_callback_info, py_callback);
	if (info == NULL) {
		return NULL;
	}

	FSEventStreamContext context = m_python_context_template;
	context.info = info;

	FSEventStreamRef stream = NULL;

	PyObjC_DURING
		stream = FSEventStreamCreateRelativeToDevice(
				allocator,
				m_FSEVentStreamCallback,
				&context,
				deviceToWatch,
				pathsToWatch,
				sinceWhen,
				latency,
				flags);
	PyObjC_HANDLER
		stream = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(info);

	if (stream == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (stream == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* result = PyObjC_ObjCToPython(
			@encode(FSEventStreamRef), &stream);
	// FSEventStreamRef is not a CF type (AFAIK), hence the user is 
	// responsible for maintaining the refcount.
	//FSEventStreamRelease(stream);
	return result;
}


static PyMethodDef m_methods[] = {
	{
		"FSEventStreamCreate",
		(PyCFunction)m_FSEventStreamCreate,
		METH_VARARGS,
		m_FSEventStreamCreate_doc
	},

	{
		"FSEventStreamCreateRelativeToDevice",
		(PyCFunction)m_FSEventStreamCreateRelativeToDevice,
		METH_VARARGS,
		m_FSEventStreamCreateRelativeToDevice_doc
	},


	{ 0, 0, 0, }
};

void init_callbacks(void);
void init_callbacks(void)
{
	PyObject* m = Py_InitModule4("_callbacks", m_methods,
		NULL, NULL, PYTHON_API_VERSION);

        if (PyObjC_ImportAPI(m) < 0) { return; }
}
