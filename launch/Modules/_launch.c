#include "Python.h"
#include <launch.h>

/*
 * The types that are used to represent file descriptors and errno values.
 *
 * These are assumed to be subtypes of int.
 */
static PyObject* file_descriptor_type = NULL;
static PyObject* errno_type = NULL;

/*
 * Conversion of a launch_data_t item to a pytho object
 */

static PyObject* launchdict2python(launch_data_t data);
static PyObject* launcharray2python(launch_data_t data);


static PyObject* 
launch2python(launch_data_t data)
{
	launch_data_type_t tp;

	tp = launch_data_get_type(data);
	switch (tp) {
	case LAUNCH_DATA_DICTIONARY:
		return launchdict2python(data);
	
	case LAUNCH_DATA_ARRAY:
		return launcharray2python(data);
	
	case LAUNCH_DATA_FD:
		return PyObject_CallFunction(file_descriptor_type, "i", 
				launch_data_get_fd(data));
		return NULL;

	case LAUNCH_DATA_INTEGER:
		return PyLong_FromLongLong(launch_data_get_integer(data));

	case LAUNCH_DATA_REAL:
		return PyFloat_FromDouble(launch_data_get_real(data));

	case LAUNCH_DATA_BOOL:
		return PyBool_FromLong(launch_data_get_bool(data));

	case LAUNCH_DATA_STRING:
		return PyString_FromString(launch_data_get_string(data));

	case LAUNCH_DATA_OPAQUE:
		return PyBuffer_FromMemory(
				launch_data_get_opaque(data),
				launch_data_get_opaque_size(data));

	case LAUNCH_DATA_ERRNO:
		return PyObject_CallFunction(errno_type, "i", 
				launch_data_get_errno(data));

	default:
		PyErr_Format(PyExc_ValueError,
			"Unhandled launch data type (tag: %d)", (int)tp);
		return NULL;
	}
}

static PyObject* 
launcharray2python(launch_data_t data)
{
	size_t count = launch_data_array_get_count(data);
	size_t i;
	PyObject* result = PyList_New(count);

	for (i = 0; i < 0; i ++) {
		launch_data_t v = launch_data_array_get_index(data, i);
		PyList_SET_ITEM(result, i, launch2python(data));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(result);
		return NULL;
	}
	return result;
}

static void
launchdict_cb(launch_data_t value, const char* key, void* pydict)
{
	PyDict_SetItemString((PyObject*)pydict,
			key,
			launch2python(value));
}

static PyObject* 
launchdict2python(launch_data_t data)
{
	PyObject* result = PyDict_New();

	launch_data_dict_iterate(data, launchdict_cb, result);
	if (PyErr_Occurred()) {
		Py_DECREF(result);
		return NULL;
	}
	return result;
}

/*
 * Conversion of a python object to a launch_data_t item.
 */

static launch_data_t pythondict2launch(PyObject* object);
static launch_data_t pythonarray2launch(PyObject* object);

static launch_data_t
python2launch(PyObject* object)
{
	launch_data_t result;

	if (PyDict_Check(object)) {
		/* PyMapping_Check doesn't work because a lot of sequence types
		 * are mappings as wel to support extended slices a[i:j:k]
		 */
		return pythondict2launch(object);
	} else if (PySequence_Check(object)) {
		return pythonarray2launch(object);
	} else if (PyInt_Check(object)) {
		long value = PyInt_AsLong(object);
		
		result = launch_data_alloc(LAUNCH_DATA_INTEGER);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_integer(result, value)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}
	} else if (PyLong_Check(object)) {
		long long value = PyLong_AsLongLong(object);

		result = launch_data_alloc(LAUNCH_DATA_INTEGER);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_integer(result, value)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}

	} else if (PyString_Check(object)) {
		char* value = PyString_AsString(object);

		result = launch_data_alloc(LAUNCH_DATA_STRING);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_string(result, value)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}

	} else if ((PyObject*)(object->ob_type) == file_descriptor_type) {
		long value = PyInt_AsLong(object);
		
		result = launch_data_alloc(LAUNCH_DATA_FD);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_fd(result, value)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}

	} else if ((PyObject*)(object->ob_type) == errno_type) {
		long value = PyInt_AsLong(object);
		
		result = launch_data_alloc(LAUNCH_DATA_ERRNO);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_errno(result, value)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}

	} else if (object->ob_type->tp_as_buffer != NULL) {
		PyBufferProcs* bp = object->ob_type->tp_as_buffer;
		void* ptr;
		size_t size;

		size = bp->bf_getreadbuffer(object, 0, &ptr);
		if (size == (size_t)-1) {
			return NULL;
		}

		result = launch_data_alloc(LAUNCH_DATA_OPAQUE);
		if (result == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"allocating launch_data_t failed");
			return NULL;
		}
		if (!launch_data_set_opaque(result, ptr, size)) {
			PyErr_SetString(PyExc_TypeError,
				"setting launch_data_t failed");
			launch_data_free(result);
			return NULL;
		}

	} else {
		PyErr_Format(PyExc_TypeError,
			"Don't know how to convert object of type %s to launch",
			object->ob_type->tp_name);
		return NULL;
	}
}

static launch_data_t 
pythonarray2launch(PyObject* object)
{
	/* TODO: Using PySequence_Fast */
	return NULL;
}

static launch_data_t 
pythondict2launch(PyObject* object)
{
	/* TODO */
	return NULL;
}


PyDoc_STRVAR(doc_launch_get_fd,
    "launch_get_fd() -> file_descriptor\n\n"
    "Returns the file descriptor that this API uses, for use with async \n"
    "I/O APIs like select()");
static PyObject*
wrap_launch_get_fd(PyObject* self)
{
	return PyInt_FromLong(launch_get_fd());
}

PyDoc_STRVAR(doc_launch_msg,
    "launch_msg(message) -> message\n\n"
    "Use this to send and receive messages. The argument is the message to \n"
    "send or None. Returns None if no more messages are available.\n"
    "\n"
    "The message is a normal python data structure (dict, list, string, ...)\n"
    "use errno_wrapper to send an errno and file_descriptor_wrapper to send \n"
    "a file descriptor."
);
static PyObject* 
wrap_launch_msg(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "message", NULL };
	launch_data_t  to_send, to_receive;
	PyObject* message;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &message)) {
		return NULL;
	}

 	if (message == Py_None) {
		to_send = NULL;
	} else {
		to_send = python2launch(message);
		if (to_send == NULL) {
			return NULL;
		}
	}

	/* launch_msg returns NULL if no message has arrived or when there
	 * was a problem sending. It only sets errno in the latter case.
	 */
	Py_BEGIN_ALLOW_THREADS
		errno = 0;
		to_receive = launch_msg(to_send);
	Py_END_ALLOW_THREADS
	if (to_send != NULL) {
		launch_data_free(to_send);
		to_send = NULL;
	}

	if (to_receive == NULL) {
		if (errno) {
			PyErr_SetFromErrno(PyExc_IOError);
			return NULL;
		}
		Py_INCREF(Py_None);
		return Py_None;
	} else {
		message = launch2python(to_receive);
		launch_data_free(to_receive);
		return message;
	}
}

static PyObject*
set_types(PyObject* self, PyObject* args)
{
	 if(!PyArg_ParseTuple(args, "OO", &file_descriptor_type, &errno_type)) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef launch_methods[] = {
	{
		"launch_get_fd",
		(PyCFunction)wrap_launch_get_fd,
		METH_NOARGS,
		doc_launch_get_fd
	},
	{
		"launch_msg",
		(PyCFunction)wrap_launch_msg,
		METH_VARARGS|METH_KEYWORDS,
		doc_launch_msg
	},
	{
		"set_types",
		(PyCFunction)set_types,
		METH_VARARGS,
		NULL
	},
	{
		NULL, NULL, 0, NULL
	}
};

void
init_launch(void)
{
	Py_InitModule3("_launch", launch_methods, NULL);
}
