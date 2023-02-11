#include "pyobjc.h"

/*
 * descriptor objc_ivar
 *
 * We start of with a descriptor object that allows the user to access
 * (read and write) objective-C instance variables.
 *
 * These descriptors are used in two places:
 * 1) the wrapper for objective-C classes and objects use these to provide
 *    access to existing instance variables
 * 2) the user can define new instance variables (most likely 'outlets') when
 *    defining subclasses of objective-C classes.
 */

NS_ASSUME_NONNULL_BEGIN

static void
ivar_dealloc(PyObject* _ivar)
{
    PyObjCInstanceVariable* ivar = (PyObjCInstanceVariable*)_ivar;
    if (ivar->name) {
        PyMem_Free(ivar->name);
    }
    if (ivar->type) {
        PyMem_Free(ivar->type);
    }
    PyTypeObject* tp = Py_TYPE(ivar);
    tp->tp_base->tp_dealloc(_ivar);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

static PyObject* _Nullable ivar_repr(PyObject* _self)
{
    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
    if (self->isOutlet) {
        if (self->name) {
            return PyUnicode_FromFormat("<IBOutlet %s>", self->name);
        } else {
            return PyUnicode_FromString("<IBOutlet>");
        }

    } else {
        if (self->name) {
            return PyUnicode_FromFormat("<instance-variable %s>", self->name);
        } else {
            return PyUnicode_FromString("<instance-variable>");
        }
    }
}

static PyObject* _Nullable ivar_descr_get(PyObject* _self, PyObject* _Nullable obj,
                                          PyObject* type __attribute__((__unused__)))
{
    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
    Ivar                    var;
    id                      objc;
    PyObject*               res;

    if (!obj) {
        /* Getting the instance variable from a class, return the descriptor itself
         * to make it easier to introspect.
         */
        Py_INCREF(_self);
        return _self;
    }

    if (!obj || PyObjCClass_Check(obj)) {
        /* XXX: Not sure if this is ever true... */
        PyErr_SetString(PyExc_TypeError, "Cannot access Objective-C instance-variables "
                                         "through class");
        return NULL;
    }

    if (!PyObjCObject_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "objc.ivar descriptor on a plain Python object");
        return NULL;
    }

    objc = PyObjCObject_GetObject(obj);
    if (objc == NULL) {
        PyErr_SetString(PyExc_TypeError,
                        "Cannot access Objective-C instance-variables of NULL");
        return NULL;
    }

    if (self->name == NULL) {
        PyErr_SetString(PyExc_TypeError, "Using unnamed instance variable");
        return NULL;
    }

    var = class_getInstanceVariable(object_getClass(objc), self->name);
    if (var == NULL) {
        PyErr_Format(
            PyExc_RuntimeError,
            "objc.ivar descriptor for non-existing instance variable '%s' in class '%s'",
            self->name, class_getName(object_getClass(objc)));
        return NULL;
    }

    if (self->isSlot) {
        res = *(PyObject**)(((char*)objc) + ivar_getOffset(var));

        if (res == NULL) {
            PyErr_Format(PyExc_AttributeError, "No attribute %s\n", ivar_getName(var));
        } else {
            Py_INCREF(res);
        }

    } else {
        const char* encoding = ivar_getTypeEncoding(var);

        if (encoding == NULL) {
            PyErr_SetString(PyObjCExc_Error, "Cannot extract type encoding from ivar");
            return NULL;
        }

        if (encoding[0] == _C_ID) {
            /* An object */
            id value = object_getIvar(objc, var);
            res      = pythonify_c_value(encoding, &value);
        } else {
            res = pythonify_c_value(encoding, ((char*)objc) + ivar_getOffset(var));
        }
    }
    return res;
}

static int
ivar_descr_set(PyObject* _self, PyObject* _Nullable obj, PyObject* _Nullable value)
{
    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
    Ivar                    var;
    id                      objc;
    Py_ssize_t              size;
    int                     res;

    if (value == NULL && !self->isSlot) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete Objective-C instance variables");
        return -1;
    }

    if (!obj || PyObjCClass_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "Cannot set Objective-C instance-variables "
                                         "through class");
        return -1;
    }

    if (!PyObjCObject_Check(obj)) {
        PyErr_SetString(PyExc_TypeError, "objc.ivar descriptor on a plain Python object");
        return -1;
    }

    objc = PyObjCObject_GetObject(obj);
    if (objc == NULL) {
        PyErr_SetString(PyExc_TypeError,
                        "Cannot access Objective-C instance-variables of NULL");
        return -1;
    }

    if (self->name == NULL) {
        PyErr_SetString(PyExc_TypeError, "Using unnamed instance variable");
        return -1;
    }

    if (self->ivar == NULL) {
        var = class_getInstanceVariable(object_getClass(objc), self->name);
        if (var == NULL) {
            PyErr_SetString(PyExc_RuntimeError,
                            "objc_ivar descriptor for non-existing instance "
                            "variable");
            return -1;
        }
        self->ivar = var;
    } else {
        var = self->ivar;
    }

    // NSString* ocName = [NSString stringWithUTF8String:self->name];
    // [objc willChangeValueForKey:ocName];

    if (self->isSlot) {
        PyObject** slotval = (PyObject**)(((char*)objc) + ivar_getOffset(var));
        Py_XINCREF(value);
        Py_XDECREF(*slotval);
        *slotval = value;

        // [objc didChangeValueForKey:ocName];
        return 0;
    }

    if (strcmp(ivar_getTypeEncoding(var), @encode(id)) == 0) {
        /* Automagically manage refcounting of instance variables */
        id new_value;

        res = depythonify_c_value(@encode(id), value, &new_value);
        if (res == -1) {
            // [objc didChangeValueForKey:ocName];
            return -1;
        }

        if (!self->isOutlet) {
            Py_BEGIN_ALLOW_THREADS
                @try {
                    id old_value = object_getIvar(objc, var);
                    [new_value retain];
                    [old_value release];
                } @catch (NSObject* localException) {
                    NSLog(@"PyObjC: ignoring exception during attribute replacement: %@",
                          localException);
                }
            Py_END_ALLOW_THREADS
        }

        object_setIvar(objc, var, new_value);
        // [objc didChangeValueForKey:ocName];

        return 0;
    }

    size = PyObjCRT_SizeOfType(ivar_getTypeEncoding(var));
    if (size == -1) {
        // [objc didChangeValueForKey:ocName];
        return -1;
    }
    res = depythonify_c_value(ivar_getTypeEncoding(var), value,
                              (void*)(((char*)objc) + ivar_getOffset(var)));
    if (res == -1) {
        // [objc didChangeValueForKey:ocName];
        return -1;
    }

    // [objc didChangeValueForKey:ocName];
    return 0;
}

static int
ivar_init(PyObject* _self, PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char*            keywords[]  = {"name", "type", "isOutlet", "isSlot", NULL};
    PyObjCInstanceVariable* self        = (PyObjCInstanceVariable*)_self;
    char*                   name        = NULL;
    char*                   type        = @encode(id);
    PyObject*               isOutletObj = NULL;
    PyObject*               isSlotObj   = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|syOO:objc_ivar", keywords, &name,
                                     &type, &isOutletObj, &isSlotObj)) {
        return -1;
    }

    if (PyObjCRT_SizeOfType(type) == -1) {
        PyErr_SetString(PyExc_ValueError, "Invalid type encoding");
        return -1;
    }

    if (name) {
        self->name = PyObjCUtil_Strdup(name);
        if (self->name == NULL) {
            return -1;
        }

    } else {
        self->name = NULL;
    }

    char* type_copy = PyObjCUtil_Strdup(type);
    if (type_copy == NULL) {
        if (name) {
            PyMem_Free(self->name);
        }
        return -1;
    }
    self->type = type_copy;
    if (isOutletObj) {
        self->isOutlet = PyObject_IsTrue(isOutletObj);

    } else {
        self->isOutlet = 0;
    }

    if (isSlotObj) {
        self->isSlot = PyObject_IsTrue(isSlotObj);

    } else {
        self->isSlot = 0;
    }

    self->ivar = NULL;

    return 0;
}

static PyObject* _Nullable ivar_class_setup(PyObject* _self, PyObject* _Nullable args,
                                            PyObject* _Nullable kwds)
{
    static char* keywords[] = {"name", "class_dict", "instance_method_list",
                               "class_method_list", NULL};

    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;
    char*                   name;
    PyObject*               class_dict;
    PyObject*               instance_method_list;
    PyObject*               class_method_list;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "sO!O!O!", keywords, &name, &PyDict_Type,
                                     &class_dict, &PySet_Type, &instance_method_list,
                                     &PySet_Type, &class_method_list)) {

        return NULL;
    }

    if (self->name == NULL) {
        self->name = PyObjCUtil_Strdup(name);
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static Py_hash_t
ivar_hash(PyObject* o)
{
    Py_hash_t result = 0;

    if (PyObjCInstanceVariable_GetName(o)) {
        result = PyHash_GetFuncDef()->hash(PyObjCInstanceVariable_GetName(o),
                                           strlen(PyObjCInstanceVariable_GetName(o)));
    }

    if (PyObjCInstanceVariable_GetType(o)) {
        result ^= PyHash_GetFuncDef()->hash(PyObjCInstanceVariable_GetType(o),
                                            strlen(PyObjCInstanceVariable_GetType(o)));
    }

    if (PyObjCInstanceVariable_IsOutlet(o)) {
        result ^= 0x10;
    }

    if (PyObjCInstanceVariable_IsSlot(o)) {
        result ^= 0x20;
    }

    if (result == -1) {
        result = -2;
    }

    return result;
}

static PyObject* _Nullable ivar_richcompare(PyObject* a, PyObject* b, int op)
{
    if (op == Py_EQ || op == Py_NE) {
        if (PyObjCInstanceVariable_Check(a) && PyObjCInstanceVariable_Check(b)) {
            int same = 1;

            if (PyObjCInstanceVariable_GetName(a) == NULL) {
                if (PyObjCInstanceVariable_GetName(b) != NULL) {
                    same = 0;
                }
            } else if (PyObjCInstanceVariable_GetName(b) != NULL) {
                same = same
                       && (strcmp(PyObjCInstanceVariable_GetName(a),
                                  PyObjCInstanceVariable_GetName(b))
                           == 0);
            }

            if (PyObjCInstanceVariable_GetType(a) == NULL) {
                if (PyObjCInstanceVariable_GetType(b) != NULL) {
                    same = 0;
                }
            } else if (PyObjCInstanceVariable_GetType(b) != NULL) {
                same = same
                       && (strcmp(PyObjCInstanceVariable_GetType(a),
                                  PyObjCInstanceVariable_GetType(b))
                           == 0);
            }

            if (PyObjCInstanceVariable_IsSlot(a) != PyObjCInstanceVariable_IsSlot(b)) {
                same = 0;
            }

            if (PyObjCInstanceVariable_IsOutlet(a)
                != PyObjCInstanceVariable_IsOutlet(b)) {
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
    }
    Py_INCREF(Py_NotImplemented);
    return Py_NotImplemented;
}

static PyMethodDef ivar_methods[] = {{
                                         .ml_name  = "__pyobjc_class_setup__",
                                         .ml_meth  = (PyCFunction)ivar_class_setup,
                                         .ml_flags = METH_VARARGS | METH_KEYWORDS,
                                     },

                                     {
                                         .ml_name = NULL /* SENTINEL */
                                     }};

PyDoc_STRVAR(
    ivar_doc,
    "ivar(name, type='@', isOutlet=False, isSlot=False) -> instance-variable\n" CLINIC_SEP
    "\n"
    "Creates a descriptor for accessing an Objective-C instance variable.\n\n"
    "This should only be used in the definition of Objective-C subclasses, and\n"
    "will then automatically define the instance variable in the objective-C side.\n"
    "\n"
    "'type' is optional and should be a signature string.\n"
    "\n"
    "The name is optional in class definitions and will default to the name the\n"
    "value is assigned to");

PyDoc_STRVAR(ivar_typestr_doc, "The Objective-C type encoding");
static PyObject* _Nullable ivar_get_typestr(PyObject* _self, void* _Nullable closure
                                            __attribute__((__unused__)))
{
    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;

    return PyBytes_FromString(self->type);
}

PyDoc_STRVAR(ivar_name_doc, "The Objective-C name");
static PyObject* _Nullable ivar_get_name(PyObject* _self, void* _Nullable closure
                                         __attribute__((__unused__)))
{
    PyObjCInstanceVariable* self = (PyObjCInstanceVariable*)_self;

    if (self->name) {
        return PyUnicode_FromString(self->name);
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}

PyDoc_STRVAR(ivar_isOutlet_doc, "True if the instance variable is an IBOutlet");
static PyObject* _Nullable ivar_get_isOutlet(PyObject* _self, void* _Nullable closure
                                             __attribute__((__unused__)))
{
    PyObjCInstanceVariable* self   = (PyObjCInstanceVariable*)_self;
    PyObject*               result = self->isOutlet ? Py_True : Py_False;
    Py_INCREF(result);
    return result;
}

PyDoc_STRVAR(ivar_isSlot_doc, "True if the instance variable is a Python slot");
static PyObject* _Nullable ivar_get_isSlot(PyObject* _self, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    PyObjCInstanceVariable* self   = (PyObjCInstanceVariable*)_self;
    PyObject*               result = self->isSlot ? Py_True : Py_False;
    Py_INCREF(result);
    return result;
}

static PyGetSetDef ivar_getset[] = {{
                                        .name = "__typestr__",
                                        .get  = ivar_get_typestr,
                                        .doc  = ivar_typestr_doc,
                                    },
                                    {
                                        .name = "__name__",
                                        .get  = ivar_get_name,
                                        .doc  = ivar_name_doc,
                                    },
                                    {
                                        .name = "__isOutlet__",
                                        .get  = ivar_get_isOutlet,
                                        .doc  = ivar_isOutlet_doc,
                                    },
                                    {
                                        .name = "__isSlot__",
                                        .get  = ivar_get_isSlot,
                                        .doc  = ivar_isSlot_doc,
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

static PyType_Slot ivar_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&ivar_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&ivar_repr},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_richcompare, .pfunc = (void*)&ivar_richcompare},
    {.slot = Py_tp_hash, .pfunc = (void*)&ivar_hash},
    {.slot = Py_tp_doc, .pfunc = (void*)&ivar_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&ivar_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&ivar_getset},
    {.slot = Py_tp_descr_get, .pfunc = (void*)&ivar_descr_get},
    {.slot = Py_tp_descr_set, .pfunc = (void*)&ivar_descr_set},
    {.slot = Py_tp_init, .pfunc = (void*)&ivar_init},

    {0, NULL} /* sentinel */
};

static PyType_Spec ivar_spec = {
    .name      = "objc.ivar",
    .basicsize = sizeof(PyObjCInstanceVariable),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = ivar_slots,
};

PyObject* PyObjCInstanceVariable_Type = (PyObject* _Nonnull)NULL;

int
PyObjCInstanceVariable_Setup(PyObject* module)
{
    PyObject* tmp = PyType_FromSpec(&ivar_spec);
    if (tmp == NULL) {
        return -1;
    }
    PyObjCInstanceVariable_Type = tmp;

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "ivar", PyObjCInstanceVariable_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCInstanceVariable_Type);
    return 0;
}

NS_ASSUME_NONNULL_END
