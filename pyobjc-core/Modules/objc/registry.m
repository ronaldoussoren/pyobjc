/*
 * registry.m -- Storing and finding exception data.
 *
 * This file defines generic functionality to store exception data for
 * a class/method.
 */
#include "pyobjc.h"

BOOL PyObjC_UpdatingMetaData = NO;

PyObject*
PyObjC_NewRegistry(void)
{
	return PyDict_New();
}


int 
PyObjC_AddToRegistry(
		PyObject* registry,
		PyObject* class_name, PyObject* selector, 
		PyObject* value)
{
	PyObject* sublist;
	PyObject* item = Py_BuildValue("(OO)", class_name, value);	
	if (item == NULL) {
		return -1;
	}

	sublist = PyDict_GetItem(registry, selector);
	if (sublist == NULL) {
		sublist = PyList_New(0);
		PyDict_SetItem(registry, selector, sublist);
		Py_DECREF(sublist);
	}

	if (!PyObjC_UpdatingMetaData) {
		PyObjC_MappingCount += 1;
	}
	int result = PyList_Append(sublist, item);
	Py_DECREF(item);
	return result;
}

PyObject*
PyObjC_FindInRegistry(PyObject* registry, Class cls, SEL selector)
{
	Py_ssize_t i;
	Py_ssize_t len;
	PyObject* cur;
	Class found_class = nil;
	PyObject* found_value = NULL;
	PyObject* sublist;

	if (registry == NULL) {
		return NULL;
	}
	sublist = PyDict_GetItemString(registry, (char*)sel_getName(selector));
	if (sublist == NULL) return NULL;

	len = PyList_Size(sublist);
	for (i = 0; i < len; i++) {
		Class cur_class;

		cur = PyList_GET_ITEM(sublist, i);
		if (cur == NULL) {
			PyErr_Clear();
			continue;
		}

		if (!PyTuple_CheckExact(cur)) {
			PyErr_SetString(PyObjCExc_InternalError, 
				"Exception registry element isn't a tuple");
			return NULL;
		}

		cur_class = objc_lookUpClass(
				PyString_AsString(PyTuple_GET_ITEM(cur, 0)));
		if (cur_class == nil) {
			continue;
		}

		if (!class_isSubclassOf(cls, cur_class) && !class_isSubclassOf(cls, object_getClass(cur_class))) {
			continue;
		}

		if (found_class != NULL && found_class != cur_class) {
			if (class_isSubclassOf(found_class, cur_class)) {
				continue;
			}
		}
	
		found_class = cur_class;
		Py_INCREF(PyTuple_GET_ITEM(cur, 1));
		Py_XDECREF(found_value);
		found_value = PyTuple_GET_ITEM(cur, 1);
	}
	
	return found_value;
}
