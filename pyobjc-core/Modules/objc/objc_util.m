/*
 * Some utility functions...
 */

#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

NSNull* NSNull_null;
Class NSAutoreleasePool_class;

PyObject* PyObjCExc_Error;
PyObject* PyObjCExc_NoSuchClassError;
PyObject* PyObjCExc_InternalError;
PyObject* PyObjCExc_UnInitDeallocWarning; /* XXX: Drop in PyObjC 12 */
PyObject* PyObjCExc_ObjCRevivalWarning;
PyObject* PyObjCExc_LockError;
PyObject* PyObjCExc_BadPrototypeError;
PyObject* PyObjCExc_UnknownPointerError;
PyObject* PyObjCExc_DeprecationWarning;
PyObject* PyObjCExc_ObjCPointerWarning;
PyObject* PyObjCExc_ObjCSuperWarning;

PyObject* PyObjCNM_insert;
PyObject* PyObjCNM_readonly;
PyObject* PyObjCNM_copy;
PyObject* PyObjCNM_retain;
PyObject* PyObjCNM_nonatomic;
PyObject* PyObjCNM_dynamic;
PyObject* PyObjCNM_weak;
PyObject* PyObjCNM_collectable;
PyObject* PyObjCNM_getter;
PyObject* PyObjCNM_setter;
PyObject* PyObjCNM__pyobjc_info_;
PyObject* PyObjCNM_append;
PyObject* PyObjCNM_extend;
PyObject* PyObjCNM_timestamp;
PyObject* PyObjCNM_fromtimestamp;
PyObject* PyObjCNM_strftime;
PyObject* PyObjCNM_keys;
PyObject* PyObjCNM_clear;
PyObject* PyObjCNM_discard;
PyObject* PyObjCNM_add;
PyObject* PyObjCNM_values;
PyObject* PyObjCNM_description;
PyObject* PyObjCNM___get__;
PyObject* PyObjCNM_date_format_string;
PyObject* PyObjCNM_objc_memview_object;
PyObject* PyObjCNM_objc_NULL;
PyObject* PyObjCNM___new__;
PyObject* PyObjCNM_reason;
PyObject* PyObjCNM_name;
PyObject* PyObjCNM_userInfo;
PyObject* PyObjCNM__template;
PyObject* PyObjCNM_already_cfretained;
PyObject* PyObjCNM_already_retained;
PyObject* PyObjCNM_arguments;
PyObject* PyObjCNM_c_array_delimited_by_null;
PyObject* PyObjCNM_c_array_length_in_arg;
PyObject* PyObjCNM_c_array_length_in_result;
PyObject* PyObjCNM_c_array_of_fixed_length;
PyObject* PyObjCNM_c_array_of_variable_length;
PyObject* PyObjCNM_callable;
PyObject* PyObjCNM_callable_retained;
PyObject* PyObjCNM_deprecated;
PyObject* PyObjCNM_deref_result_pointer;
PyObject* PyObjCNM_free_result;
PyObject* PyObjCNM_initializer;
PyObject* PyObjCNM_full_signature;
PyObject* PyObjCNM_null_accepted;
PyObject* PyObjCNM_printf_format;
PyObject* PyObjCNM_retval;
PyObject* PyObjCNM_sel_of_type;
PyObject* PyObjCNM_suggestion;
PyObject* PyObjCNM_type;
PyObject* PyObjCNM_type_modifier;
PyObject* PyObjCNM_variadic;
PyObject* PyObjCNM___slots__;
PyObject* PyObjCNM___doc__;
PyObject* PyObjCNM_classmethod;
PyObject* PyObjCNM_hidden;
PyObject* PyObjCNM_return_unitialized_object;
PyObject* PyObjCNM_protocols;
PyObject* PyObjCNM___pyobjc_protocols__;
PyObject* PyObjCNM___del__;
PyObject* PyObjCNM_bundleForClass;
PyObject* PyObjCNM___useKVO__;
PyObject* PyObjCNM_typestr;
PyObject* PyObjCNM_classname;
PyObject* PyObjCNM___typestr__;
PyObject* PyObjCNM___module__;
PyObject* PyObjCNM___dict__;
PyObject* PyObjCNM_return_uninitialized_object;
PyObject* PyObjCNM__fields;
PyObject* PyObjCNM___match_args__;
PyObject* PyObjCNM___struct_pack__;
PyObject* PyObjCNM_pyobjcSetValue_;
PyObject* PyObjCNM_tzinfo;
PyObject* PyObjCNM_update;
PyObject* PyObjCNM_co_consts;
PyObject* PyObjCNM___call__;


int
PyObjCUtil_Init(PyObject* module)
{
    NSNull_null = [[NSNull null] retain];
    NSAutoreleasePool_class = [NSAutoreleasePool class];

#define NEW_EXC(identifier, name, base_class)                                            \
    identifier = PyErr_NewException("objc." name, base_class, NULL);                     \
    if (identifier == NULL)                                                              \
        return -1;                                                                       \
    Py_INCREF(identifier);                                                               \
    if (PyModule_AddObject(module, name, identifier) < 0)                                \
        return -1;

    NEW_EXC(PyObjCExc_Error, "error", NULL);
    NEW_EXC(PyObjCExc_NoSuchClassError, "nosuchclass_error", PyObjCExc_Error);
    NEW_EXC(PyObjCExc_InternalError, "internal_error", PyObjCExc_Error);
    NEW_EXC(PyObjCExc_UnInitDeallocWarning, "UninitializedDeallocWarning", PyExc_Warning); /* XXX */
    NEW_EXC(PyObjCExc_ObjCRevivalWarning, "RevivedObjectiveCObjectWarning",
            PyExc_Warning);
    NEW_EXC(PyObjCExc_LockError, "LockError", PyObjCExc_Error);
    NEW_EXC(PyObjCExc_BadPrototypeError, "BadPrototypeError", PyObjCExc_Error);
    NEW_EXC(PyObjCExc_UnknownPointerError, "UnknownPointerError", PyObjCExc_Error);
    NEW_EXC(PyObjCExc_DeprecationWarning, "ApiDeprecationWarning",
            PyExc_DeprecationWarning);
    NEW_EXC(PyObjCExc_ObjCPointerWarning, "ObjCPointerWarning", PyExc_Warning);
    NEW_EXC(PyObjCExc_ObjCSuperWarning, "ObjCSuperWarning", PyExc_Warning);

#undef NEW_EXC

#define NEW_STR(identifier, strvalue) do {                                               \
    identifier = PyUnicode_InternFromString(strvalue);                                   \
    if (identifier == NULL)                                                              \
        return -1;                                                                       \
    } while(0)

    NEW_STR(PyObjCNM_insert, "insert");
    NEW_STR(PyObjCNM_readonly, "readonly");
    NEW_STR(PyObjCNM_copy, "copy");
    NEW_STR(PyObjCNM_retain, "retain");
    NEW_STR(PyObjCNM_nonatomic, "nonatomic");
    NEW_STR(PyObjCNM_dynamic, "dynamic");
    NEW_STR(PyObjCNM_weak, "weak");
    NEW_STR(PyObjCNM_collectable, "collectable");
    NEW_STR(PyObjCNM_getter, "getter");
    NEW_STR(PyObjCNM_setter, "setter");
    NEW_STR(PyObjCNM_append, "append");
    NEW_STR(PyObjCNM_extend, "extend");
    NEW_STR(PyObjCNM_timestamp, "timestamp");
    NEW_STR(PyObjCNM_fromtimestamp, "fromtimestamp");
    NEW_STR(PyObjCNM_strftime, "strftime");
    NEW_STR(PyObjCNM_keys, "keys");
    NEW_STR(PyObjCNM_clear, "clear");
    NEW_STR(PyObjCNM_discard, "discard");
    NEW_STR(PyObjCNM_add, "add");
    NEW_STR(PyObjCNM_values, "values");
    NEW_STR(PyObjCNM_description, "description");
    NEW_STR(PyObjCNM___get__, "__get__");
    NEW_STR(PyObjCNM_date_format_string, "%s");
    NEW_STR(PyObjCNM_objc_memview_object, "objc.memview object");
    NEW_STR(PyObjCNM_objc_NULL, "objc.NULL");
    NEW_STR(PyObjCNM___new__, "__new__");
    NEW_STR(PyObjCNM_reason, "reason");
    NEW_STR(PyObjCNM_name, "name");
    NEW_STR(PyObjCNM_userInfo, "userInfo");;
    NEW_STR(PyObjCNM__pyobjc_info_, "_pyobjc_info_");
    NEW_STR(PyObjCNM__template, "_template");
    NEW_STR(PyObjCNM_already_cfretained, "already_cfretained");
    NEW_STR(PyObjCNM_already_retained, "already_retained");
    NEW_STR(PyObjCNM_arguments, "arguments");
    NEW_STR(PyObjCNM_c_array_delimited_by_null, "c_array_delimited_by_null");
    NEW_STR(PyObjCNM_c_array_length_in_arg, "c_array_length_in_arg");
    NEW_STR(PyObjCNM_c_array_length_in_result, "c_array_length_in_result");
    NEW_STR(PyObjCNM_c_array_of_fixed_length, "c_array_of_fixed_length");
    NEW_STR(PyObjCNM_c_array_of_variable_length, "c_array_of_variable_length");
    NEW_STR(PyObjCNM_callable, "callable");
    NEW_STR(PyObjCNM_callable_retained, "callable_retained");
    NEW_STR(PyObjCNM_deprecated, "deprecated");
    NEW_STR(PyObjCNM_deref_result_pointer, "deref_result_pointer");
    NEW_STR(PyObjCNM_free_result, "free_result");
    NEW_STR(PyObjCNM_initializer, "initializer");
    NEW_STR(PyObjCNM_full_signature, "full_signature");
    NEW_STR(PyObjCNM_null_accepted, "null_accepted");
    NEW_STR(PyObjCNM_printf_format, "printf_format");
    NEW_STR(PyObjCNM_retval, "retval");
    NEW_STR(PyObjCNM_sel_of_type, "sel_of_type");
    NEW_STR(PyObjCNM_suggestion, "suggestion");
    NEW_STR(PyObjCNM_type, "type");
    NEW_STR(PyObjCNM_type_modifier, "type_modifier");
    NEW_STR(PyObjCNM_variadic, "variadic");
    NEW_STR(PyObjCNM___slots__, "__slots__");
    NEW_STR(PyObjCNM___doc__, "__doc__");
    NEW_STR(PyObjCNM_classmethod, "classmethod");
    NEW_STR(PyObjCNM_hidden, "hidden");
    NEW_STR(PyObjCNM_return_unitialized_object, "return_unitialized_object");
    NEW_STR(PyObjCNM_protocols, "protocols");
    NEW_STR(PyObjCNM___pyobjc_protocols__, "__pyobjc_protocols__");
    NEW_STR(PyObjCNM___del__, "__del__");
    NEW_STR(PyObjCNM_bundleForClass, "bundleForClass");
    NEW_STR(PyObjCNM___useKVO__, "__useKVO__");
    NEW_STR(PyObjCNM_typestr, "typestr");
    NEW_STR(PyObjCNM_classname, "classname");
    NEW_STR(PyObjCNM___typestr__, "__typestr__");
    NEW_STR(PyObjCNM___module__, "__module__");
    NEW_STR(PyObjCNM___dict__, "__dict__");
    NEW_STR(PyObjCNM_return_uninitialized_object, "return_uninitialized_object");
    NEW_STR(PyObjCNM__fields, "_fields");
    NEW_STR(PyObjCNM___match_args__, "__match_args__");
    NEW_STR(PyObjCNM___struct_pack__, "__struct_pack__");
    NEW_STR(PyObjCNM_pyobjcSetValue_, "pyobjcSetValue_");
    NEW_STR(PyObjCNM_tzinfo, "tzinfo");
    NEW_STR(PyObjCNM_update, "update");
    NEW_STR(PyObjCNM_co_consts, "co_consts");
    NEW_STR(PyObjCNM___call__, "__call__");

#undef NEW_STR

    return 0;
}

static PyObject*
ObjCErr_PyExcForName(const char* _Nullable value)
{
    if (value == NULL) {
        return PyObjCExc_Error;
    } else if (strcmp(value, "NSRangeException") == 0) {
        return PyExc_IndexError;

    } else if (strcmp(value, "NSInvalidArgumentException") == 0) {
        return PyExc_ValueError;

    } else if (strcmp(value, "NSMallocException") == 0) {
        return PyExc_MemoryError;

    } else if (strcmp(value, "NSUnknownKeyException") == 0) {
        return PyExc_KeyError;
    }

    return PyObjCExc_Error;
}

void
PyObjCErr_FromObjC(NSObject* localException)
{
    NSDictionary* userInfo;
    PyObject*     dict;
    PyObject*     exception;
    PyObject*     v;
    PyObject*     exc_type;
    PyObject*     exc_value = NULL;
    PyObject*     exc_traceback = NULL;
    PyObject*     c_localException_name;
    PyObject*     c_localException_reason;

    /* XXX: add protection for ObjC exceptions */
    PyObjC_BEGIN_WITH_GIL
        if (![localException isKindOfClass:[NSException class]]) {
            /* We caught some random objects as the exception, do the minimal possible
             */
            PyErr_SetString(PyObjCExc_Error, "non-NSException object caught");

            PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
            PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

            PyObject* exc = id_to_python(localException);
            if (exc == NULL) { // LCOV_BR_EXCL_LINE
                PyErr_Clear(); // LCOV_EXCL_LINE
            } else { // LCOV_EXCL_LINE
                if (PyObject_SetAttrString( // LCOV_BR_EXCL_LINE
                        exc_value, "_pyobjc_exc_", exc) == -1) {
                    PyErr_Clear(); // LCOV_EXCL_LINE
                } // LCOV_EXCL_LINE
            }
            Py_CLEAR(exc);
            PyErr_Restore(exc_type, exc_value, exc_traceback);
        } else {
            exception =
                ObjCErr_PyExcForName([[(NSException*)localException name] UTF8String]);

            userInfo = [(NSException*)localException userInfo];
            if (userInfo) {
                id val;

                val = [userInfo objectForKey:@"__pyobjc_exc_type__"];
                if (val) {
                    id temp;
                    exc_type = id_to_python(val);
                    if (exc_type == NULL) { // LCOV_BR_EXCL_LINE
                        PyObjC_GIL_RETURNVOID; // LCOV_EXCL_LINE
                    }

                    temp = [userInfo objectForKey:@"__pyobjc_exc_value__"];
                    if (temp != nil) {
                        exc_value     = id_to_python(temp);
                        if (exc_value == NULL) { // LCOV_BR_EXCL_LINE
                            // LCOV_EXCL_START
                            Py_CLEAR(exc_type);
                            PyObjC_GIL_RETURNVOID;
                            // LCOV_EXCL_STOP
                        }
                    }

                    temp = [userInfo objectForKey:@"__pyobjc_exc_traceback__"];
                    if (temp != nil) {
                        exc_traceback     = id_to_python(temp);
                        if (exc_traceback == NULL) { // LCOV_BR_EXCL_LINE
                            // LCOV_EXCL_START
                            Py_CLEAR(exc_type);
                            Py_CLEAR(exc_value);
                            PyObjC_GIL_RETURNVOID;
                            // LCOV_EXCL_STOP
                        }
                    }

                    PyErr_Restore(exc_type, exc_value, exc_traceback);

                    PyObjC_GIL_RETURNVOID;
                } // LCOV_EXCL_LINE
            }

            c_localException_name = id_to_python([(NSException*)localException name]);
            if (c_localException_name == NULL) { // LCOV_BR_EXCL_LINE
                PyObjC_GIL_RETURNVOID;           // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

            c_localException_reason = id_to_python([(NSException*)localException reason]);
            if (c_localException_reason == NULL) { // LCOV_BR_EXCL_LINE
                Py_DECREF(c_localException_name);  // LCOV_EXCL_LINE
                PyObjC_GIL_RETURNVOID;             // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

            dict = PyDict_New();
            if (dict == NULL) {                     // LCOV_BR_EXCL_LINE
                Py_DECREF(c_localException_name);   // LCOV_EXCL_LINE
                Py_DECREF(c_localException_reason); // LCOV_EXCL_LINE
                PyObjC_GIL_RETURNVOID;              // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

            /* Ignore errors in setting up ``dict``, the exception state
             * will be replaced later.
             */
            if ( PyDict_SetItem( // LCOV_BR_EXCL_LINE
                    dict, PyObjCNM_name, c_localException_name) == -1) {
                PyErr_Clear(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            Py_DECREF(c_localException_name);

            if ( PyDict_SetItem( // LCOV_BR_EXCL_LINE
                    dict, PyObjCNM_reason, c_localException_reason) == -1) {
                PyErr_Clear(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            Py_DECREF(c_localException_reason);
            if (userInfo) {
                v = id_to_python(userInfo);
                if (v != NULL) {
                    if ( PyDict_SetItem( // LCOV_BR_EXCL_LINE
                            dict, PyObjCNM_userInfo, v) == -1) {
                        PyErr_Clear(); // LCOV_EXCL_LINE
                    } // LCOV_EXCL_LINE
                    Py_DECREF(v);
                } else {           // LCOV_BR_EXCL_LINE
                    PyErr_Clear(); // LCOV_EXCL_LINE
                }
            } else {
                if ( PyDict_SetItem( // LCOV_BR_EXCL_LINE
                        dict, PyObjCNM_userInfo, Py_None) == -1) {
                    PyErr_Clear(); // LCOV_EXCL_LINE
                } // LCOV_EXCL_LINE
            }

            const char* name   = [[(NSException*)localException name] UTF8String];
            const char* reason = [[(NSException*)localException reason] UTF8String];
            if (reason != NULL) {
                PyErr_Format(exception, "%s - %s", name ? name : "<null>", reason);
            } else {
                PyErr_SetString(exception, name ? name : "<null>"); // LCOV_BR_EXCL_LINE
            }
            PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
            PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

            if ( PyObject_SetAttr( // LCOV_BR_EXCL_LINE
                    exc_value, PyObjCNM__pyobjc_info_, dict) == -1) {
                PyErr_Clear(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            Py_CLEAR(dict);
            if ( PyObject_SetAttr( // LCOV_BR_EXCL_LINE
                    exc_value, PyObjCNM_name, c_localException_name) == -1) {
                PyErr_Clear(); // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE
            PyErr_Restore(exc_type, exc_value, exc_traceback);
        }
    PyObjC_END_WITH_GIL
} // LCOV_EXCL_LINE

static NSException* _Nullable python_exception_to_objc(void)
{
    PyObject*            exc_type;
    PyObject*            exc_value;
    PyObject*            exc_traceback;
    PyObject*            args;
    PyObject*            repr;
    PyObject*            typerepr;
    NSException*         val;
    NSMutableDictionary* userInfo = nil;

    assert(PyErr_Occurred());

    PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
    if (exc_type == NULL) { // LCOV_BR_EXCL_LINE
        return nil;         // LCOV_EXCL_LINE
    }

    PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

    args = PyObject_GetAttrString(exc_value, "_pyobjc_exc_");
    if (args == NULL) {
        PyErr_Clear();
    } else {
        id result;

        if (depythonify_python_object(args, &result) == -1) {
            PyErr_Clear();
            result = [[NSException alloc] initWithName:NSInternalInconsistencyException
                                                reason:@"Cannot convert Python exception"
                                              userInfo:nil];
        }
        return result;
    }

    args = PyObject_GetAttrString(exc_value, "_pyobjc_info_");
    if (args == NULL) {
        PyErr_Clear();

    } else {
        /* This may be an exception that started out in
         * Objective-C code.
         */
        PyObject* v;
        int r;
        NSString* reason = nil;
        NSString* name   = nil;

        r = PyDict_GetItemRef(args, PyObjCNM_reason, &v);
        switch (r) { // LCOV_BR_EXCL_LINE
        case -1:
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        case 1:
            if (depythonify_python_object(v, &reason) < 0) {
                PyErr_Clear();
            }
            Py_DECREF(v);
        }

        r = PyDict_GetItemRef(args, PyObjCNM_name, &v);
        switch (r) { // LCOV_BR_EXCL_LINE
        case -1:
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        case 1:
            if (depythonify_python_object(v, &name) < 0) {
                PyErr_Clear();
            }
            Py_DECREF(v);
        }

        r = PyDict_GetItemRef(args, PyObjCNM_userInfo, &v);
        switch (r) { // LCOV_BR_EXCL_LINE
        case -1:
            // LCOV_EXCL_START
            PyErr_Clear();
            break;
            // LCOV_EXCL_STOP
        case 1:
            if (depythonify_python_object(v, &userInfo) < 0) {
                PyErr_Clear();
            }
            Py_DECREF(v);
        }


        if (name && reason) {
            val = [NSException exceptionWithName:name reason:reason userInfo:userInfo];
            Py_DECREF(args);
            Py_XDECREF(exc_type);
            Py_XDECREF(exc_value);
            Py_XDECREF(exc_traceback);

            return val;
        }
    }

    repr     = PyObject_Str(exc_value);
    typerepr = PyObject_Str(exc_type);
    userInfo = [NSMutableDictionary dictionaryWithCapacity:3];

    /* XXX: For recent enough versions of Python we don't need to store all three */
    [userInfo setObject:[[[OC_PythonObject alloc] initWithPyObject:exc_type] autorelease]
                 forKey:@"__pyobjc_exc_type__"];

    if (exc_value != NULL) {
        [userInfo
            setObject:[[[OC_PythonObject alloc] initWithPyObject:exc_value] autorelease]
               forKey:@"__pyobjc_exc_value__"];
    }

    if (exc_traceback != NULL) {
        [userInfo setObject:[[[OC_PythonObject alloc] initWithPyObject:exc_traceback]
                                autorelease]
                     forKey:@"__pyobjc_exc_traceback__"];
    }

    NSObject* oc_typerepr = nil;
    NSObject* oc_repr     = nil;

    if (typerepr) {
        if (depythonify_python_object(typerepr, &oc_typerepr) == -1) { // LCOV_BR_EXCL_LINE
            /* Ignore errors in conversion */
            PyErr_Clear(); // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE
    }
    if (repr) {
        if (depythonify_python_object(repr, &oc_repr) == -1) { // LCOV_BR_EXCL_LINE
            /* Ignore errors in conversion */
            PyErr_Clear(); // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE
    }

    val = [NSException
        exceptionWithName:@"OC_PythonException"
                   reason:[NSString stringWithFormat:@"%@: %@", oc_typerepr, oc_repr]
                 userInfo:userInfo];

    Py_XDECREF(typerepr);
    Py_XDECREF(repr);

    if (PyObjC_Verbose) {
        PyErr_Restore(exc_type, exc_value, exc_traceback);
        PySys_WriteStderr("PyObjC: Converting exception to Objective-C:");
        PyErr_Print();

    } else {
        Py_DECREF(exc_type);
        Py_XDECREF(exc_value);
        Py_XDECREF(exc_traceback);
    }
    return val;
}

void __attribute__((__noreturn__))
PyObjCErr_ToObjCWithGILState(PyGILState_STATE* _Nonnull state)
{
    NSException* exc = python_exception_to_objc();
    if (exc == nil)                // LCOV_BR_EXCL_LINE
        PyObjCErr_InternalError(); // LCOV_EXCL_LINE

    if (state) {
        PyGILState_Release(*state);
    }
    @throw exc;
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunreachable-code"
    __builtin_unreachable();
#pragma clang diagnostic pop
}

char* _Nullable PyObjCUtil_Strdup(const char* value)
{
    Py_ssize_t len;
    char*      result;

    len    = strlen(value);
    result = PyMem_Malloc(len + 1);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    memcpy(result, value, len);
    result[len] = 0;
    return result;
}

NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks = {
    NULL, NULL, NULL, NULL, NULL, NULL,
};

NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks = {
    NULL,
    NULL,
    NULL,
};

#define SHOULD_FREE 1
#define SHOULD_IGNORE 2

void
PyObjC_FreeCArray(int code, Py_buffer* view)
{
    if (code == SHOULD_FREE) {
        PyBuffer_Release(view);
    }
}

static char struct_elem_code(const char* typestr);

static char
array_typestr(PyObject* array)
{
    PyObject* typecode;
    PyObject* bytes;
    char      res;

    typecode = PyObject_GetAttrString(array, "typecode");
    if (typecode == NULL) { // LCOV_BR_EXCL_LINE
        /* Should not happen: ``array`` is an array.array
         * which always has this attribute.
         */
        return '\0'; // LCOV_EXCL_LINE
    }

    if (PyUnicode_Check(typecode)) { // LCOV_BR_EXCL_LINE
        bytes = PyUnicode_AsEncodedString(typecode, NULL, NULL);
        if (bytes == NULL) { // LCOV_BR_EXCL_LINE
            /* Should not happen: array.array typecode is an
             * ascii string.
             */
            return '\0'; // LCOV_EXCL_LINE
        }

    } else {
        /* Should not happen: array.array typecode is an
         * ascii string.
         */
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_TypeError, "typecode not a string");
        return '\0';
        // LCOV_EXCL_STOP
    }

    res = *PyBytes_AS_STRING(bytes);
    Py_DECREF(typecode);
    Py_DECREF(bytes);

    return res;
}

static char
array_elem_code(const char* typestr)
{
    char res = '\0';

    typestr++;

    while (isdigit(*typestr))
        typestr++;

    if (*typestr == _C_ARY_E) { // LCOV_BR_EXCL_LINE
        return '\0'; // LCOV_EXCL_LINE
    }

    switch (*typestr) {
    case _C_ARY_B:
        res = array_elem_code(typestr);
        if (res == '\0') {
            return '\0';
        }

        break;

    case _C_STRUCT_B:
        res = struct_elem_code(typestr);
        if (res == '\0') {
            return '\0';
        }
        break;

    case _C_UNION_B:
    case _C_VECTOR_B:
        return '\0';

    default:
        res = *typestr;
    }

    const char* next = PyObjCRT_SkipTypeSpec(typestr);
    if (next == NULL) { // LCOV_BR_EXCL_LINE
        return '\0'; // LCOV_EXCL_LINE
    }
    if (*next++ != _C_ARY_E) {
        return  '\0';
    }
    return res;
}

static char
struct_elem_code(const char* start_typestr)
{
    char res = '\0';
    char tmp;

    const char* _Nullable typestr = start_typestr;
    typestr++;

    while (*typestr != '=' && *typestr != _C_STRUCT_E) {
        typestr++;
    }

    if (*typestr == _C_STRUCT_E) { // LCOV_BR_EXCL_LINE
        /* Cannot happen because this function is
         * called after calculating the size and checking
         * the size is larger than 0.
         */
        return '\0'; // LCOV_EXCL_LINE
    }
    typestr++;

    while (typestr && *typestr != _C_STRUCT_E && *typestr != '\0') {
        switch (*typestr) {
        case _C_ARY_B:
            tmp = array_elem_code(typestr);
            if (tmp == '\0') {
                return '\0';
            }

            if (res == '\0') {
                res = tmp;

            } else if (tmp != res) {
                return '\0';
            }
            break;

        case _C_STRUCT_B:
            tmp = struct_elem_code(typestr);
            if (tmp == '\0') {
                return '\0';
            }

            if (res == '\0') {
                res = tmp;

            } else if (tmp != res) {
                return '\0';
            }
            break;

        case _C_UNION_B:
        case _C_VECTOR_B:
            return '\0';

        default:
            tmp = *typestr;
            if (res != '\0' && res != tmp) {
                return '\0';
            }
            res = tmp;
        }

        typestr = PyObjCRT_SkipTypeSpec(typestr);
    }
    if (typestr == NULL || *typestr != _C_STRUCT_E) {
        return '\0';
    }

    return res;
}

/*
 * Return YES iff 'array_code' and 'type_code'
 * are compatible. Both are the encodings for
 * an element, but in their native encoding:
 *
 * - array_code is the "type code" for an array.array
 * - type_code is the encoding for an ObjC type (_C_...)
 */
static BOOL
code_compatible(char array_code, char type_code)
{
    _Static_assert(sizeof(wchar_t) == 4, "sizeof(wchar_t)");
    _Static_assert(sizeof(long) == 8, "sizeof(long)");

    switch (array_code) {
    case 'b':
        switch (type_code) {
        case _C_CHR:
        case _C_CHAR_AS_INT:
        case _C_CHAR_AS_TEXT:
        case _C_BOOL:
        case _C_NSBOOL:
            return YES;
        } // LCOV_EXCL_LINE

    case 'B':
        switch (type_code) {
        case _C_CHAR_AS_TEXT:
        case _C_UCHR:
            return YES;
        case _C_CHAR_AS_INT:
            /* This is not correct, but kept for backward
             * compatibility.
             */
            return YES;
        } // LCOV_EXCL_LINE

    case 'u':
#if PY_VERSION_HEX >= 0x030d0000
    case 'w':
#endif
        return type_code == _C_INT;

    case 'h':
        switch (type_code) {
        case  _C_SHT:
        case  _C_UNICHAR:
            return YES;
        }

    case 'H':
        return type_code == _C_USHT;

    case 'i':
        return type_code == _C_INT;

    case 'I':
        return type_code == _C_UINT;

    case 'l':
    case 'q':
        switch (type_code) {
        case _C_LNG:
        case _C_LNG_LNG:
            return YES;
        } // LCOV_EXCL_LINE

    case 'L':
    case 'Q':
        switch (type_code) {
        case _C_ULNG:
        case _C_ULNG_LNG:
            return YES;
        } // LCOV_EXCL_LINE

    case 'f':
        return type_code == _C_FLT;

    case 'd':
        return type_code == _C_DBL;

    }

    /* Should not get here, the switch
     * above is up-to-date with the array.array
     * type codes as of Python 3.13
     */
    return NO; // LCOV_EXCL_LINE
}

/*
 * Convert a Python object to an array of 'elementType'. The array should
 * contain 'pythonCount' elements, Py_None or NULL is accepted and will result
 * in converting the entire Python sequence.
 *
 * The pythonList should either be a python sequence with appropriate entries,
 * an array.array whose element-types match the element-types of the
 * 'elementType' or an appropriately typed and shaped numeric array.
 */
int
PyObjC_PythonToCArray(BOOL writable, BOOL exactSize, const char* elementType,
                      PyObject* pythonList, void* _Nullable* _Nonnull array,
                      Py_ssize_t* _Nullable size, PyObject* _Nullable* _Nonnull bufobj,
                      Py_buffer* view)
{
    Py_ssize_t eltsize = PyObjCRT_SizeOfType(elementType);
    Py_ssize_t i;
    int        r;

    if (eltsize == -1) {
        return -1;
    }
    if (eltsize == 0 && ((elementType[0] == _C_STRUCT_B || elementType[0] == _C_ARY_B))) {
        PyErr_Format(PyExc_ValueError, "0 sized struct or array: %s", elementType);
        return -1;
    }


    if ((eltsize == 1 || eltsize == 0)
        && !(*elementType == _C_NSBOOL || *elementType == _C_BOOL
             || *elementType == _C_CHAR_AS_INT)) {
        /* A simple byte-array */

        /* NOTE: PyUnicode is explicitly excluded because it
         * implemenents the character buffer interface giving access
         * to the raw implementation. That's almost always not want
         * you want.
         */

        int have_buffer;

        if (PyUnicode_Check(pythonList)) {
            PyErr_Format(PyExc_TypeError, "Expecting byte-buffer, got %s",
                         Py_TYPE(pythonList)->tp_name);
            return -1;
        }

        have_buffer = PyObject_GetBuffer(pythonList, view,
                                         writable ? PyBUF_CONTIG : PyBUF_CONTIG_RO);
        if (have_buffer == -1) {
            if (writable) {
                /* Ensure that the expected semantics still work
                 * when the passed in buffer is read-only
                 */
                PyErr_Clear();
                PyObject* byte_array;

                if (PyObject_GetBuffer(pythonList, view, PyBUF_CONTIG_RO) == -1) {
                    return -1;
                }

                if (size == NULL || *size == -1) {
                    byte_array = PyByteArray_FromStringAndSize(view->buf, view->len);
                } else {
                    if ((exactSize && *size != view->len)
                        || (!exactSize && *size > view->len)) {
                        PyErr_Format(PyExc_ValueError,
                                     "Requesting buffer of %" PY_FORMAT_SIZE_T
                                     "d, have buffer "
                                     "of %" PY_FORMAT_SIZE_T "d",
                                     *size, view->len);
                        return -1;
                    }

                    byte_array = PyByteArray_FromStringAndSize(view->buf, *size);
                }

                PyBuffer_Release(view);

                if (byte_array == NULL) { // LCOV_BR_EXCL_LINE
                    return -1; // LCOV_EXCL_LINE
                }

                if (PyObject_GetBuffer(byte_array, view, PyBUF_CONTIG) == -1) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(byte_array);
                    return -1;
                    // LCOV_EXCL_STOP
                }

                Py_DECREF(byte_array); /* Reference is kept by the view */
                *array = view->buf;
                return SHOULD_FREE;
            }
        }

        if (have_buffer != -1) {
            if (size == NULL) {
                *array  = view->buf;
                *bufobj = pythonList;
                Py_INCREF(pythonList);

            } else if (*size == -1) {
                *array  = view->buf;
                *size   = view->len;
                *bufobj = pythonList;
                Py_INCREF(pythonList);

            } else {
                if ((exactSize && *size != view->len)
                    || (!exactSize && *size > view->len)) {
                    PyErr_Format(PyExc_ValueError,
                                 "Requesting buffer of %" PY_FORMAT_SIZE_T
                                 "d, have buffer "
                                 "of %" PY_FORMAT_SIZE_T "d",
                                 *size, view->len);
                    return -1;
                }

                *array  = view->buf;
                *bufobj = pythonList;
                Py_INCREF(pythonList);
            }
            return SHOULD_FREE;
        }

        PyErr_Clear();
    }

    if (*elementType == _C_UNICHAR && PyUnicode_Check(pythonList)) {
        PyObject* bytes_array;

        bytes_array = PyUnicode_AsUTF16String(pythonList);

        if (bytes_array == NULL) {
            return -1;
        }

        /* 2 bytes per UniChar, and subtract 1 to ignore the BOM at the start */
        Py_ssize_t bufsize = (PyBytes_Size(bytes_array) / 2) - 1;

        if (size == NULL) {
            /* pass */
        } else if (*size == -1) {
            *size = bufsize;

        } else if ((exactSize && *size != bufsize) || (!exactSize && *size > bufsize)) {
            /* NOTE: The size check is performed after the conversion to UTF16 to avoid
             * problems with characters outside of the BMP.
             */
            PyErr_Format(PyExc_ValueError,
                         "Requesting unicode buffer of %" PY_FORMAT_SIZE_T
                         "d, have unicode buffer "
                         "of %" PY_FORMAT_SIZE_T "d",
                         *size, bufsize);
            return -1;
        }

        if (writable) {
            PyObject* tmp = PyByteArray_FromObject(bytes_array);
            Py_DECREF(bytes_array);
            if (tmp == NULL) {
                return -1;
            }

            bytes_array = tmp;
        }

        if (PyObject_GetBuffer(bytes_array, view,
                               writable ? PyBUF_CONTIG : PyBUF_CONTIG_RO)
            == -1) {
            Py_DECREF(bytes_array);
            return -1;
        }

        *array = (void*)((char*)view->buf + 2);
        Py_DECREF(bytes_array); /* Kept alive by view */
        return SHOULD_FREE;
    }

    /* A more complex array */

    if (PyObject_CheckBuffer(pythonList)) {
        /* An object that implements the new-style buffer interface.
         * Use the buffer interface description to check if the buffer
         * type is compatible with what we expect.
         *
         * Specifically:
         * - If the C code expects an array of basic types:
         *   the buffer must be a single-dimensional array of
         *   a compatible type.
         * - If the C code expects and array of structures:
         *   The python array must be two dimensional, one row
         *   in the python array corresponds to one struct "instance"
         * - If the C code expects a multi-dimensional array:
         *   the python buffer must have a compatible dimension.
         *
         * The array must be large enough and  mustn't contain holes
         * in the fragment that gets used by us.
         */
    }

    if (PyObjC_ArrayTypeCheck(pythonList)) {
        /* An array.array. Only convert if the typestr describes an
         * simple type of the same type as the array, or a struct/array
         * containing only elements of the type of the array.
         */
        char code = array_typestr(pythonList);
        if (code_compatible(code, *elementType)) {
            /* Simple array, ok */

        } else if (*elementType == _C_ARY_B) {
            /* Array of arrays, 'code' must be the same as the
             * element-type of the array.
             */
            if (!code_compatible(code, array_elem_code(elementType))) {
                PyErr_Format(PyExc_ValueError,
                             "type mismatch between array.array "
                             "of %c and and C array of %s",
                             code, elementType);
                return -1;
            }

        } else if (*elementType == _C_STRUCT_B) {
            /* Array of structs, 'code' must be the same as the
             * the field-types of the structs (that is, the struct
             * must contain one or more fields of type 'code').
             */
            if (!code_compatible(code, struct_elem_code(elementType))) {
                PyErr_Format(PyExc_ValueError,
                             "type mismatch between array.array "
                             "of %c and and C array of %s",
                             code, elementType);
                return -1;
            }

        } else {
            PyErr_Format(PyExc_ValueError,
                         "type mismatch between array.array "
                         "of %c and and C array of %s",
                         code, elementType);
            return -1;
        }

        if (PyObject_GetBuffer(pythonList, view,
                               writable ? PyBUF_CONTIG : PyBUF_CONTIG_RO)
            == -1) {
            return -1;
        }

        if (eltsize == 0) {
            PyErr_SetString(PyExc_ValueError, "array.array with elements without a size");
            return -1;
        }

        if ((view->len % eltsize) != 0) {
            PyErr_SetString(PyExc_ValueError, "Badly shaped array.array");
            return -1;
        }

        *array = view->buf;

        if (size == NULL) {
            /* pass */

        } else if (*size == -1) {
            *size = view->len / eltsize;

        } else {
            Py_ssize_t bufsize = view->len / eltsize;

            if ((exactSize && *size != bufsize) || (!exactSize && *size > bufsize)) {
                PyErr_Format(PyExc_ValueError,
                             "Requesting buffer of %" PY_FORMAT_SIZE_T "d, have buffer "
                             "of %" PY_FORMAT_SIZE_T "d",
                             *size, bufsize);
                return -1;
            }
            *array = view->buf;
        }
        *bufobj = pythonList;
        Py_INCREF(pythonList);
        return SHOULD_FREE;

    } else {
        Py_ssize_t seqlen;
        Py_ssize_t pycount;
        PyObject*  seq;

        if (*elementType == _C_NSBOOL) {
            if (PyBytes_Check(pythonList)) {
                PyErr_Format(PyExc_ValueError, "Need array of BOOL, got byte string");
                return -1;
            }

        } else if (*elementType == _C_CHAR_AS_INT) {
            if (PyBytes_Check(pythonList)) {
                PyErr_Format(PyExc_ValueError,
                             "Need array of small integers, got byte string");
                return -1;
            }
        }

        seq = PyObjCSequence_Tuple(pythonList, "converting to a C array");
        if (seq == NULL) {
            return -1;
        }

        seqlen = PyTuple_GET_SIZE(seq);
        if (size == NULL || *size == -1) {
            pycount = seqlen;

        } else {
            pycount = *size;
        }

        if ((exactSize && seqlen != pycount) || (!exactSize && seqlen < pycount)) {
            Py_DECREF(seq);
            if (exactSize) {
                PyErr_Format(PyExc_ValueError,
                             "expecting %" PY_FORMAT_SIZE_T "d values "
                             "got %" PY_FORMAT_SIZE_T "d",
                             pycount, seqlen);
            } else {
                PyErr_Format(PyExc_ValueError,
                             "too few values (%" PY_FORMAT_SIZE_T "d) expecting at "
                             "least %" PY_FORMAT_SIZE_T "d",
                             seqlen, pycount);
            }
            return -1;
        }

        PyObject* bytes_array = PyByteArray_FromStringAndSize(NULL, 0);
        if (bytes_array == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(seq);
            return -1;
            // LCOV_EXCL_STOP
        }

        if (PyByteArray_Resize( // LCOV_BR_EXCL_LINE
                    bytes_array, eltsize * pycount) == -1) {
            // LCOV_EXCL_START
            Py_DECREF(bytes_array);
            Py_DECREF(seq);
            return -1;
            // LCOV_EXCL_STOP
        }

        if (PyObject_GetBuffer( // LCOV_BR_EXCL_LINE
                    bytes_array, view, PyBUF_CONTIG) == -1) {
            // LCOV_EXCL_START
            Py_DECREF(bytes_array);
            Py_DECREF(seq);
            return -1;
            // LCOV_EXCL_STOP
        }
        *array = view->buf;
        Py_DECREF(bytes_array); /* kept alive by view */

        if (size) {
            *size = pycount;
        }

        *bufobj = NULL;

        for (i = 0; i < pycount; i++) {
            PyObject* item = PyTuple_GET_ITEM(seq, i);

            r = depythonify_c_value(elementType, item, ((char*)*array) + (i * eltsize));
            if (r == -1) {
                Py_DECREF(seq);
                PyBuffer_Release(view);
                *array = NULL;
                return -1;
            }
        }
        return SHOULD_FREE;
    }
}

PyObject* _Nullable PyObjC_CArrayToPython(const char* elementType, const void* array,
                                          Py_ssize_t size)
{
    PyObject*  result;
    Py_ssize_t i;
    Py_ssize_t eltsize;

    eltsize = PyObjCRT_SizeOfType(elementType);
    if (eltsize == -1) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    if (eltsize == 1 || eltsize == 0) {
        if (*elementType == _C_CHAR_AS_TEXT) {
            return PyBytes_FromStringAndSize(array, size);
        }

        if (*elementType != _C_NSBOOL && *elementType != _C_BOOL
            && *elementType != _C_CHAR_AS_INT) {
            /* Special case for buffer-like objects */
            return PyBytes_FromStringAndSize(array, size);
        }
    } // LCOV_EXCL_LINE

    if (*elementType == _C_UNICHAR) {
        int byteorder = 0;
        result        = PyUnicode_DecodeUTF16(array, size * 2, NULL, &byteorder);
        return result;
    }

    result = PyTuple_New(size);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    for (i = 0; i < size; i++) {
        PyObject* elt = pythonify_c_value(elementType, array);
        if (elt == NULL) {
            Py_DECREF(result);
            return NULL;
        }

        PyTuple_SET_ITEM(result, i, elt);
        array = ((char*)array) + eltsize;
    }

    return result;
}

int
PyObjC_IsPythonKeyword(const char* word)
{
    /*
     * We cheat a little: this list only contains those keywords that
     * are actually used in Cocoa.
     */
    static const char* keywords[] = {"class", "raise", "from", NULL};
    const char**       cur;

    for (cur = keywords; *cur != NULL; cur++) {
        if (strcmp(word, *cur) == 0) {
            return 1;
        }
    }
    return 0;
}

int
PyObjCRT_SimplifySignature(const char* signature, char* buf, size_t buflen)
{
    const char* cur;
    const char* end;
    const char* next;

    cur  = signature;
    *buf = '\0';

    while (*cur != '\0') {
        next = end = PyObjCRT_SkipTypeSpec(cur);
        if (end == NULL) {
            return -1;
        }
        end -= 1;
        while (end != cur && isdigit(*end)) {
            end--;
        }
        end++;

        if ((size_t)(end - cur) > buflen) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_Error, "signature too long");
            return -1;
            // LCOV_EXCL_STOP
        }

        memcpy(buf, cur, end - cur);
        buflen -= (end - cur);
        buf += (end - cur);
        *buf = '\0';
        cur  = next;
    }
    return 0;
}

PyObject* _Nullable PyObjC_CArrayToPython2(const char* elementType, const void* array,
                                           Py_ssize_t size, bool alreadyRetained,
                                           bool alreadyCFRetained)
{
    PyObject*  result;
    Py_ssize_t i;
    Py_ssize_t eltsize;

    if (size == -1) {
        /* XXX: Can this happen? */
        size = 0;
    }

    eltsize = PyObjCRT_SizeOfType(elementType);
    if (eltsize == -1) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    if (eltsize == 1 || eltsize == 0) {
        if (*elementType == _C_CHAR_AS_TEXT) {
            return PyBytes_FromStringAndSize(array, size);
        }
        if (*elementType != _C_NSBOOL && *elementType != _C_BOOL
            && *elementType != _C_CHAR_AS_INT) {
            /* Special case for buffer-like objects */
            return PyBytes_FromStringAndSize(array, size);
        }
    }

    if (*elementType == _C_UNICHAR) {
        int byteorder = 0;
        result        = PyUnicode_DecodeUTF16(array, size * 2, NULL, &byteorder);
        return result;
    }

    result = PyTuple_New(size);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }

    for (i = 0; i < size; i++) {
        PyObject* elt = pythonify_c_value(elementType, array);
        if (elt == NULL) {
            Py_DECREF(result);
            return NULL;
        }

        if (alreadyRetained) {
            [*(id*)array release];

        } else if (alreadyCFRetained) {
            CFRelease(*(id*)array);
        }

        PyTuple_SET_ITEM(result, i, elt);
        array = ((char*)array) + eltsize;
    }

    return result;
}

int
PyObjCObject_Convert(PyObject* object, void* pvar)
{
    int r;
    r = depythonify_c_value(@encode(id), object, (id*)pvar);
    if (r == -1) {
        return 0;
    } else {
        return 1;
    }
}

int
PyObjCClass_Convert(PyObject* object, void* pvar)
{
    if (!PyObjCClass_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expected objective-C class");
        return 0;
    }

    *(Class*)pvar = PyObjCClass_GetClass(object);
    if (*(Class*)pvar == NULL) // LCOV_BR_EXCL_LINE
        return 0; // LCOV_EXCL_LINE
    return 1;
}

int
PyObjC_is_ascii_string(PyObject* unicode_string, const char* ascii_string)
{
    if (!PyUnicode_IS_ASCII(unicode_string)) {
        return 0;

    } else {
        return strcmp((const char*)(PyUnicode_DATA(unicode_string)), ascii_string) == 0;
    }
}

int
PyObjC_is_ascii_prefix(PyObject* unicode_string, const char* ascii_string, size_t n)
{

    size_t uni_sz = PyUnicode_GetLength(unicode_string);

    if (uni_sz < n) {
        return 0;
    }

    if (!PyUnicode_IS_ASCII(unicode_string)) {
        return 0;
    }

    return strncmp((const char*)(PyUnicode_DATA(unicode_string)), ascii_string, n) == 0;
}

PyObject* _Nullable PyObjC_AdjustSelf(PyObject* object)
{
    if (PyType_Check(object)
        && PyType_IsSubtype((PyTypeObject*)object, &PyObjCClass_Type)) {
        PyObject* temp = PyObjCClass_ClassForMetaClass(object);
        if (temp == NULL) {
            Py_DECREF(object);
            PyErr_Format(PyObjCExc_Error, "Cannot find class for metaclass %R", object);
            return NULL;
        }
        Py_INCREF(temp);
        Py_DECREF(object);
        return temp;
    }
    return object;
}

int
PyObjCRT_SignaturesEqual(const char* sig1, const char* sig2)
{
    char buf1[1024];
    char buf2[1024];
    int  r;

    /* Return 0 if the two signatures are not equal */
    if (strcmp(sig1, sig2) == 0)
        return 1;

    /* For some reason compiler-generated signatures contain numbers that
     * are not used by the runtime. These are irrelevant for our comparison
     */
    r = PyObjCRT_SimplifySignature(sig1, buf1, sizeof(buf1));
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }

    r = PyObjCRT_SimplifySignature(sig2, buf2, sizeof(buf2));
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }
    r = PyObjC_RemoveInternalTypeCodes(buf1);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }
    r = PyObjC_RemoveInternalTypeCodes(buf2);
    if (r == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }
    return strcmp(buf1, buf2) == 0;
}

PyObject* _Nullable PyObjC_SELToPythonName(SEL sel)
{
    const char*  selname = sel_getName(sel);
    size_t selname_len = strlen(selname);

    if (PyObjC_IsPythonKeyword(selname)) {
        return PyUnicode_FromFormat("%s__", selname);

    } else {
        PyObject* result = PyUnicode_New(selname_len, 127);
        if (result == NULL) { // LCOV_BR_EXCL_LINE
            return NULL; // LCOV_EXCL_LINE
        }

        for (Py_ssize_t idx = 0; *selname != '\0'; selname++, idx++) {
            int r = PyUnicode_WriteChar(result, idx, *selname == ':'?'_':*selname);
            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_CLEAR(result);
                return NULL;
                // LCOV_EXCL_STOP
            }
        }

        return result;
    }
}

int
PyObjC_CheckArgCount(PyObject* callable, size_t min_args, size_t max_args, size_t nargsf)
{
    size_t nargs = PyVectorcall_NARGS(nargsf);
    if (nargs < min_args || nargs > max_args) {
        if (min_args == max_args) {
            if (min_args == 0) {
                PyErr_Format(PyExc_TypeError, "%R expected no arguments, got %zu",
                             callable, nargs);
            } else {
                PyErr_Format(PyExc_TypeError, "%R expected %zu arguments, got %zu",
                             callable, min_args, nargs);
            }
        } else {
            PyErr_Format(PyExc_TypeError,
                         "%R expected between %zu and %zu arguments, got %zu", callable,
                         min_args, max_args, nargs);
        }
        return -1;
    }
    return 0;
}

int
PyObjC_CheckNoKwnames(PyObject* callable, PyObject* _Nullable kwnames)
{
    if (kwnames == NULL)
        return 0;
    if (PyObject_Size(kwnames) == 0)
        return 0;
    if (PyErr_Occurred())
        return -1;
    PyErr_Format(PyExc_TypeError, "%R does not accept keyword arguments", callable);
    return -1;
}

PyObject* _Nullable PyObjC_MakeCVoidP(void* ptr)
{
    PyObject* c_void_p = PyObjC_get_c_void_p();
    if (c_void_p == NULL) {
        return NULL;
    }

    PyObject* pyptr = PyLong_FromVoidPtr(ptr);
    if (pyptr == NULL) { // LCOV_BR_EXCL_LINE
        return NULL; // LCOV_EXCL_LINE
    }
    PyObject* args[2] = {NULL, pyptr};
    PyObject* res =
        PyObject_Vectorcall(c_void_p, args + 1, 1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_DECREF(pyptr);
    return res;
}

bool
version_is_deprecated(int version)
{
    /*
     * Use a local variable to avoid a race condition when using a free-threaded
     * build.
     */
    int depcrecation_version = PyObjC_DeprecationVersion;
    return (depcrecation_version && version && version <= depcrecation_version);
}

/* PyObjC uses a number of typecode descriptors that aren't available in
 * the objc runtime. Remove these from the type string (inline).
 *
 */
static int
tc2tc(char* buf)
{
    /* Skip pointer declarations and annotations */
    for (;;) {
        switch (*buf) {
        case _C_PTR:
        case _C_IN:
        case _C_OUT:
        case _C_INOUT:
        case _C_ONEWAY:
        case _C_CONST:
            buf++;
            break;
        default:
            goto exit;
        }
    }

exit:
    switch (*buf) {
    case _C_NSBOOL:
#ifdef __arm64__
        *buf = _C_BOOL;
#else
        *buf = _C_CHR;
#endif
        break;

    case _C_CHAR_AS_INT:
    case _C_CHAR_AS_TEXT:
        *buf = _C_CHR;
        break;

    case _C_UNICHAR:
        *buf = _C_SHT;
        break;

    case _C_STRUCT_B:
        while (*buf != _C_STRUCT_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_STRUCT_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf + 1, '"');
                if (buf == NULL) {
                    return -1;
                }
                buf++;
            }
            tc2tc(buf);
            char* new_buf = (char*)PyObjCRT_SkipTypeSpec(buf);
            if (new_buf == NULL) {
                return -1;
            }
            buf = new_buf;
        }
        break;

    case _C_UNION_B:
        while (*buf != _C_UNION_E && *buf && *buf++ != '=') {
        }
        while (buf && *buf && *buf != _C_UNION_E) {
            if (*buf == '"') {
                /* embedded field name */
                buf = strchr(buf + 1, '"');
                if (buf == NULL) {
                    return -1;
                }
                buf++;
            }
            tc2tc(buf);
            char* new_buf = (char*)PyObjCRT_SkipTypeSpec(buf);
            if (new_buf == NULL) {
                return -1;
            }
            buf = new_buf;
        }
        break;

    case _C_ARY_B:
        while (isdigit(*++buf))
            ;
        tc2tc(buf);
        break;
    }
    return 0;
}

/*
 * XXX: _C_VECTOR... requires completely removing part of the buffer
 */
int
PyObjC_RemoveInternalTypeCodes(char* buf)
{
    char* _Nullable cur = buf;

    while (*cur) {
        if (tc2tc(cur) == -1) {
            PyErr_SetString(PyObjCExc_Error, "invalid type encoding");
            return -1;
        }
        cur = (char*)PyObjCRT_SkipTypeSpec(cur);
        if (cur == NULL) {
            return -1;
        }
    }
    return 0;
}

PyObject* _Nullable
PyObjCSequence_Tuple(PyObject* value, const char* context)
{
    PyObject* result = PySequence_Tuple(value);
    if (result == NULL) {
#if PY_VERSION_HEX >= 0x030c0000
        PyObject* cause = PyErr_GetRaisedException();

        PyErr_SetString(PyExc_TypeError, context);

        PyObject* exc = PyErr_GetRaisedException();
        PyException_SetCause(exc, cause);
        PyErr_SetRaisedException(exc);
#else /* PY_VERSION_HEX < 0x030c0000 */
        PyObject *type, *cause, *traceback;
        PyErr_Fetch(&type, &cause, &traceback);
        PyErr_NormalizeException(&type, &cause, &traceback);
        if (traceback != NULL) {
            if (PyException_SetTraceback(cause, traceback) == -1) {
                return NULL;
            }
        }
        Py_CLEAR(type);
        Py_CLEAR(traceback);

        PyErr_SetString(PyExc_TypeError, context);
        PyObject* exc;

        PyErr_Fetch(&type, &exc, &traceback);
        PyErr_NormalizeException(&type, &exc, &traceback);
        if (traceback != NULL) {
            if (PyException_SetTraceback(exc, traceback) == -1) {
                return NULL;
            }
        }

        PyException_SetCause(exc, cause);
        PyErr_Restore(type, exc, traceback);
#endif /* PY_VERSION_HEX < 0x030c0000 */
        return NULL;
    }

    return result;
}

/*
 * XXX: Make this a static variable set during module init
 */
PyObject* _Nullable PyObjC_get_c_void_p(void)
{
#ifdef Py_GIL_DISABLED
    static PyMutex c_void_p_mutex = { 0 };
#endif
    static PyObject* c_void_p = NULL;
    if (c_void_p == NULL) {
#ifdef Py_GIL_DISABLED
        PyMutex_Lock(&c_void_p_mutex);
        if (c_void_p != NULL) {
            PyMutex_Unlock(&c_void_p_mutex);
            return c_void_p;
        }
#endif
        PyObject* mod_ctypes = PyImport_ImportModule("ctypes");
        if (mod_ctypes == NULL) { // LCOV_BR_EXCL_LINE
            /* ctypes is not available */
            // LCOV_EXCL_START
#ifdef Py_GIL_DISABLED
            PyMutex_Unlock(&c_void_p_mutex);
#endif
            return NULL;
            // LCOV_EXCL_STOP
        }

        c_void_p = PyObject_GetAttrString(mod_ctypes, "c_void_p");
        Py_DECREF(mod_ctypes);
        if (c_void_p == NULL) { // LCOV_BR_EXCL_LINE
            /* invalid or incomplete module */
            // LCOV_EXCL_START
#ifdef Py_GIL_DISABLED
            PyMutex_Unlock(&c_void_p_mutex);
#endif
            return NULL;
            // LCOV_EXCL_STOP
        }
#ifdef Py_GIL_DISABLED
        PyMutex_Unlock(&c_void_p_mutex);
#endif
    } // LCOV_BR_EXCL_LINE
    return c_void_p;
}

NS_ASSUME_NONNULL_END
