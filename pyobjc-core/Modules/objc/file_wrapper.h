#if PY_MAJOR_VERSION == 3
/* A basic wrapper for C's "FILE*"
 * that implements a usable API.
 */
extern PyTypeObject FILE_Type;

#define FILE_Check(obj) PyObject_TypeCheck(obj, &FILE_Type)

extern PyObject* FILE_create(FILE* fp);
extern FILE* FILE_get(PyObject* fp);

#endif
