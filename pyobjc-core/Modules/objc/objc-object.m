/*
 * Implementation of objective-C object wrapper
 *
 * XXX: Free-threading: Access to 'flags' is not yet thread safe, need to audit all
 *      paths that change flags.
 */
#include "pyobjc.h"

#include <objc/Object.h>
#include <stddef.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable object_new(PyTypeObject* type __attribute__((__unused__)),
                                      PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"cobject", "c_void_p", NULL};
    PyObject*    cobject    = NULL;
    PyObject*    c_void_p   = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OO", keywords, &cobject, &c_void_p)) {
        return NULL;
    }

    if (cobject != NULL && c_void_p != NULL) {
        PyErr_SetString(PyExc_TypeError, "Pass either cobject or c_void_p, but not both");
        return NULL;
    }

    if (cobject != NULL) {
        if (!PyCapsule_CheckExact(cobject)) {
            PyErr_SetString(PyExc_TypeError, "cobject' argument is not a PyCapsule");
            return NULL;
        }

        NSObject* p = PyCapsule_GetPointer(cobject, "objc.__object__");
        if (PyErr_Occurred()) {
            return NULL;
        }

        return id_to_python(p);

    } else if (c_void_p != NULL) {
        NSObject* p;
        PyObject* attrval;

        if (PyLong_Check(c_void_p)) {
            attrval = c_void_p;
            Py_INCREF(attrval);

        } else {
            attrval = PyObject_GetAttrString(c_void_p, "value");
            if (attrval == NULL) {
                return NULL;
            }
        }

        if (PyLong_Check(attrval)) {
            p = PyLong_AsVoidPtr(attrval);
            if (p == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(attrval);
                return NULL;
                // LCOV_EXCL_STOP
            }

        } else {
            PyErr_SetString(PyExc_ValueError, "c_void_p.value is not an integer");
            return NULL;
        }

        Py_DECREF(attrval);
        return id_to_python(p);

    } else {
        PyErr_SetString(PyExc_TypeError,
                        "Use class methods to instantiate new Objective-C objects");
        return NULL;
    }
}

static PyObject* _Nullable object_repr(PyObject* _self)
{
    PyObjCObject* self = (PyObjCObject*)_self;
    PyObject*     res;
    unsigned int  flags;

    flags = self->flags;

    if (flags & PyObjCObject_kMAGIC_COOKIE) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        //
        // There currently is no code path that can create objective-c
        // magic instances, only through CoreFoundation (corefoundation.m)
        // and those don't hit this path.
        return PyUnicode_FromFormat("<%s objective-c magic instance %p>",
                                    Py_TYPE(self)->tp_name, self->objc_object);
        // LCOV_EXCL_STOP
    }

    /* Try to call the method 'description', which is the ObjC
     * equivalent of __repr__. If that fails we'll fall back to
     * the default repr.
     * Don't call 'description' for uninitialized objects, that
     * is undefined behaviour and will crash the interpreter sometimes.
     *
     * Free threaded: the UNINITIALIZED flags is never re-set once cleared.
     */
    PyObject* args[2] = {NULL, (PyObject*)self};
    res               = PyObject_VectorcallMethod(PyObjCNM_description, args + 1,
                                                  1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    if (res == NULL) {
        PyErr_Clear();
    } else if (res == Py_None) {
        Py_DECREF(res);
    } else {
        return res;
    }

    res = PyUnicode_FromFormat("<%s objective-c instance %p>", Py_TYPE(self)->tp_name,
                               self->objc_object);

    return res;
}

// LCOV_EXCL_START
static void
object_del(PyObject* obj __attribute__((__unused__)))
{
    /* Dummy function, we do not want the default implementation */
}
// LCOV_EXCL_STOP

static void
object_dealloc(PyObject* obj)
{
    /*
     * Save exception information, needed because releasing the object
     * might clear or modify the exception state.
     *
     * free-threaded: the dealloc method can only be called when there
     * are no references to `obj` left, hence no need to use locking here.
     */
    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);
    id objc_object = ((PyObjCObject*)obj)->objc_object;

    PyObjC_UnregisterPythonProxy(objc_object, obj);

    if (PyObjCObject_GetFlags(obj) != PyObjCObject_kDEALLOC_HELPER) {
        /* Release the proxied object, we don't have to do this when
         * there is no proxied object.
         */
        if ((((PyObjCObject*)obj)->flags & PyObjCObject_kSHOULD_NOT_RELEASE)) {
            /* pass */

        } else {
            Py_BEGIN_ALLOW_THREADS
                @try {
                    [objc_object release];

                } @catch (NSObject* localException) {
                    NSLog(@"PyObjC: Exception during dealloc of proxy: %@",
                          localException);
                }
            Py_END_ALLOW_THREADS;
        }
    }
    if (PyObjCObject_IsBlock(obj)) {
        SET_FIELD(((PyObjCBlockObject*)obj)->signature, NULL);
    }
    Py_TYPE(obj)->tp_free(obj);

    PyErr_Restore(ptype, pvalue, ptraceback);
}

static int
object_verify_type(PyObject* obj)
{
    /* Check that the Objective-C type of 'obj' hasn't changed */
    id obj_inst;

    obj_inst = PyObjCObject_OBJECT(obj);
    assert(obj_inst != nil);

    if (PyObjCClass_IsCFWrapper(Py_TYPE(obj))) {
        /* Object is a CoreFoundation type, ISA swiffling doesn't
         * apply, and the bridge uses different Python types for
         * the various CF types while those have one of a (very)
         * small set of Objective-C classes.
         */
        return 0;
    }

    if (PyObjCObject_GetFlags(obj) & PyObjCObject_kMAGIC_COOKIE) {
        /* A magic cookie object, don't treat this like a normal
         * object because that might cause havoc.
         */

    } else { // LCOV_EXCL_LINE
        /* Special hack for KVO on MacOS X, when an object is observed it's
         * ISA is changed by the runtime. We change the python type as well.
         *
         * (The same can happen when other code perform ISA swiffling)
         */

        /* object_getClass only returns Nil if its argument is nil */
        PyTypeObject* tp =
            (PyTypeObject*)PyObjCClass_New((Class _Nonnull)object_getClass(obj_inst));

        if (tp == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_Format(PyObjCExc_Error, "Cannot get class for Objective-C class '%s'",
                         class_getName((Class _Nonnull)object_getClass(obj_inst)));
            return -1;
            // LCOV_EXCL_STOP
        }

        if (tp != Py_TYPE(obj)) {
            int did_change = 0;

            /* XXX: The correct way to do this is calling ``setattr(obj, "__class__",
             * tp)`` Investigate the impact of that. Performance shouldn't be an issue
             * here, a isa change should not happen often.
             *
             * XXX: the setattr call above works from Python, which is confusing
             * behaviour (it changes the class of the proxy, not the ISA). Change
             * object_setattr to either change the ObjC class as well, or to avoid
             * changing the class. The latter is safer, as we cannot properly check if the
             * old and new types are compatible.
             *
             * XXX: Probably need to call PyObject_Type.tp_setattro(...) to avoid hitting
             * calling object_setattro in this file.
             */
            PyTypeObject* tmp = NULL;
            Py_BEGIN_CRITICAL_SECTION(obj);
#ifdef Py_GIL_DISABLED
            /* Recheck in a free threaded build, another thread
             * may have raced us.
             */
            if (tp != Py_TYPE(obj)) {
#endif
                tmp = Py_TYPE(obj);
                Py_SET_TYPE(obj, tp);
                Py_INCREF(tp);
                did_change = 1;

#ifdef Py_GIL_DISABLED
            }
#endif
            Py_END_CRITICAL_SECTION();
            Py_XDECREF(tmp);
            if (did_change) {
                if (PyObjCClass_CheckMethodList((PyObject*)tp, 0)
                    < 0) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(tp);
                    return -1;
                    // LCOV_EXCL_STOP
                }
            }
        }
        Py_CLEAR(tp);
    }
    return 0;
}

static PyObject* _Nullable* _Nullable _get_dictptr(PyObject* obj)
{
    /* XXX: See above: should be safe with a free-threaded build
     */
    Py_ssize_t dictoffset;
    id         objc_object;
    dictoffset = PyObjCClass_DictOffset((PyObject*)Py_TYPE(obj));
    if (dictoffset == 0)
        return NULL;
    objc_object = PyObjCObject_OBJECT(obj);
    assert(objc_object != nil);
    return (PyObject**)(((char*)objc_object) + dictoffset);
}

/* returns a new reference */
static inline PyObject* _Nullable _type_lookup(PyTypeObject* tp, PyObject* name,
                                               const char* name_bytes)
{
    Py_ssize_t i, n;
    PyObject * mro, *base, *dict;
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
    PyObject* first_class = NULL;
#endif
    PyObject* descr = NULL;
    SEL       sel   = PyObjCSelector_DefaultSelector(name_bytes);

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);
    for (i = 0; i < n; i++) {
        base = PyTuple_GET_ITEM(mro, i);

        if (PyObjCClass_Check(base)) {
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
            if (i == 0) {
                first_class = base;
            }
            PyObject* cache = PyObjCClass_GetLookupCache((PyTypeObject*)base);
            if (cache != NULL) {
                int r = PyDict_GetItemRef(cache, name, &descr);
                Py_CLEAR(cache);
                if (r == -1) { // LCOV_BR_EXCL_LINE
                    Py_CLEAR(mro);
                    return NULL; // LCOV_EXCL_LINE
                } else if (r == 1) {
                    break;
                }
            }
#endif

            if (PyObjCClass_CheckMethodList(base, 0) < 0) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(mro);
                return NULL;
                // LCOV_EXCL_STOP
            }

            dict = PyType_GetDict((PyTypeObject*)base);

        } else if (PyType_Check(base)) { // LCOV_BR_EXCL_LINE

            dict = PyType_GetDict((PyTypeObject*)base);

        } else {
            /* This can only happen when an MRO entry
             * is not a class, that shouldn't be possible
             * for Objective-C classes.
             */
            // LCOV_EXCL_START
            Py_CLEAR(mro);
            return NULL;
            // LCOV_EXCL_STOP
        }

        assert(dict && PyDict_Check(dict));

        int r = PyDict_GetItemRef(dict, name, &descr);
        Py_CLEAR(dict);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(mro);
            return NULL;
            // LCOV_EXCL_STOP
        } else if (r == 1) {
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
            if (first_class != NULL) {
                if (PyObjCClass_AddToLookupCache((PyTypeObject*)first_class, name, descr)
                    == -1) {
                    PyErr_Clear();
                }
            }
#endif
            break;
        }

        if (PyObjCClass_Check(base)) {
            /* Check if the name is a selector that
             * is not cached yet
             *
             * Skip hidden methods.
             */
            PyObject* hidden = PyObjCClass_HiddenSelector(base, sel, NO);
            if (!hidden) {
                if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                descr = PyObjCClass_TryResolveSelector(base, name, sel);
                if (descr) {
                    Py_CLEAR(mro);
                    return descr;
                } else if (PyErr_Occurred()) {
                    Py_CLEAR(mro);
                    return NULL;
                }
            }
            Py_CLEAR(hidden);
        }
    }

    Py_CLEAR(mro);
    return descr;
}

/* XXX: Consider passing in name_bytes as well */
/* returns a new reference */
static inline PyObject* _Nullable _type_lookup_harder(PyTypeObject* tp, PyObject* name)
{
    Py_ssize_t i, n;
    PyObject * mro, *base;
    PyObject*  descr = NULL;

    /* Look in tp_dict of types in MRO */
    Py_BEGIN_CRITICAL_SECTION(tp);
    mro = tp->tp_mro;
    Py_XINCREF(mro);
    Py_END_CRITICAL_SECTION();
    if (mro == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    assert(PyTuple_Check(mro));
    n = PyTuple_GET_SIZE(mro);

    for (i = 0; i < n; i++) {
        Class        cls;
        Method*      methods;
        unsigned int method_count, j;
        base = PyTuple_GET_ITEM(mro, i);

        if (!PyObjCClass_Check(base)) { // LCOV_BR_EXCL_LINE
            /* Should not be hit: The last entry
             * on the MRO that is not an ObjC class
             * is ``objc.objc_class`` and that has
             * a Nil Class value, which means that
             * the check below will exit the loop (
             * e.g. never ending up at the PyType_Type
             * on the MRO)
             */
            continue; // LCOV_EXCL_LINE
        }

        cls = PyObjCClass_GetClass(base);
        if (cls == NULL) {
            Py_CLEAR(mro);
            return NULL;
        }

        /* class_copyMethodList will only return NULL when it also
         * sets method_count to 0.
         */
        methods = (Method* _Nonnull)class_copyMethodList(cls, &method_count);
        for (j = 0; j < method_count; j++) {
            Method    m      = methods[j];
            PyObject* hidden = PyObjCClass_HiddenSelector(base, method_getName(m), NO);

            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(mro);
                return NULL;
                // LCOV_EXCL_STOP
            } else if (hidden) {
                Py_CLEAR(hidden);
                continue;
            }

            PyObject* sel_name = PyObjC_SELToPythonName(method_getName(m));
            if (sel_name == NULL) { // LCOV_BR_EXCL_LINE
                /* This can only be hit if the method selector is nil or
                 * if the selector name is longer than 1K
                 */
                // LCOV_EXCL_START
                PyErr_Clear();
                continue;
                // LCOV_EXCL_STOP
            }

            int same = PyObject_RichCompareBool(sel_name, name, Py_EQ);
            Py_CLEAR(sel_name);
            if (same == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_Clear();
                continue;
                // LCOV_EXCL_STOP
            }
            if (same) {
                const char* encoding  = method_getTypeEncoding(m);
                SEL         meth_name = method_getName(m);

                if (encoding == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    free(methods);
                    Py_CLEAR(mro);
                    PyErr_SetString(PyObjCExc_Error,
                                    "Native selector with Nil type encoding");
                    return NULL;
                    // LCOV_EXCL_STOP
                }
                if (meth_name == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    free(methods);
                    Py_CLEAR(mro);
                    PyErr_SetString(PyObjCExc_Error, "Native selector with Nil selector");
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                /* Create (unbound) selector */
                descr = PyObjCSelector_NewNative(cls, meth_name, encoding, 0);
                free(methods);
                if (descr == NULL) { // LCOV_BR_EXCL_LINE
                    /* Can only fail due to memory errors */
                    // LCOV_EXCL_START
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                /* add to __dict__ 'cache' */
                /* 'base' is a PyObjClass instance, using tp_dict is safe */
                if (PyDict_SetItem(((PyTypeObject*)base)->tp_dict, name, descr)
                    == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(descr);
                    Py_CLEAR(mro);
                    return NULL;
                    // LCOV_EXCL_STOP
                }

                Py_CLEAR(mro);
                return descr;
            }
        }
        free(methods);
    }

    Py_CLEAR(mro);
    return descr;
}

static PyObject* _Nullable object_getattro(PyObject* obj, PyObject* name)
{
    PyTypeObject* tp    = NULL;
    PyObject*     descr = NULL;
    PyObject*     res   = NULL;
    descrgetfunc  f;
    PyObject**    dictptr;
    const char*   namestr;

    assert(name != NULL);

    if (!PyUnicode_Check(name)) { // LCOV_BR_EXCL_LINE
        /* Can only happen when someone calls the tp_getattro slot
         * directly.
         */
        // LCOV_EXCL_START
        PyErr_Format(PyExc_TypeError, "attribute name must be string, got %s",
                     Py_TYPE(name)->tp_name);
        return NULL;
        // LCOV_EXCL_STOP
    }

    namestr = PyUnicode_AsUTF8(name);
    if (namestr == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;       // LCOV_EXCL_LINE
    }

    if (object_verify_type(obj) == -1) {
        goto done;
    }

    tp = Py_TYPE(obj);

    /* replace _PyType_Lookup */
    if (descr == NULL) {
        descr = _type_lookup(tp, name, namestr);
        if (descr == NULL && PyErr_Occurred()) {
            return NULL;
        }
    }

    f = NULL;
    if (descr != NULL) {
        f = Py_TYPE(descr)->tp_descr_get;
        if (f != NULL && PyDescr_IsData(descr)) {
            res = f(descr, obj, (PyObject*)Py_TYPE(obj));
            if (res == NULL && !PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(descr);
                PyErr_SetString(PyObjCExc_Error, "Descriptor getter returned NULL "
                                                 "without raising an exception");
                // LCOV_EXCL_STOP
            } // LCOV_EXCL_LINE
            goto done;
        }
    }

    if (PyObjC_is_ascii_string(name, "__del__")) {
        res = PyObjCClass_GetDelMethod((PyObject*)Py_TYPE(obj));
        if (res != NULL) {
            descrgetfunc f = Py_TYPE(res)->tp_descr_get;
            if (f != NULL) {
                PyObject* tmp = f(res, obj, (PyObject*)Py_TYPE(obj));
                Py_CLEAR(res);
                res = tmp;
            }
        } else {
            PyErr_Format(PyExc_AttributeError, "'%.50s' object has no attribute '%.400s'",
                         tp->tp_name, namestr);
        }
        goto done;
    }

    /* First try the __dict__ */
    dictptr = _get_dictptr(obj);

    if (dictptr != NULL) {
        PyObject* dict;

        if (PyObjC_is_ascii_string(name, "__dict__")) {

            res = *(PyObject * PyObjC_ATOMIC*)dictptr;
            if (res == NULL) {
                res = PyDict_New();

                /* free-threading: setting *dictptr must
                 * be done using a critical section to avoid
                 * races between two threads.
                 */
                PyObject* to_clear = NULL;
                Py_BEGIN_CRITICAL_SECTION(obj);
                if (*(PyObject * PyObjC_ATOMIC*)dictptr == NULL) {
                    *(PyObject * PyObjC_ATOMIC*)dictptr = res;
                } else {
                    to_clear = res;
                    res      = *(PyObject * PyObjC_ATOMIC*)dictptr;
                }
                Py_END_CRITICAL_SECTION();
                Py_CLEAR(to_clear);
            }

            if (res != NULL) {
                Py_INCREF(res);
                goto done;
            }

        } else { // LCOV_EXCL_LINE
            dict = *dictptr;
            if (dict != NULL) {
                switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
                    dict, name, &res)) {
                case -1:
                    goto done; // LCOV_EXCL_LINE
                /* case 0: pass */
                case 1:
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
        descr = _type_lookup_harder(tp, name);

        if (descr != NULL) {
            f = Py_TYPE(descr)->tp_descr_get;
        }
        if (descr == NULL && PyErr_Occurred()) {
            return NULL;
        }
    }

    if (f != NULL) {
        res = f(descr, obj, (PyObject*)Py_TYPE(obj));
        if (res == NULL && !PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_Error, "Descriptor getter returned NULL "
                                             "without raising an exception");
            // LCOV_EXCL_STOP
        } // LCOV_EXCL_LINE
        goto done;
    }

    if (descr != NULL) {
        res   = descr;
        descr = NULL;
        goto done;
    }

    res = PyObjCSelector_FindNative(obj, namestr);
    if (res)
        goto done;

    PyErr_Format(PyExc_AttributeError, "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, namestr);

done:
    Py_CLEAR(descr);
    if (res != NULL) {
        /* class methods cannot be accessed through instances */
        if (PyObjCSelector_Check(res) && PyObjCSelector_IsClassMethod(res)) {
            Py_DECREF(res);
            PyErr_Format(PyExc_AttributeError, "'%.50s' object has no attribute '%U'",
                         tp->tp_name, name);
            res = NULL;
        }
    }
    return res;
}

static int
object_setattro(PyObject* obj, PyObject* name, PyObject* _Nullable value)
{
    PyTypeObject* tp = Py_TYPE(obj);
    PyObject*     descr;
    descrsetfunc  f;
    PyObject**    dictptr;
    int           res;
    id            obj_inst;
    NSString*     obj_name;
    const char*   namestr;

    if (!PyUnicode_Check(name)) {
        PyErr_Format(PyExc_TypeError, "attribute name must be string, got %s",
                     Py_TYPE(name)->tp_name);
        return -1;
    }
    namestr = PyUnicode_AsUTF8(name);
    if (namestr == NULL) {
        return -1;
    }

    obj_inst = PyObjCObject_GetObject(obj);

    obj_name = nil;
    if (((PyObjCClassObject*)tp)->useKVO) {
        if (!PyObjC_is_ascii_prefix(name, "_", 1)) {
            obj_name = [NSString
                stringWithUTF8String:(const char* _Nonnull)PyUnicode_AsUTF8(name)];

            if (obj_name == nil) {
                PyErr_SetString(PyObjCExc_Error,
                                "Cannot convert attribute name to NSString");
                return -1;
            }

            @try {
                [(NSObject*)obj_inst willChangeValueForKey:obj_name];
            } @catch (NSObject* localException) {
                PyObjCErr_FromObjC(localException);
            }
            if (PyErr_Occurred()) {
                return -1;
            }
        }
    }
    descr = _type_lookup(tp, name, namestr);
    if (descr == NULL && PyErr_Occurred()) {
        return -1;
    }
    f = NULL;
    if (descr != NULL) {
        f = Py_TYPE(descr)->tp_descr_set;
        if (f != NULL && PyDescr_IsData(descr)) {
            res = f(descr, obj, value);
            goto done;
        }
    }

    dictptr = _get_dictptr(obj);
    if (dictptr != NULL) {
        PyObject* dict;

        dict = *dictptr;

        if (dict == NULL && value != NULL) {
            dict = PyDict_New();
            if (dict == NULL) {
                res = -1;
                goto done;
            }

            /* free-threading: setting *dictptr must
             * be done using a critical section to avoid
             * races between two threads.
             */
            PyObject* to_clear = NULL;
            Py_BEGIN_CRITICAL_SECTION(obj);
            if (*dictptr == NULL) {
                *dictptr = dict;
            } else {
                to_clear = dict;
                dict     = *dictptr;
            }
            Py_END_CRITICAL_SECTION();
            Py_CLEAR(to_clear);
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
        PyErr_Format(PyExc_AttributeError, "'%.50s' object has no attribute '%.400s'",
                     tp->tp_name, PyUnicode_AsUTF8(name));
        res = -1;
        goto done;
    }

    PyErr_Format(PyExc_AttributeError, "'%.50s' object attribute '%.400s' is read-only",
                 tp->tp_name, PyUnicode_AsUTF8(name));
    res = -1;
done:
    Py_CLEAR(descr);
    if (obj_inst && obj_name) {
        @try {
            [(NSObject*)obj_inst didChangeValueForKey:obj_name];
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
        if (PyErr_Occurred()) {
            res = -1;
        }
    }
    return res;
}

PyDoc_STRVAR(objc_get_real_class_doc, "Return the current ISA of the object");

static PyObject* _Nullable objc_get_real_class(PyObject* self,
                                               void* closure __attribute__((__unused__)))
{
    id        objc_object;
    PyObject* ret;

    objc_object = PyObjCObject_OBJECT(self);
    assert(objc_object != nil);

    /* object_getClass only return Nil if its argument is nil */
    ret = PyObjCClass_New((Class _Nonnull)object_getClass(objc_object));
    if (ret == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }
    if (ret != (PyObject*)Py_TYPE(self)) {
        Py_BEGIN_CRITICAL_SECTION(self);
#ifdef Py_GIL_DISABLED
        /* Free-threading: Recheck within a critical section to avoid a race */
        if (ret != (PyObject*)Py_TYPE(self)) {
#endif
            Py_DECREF(Py_TYPE(self));
            Py_SET_TYPE(self, (PyTypeObject*)ret);
            Py_INCREF(ret);
#ifdef Py_GIL_DISABLED
        }
#endif
        Py_END_CRITICAL_SECTION();
    } // LCOV_EXCL_LINE
    return ret;
}

PyDoc_STRVAR(
    obj_get_instanceMethods_doc,
    "The attributes of this field are the instance methods of this object. This\n"
    "can be used to force access to an instance method.");

static PyObject* _Nullable obj_get_instanceMethods(PyObject* _self, void* closure
                                                   __attribute__((__unused__)))
{
    PyObjCObject* self = (PyObjCObject*)_self;
    return PyObjCMethodAccessor_New((PyObject*)self, 0);
}

static PyObject* _Nullable obj_get_flags(PyObject* self,
                                         void*     closure __attribute__((__unused__)))
{
    return PyLong_FromUnsignedLong(PyObjCObject_GetFlags(self));
}

static PyObject* _Nullable obj_get_blocksignature(PyObject* self, void* closure
                                                  __attribute__((__unused__)))
{
    if (PyObjCObject_IsBlock(self)) {
        PyObjCMethodSignature* v = PyObjCObject_GetBlockSignature(self);
        if (v != NULL) {
            Py_INCREF(v);
            return (PyObject*)v;
        } else {
            id objc_self = PyObjCObject_GetObject(self);
            assert(objc_self != nil);

            const char* typestr = PyObjCBlock_GetSignature(objc_self);
            if (typestr != NULL) {
                v = PyObjCMethodSignature_WithMetaData(typestr, NULL, YES);
                if (v == NULL) {
                    return NULL;
                }
                PyObjCMethodSignature* result = PyObjCObject_SetBlockSignature(self, v);
                Py_DECREF(v);
                return (PyObject*)result;
            }
        }
    }

    Py_RETURN_NONE;
}

static int
obj_set_blocksignature(PyObject* self, PyObject* _Nullable newVal,
                       void*     closure __attribute__((__unused__)))
{
    if (newVal == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete '__block_signature__'");
        return -1;
    }
    if (!PyObjCObject_IsBlock(self)) {
        PyErr_SetString(PyExc_TypeError,
                        "'__block_signature__' can only be set on Block objects");
        return -1;
    }

    if (!PyObjCMethodSignature_Check(newVal)) {
        PyErr_SetString(PyExc_TypeError, "New value must be a method signature");
        return -1;
    }

    PyObjCMethodSignature* result =
        PyObjCObject_SetBlockSignature(self, (PyObjCMethodSignature*)newVal);
    Py_DECREF(newVal);
    Py_XDECREF(result);
    if (result != NULL && newVal != (PyObject*)result) {
        PyErr_SetString(PyObjCExc_Error, "Cannot reset __block_signature__");
        return -1;
    }
    return result != NULL ? 0 : -1;
}

static PyGetSetDef obj_getset[] = {{
                                       .name = "pyobjc_ISA",
                                       .get  = objc_get_real_class,
                                       .doc  = objc_get_real_class_doc,
                                   },
                                   {
                                       .name = "pyobjc_instanceMethods",
                                       .get  = obj_get_instanceMethods,
                                       .doc  = obj_get_instanceMethods_doc,
                                   },
                                   {
                                       .name = "__block_signature__",
                                       .get  = obj_get_blocksignature,
                                       .set  = obj_set_blocksignature,
                                       .doc  = "Call signature for a block, or None",
                                   },
                                   {
                                       .name = "__flags__",
                                       .get  = obj_get_flags,
                                   },
                                   {
                                       .name = NULL /* SENTINEL */
                                   }};

/*
 * We don't support pickling of Objective-C objects at the moment. The new
 * version 2 of the pickle protocol has a default pickle method for new-style
 * classes that doesn't work for us (it will write incomplete values to the
 * pickle). This method forces a failure during pickling.
 */
static PyObject* _Nullable meth_reduce(PyObject* self __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "Cannot pickle Objective-C objects");
    return NULL;
}

static PyObject* _Nullable meth_sizeof(PyObject* self __attribute__((__unused__)))
{
    /* Basis __sizeof__ implementation for Cocoa objects.
     * This doesn't return the correct size for collections (such as NSArray),
     * but is better than the default implementation
     */
    id objc_value = PyObjCObject_GetObject(self);
    assert(objc_value != nil);

    return PyLong_FromSize_t(Py_TYPE(self)->tp_basicsize
                             + class_getInstanceSize(object_getClass(objc_value)));
}

static PyObject*
meth_is_magic(PyObject* self)
{
    if (PyObjCObject_IsMagic(self)) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyObject* _Nullable as_cobject(PyObject* self)
{
    id self_value = PyObjCObject_OBJECT(self);
    assert(self_value != nil);

    return PyCapsule_New(self_value, "objc.__object__", NULL);
}

static PyObject* _Nullable as_ctypes_voidp(PyObject* self)
{
    id self_value = PyObjCObject_OBJECT(self);
    assert(self_value != nil);
    return PyObjC_MakeCVoidP(self_value);
}

/*
 * Implementation of __dir__, which is the hook used by dir() on python 2.6 or later.
 */
static PyObject* _Nullable meth_dir(PyObject* self)
{
    PyObject*    result;
    PyObject*    result_list;
    Class        cls;
    Method*      methods;
    unsigned int method_count, i;

    /* Start of with keys in __dict__ */
    PyObject* class_dict = Py_TYPE(self)->tp_dict;

    result = PySet_New(class_dict);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    PyObject** dictptr = _get_dictptr(self);
    if (dictptr != NULL && *dictptr != NULL) {
        PyObject* args[] = {NULL, result, *dictptr};
        PyObject* tmp    = PyObject_VectorcallMethod(
            PyObjCNM_update, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
        if (tmp == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_CLEAR(tmp);
    } // LCOV_BR_EXCL_LINE

    if (PyObjCObject_IsMagic(self)) {
        /* "magic cookie" objects don't have Objective-C methods */
        goto done;
    }

    cls = object_getClass(PyObjCObject_GetObject(self));
    while (cls != NULL) {
        /* Now add all instance method names */

        /* class_copyMethodList will only return NULL when it sets
         * method_count to 0
         */
        methods = (Method* _Nonnull)class_copyMethodList(cls, &method_count);
        for (i = 0; i < method_count; i++) {
            PyObject* item;
            SEL       sel;

            /* Check if the selector should be hidden */
            sel = method_getName(methods[i]);
            if (sel == NULL) // LCOV_BR_EXCL_LINE
                continue;    // LCOV_EXCL_LINE

            PyObject* hidden =
                PyObjCClass_HiddenSelector((PyObject*)Py_TYPE(self), sel, NO);
            if (hidden == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            } else if (hidden) {
                continue;
            }

            item = PyObjC_SELToPythonName(method_getName(methods[i]));
            if (item == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            if (PySet_Add(result, item) == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(methods);
                Py_DECREF(result);
                Py_DECREF(item);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(item);
        }
        free(methods);

        cls = class_getSuperclass(cls);
    }

done:
    result_list = PySequence_List(result);
    Py_CLEAR(result);
    return result_list;
}

static PyMethodDef obj_methods[] = {
    {.ml_name  = "__reduce__",
     .ml_meth  = (PyCFunction)meth_reduce,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Used for pickling"},
    {.ml_name  = "__cobject__",
     .ml_meth  = (PyCFunction)as_cobject,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Return a CObject representing this object"},
    {.ml_name  = "__c_void_p__",
     .ml_meth  = (PyCFunction)as_ctypes_voidp,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Return a ctypes.c_void_p representing this object"},
    {
        .ml_name  = "__sizeof__",
        .ml_meth  = (PyCFunction)meth_sizeof,
        .ml_flags = METH_NOARGS,
    },
    {
        .ml_name  = "__pyobjc_magic_coookie__",
        .ml_meth  = (PyCFunction)meth_is_magic,
        .ml_flags = METH_NOARGS,
    },
    {.ml_name  = "__dir__",
     .ml_meth  = (PyCFunction)meth_dir,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "dir() hook, don't call directly"},
    {
        .ml_name = NULL /* SENTINEL */
    }};

PyObjCClassObject PyObjCObject_Type = {
    .base = {
        .ht_type =
            {
                PyVarObject_HEAD_INIT(&PyObjCClass_Type, 0).tp_name = "objc.objc_object",
                .tp_basicsize = sizeof(PyObjCObject),
                .tp_itemsize  = 0,
                .tp_dealloc   = object_dealloc,
                .tp_repr      = object_repr,
                .tp_getattro  = object_getattro,
                .tp_setattro  = object_setattro,
                .tp_flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
                .tp_methods   = obj_methods,
                .tp_getset    = obj_getset,
                .tp_alloc     = PyType_GenericAlloc,
                .tp_new       = object_new,
                .tp_del       = (destructor)object_del,
                .tp_doc       = "objc_object()",
            },
    }};

/*
 *  Allocate a proxy object for use during the call of __del__,
 *  this isn't a full-featured proxy object.
 */
PyObject* _Nullable _PyObjCObject_NewDeallocHelper(id objc_object)
{
    PyObject*     res;
    PyTypeObject* cls_type;

    assert(objc_object != nil);
    cls_type =
        (PyTypeObject*)PyObjCClass_New((Class _Nonnull)object_getClass(objc_object));
    if (cls_type == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    res = cls_type->tp_alloc(cls_type, 0);
    Py_DECREF(cls_type);
    if (res == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    if (PyObjCClass_CheckMethodList((PyObject*)Py_TYPE(res), 1) < 0) {
        Py_DECREF(res);
        return NULL;
    }

    ((PyObjCObject*)res)->objc_object = objc_object;

    ((PyObjCObject*)res)->flags = PyObjCObject_kDEALLOC_HELPER;
    return res;
}

void
_PyObjCObject_FreeDeallocHelper(PyObject* obj)
{
#ifdef Py_GIL_DISABLED
    if (PyUnstable_Object_IsUniquelyReferenced(obj) != 1) {
#else
    if (Py_REFCNT(obj) != 1) {
#endif
        /* Someone revived this object. Objective-C doesn't like
         * this at all, therefore warn the user about this and
         * zero out the instance.
         */
        char buf[256];
        snprintf(buf, sizeof(buf),
                 "revived Objective-C object of type %s. Object is zero-ed out.",
                 Py_TYPE(obj)->tp_name);

        id objc_object = PyObjCObject_GetObject(obj);
        assert(objc_object != nil);

        PyObjC_UnregisterPythonProxy(objc_object, obj);

        /* Object is set to ``[NSNull null]`` to maintain the invariant */
        ((PyObjCObject*)obj)->objc_object = NSNull_null;

        if (PyErr_Warn(PyObjCExc_ObjCRevivalWarning, buf) == -1) {
            PyErr_WriteUnraisable(obj);
        }
    }
    Py_DECREF(obj);
}

PyObject* _Nullable PyObjCObject_New(id objc_object, int flags, int retain)
{
    assert(objc_object != nil);

    /* object_getClass only returns Nil if its argument is nil */
    Class         cls = (Class _Nonnull)object_getClass(objc_object);
    PyTypeObject* cls_type;
    PyObject*     res;

    if ((flags & PyObjCObject_kNEW_WRAPPER) == 0) {
        res = PyObjC_FindPythonProxy(objc_object);
        if (res)
            return res;
    } else {
        flags &= ~PyObjCObject_kNEW_WRAPPER;
    }

    cls_type = (PyTypeObject*)PyObjCClass_New(cls);
    if (cls_type == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (!PyErr_Occurred()) {
            PyErr_Format(PyObjCExc_Error, "Cannot find python proxy for class '%s'",
                         class_getName(cls));
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    res = cls_type->tp_alloc(cls_type, 0);
    Py_DECREF(cls_type);
    if (res == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    if (cls_type->tp_basicsize == sizeof(PyObjCBlockObject)) {
        flags |= PyObjCObject_kBLOCK;
    }

    /* This should be in the tp_alloc for the new class, but
     * adding a tp_alloc to PyObjCClass_Type doesn't seem to help
     */
    if (PyObjCClass_CheckMethodList((PyObject*)Py_TYPE(res), 1) < 0) {
        Py_DECREF(res);
        return NULL;
    }

    ((PyObjCObject*)res)->objc_object = objc_object;
    ((PyObjCObject*)res)->flags       = flags;

    if (flags & PyObjCObject_kBLOCK) {
        ((PyObjCBlockObject*)res)->signature = NULL;
    }

    if (retain) {
        if (object_getClass(objc_object) != NSAutoreleasePool_class) {
            /* NSAutoreleasePool doesn't like retain */
            [objc_object retain];
        }
    }

    /*
     * Don't register if we use the default flags, other parts will do
     * that if necessary. I don't like this, but don't want to pollute
     * the interface of this function with yet another argument.
     */
    if (flags != PyObjCObject_kDEFAULT) {
        PyObject* actual = PyObjC_RegisterPythonProxy(objc_object, res);
        Py_DECREF(res);
        return actual;
    }
    return res;
}

PyObject* _Nullable PyObjCObject_FindSelector(PyObject* object, SEL selector)
{
    return PyObjCClass_FindSelector((PyObject*)Py_TYPE(object), selector, NO);
}

id
PyObjCObject_GetObject(PyObject* object)
{
    id result = PyObjCObject_OBJECT(object);
    return result;
}

unsigned int
PyObjCObject_GetFlags(PyObject* object)
{
    unsigned int result = PyObjCObject_FLAGS(object);
    assert((result & ~PyObjCObject_kALL_FLAGS) == 0);
    return result;
}

bool
PyObjCObject_IsBlock(PyObject* object)
{
    assert(PyObjCObject_Check(object));
    return (PyObjCObject_FLAGS(object) & PyObjCObject_kBLOCK) != 0;
}

bool
PyObjCObject_IsMagic(PyObject* object)
{
    assert(PyObjCObject_Check(object));
    return (PyObjCObject_FLAGS(object) & PyObjCObject_kMAGIC_COOKIE) != 0;
}

PyObjCMethodSignature* _Nullable PyObjCObject_GetBlockSignature(PyObject* object)
{
    PyObjCMethodSignature* result;
    assert(PyObjCObject_IsBlock(object));
    Py_BEGIN_CRITICAL_SECTION(object);
    result = (((PyObjCBlockObject*)(object))->signature);
    Py_XINCREF(result);
    Py_END_CRITICAL_SECTION();
    return result;
}

PyObjCMethodSignature*
PyObjCObject_SetBlockSignature(PyObject* object, PyObjCMethodSignature* methinfo)
{
    assert(PyObjCObject_IsBlock(object));
    PyObjCMethodSignature* result;

    Py_BEGIN_CRITICAL_SECTION(object);
    result = ((PyObjCBlockObject*)(object))->signature;
    if (result == NULL) {
        SET_FIELD_INCREF(((PyObjCBlockObject*)(object))->signature, methinfo);
        result = methinfo;
    }
    Py_INCREF(result);
    Py_END_CRITICAL_SECTION();
    return result;
}

PyObject* _Nullable PyObjCObject_GetAttrString(PyObject* obj, char* name)
{
    PyObject* pyname = PyUnicode_FromString(name);
    if (pyname == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_START

    PyObject* rv = object_getattro(obj, pyname);
    Py_DECREF(pyname);
    return rv;
}

NS_ASSUME_NONNULL_END
