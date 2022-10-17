/*
 * Some helper function to replace most usage of
 * PyFunction_* and PyMethod_* APIs in PyObjC.
 *
 * The primary reason for introducing these APIs
 * is to enhance compatibility with Nuitka which
 * compiles Python code into C extensions and
 * in the compiled code functions and method are
 * represented by objects with the same interface,
 * but not inheriting in C from PyFunction and PyMethod.
 */
NS_ASSUME_NONNULL_BEGIN

extern int PyObjC_is_pyfunction(PyObject*);
extern int PyObjC_is_pymethod(PyObject*);
extern PyCodeObject* _Nullable PyObjC_get_code(PyObject*);
extern bool       PyObjC_returns_value(PyObject*);
extern Py_ssize_t PyObjC_num_defaults(PyObject*);
extern Py_ssize_t PyObjC_num_kwdefaults(PyObject*);
extern Py_ssize_t PyObjC_num_arguments(PyObject*);

NS_ASSUME_NONNULL_END
