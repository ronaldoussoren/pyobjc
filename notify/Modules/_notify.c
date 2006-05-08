/*
 * Wrappers for C functions in notify.h
 */
#include <Python.h>

#include <notify.h>

static PyObject* error = NULL;

static PyObject* raise_exception(uint32_t status)
{
	PyObject* v = Py_BuildValue("L", (unsigned long)status);
	if (v == NULL) return NULL;

	PyErr_SetObject(error, v);
	Py_DECREF(v);
	return NULL;
}

PyDoc_STRVAR(doc_notify_post,
"notify_post(name) -> None\n\n"
"Send a notification for the given name to all clients that have registered \n"
"for notifications of this name. This is the only API required for an \n"
"application that only produces notifications."
);
static PyObject*
wrap_notify_post(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", NULL };

	char* name;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &name)) {
		return NULL;
	}
	
	Py_BEGIN_ALLOW_THREADS
		status = notify_post(name);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(doc_notify_register_check,
"notify_register_check(name) -> token\n\n"
"Creates a registration token to be used with notify_check, but no active\n"
"notifications will be delivered");
static PyObject*
wrap_notify_register_check(PyObject* self, PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "name", NULL };

	char* name;
	int token = 0;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", keywords, &name)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		status = notify_register_check(name, &token);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	return Py_BuildValue("i", token);
}

PyDoc_STRVAR(doc_notify_register_signal,
"notify_register_signal(name, signum) -> token\n\n"
"Request notification delivery by UNIX signal. A client may request signal\n"
"notification for multiple names. After a signal is delivered, the \n"
"notify_check routine may be called with each notification token to \n"
"determine wich name (if any) generated the signal notification");
static PyObject*
wrap_notify_register_signal(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "signum", NULL };

	char* name;
	int signum;
	int token = 0;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "si", keywords, &name, &signum)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		status = notify_register_signal(name, signum, &token);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	return Py_BuildValue("i", token);
}

/* XXX: Not wrapped: notify_register_mach_port, due to lack of a mach_port
 * datatype in Python.
 */

PyDoc_STRVAR(doc_notify_register_file_descriptor,
"notify_register_file_descriptor(name, notify_fd, flags) -> (notify_fd, token)\n\n"
"Request notification by file descriptor. This function will allocate a new\n"
"file descriptor unless NOTIFY_REUSE is set in the flags argument, in which\n"
"notify_fd must be a file descriptor that was returned from an earlier call\n"
"to this function.\n"
"\nNote that the kernel buffer for queued writes is limited, hence prompt \n"
"processing of notification is required to avoid loosing messages due to\n"
"overflow.\n"
"\nNotifications are delivered by an integer value written to the file \n"
"descriptor. The value will match the notification token for which the \n"
"notificaton was generated.\n");
static PyObject*
wrap_notify_register_file_descriptor(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "name", "notify_fd", "flags", NULL };

	char* name;
	int notify_fd;
	int flags;
	int token = 0;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sii", keywords,
					&name, &notify_fd, &flags)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		status = notify_register_file_descriptor(name, &notify_fd, flags, &token);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	return Py_BuildValue("ii", notify_fd, token);
}

PyDoc_STRVAR(doc_notify_check,
"notify_check(token) -> True|False"
"Check if any notifications have been posted. The result is true the first \n"
"time notify_check is called for a token. Subsequent calls returnTrue when \n"
"notifications have been posted for the name associated with the notification\n"
"token. \n\n"
"This routine is independent of notify_post. That is, this function will \n"
"return True if an application calls notify_post for a name and then calls\n"
"notify_check for a token associated with that name."
);
static PyObject*
wrap_notify_check(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "token", NULL };

	int token;
	int check;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "i", keywords, &token)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		status = notify_check(token, &check);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	return PyBool_FromLong(check);
}

PyDoc_STRVAR(doc_notify_cancel,
"notify_cancel(token) -> None\n\n"
"Cancel notification and free resources associated with a notification token.\n"
"Mach ports and file descriptors associated with a token are released when \n"
"all registration tokens associated with the port or file descriptor have \n"
"been cancelled\n");
static PyObject*
wrap_notify_cancel(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "token", NULL };

	int token;
	int check;
	uint32_t status;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "i", keywords, &token)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		status = notify_cancel(token);
	Py_END_ALLOW_THREADS

	if (status != NOTIFY_STATUS_OK) {
		return raise_exception(status);
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef notify_methods[] = {
	{
		"notify_post",
		(PyCFunction)wrap_notify_post,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_post
	},
	{
		"notify_register_check",
		(PyCFunction)wrap_notify_register_check,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_register_check
	},
	{
		"notify_register_signal",
		(PyCFunction)wrap_notify_register_signal,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_register_check
	},
	{
		"notify_register_file_descriptor",
		(PyCFunction)wrap_notify_register_file_descriptor,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_register_file_descriptor
	},
	{
		"notify_check",
		(PyCFunction)wrap_notify_check,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_check
	},
	{
		"notify_cancel",
		(PyCFunction)wrap_notify_cancel,
		METH_VARARGS|METH_KEYWORDS,
		doc_notify_cancel
	},
	{
		NULL,
		NULL,
		0,
		NULL
	}
};


void init_notify(void)
{
	PyObject* m;
	PyObject* v;
	PyObject* d;

	m = Py_InitModule3("_notify", notify_methods, NULL);
	if (m == NULL) {
		return;
	}

	v = PyDict_New();
	if (v == NULL) {
		return;
	}

	d = PyString_FromString(
"Raised by the notify functions when there is something wrong. The exception\n"
"code is one of the status codes defined in this module.");
	if (d == NULL) {
		Py_DECREF(v);
		return;
	}

	PyDict_SetItemString(v, "__doc__", d);
	Py_DECREF(d); d = NULL;
	
	error = PyErr_NewException("notify.error", NULL, v);
	Py_DECREF(v); v = NULL;
	if (error == NULL) {
		return;
	}

	/* XXX: check refcount semantics of this function */
	if (PyModule_AddObject(m, "error", error) != 0) {
		return;
	}
}
