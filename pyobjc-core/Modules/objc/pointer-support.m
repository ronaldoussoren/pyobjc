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

struct wrapper {
    const char* name;
    const char* signature;
    size_t      offset;
    PyObject* _Nullable (*pythonify)(void*);
    int (*depythonify)(PyObject*, void*);
};

/* Using an array is pretty lame, this needs to be replaced by a more
 * efficient datastructure. However: As long as their is only a limited
 * number of custom wrappers this should not be a problem.
 */
static struct wrapper* items      = 0;
static Py_ssize_t      item_count = 0;

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

static struct wrapper* _Nullable FindWrapper(const char* signature)
{
    /* XXX: This is a linear search, find better way to do this! */
    Py_ssize_t i;

    for (i = 0; i < item_count; i++) {
        if (strncmp(signature, items[i].signature, items[i].offset) == 0) {
            /* See comment just above find_end_of_structname */
            if (signature[1] == _C_CONST && signature[2] == _C_STRUCT_B) {
                /* XXX: Shouldn't this adjust for _C_CONST? */
                char ch = signature[items[i].offset];
                if (ch == '=' || ch == _C_STRUCT_E) {
                    return items + i;
                }

            } else if (signature[1] == _C_STRUCT_B) {
                char ch = signature[items[i].offset];
                if (ch == '=' || ch == _C_STRUCT_E) {
                    return items + i;
                }

            } else {
                if (signature[items[i].offset] == '\0') {
                    return items + i;
                }
            }
        }
    }
    return NULL;
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
            PyObjC_RegisterPythonProxy(idValue, result);
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
    if (result == NULL) {
        return NULL;
    }
    for (i = 0; i < item_count; i++) {
        if (items[i].pythonify == (PyObjCPointerWrapper_ToPythonFunc)&ID_to_py) {
            PyObject* cur = PyBytes_FromString(items[i].signature);
            if (cur == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            if (PyList_Append(result, cur) == -1) {
                Py_DECREF(cur);
                Py_DECREF(result);
                return NULL;
            }
            Py_DECREF(cur);
        }
    }
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

    struct wrapper* value = FindWrapper(signature);

    if (value != NULL) {
        /* Update existing registration */
        value->pythonify   = pythonify;
        value->depythonify = depythonify;
        return 0;
    }

    struct wrapper* tmp = PyMem_Realloc(items, sizeof(struct wrapper) * (item_count + 1));
    if (tmp == NULL) {    // LCOV_BR_EXCL_LINE
        PyErr_NoMemory(); // LCOV_EXCL_LINE
        return -1;        // LCOV_EXCL_LINE
    }
    items = tmp;
    item_count++;

    value = items + (item_count - 1);

    char* tmp_name = PyObjCUtil_Strdup(name);
    if (tmp_name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        item_count--;
        return -1;
        // LCOV_EXCL_STOP
    }
    value->name = tmp_name;

    char* tmp_sig = PyObjCUtil_Strdup(signature);
    if (tmp_sig == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free((void*)value->name);
        PyErr_NoMemory();
        item_count--;
        return -1;
        // LCOV_EXCL_STOP
    }
    value->signature = tmp_sig;

    value->offset = find_end_of_structname(value->signature);

    value->pythonify   = pythonify;
    value->depythonify = depythonify;

    return 0;
}

PyObject* _Nullable PyObjCPointerWrapper_ToPython(const char* type, const void* datum)
{
    struct wrapper* item;
    PyObject*       result;

    item = FindWrapper(type);
    if (item == NULL) {
        return NULL;
    }

    result = item->pythonify(*(void**)datum);
    return result;
}

int
PyObjCPointerWrapper_FromPython(const char* type, PyObject* value, void* datum)
{
    struct wrapper* item;
    int             r;

    if (value == PyObjC_NULL) {
        *(void**)datum = NULL;
        return 0;
    }

    item = FindWrapper(type);
    if (item == NULL) {
        return -1;
    }

    r = item->depythonify(value, datum);
    if (r == 0) {
        return 0;
    } else {
        return -1;
    }
}

int
PyObjCPointerWrapper_HaveWrapper(const char* type)
{
    return (FindWrapper(type) != NULL);
}

static PyObject* _Nullable PyObjectPtr_New(void* obj) { return (PyObject*)obj; }

static int
PyObjectPtr_Convert(PyObject* obj, void* pObj)
{
    *(void**)pObj = (void*)obj;
    return 0;
}

static PyObject* _Nullable class_new(void* obj) { return pythonify_c_value("#", obj); }

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
    struct wrapper* wrapper = FindWrapper(signature);
    if (wrapper == NULL)
        return NULL;

    return wrapper->name;
}

NS_ASSUME_NONNULL_END
