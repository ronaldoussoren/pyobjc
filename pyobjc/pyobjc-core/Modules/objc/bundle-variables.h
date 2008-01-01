#ifndef PyObjC_BUNDLE_VARIABLES_H
#define PyObjC_BUNDLE_VARIABLES_H

PyObject* PyObjC_loadSpecialVar(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds);
PyObject* PyObjC_loadBundleVariables(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds);

PyObject* PyObjC_loadBundleFunctions(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds);

PyObject* PyObjC_loadFunctionList(PyObject* self __attribute__((__unused__)),
		                PyObject* args, PyObject* kwds);


#endif /* PyObjC_BUNDLE_VARIABLES_H */
