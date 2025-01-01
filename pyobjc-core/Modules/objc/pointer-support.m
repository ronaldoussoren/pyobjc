/*
 * Special wrappers for pointer values
 *
 * Pointer arguments to methods can be split into 3 classes:
 * - Pass-by-reference arguments (in, out, inout).
 *   This is supported by using the modifiers _C_IN, _C_OUT and _C_INOUT
 * - Pointers to buffers
 *   This requires special support, you can't detect the size of the buffer
 *   from the signature
 * - Opaque values
 *   Types like FSRef are for all intents and purposes opaque values,
 *   that happen to be represented using pointers (to structs). The functions
 *   in this file allow extension modules to register functions to convert these
 *   values to and from their Python representation.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

typedef    PyObject* _Nullable (*pythonify_func)(void*);
typedef    int (*depythonify_func)(PyObject*, void*);

struct wrapper {
    const char* name;
    const char* signature;
    size_t      offset;
    pythonify_func pythonify;
    depythonify_func depythonify;
};

/* Using an array is pretty lame, this needs to be replaced by a more
 * efficient datastructure. However: As long as their is only a limited
 * number of custom wrappers this should not be a problem.
 */
static struct wrapper* items      = 0;
static Py_ssize_t      item_count = 0;

#ifdef Py_GIL_DISABLED
/*
 * Mutex protecting *items*.
 */
static PyMutex items_mutex = {0};
#endif


/*
 * If signature is a pointer to a structure return the index of the character
 * just beyond the end of the struct name. This information is needed because
 * @encode(struct foo*) can return two different strings:
 * 1) ^{foo} if the compiler has not yet seen a full definition of struct foo
 * 2) ^{foo=...} if the compiler has seen a full definition of the struct
 * We want to treat those two pointer as the same type, therefore we need to
 * ignore everything beyond the end of the struct name.
 */
static size_t
find_end_of_structname(const char* signature)
{
    if ((signature[1] == _C_CONST && signature[2] == _C_STRUCT_B)
        || (signature[1] == _C_STRUCT_B)) {

        char* end;

        end = strchr(signature, '=');

        if (end == NULL) {
            end = strchr(signature, _C_STRUCT_E);
            /* XXX: What if end is NULL */
            return (size_t)(end - signature);

        } else {
            return (size_t)(end - signature);
        }
    }
    return strlen(signature);
}

/* XXX: This is unsafe in free threaded mode, options:
 * 1. Return 'struct wrapper' (e.g. a copy of the found entry)
 * 2. Add variants returning the fields used by other parts of this file
 */
static int FindWrapper(const char* signature, pythonify_func* _Nullable pythonify, depythonify_func* _Nullable depythonify, const char**_Nullable name)
{
    /* XXX: This is a linear search, find better way to do this! */
    Py_ssize_t i;

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&items_mutex);
#endif
    for (i = 0; i < item_count; i++) {
        if (strncmp(signature, items[i].signature, items[i].offset) == 0) {
            /* See comment just above find_end_of_structname */
            if (signature[1] == _C_CONST && signature[2] == _C_STRUCT_B) {
                /* XXX: Shouldn't this adjust for _C_CONST? */
                char ch = signature[items[i].offset];
                if (ch == '=' || ch == _C_STRUCT_E) {
                    if (pythonify != NULL) {
                        *pythonify = items[i].pythonify;
                    }
                    if (depythonify != NULL) {
                        *depythonify = items[i].depythonify;
                    }
                    if (name != NULL) {
                        *name = items[i].name;
                    }
#ifdef Py_GIL_DISABLED
                    PyMutex_Unlock(&items_mutex);
#endif
                    return 0;
                }

            } else if (signature[1] == _C_STRUCT_B) {
                char ch = signature[items[i].offset];
                if (ch == '=' || ch == _C_STRUCT_E) {
                    if (pythonify != NULL) {
                        *pythonify = items[i].pythonify;
                    }
                    if (depythonify != NULL) {
                        *depythonify = items[i].depythonify;
                    }
                    if (name != NULL) {
                        *name = items[i].name;
                    }
#ifdef Py_GIL_DISABLED
                    PyMutex_Unlock(&items_mutex);
#endif
                    return 0;
                }

            } else {
                if (signature[items[i].offset] == '\0') {
                    if (pythonify != NULL) {
                        *pythonify = items[i].pythonify;
                    }
                    if (depythonify != NULL) {
                        *depythonify = items[i].depythonify;
                    }
                    if (name != NULL) {
                        *name = items[i].name;
                    }
#ifdef Py_GIL_DISABLED
                    PyMutex_Unlock(&items_mutex);
#endif
                    return 0;
                }
            }
        }
    }
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&items_mutex);
#endif
    if (pythonify != NULL) {
        *pythonify = NULL;
    }
    if (depythonify != NULL) {
        *depythonify = NULL;
    }
    if (name != NULL) {
        *name = NULL;
    }
    return -1;
}

static PyObject* _Nullable ID_to_py(const void* idValue)
{
    if (idValue == kCFAllocatorUseContext) {
        /* kCFAllocatorUseContext is a bit too magic for its
         * own good.
         *
         * Note that this is a crude hack, but as long as this
         * is the only such object I don't think its worthwhile
         * to add generic support for this.
         */
        PyObject* result = PyObjC_FindPythonProxy((id)idValue);
        if (result != NULL) {
            return result;
        }

        result = PyObjCCF_NewSpecialFromTypeID(CFAllocatorGetTypeID(), (void*)idValue);

        if (result != NULL) {
            PyObject* actual = PyObjC_RegisterPythonProxy(idValue, result);
            Py_DECREF(result);
            return actual;
        }
        return result;
    }
    return id_to_python((id)idValue);
}

static int
py_to_ID(PyObject* obj, void* output)
{
    return depythonify_python_object(obj, output);
}

PyObject* _Nullable PyObjCPointer_GetIDEncodings(void)
{
    Py_ssize_t i;
    PyObject*  result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }
#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&items_mutex);
#endif
    for (i = 0; i < item_count; i++) {
        if (items[i].pythonify == (PyObjCPointerWrapper_ToPythonFunc)&ID_to_py) {
            PyObject* cur = PyBytes_FromString(items[i].signature);
            if (cur == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(result);
#ifdef Py_GIL_DISABLED
                PyMutex_Unlock(&items_mutex);
#endif
                return NULL;
                // LCOV_EXCL_STOP
            }
            if (PyList_Append(result, cur) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(cur);
                Py_DECREF(result);
#ifdef Py_GIL_DISABLED
                PyMutex_Unlock(&items_mutex);
#endif
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(cur);
        }
    }
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&items_mutex);
#endif
    return result;
}

int
PyObjCPointerWrapper_RegisterID(const char* name, const char* signature)
{
    return PyObjCPointerWrapper_Register(name, signature,
                                         (PyObjCPointerWrapper_ToPythonFunc)&ID_to_py,
                                         (PyObjCPointerWrapper_FromPythonFunc)&py_to_ID);
}

int
PyObjCPointerWrapper_Register(const char* name, const char* signature,
                              PyObjCPointerWrapper_ToPythonFunc   pythonify,
                              PyObjCPointerWrapper_FromPythonFunc depythonify)
{
    PyObjC_Assert(signature, -1);
    PyObjC_Assert(pythonify, -1);
    PyObjC_Assert(depythonify, -1);
    PyObjCPointerWrapper_ToPythonFunc cur_pythonify;
    PyObjCPointerWrapper_FromPythonFunc cur_depythonify;

#if 0
    /* XXX: Disabled because this is inherently problematic for
     *      the free threaded build.
     *
     *      It should be possibly to implement this in a way that's
     *      compatible with free threading, but that's only needed
     *      if the code is actually needed.
     */
    struct wrapper* value = FindWrapper(signature);

    if (value != NULL) {
        /* Update existing registration */
        value->pythonify   = pythonify;
        value->depythonify = depythonify;
        return 0;
    }
#else
    if (FindWrapper(signature, &cur_pythonify, &cur_depythonify, NULL) == 0) {
        if (cur_pythonify != pythonify || cur_depythonify != depythonify) { // LCOV_BR_EXCL_LINE
            /* Hitting this would be a bug in PyObjC (aka, this is a fancy spelling of  PyObjC_Assert) */
            // LCOV_EXCL_START
            PyErr_Format(PyObjCExc_Error, "already have registration for signature '%s'", signature);
            return -1;
            // LCOV_EXCL_STOP
        }
    }
#endif

#ifdef Py_GIL_DISABLED
    PyMutex_Lock(&items_mutex);
#endif
    struct wrapper* tmp = PyMem_Realloc(items, sizeof(struct wrapper) * (item_count + 1));
    if (tmp == NULL) {    // LCOV_BR_EXCL_LINE
        PyErr_NoMemory(); // LCOV_EXCL_LINE
        return -1;        // LCOV_EXCL_LINE
    }
    items = tmp;
#ifdef Py_GIL_DISABLED
    PyMutex_Unlock(&items_mutex);
#endif

    char* tmp_name = PyObjCUtil_Strdup(name);
    if (tmp_name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }
    items[item_count].name = tmp_name;

    char* tmp_sig = PyObjCUtil_Strdup(signature);
    if (tmp_sig == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free((void*)items[item_count].name);
        PyErr_NoMemory();
        return -1;
        // LCOV_EXCL_STOP
    }
    items[item_count].signature = tmp_sig;

    items[item_count].offset = find_end_of_structname(items[item_count].signature);

    items[item_count].pythonify   = pythonify;
    items[item_count].depythonify = depythonify;

    /* Update item_count to ensure that other threads won't see
     * a partially initialized entry.
     */
    item_count++;

    return 0;
}

PyObject* _Nullable PyObjCPointerWrapper_ToPython(const char* type, const void* datum)
{
    PyObject*       result;
    pythonify_func  pythonify;


    if (FindWrapper(type, &pythonify, NULL, NULL) == -1) {
        return NULL;
    }

    result = pythonify(*(void**)datum);
    return result;
}

int
PyObjCPointerWrapper_FromPython(const char* type, PyObject* value, void* datum)
{
    depythonify_func depythonify;

    if (value == PyObjC_NULL) {
        *(void**)datum = NULL;
        return 0;
    }

    if (FindWrapper(type, NULL, &depythonify, NULL) == -1) {
        return -1;
    }

    return depythonify(value, datum)==0?0:-1;
}

int
PyObjCPointerWrapper_HaveWrapper(const char* type)
{
    return (FindWrapper(type, NULL, NULL, NULL) != -1);
}

static PyObject* _Nullable PyObjectPtr_New(void* obj) { return (PyObject*)obj; }

static int
PyObjectPtr_Convert(PyObject* obj, void* pObj)
{
    *(void**)pObj = (void*)obj;
    return 0;
}

static PyObject* _Nullable class_new(void* obj) { return pythonify_c_value("#", &obj); }

static int
class_convert(PyObject* obj, void* pObj)
{
    return depythonify_c_value("#", obj, pObj);
}

static PyObject* _Nullable FILE_New(void* obj)
{
    FILE* fp = (FILE*)obj;

    return FILE_create(fp);
}

static int
FILE_Convert(PyObject* obj, void* pObj)
{
    *(FILE**)pObj = FILE_get(obj);
    if (*(FILE**)pObj == NULL) {
        return 1;
    }

    return 0;
}

int
PyObjCPointerWrapper_Init(PyObject* module __attribute__((__unused__)))
{
    int r = 0;

    r = PyObjCPointerWrapper_Register("PyObject*", @encode(PyObject*), PyObjectPtr_New,
                                      PyObjectPtr_Convert);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjCPointerWrapper_Register("PyObject*", "^{PyObject=}", PyObjectPtr_New,
                                      PyObjectPtr_Convert);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjCPointerWrapper_Register("Class", "^{objc_class=}", class_new,
                                      class_convert);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    r = PyObjCPointerWrapper_Register("FILE*", @encode(FILE*), FILE_New, FILE_Convert);
    if (r == -1)   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE

    /* Issue #298, at least in Xcode 11.3 the following code results in
     * a type encoding of "^{NSObject=#}" instead of "@" for the property:
     *
     * typedef NSObject<NSObject> ObjectClass;
     *
     * ...
     * @property ObjectClass* value;
     * ...
     */
    if (PyObjCPointerWrapper_RegisterID( // LCOV_BR_EXCL_LINE
            "NSObject", "^{NSObject=#}")
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

const char* _Nullable PyObjCPointerWrapper_Describe(const char* signature)
{
    const char* name;
    if (FindWrapper(signature, NULL, NULL, &name) == -1) {
        return NULL;
    }

    return name;
}

NS_ASSUME_NONNULL_END
