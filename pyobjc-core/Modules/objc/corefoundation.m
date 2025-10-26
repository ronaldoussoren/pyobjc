/*
 * This file implements generic support for CoreFoundation types.
 *
 * CF-based proxy types are implemented as subclasses of the proxy for NSCFType,
 * that way CF-based types fit in nicely with the PyObjC machinery (specifically
 * subclass tests keep working).
 *
 * Major assumption:
 * - NSCFType is the ObjC type that all non-toll-free bridged types inherit
 *   from, toll-free bridged types are not subclasses of NSCFType.
 */
#include "pyobjc.h"

#import <CoreFoundation/CoreFoundation.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* gTypeid2class        = NULL;
PyObject*        PyObjC_NSCFTypeClass = NULL;

static PyObject* _Nullable cf_repr(PyObject* self)
{
    if (PyObjCObject_GetFlags(self) & PyObjCObject_kMAGIC_COOKIE) {
        return PyUnicode_FromFormat("<%s CoreFoundation magic instance %p>",
                                    Py_TYPE(self)->tp_name, PyObjCObject_GetObject(self));
    }

    CFStringRef repr = CFCopyDescription(PyObjCObject_GetObject(self));
    if (repr) { // LCOV_BR_EXCL_LINE
        PyObject* result = id_to_python((id)repr);
        CFRelease(repr);
        return result;

    } else {
        // LCOV_EXCL_START
        return PyUnicode_FromFormat("<%s object at %p>", Py_TYPE(self)->tp_name,
                                    PyObjCObject_GetObject(self));
        // LCOV_EXCL_STOP
    }
}

PyObject* _Nullable PyObjC_TryCreateCFProxy(NSObject* value)
{
    PyObject* rval = NULL;

    assert(gTypeid2class != NULL);

    PyObject*     cfid;
    PyTypeObject* tp;
    int           r;

    cfid = PyLong_FromLong(CFGetTypeID((CFTypeRef)value));
    if (cfid == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }
    r = PyDict_GetItemRef(gTypeid2class, cfid, (PyObject**)&tp);
    Py_DECREF(cfid);
    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        return NULL; // LCOV_EXCL_LINE

    case 0:
        return NULL;

    default:
        rval = tp->tp_alloc(tp, 0);
        Py_DECREF(tp);
        if (rval == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;    // LCOV_EXCL_LINE
        }

        ((PyObjCObject*)rval)->objc_object = value;
        ((PyObjCObject*)rval)->flags = PyObjCObject_kDEFAULT | PyObjCObject_kCFOBJECT;
        CFRetain(value);

        return rval;
    }
}

#ifdef PyObjC_ENABLE_CFTYPE_CATEGORY
/* Implementation for: -(PyObject*)__pyobjc_PythonObject__ on NSCFType. We cannot
 * define a category on that type because the class definition isn't public.
 */
static PyObject* _Nullable pyobjc_PythonObject(NSObject* self,
                                               SEL       _sel __attribute__((__unused__)))
{
    PyObject* rval = NULL;

    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) { // LCOV_BR_EXCL_LINE
        rval = PyObjC_TryCreateCFProxy(self);
        if (rval == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;                        // LCOV_EXCL_LINE
        }
        if (rval == NULL) {
            /* There is no wrapper for this type, fall back to
             * the generic behaviour.
             */
            rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        }

        /* rval can be NULL for memory errors and the like, but not
         * in normal circumstances
         */
        if (rval) { // LCOV_BR_EXCL_LINE
            PyObject* actual = PyObjC_RegisterPythonProxy(self, rval);
            Py_DECREF(rval);
            return actual;
        }
    } // LCOV_EXCL_LINE

    /* Currently all code paths that end up calling
     * the __pyobjc_PythonObject__ selector already
     * checked if the proxy exists fore calling the
     * selector.
     */
    return rval; // LCOV_EXCL_LINE
}
#endif

PyObject* _Nullable PyObjCCFType_New(char* name, char* encoding, CFTypeID typeID)
{
    PyObject*          args;
    PyObject*          dict;
    PyObject*          result;
    PyObject*          bases;
    PyObjCClassObject* info;
    int                r;

    if (encoding[0] != _C_ID) {
        if (PyObjCPointerWrapper_RegisterID(name, encoding) == -1) { // LCOV_BR_EXCL_LINE
            return NULL;                                             // LCOV_EXCL_LINE
        }
    }

    if (typeID == 0) { // LCOV_BR_EXCL_LINE
        /* Partially registered type, just wrap as a
         * a plain CFTypeRef
         *
         * XXX: Can we reproduce this in testing?
         */
        // LCOV_EXCL_START
        assert(PyObjC_NSCFTypeClass != NULL);
        Py_INCREF(PyObjC_NSCFTypeClass);
        return PyObjC_NSCFTypeClass;
        // LCOV_EXCL_STOP
    }

    Class cf_class = PyObjCClass_GetClass(PyObjC_NSCFTypeClass);
    if (cf_class == Nil) { // LCOV_BR_EXCL_LINE
        return NULL;       // LCOV_EXCL_LINE
    }

    PyObject* cf = PyLong_FromUnsignedLongLong(typeID);
    if (cf == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;  // LCOV_EXCL_LINE
    }

    r = PyDict_GetItemRef(gTypeid2class, cf, &result);
    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    case 1:
        /* This type is the same as an already registered type,
         * return that type
         */
        Py_DECREF(cf);
        return result;
    }
    /* case 0: */
    dict = PyDict_New();
    if (dict == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* slots = PyTuple_New(0);
    if (slots == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(dict);
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
            dict, PyObjCNM___slots__, slots)
        == -1) {
        // LCOV_EXCL_START
        Py_DECREF(slots);
        Py_DECREF(dict);
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(slots);

    bases = PyTuple_Pack(1, PyObjC_NSCFTypeClass);
    if (bases == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(dict);
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* nm = PyUnicode_FromString(name);
    if (nm == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(bases);
        Py_DECREF(dict);
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }
    args = PyTuple_Pack(3, nm, bases, dict);
    Py_CLEAR(nm);
    Py_CLEAR(bases);
    Py_CLEAR(dict);
    if (args == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    result = PyType_Type.tp_new(&PyObjCClass_Type, args, NULL);
    Py_DECREF(args);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    ((PyTypeObject*)result)->tp_repr = cf_repr;
    ((PyTypeObject*)result)->tp_str  = cf_repr;

    info                = (PyObjCClassObject*)result;
    info->class         = cf_class;
    info->sel_to_py     = NULL;
    info->dictoffset    = 0;
    info->useKVO        = 0;
    info->delmethod     = NULL;
    info->hasPythonImpl = 0;
    info->isCFWrapper   = 1;

    if (PyObject_SetAttrString( // LCOV_BR_EXCL_LINE
            result, "__module__", PyObjCClass_DefaultModule)
        < 0) {
        PyErr_Clear(); // LCOV_EXCL_LINE
    } // LCOV_EXCL_LINE

    if (PyDict_SetItem(gTypeid2class, cf, result) == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        Py_DECREF(cf);
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_DECREF(cf);
    return result;
}

static const char* _Nullable gNames[] = {
    "__NSCFType",
    "NSCFType",
    "___NSCFType",
    NULL,
};

int
PyObjCCFType_Setup(PyObject* module __attribute__((__unused__)))
{
#ifdef PyObjC_ENABLE_CFTYPE_CATEGORY
    static char encodingBuf[128];
#endif
    Class        cls;
    const char** cur;

    gTypeid2class = PyDict_New();
    if (gTypeid2class == NULL) { // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE
    }

#ifdef PyObjC_ENABLE_CFTYPE_CATEGORY
    snprintf(encodingBuf, sizeof(encodingBuf), "%s%c%c", @encode(PyObject*), _C_ID,
             _C_SEL);
#endif

    for (cur = gNames; *cur != NULL; cur++) {
        cls = objc_lookUpClass(*cur);
        if (cls == Nil)
            continue;

#ifdef PyObjC_ENABLE_CFTYPE_CATEGORY
        /* Add a __pyobjc_PythonObject__ method to NSCFType. Can't use a
         * category because the type isn't public.
         */
        if (!class_addMethod(cls, @selector(__pyobjc_PythonObject__), // LCOV_BR_EXCL_LINE
                             (IMP)pyobjc_PythonObject, encodingBuf)) {

            return -1; // LCOV_EXCL_LINE
        }
#endif

        if (PyObjC_NSCFTypeClass == NULL) {
            PyObjC_NSCFTypeClass = PyObjCClass_New(cls);
            if (PyObjC_NSCFTypeClass == NULL) { // LCOV_BR_EXCL_LINE
                return -1;                      // LCOV_EXCL_LINE
            }
        }
#ifndef PyObjC_ENABLE_CFTYPE_CATEGORY
        break;
#endif
    }

    if (PyObjC_NSCFTypeClass == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_RuntimeError, "Cannot locate NSCFType");
        return -1;
        // LCOV_EXCL_STOP
    }

    return 0;
}

/*
 * Create proxy object for a special value of a CFType, that
 * is a value that just a magic cookie and not a valid
 * object. Such objects are sometimes used in CoreFoundation
 * (sadly enough).
 */
PyObject* _Nullable PyObjCCF_NewSpecialFromTypeEncoding(char* typestr, void* datum)
{
    PyObject* v;
    PyObject* typestr_obj = PyUnicode_FromString(typestr);
    if (typestr_obj == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;           // LCOV_EXCL_LINE
    }
    int r = PyDict_GetItemRef(PyObjC_TypeStr2CFTypeID, typestr_obj, &v);
    Py_DECREF(typestr_obj);

    CFTypeID typeid;

    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        return NULL; // LCOV_EXCL_LINE
    case 0:
        PyErr_Format(PyExc_ValueError,
                     "Don't know CF type for typestr '%s', cannot create special wrapper",
                     typestr);
        return NULL;
    default:
        if (depythonify_c_value(@encode(CFTypeID), v, &typeid) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(v);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(v);

        return PyObjCCF_NewSpecialFromTypeID(typeid, datum);
    }
}

/*
 * Create proxy object for a special value of a CFType, that
 * is a value that just a magic cookie and not a valid
 * object. Such objects are sometimes used in CoreFoundation
 * (sadly enough).
 */
PyObject*
PyObjCCF_NewSpecialFromTypeID(CFTypeID typeid, void* datum)
{
    PyObject* rval = NULL;
    int       r;

    assert(gTypeid2class != NULL);

    PyObject*     cfid;
    PyTypeObject* tp;

    cfid = PyLong_FromLong(typeid);
    r    = PyDict_GetItemRef(gTypeid2class, cfid, (PyObject**)&tp);
    Py_DECREF(cfid);
    switch (r) { // LCOV_BR_EXCL_LINE
    case -1:
        return NULL; // LCOV_EXCL_LINE
    case 0:
        return (PyObject*)PyObjCObject_New(
            datum, PyObjCObject_kMAGIC_COOKIE | PyObjCObject_kSHOULD_NOT_RELEASE, NO);
    default:
        rval = tp->tp_alloc(tp, 0);
        Py_DECREF(tp);
        if (rval == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;    // LCOV_EXCL_LINE
        }

        ((PyObjCObject*)rval)->objc_object = datum;
        ((PyObjCObject*)rval)->flags       = PyObjCObject_kDEFAULT
                                       | PyObjCObject_kSHOULD_NOT_RELEASE
                                       | PyObjCObject_kMAGIC_COOKIE;
        return rval;
    }
}

NS_ASSUME_NONNULL_END
