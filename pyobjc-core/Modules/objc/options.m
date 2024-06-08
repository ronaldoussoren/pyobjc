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

#define _STR(v) #v
#define STR(v) _STR(v)

#define SSIZE_T_PROP(NAME, VAR, DFLT)                                                    \
    Py_ssize_t VAR = DFLT;                                                               \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        return Py_BuildValue("n", VAR);                                                  \
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
        if (!PyArg_Parse(newVal, "n", &VAR)) {                                           \
            return -1;                                                                   \
        }                                                                                \
        return 0;                                                                        \
    }

#define INT_PROP(NAME, VAR, DFLT)                                                        \
    int VAR = DFLT;                                                                      \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        return Py_BuildValue("i", VAR);                                                  \
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
        if (!PyArg_Parse(newVal, "i", &VAR)) {                                           \
            return -1;                                                                   \
        }                                                                                \
        return 0;                                                                        \
    }

#define BOOL_PROP(NAME, VAR, DFLT)                                                       \
    BOOL VAR = DFLT;                                                                     \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        return PyBool_FromLong(VAR);                                                     \
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

/* XXX: Either set the default from PyObjC_SetupOptions, or
 *      make sure that setting the value of 'None' sets the global
 *      variable to NULL (and check users!)
 */
#define OBJECT_PROP(NAME, VAR, DFLT)                                                     \
    PyObject* VAR = DFLT;                                                                \
                                                                                         \
    static PyObject* NAME##_get(PyObject* s __attribute__((__unused__)),                 \
                                void*     c __attribute__((__unused__)))                 \
    {                                                                                    \
        if (VAR != NULL) {                                                               \
            Py_INCREF(VAR);                                                              \
            return VAR;                                                                  \
                                                                                         \
        } else {                                                                         \
            Py_INCREF(Py_None);                                                          \
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
        SET_FIELD_INCREF(VAR, newVal);                                                   \
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

INT_PROP(_nscoding_version, PyObjC_NSCoding_Version, 0)
SSIZE_T_PROP(_mapping_count, PyObjC_MappingCount, 0)

/* Private properties */
OBJECT_PROP(_nscoding_encoder, PyObjC_Encoder, NULL)
OBJECT_PROP(_nscoding_decoder, PyObjC_Decoder, NULL)
OBJECT_PROP(_copy, PyObjC_CopyFunc, NULL)
OBJECT_PROP(_class_extender, PyObjC_ClassExtender, NULL)
OBJECT_PROP(_make_bundleForClass, PyObjC_MakeBundleForClass, NULL)
OBJECT_PROP(_nsnumber_wrapper, PyObjC_NSNumberWrapper, NULL)
OBJECT_PROP(_callable_doc, PyObjC_CallableDocFunction, NULL)
OBJECT_PROP(_callable_signature, PyObjC_CallableSignatureFunction, NULL)
OBJECT_PROP(_mapping_types, PyObjC_DictLikeTypes, NULL)
OBJECT_PROP(_sequence_types, PyObjC_ListLikeTypes, NULL)
OBJECT_PROP(_set_types, PyObjC_SetLikeTypes, NULL)
OBJECT_PROP(_date_types, PyObjC_DateLikeTypes, NULL)
OBJECT_PROP(_path_types, PyObjC_PathLikeTypes, NULL)
OBJECT_PROP(_datetime_date_type, PyObjC_DateTime_Date_Type, NULL)
OBJECT_PROP(_datetime_datetime_type, PyObjC_DateTime_DateTime_Type, NULL)
OBJECT_PROP(_getKey, PyObjC_getKey, NULL)
OBJECT_PROP(_setKey, PyObjC_setKey, NULL)
OBJECT_PROP(_getKeyPath, PyObjC_getKeyPath, NULL)
OBJECT_PROP(_setKeyPath, PyObjC_setKeyPath, NULL)
OBJECT_PROP(_transformAttribute, PyObjC_transformAttribute, NULL)
OBJECT_PROP(_processClassDict, PyObjC_processClassDict, NULL)
OBJECT_PROP(_setDunderNew, PyObjC_setDunderNew, NULL)
OBJECT_PROP(_genericNewClass, PyObjC_genericNewClass, NULL)

static PyObject*
bundle_hack_get(PyObject* s __attribute__((__unused__)),
                void*     c __attribute__((__unused__)))
{
    return PyBool_FromLong([OC_NSBundleHack bundleHackUsed]);
}

int PyObjC_DeprecationVersion = 0;

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
    GETSET(_nscoding_version, "Private version number for NSCoding support"),
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

    return PyModule_AddObject(m, "options", o);
}

NS_ASSUME_NONNULL_END
