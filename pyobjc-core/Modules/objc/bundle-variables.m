/*
 * This module exports a function to load variables in a bundle
 *
 * NOTE: The interface is specified with NSBundles, but we have to
 * use CFBundles in the implementation.
 */
#include "pyobjc.h"

#include <CoreFoundation/CoreFoundation.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSURL.h>

#include <dlfcn.h>

NS_ASSUME_NONNULL_BEGIN

static CFBundleRef _Nullable CreateCFBundleFromNSBundle(NSBundle* bundle)
{
    CFURLRef bundleURL;

    bundleURL = (CFURLRef)[NSURL fileURLWithPath:[bundle bundlePath]];
    return CFBundleCreate(kCFAllocatorDefault, bundleURL);
}

PyObject* _Nullable PyObjC_loadSpecialVar(PyObject* self __attribute__((__unused__)),
                                          PyObject* _Nullable args,
                                          PyObject* _Nullable kwds)
{
    static char* keywords[] = {"bundle", "module_globals", "typeid",
                               "name",   "skip_undefined", NULL};

    NSBundle* bundle;
    NSString* name;
    PyObject* module_globals;
    Py_ssize_t typeid;
    Py_ssize_t  skip_undefined = 1;
    CFBundleRef cfBundle;
    void*       value;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O!iO&|i", keywords,
                                     PyObjCObject_Convert, &bundle, &PyDict_Type,
                                     &module_globals, &typeid, PyObjCObject_Convert,
                                     &name, &skip_undefined)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            cfBundle = CreateCFBundleFromNSBundle(bundle);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            cfBundle = NULL;
        }
    Py_END_ALLOW_THREADS

    if (cfBundle == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        PyErr_Format(PyObjCExc_Error, "Cannot convert NSBundle to CFBundle");
        return NULL;
    }

    if (![name isKindOfClass:[NSString class]]) {
        PyErr_SetString(PyExc_TypeError, "variable name not a string");
        return NULL;
    }

    value = CFBundleGetDataPointerForName(cfBundle, (CFStringRef)name);
    if (value == NULL) {
        if (!skip_undefined) {
            PyErr_SetString(PyObjCExc_Error, "cannot find a variable");
            return NULL;
        }

    } else {
        PyObject* py_val = PyObjCCF_NewSpecialFromTypeID(typeid, *(id*)value);
        if (py_val == NULL) {
            return NULL;
        }

        if (PyDict_SetItemString(module_globals, [name UTF8String], py_val) == -1) {
            Py_DECREF(py_val);
            return NULL;
        }
        Py_DECREF(py_val);
    }

    Py_INCREF(Py_None);
    return Py_None;
}

PyObject* _Nullable PyObjC_loadBundleVariables(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"bundle", "module_globals", "variableInfo",
                               "skip_undefined", NULL};
    NSBundle*    bundle;
    PyObject*    module_globals;
    PyObject*    variableInfo;
    Py_ssize_t   skip_undefined = 1;
    CFBundleRef  cfBundle;
    PyObject*    seq;
    Py_ssize_t   i, len;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O!O|i", keywords,
                                     PyObjCObject_Convert, &bundle, &PyDict_Type,
                                     &module_globals, &variableInfo, &skip_undefined)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            cfBundle = CreateCFBundleFromNSBundle(bundle);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
            cfBundle = NULL;
        }
    Py_END_ALLOW_THREADS

    if (cfBundle == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }
        PyErr_Format(PyObjCExc_Error, "Cannot convert NSBundle to CFBundle");
        return NULL;
    }

    seq = PySequence_Fast(variableInfo, "variableInfo not a sequence");
    if (seq == NULL) {
        return NULL;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    for (i = 0; i < len; i++) {
        PyObject* item = PySequence_Fast_GET_ITEM(seq, i);
        void*     value;
        char*     signature;
        PyObject* py_name;
        NSString* name;

        if (!PyTuple_Check(item)) {
            PyErr_Format(PyExc_TypeError,
                         "item %" PY_FORMAT_SIZE_T "d has type %s not tuple", i,
                         Py_TYPE(item)->tp_name);
            Py_DECREF(seq);
            return NULL;
        }

        if (!PyArg_ParseTuple(item, "O!y:variableInfo", &PyUnicode_Type, &py_name,
                              &signature)) {
            Py_DECREF(seq);
            return NULL;
        }

        if (depythonify_python_object(py_name, &name) == -1) {
            return NULL;
        }

        value = CFBundleGetDataPointerForName(cfBundle, (CFStringRef)name);
        if (value == NULL) {
            value = dlsym(RTLD_DEFAULT, [(NSString*)name UTF8String]);
        }
        if (value == NULL) {
            if (!skip_undefined) {
                PyErr_SetString(PyObjCExc_Error, "cannot find a variable");
                Py_DECREF(seq);
                return NULL;
            }

        } else {
            PyObject* py_val;

            if (*signature == _C_CHARPTR) {
                py_val = pythonify_c_value(signature, &value);
            } else {
                py_val = pythonify_c_value(signature, value);
            }
            if (py_val == NULL) {
                Py_DECREF(seq);
                return NULL;
            }

            if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
                    module_globals, [name UTF8String], py_val)
                == -1) {
                // LCOV_EXCL_START
                Py_DECREF(seq);
                Py_DECREF(py_val);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(py_val);
        }
    }
    Py_DECREF(seq);
    Py_INCREF(Py_None);
    return Py_None;
}

PyObject* _Nullable PyObjC_loadBundleFunctions(PyObject* self __attribute__((__unused__)),
                                               PyObject* _Nullable args,
                                               PyObject* _Nullable kwds)
{
    static char* keywords[] = {"bundle", "module_globals", "functionInfo",
                               "skip_undefined", NULL};
    NSBundle*    bundle;
    PyObject*    module_globals;
    PyObject*    functionInfo;
    int          skip_undefined = 1;
    CFBundleRef  cfBundle;
    PyObject*    seq;
    Py_ssize_t   i, len;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O!O|i", keywords,
                                     PyObjCObject_Convert, &bundle, &PyDict_Type,
                                     &module_globals, &functionInfo, &skip_undefined)) {
        return NULL;
    }

    if (bundle == NULL) {
        cfBundle = NULL;
    } else {
        Py_BEGIN_ALLOW_THREADS
            @try {
                cfBundle = CreateCFBundleFromNSBundle(bundle);

            } @catch (NSObject* localException) {
                PyObjCErr_FromObjC(localException);
                cfBundle = NULL;
            }
        Py_END_ALLOW_THREADS

        if (cfBundle == NULL && PyErr_Occurred()) {
            return NULL;
        }

        if (cfBundle == NULL) {
            PyErr_Format(PyObjCExc_Error, "Cannot convert NSBundle to CFBundle");
            return NULL;
        }
    }

    seq = PySequence_Fast(functionInfo, "functionInfo not a sequence");
    if (seq == NULL) {
        return NULL;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    for (i = 0; i < len; i++) {
        PyObject* item = PySequence_Fast_GET_ITEM(seq, i);
        void*     value;
        char*     signature;
        NSString* name;
        char*     c_name;
        PyObject* doc;
        PyObject* meta = NULL;

        if (!PyTuple_Check(item)) {
            PyErr_Format(PyExc_TypeError,
                         "item %" PY_FORMAT_SIZE_T "d has type %s not tuple", i,
                         Py_TYPE(item)->tp_name);
            Py_DECREF(seq);
            return NULL;
        }

        doc = NULL;
        if (cfBundle != NULL) {
            if (!PyArg_ParseTuple(item, "O&y|UO:functionInfo", PyObjCObject_Convert,
                                  &name, &signature, &doc, &meta)) {
                Py_DECREF(seq);
                return NULL;
            }
            if (![name isKindOfClass:[NSString class]]) {
                PyErr_SetString(PyExc_TypeError, "functionInfo name not a string");
                Py_DECREF(seq);
                return NULL;
            }

            value = CFBundleGetFunctionPointerForName(cfBundle, (CFStringRef)name);
        } else {
            if (!PyArg_ParseTuple(item, "sy|UO:functionInfo", &c_name, &signature, &doc,
                                  &meta)) {
                Py_DECREF(seq);
                return NULL;
            }

            value = dlsym(RTLD_DEFAULT, c_name);
        }

        if (value == NULL) {
            if (!skip_undefined) {
                PyErr_Format(PyObjCExc_Error, "cannot find a function: %R", item);
                Py_DECREF(seq);
                return NULL;
            }

        } else {
            PyObject* py_name;
            PyObject* py_val;

            if (cfBundle == NULL) {
                py_name = PyUnicode_FromString(c_name);
            } else {
                py_name = id_to_python(name);
            }

            py_val = PyObjCFunc_New(py_name, value, signature, doc, meta);
            if (py_val == NULL) {
                Py_DECREF(seq);
                Py_DECREF(py_name);
                return NULL;
            }

            if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                    module_globals, py_name, py_val)
                == -1) {
                // LCOV_EXCL_START
                Py_DECREF(seq);
                Py_DECREF(py_name);
                Py_DECREF(py_val);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(py_name);
            Py_DECREF(py_val);
        }
    }
    Py_DECREF(seq);
    Py_INCREF(Py_None);
    return Py_None;
}

typedef void (*function)(void);
struct functionlist {
    char*    name;
    function func;
};

static function _Nullable find_function(struct functionlist* functions, PyObject* name)
{
    while (functions->name != NULL) {
        if (PyObjC_is_ascii_string(name, functions->name)) {
            return functions->func;
        }
        functions++;
    }
    return NULL;
}

PyObject* _Nullable PyObjC_loadFunctionList(PyObject* self __attribute__((__unused__)),
                                            PyObject* _Nullable args,
                                            PyObject* _Nullable kwds)
{
    static char*         keywords[] = {"function_list", "module_globals", "functionInfo",
                                       "skip_undefined", NULL};
    PyObject*            pyFunctionsList;
    PyObject*            module_globals;
    PyObject*            functionInfo;
    int                  skip_undefined = 1;
    PyObject*            seq;
    Py_ssize_t           i, len;
    struct functionlist* function_list;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O!O!O|i", keywords, &PyCapsule_Type,
                                     &pyFunctionsList, &PyDict_Type, &module_globals,
                                     &functionInfo, &skip_undefined)) {
        return NULL;
    }

    function_list = PyCapsule_GetPointer(pyFunctionsList, "objc.__inline__");
    if (function_list == NULL) {
        /* NULL is always an error return from PyCapsule_GetPointer as the
         * API doesn't allow creating a capsule for a NULL pointer.
         */
        return NULL;
    }

    seq = PySequence_Fast(functionInfo, "functionInfo not a sequence");
    if (seq == NULL) {
        return NULL;
    }

    len = PySequence_Fast_GET_SIZE(seq);
    for (i = 0; i < len; i++) {
        PyObject* item = PySequence_Fast_GET_ITEM(seq, i);
        function  value;
        char*     signature;
        PyObject* name;
        PyObject* doc;
        PyObject* meta = NULL;

        if (!PyTuple_Check(item)) {
            PyErr_Format(PyExc_TypeError,
                         "item %" PY_FORMAT_SIZE_T "d has type %s not tuple", i,
                         Py_TYPE(item)->tp_name);
            Py_DECREF(seq);
            return NULL;
        }

        doc = NULL;
        if (!PyArg_ParseTuple(item, "Uy|O!O:functionInfo tuple", &name, &signature,
                              &PyUnicode_Type, &doc, &meta)) {
            Py_DECREF(seq);
            return NULL;
        }

        value = find_function(function_list, name);
        if (value == NULL) {
            if (!skip_undefined) {
                PyErr_Format(PyObjCExc_Error, "cannot find function %R", name);
                Py_DECREF(seq);
                return NULL;
            }

        } else {
            PyObject* py_val = PyObjCFunc_New(name, (void*)value, signature, doc, meta);
            if (py_val == NULL) {
                Py_DECREF(seq);
                return NULL;
            }

            if (PyDict_SetItem( // LCOV_BR_EXCL_LINE
                    module_globals, name, py_val)
                == -1) {
                // LCOV_EXCL_START
                Py_DECREF(seq);
                Py_DECREF(py_val);
                return NULL;
                // LCOV_EXCL_STOP
            }
            Py_DECREF(py_val);
        }
    }
    Py_DECREF(seq);
    Py_INCREF(Py_None);
    return Py_None;
}

NS_ASSUME_NONNULL_END
