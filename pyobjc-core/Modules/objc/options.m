/*
 * This file defines a singleton object for getting/setting options/properties
 * for the core bridge.
 *
 * There are both public and private options/properties. The private ones have
 * names starting with an underscore and those can be changed without concern
 * for backward compatibility between releases.
 */
#include "pyobjc.h"

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

#if Py_GIL_DISABLED
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
    PyObjC_ATOMIC int VAR = DFLT;                                                                      \
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
    PyObjC_ATOMIC BOOL VAR = DFLT;                                                                     \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        PyObject* result;                                                                \
        result = PyBool_FromLong(VAR);                                                   \
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
        VAR = PyObject_IsTrue(newVal) ? YES : NO;                                        \
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
        if (VAR != NULL) {                                                               \
            Py_INCREF(VAR);                                                              \
            UNLOCK(VAR);                                                                 \
            return VAR;                                                                  \
                                                                                         \
        } else {                                                                         \
            Py_INCREF(Py_None);                                                          \
            UNLOCK(VAR);                                                                 \
            return Py_None;                                                              \
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
        if (VAR != NULL) {                                                               \
            Py_INCREF(VAR);                                                              \
            UNLOCK(VAR);                                                                 \
            return VAR;                                                                  \
                                                                                         \
        } else {                                                                         \
            Py_INCREF(Py_None);                                                          \
            UNLOCK(VAR);                                                                 \
            return Py_None;                                                              \
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
OBJECT_PROP(_class_extender, PyObjC_ClassExtender)
OBJECT_PROP(_make_bundleForClass, PyObjC_MakeBundleForClass)
OBJECT_PROP(_nsnumber_wrapper, PyObjC_NSNumberWrapper)
OBJECT_PROP(_callable_doc, PyObjC_CallableDocFunction)
OBJECT_PROP(_callable_signature, PyObjC_CallableSignatureFunction)
OBJECT_PROP(_mapping_types, PyObjC_DictLikeTypes)
OBJECT_PROP(_sequence_types, PyObjC_ListLikeTypes)
OBJECT_PROP(_set_types, PyObjC_SetLikeTypes)
OBJECT_PROP(_date_types, PyObjC_DateLikeTypes)
OBJECT_PROP(_path_types, PyObjC_PathLikeTypes)
OBJECT_PROP(_datetime_date_type, PyObjC_DateTime_Date_Type)
OBJECT_PROP(_datetime_datetime_type, PyObjC_DateTime_DateTime_Type)
OBJECT_PROP_STATIC(_getKey, PyObjC_getKey)
OBJECT_PROP_STATIC(_setKey, PyObjC_setKey)
OBJECT_PROP_STATIC(_getKeyPath, PyObjC_getKeyPath)
OBJECT_PROP_STATIC(_setKeyPath, PyObjC_setKeyPath)
OBJECT_PROP(_transformAttribute, PyObjC_transformAttribute)
OBJECT_PROP(_processClassDict, PyObjC_processClassDict)
OBJECT_PROP(_setDunderNew, PyObjC_setDunderNew)
OBJECT_PROP(_genericNewClass, PyObjC_genericNewClass)

static PyObject*
bundle_hack_get(PyObject* s __attribute__((__unused__)),
                void*     c __attribute__((__unused__)))
{
    return PyBool_FromLong([OC_NSBundleHack bundleHackUsed]);
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
        if (text == NULL) {
            return -1;
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
        if (cdr == NULL) {
            Py_DECREF(decoder);
            return NULL;
        }

        PyObject* self_as_python = PyObjCObject_New(self, 0, YES);
        if (self_as_python == NULL) {   // LCOV_BR_EXCL_LINE
            Py_DECREF(cdr);
            Py_DECREF(decoder);
            return NULL;
        }

        PyObject* setvalue_method = PyObject_GetAttr(self_as_python, PyObjCNM_pyobjcSetValue_);
        Py_CLEAR(self_as_python);
        if (setvalue_method == NULL) {
            Py_DECREF(cdr);
            Py_DECREF(decoder);
            return NULL;
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
    if (keyName == NULL) {
        Py_DECREF(func);
        return -1;
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
    if (keyName == NULL) {
        Py_DECREF(func);
        return -1;
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
    if (keyName == NULL) {
        Py_DECREF(func);
        return -1;
    }

    PyObject* pyValue = id_to_python(value);
    if (pyValue == NULL) {
        Py_DECREF(keyName);
        Py_DECREF(func);
        return -1;
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
    if (keyName == NULL) {
        Py_DECREF(func);
        return -1;
    }

    PyObject* pyValue = id_to_python(value);
    if (pyValue == NULL) {
        Py_DECREF(keyName);
        Py_DECREF(func);
        return -1;
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
    INIT(PyObjC_DictLikeTypes);
    INIT(PyObjC_ListLikeTypes);
    INIT(PyObjC_SetLikeTypes);
    INIT(PyObjC_DateLikeTypes);
    INIT(PyObjC_PathLikeTypes);
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
#undef INIT

    return PyModule_AddObject(m, "options", o);
}

NS_ASSUME_NONNULL_END
