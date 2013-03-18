/*
 * This file defines a singleton object for getting/setting options/properties
 * for the core bridge.
 *
 * There are both public and private options/properties. The private ones have
 * names starting with an underscore and those can be changed without concern
 * for backward compatibility between releases.
 */
#include "pyobjc.h"

/*
 * Empty object definition for the options object, this
 * is a singleton whose actual value is stored as a number
 * of global variables to make the options easier to use
 * from C.
 */
struct options {
    PyObject_HEAD;
};

#define _STR(v) #v
#define STR(v) _STR(v)


#define BOOL_PROP(NAME, VAR, DFLT)                                          \
    BOOL VAR = DFLT;                                                        \
                                                                            \
    static PyObject* NAME ## _get(PyObject* s __attribute__((__unused__)),  \
            void *c __attribute__((__unused__)))                            \
    {                                                                       \
        return PyBool_FromLong(VAR);                                        \
    }                                                                       \
                                                                            \
    static int NAME ## _set(PyObject* s __attribute__((__unused__)),        \
            PyObject* newVal, void* c __attribute__((__unused__)))          \
    {                                                                       \
        VAR = PyObject_IsTrue(newVal) ? YES : NO;                           \
        return 0;                                                           \
    }

#define OBJECT_PROP(NAME, VAR, DFLT)                                        \
    PyObject* VAR = DFLT;                                                   \
                                                                            \
    static PyObject* NAME ## _get(PyObject* s __attribute__((__unused__)),  \
            void *c __attribute__((__unused__)))                            \
    {                                                                       \
        if (VAR != NULL) {                                                  \
            Py_INCREF(VAR);                                                 \
            return VAR;                                                     \
                                                                            \
        } else {                                                            \
            Py_INCREF(Py_None);                                             \
            return Py_None;                                                 \
        }                                                                   \
    }                                                                       \
                                                                            \
    static int NAME ## _set(PyObject* s __attribute__((__unused__)),        \
            PyObject* newVal, void* c __attribute__((__unused__)))          \
    {                                                                       \
        SET_FIELD_INCREF(VAR, newVal);                                      \
        return 0;                                                           \
    }


#define GETSET(NAME, DOC)      \
    {                               \
        STR(NAME),                  \
        NAME ## _get,               \
        NAME ## _set,               \
        DOC,                        \
        0                           \
    }


/* Public properties */
BOOL_PROP(verbose, PyObjC_Verbose, NO)
BOOL_PROP(use_kvo, PyObjC_UseKVO, YES)
BOOL_PROP(unknown_pointer_raises, PyObjCPointer_RaiseException, YES)

#if PY_MAJOR_VERSION == 2
BOOL_PROP(strbridge_enabled, PyObjC_StrBridgeEnabled, YES)
#endif /* PY_MAJOR_VERSION == 2 */

int PyObjC_NSCoding_Version = 0;

static PyObject* _nscoding_version_get(PyObject* s __attribute__((__unused__)),
        void *c __attribute__((__unused__)))
{
    return PyInt_FromLong(PyObjC_NSCoding_Version);
}

static int _nscoding_version_set(PyObject* s __attribute__((__unused__)),
        PyObject* newVal, void* c __attribute__((__unused__)))
{
    if (PyArg_Parse(newVal, "i", &PyObjC_NSCoding_Version) < 0) {
        return -1;
    }

    return 0;
}


/* Private properties */
OBJECT_PROP(_nscoding_encoder, PyObjC_Encoder, NULL)
OBJECT_PROP(_nscoding_decoder, PyObjC_Decoder, NULL)
OBJECT_PROP(_copy, PyObjC_CopyFunc, NULL)
OBJECT_PROP(_class_extender, PyObjC_ClassExtender, NULL)
OBJECT_PROP(_nsnumber_wrapper, PyObjC_NSNumberWrapper, NULL)
OBJECT_PROP(_callable_doc, PyObjC_CallableDocFunction, NULL)
#if PY_VERSION_HEX >= 0x03030000
OBJECT_PROP(_callable_signature, PyObjC_CallableSignatureFunction, NULL)
#endif
OBJECT_PROP(_mapping_types, PyObjC_DictLikeTypes, NULL)
OBJECT_PROP(_sequence_types, PyObjC_ListLikeTypes, NULL)
OBJECT_PROP(_set_types, PyObjC_SetLikeTypes, NULL)
OBJECT_PROP(_date_types, PyObjC_DateLikeTypes, NULL)

static PyGetSetDef object_getset[] = {
    /* Public properties */
    GETSET(verbose,                 "If True the bridge is more verbose"),
    GETSET(use_kvo,                 "The default value for __useKVO__ for new classes"),
    GETSET(unknown_pointer_raises,  "If True the bridge raises an exception instead of creating an ObjCPointer"),

#if PY_MAJOR_VERSION == 2
    GETSET(strbridge_enabled,       "If True the transparent str() bridge is enabled"),
#endif /* PY_MAJOR_VERSION == 2 */

    /* Private properties */
    GETSET(_nscoding_version,       "Private version number for NSCoding support"),
    GETSET(_nscoding_encoder,       "Private helper function for NSCoding support"),
    GETSET(_nscoding_decoder,       "Private helper function for NSCoding support"),
    GETSET(_copy,                   "Private helper function for copy support"),
    GETSET(_class_extender,         "Private helper function for enriching class APIs"),
    GETSET(_nsnumber_wrapper,       "Private type used for proxying NSNumber instances"),
    GETSET(_callable_doc,           "Private helper function for generating __doc__ for selectors"),
    GETSET(_mapping_types,          "Private list of types that proxied as instances of NSMutableDictionary"),
    GETSET(_sequence_types,         "Private list of types that proxied as instances of NSMutableArray"),
    GETSET(_set_types,              "Private list of types that proxied as instances of NSMutableSet"),
    GETSET(_date_types,             "Private list of types that proxied as instances of NSDate"),
#if PY_VERSION_HEX >= 0x03030000
    GETSET(_callable_signature,     "Private helper function for generating __signature__ for selectors"),
#endif /* PY_VERSION_HEX >= 0x03030000 */

    { 0, 0, 0, 0, 0 } /* Sentinel */
};

static PyObject*
object_new(PyTypeObject* tp __attribute__((__unused__)),
            PyObject* args __attribute__((__unused__)),
            PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_ValueError, "Cannot create instances of this type");
    return NULL;
}

static PyObject*
object_dont_call(PyObject* self __attribute__((__unused__)),
            PyObject* args __attribute__((__unused__)),
            PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_ValueError, "Cannot call this method");
    return NULL;
}

static PyMethodDef object_methods[] = {
    {
        "__copy__",
        (PyCFunction)object_dont_call,
        METH_VARARGS|METH_KEYWORDS,
        0,
    },
    {
        "__reduce__",
        (PyCFunction)object_dont_call,
        METH_VARARGS|METH_KEYWORDS,
        0,
    },

    { 0, 0, 0, 0 } /* sentinel */
};

static PyTypeObject PyObjCOptions_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc._OptionsType",
    .tp_basicsize   = sizeof(struct options),
    .tp_itemsize    = 0,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_methods     = object_methods,
    .tp_getset      = object_getset,
    .tp_new         = object_new,
};


int PyObjC_SetupOptions(PyObject* m)
{
    if (PyType_Ready(&PyObjCOptions_Type) < 0) {
        return -1;
    }

    PyObject* o = (PyObject*)PyObject_New(struct object, &PyObjCOptions_Type);
    if (o == NULL) {
        return -1;
    }

    int r = PyModule_AddObject(m, "options", o);
    return r;
}
