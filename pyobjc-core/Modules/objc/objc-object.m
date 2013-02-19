/*
 * Implementation of objective-C object wrapper
 *
 * NOTE: We're using CFRetain and CFRelease to manage the retaincount of the Objective-C
 * objects because that will do the right thing when Garbage Collection is involved.
 */
#include "pyobjc.h"

#include <stddef.h>
#include <objc/Object.h>

static PyObject*
object_new(
    PyTypeObject*  type __attribute__((__unused__)),
    PyObject* args,
    PyObject* kwds)
{
static char* keywords[] = { "cobject", "c_void_p", NULL };
    PyObject* cobject = NULL;
    PyObject* c_void_p = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OO", keywords, &cobject, &c_void_p)) {
        return NULL;
    }

    if (cobject != NULL && c_void_p != NULL) {
        PyErr_SetString(PyExc_TypeError, "Pass either cobject or c_void_p, but not both");
        return NULL;
    }

    if (cobject != NULL && PyCapsule_CheckExact(cobject)) {
        NSObject* p = PyCapsule_GetPointer(cobject, "objc.__object__");
        if (PyErr_Occurred()) {
            return NULL;
        }

        return PyObjC_IdToPython(p);

    } else if (c_void_p != NULL) {
        NSObject* p;
        PyObject* attrval;

        if (PyLong_Check(c_void_p)
#if PY_MAJOR_VERSION == 2
                || PyInt_Check(c_void_p)
#endif
            ) {
                attrval = c_void_p;
                Py_INCREF(attrval);

        } else {
            attrval = PyObject_GetAttrString(c_void_p, "value");
            if (attrval == NULL) {
                return NULL;
            }
        }

        if (
#if PY_MAJOR_VERSION == 2
            PyInt_Check(attrval) ||
            /* NOTE: PyLong_AsVoidPtr works on Int objects as well */
#endif /* PY_MAJOR_VERSION == 2 */
            PyLong_Check(attrval)
        ) {
            p = PyLong_AsVoidPtr(attrval);
            if (p == NULL && PyErr_Occurred()) {
                Py_DECREF(attrval);
                return NULL;
            }

        } else {
            PyErr_SetString(PyExc_ValueError,
                "c_void_p.value is not an integer");
            return NULL;
        }

        Py_DECREF(attrval);
        return PyObjC_IdToPython(p);

    } else {
        PyErr_SetString(PyExc_TypeError,
            "Use class methods to instantiate new Objective-C objects");
        return NULL;
    }
}

static PyObject*
object_repr(PyObject* _self)
{
    PyObjCObject* self = (PyObjCObject*)_self;
    PyObject* res;

    if (self->flags & PyObjCObject_kMAGIC_COOKIE) {
        return PyText_FromFormat(
            "<%s objective-c magic instance %p>",
            Py_TYPE(self)->tp_name, self->objc_object);
    }

    if ((self->flags & PyObjCObject_kUNINITIALIZED) == 0 && !PyObjCObject_IsClassic(self)) {
        /* Try to call the method 'description', which is the ObjC
         * equivalent of __repr__. If that fails we'll fall back to
         * the default repr.
         * Don't call 'description' for uninitialized objects, that
         * is undefined behaviour and will crash the interpreter sometimes.
         */
        res = PyObject_CallMethod((PyObject*)self, "description", NULL);
        if (res == NULL) {
            PyErr_Clear();
        } else {
            return res;
        }
    }
    return PyText_FromFormat(
        "<%s objective-c instance %p>",
        Py_TYPE(self)->tp_name, self->objc_object);
}

static void
object_del(PyObject* obj __attribute__((__unused__)))
{
    /* Dummy function, we do not want the default implementation */
}

static void
object_dealloc(PyObject* obj)
{
    /*
     * Save exception information, needed because releasing the object
     * might clear or modify the exception state.
     */
    PyObject* ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);

    if (PyObjCObject_IsBlock(obj)) {
        PyObjCMethodSignature* v = PyObjCObject_GetBlock(obj);
        PyObjCObject_SET_BLOCK(obj, NULL);
        Py_XDECREF(v);
    }

    if (PyObjCObject_GetFlags(obj) != PyObjCObject_kDEALLOC_HELPER
            && PyObjCObject_GetObject(obj) != nil) {
        /* Release the proxied object, we don't have to do this when
         * there is no proxied object.
         */
        PyObjC_UnregisterPythonProxy(
            PyObjCObject_GetObject(obj), obj);

        if (PyObjCObject_IsClassic(obj)) {
            /* pass */

        } else if ((((PyObjCObject*)obj)->flags
                & PyObjCObject_kSHOULD_NOT_RELEASE)) {
            /* pass */

        } else if (((PyObjCObject*)obj)->flags
                & PyObjCObject_kUNINITIALIZED) {
            /* Freeing of an uninitialized object, just leak because
             * there is no reliable manner to free such objects.
             *
             * - [obj release] doesn't work because some classes
             *   cause crashes for uninitialized objects
             * - [[obj init] release] also doesn't work because
             *   not all classes implement -init
             * - [obj dealloc] doesn't work for class
             *   clusters like NSArray.
             */
            char buf[256];
            snprintf(buf, sizeof(buf),
                "leaking an uninitialized object of type %s",
                Py_TYPE(obj)->tp_name);
            PyErr_Warn(PyObjCExc_UnInitDeallocWarning, buf);
            ((PyObjCObject*)obj)->objc_object = nil;

        } else {
            PyObjC_DURING
                if (((PyObjCObject*)obj)->flags & PyObjCObject_kCFOBJECT) {
                    CFRelease(((PyObjCObject*)obj)->objc_object);
                } else if (strcmp(object_getClassName(((PyObjCObject*)obj)->objc_object),
                        "NSAutoreleasePool") != 0) {

                        CFRelease(((PyObjCObject*)obj)->objc_object);
                } else {
                    CFRelease(((PyObjCObject*)obj)->objc_object);
                }

            PyObjC_HANDLER
                NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
                    localException);

            PyObjC_ENDHANDLER
            ((PyObjCObject*)obj)->objc_object = nil;
        }
    }

    Py_TYPE(obj)->tp_free(obj);

    PyErr_Restore(ptype, pvalue, ptraceback);
}


static inline PyObject*
_type_lookup(PyTypeObject* tp, PyObject* name
#ifndef PyObjC_FAST_UNICODE_ASCII
        , PyObject* name_bytes
#endif
    )
{
    Py_ssize_t i, n;
    PyObject *mro, *base, *dict;
    PyObject *descr = NULL;
    PyObject* res;
#ifndef PyObjC_FAST_UNICODE_ASCII
    SEL sel = PyObjCSelector_DefaultSelector(PyBytes_AsString(name_bytes));
#else
    SEL sel = PyObjCSelector_DefaultSelector(PyObjC_Unicode_Fast_Bytes(name));
#endif

    /* Look in tp_dict of types in MRO */
    mro = tp->tp_mro;
    if (mro == NULL) {
        return NULL;
    }

    res = NULL;
    PyObjC_Assert(PyTuple_Check(mro), NULL);
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        base = PyTuple_GET_ITEM(mro, i);

        if (PyObjCClass_Check(base)) {
            PyObjCClass_CheckMethodList(base, 0);
            dict = ((PyTypeObject *)base)->tp_dict;

        } else if (PyType_Check(base)) {
            dict = ((PyTypeObject *)base)->tp_dict;


#if PY_MAJOR_VERSION == 2
        } else if (PyClass_Check(base)) {
            dict = ((PyClassObject*)base)->cl_dict;
#endif
        } else {
            return NULL;
        }

        PyObjC_Assert(dict && PyDict_Check(dict), NULL);

        descr = PyDict_GetItem(dict, name);
        if (descr != NULL) {
            break;
        }

        if (PyObjCClass_Check(base)) {
            /* Check if the name is a selector that
             * is not cached yet
             *
             * Skip hidden methods.
             */
            if (!PyObjCClass_HiddenSelector(base, sel, NO)) {
                descr = PyObjCClass_TryResolveSelector(base, name, sel);
                if (descr) {
                    return descr;
                } else if (PyErr_Occurred()) {
                    return NULL;
                }
            }
        }
    }

    return descr;
}

static inline PyObject*
_type_lookup_harder(PyTypeObject* tp, PyObject* name
#ifndef PyObjC_FAST_UNICODE_ASCII
        , PyObject* name_bytes
#endif
    )
    /* XXX: Name needs changing.
     *      Second pass through the class hierarchy when _type_lookup failed and the name is not in __dict__
     *      Used to look for selectors that cannot be found using the default translation from Python to ObjC
     *      (for example 'some_methodWithArg:andArg').
     *
     *      The assumption is that user code is not buggy, and hence it is acceptable to take an expensive
     *      path once in a while.
     * XXX: May need to cache the found methods in subclasses as well to be 100% reliable, add test
     *      that first finds the method in a superclass, then loads a shared library with a subclass that
     *      also defines the method. This should find the subclass method (but might not with current code).
     */
{
    Py_ssize_t i, n;
    PyObject *mro, *base;
    PyObject *descr = NULL;
    PyObject* res;
    char selbuf[2048];
    char* sel_name;

    /* Look in tp_dict of types in MRO */
    mro = tp->tp_mro;
    if (mro == NULL) {
        return NULL;
    }
    res = NULL;
    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        Class cls;
        Method*   methods;
        unsigned int method_count, j;
        base = PyTuple_GET_ITEM(mro, i);

        if (!PyObjCClass_Check(base)) {
            continue;
        }

        cls = PyObjCClass_GetClass(base);

        methods = class_copyMethodList(cls, &method_count);
        for (j = 0; j < method_count; j++) {
            Method m = methods[j];
            if (PyObjCClass_HiddenSelector(base, method_getName(m), NO)) {
                continue;
            }

            sel_name = (char*)PyObjC_SELToPythonName(
                        method_getName(m),
                        selbuf,
                        sizeof(selbuf));
            if (sel_name == NULL) continue;

            if (strcmp(sel_name,
#ifndef PyObjC_FAST_UNICODE_ASCII
                PyBytes_AS_STRING(name_bytes)
#else
                PyObjC_Unicode_Fast_Bytes(name)
#endif
                ) == 0) {

                /* Create (unbound) selector */
                descr = PyObjCSelector_NewNative(
                        cls, method_getName(m),
                        method_getTypeEncoding(m), 0);
                free(methods);
                if (descr == NULL) {
                    return NULL;
                }


                /* add to __dict__ 'cache' */
                if (PyDict_SetItem(((PyTypeObject*)base)->tp_dict, name, descr) == -1) {
                    Py_DECREF(descr);
                    return NULL;
                }

                /* and return as a borrowed reference */
                Py_DECREF(descr);
                return descr;
            }
        }
        free(methods);
    }

    return descr;
}

PyObject*
PyObjCClass_TryResolveSelector(PyObject* base, PyObject* name, SEL sel)
{
    Class cls = PyObjCClass_GetClass(base);
    PyObject* dict = ((PyTypeObject *)base)->tp_dict;
    Method m = class_getInstanceMethod(cls, sel);
    if (m) {
#ifndef PyObjC_FAST_BUT_INEXACT
        int use = 1;
        Class sup = class_getSuperclass(cls);
        if (sup) {
            Method m_sup = class_getInstanceMethod(sup, sel);
            if (m_sup == m) {
                use = 0;
            }
        }
        if (!use) return NULL;
#endif

        /* Create (unbound) selector */
        PyObject* result = PyObjCSelector_NewNative(
                cls, sel, method_getTypeEncoding(m), 0);
        if (result == NULL) {
            return NULL;
        }

        /* add to __dict__ 'cache' */
        if (PyDict_SetItem(dict, name, result) == -1) {
            Py_DECREF(result);
            return NULL;
        }

        /* and return as a borrowed reference */
        Py_DECREF(result);
        return result;
    }
    return NULL;
}

static PyObject**
_get_dictptr(PyObject* obj)
{
    Py_ssize_t dictoffset;
    id obj_object;
    dictoffset = PyObjCClass_DictOffset((PyObject*)Py_TYPE(obj));
    if (dictoffset == 0) return NULL;
    obj_object = PyObjCObject_GetObject(obj);
    PyObjC_Assert(obj_object != nil, NULL);
    return (PyObject**)(((char*)obj_object) + dictoffset);
}

static PyObject *
object_getattro(PyObject *obj, PyObject * volatile name)
{
    PyTypeObject *tp = NULL;
    PyObject *descr = NULL;
    PyObject *res = NULL;
    descrgetfunc f;
    PyObject** dictptr;
    id obj_inst;
    const char* namestr;
#ifndef PyObjC_FAST_UNICODE_ASCII
    PyObject* name_bytes;
#endif

    if (name == NULL) {
        PyErr_SetString(PyExc_TypeError, "<nil> name");
        return NULL;
    }

    if (PyUnicode_Check(name)) {
#ifndef PyObjC_FAST_UNICODE_ASCII
        name_bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
        if (name_bytes == NULL) return NULL;
#else
        if (PyObjC_Unicode_Fast_Bytes(name) == NULL) return NULL;
#endif

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(name)) {
        name_bytes = name; Py_INCREF(name_bytes);
#endif
    } else {
        PyErr_Format(PyExc_TypeError,
            "attribute name must be string, got %s",
            Py_TYPE(name)->tp_name);
        return NULL;
    }

#ifndef PyObjC_FAST_UNICODE_ASCII
    namestr = PyBytes_AsString(name_bytes);
#else
    namestr = PyObjC_Unicode_Fast_Bytes(name);
#endif
    if (namestr == NULL) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_ValueError, "Empty name");
        }
        return NULL;
    }

    obj_inst = PyObjCObject_GetObject(obj);
    if (!obj_inst) {
#if PY_MAJOR_VERSION == 2
        PyErr_Format(PyExc_AttributeError,
             "cannot access attribute '%.400s' of NIL '%.50s' object",
             PyString_AS_STRING(name),
             Py_TYPE(obj)->tp_name);
#else
        PyErr_Format(PyExc_AttributeError,
             "cannot access attribute '%U' of NIL '%.50s' object",
             name,
             Py_TYPE(obj)->tp_name);
#endif
        goto done;
    }

    if (PyObjCObject_GetFlags(obj) & PyObjCObject_kMAGIC_COOKIE) {
        /* A magic cookie object, don't treat this like a normal
         * object because that might cause havoc.
         */

    } else {
        /* Special hack for KVO on MacOS X, when an object is observed it's
         * ISA is changed by the runtime. We change the python type as well.
         */
        tp = (PyTypeObject*)PyObjCClass_New(object_getClass(obj_inst));

        descr = NULL;

        if (tp != Py_TYPE(obj)) {
            /* Workaround for KVO implementation feature */
            PyObject* dict;

            if (tp->tp_dict == NULL) {
                if (PyType_Ready(tp) < 0)
                    goto done;
            }

            Py_DECREF(Py_TYPE(obj));
            Py_TYPE(obj) = tp;
            Py_INCREF(tp);

            PyObjCClass_CheckMethodList((PyObject*)tp, 0);
            dict = tp->tp_dict;

            PyObjC_Assert(dict && PyDict_Check(dict), NULL);
            descr = PyDict_GetItem(dict, name);
        }
        Py_CLEAR(tp);
    }

    tp = Py_TYPE(obj);
    if (tp->tp_dict == NULL) {
        if (PyType_Ready(tp) < 0)
            goto done;
    }

    /* replace _PyType_Lookup */
    if (descr == NULL) {
        descr = _type_lookup(tp, name
#ifndef PyObjC_FAST_UNICODE_ASCII
            , name_bytes
#endif
        );
    }

    f = NULL;
    if (descr != NULL
#if PY_MAJOR_VERSION == 2
        && PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)
#endif
        ) {
        f = Py_TYPE(descr)->tp_descr_get;
        if (f != NULL && PyDescr_IsData(descr)) {
            res = f(descr, obj, (PyObject*)Py_TYPE(obj));
            if (res == NULL && !PyErr_Occurred()) {
                PyErr_SetString(PyObjCExc_Error,
                    "Descriptor getter returned NULL "
                    "without raising an exception");
            }
            goto done;
        }
    }

    if (strcmp(
#ifndef PyObjC_FAST_UNICODE_ASCII
        PyBytes_AS_STRING(name_bytes),
#else
        PyObjC_Unicode_Fast_Bytes(name),
#endif

        "__del__") == 0) {

        res = PyObjCClass_GetDelMethod((PyObject*)Py_TYPE(obj));
        goto done;
    }

    /* First try the __dict__ */
    dictptr = _get_dictptr(obj);

    if (dictptr != NULL) {
        PyObject *dict;

        if (strcmp(
#ifndef PyObjC_FAST_UNICODE_ASCII
            PyBytes_AS_STRING(name_bytes),
#else
            PyObjC_Unicode_Fast_Bytes(name),
#endif
            "__dict__") == 0) {

            res = *dictptr;
            if (res == NULL) {
                *dictptr = PyDict_New();
                if (*dictptr == NULL) {
                    PyErr_Clear();
                }
                res = *dictptr;
            }
            if (res != NULL) {
                Py_INCREF(res);
                goto done;
            }
        } else {
            dict = *dictptr;
            if (dict != NULL) {
                res = PyDict_GetItem(dict, name);
                if (res != NULL) {
                    Py_INCREF(res);
                    goto done;
                }
            }
        }
    }

    if (descr == NULL) {
        /*
         * The method cannot be found in the regular path.
         * Assume that the user knows what he's doing and is looking
         * for a method where the selector does not conform to the
         * naming convention that _type_lookup expects.
         */
        descr = _type_lookup_harder(tp, name
#ifndef PyObjC_FAST_UNICODE_ASCII
            , name_bytes
#endif
        );
        if (descr != NULL
#if PY_MAJOR_VERSION == 2
            && PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)
#endif
            ) {
            f = Py_TYPE(descr)->tp_descr_get;
        }
    }

    if (f != NULL) {
        res = f(descr, obj, (PyObject*)Py_TYPE(obj));
        if (res == NULL && !PyErr_Occurred()) {
            PyErr_SetString(PyObjCExc_Error,
                "Descriptor getter returned NULL "
                "without raising an exception");
        }
        goto done;
    }

    if (descr != NULL) {
        Py_INCREF(descr);
        res = descr;
        goto done;
    }

    if (!PyObjCObject_IsClassic(obj)) {
        res = PyObjCSelector_FindNative(obj, namestr);
        if (res) goto done;
    }

    PyErr_Format(PyExc_AttributeError,
         "'%.50s' object has no attribute '%.400s'",
         tp->tp_name, namestr);

done:
    if (res != NULL) {
        /* class methods cannot be accessed through instances */
        if (PyObjCSelector_Check(res)
                && PyObjCSelector_IsClassMethod(res)) {
            Py_DECREF(res);
#if PY_MAJOR_VERSION == 2
            PyErr_Format(PyExc_AttributeError,
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#else
            PyErr_Format(PyExc_AttributeError,
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#endif
            res = NULL;
        }
    }
#ifndef PyObjC_FAST_UNICODE_ASCII
    Py_DECREF(name_bytes);
#endif
    return res;
}


static int
object_setattro(PyObject *obj, PyObject *name, PyObject *value)
{
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrsetfunc f;
    PyObject** dictptr;
    int res;
    id obj_inst;
    NSString *obj_name;
#ifndef PyObjC_FAST_UNICODE_ASCII
    PyObject* name_bytes;
#endif

    if (PyUnicode_Check(name)) {
#ifndef PyObjC_FAST_UNICODE_ASCII
        name_bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
        if (name_bytes == NULL) return -1;
#else
        if (PyObjC_Unicode_Fast_Bytes(name) == NULL) return -1;
#endif

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(name)) {
        name_bytes = name; Py_INCREF(name_bytes);
#endif
    } else {
        PyErr_Format(PyExc_TypeError,
            "attribute name must be string, got %s",
            Py_TYPE(name)->tp_name);
        return -1;
    }

    obj_inst = PyObjCObject_GetObject(obj);
    if (obj_inst == nil) {
        PyErr_Format(PyExc_AttributeError,
             "Cannot set '%s.400s' on NIL '%.50s' object",
#ifndef PyObjC_FAST_UNICODE_ASCII
             PyBytes_AS_STRING(name_bytes),
#else
             PyObjC_Unicode_Fast_Bytes(name),
#endif
             tp->tp_name);
#ifndef PyObjC_FAST_UNICODE_ASCII
        Py_DECREF(name_bytes);
#endif
        return -1;
    }

    obj_name = nil;
    if (((PyObjCClassObject*)tp)->useKVO) {
        if ((PyObjCObject_GetFlags(obj) & PyObjCObject_kUNINITIALIZED) == 0) {
            if (!PyObjC_is_ascii_prefix(name, "_", 1)) {
                obj_name = [NSString stringWithUTF8String:
#ifndef PyObjC_FAST_UNICODE_ASCII
                    PyBytes_AS_STRING(name_bytes)
#else
                    PyObjC_Unicode_Fast_Bytes(name)
#endif
                ];
                NS_DURING
                    [(NSObject*)obj_inst willChangeValueForKey:obj_name];
                NS_HANDLER
                    PyObjCErr_FromObjC(localException);
                NS_ENDHANDLER
                if (PyErr_Occurred()) {
#ifndef PyObjC_FAST_UNICODE_ASCII
                    Py_DECREF(name_bytes);
#endif
                    return -1;
                }
            }
        }
    }
    descr = _type_lookup(tp, name
#ifndef PyObjC_FAST_UNICODE_ASCII
        , name_bytes
#endif
    );
    f = NULL;
    if (descr != NULL
#if PY_MAJOR_VERSION == 2
        && PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)
#endif
       ) {
        f = Py_TYPE(descr)->tp_descr_set;
        if (f != NULL && PyDescr_IsData(descr)) {
            res = f(descr, obj, value);
            goto done;
        }
    }

    dictptr = _get_dictptr(obj);
    if (dictptr != NULL) {
        PyObject *dict;

        dict = *dictptr;

        if (dict == NULL && value != NULL) {
            dict = PyDict_New();
            if (dict == NULL) {
                res = -1;
                goto done;
            }

            *dictptr = dict;
        }

        if (dict != NULL) {
            if (value == NULL) {
                res = PyDict_DelItem(dict, name);

            } else {
                res = PyDict_SetItem(dict, name, value);
            }

            if (res < 0 && PyErr_ExceptionMatches(PyExc_KeyError)) {
                PyErr_SetObject(PyExc_AttributeError, name);
            }
            goto done;
        }
    }

    if (f != NULL) {
        res = f(descr, obj, value);
        goto done;
    }

    if (descr == NULL) {
        PyErr_Format(PyExc_AttributeError,
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name,
#ifndef PyObjC_FAST_UNICODE_ASCII
                 PyBytes_AS_STRING(name_bytes)
#else
                 PyObjC_Unicode_Fast_Bytes(name)
#endif
             );
        res = -1;
        goto done;
    }

    PyErr_Format(PyExc_AttributeError,
             "'%.50s' object attribute '%.400s' is read-only",
             tp->tp_name,
#ifndef PyObjC_FAST_UNICODE_ASCII
             PyBytes_AS_STRING(name_bytes)
#else
             PyObjC_Unicode_Fast_Bytes(name)
#endif
    );
    res = -1;
  done:
    if (obj_inst && obj_name) {
        NS_DURING
            [(NSObject*)obj_inst didChangeValueForKey:obj_name];
        NS_HANDLER
            PyObjCErr_FromObjC(localException);
        NS_ENDHANDLER
        if (PyErr_Occurred()) {
            res = -1;
        }
    }
#ifndef PyObjC_FAST_UNICODE_ASCII
    Py_DECREF(name_bytes);
#endif
    return res;
}

PyDoc_STRVAR(objc_get_real_class_doc, "Return the current ISA of the object");

static PyObject*
objc_get_real_class(PyObject* self, void* closure __attribute__((__unused__)))
{
    id obj_object;
    PyObject* ret;

    obj_object = PyObjCObject_GetObject(self);
    PyObjC_Assert(obj_object != nil, NULL);
    ret = PyObjCClass_New(object_getClass(obj_object));
    if (ret != (PyObject*)Py_TYPE(self)) {
        Py_DECREF(Py_TYPE(self));
        Py_TYPE(self) = (PyTypeObject*)ret;
        Py_INCREF(ret);
    }
    return ret;
}

PyDoc_STRVAR(obj_get_instanceMethods_doc,
"The attributes of this field are the instance methods of this object. This\n"
"can be used to force access to an instance method."
);

static PyObject*
obj_get_instanceMethods(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCObject* self = (PyObjCObject*)_self;
    return PyObjCMethodAccessor_New((PyObject*)self, 0);
}

static PyObject*
obj_get_blocksignature(PyObject* self, void* closure __attribute__((__unused__)))
{
    if (PyObjCObject_IsBlock(self)) {
        PyObject* v = (PyObject*)PyObjCObject_GetBlock(self);
        if (v != NULL) {
            Py_INCREF(v);
            return v;
        }
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static int
obj_set_blocksignature(PyObject* self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
    if (!PyObjCObject_IsBlock(self)) {
        PyErr_SetString(PyExc_TypeError, "You can only change this value on blocks");
        return  -1;
    }

    if (newVal != NULL) {
        if (!PyObjCMethodSignature_Check(newVal)) {
            PyErr_SetString(PyExc_TypeError, "New value must be a method signature");
            return -1;
        }
    }

    PyObject* v = (PyObject*)PyObjCObject_GetBlock(self);
    if (v != NULL) {
        Py_DECREF(v);
    }

    Py_XINCREF(newVal);
    PyObjCObject_SET_BLOCK(self, (PyObjCMethodSignature*)newVal);
    return 0;
}

static PyGetSetDef obj_getset[] = {
    {
        "pyobjc_ISA",
        objc_get_real_class,
        NULL,
        objc_get_real_class_doc,
        0
    },
    {
        "pyobjc_instanceMethods",
        obj_get_instanceMethods,
        NULL,
        obj_get_instanceMethods_doc,
        0
    },
    {
        "__block_signature__",
        obj_get_blocksignature,
        obj_set_blocksignature,
        "Call signature for a block, or None",
        0
    },
    { 0, 0, 0, 0, 0 }
};

/*
 * We don't support pickling of Objective-C objects at the moment. The new
 * version 2 of the pickle protocol has a default pickle method for new-style
 * classes that doesn't work for us (it will write incomplete values to the
 * pickle). This method forces a failure during pickling.
 */
static PyObject*
meth_reduce(PyObject* self __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError,
        "Cannot pickle Objective-C objects");
    return NULL;
}

static PyObject*
meth_sizeof(PyObject* self __attribute__((__unused__)))
{
    /* Basis __sizeof__ implementation for Cocoa objects.
     * This doesn't return the correct size for collections (such as NSArray),
     * but is better than the default implementation
     */
    if (PyObjCObject_GetObject(self) == nil) {
        return PyLong_FromSize_t(Py_TYPE(self)->tp_basicsize);

    } else {
        return PyLong_FromSize_t(
                  Py_TYPE(self)->tp_basicsize
                + class_getInstanceSize(object_getClass(PyObjCObject_GetObject(self)))
            );
    }
}

static PyObject*
as_cobject(PyObject* self)
{
    if (PyObjCObject_GetObject(self) == nil) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyCapsule_New(PyObjCObject_GetObject(self), "objc.__object__", NULL);
}

PyObject*
PyObjC_get_c_void_p(void)
{
static  PyObject* c_void_p = NULL;
    if (c_void_p == NULL) {
        PyObject* mod_ctypes = PyImport_ImportModule("ctypes");
        if (mod_ctypes == NULL) {
            /* ctypes is nota available */
            return NULL;
        }

        c_void_p = PyObject_GetAttrString(mod_ctypes, "c_void_p");
        Py_DECREF(mod_ctypes);
        if (c_void_p == NULL) {
            /* invalid or incomplete module */
            return NULL;
        }
    }
    return c_void_p;
}

static PyObject*
as_ctypes_voidp(PyObject* self)
{
    PyObject* c_void_p;

    if (PyObjCObject_GetObject(self) == nil) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    c_void_p = PyObjC_get_c_void_p();
    if (c_void_p == NULL) {
        return NULL;
    }

    return PyObject_CallFunction(c_void_p, "k", (long)PyObjCObject_GetObject(self));
}


/*
 * Implementation of __dir__, which is the hook used by dir() on python 2.6 or later.
 */
static PyObject*
meth_dir(PyObject* self)
{
    PyObject* result;
    Class     cls;
    Method*   methods;
    unsigned int method_count, i;
    char      selbuf[2048];


    /* Start of with keys in __dict__ */
    result = PyDict_Keys(Py_TYPE(self)->tp_dict);
    if (result == NULL) {
        return NULL;
    }

    cls = object_getClass(PyObjCObject_GetObject(self));
    while (cls != NULL) {
        /* Now add all instance method names */
        methods = class_copyMethodList(cls, &method_count);
        for (i = 0; i < method_count; i++) {
            char* name;
            PyObject* item;

            /* Check if the selector should be hidden */
            if (PyObjCClass_HiddenSelector((PyObject*)Py_TYPE(self),
                        method_getName(methods[i]), NO)) {
                continue;
            }

            name = (char*)PyObjC_SELToPythonName(
                        method_getName(methods[i]),
                        selbuf,
                        sizeof(selbuf));
            if (name == NULL) continue;

            item = PyText_FromString(name);
            if (item == NULL) {
                free(methods);
                Py_DECREF(result);
                return NULL;
            }

            if (PyList_Append(result, item) == -1) {
                free(methods);
                Py_DECREF(result);
                Py_DECREF(item);
                return NULL;
            }
            Py_DECREF(item);
        }
        free(methods);

        cls = class_getSuperclass(cls);
    }
    return result;
}

static PyMethodDef obj_methods[] = {
    {
        "__reduce__",
        (PyCFunction)meth_reduce,
        METH_NOARGS,
        "Used for pickling"
    },
    {
        "__cobject__",
        (PyCFunction)as_cobject,
        METH_NOARGS,
        "Return a CObject representing this object"
    },
    {
        "__c_void_p__",
        (PyCFunction)as_ctypes_voidp,
        METH_NOARGS,
        "Return a ctypes.c_void_p representing this object"
    },
    {
        "__sizeof__",
        (PyCFunction)meth_sizeof,
        METH_NOARGS,
        0
    },
    {
        "__dir__",
        (PyCFunction)meth_dir,
        METH_NOARGS,
        "dir() hook, don't call directly"
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }
};


PyObjCClassObject PyObjCObject_Type = {
    .base = {
        .ht_type = {
            PyVarObject_HEAD_INIT(&PyObjCClass_Type, 0)
            .tp_name        = "objc_object",
            .tp_basicsize   = sizeof(PyObjCObject),
            .tp_itemsize    = 0,
            .tp_dealloc     = object_dealloc,
            .tp_repr        = object_repr,
            .tp_getattro    = object_getattro,
            .tp_setattro    = object_setattro,
            .tp_flags       = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
            .tp_methods     = obj_methods,
            .tp_getset      = obj_getset,
            .tp_alloc       = PyType_GenericAlloc,
            .tp_new         = object_new,
            .tp_del         = (destructor)object_del
        },
    }
};

/*
 *  Allocate a proxy object for use during the call of __del__,
 *  this isn't a full-featured proxy object.
 */
PyObject*
_PyObjCObject_NewDeallocHelper(id objc_object)
{
    PyObject* res;
    PyTypeObject* cls_type;

    PyObjC_Assert(objc_object != nil, NULL);
    cls_type = (PyTypeObject*)PyObjCClass_New(object_getClass(objc_object));
    if (cls_type == NULL) {
        return NULL;
    }

    res = cls_type->tp_alloc(cls_type, 0);
    Py_DECREF(cls_type);
    if (res == NULL) {
        return NULL;
    }

    PyObjCClass_CheckMethodList((PyObject*)Py_TYPE(res), 1);

    ((PyObjCObject*)res)->objc_object = objc_object;
    ((PyObjCObject*)res)->flags = PyObjCObject_kDEALLOC_HELPER;
    return res;
}

void
_PyObjCObject_FreeDeallocHelper(PyObject* obj)
{
    if (Py_REFCNT(obj) != 1) {
        /* Someone revived this object. Objective-C doesn't like
         * this at all, therefore warn the user about this and
         * zero out the instance.
         */
        char buf[256];
        snprintf(buf, sizeof(buf),
            "revived Objective-C object of type %s. Object is zero-ed out.",
            Py_TYPE(obj)->tp_name);

        PyErr_Warn(PyObjCExc_ObjCRevivalWarning, buf);

        id objc_object = PyObjCObject_GetObject(obj);

        if (((PyObjCObject*)obj)->flags & PyObjCObject_kSHOULD_NOT_RELEASE) {
            /* pass */
        } else if (((PyObjCObject*)obj)->flags & PyObjCObject_kUNINITIALIZED) {
            /* pass */
        } else {
            CFRelease(objc_object);
        }

        PyObjC_UnregisterPythonProxy(
            objc_object, obj);
        ((PyObjCObject*)obj)->objc_object = nil;

        Py_DECREF(obj);

        return;
    }
    Py_DECREF(obj);
}


PyObject*
PyObjCObject_New(id objc_object, int flags, int retain)
{
    Class cls = object_getClass(objc_object);
    PyTypeObject* cls_type;
    PyObject*     res;

    res = PyObjC_FindPythonProxy(objc_object);
    if (res) return res;

    PyObjC_Assert(objc_object != nil, NULL);

    cls_type = (PyTypeObject*)PyObjCClass_New(cls);
    if (cls_type == NULL) {
        return NULL;
    }

    res = cls_type->tp_alloc(cls_type, 0);
    Py_DECREF(cls_type);
    if (res == NULL) {
        return NULL;
    }

    if (cls_type->tp_basicsize == sizeof(PyObjCBlockObject)) {
        flags |= PyObjCObject_kBLOCK;
    }

    /* This should be in the tp_alloc for the new class, but
     * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
     */
    PyObjCClass_CheckMethodList((PyObject*)Py_TYPE(res), 1);

    ((PyObjCObject*)res)->objc_object = objc_object;
    ((PyObjCObject*)res)->flags = flags;

    if (flags & PyObjCObject_kBLOCK) {
        ((PyObjCBlockObject*)res)->signature = NULL;
        }

    if (retain) {
        if (strcmp(object_getClassName(objc_object),
                        "NSAutoreleasePool") != 0) {
            /* NSAutoreleasePool doesn't like retain */
            CFRetain(objc_object);
        }
    }

    /*
     * Don't register if we use the default flags, other parts will do
     * that if necessary. I don't like this, but don't want to pollute
     * the interface of this function with yet another argument.
     */
    if (flags != PyObjCObject_kDEFAULT) {
        PyObjC_RegisterPythonProxy(objc_object, res);
    }
    return res;
}

PyObject*
PyObjCObject_FindSelector(PyObject* object, SEL selector)
{
    PyObject* meth;

    meth = PyObjCClass_FindSelector((PyObject*)Py_TYPE(object), selector, NO);

    if (meth == NULL) {
        return NULL;
    } else {
        return meth;
    }
}

id
(PyObjCObject_GetObject)(PyObject* object)
{
    if (!PyObjCObject_Check(object)) {
        PyErr_Format(PyExc_TypeError,
            "'objc.objc_object' expected, got '%s'",
            Py_TYPE(object)->tp_name);

    }
    return PyObjCObject_GetObject(object);
}

void
PyObjCObject_ClearObject(PyObject* object)
{
    if (!PyObjCObject_Check(object)) {
        PyErr_Format(PyExc_TypeError,
            "'objc.objc_object' expected, got '%s'",
            Py_TYPE(object)->tp_name);

    }
    PyObjC_UnregisterPythonProxy(
            ((PyObjCObject*)object)->objc_object, object);
    ((PyObjCObject*)object)->objc_object = nil;
}

PyObject* PyObjCObject_GetAttr(PyObject* obj, PyObject* name)
{
    return object_getattro(obj, name);
}


PyObject* PyObjCObject_GetAttrString(PyObject* obj, char* name)
{
    PyObject* pyname = PyText_FromString(name);
    if (pyname == NULL) return NULL;

    PyObject* rv = object_getattro(obj, pyname);
    Py_DECREF(pyname);
    return rv;
}
