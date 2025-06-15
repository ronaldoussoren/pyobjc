/*
 * This file defines a singleton object for getting/setting options/properties
 * for the core bridge.
 *
 * There are both public and private options/properties. The private ones have
 * names starting with an underscore and those can be changed without concern
 * for backward compatibility between releases.
 */
#include "pyobjc.h"

#include <netdb.h>


NS_ASSUME_NONNULL_BEGIN

/*
 * Empty object definition for the options object, this
 * is a singleton whose actual value is stored as a number
 * of global variables to make the options easier to use
 * from C.
 */
struct options {
    PyObject_HEAD
};

static PyObject* PyObjCOptions_Type;

/*
 * Free threading:
 * - PyObject options are guarded by a mutex to avoid race conditions between
 *   setting and using;
 * - Other options use atomic vars to ensure consistent updates.*
 *
 * Users of options should cache the value locally to get a consistent value
 * when it is used multiple times. PyObject users must either use the value
 * with an acquired lock, or get a local owned reference while holding the
 * mutex.
 */

#define _STR(v) #v
#define STR(v) _STR(v)

#ifdef Py_GIL_DISABLED
#   define MUTEX_FOR(VAR)        static PyMutex VAR##_lock = { 0 };
#   define LOCK(VAR)             PyMutex_Lock(&VAR##_lock)
#   define UNLOCK(VAR)           PyMutex_Unlock(&VAR##_lock)
#else
#   define MUTEX_FOR(VAR)
#   define LOCK(VAR) do {} while(0)
#   define UNLOCK(VAR) do {} while(0)
#endif

#define SSIZE_T_PROP(NAME, VAR, DFLT)                                                    \
    PyObjC_ATOMIC Py_ssize_t VAR = DFLT;                                                 \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        PyObject* result;                                                                \
        result = PyLong_FromSsize_t(VAR);                                                \
        return result;                                                                   \
    }                                                                                    \
                                                                                         \
    static int NAME##_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,     \
                          void* c __attribute__((__unused__)))                           \
    {                                                                                    \
        if (newVal == NULL) {                                                            \
            PyErr_SetString(PyExc_AttributeError,                                        \
                            "Cannot delete option '" STR(NAME) "'");                     \
            return -1;                                                                   \
        }                                                                                \
                                                                                         \
        Py_ssize_t temp;                                                                 \
        if (!PyArg_Parse(newVal, "n", &temp)) {                                          \
            return -1;                                                                   \
        }                                                                                \
        VAR = temp;                                                                      \
        return 0;                                                                        \
    }

#define INT_PROP(NAME, VAR, DFLT)                                                        \
    PyObjC_ATOMIC int VAR = DFLT;                                                        \
    MUTEX_FOR(VAR)                                                                       \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        PyObject* result;                                                                \
        result = PyLong_FromLong(VAR);                                                   \
        return result;                                                                   \
    }                                                                                    \
                                                                                         \
    static int NAME##_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,     \
                          void* c __attribute__((__unused__)))                           \
    {                                                                                    \
        if (newVal == NULL) {                                                            \
            PyErr_SetString(PyExc_AttributeError,                                        \
                            "Cannot delete option '" STR(NAME) "'");                     \
            return -1;                                                                   \
        }                                                                                \
                                                                                         \
        int temp;                                                                        \
        if (!PyArg_Parse(newVal, "i", &temp)) {                                          \
            return -1;                                                                   \
        }                                                                                \
        VAR = temp;                                                                      \
        return 0;                                                                        \
    }

#define BOOL_PROP(NAME, VAR, DFLT)                                                       \
    PyObjC_ATOMIC BOOL VAR = DFLT;                                                       \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        if (VAR) {                                                                       \
            Py_RETURN_TRUE;                                                              \
        } else {                                                                         \
            Py_RETURN_FALSE;                                                             \
        }                                                                                \
    }                                                                                    \
                                                                                         \
    static int NAME##_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,     \
                          void* c __attribute__((__unused__)))                           \
    {                                                                                    \
        if (newVal == NULL) {                                                            \
            PyErr_SetString(PyExc_AttributeError,                                        \
                            "Cannot delete option '" STR(NAME) "'");                     \
            return -1;                                                                   \
        }                                                                                \
        int b = PyObject_IsTrue(newVal);                                                 \
        if (b == -1) {                                                                   \
            return -1;                                                                   \
        }                                                                                \
        VAR = b ? YES : NO;                                                              \
        return 0;                                                                        \
    }

#define OBJECT_PROP(NAME, VAR)                                                           \
    PyObject* VAR = NULL;                                                                \
    MUTEX_FOR(VAR)                                                                       \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        LOCK(VAR);                                                                       \
        Py_INCREF(VAR);                                                                  \
        UNLOCK(VAR);                                                                     \
        return VAR;                                                                      \
    }                                                                                    \
                                                                                         \
    static int NAME##_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,     \
                          void* c __attribute__((__unused__)))                           \
    {                                                                                    \
        if (newVal == NULL) {                                                            \
            PyErr_SetString(PyExc_AttributeError,                                        \
                            "Cannot delete option '" STR(NAME) "'");                     \
            return -1;                                                                   \
        }                                                                                \
        LOCK(VAR);                                                                       \
        SET_FIELD_INCREF(VAR, newVal);                                                   \
        UNLOCK(VAR);                                                                     \
        return 0;                                                                        \
    }

#define OBJECT_PROP_STATIC(NAME, VAR)                                                    \
    static PyObject* VAR = NULL;                                                         \
    MUTEX_FOR(VAR)                                                                       \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        LOCK(VAR);                                                                       \
        Py_INCREF(VAR);                                                                  \
        UNLOCK(VAR);                                                                     \
        return VAR;                                                                      \
    }                                                                                    \
                                                                                         \
    static int NAME##_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,     \
                          void* c __attribute__((__unused__)))                           \
    {                                                                                    \
        if (newVal == NULL) {                                                            \
            PyErr_SetString(PyExc_AttributeError,                                        \
                            "Cannot delete option '" STR(NAME) "'");                     \
            return -1;                                                                   \
        }                                                                                \
        LOCK(VAR);                                                                       \
        SET_FIELD_INCREF(VAR, newVal);                                                   \
        UNLOCK(VAR);                                                                     \
        return 0;                                                                        \
    }

#define GETSET(NAME, DOC)                                                                \
    {                                                                                    \
        .name = STR(NAME), .get = NAME##_get, .set = NAME##_set, .doc = DOC,             \
    }

/* Public properties */
BOOL_PROP(verbose, PyObjC_Verbose, NO)
BOOL_PROP(use_kvo, PyObjC_UseKVO, YES)
BOOL_PROP(unknown_pointer_raises, PyObjCPointer_RaiseException, NO)
BOOL_PROP(structs_indexable, PyObjC_StructsIndexable, YES)
BOOL_PROP(structs_writable, PyObjC_StructsWritable, YES)

SSIZE_T_PROP(_mapping_count, PyObjC_MappingCount, 0)

/* Private properties */

OBJECT_PROP_STATIC(_nscoding_encoder, PyObjC_Encoder)
OBJECT_PROP_STATIC(_nscoding_decoder, PyObjC_Decoder)
OBJECT_PROP_STATIC(_copy, PyObjC_CopyFunc)
OBJECT_PROP_STATIC(_class_extender, PyObjC_ClassExtender)
OBJECT_PROP_STATIC(_make_bundleForClass, PyObjC_MakeBundleForClass)
OBJECT_PROP_STATIC(_nsnumber_wrapper, PyObjC_NSNumberWrapper)
OBJECT_PROP_STATIC(_callable_doc, PyObjC_CallableDocFunction)
OBJECT_PROP_STATIC(_callable_signature, PyObjC_CallableSignatureFunction)
OBJECT_PROP_STATIC(_mapping_types, PyObjC_DictLikeTypes)
OBJECT_PROP_STATIC(_sequence_types, PyObjC_ListLikeTypes)
OBJECT_PROP_STATIC(_set_types, PyObjC_SetLikeTypes)
OBJECT_PROP_STATIC(_date_types, PyObjC_DateLikeTypes)
OBJECT_PROP_STATIC(_path_types, PyObjC_PathLikeTypes)
OBJECT_PROP_STATIC(_datetime_date_type, PyObjC_DateTime_Date_Type)
OBJECT_PROP_STATIC(_datetime_datetime_type, PyObjC_DateTime_DateTime_Type)
OBJECT_PROP_STATIC(_getKey, PyObjC_getKey)
OBJECT_PROP_STATIC(_setKey, PyObjC_setKey)
OBJECT_PROP_STATIC(_getKeyPath, PyObjC_getKeyPath)
OBJECT_PROP_STATIC(_setKeyPath, PyObjC_setKeyPath)
OBJECT_PROP_STATIC(_transformAttribute, PyObjC_transformAttribute)
OBJECT_PROP_STATIC(_processClassDict, PyObjC_processClassDict)
OBJECT_PROP_STATIC(_setDunderNew, PyObjC_setDunderNew)
OBJECT_PROP_STATIC(_genericNewClass, PyObjC_genericNewClass)
OBJECT_PROP_STATIC(_ArrayType, PyObjC_ArrayType)
OBJECT_PROP_STATIC(_deepcopy, PyObjC_deepcopyFunc)
OBJECT_PROP_STATIC(_socket_error, PyObjC_socket_error)
OBJECT_PROP_STATIC(_socket_gaierror, PyObjC_socket_gaierror)
OBJECT_PROP_STATIC(_c_void_p, PyObjC_c_void_p)

static PyObject*
bundle_hack_get(PyObject* s __attribute__((__unused__)),
                void*     c __attribute__((__unused__)))
{
    /* XXX: Need to test on a 10.9 VM to check if this option is still needed... */
    if ([OC_NSBundleHack bundleHackUsed]) { // LCOV_BR_EXCL_LINE
        Py_RETURN_TRUE; // LCOV_EXCL_LINE
    } else {
        Py_RETURN_FALSE;
    }
}

PyObjC_ATOMIC int PyObjC_DeprecationVersion = 0;

static PyObject*
deprecation_warnings_get(PyObject* s __attribute__((__unused__)),
                         void*     c __attribute__((__unused__)))
{
    return PyUnicode_FromFormat("%d.%d", PyObjC_DeprecationVersion / 100,
                                PyObjC_DeprecationVersion % 100);
}

static int
deprecation_warnings_set(PyObject* s __attribute__((__unused__)), PyObject* newVal,
                         void* c __attribute__((__unused__)))
{
    if (newVal == NULL) {
        PyErr_SetString(PyExc_AttributeError,
                        "Cannot delete option 'deprecation_warnings'");
        return -1;
    } else if (PyLong_Check(newVal)) {
        if (PyErr_WarnEx(
                PyExc_DeprecationWarning,
                "Setting 'objc.options.deprecation_warnings' to an integer is deprecated",
                1)
            < 0) {
            return -1;
        }
        PyObjC_DeprecationVersion = (int)PyLong_AsLong(newVal);
        if (PyObjC_DeprecationVersion == -1 && PyErr_Occurred()) {
            return -1;
        }
        return 0;
    } else if (newVal == Py_None) {
        PyObjC_DeprecationVersion = 0;
        return 0;
    } else if (PyUnicode_Check(newVal)) {
        /* Cast to 'char*' is necessary to get rid of 'const', and that's
         * needed due to the harebrained interface of strtoul
         */
        char* text = (char*)PyUnicode_AsUTF8(newVal);
        if (text == NULL) { // LCOV_BR_EXCL_LINE
            return -1; // LCOV_EXCL_LINE
        }

        unsigned long major = 0;
        unsigned long minor = 0;

        errno = 0;
        major = strtoul(text, &text, 10);
        if (major >= 100 || ((major == 0 || major == ULONG_MAX) && errno != 0)) {
            PyErr_Format(PyExc_ValueError,
                         "Invalid version for 'objc.options.deprecation_warning': %R",
                         newVal);
            return -1;
        }
        if (*text != '\0') {
            if (*text != '.') {
                PyErr_Format(PyExc_ValueError,
                             "Invalid version for 'objc.options.deprecation_warning': %R",
                             newVal);
                return -1;
            }

            text++;

            minor = strtoul(text, &text, 10);
            if (minor >= 100 || ((minor == 0 || minor == ULONG_MAX) && errno != 0)) {
                PyErr_Format(PyExc_ValueError,
                             "Invalid version for 'objc.options.deprecation_warning': %R",
                             newVal);
                return -1;
            }
            if (*text != '\0') {
                PyErr_Format(PyExc_ValueError,
                             "Invalid version for 'objc.options.deprecation_warning': %R",
                             newVal);
                return -1;
            }
        }

        PyObjC_DeprecationVersion = (int)(major * 100 + minor);
        return 0;

    } else {
        PyErr_Format(PyExc_TypeError,
                     "Expecting 'str' value for 'objc.options.deprecation_warnings', got "
                     "instance of '%s'",
                     Py_TYPE(newVal)->tp_name);
        return -1;
    }
}

static PyGetSetDef options_getset[] = {
    /* Public properties */
    GETSET(verbose, "If True the bridge is more verbose"),
    GETSET(use_kvo, "The default value for __useKVO__ for new classes"),
    GETSET(unknown_pointer_raises,
           "If True the bridge raises an exception instead of creating an ObjCPointer"),
    GETSET(structs_indexable, "If True wrappers for C structs can be used as a sequence"),
    GETSET(structs_writable, "If True wrappers for C structs can be modified"),

    /* Private properties */
    GETSET(_nscoding_encoder, "Private helper function for NSCoding support"),
    GETSET(_nscoding_decoder, "Private helper function for NSCoding support"),
    GETSET(_mapping_count, "Private counter for noticing metadata updates"),
    GETSET(_copy, "Private helper function for copy support"),
    GETSET(_class_extender, "Private helper function for enriching class APIs"),
    GETSET(_make_bundleForClass, "Private helper function for enriching class APIs"),
    GETSET(_nsnumber_wrapper, "Private type used for proxying NSNumber instances"),
    GETSET(_callable_doc, "Private helper function for generating __doc__ for selectors"),
    GETSET(_mapping_types,
           "Private list of types that proxied as instances of NSMutableDictionary"),
    GETSET(_sequence_types,
           "Private list of types that proxied as instances of NSMutableArray"),
    GETSET(_set_types, "Private list of types that proxied as instances of NSMutableSet"),
    GETSET(_date_types, "Private list of types that proxied as instances of NSDate"),
    GETSET(_path_types, "Private list of types that proxied as instances of NSURL"),
    GETSET(_datetime_date_type, "Prive config for datetime.date"),
    GETSET(_datetime_datetime_type, "Prive config for datetime.datetime"),
    GETSET(_callable_signature,
           "Private helper function for generating __signature__ for selectors"),
    GETSET(_getKey, "Private helper used for KeyValueCoding support"),
    GETSET(_setKey, "Private helper used for KeyValueCoding support"),
    GETSET(_getKeyPath, "Private helper used for KeyValueCoding support"),
    GETSET(_setKeyPath, "Private helper used for KeyValueCoding support"),
    GETSET(_transformAttribute,
           "Private helper used for transforming attributes for Objective-C classes"),
    GETSET(_processClassDict,
           "Private helper used for splitting a class dict into parts"),
    GETSET(_setDunderNew,
           "Private helper used for setting __new__ of a new Python subclass"),
    GETSET(_genericNewClass,
           "Class of the generic __new__ implementation"),
    GETSET(_ArrayType,
           "set to array.ArrayType"),
    GETSET(_deepcopy,
           "set to copy.deepcopy"),
    GETSET(_socket_error,
           "set to socket.error"),
    GETSET(_socket_gaierror,
           "set to socket.gaierror"),
    GETSET(_c_void_p,
           "set to ctypes.c_void_p"),
    {
        .name = "deprecation_warnings",
        .get  = deprecation_warnings_get,
        .set  = deprecation_warnings_set,
        .doc  = "If not '0.0.0' give deprecation warnings for the given SDK version",
    },
    {
        .name = "_bundle_hack_used",
        .get  = bundle_hack_get,
        .doc  = "[R/O] True iff OC_BundleHack is used on this system",
    },

    {0, 0, 0, 0, 0} /* Sentinel */
};


/*
 * Helper for calling 'options._nscoder_encoder'.
 *
 * GIL must be held when calling.
 */
int
PyObjC_encodeWithCoder(PyObject* pyObject, NSCoder* coder)
{
    PyObject* encoder;
    LOCK(PyObjC_Encoder);
    encoder = PyObjC_Encoder;
    Py_INCREF(encoder);
    UNLOCK(PyObjC_Encoder);

    if (encoder != Py_None) {
            PyObject* cdr = id_to_python(coder);
            if (cdr == NULL) {            // LCOV_BR_EXCL_LINE
                return -1; // LCOV_EXCL_LINE
            }

            PyObject* args[3] = {NULL, pyObject, cdr};

            PyObject* r = PyObject_Vectorcall(encoder, args + 1,
                                              2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
            Py_DECREF(cdr);
            Py_XDECREF(r);
            Py_DECREF(encoder);

            return r == NULL?-1:0;
    } else {
        PyErr_SetString(PyExc_ValueError, "encoding Python objects is not supported");
        Py_DECREF(encoder);
        return -1;
    }
}

/*
 * Helper for calling 'options._nscoder_decoder'.
 *
 * GIL must be held when calling.
 */
PyObject* _Nullable  PyObjC_decodeWithCoder(NSCoder* coder, id self)
{
    PyObject* decoder;

    LOCK(PyObjC_Decoder);
    decoder = PyObjC_Decoder;
    Py_INCREF(decoder);
    UNLOCK(PyObjC_Decoder);

    if (decoder != Py_None) {
        PyObject* cdr = id_to_python(coder);
        if (cdr == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(decoder);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyObject* self_as_python = PyObjCObject_New(self, 0, YES);
        if (self_as_python == NULL) {   // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(cdr);
            Py_DECREF(decoder);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyObject* setvalue_method = PyObject_GetAttr(self_as_python, PyObjCNM_pyobjcSetValue_);
        Py_CLEAR(self_as_python);
        if (setvalue_method == NULL) { // LCOV_BR_EXCL_LINE
            /* Cannot fail with the classes we use this function in */
            // LCOV_EXCL_START
            Py_DECREF(cdr);
            Py_DECREF(decoder);
            return NULL;
            // LCOV_EXCL_STOP
        }

        PyObject* args[3] = {NULL, cdr, setvalue_method};

        PyObject* result = PyObject_Vectorcall(decoder, args + 1,
                               2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);

        Py_DECREF(cdr);
        Py_DECREF(decoder);
        Py_DECREF(setvalue_method);

        return result;

    } else {
        Py_DECREF(decoder);
        PyErr_SetString(PyExc_ValueError, "decoding Python objects is not supported");
        return NULL;
    }
}

PyObject* _Nullable PyObjC_Copy(PyObject* arg)
{
    PyObject* copy;

    LOCK(PyObjC_CopyFunc);
    copy = PyObjC_CopyFunc;
    Py_INCREF(copy);
    UNLOCK(PyObjC_CopyFunc);

    if (copy != Py_None) {
        PyObject* args[2] = {NULL, arg};

        PyObject* result = PyObject_Vectorcall(copy, args + 1,
                                   1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        Py_DECREF(copy);
        return result;
    } else {
        Py_DECREF(copy);

        PyErr_SetString(PyExc_ValueError, "cannot copy Python objects");
        return NULL;
    }
}

int PyObjC_GetKey(PyObject* object, id key, id* value)
{
    PyObject* func;

    LOCK(PyObjC_getKey);
    func = PyObjC_getKey;
    Py_INCREF(func);
    UNLOCK(PyObjC_getKey);

    if (func == Py_None) {
        Py_DECREF(func);
        PyErr_SetString(PyExc_ValueError, "helper function for getKey not set");
        return -1;
    }

    PyObject* keyName = id_to_python(key);
    if (keyName == NULL) { //LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* args[3] = {NULL, object, keyName};

    PyObject* val = PyObject_Vectorcall(func, args + 1,
                              2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(keyName);
    Py_DECREF(func);

    if (val == NULL) {
        return -1;
    }

    int result = depythonify_c_value(@encode(id), val, value);
    Py_DECREF(val);
    return result;
}

int PyObjC_GetKeyPath(PyObject* object, id keypath, id* value)
{
    PyObject* func;

    LOCK(PyObjC_getKeyPath);
    func = PyObjC_getKeyPath;
    Py_INCREF(func);
    UNLOCK(PyObjC_getKeyPath);

    if (func == Py_None) {
        Py_DECREF(func);
        PyErr_SetString(PyExc_ValueError, "helper function for getKeyPath not set");
        return -1;
    }

    PyObject* keyName = id_to_python(keypath);
    if (keyName == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* args[3] = {NULL, object, keyName};

    PyObject* val = PyObject_Vectorcall(func, args + 1,
                              2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(keyName);
    Py_DECREF(func);

    if (val == NULL) {
        return -1;
    }

    int result = depythonify_c_value(@encode(id), val, value);
    Py_DECREF(val);
    return result;
}

int PyObjC_SetKey(PyObject* object, id key, id value)
{
    PyObject* func;

    LOCK(PyObjC_setKey);
    func = PyObjC_setKey;
    Py_INCREF(func);
    UNLOCK(PyObjC_setKey);

    if (func == Py_None) {
        Py_DECREF(func);
        PyErr_SetString(PyExc_ValueError, "helper function for setKey not set");
        return -1;
    }

    PyObject* keyName = id_to_python(key);
    if (keyName == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* pyValue = id_to_python(value);
    if (pyValue == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(keyName);
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* args[4] = {NULL, object, keyName, pyValue};

    PyObject* val = PyObject_Vectorcall(func, args + 1,
                              3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(keyName);
    Py_DECREF(pyValue);
    Py_DECREF(func);

    if (val == NULL) {
        return -1;
    } else {
        Py_DECREF(val);
        return 0;
    }
}


int PyObjC_SetKeyPath(PyObject* object, id keypath, id value)
{
    PyObject* func;

    LOCK(PyObjC_setKeyPath);
    func = PyObjC_setKeyPath;
    Py_INCREF(func);
    UNLOCK(PyObjC_setKeyPath);

    if (func == Py_None) {
        Py_DECREF(func);
        PyErr_SetString(PyExc_ValueError, "helper function for setKeyPath not set");
        return -1;
    }

    PyObject* keyName = id_to_python(keypath);
    if (keyName == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* pyValue = id_to_python(value);
    if (pyValue == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(keyName);
        Py_DECREF(func);
        return -1;
        // LCOV_EXCL_STOP
    }

    PyObject* args[4] = {NULL, object, keyName, pyValue};

    PyObject* val = PyObject_Vectorcall(func, args + 1,
                              3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(keyName);
    Py_DECREF(pyValue);
    Py_DECREF(func);

    if (val == NULL) {
        return -1;
    } else {
        Py_DECREF(val);
        return 0;
    }
}

bool
PyObjC_IsBuiltinDate(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_DateTime_Date_Type);
    type = PyObjC_DateTime_Date_Type;
    Py_INCREF(type);
    UNLOCK(PyObjC_DateTime_Date_Type);

    if (type == Py_None) {
        Py_DECREF(type);
        return false;
    }
    bool result =  ((PyObject*)Py_TYPE(object) == type);
    Py_DECREF(type);
    return result;
}

PyObject* _Nullable PyObjC_DateFromTimestamp(double timestamp)
{
    PyObject* type;

    LOCK(PyObjC_DateTime_Date_Type);
    type = PyObjC_DateTime_Date_Type;
    Py_INCREF(type);
    UNLOCK(PyObjC_DateTime_Date_Type);

    PyObject* args[3] = {
        NULL,
        type,
        PyFloat_FromDouble(timestamp),
    };
    if (args[2] == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(type);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* value = PyObject_VectorcallMethod(PyObjCNM_fromtimestamp, args + 1,
                                      2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_CLEAR(args[2]);
    Py_DECREF(type);
    return value;
}


bool
PyObjC_IsBuiltinDatetime(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_DateTime_DateTime_Type);
    type = PyObjC_DateTime_DateTime_Type;
    Py_INCREF(type);
    UNLOCK(PyObjC_DateTime_DateTime_Type);

    if (type == Py_None) {
        Py_DECREF(type);
        return false;
    }
    bool result =  ((PyObject*)Py_TYPE(object) == type);
    Py_DECREF(type);
    return result;
}

PyObject* _Nullable PyObjC_DatetimeFromTimestamp(double timestamp, id _Nullable c_info)
{
    PyObject* type;
    PyObject* tzinfo = NULL;

    LOCK(PyObjC_DateTime_DateTime_Type);
    type = PyObjC_DateTime_DateTime_Type;
    Py_INCREF(type);
    UNLOCK(PyObjC_DateTime_DateTime_Type);

    if (c_info != nil) {
        tzinfo = id_to_python(c_info);
        if (tzinfo == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(type);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    PyObject* args[4] = {
        NULL,
        type,
        PyFloat_FromDouble(timestamp),
        tzinfo,
    };
    if (args[2] == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(type);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* value = PyObject_VectorcallMethod(PyObjCNM_fromtimestamp, args + 1,
                                      (2 + (tzinfo != NULL)) | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_CLEAR(args[2]);
    Py_DECREF(type);
    Py_CLEAR(tzinfo);
    return value;
}

int PyObjC_IsDictLike(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_DictLikeTypes);
    type = PyObjC_DictLikeTypes;
    Py_INCREF(type);
    UNLOCK(PyObjC_DictLikeTypes);

    if (type == Py_None) {
        Py_DECREF(type);
        return 0;
    }
    int result =  PyObject_IsInstance(object, type);
    Py_DECREF(type);
    return result;
}

int PyObjC_IsListLike(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_ListLikeTypes);
    type = PyObjC_ListLikeTypes;
    Py_INCREF(type);
    UNLOCK(PyObjC_ListLikeTypes);

    if (type == Py_None) {
        Py_DECREF(type);
        return 0;
    }
    int result =  PyObject_IsInstance(object, type);
    Py_DECREF(type);
    return result;
}

int PyObjC_IsSetLike(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_SetLikeTypes);
    type = PyObjC_SetLikeTypes;
    Py_INCREF(type);
    UNLOCK(PyObjC_SetLikeTypes);

    if (type == Py_None) {
        Py_DECREF(type);
        return 0;
    }
    int result =  PyObject_IsInstance(object, type);
    Py_DECREF(type);
    return result;
}

int PyObjC_IsDateLike(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_DateLikeTypes);
    type = PyObjC_DateLikeTypes;
    Py_INCREF(type);
    UNLOCK(PyObjC_DateLikeTypes);

    if (type == Py_None) {
        Py_DECREF(type);
        return 0;
    }
    int result =  PyObject_IsInstance(object, type);
    Py_DECREF(type);
    return result;
}

int PyObjC_IsPathLike(PyObject* object)
{
    PyObject* type;

    LOCK(PyObjC_PathLikeTypes);
    type = PyObjC_PathLikeTypes;
    Py_INCREF(type);
    UNLOCK(PyObjC_PathLikeTypes);

    if (type == Py_None) {
        Py_DECREF(type);
        return 0;
    }
    int result =  PyObject_IsInstance(object, type);
    Py_DECREF(type);
    return result;
}


PyObject* _Nullable PyObjC_GetCallableDocString(PyObject* callable, void* _Nullable closure __attribute__((__unused__)))
{
    PyObject* func;

    LOCK(PyObjC_CallableDocFunction);
    func = PyObjC_CallableDocFunction;
    Py_INCREF(func);
    UNLOCK(PyObjC_CallableDocFunction);

    if (func == Py_None) {
        Py_DECREF(func);
        Py_RETURN_NONE;
    }

    PyObject* args[2] = {NULL, callable};
    PyObject* result = PyObject_Vectorcall(func, args + 1,
                               1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    return result;
}

PyObject* _Nullable PyObjC_GetCallableSignature(PyObject* callable, void* _Nullable closure __attribute__((__unused__)))
{
    PyObject* func;

    LOCK(PyObjC_CallableSignatureFunction);
    func = PyObjC_CallableSignatureFunction;
    Py_INCREF(func);
    UNLOCK(PyObjC_CallableSignatureFunction);

    if (func == Py_None) {
        Py_DECREF(func);
        Py_RETURN_NONE;
    }
    PyObject* args[2] = {NULL, callable};
    PyObject* result = PyObject_Vectorcall(func, args + 1,
                               1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    return result;
}

int PyObjC_CallClassExtender(PyObject* cls)
{
    assert(PyObjCClass_Check(cls));

    LOCK(PyObjC_ClassExtender);
    PyObject* func = PyObjC_ClassExtender;
    Py_INCREF(func);
    UNLOCK(PyObjC_ClassExtender);

    if (func == Py_None) {
        Py_DECREF(func);
        return 0;
    }

    PyObject* dict = PyDict_New();
    if (dict == NULL) { // LCOV_BR_EXCL_LINE
        Py_DECREF(func); // LCOV_EXCL_LINE
        return -1;      // LCOV_EXCL_LINE
    }

    PyObject* args[3] = {NULL, cls, dict};

    PyObject* res = PyObject_Vectorcall(func, args + 1,
                              2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    if (res == NULL) {
        Py_DECREF(dict);
        return -1;
    }
    Py_DECREF(res);

    PyObject*  k = NULL;
    PyObject*  v = NULL;
    Py_ssize_t pos = 0;

    while (PyDict_Next(dict, &pos, &k, &v)) {
        if (PyUnicode_Check(k)) {
            if (PyObjC_is_ascii_string(k, "__dict__")
                || PyObjC_is_ascii_string(k, "__bases__")
                || PyObjC_is_ascii_string(k, "__slots__")
                || PyObjC_is_ascii_string(k, "__mro__")) {

                continue;
            }

            /* k and v are borrowed references, make sure we own
             * a copy during the call to tp_setattro.
             */
            Py_INCREF(k);
            Py_INCREF(v);

#ifdef Py_GIL_DISABLED
            /* free-threading: First check if the attribute is already set
             * to the "new" value, and avoid resetting the attribute to the
             * same value.
             *
             * In python 3.13 and 3.14 there is a race condition in
             * the implementation of updating type slots.
             *
             * That race condition is fixed in 3.15, but that makes updating
             * slots expensive, making it important to avoid spurious updates.
             */
            PyObject* c;
            int r = PyDict_GetItemRef(((PyTypeObject*)cls)->tp_dict, k, &c);
            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(k);
                Py_CLEAR(v);
                Py_CLEAR(dict);
                return -1;
                // LCOV_EXCL_STOP
            }

            if (c == NULL) {
                r = 0;
            } else {
                r = PyObject_RichCompareBool(v, c, Py_EQ);
            }
            switch (r) {
            case -1:
                Py_CLEAR(k);
                Py_CLEAR(v);
                Py_CLEAR(dict);
                return -1;
            case 0:
#endif
                if (PyType_Type.tp_setattro(cls, k, v) == -1) {
                    PyErr_Clear();
                }
#ifdef Py_GIL_DISABLED
            /* case 1: */
                /* pass */
            }
            Py_CLEAR(c);
#endif
            Py_CLEAR(k);
            Py_CLEAR(v);

        } else {
            /* 'cls' is known to be an PyObjCClass instance, hence the tp_dict
             * slot is usable directly.
             */
            if (PyDict_SetItem(((PyTypeObject*)cls)->tp_dict, k, v) == -1) { // LCOV_BR_EXCL_LINE
                PyErr_Clear(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
        }
    }
    Py_DECREF(dict);
    return 0;
}

void PyObjCErr_SetGAIError(int error)
{
    PyObject* type;

    if (error == EAI_SYSTEM) { // LCOV_BR_EXCL_LINE
        /* This can happen, but haven't found a way to trigger
         * this in testing.
         */
        // LCOV_EXCL_START
        LOCK(PyObjC_socket_error);
        type = PyObjC_socket_error;
        Py_INCREF(type);
        UNLOCK(PyObjC_socket_error);
        PyErr_SetFromErrno(type);
        Py_DECREF(type);
        return;
        // LCOV_EXCL_STOP
    }

    LOCK(PyObjC_socket_gaierror);
    type = PyObjC_socket_gaierror;
    Py_INCREF(type);
    UNLOCK(PyObjC_socket_gaierror);

    PyObject* v = Py_BuildValue("is", error, gai_strerror(error));
    if (v != NULL) { // LCOV_BR_EXCL_LINE
        PyErr_SetObject(type, v);
        Py_DECREF(v);
    }
    Py_DECREF(type);
}

PyObject* _Nullable PyObjCErr_SetSocketError(const char* message)
{
    PyObject* type;
    LOCK(PyObjC_socket_error);
    type = PyObjC_socket_error;
    Py_INCREF(type);
    UNLOCK(PyObjC_socket_error);

    PyErr_SetString(type, message);
    Py_DECREF(type);
    return NULL;
}



/*
 * Returns NULL without setting an exception when
 * the option is not set.
 */
PyObject* _Nullable PyObjC_GetBundleForClassMethod(void)
{
    LOCK(PyObjC_MakeBundleForClass);
    PyObject* func = PyObjC_MakeBundleForClass;
    Py_INCREF(func);
    UNLOCK(PyObjC_MakeBundleForClass);

    if (func == Py_None) {
        Py_DECREF(func);
        return NULL;
    }

    PyObject* args[1] = {NULL};

    PyObject* m = PyObject_Vectorcall(func, args + 1,
                                  0 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);

    Py_DECREF(func);
    if (m == NULL) {
        return NULL;
    }

    if (!PyObjCPythonSelector_Check(m)) {
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

PyObject* _Nullable PyObjC_CreateNSNumberProxy(NSNumber* value)
{
    PyObject* rval = PyObjCObject_New(value, PyObjCObject_kDEFAULT, YES);
    if (rval == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    LOCK(PyObjC_NSNumberWrapper);
    PyObject* func = PyObjC_NSNumberWrapper;
    Py_INCREF(func);
    UNLOCK(PyObjC_NSNumberWrapper);

    if (func == Py_None) {
        Py_DECREF(func);
        return rval;
    }


    PyObject* args[2] = {NULL, rval};
    rval              = PyObject_Vectorcall(PyObjC_NSNumberWrapper, args + 1,
                                                1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    Py_DECREF(args[1]);

    return rval;
}

PyObject* _Nullable PyObjC_TransformAttribute(PyObject* name, PyObject* value,
                                              PyObject* class_object, PyObject* protocols)
{
    LOCK(PyObjC_transformAttribute);
    PyObject* func = PyObjC_transformAttribute;
    Py_INCREF(func);
    UNLOCK(PyObjC_transformAttribute);

    if (func == Py_None) {
        Py_DECREF(func);
        Py_INCREF(value);
        return value;
    }

    PyObject* args[5] = {NULL, name, value, class_object, protocols};
    PyObject* result = PyObject_Vectorcall(PyObjC_transformAttribute, args + 1,
                               4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    return result;
}

int PyObjC_SetDunderNew(PyObject* value)
{
    LOCK(PyObjC_setDunderNew);
    PyObject* func = PyObjC_setDunderNew;
    Py_INCREF(func);
    UNLOCK(PyObjC_setDunderNew);

    if (func == Py_None) {
        Py_DECREF(func);
        return 0;
    }

    PyObject* args[2] = {NULL, value};

    PyObject* rv = PyObject_Vectorcall(func, args + 1,
                                  1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    if (rv == NULL) {
        return -1;
    }
    Py_DECREF(rv);
    return 0;
}

int PyObjC_IsGenericNew(PyObject* value)
{
    LOCK(PyObjC_genericNewClass);
    PyObject* type = PyObjC_genericNewClass;
    Py_INCREF(type);
    UNLOCK(PyObjC_genericNewClass);

    int r = PyObject_TypeCheck(value, (PyTypeObject*)type);
    Py_DECREF(type);
    return r;
}

int PyObjC_ArrayTypeCheck(PyObject* value)
{
    LOCK(PyObjC_genericNewClass);
    PyObject* type = PyObjC_ArrayType;
    Py_INCREF(type);
    UNLOCK(PyObjC_genericNewClass);

    if (type == Py_None) {
        return 0;
    }

    int r = PyObject_TypeCheck(value, (PyTypeObject*)type);
    Py_DECREF(type);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }
    return r;
}

PyObject* _Nullable PyObjC_MakeCVoidP(void* ptr)
{
    PyObject* type;

    LOCK(PyObjC_c_void_p);
    type = PyObjC_c_void_p;
    Py_INCREF(type);
    UNLOCK(PyObjC_c_void_p);

    PyObject* pyptr = PyLong_FromVoidPtr(ptr);
    if (pyptr == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }
    PyObject* args[2] = {NULL, pyptr};
    PyObject* res =
        PyObject_Vectorcall(type, args + 1, 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(pyptr);
    Py_DECREF(type);
    return res;
}

PyObject* _Nullable PyObjC_deepcopy(PyObject* value, PyObject* _Nullable memo)
{
    PyObject* func;
    LOCK(PyObjC_deepcopyFunc);
    func = PyObjC_deepcopyFunc;
    Py_INCREF(func);
    UNLOCK(PyObjC_deepcopyFunc);

    if (func == Py_None) {
        PyErr_SetString(PyObjCExc_Error, "options._deepcopy is not set");
        Py_DECREF(func);
        return NULL;
    }

    PyObject* args[3] = {NULL, value, memo};
    PyObject* result       = PyObject_Vectorcall(
            func, args + 1, (memo?2:1) | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    return result;
}

extern PyObject* _Nullable PyObjC_ProcessClassDict(const char* name, PyObject* class_dict,
                                                   PyObject* meta_dict, PyObject* py_superclass,
                                                   PyObject* protocols, PyObject* hiddenSelectors,
                                                   PyObject* hiddenClassSelectors)
{
    LOCK(PyObjC_processClassDict);
    PyObject* func = PyObjC_processClassDict;
    Py_INCREF(func);
    UNLOCK(PyObjC_processClassDict);

    if (func == Py_None) {
        Py_DECREF(func);
        PyErr_SetString(
            PyObjCExc_InternalError,
            "Cannot create class because 'objc.options._processClassDict' is not set");
        return NULL;
    }

    PyObject* py_name = PyUnicode_FromString(name);
    if (py_name == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(func);
        return NULL;
        // LCOV_EXCL_STOP
    }

    assert(!PyErr_Occurred());
    PyObject* args[] = {NULL,      py_name, class_dict,      meta_dict,           py_superclass,
                        protocols, hiddenSelectors, hiddenClassSelectors};
    PyObject* rv     = PyObject_Vectorcall(func, args + 1,
                                           7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(func);
    Py_DECREF(py_name);

    assert(rv == NULL || !PyErr_Occurred());

    return rv;
}


#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable options_new(PyTypeObject* tp __attribute__((__unused__)),
                                       PyObject* _Nullable args
                                       __attribute__((__unused__)),
                                       PyObject* _Nullable kwds
                                       __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc._OptionsType' instances");
    return NULL;
}
#endif

static PyObject* _Nullable options_dont_call(PyObject* self __attribute__((__unused__)),
                                             PyObject* _Nullable args
                                             __attribute__((__unused__)),
                                             PyObject* _Nullable kwds
                                             __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "Cannot call this method");
    return NULL;
}

static PyMethodDef options_methods[] = {{
                                            .ml_name  = "__copy__",
                                            .ml_meth  = (PyCFunction)options_dont_call,
                                            .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                        },
                                        {
                                            .ml_name  = "__reduce__",
                                            .ml_meth  = (PyCFunction)options_dont_call,
                                            .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                        },
                                        {
                                            .ml_name = NULL /* SENTINEL */
                                        }};

static PyType_Slot options_slots[] = {
    {.slot = Py_tp_methods, .pfunc = (void*)&options_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&options_getset},
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&options_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec options_spec = {
    .name      = "objc._OptionsType",
    .basicsize = sizeof(struct options),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = options_slots,
};

int
PyObjC_SetupOptions(PyObject* m)
{
    PyObjCOptions_Type = PyType_FromSpec(&options_spec);
    if (PyObjCOptions_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                    // LCOV_EXCL_LINE
    }

    PyObject* o =
        (PyObject*)PyObject_New(struct object, (PyTypeObject*)PyObjCOptions_Type);
    if (o == NULL) { // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE
    }

#   define INIT(VAR) do { VAR = Py_None; Py_INCREF(Py_None); } while(0)
    INIT(PyObjC_Encoder);
    INIT(PyObjC_Decoder);
    INIT(PyObjC_CopyFunc);
    INIT(PyObjC_ClassExtender);
    INIT(PyObjC_MakeBundleForClass);
    INIT(PyObjC_NSNumberWrapper);
    INIT(PyObjC_CallableDocFunction);
    INIT(PyObjC_CallableSignatureFunction);
    INIT(PyObjC_DateTime_Date_Type);
    INIT(PyObjC_DateTime_DateTime_Type);
    INIT(PyObjC_getKey);
    INIT(PyObjC_setKey);
    INIT(PyObjC_getKeyPath);
    INIT(PyObjC_setKeyPath);
    INIT(PyObjC_transformAttribute);
    INIT(PyObjC_processClassDict);
    INIT(PyObjC_setDunderNew);
    INIT(PyObjC_genericNewClass);
    INIT(PyObjC_genericNewClass);
    INIT(PyObjC_ArrayType);
    INIT(PyObjC_deepcopyFunc);
    INIT(PyObjC_socket_error);
    INIT(PyObjC_socket_gaierror);
    INIT(PyObjC_c_void_p);
#undef INIT

    // LCOV_BR_EXCL_START
    PyObjC_DictLikeTypes = PyTuple_New(0);
    if (PyObjC_DictLikeTypes == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    PyObjC_ListLikeTypes = PyTuple_New(0);
    if (PyObjC_ListLikeTypes == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    PyObjC_SetLikeTypes = PyTuple_New(0);
    if (PyObjC_SetLikeTypes == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    PyObjC_DateLikeTypes = PyTuple_New(0);
    if (PyObjC_DateLikeTypes == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    PyObjC_PathLikeTypes = PyTuple_New(0);
    if (PyObjC_DictLikeTypes == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    return PyModule_AddObject(m, "options", o);
}

NS_ASSUME_NONNULL_END
