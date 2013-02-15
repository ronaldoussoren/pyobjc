/*
 * Implementation of 'native' and 'python' selectors
 */
#include "pyobjc.h"

#include "compile.h" /* from Python */
#include "opcode.h"

#include <objc/Object.h>

static Class Object_class = nil;

static char* pysel_default_signature(PyObject* callable);
static PyObject* pysel_new(PyTypeObject* type, PyObject* args, PyObject* kwds);

/*
 * Base type for objective-C selectors
 *
 * selectors are callable objects with the following attributes:
 * - 'signature': The objective-C signature of the method
 * - 'selector':  The name in the objective-C runtime
 */

PyObjCMethodSignature*
PyObjCSelector_GetMetadata(PyObject* _self)
{
    PyObjCSelector* self = (PyObjCSelector*)_self;

    if (self->sel_methinfo == NULL) {
        self->sel_methinfo = PyObjCMethodSignature_ForSelector(
            self->sel_class,
            (self->sel_flags & PyObjCSelector_kCLASS_METHOD) != 0,
            self->sel_selector,
            self->sel_python_signature,
            PyObjCNativeSelector_Check(self)
        );

        if (self->sel_methinfo == NULL) return NULL;

        if (PyObjCPythonSelector_Check(_self)) {
            Py_ssize_t i;

            ((PyObjCPythonSelector*)_self)->numoutput = 0;
            for (i = 0; i < Py_SIZE(((PyObjCPythonSelector*)_self)->sel_methinfo); i++) {
                if (((PyObjCPythonSelector*)_self)->sel_methinfo->argtype[i].type[0] == _C_OUT) {
                    ((PyObjCPythonSelector*)_self)->numoutput ++;
                }
            }
        }
    }

    return self->sel_methinfo;
}


PyDoc_STRVAR(sel_metadata_doc, "Return a dict that describes the metadata for this method, including metadata for the 2 hidden ObjC parameters (self and _sel) ");
static PyObject* sel_metadata(PyObject* self)
{
    PyObject* result = PyObjCMethodSignature_AsDict(PyObjCSelector_GetMetadata(self));
    int r;

    r = PyDict_SetItemString(result, "classmethod",
        (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kCLASS_METHOD) ? Py_True : Py_False);
    if (r == -1) {
        Py_DECREF(result);
        return NULL;
    }

    r = PyDict_SetItemString(result, "hidden",
            (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kHIDDEN) ? Py_True : Py_False);

    if (r == -1) {
        Py_DECREF(result);
        return NULL;
    }

    if (((PyObjCSelector*)self)->sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
        r = PyDict_SetItemString(result, "return_uninitialized_object", Py_True);
        if (r == -1) {
            Py_DECREF(result);
            return NULL;
        }
    }
    return result;
}

static PyMethodDef sel_methods[] = {
    {
          "__metadata__",
              (PyCFunction)sel_metadata,
              METH_NOARGS,
          sel_metadata_doc
    },
    { 0, 0, 0, 0 }
};


PyDoc_STRVAR(base_self_doc, "'self' object for bound methods, None otherwise");

static PyObject*
base_self(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    if (self->sel_self) {
        Py_INCREF(self->sel_self);
        return self->sel_self;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(base_signature_doc, "Objective-C signature for the method");

static PyObject*
base_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    return PyBytes_FromString(self->sel_python_signature);
}


PyDoc_STRVAR(base_native_signature_doc, "original Objective-C signature for the method");

static PyObject*
base_native_signature(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    if (self->sel_native_signature == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyBytes_FromString(self->sel_native_signature);
}

static int
base_signature_setter(PyObject* _self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    char* t;
    if (!PyBytes_Check(newVal)) {
        PyErr_SetString(PyExc_TypeError, "signature must be byte string");
        return -1;
    }

    t = PyObjCUtil_Strdup(PyBytes_AsString(newVal));
    if (t == NULL) {
        PyErr_NoMemory();
        return -1;
    }

    PyMem_Free((char*)self->sel_python_signature);
    self->sel_python_signature = t;
    return 0;
}

PyDoc_STRVAR(base_hidden_doc, "If True the method is not directly accessible as an object attribute");

static PyObject*
base_hidden(PyObject* _self, void* closure __attribute__((__unused__)))
{
    return PyBool_FromLong(((PyObjCSelector*)_self)->sel_flags & PyObjCSelector_kHIDDEN);
}
static int
base_hidden_setter(PyObject* _self, PyObject* newVal, void* closure __attribute__((__unused__)))
{
    if (PyObject_IsTrue(newVal)) {
        ((PyObjCSelector*)_self)->sel_flags |= PyObjCSelector_kHIDDEN;
    } else {
        ((PyObjCSelector*)_self)->sel_flags &= ~PyObjCSelector_kHIDDEN;
    }
    return 0;
}

PyDoc_STRVAR(base_selector_doc, "Objective-C name for the method");

static PyObject*
base_selector(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    return PyBytes_FromString(sel_getName(self->sel_selector));
}

PyDoc_STRVAR(base_name_doc, "Name for the method");

static PyObject*
base_name(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCSelector* self = (PyObjCSelector*)_self;
    char buf[2048];
    const char* name;

    name = PyObjC_SELToPythonName(
        self->sel_selector, buf, sizeof(buf));

    return PyText_FromString(name);
}

PyDoc_STRVAR(base_class_doc, "Objective-C Class that defines the method");
static PyObject*
base_class(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    if (self->sel_class != nil) {
        return PyObjCClass_New(self->sel_class);
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(base_class_method_doc,
    "True if this is a class method, False otherwise");

static PyObject*
base_class_method(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    return PyBool_FromLong(0 != (self->sel_flags & PyObjCSelector_kCLASS_METHOD));
}

PyDoc_STRVAR(base_required_doc,
    "True if this is a required method, False otherwise");

static PyObject*
base_required(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    return PyBool_FromLong(0 != (self->sel_flags & PyObjCSelector_kREQUIRED));
}

static PyGetSetDef base_getset[] = {
    {
        "isHidden",
        base_hidden,
        base_hidden_setter,
        base_hidden_doc,
        0
    },
    {
        "isRequired",
        base_required,
        0,
        base_required_doc,
        0
    },
    {
        "isClassMethod",
        base_class_method,
        0,
        base_class_method_doc,
        0
    },
    {
        "definingClass",
        base_class,
        0,
        base_class_doc,
        0
    },
    {
        "__objclass__",
        base_class,
        0,
        base_class_doc,
        0
    },
    {
        "signature",
        base_signature,
        base_signature_setter,
        base_signature_doc,
        0
    },
    {
        "native_signature",
        base_native_signature,
        0,
        base_native_signature_doc,
        0
    },
    {
        "self",
        base_self,
        0,
        base_self_doc,
        0
    },
    {
        "selector",
        base_selector,
        0,
        base_selector_doc,
        0
    },
    {
        "__name__",
        base_name,
        0,
        base_name_doc,
        0
    },
    { 0, 0, 0, 0, 0 }
};

static void
sel_dealloc(PyObject* object)
{
    PyObjCSelector* self = (PyObjCSelector*)object;
    Py_CLEAR(self->sel_methinfo);

    PyMem_Free((char*)self->sel_python_signature);
    self->sel_python_signature = NULL;

    if (self->sel_native_signature != NULL) {
        PyMem_Free((char*)self->sel_native_signature);
        self->sel_native_signature = NULL;
    }
    Py_CLEAR(self->sel_self);
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(base_selector_type_doc,
"selector(function, [, selector] [, signature] [, isClassMethod=0]\n"
"    [, isRequired=True]) -> selector\n"
"\n"
"Return an Objective-C method from a function. The other arguments \n"
"specify attributes of the Objective-C method.\n"
"\n"
"function:\n"
"  A function object with at least one argument. The first argument will\n"
"  be used to pass 'self'. This argument may be None when defining an\n"
"  informal_protocol object. The function must not be a ``staticmethod``\n"
"  instance. \n"
"\n"
"selector:\n"
"  The name of the Objective-C method. The default value of this\n"
"  attribute is the name of the function, with all underscores replaced\n"
"  by colons.\n"
"\n"
"signature:\n"
"  Method signature for the Objective-C method. This should be a raw\n"
"  Objective-C method signature, including specifications for 'self' and\n"
"  '_cmd'. The default value a signature that describes a method with\n"
"  arguments of type 'id' and a return-value of the same type.\n"
"\n"
"isClassMethod:\n"
"  True if the method is a class method, false otherwise. The default is \n"
"  False, unless the function is an instance of ``classmethod``.\n"
"\n"
"isRequired:\n"
"  True if this is a required method in an informal protocol, False\n"
"  otherwise. The default value is 'True'. This argument is only used\n"
"  when defining an 'informal_protocol' object.\n"
);
PyTypeObject PyObjCSelector_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.selector",
    .tp_basicsize   = sizeof(PyObjCSelector),
    .tp_itemsize    = 0,
    .tp_dealloc     = sel_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = base_selector_type_doc,
    .tp_methods     = sel_methods,
    .tp_getset      = base_getset,
    .tp_new         = pysel_new,
};


/*
 * Selector type for 'native' selectors (that is, selectors that are not
 * implemented as python methods)
 */
static PyObject*
objcsel_repr(PyObject* _self)
{
    PyObjCNativeSelector* sel = (PyObjCNativeSelector*)_self;
    PyObject *rval;
    if (sel->sel_self == NULL) {
        rval = PyText_FromFormat("<unbound native-selector %s in %s>", sel_getName(sel->sel_selector), class_getName(sel->sel_class));

    } else {
#if PY_MAJOR_VERSION == 2
        PyObject* selfrepr = PyObject_Repr(sel->sel_self);
        if (selfrepr == NULL) {
            return NULL;
        }

        if (!PyString_Check(selfrepr)) {
            Py_DECREF(selfrepr);
            return NULL;
        }

        rval = PyText_FromFormat("<native-selector %s of %s>", sel_getName(sel->sel_selector), PyString_AS_STRING(selfrepr));
        Py_DECREF(selfrepr);

#else
        rval = PyUnicode_FromFormat("<native-selector %s of %R>", sel_getName(sel->sel_selector),
                    sel->sel_self);
#endif
    }

    return rval;
}

static PyObject* objcsel_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCNativeSelector_Check(a) && PyObjCNativeSelector_Check(b)) {

            PyObjCNativeSelector* sel_a = (PyObjCNativeSelector*)a;
            PyObjCNativeSelector* sel_b = (PyObjCNativeSelector*)b;
            int same = 1;

            if (sel_a->sel_selector != sel_b->sel_selector) {
                same = 0;
            }
            if (sel_a->sel_class != sel_b->sel_class) {
                same = 0;
            }
            if (sel_a->sel_self != sel_b->sel_self) {
                same = 0;
            }
            if ((op == Py_EQ && !same) || (op == Py_NE && same)) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }

        } else {
            if (op == Py_EQ) {
                Py_INCREF(Py_False);
                return Py_False;

            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }
        }

    } else {
        PyErr_SetString(PyExc_TypeError, "Cannot use '<', '<=', '>=' and '>' with objc.selector");
        return NULL;
    }
}


static PyObject*
objcsel_call(PyObject* _self, PyObject* args, PyObject* kwds)
{
    PyObjCNativeSelector* self = (PyObjCNativeSelector*)_self;
    PyObject* pyself = self->sel_self;
    PyObjC_CallFunc execute = NULL;
    PyObject* res;
    PyObject* pyres;

    if (kwds != NULL && PyObject_Size(kwds) != 0) {
        PyErr_SetString(PyExc_TypeError,
            "Objective-C selectorrs don't support keyword arguments");
        return NULL;
    }

    if (pyself == NULL) {
        Py_ssize_t argslen;
        argslen = PyTuple_Size(args);
        if (argslen < 1) {
            PyErr_SetString(PyExc_TypeError,
                "Missing argument: self");
            return NULL;
        }

        pyself = PyTuple_GET_ITEM(args, 0);
        if (pyself == NULL) {
            return NULL;
        }
    }

    if (self->sel_call_func) {
        execute = self->sel_call_func;
    } else {
        execute = PyObjC_FindCallFunc(
                self->sel_class,
                self->sel_selector);
        if (execute == NULL) return NULL;
        self->sel_call_func = execute;
    }

    if (self->sel_self != NULL) {
        pyres = res = execute((PyObject*)self, self->sel_self, args);
        if (pyres != NULL
                && PyTuple_Check(pyres)
                && PyTuple_GET_SIZE(pyres) >= 1
                && PyTuple_GET_ITEM(pyres, 0) == pyself) {

            pyres = pyself;
        }

        if (PyObjCObject_Check(self->sel_self) && (((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED)) {
            if (self->sel_self != pyres && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(self->sel_self);
            }
        }

    } else {
        PyObject* arglist;
        PyObject* myClass;
        Py_ssize_t i;
        Py_ssize_t argslen;

        argslen = PyTuple_Size(args);
        arglist = PyTuple_New(argslen - 1);

        for (i = 1; i < argslen; i++) {
            PyObject* v = PyTuple_GET_ITEM(args, i);
            if (v == NULL) {
                Py_DECREF(arglist);
                return NULL;
            }

            PyTuple_SET_ITEM(arglist, i-1, v);
            Py_INCREF(v);
        }

        myClass = PyObjCClass_New(self->sel_class);
        if (!(PyObject_IsInstance(pyself, myClass)
#if PY_MAJOR_VERSION == 2
            || (PyString_Check(pyself) && class_isSubclassOf(self->sel_class, [NSString class]))
#endif
            || (PyUnicode_Check(pyself) && class_isSubclassOf(self->sel_class, [NSString class]))
        )) {

            Py_DECREF(arglist);
            Py_DECREF(myClass);
            PyErr_Format(PyExc_TypeError,
                "Expecting instance of %s as self, got one "
                "of %s", class_getName(self->sel_class),
                Py_TYPE(pyself)->tp_name);
            return NULL;
        }
        Py_DECREF(myClass);

        pyres = res = execute((PyObject*)self, pyself, arglist);
        if (pyres != NULL
            && PyTuple_Check(pyres)
            && PyTuple_GET_SIZE(pyres) > 1
            && PyTuple_GET_ITEM(pyres, 0) == pyself) {
            pyres = pyself;
        }

        if (PyObjCObject_Check(pyself) && (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED)) {
            if (pyself != pyres && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(pyself);
            }
        }

        Py_DECREF(arglist);
    }

    if (pyres && PyObjCObject_Check(pyres)) {
        if (self->sel_flags & PyObjCSelector_kRETURNS_UNINITIALIZED) {
            ((PyObjCObject*)pyres)->flags |= PyObjCObject_kUNINITIALIZED;
        } else if (((PyObjCObject*)pyself)->flags & PyObjCObject_kUNINITIALIZED) {
            ((PyObjCObject*)pyself)->flags &=
                ~PyObjCObject_kUNINITIALIZED;
            if (self->sel_self && self->sel_self != pyres && !PyErr_Occurred()) {
                PyObjCObject_ClearObject(self->sel_self);
            }
        }
    }

    return res;
}

static PyObject*
objcsel_descr_get(PyObject* _self, PyObject* volatile obj, PyObject* class)
{
    PyObjCNativeSelector* meth = (PyObjCNativeSelector*)_self;
    PyObjCNativeSelector* result;

    if (meth->sel_self != NULL || obj == Py_None) {
        Py_INCREF(meth);
        return (PyObject*)meth;
    }

    if (class != nil && PyType_Check(class) && PyType_IsSubtype((PyTypeObject*)class, &PyObjCClass_Type)) {
        class = PyObjCClass_ClassForMetaClass(class);
    }

    /* Bind 'self' */
    if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
        obj = class;
    } else {
        if (obj && PyObjCClass_Check(obj)) {
            obj = NULL;
        }
    }
    result = PyObject_New(PyObjCNativeSelector, &PyObjCNativeSelector_Type);
    result->sel_selector   = meth->sel_selector;
    result->sel_python_signature  = PyObjCUtil_Strdup(meth->sel_python_signature);
    if (result->sel_python_signature == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    if (meth->sel_native_signature != NULL) {
        result->sel_native_signature = PyObjCUtil_Strdup(meth->sel_native_signature);
        if (result->sel_native_signature == NULL) {
            Py_DECREF(result);
            return NULL;
        }
    } else {
        result->sel_native_signature = NULL;
    }

    result->sel_flags = meth->sel_flags;
    result->sel_class = meth->sel_class;

    if (meth->sel_call_func == NULL) {
        if (class_isMetaClass(meth->sel_class)) {
            PyObject* metaclass_obj = PyObjCClass_New(meth->sel_class);
            PyObject* class_obj = PyObjCClass_ClassForMetaClass(metaclass_obj);
            Py_CLEAR(metaclass_obj);

            meth->sel_call_func = PyObjC_FindCallFunc(PyObjCClass_GetClass(class_obj),
                meth->sel_selector);
            Py_CLEAR(class_obj);

        } else {
            meth->sel_call_func = PyObjC_FindCallFunc(meth->sel_class,
                meth->sel_selector);
        }
    }
    result->sel_call_func = meth->sel_call_func;

    result->sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
    if (result->sel_methinfo) {
        Py_INCREF(result->sel_methinfo);
    } else {
        PyErr_Clear();
    }

    result->sel_self = obj;
    if (result->sel_self) {
        Py_INCREF(result->sel_self);
    }

    return (PyObject*)result;
}

static PyGetSetDef objcsel_getset[] = {
    {
        "__doc__",
        PyObjC_callable_docstr_get,
        0,
        "The document string for a method",
        0
    },
#if PY_VERSION_HEX >= 0x03030000
    {
        "__signature__",
        PyObjC_callable_signature_get,
        0,
        "inspect.Signature for a method",
        0
    },
#endif
    { 0, 0, 0, 0, 0 }
};


PyTypeObject PyObjCNativeSelector_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name = "objc.native_selector",
    .tp_basicsize = sizeof(PyObjCNativeSelector),
    .tp_itemsize = 0,
    .tp_dealloc = sel_dealloc,
    .tp_repr = objcsel_repr,
    .tp_call = objcsel_call,
    .tp_getattro = PyObject_GenericGetAttr,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_richcompare = objcsel_richcompare,
    .tp_getset = objcsel_getset,
    .tp_base = &PyObjCSelector_Type,
    .tp_descr_get = objcsel_descr_get,
};

PyObject*
PyObjCSelector_FindNative(PyObject* self, const char* name)
{
    SEL sel = PyObjCSelector_DefaultSelector(name);
    PyObject* retval;

    NSMethodSignature* methsig;
    char buf[2048];

    if (PyObjCObject_Check(self)) {
        if (PyObjCClass_HiddenSelector((PyObject*)Py_TYPE(self), sel, NO)) {
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            return NULL;
        }

    } else {
        if (PyObjCClass_HiddenSelector(self, sel, YES)) {
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            return NULL;
        }
    }

    if (Object_class == nil) {
        Object_class = objc_getClass("Object");
    }

    if (name[0] == '_' && name[1] == '_') {
        /* No known Objective-C class has methods whose name
         * starts with '__' or '_:'. This allows us to shortcut
         * lookups for special names, which speeds up tools like
         * pydoc.
         */
        PyErr_Format(PyExc_AttributeError,
            "No attribute %s", name);
        return NULL;
    }

    if (PyObjCClass_Check(self)) {
        Class cls = PyObjCClass_GetClass(self);

        if (!cls) {
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            return NULL;
        }

        if (strcmp(class_getName(cls), "_NSZombie") == 0) {
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            return NULL;
        }

        if (strcmp(class_getName(cls), "NSProxy") == 0) {
            if (sel == @selector(methodSignatureForSelector:)) {
                PyErr_Format(PyExc_AttributeError,
                    "Accessing NSProxy.%s is not supported",
                    name);
                return NULL;
            }
        }


        NS_DURING
            if ([cls respondsToSelector:sel]) {
                methsig = [cls methodSignatureForSelector:sel];
                retval = PyObjCSelector_NewNative(cls, sel,
                    PyObjC_NSMethodSignatureToTypeString(methsig, buf, sizeof(buf)), 1);
            } else if ((Object_class != nil) && (cls != Object_class) && nil != (methsig = [(NSObject*)cls methodSignatureForSelector:sel])) {
                retval = PyObjCSelector_NewNative(cls, sel,
                    PyObjC_NSMethodSignatureToTypeString(
                        methsig, buf, sizeof(buf)), 1);
            } else {
                PyErr_Format(PyExc_AttributeError,
                    "No attribute %s", name);
                retval = NULL;
            }

        NS_HANDLER
            PyObjCErr_FromObjC(localException);
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            retval = NULL;

        NS_ENDHANDLER

        return retval;

    } else if (PyObjCObject_Check(self)) {
        id object;

        object = PyObjCObject_GetObject(self);

        NS_DURING
            if (nil != (methsig = [object methodSignatureForSelector:sel])){
                PyObjCNativeSelector* res;

                res =  (PyObjCNativeSelector*)PyObjCSelector_NewNative(
                    object_getClass(object), sel,
                    PyObjC_NSMethodSignatureToTypeString(methsig,
                        buf, sizeof(buf)), 0);
                if (res != NULL) {
                    /* Bind the method to self */
                    res->sel_self = self;
                    Py_INCREF(res->sel_self);
                }
                retval = (PyObject*)res;
            } else {
                PyErr_Format(PyExc_AttributeError,
                    "No attribute %s", name);
                retval = NULL;
            }

        NS_HANDLER
            PyErr_Format(PyExc_AttributeError,
                "No attribute %s", name);
            retval = NULL;

        NS_ENDHANDLER

        return retval;

    } else {
        PyErr_SetString(PyExc_RuntimeError,
            "PyObjCSelector_FindNative called on plain "
            "python object");
        return NULL;
    }
}


PyObject*
PyObjCSelector_NewNative(Class class,
            SEL selector, const char* signature, int class_method)
{
    PyObjCNativeSelector* result;
    const char* native_signature = signature;

    if (signature == NULL) {
        PyErr_Format(PyExc_RuntimeError,
            "PyObjCSelector_NewNative: nil signature for %s", sel_getName(selector));
        return NULL;
    }

    result = PyObject_New(PyObjCNativeSelector, &PyObjCNativeSelector_Type);
    if (result == NULL) return NULL;

    result->sel_selector = selector;
    result->sel_python_signature = PyObjCUtil_Strdup(signature);
    result->sel_native_signature = PyObjCUtil_Strdup(native_signature);
    if (result->sel_python_signature == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    result->sel_self = NULL;
    result->sel_class = class;
    result->sel_call_func = NULL;
    result->sel_methinfo = NULL;
    result->sel_flags = 0;
    if (class_method) {
        result->sel_flags |= PyObjCSelector_kCLASS_METHOD;
    }
    if (sel_isEqual(selector, @selector(alloc)) || sel_isEqual(selector, @selector(allocWithZone:))) {
          result->sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
    }
    result->sel_call_func = NULL;
    return (PyObject*)result;
}


static char gSheetMethodSignature[] = { _C_VOID, _C_ID, _C_SEL, _C_ID, _C_INT, _C_PTR , _C_VOID, 0 };

PyObject*
PyObjCSelector_New(PyObject* callable,
    SEL selector, const char* signature, int class_method, Class cls)
{
    PyObjCPythonSelector* result;
    if (signature == NULL) {
        const char* selname = sel_getName(selector);
        size_t len = strlen(selname);
        if (len > 30 && strcmp(selname+len-30, "DidEnd:returnCode:contextInfo:") == 0) {
            signature = PyObjCUtil_Strdup(gSheetMethodSignature);
        } else {
            signature = pysel_default_signature(callable);
        }
    } else {
        signature = PyObjCUtil_Strdup(signature);
    }
    if (signature == NULL) return NULL;

    result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
    if (result == NULL) return NULL;

    result->sel_selector = selector;
    result->sel_python_signature = signature;
    result->sel_native_signature = PyObjCUtil_Strdup(signature);
    if (result->sel_native_signature == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    PyObjC_RemoveInternalTypeCodes((char*)result->sel_native_signature);

    result->sel_self = NULL;
    result->sel_class = cls;
    result->sel_flags = 0;
    result->sel_methinfo = NULL; /* We might not know the class right now */

    if (PyObjCPythonSelector_Check(callable)) {
        callable = ((PyObjCPythonSelector*)callable)->callable;
    }

    if (PyFunction_Check(callable)) {
        result->argcount = ((PyCodeObject*)PyFunction_GetCode(callable))->co_argcount;

    } else if (PyMethod_Check(callable)) {
        if (PyMethod_Self(callable) == NULL) {
            result->argcount = ((PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable)))->co_argcount;

        } else {
            result->argcount = ((PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable)))->co_argcount - 1;
        }

    } else if (callable == Py_None) {
        result->argcount = 0;

    } else {
        /* XXX: Should not happen... */
        result->argcount = 0;
        const char* s = sel_getName(selector);
        while ((s = strchr(s, ':')) != NULL) {
            result->argcount++;
            s++;
        }
    }

    if (class_method) {
        result->sel_flags |= PyObjCSelector_kCLASS_METHOD;
    }
    if (sel_isEqual(selector, @selector(alloc)) || sel_isEqual(selector, @selector(allocWithZone:))) {
          result->sel_flags |= PyObjCSelector_kRETURNS_UNINITIALIZED;
    }

    result->callable = callable;
    Py_INCREF(result->callable);

    return (PyObject*)result;
}


/*
 * Selector type for python selectors (that is, selectors that are
 * implemented as python methods)
 *
 * This one can be allocated from python code.
 */

static long
pysel_hash(PyObject* o)
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)o;
    long h = 0;

    if (self->sel_self) {
        h ^= PyObject_Hash(self->sel_self);
    }
    h ^= (long)(self->sel_class);
    h ^= PyObject_Hash(self->callable);

    return h;
}


static PyObject*
pysel_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCPythonSelector_Check(a) && PyObjCPythonSelector_Check(b)) {
            PyObjCPythonSelector* sel_a = (PyObjCPythonSelector*)a;
            PyObjCPythonSelector* sel_b = (PyObjCPythonSelector*)b;
            int same = 1;
            int r;

            if (sel_a->sel_selector != sel_b->sel_selector) {
                same = 0;
            }
            if (sel_a->sel_class != sel_b->sel_class) {
                same = 0;
            }
            if (sel_a->sel_self != sel_b->sel_self) {
                same = 0;
            }
            r = PyObject_RichCompareBool(
                    sel_a->callable,
                    sel_b->callable, Py_EQ);
            if (r == -1) {
                return NULL;
            }
            if (!r) {
                same = 0;
            }

            if ((op == Py_EQ && !same) || (op == Py_NE && same)) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }

        } else {
            if (op == Py_EQ) {
                Py_INCREF(Py_False);
                return Py_False;
            } else {
                Py_INCREF(Py_False);
                return Py_True;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "Cannot use '<', '<=', '>=' and '>' with objc.selector");
        return NULL;
    }
}

static PyObject*
pysel_repr(PyObject* _self)
{
    PyObjCPythonSelector* sel = (PyObjCPythonSelector*)_self;
    PyObject *rval;

    if (sel->sel_self == NULL) {
        if (sel->sel_class) {
            rval = PyText_FromFormat("<unbound selector %s of %s at %p>", sel_getName(sel->sel_selector), class_getName(sel->sel_class), sel);

        } else {
            rval = PyText_FromFormat("<unbound selector %s at %p>", sel_getName(sel->sel_selector), sel);
        }

    } else {
#if PY_MAJOR_VERSION == 2
        PyObject* selfrepr = PyObject_Repr(sel->sel_self);
        if (selfrepr == NULL) {
            return NULL;
        }

        if (!PyString_Check(selfrepr)) {
            Py_DECREF(selfrepr);
            return NULL;
        }

        rval = PyText_FromFormat("<selector %s of %s>", sel_getName(sel->sel_selector), PyString_AS_STRING(selfrepr));
        Py_DECREF(selfrepr);

#else
        rval = PyText_FromFormat("<selector %s of %R>", sel_getName(sel->sel_selector), sel->sel_self);
#endif
    }
    return rval;
}


/*
 * Calling the method from Python is sligtly complicated by the fact that
 * output arguments are optionally present (both in the method signature
 * and the actual argument list).
 *
 * pysel_call needs to compensate for this, which is done by this function.
 */
static PyObject*
compensate_arglist(PyObject* _self, PyObject* args, PyObject* kwds)
{
    /* XXX: need to do a full metadata processing run here to get exactly the right
     * semantics, we also have to do a metadata run on the result!
     */
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
    BOOL argsmatch;
    Py_ssize_t i;
    Py_ssize_t first_arg;

    if (self->sel_methinfo == NULL) {
        /* Make sure we actually have metadata */
        PyObjCSelector_GetMetadata(_self);
    }
    if (self->numoutput == 0) {
        Py_INCREF(args);
        return args;
    }

    if (kwds && PyDict_Size(kwds) != 0) {
        /* XXX: we cannot do anything here without reimplementing Python's argument
         * matching code...
         */
        Py_INCREF(args);
        return args;
    }

    argsmatch = ((PyTuple_Size(args) + (self->sel_self?1:0)) == self->argcount);

    first_arg = self->sel_self ? 0 : 1;

    if (self->argcount == Py_SIZE(self->sel_methinfo)-1) { /* the selector has an implicit '_sel' argument as well */
        /* All arguments are present, including output arguments */
        if (argsmatch) {
            for (i = 2; i < Py_SIZE(self->sel_methinfo); i++) {
                if (self->sel_methinfo->argtype[i].type[0] == _C_OUT) {
                    PyObject* a = PyTuple_GET_ITEM(args, first_arg + i - 2);
                    if (a != Py_None && a != PyObjC_NULL) {
                        PyErr_Format(PyExc_TypeError,
                            "argument %" PY_FORMAT_SIZE_T "d is an output argument but is passed a value other than None or objc.NULL (%s)",
                            i-1-first_arg, PyObject_REPR(args));
                        return NULL;
                    }
                }
            }
            Py_INCREF(args);
            return args;

        } else {
            if ((PyTuple_Size(args) + (self->sel_self?1:0)) != (self->argcount - self->numoutput)) {
                /* There's the wrong number of arguments */
                PyErr_Format(PyExc_TypeError,
                    "expecting %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d", self->argcount - (self->sel_self?1:0), PyTuple_Size(args));
                return NULL;
            }

            PyObject* real_args;
            Py_ssize_t pyarg;


            real_args = PyTuple_New(self->argcount - (self->sel_self?1:0));
            if (real_args == NULL) {
                return NULL;
            }

            pyarg = 0;
            if (self->sel_self == NULL) {
                pyarg = 1;
                PyTuple_SET_ITEM(real_args, 0, PyTuple_GET_ITEM(args, 0));
                Py_INCREF(PyTuple_GET_ITEM(args, 0));
            }

            PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(_self);
            for (i = 2; i < Py_SIZE(methinfo); i++) {
                if (methinfo->argtype[i].type[0] == _C_OUT) {
                    PyTuple_SET_ITEM(real_args, i-2+first_arg, Py_None);
                    Py_INCREF(Py_None);
                } else {
                    PyTuple_SET_ITEM(real_args, i-2+first_arg, PyTuple_GET_ITEM(args, pyarg));
                    Py_INCREF(PyTuple_GET_ITEM(args, pyarg));
                    pyarg++;
                }
            }

            return real_args;
        }

    } else {
        /* Not all arguments are present, output arguments should
         * be excluded.
         */
        if (argsmatch) {
            Py_INCREF(args);
            return args;
        } else {
            if (PyTuple_Size(args) + (self->sel_self?1:0) != self->argcount + self->numoutput) {
                /* There's the wrong number of arguments */
                PyErr_Format(PyExc_TypeError,
                    "expecting %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d", self->argcount - (self->sel_self?1:0), PyTuple_Size(args));
                return NULL;
            }
            PyObject* real_args;
            Py_ssize_t pyarg;

            real_args = PyTuple_New(self->argcount - (self->sel_self?1:0));
            if (real_args == NULL) {
                return NULL;
            }

            pyarg = 0;
            if (self->sel_self == NULL) {
                pyarg = 1;
                PyTuple_SET_ITEM(real_args, 0, PyTuple_GET_ITEM(args, 0));
                Py_INCREF(PyTuple_GET_ITEM(args, 0));
            }

            PyObjCMethodSignature* methinfo = PyObjCSelector_GetMetadata(_self);
            for (i = 2; i < Py_SIZE(methinfo); i++) {
                if (methinfo->argtype[i].type[0] != _C_OUT) {
                    PyTuple_SET_ITEM(real_args, pyarg, PyTuple_GET_ITEM(args, i-2+first_arg));
                    Py_INCREF(PyTuple_GET_ITEM(args, i-2+first_arg));
                    pyarg++;
                }
            }

            return real_args;
        }
    }
}


static PyObject*
pysel_call(PyObject* _self, PyObject* args, PyObject* kwargs)
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
    PyObject* result;

    if (self->callable == NULL) {
        PyErr_Format(PyExc_TypeError,
            "Calling abstract methods with selector %s",
            sel_getName(self->sel_selector));
        return NULL;
    }

    args = compensate_arglist(_self, args, kwargs);
    if (args == NULL) {
        return NULL;
    }

    if (!PyMethod_Check(self->callable)) {
        if (self->sel_self == NULL) {
            PyObject* self_arg;
            if (PyTuple_Size(args) < 1) {
                Py_DECREF(args);
                PyErr_SetString(PyObjCExc_Error, "need self argument");
                return NULL;
            }

            self_arg = PyTuple_GET_ITEM(args, 0);

            if (!PyObjCObject_Check(self_arg) && !PyObjCClass_Check(self_arg)) {
                Py_DECREF(args);
                PyErr_Format(PyExc_TypeError,
                    "Expecting an Objective-C class or "
                    "instance as self, got a %s",
                    Py_TYPE(self_arg)->tp_name);
                return NULL;
            }
        }

        /* normal function code will perform other checks */
    }

    /*
     * Assume callable will check arguments
     */
    if (self->sel_self == NULL) {
        result  = PyObject_Call(self->callable, args, kwargs);
        Py_DECREF(args);

    } else {
        Py_ssize_t argc = PyTuple_Size(args);
        PyObject* actual_args = PyTuple_New(argc+1);
        Py_ssize_t i;

        if (actual_args == NULL) {
            return NULL;
        }

        Py_INCREF(self->sel_self);
        PyTuple_SetItem(actual_args, 0, self->sel_self);

        for (i = 0; i < argc; i++) {
            PyObject* v = PyTuple_GET_ITEM(args, i);
            Py_XINCREF(v);
            PyTuple_SET_ITEM(actual_args, i+1, v);
        }

        result = PyObject_Call(self->callable, actual_args, kwargs);
        Py_DECREF(actual_args);
        Py_DECREF(args);
    }

    if ( result && (self->sel_self) && (PyObjCObject_Check(self->sel_self)) &&
         ((PyObjCObject*)self->sel_self)->flags & PyObjCObject_kUNINITIALIZED) {

         ((PyObjCObject*)self->sel_self)->flags &= ~PyObjCObject_kUNINITIALIZED;

    }

    return result;
}

static char*
pysel_default_signature(PyObject* callable)
{
    PyCodeObject* func_code;
    Py_ssize_t    arg_count;
    char*         result;
    const unsigned char *buffer;
    Py_ssize_t    buffer_len;
    Py_ssize_t    i;
    int           was_none;

    if (PyFunction_Check(callable)) {
        func_code = (PyCodeObject*)PyFunction_GetCode(callable);

    } else if (PyMethod_Check(callable)) {
        func_code = (PyCodeObject*)PyFunction_GetCode(PyMethod_Function(callable));

    } else {
        PyErr_SetString(PyExc_TypeError,
            "Cannot calculate default method signature");
        return NULL;
    }

    arg_count = func_code->co_argcount;
    if (arg_count < 1) {
        PyErr_SetString(PyExc_TypeError,
            "Objective-C callable methods must take at least one argument");
        return NULL;
    }


    /* arguments + return-type + selector */
    result = PyMem_Malloc(arg_count+3);
    if (result == 0) {
        PyErr_NoMemory();
        return NULL;
    }

    /* We want: v@:@... (final sequence of arg_count-1 @-chars) */
    memset(result, _C_ID, arg_count+2);
    result[0] = _C_VOID;
    result[2] = _C_SEL;
    result[arg_count+2] = '\0';

    if (PyObject_AsReadBuffer(func_code->co_code, (const void **)&buffer, &buffer_len)) {
        return NULL;
    }

    /*
       Scan bytecode to find return statements.  If any non-bare return
       statement exists, then set the return type to @ (id).
    */
    was_none = 0;
    for (i=0; i<buffer_len; ++i) {
        int op = buffer[i];
        if (op == LOAD_CONST && buffer[i+1] == 0 && buffer[i+2] == 0) {
            was_none = 1;
        } else {
            if (op == RETURN_VALUE) {
                if (!was_none) {
                    result[0] = _C_ID;
                    break;
                }
            }
            was_none = 0;
        }
        if (op >= HAVE_ARGUMENT) {
            i += 2;
        }
    }
    return result;
}

static SEL
pysel_default_selector(PyObject* callable)
{
    char buf[1024];
    char* cur;
    PyObject* name = PyObject_GetAttrString(callable, "__name__");

    if (name == NULL) return NULL;

    if (PyUnicode_Check(name)) {
        PyObject* bytes = PyUnicode_AsEncodedString(name, NULL, NULL);
        if (bytes == NULL) {
            return NULL;
        }
        strncpy(buf, PyBytes_AS_STRING(bytes), sizeof(buf)-1);
        Py_DECREF(bytes);


#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(name)) {
        strncpy(buf, PyString_AS_STRING(name), sizeof(buf)-1);
#endif

    } else  {
        return NULL;
    }


    cur = strchr(buf, '_');
    while (cur != NULL) {
        *cur = ':';
        cur = strchr(cur, '_');
    }
    return sel_registerName(buf);
}

SEL
PyObjCSelector_DefaultSelector(const char* methname)
{
    char buf[1024];
    char* cur;
    Py_ssize_t ln;

    strncpy(buf, methname, sizeof(buf)-1);
    ln = strlen(buf);

    cur = buf + ln;
    if (cur - buf > 3) {
        if (cur[-1] != '_') {
            return sel_registerName(buf);
        }

        if (cur[-1] == '_' && cur[-2] == '_') {
            cur[-2] = '\0';
            if (PyObjC_IsPythonKeyword(buf)) {
                return sel_registerName(buf);
            }
            cur[-2] = '_';
        }
    }

    /* Skip leading underscores, '_doFoo_' is probably '_doFoo:' in
     * Objective-C, not ':doFoo:'.
     *
     * Also if the name starts and ends with two underscores, return
     * it unmodified. This avoids mangling of Python's special methods.
     *
     * Also don't rewrite two underscores between name elements, such
     * as '__pyobjc__setItem_' -> '__pyobjc__setitem:'
     *
     * Also: when the name starts with two capital letters and an underscore
     * don't replace the underscore, the 'XX_' prefix is a common way to
     * namespace selectors.
     *
     * Both are heuristics and could be the wrong choice, but either
     * form is very unlikely to exist in ObjC code.
     */
    cur = buf;

    if (ln > 5) {
        if (cur[0] == '_' && cur[1] == '_' &&
            cur[ln-1] == '_' && cur[ln-2] == '_') {
            return sel_registerName(buf);
        }
    }

    while (*cur == '_') {
        cur++;
    }

    if (isupper(cur[0]) && isupper(cur[1]) && cur[2] == '_') {
        cur += 3;
    }

    /* Replace all other underscores by colons */
    cur = strchr(cur, '_');
    while (cur != NULL) {
        if (cur[1] == '_' && cur[2] && cur[2] != '_' && cur[-1] != '_') {
            /* Don't translate double underscores between
             * name elements.
             *
             * NOTE: cur[-1] is save because we've skipped leading
             * underscores earlier in this function.
             */
            cur += 2;
        } else {
            *cur = ':';
        }
        cur = strchr(cur, '_');
    }
    return sel_registerName(buf);
}

static PyObject*
pysel_new(PyTypeObject* type __attribute__((__unused__)),
      PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "function", "selector", "signature",
                "isClassMethod", "isRequired", "isHidden", NULL };
    PyObjCPythonSelector* result;
    PyObject* callable;
    char* signature = NULL;
    char* selector = NULL;
    SEL objc_selector;
    int class_method = 0;
    int required = 1;
    int hidden = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
            "O|"Py_ARG_BYTES Py_ARG_BYTES"iii",
            keywords, &callable, &selector, &signature,
            &class_method, &required, &hidden)) {
        return NULL;
    }

    if (signature != NULL) {
        /* Check if the signature string is valid */
        const char* cur;

        cur = signature;
        while (*cur != '\0') {
            cur = PyObjCRT_SkipTypeSpec(cur);
            if (cur == NULL) {
                PyErr_SetString(
                    PyExc_ValueError,
                    "invalid signature");
                return NULL;
            }
        }
    }

    if (callable != Py_None && !PyCallable_Check(callable)) {
        PyErr_SetString(PyExc_TypeError,
            "argument 'method' must be callable");
        return NULL;
    }

    if (PyObject_TypeCheck(callable, &PyClassMethod_Type)) {
        /* Special treatment for 'classmethod' instances */
        PyObject* tmp = PyObject_CallMethod(callable, "__get__", "OO", Py_None, &PyList_Type);
        if (tmp == NULL) {
            return NULL;
        }

        if (PyFunction_Check(tmp)) {
            /* A 'staticmethod' instance, cannot convert */
            Py_DECREF(tmp);
            PyErr_SetString(PyExc_TypeError,
                    "cannot use staticmethod as the "
                    "callable for a selector.");
            return NULL;
        }

#if PY_MAJOR_VERSION == 2
        callable = PyObject_GetAttrString(tmp, "im_func");
#else
        callable = PyObject_GetAttrString(tmp, "__func__");
#endif
        Py_DECREF(tmp);
        if (callable == NULL) {
            return NULL;
        }

    } else {
        Py_INCREF(callable);
    }

    if (selector == NULL) {
        objc_selector = pysel_default_selector(callable);
    } else {
        objc_selector = sel_registerName(selector);
    }

    result = (PyObjCPythonSelector*)PyObjCSelector_New(callable,
            objc_selector, signature, class_method, nil);
    Py_DECREF(callable);
    if (!result) {
        return NULL;
    }

    if (required) {
        result->sel_flags |= PyObjCSelector_kREQUIRED;
    }

    if (hidden) {
        result->sel_flags |= PyObjCSelector_kHIDDEN;
    }
    return (PyObject *)result;
}

static PyObject*
pysel_descr_get(PyObject* _meth, PyObject* obj, PyObject* class)
{
    PyObjCPythonSelector* meth = (PyObjCPythonSelector*)_meth;
    PyObjCPythonSelector* result;

    if (meth->sel_self != NULL || obj == Py_None) {
        Py_INCREF(meth);
        return (PyObject*)meth;
    }

    /* Bind 'self' */
    if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
        obj = class;
        if (PyType_Check(obj) && PyType_IsSubtype((PyTypeObject*)obj, &PyObjCClass_Type)) {
            obj = PyObjCClass_ClassForMetaClass(obj);
        }
    }

    result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
    result->sel_selector   = meth->sel_selector;
    result->sel_class   = meth->sel_class;
    result->sel_python_signature  = PyObjCUtil_Strdup(meth->sel_python_signature);

    if (result->sel_python_signature == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    if (meth->sel_native_signature) {
        result->sel_native_signature  = PyObjCUtil_Strdup(meth->sel_native_signature);
        if (result->sel_native_signature == NULL) {
            Py_DECREF(result);
            return NULL;
        }

    } else {
        result->sel_native_signature = NULL;
    }

    result->sel_methinfo = PyObjCSelector_GetMetadata((PyObject*)meth);
    Py_XINCREF(result->sel_methinfo);
    result->argcount = meth->argcount;
    result->numoutput = meth->numoutput;

    result->sel_self       = obj;
    result->sel_flags = meth->sel_flags;
    result->callable = meth->callable;

    if (result->sel_self) {
        Py_INCREF(result->sel_self);
    }

    if (result->callable) {
        Py_INCREF(result->callable);
    }

    return (PyObject*)result;
}


static void
pysel_dealloc(PyObject* obj)
{
    Py_CLEAR(((PyObjCPythonSelector*)obj)->callable);
    sel_dealloc(obj);
}

PyDoc_STRVAR(pysel_get_callable_doc,
"Returns the python 'function' that implements this method.\n"
"\n"
);
static PyObject*
pysel_get_callable(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;
    Py_INCREF(self->callable);
    return self->callable;
}

PyDoc_STRVAR(pysel_docstring_doc,
    "The document string for a method");
static PyObject*
pysel_docstring(PyObject* _self, void* closure __attribute__((__unused__)))
{
    PyObjCPythonSelector* self = (PyObjCPythonSelector*)_self;

    PyObject* docstr = PyObject_GetAttrString(self->callable, "__doc__");
    return docstr;
}


static PyGetSetDef pysel_getset[] = {
    {
        "callable",
        pysel_get_callable,
        0,
        pysel_get_callable_doc,
        0
    },
    {
        "__doc__",
        pysel_docstring,
        0,
        pysel_docstring_doc,
        0
    },
#if PY_VERSION_HEX >= 0x03030000
    {
        "__signature__",
        PyObjC_callable_signature_get,
        0,
            "inspect.Signaturefor a method",
        0
    },
#endif

    {
        NULL,
        NULL,
        NULL,
        NULL,
        0
    }
};

PyTypeObject PyObjCPythonSelector_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.python_selector",
    .tp_basicsize   = sizeof(PyObjCPythonSelector),
    .tp_itemsize    = 0,
    .tp_dealloc     = pysel_dealloc,
    .tp_repr        = pysel_repr,
    .tp_hash        = pysel_hash,
    .tp_call        = pysel_call,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_richcompare = pysel_richcompare,
    .tp_getset      = pysel_getset,
    .tp_base        = &PyObjCSelector_Type,
    .tp_descr_get   = pysel_descr_get,
};

const char* PyObjCSelector_Signature(PyObject* obj)
{
    return ((PyObjCSelector*)obj)->sel_python_signature;
}

Class
PyObjCSelector_GetClass(PyObject* sel)
{
    if (!PyObjCNativeSelector_Check(sel)) {
        PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
        return NULL;
    }

    return ((PyObjCNativeSelector*)sel)->sel_class;
}

SEL
PyObjCSelector_GetSelector(PyObject* sel)
{
    if (!PyObjCSelector_Check(sel)) {
        PyErr_SetString(PyExc_TypeError, "Expecting PyObjCSelector");
        return NULL;
    }

    return ((PyObjCSelector*)sel)->sel_selector;
}


int   PyObjCSelector_Required(PyObject* obj)
{
    return (((PyObjCSelector*)obj)->sel_flags & PyObjCSelector_kREQUIRED) != 0;
}

int   PyObjCSelector_IsClassMethod(PyObject* obj)
{
    return (PyObjCSelector_GetFlags(obj) & PyObjCSelector_kCLASS_METHOD) != 0;
}

int   PyObjCSelector_IsHidden(PyObject* obj)
{
    return (PyObjCSelector_GetFlags(obj) & PyObjCSelector_kHIDDEN) != 0;
}

int   PyObjCSelector_GetFlags(PyObject* obj)
{
    return ((PyObjCSelector*)obj)->sel_flags;
}


/*
 * Find the signature of 'selector' in the list of protocols.
 */
static const char*
find_protocol_signature(PyObject* protocols, SEL selector, int is_class_method)
{
    Py_ssize_t i;
    PyObject* proto;
    PyObject* info;

    if (!PyList_Check(protocols)) {
        PyErr_Format(PyObjCExc_InternalError,
            "Protocol-list is not a 'list', but '%s'",
            Py_TYPE(protocols)->tp_name);
        return NULL;
    }

    /* First try the explicit protocol definitions */
    for (i = 0; i < PyList_GET_SIZE(protocols); i++) {
        proto = PyList_GET_ITEM(protocols, i);
        if (proto == NULL) {
            PyErr_Clear();
            continue;
        }
        Py_INCREF(proto);

        if (PyObjCFormalProtocol_Check(proto)) {
            const char* signature;

            signature = PyObjCFormalProtocol_FindSelectorSignature(
                    proto, selector, is_class_method
            );
            if (signature != NULL) {
                Py_DECREF(proto);
                return (char*)signature;
            }
        }

        info = PyObjCInformalProtocol_FindSelector(proto, selector, is_class_method);
        Py_DECREF(proto);
        if (info != NULL) {
            return PyObjCSelector_Signature(info);
        }
    }

    /* Then check if another protocol users this selector */
    proto = PyObjCInformalProtocol_FindProtocol(selector);
    if (proto == NULL) {
        PyErr_Clear();
        return NULL;
    }

    info = PyObjCInformalProtocol_FindSelector(proto, selector, is_class_method);
    if (info != NULL) {
        if (PyList_Append(protocols, proto) < 0) {
            return NULL;
        }
        return PyObjCSelector_Signature(info);
    }

    return NULL;
}

PyObject*
PyObjCSelector_FromFunction(
    PyObject* pyname,
    PyObject* callable,
    PyObject* template_class,
    PyObject* protocols)
{
    SEL selector;
    Method meth;
    int is_class_method = 0;
    Class oc_class = PyObjCClass_GetClass(template_class);
    PyObject* value;
    PyObject* super_sel;

    if (oc_class == NULL) {
        return NULL;
    }

    if (PyObjCPythonSelector_Check(callable)) {
        PyObjCPythonSelector* result;

        if (((PyObjCPythonSelector*)callable)->callable == NULL || ((PyObjCPythonSelector*)callable)->callable == Py_None) {
            PyErr_SetString(PyExc_ValueError, "selector object without callable");
            return NULL;
        }
        result = PyObject_New(PyObjCPythonSelector, &PyObjCPythonSelector_Type);
        result->sel_selector = ((PyObjCPythonSelector*)callable)->sel_selector;
        result->numoutput = ((PyObjCPythonSelector*)callable)->numoutput;
        result->argcount = ((PyObjCPythonSelector*)callable)->argcount;
        result->sel_methinfo = PyObjCSelector_GetMetadata(callable);
        Py_XINCREF(result->sel_methinfo);
        result->sel_class   = oc_class;
        result->sel_python_signature  = PyObjCUtil_Strdup(
                ((PyObjCPythonSelector*)callable)->sel_python_signature);
        if (result->sel_python_signature == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->sel_native_signature = NULL;
        result->sel_self = NULL;
        result->sel_flags = ((PyObjCPythonSelector*)callable)->sel_flags;
        result->callable = ((PyObjCPythonSelector*)callable)->callable;
        if (result->callable) {
            Py_INCREF(result->callable);
        }
        if (PyObjCClass_HiddenSelector(template_class, PyObjCSelector_GetSelector(callable), PyObjCSelector_IsClassMethod(callable))) {
            ((PyObjCSelector*)result)->sel_flags |= PyObjCSelector_kHIDDEN;
        }
        return (PyObject*)result;
    }

    if (!PyFunction_Check(callable) && !PyMethod_Check(callable) &&
        (Py_TYPE(callable) != &PyClassMethod_Type)) {

        PyErr_SetString(PyExc_TypeError, "expecting function, method or classmethod");
        return NULL;
    }

    if (Py_TYPE(callable) == &PyClassMethod_Type) {
        /*
         * This is a 'classmethod' or 'staticmethod'. 'classmethods'
         * will be converted to class 'selectors', 'staticmethods' are
         * returned as-is.
         */
        PyObject* tmp;
        is_class_method = 1;
        tmp = PyObject_CallMethod(callable, "__get__", "OO",
                Py_None, template_class);
        if (tmp == NULL) {
            return NULL;
        }

        if (PyFunction_Check(tmp)) {
            /* A 'staticmethod', don't convert to a selector */
            Py_DECREF(tmp);
            Py_INCREF(callable);
            return callable;
        }

#if PY_MAJOR_VERSION == 2
        callable = PyObject_GetAttrString(tmp, "im_func");
#else
        callable = PyObject_GetAttrString(tmp, "__func__");
#endif
        Py_DECREF(tmp);
        if (callable == NULL) {
            return NULL;
        }
    }

    if (pyname == NULL) {
        /* No name specified, use the function name */
        pyname = PyObject_GetAttrString(callable, "__name__");
        if (pyname == NULL) {
            return NULL;
        }
        if (PyUnicode_Check(pyname)) {
            PyObject* bytes = PyUnicode_AsEncodedString(pyname, NULL, NULL);
            if (bytes == NULL) {
                return NULL;
            }
            selector = PyObjCSelector_DefaultSelector(
                    PyBytes_AsString(bytes));
            Py_DECREF(bytes);

#if PY_MAJOR_VERSION == 2
        } else if (PyString_Check(pyname)) {
            selector = PyObjCSelector_DefaultSelector(
                    PyString_AsString(pyname));
#endif

        } else {
            PyErr_SetString(PyExc_TypeError, "Function name is not a string");
            return NULL;
        }

    } else if (PyUnicode_Check(pyname)) {
        PyObject* bytes = PyUnicode_AsEncodedString(pyname, NULL, NULL);

        if (bytes == NULL) {
            return NULL;
        }

        selector = PyObjCSelector_DefaultSelector(
                PyBytes_AsString(bytes));
        Py_DECREF(bytes);

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(pyname)) {
        selector = PyObjCSelector_DefaultSelector(
            PyString_AS_STRING(pyname));
#endif

    } else {
        PyErr_SetString(PyExc_TypeError,
            "method name must be a string");
        return NULL;
    }

    /* XXX: This seriously fails if a class method has a different signature
     * than an instance method of the same name!
     *
     * We eagerly call PyObjCClass_FindSelector because some ObjC
     * classes are not fully initialized until they are actually used,
     * and the code below doesn't seem to count but PyObjCClass_FindSelector
     * is.
     */
    super_sel = PyObjCClass_FindSelector(template_class, selector, is_class_method);
    if (super_sel == NULL) {
        PyErr_Clear();
    }

    if (is_class_method) {
        meth = class_getClassMethod(oc_class, selector);

    } else {
        meth = class_getInstanceMethod(oc_class, selector);

        if (!meth && !sel_isEqual(selector, @selector(copyWithZone:)) && !sel_isEqual(selector, @selector(mutableCopyWithZone:))) {
            /* Look for a classmethod, but don't do that for copyWithZone:
             * because that method is commonly defined in Python, and
             * overriding "NSObject +copyWithZone:" is almost certainly
             * not the intended behaviour.
             */
            meth = class_getClassMethod(oc_class, selector);
            if (meth) {
                is_class_method = 1;
            }
        }
    }

    if (meth) {
        /* The function overrides a method in the
         * objective-C class.
         *
         * Get the signature through the python wrapper,
         * the user may have specified a more exact
         * signature!
         */
        const char* typestr = NULL;

        if (super_sel == NULL) {
            /* FIXME: This isn't optimal when hiding methods with non-standard types */
            PyObject* met = PyObjCClass_HiddenSelector(template_class, selector, is_class_method);
            if (met == NULL) {
                typestr = method_getTypeEncoding(meth);
            } else {
                typestr = ((PyObjCMethodSignature*)met)->signature;
            }
        } else {
            typestr = PyObjCSelector_Signature(super_sel);
        }

        value = PyObjCSelector_New(
            callable, selector,
            typestr, is_class_method,
            oc_class);
        Py_XDECREF(super_sel);

    } else {
        const char* signature = NULL;

        PyErr_Clear(); /* The call to PyObjCClass_FindSelector failed */
        if (protocols != NULL) {
            signature = find_protocol_signature(
                    protocols, selector, is_class_method);

            if (signature == NULL && PyErr_Occurred()) {
                return NULL;
            }
        }

        value = PyObjCSelector_New(
            callable,
            selector,
            signature,
            is_class_method,
            oc_class);
    }

    if (PyObjCClass_HiddenSelector(template_class, selector, PyObjCSelector_IsClassMethod(value))) {
        ((PyObjCSelector*)value)->sel_flags |= PyObjCSelector_kHIDDEN;
    }

    return value;
}

PyObject* PyObjCSelector_Copy(PyObject* selector)
{
    if (PyObjCPythonSelector_Check(selector)) {
        return pysel_descr_get(selector, NULL, NULL);

    } else if (PyObjCNativeSelector_Check(selector)) {
        return objcsel_descr_get(selector, NULL, NULL);

    } else {
        PyErr_SetString(PyExc_TypeError, "copy non-selector");
        return NULL;
    }
}
