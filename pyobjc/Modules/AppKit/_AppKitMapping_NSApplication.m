/*
 * NSModalSession support
 *
 * NSModalSession are opaque values, the 'pointer' attribute is provided to be 
 * able to check if two NSModalSessions are actually the same.
 */

static int 
_pyobjc_install_NSApplication(PyObject* module_dict)
{
	int r = 0;
	PyObject* v;

	v = PyObjCCreateOpaquePointerType("NSModalSession", @encode(NSModalSession), NULL);
	if (v == NULL) return -1;

	r = PyDict_SetItemString(module_dict, "NSModalSession", v);
	Py_DECREF(v);
	if (r != 0) {
		return -1;
	}

	return 0;
}
