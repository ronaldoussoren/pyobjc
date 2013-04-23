#include "pyobjc.h"

static PyObjCMethodSignature* new_methodsignature(const char*);

/*
 * TODO:
 * - If this works out: als create templates for byref in/out/inout types
 * - Compile metadata into partial MethodSignature struct in "PyObjC_registerMetaData"
 *   (set 'tmpl' bit in all entries). Be careful to not cause memory corruption when
 *   existing metadata is replaced (but leak memory instead)
 */

#define TC(VAL)  [VAL] = { VAL, 0 }
static const char _static_typecodes[256][2] = {
    TC(_C_VOID),
    TC(_C_ID),
    TC(_C_CLASS),
    TC(_C_SEL),
    TC(_C_CHR),
    TC(_C_UCHR),
    TC(_C_SHT),
    TC(_C_USHT),
    TC(_C_BOOL),
    TC(_C_INT),
    TC(_C_UINT),
    TC(_C_LNG),
    TC(_C_ULNG),
    TC(_C_FLT),
    TC(_C_DBL),
    TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG),
    TC(_C_CHAR_AS_TEXT),
    TC(_C_CHAR_AS_INT),
    TC(_C_NSBOOL),
    TC(_C_UNICHAR),
};
#undef TC

static const char _block_typecode[] = { _C_ID, _C_UNDEF, 0 };

#define TC(VAL) [VAL] = { .type = _static_typecodes[VAL], .tmpl = 1, .allowNULL = 1 }
static const struct _PyObjC_ArgDescr descr_templates[256] = {
    TC(_C_VOID),
    TC(_C_ID),
    TC(_C_CLASS),
    TC(_C_SEL),
    TC(_C_CHR),
    TC(_C_UCHR),
    TC(_C_SHT),
    TC(_C_USHT),
    TC(_C_BOOL),
    TC(_C_INT),
    TC(_C_UINT),
    TC(_C_LNG),
    TC(_C_ULNG),
    TC(_C_FLT),
    TC(_C_DBL),
    TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG),
    TC(_C_CHAR_AS_TEXT),
    TC(_C_CHAR_AS_INT),
    TC(_C_NSBOOL),
    TC(_C_UNICHAR),
};
#undef TC

static const struct _PyObjC_ArgDescr block_template = {
    .type = _block_typecode,
    .tmpl = 1,
    .allowNULL = 1,
};


static PyObject*
sig_str(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    PyObject* v = PyObjCMethodSignature_AsDict(self);
    if (v == NULL) {
        PyErr_Clear();
        return PyText_FromString(self->signature);

    } else {
        PyObject* r = PyObject_Repr(v);
        Py_DECREF(v);
        return r;
    }
}

static void
sig_dealloc(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    Py_ssize_t i;

    if (self->signature) {
        PyMem_Free((char*)self->signature);
    }

    if (!self->rettype->tmpl) {
        if (self->rettype->typeOverride) {
            PyMem_Free((char*)self->rettype->type);
        }
        PyMem_Free(self->rettype);
    }

    for (i = 0; i < Py_SIZE(self); i++) {
        if (self->argtype[i] == NULL) continue;
        if (self->argtype[i]->tmpl) continue;

        if (self->argtype[i]->typeOverride) {
            PyMem_Free((char*)self->argtype[i]->type);
        }

        if (self->argtype[i]->sel_type != NULL) {
            PyMem_Free((char*)self->argtype[i]->sel_type);
        }
        PyMem_Free(self->argtype[i]);
    }
    PyObject_Free(self);
}


PyTypeObject PyObjCMethodSignature_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name        = "objc._method_signature",
    .tp_basicsize   = sizeof(PyObjCMethodSignature),
    .tp_itemsize    = sizeof(struct _PyObjC_ArgDescr*),
    .tp_dealloc     = sig_dealloc,
    .tp_repr        = sig_str,
    .tp_str         = sig_str,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
};

static int
determine_if_shortcut(PyObjCMethodSignature* methinfo)
{
    /*
     * Set shortcut_signature and shortcut_argbuf_size if appropriate,
     * clear otherwise
     *
     * These should be set if all arguments are basic types (no functions, no byreference, ...)
     * and method parts of the function setup code can be skipped.
     *
     * Note that shortcut_argbuf_size has a limited size, this will also not work when
     * there are a lot, or large, arguments/return values.
     */
    /* TODO: simple pass-by-reference objects args should work (NSError** arguments) */
   /* FIXME: structs/unions/... also use byref */
    Py_ssize_t byref_in_count = 0, byref_out_count = 0, plain_count = 0, argbuf_len = 0;
    BOOL variadic_args = NO;

    methinfo->shortcut_signature = NO;
    methinfo->shortcut_argbuf_size = 0;

    if (methinfo == NULL || methinfo->variadic) {
        return 0;
    }
#ifdef PyObjC_DEBUG
    for (Py_ssize_t i = 0; i < Py_SIZE(methinfo); i++) {
        PyObjC_Assert(methinfo->argtype[i] != NULL, -1);
        PyObjC_Assert(methinfo->argtype[i]->type != NULL, -1);
    }
    PyObjC_Assert(methinfo->rettype != NULL, -1);
    PyObjC_Assert(methinfo->rettype->type != NULL, -1);
#endif /* PyObjC_DEBUG */

    int r = PyObjCFFI_CountArguments(
            methinfo, 0, &byref_in_count, &byref_out_count, &plain_count, &argbuf_len, &variadic_args);
    if (r == -1) {
        PyErr_Clear();
        return 0;
    }

    if (byref_in_count || byref_out_count || variadic_args) {
        return 0;
    }

    if (argbuf_len >= 1 << 12) {
        return 0;
    }

    if (variadic_args) {
        return 0;
    }

    methinfo->shortcut_signature = YES;
    methinfo->shortcut_argbuf_size = (unsigned int)argbuf_len;
    return 0;
}

static struct _PyObjC_ArgDescr* alloc_meta(struct _PyObjC_ArgDescr* tmpl)
{
    struct _PyObjC_ArgDescr* retval = PyMem_Malloc(sizeof(*retval));
    if (retval == NULL) {
        PyErr_NoMemory();
        return NULL;
    }
    retval->type = tmpl?tmpl->type:NULL;
    retval->typeOverride = NO;
    retval->ptrType = PyObjC_kPointerPlain;
    retval->allowNULL = YES;
    retval->arraySizeInRetval = NO;
    retval->printfFormat = NO;
    retval->alreadyRetained = NO;
    retval->alreadyCFRetained = NO;
    retval->callableRetained = NO;
    retval->tmpl = NO;
    retval->callable = NULL;
    retval->sel_type = NULL;
    return retval;
}

static int
setup_type(struct _PyObjC_ArgDescr* meta, const char* type)
{
    const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);

    if (unlikely(*withoutModifiers == _C_ARY_B)) {
            meta->ptrType = PyObjC_kFixedLengthArray;
            meta->arrayArg = 0;
            const char* c = withoutModifiers + 1;
            const char* e;
            while (isdigit(*c)) {
                meta->arrayArg *= 10;
                meta->arrayArg += *c - '0';
                c++;
            }

            e = PyObjCRT_SkipTypeSpec(c);
            meta->typeOverride = YES;
            meta->type = PyMem_Malloc((withoutModifiers - type) + (e - c) + 3);
            if (meta->type == NULL) {
                return -1;
            }

            char* cur;
            if (unlikely(type != withoutModifiers)) {
                memcpy((void*)(meta->type), type, withoutModifiers-type);
                cur = (char*)(meta->type + (withoutModifiers-type));
            } else {
                cur = (char*)(meta->type);
                *cur++ = _C_IN;
            }
            *cur++ = _C_PTR;
            memcpy(cur, c, e-c);
            cur[e-c] = '\0';

    } else {
        meta->type = type;
        meta->typeOverride = NO;
    }
    return 0;
}

static PyObjCMethodSignature*
new_methodsignature(const char* signature)
{
    Py_ssize_t nargs;
    const char* cur;
    PyObjCMethodSignature* retval;

    PyObjC_Assert(signature != NULL, NULL);

    /* Skip return-type */
    cur = PyObjCRT_SkipTypeSpec(signature);

    nargs = 0;
    for ( ; cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
        nargs++;
    }
    retval = PyObject_NewVar(PyObjCMethodSignature,
            &PyObjCMethodSignature_Type, nargs /*+1*/);

    if (retval == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    for (Py_ssize_t i = 0; i < nargs; i++) {
        retval->argtype[i] = NULL;
    }

    Py_SIZE(retval) = nargs;
    retval->suggestion = NULL;
    retval->variadic = NO;
    retval->free_result = NO;
    retval->shortcut_signature = NO;
    retval->shortcut_argbuf_size = 0;
    retval->null_terminated_array = NO;
    retval->signature = PyObjCUtil_Strdup(signature);
    if (retval->signature == NULL) {
        Py_DECREF(retval);
        return NULL;
    }

    cur = PyObjCRT_SkipTypeQualifiers(retval->signature);
    PyObjC_Assert(cur != NULL, NULL);
    if (unlikely(cur[0] == _C_ID && cur[1] == _C_UNDEF)) {
        retval->rettype = (__typeof__(retval->rettype))&block_template;
    } else {
        retval->rettype = (__typeof__(retval->rettype))&descr_templates[*(unsigned char*)(cur)];
    }
    if (unlikely(retval->rettype->type == NULL)) {
        retval->rettype = alloc_meta(NULL);
        if (retval->rettype == NULL) {
            Py_DECREF(retval);
            return NULL;
        }

        /* Ignore type specifiers for methods returning void. Mostly needed
         * to avoid crapping out one (oneway void) methods.
         */
        PyObjC_Assert(retval->signature != NULL, NULL);
        if (setup_type(retval->rettype, cur) < 0) {
            Py_DECREF(retval);
            return NULL;
        }
        PyObjC_Assert(retval->rettype->type != NULL, NULL);
    }
    PyObjC_Assert(retval->rettype->type != NULL, NULL);

    cur = PyObjCRT_SkipTypeSpec(retval->signature);
    nargs = 0;
    for ( ; cur && *cur; cur = PyObjCRT_SkipTypeSpec(cur)) {
        if (unlikely(*cur == _C_CONST)) {
            /* Ignore a 'const' qualifier, not used by the bridge */
            cur++;
        }
        if (unlikely(cur[0] == _C_ID && cur[1] == _C_UNDEF)) {
            retval->argtype[nargs] = (__typeof__(retval->argtype[nargs]))&block_template;
        } else {
            retval->argtype[nargs] = (__typeof__(retval->argtype[nargs]))&descr_templates[*(unsigned char*)cur];
        }
        if (unlikely(retval->argtype[nargs]->type == NULL)) {
            retval->argtype[nargs] = alloc_meta(NULL);
            if (unlikely(retval->argtype[nargs] == NULL)) {
                Py_DECREF(retval);
                return NULL;
            }
            PyObjC_Assert(cur != NULL, NULL);
            if (setup_type(retval->argtype[nargs], cur) < 0) {
                Py_DECREF(retval);
                return NULL;
            }
            PyObjC_Assert(retval->argtype[nargs]->type != NULL, NULL);
        }

        nargs++;
    }


#ifdef PyObjC_DEBUG
    PyObjC_Assert(Py_SIZE(retval) == nargs, NULL);
    for (Py_ssize_t i = 0; i < Py_SIZE(retval); i++) {
        PyObjC_Assert(retval->argtype[i] != NULL, NULL);
        PyObjC_Assert(retval->argtype[i]->type != NULL, NULL);
    }
    PyObjC_Assert(retval->rettype != NULL, NULL);
    PyObjC_Assert(retval->rettype->type != NULL, NULL);
#endif /* PyObjC_DEBUG */

    if (determine_if_shortcut(retval) < 0) {
        Py_DECREF(retval);
        return NULL;
    }

    return retval;
}




char*
PyObjC_NSMethodSignatureToTypeString(
        NSMethodSignature* sig, char* buf, size_t buflen)
{
    char* result = buf;
    char* end;
    NSUInteger arg_count = [sig numberOfArguments];
    NSUInteger i;
    size_t r;

    r = snprintf(buf, buflen, "%s", [sig methodReturnType]);
    if (r > buflen) {
        return NULL;
    }

    end = (char*)PyObjCRT_SkipTypeSpec(buf);
    *end = '\0';
    buflen -= (end - buf);
    buf = end;

    for (i = 0; i < arg_count; i++) {
        r = snprintf(buf, buflen, "%s", [sig getArgumentTypeAtIndex:i]);
        if (r > buflen) {
            return NULL;
        }

        end = (char*)PyObjCRT_SkipTypeSpec(buf);
        buflen -= (end - buf);
        buf = end;
    }

    return result;
}

static PyObject* registry = NULL;

int
PyObjC_registerMetaData(PyObject* class_name, PyObject* selector,
                            PyObject* metadata)
{
    if (registry == NULL) {
        registry = PyObjC_NewRegistry();
        if (registry == NULL) {
            return -1;
        }
    }
    return PyObjC_AddToRegistry(registry, class_name, selector, metadata);
}


/*
 * Return values:
 *  0: OK
 * -1: error
 * -2: 'descr' is template, but would have to be updated.
 */
static int setup_meta(struct _PyObjC_ArgDescr* descr, PyObject* meta, BOOL is_native)
{
    PyObject* d;
    char typeModifier = 0;

    PyObjC_Assert(descr->type != NULL, -1);

    if (meta == Py_None) {
        return 0;
    }

    if (meta != NULL && !PyDict_Check(meta)) {
        PyObject* r = PyObject_Repr(meta);
        if (r == NULL) {
            return -1;
        }

        PyErr_Format(PyExc_TypeError, "metadata of type %s: %s",
                Py_TYPE(meta)->tp_name,
                PyText_AsString(r));
        Py_DECREF(r);

        return -1;
    }

    PyObjC_Assert(descr->allowNULL, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "null_accepted");
        if (d == NULL || PyObject_IsTrue(d)) {
            /* pass */
        } else {
            if (descr->tmpl) return -2;
            descr->allowNULL = NO;
        }
    }


    if (meta) {
        d = PyDict_GetItemString(meta, "already_retained");
        if (d && PyObject_IsTrue(d)) {
            if (descr->tmpl && !descr->alreadyRetained) return -2;
            descr->alreadyRetained = YES;
        } else {
            if (descr->tmpl && descr->alreadyRetained) return -2;
            descr->alreadyRetained = NO;
        }
    }

    PyObjC_Assert(!descr->alreadyCFRetained, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "already_cfretained");
        if (d && PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;
            descr->alreadyCFRetained = YES;
        } else {
            /* pass */
        }
    }

    PyObjC_Assert(!descr->callableRetained, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "callable_retained");
        if (d == NULL || PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;
            descr->callableRetained = YES;
        } else {
            /* pass */
        }
    }

    PyObjC_Assert(descr->sel_type == NULL, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "sel_of_type");
        if (d) {
            if (PyUnicode_Check(d)) {
                PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
                if (bytes == NULL) {
                    return -1;
                }

                if (descr->tmpl) {
                    Py_DECREF(bytes);
                    return -2;
                }

                descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
                Py_DECREF(bytes);
                if (descr->sel_type == NULL) {
                    return -1;
                }

            } else if (PyBytes_Check(d)) {
                if (descr->tmpl) return -2;
                descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(d));
                if (descr->sel_type == NULL) {
                    return -1;
                }
            }
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "callable");
        if (d) {
            if (descr->tmpl) return -2;

            /* Make up a dummy signature, will be overridden bij
             * the metadata.
             */
            char buffer[64];
            PyObject* a = PyDict_GetItemString(d, "arguments");

            if (a != NULL) {
                Py_ssize_t i, len = PyDict_Size(a);
                if (len == -1) {
                    return -1;
                }

                for (i = 0; i < len; i++) {
                    buffer[i] = _C_ID;
                }
                buffer[len] = _C_ID;
                buffer[len+1] = '\0';

            } else {
                buffer[0] = _C_ID;
                buffer[1] = '\0';
            }

            descr->callable = PyObjCMethodSignature_WithMetaData(buffer, d, NO);
            if (descr->callable == NULL) {
                return -1;
            }
        }
    }

    PyObjC_Assert(!descr->arraySizeInRetval, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "c_array_length_in_result");
        if (d != NULL && PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;

            descr->arraySizeInRetval = YES;
        }
    }

    PyObjC_Assert(!descr->printfFormat, -1);
    if (meta) {
        d = PyDict_GetItemString(meta, "printf_format");
        if (d != NULL && PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;
            descr->printfFormat = YES;
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "c_array_delimited_by_null");
        if (d != NULL && PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;
            descr->ptrType = PyObjC_kNullTerminatedArray;
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "c_array_of_fixed_length");
        if (d != NULL) {
            if (PyLong_Check(d)) {
                if (descr->tmpl) return -2;
                descr->ptrType = PyObjC_kFixedLengthArray;
                descr->arrayArg = PyLong_AsLong(d);
                descr->arrayArgOut = descr->arrayArg;
                if (PyErr_Occurred()) {
                    return -1;
                }
            }
#if PY_MAJOR_VERSION == 2
            else if (PyInt_Check(d)) {
                if (descr->tmpl) return -2;
                descr->ptrType = PyObjC_kFixedLengthArray;
                descr->arrayArg = PyInt_AsLong(d);
                descr->arrayArgOut = descr->arrayArg;
            }
#endif
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "c_array_of_variable_length");
        if (d != NULL && PyObject_IsTrue(d)) {
            if (descr->tmpl) return -2;
            descr->ptrType = PyObjC_kVariableLengthArray;
            descr->arrayArg = 0;
            descr->arrayArg = 0;
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "c_array_length_in_arg");
        if (d != NULL) {
            if (PyLong_Check(d)) {
                if (descr->tmpl) return -2;
                descr->ptrType = PyObjC_kArrayCountInArg;
                descr->arrayArg = PyLong_AsLong(d);
                if (PyErr_Occurred()) {
                    return -1;
                }
                descr->arrayArgOut = descr->arrayArg;

#if PY_MAJOR_VERSION == 2
            } else if (PyInt_Check(d)) {
                if (descr->tmpl) return -2;
                descr->ptrType = PyObjC_kArrayCountInArg;
                descr->arrayArg = PyInt_AsLong(d);
                descr->arrayArgOut = descr->arrayArg;
#endif
            } else if (PyTuple_Check(d)) {
                if (descr->tmpl) return -2;

                if (PyTuple_GET_SIZE(d) == 1) {
                    descr->ptrType = PyObjC_kArrayCountInArg;
                    if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
                        descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
                    } else {
#if PY_MAJOR_VERSION == 2
                        descr->arrayArg = PyInt_AsLong(PyTuple_GET_ITEM(d, 0));
#else
                        PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
                    }
                    if (PyErr_Occurred()) {
                        return -1;
                    }
                    descr->arrayArgOut = descr->arrayArg;
                } else if (PyTuple_GET_SIZE(d) >= 2) {
                    descr->ptrType = PyObjC_kArrayCountInArg;
                    if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
                        descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
                    } else {
#if PY_MAJOR_VERSION == 2
                        descr->arrayArg = PyInt_AsLong(PyTuple_GET_ITEM(d, 0));
#else
                        PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
                    }

                    if (PyErr_Occurred()) {
                        return -1;
                    }

                    if (PyLong_Check(PyTuple_GET_ITEM(d, 1))) {
                        descr->arrayArgOut = PyLong_AsLong(PyTuple_GET_ITEM(d, 1));
                    } else {
#if PY_MAJOR_VERSION == 2
                        descr->arrayArgOut = PyInt_AsLong(PyTuple_GET_ITEM(d, 1));
#else
                        PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
#endif
                    }
                    if (PyErr_Occurred()) {
                        return -1;
                    }
                }
            }
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "type_modifier");
        if (d != NULL) {
            if (PyUnicode_Check(d)) {
                PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
                if (bytes == NULL) {
                    return -1;
                }
                if (descr->tmpl) {
                    Py_DECREF(bytes);
                    return -2;
                }
                typeModifier = *PyBytes_AsString(bytes);
                Py_DECREF(bytes);
#if PY_MAJOR_VERSION == 2
            } else if (PyString_Check(d)) {
                if (descr->tmpl) return -2;
                typeModifier = *PyString_AsString(d);
#else
            } else if (PyBytes_Check(d)) {
                if (descr->tmpl) return -2;
                typeModifier = *PyBytes_AsString(d);
#endif
            }
        }
    }

    if (meta) {
        d = PyDict_GetItemString(meta, "type");

    } else {
        d = NULL;
    }

    if (d
        && (
#if PY_MAJOR_VERSION == 2
          PyString_Check(d) ||
#else
          PyBytes_Check(d) ||
#endif
          PyUnicode_Check(d))
        ) {

        PyObject* bytes = NULL;

        if (descr->tmpl) return -2;

        if (PyUnicode_Check(d)) {
            bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
            if (bytes == NULL) {
                return -1;
            }

#if PY_MAJOR_VERSION == 2
        } else if (PyString_Check(d)) {
            bytes = d; Py_INCREF(bytes);
#else /* PY_MAJOR_VERSION == 3 */

        } else if (PyBytes_Check(d)) {
            bytes = d; Py_INCREF(bytes);

#endif /* PY_MAJOR_VERSION == 3 */

        } else {
            PyErr_SetString(PyExc_SystemError, "Inconsistent if-case");
            return -1;
        }

        const char* type = PyBytes_AsString(bytes);

        if (is_native && !PyObjC_signatures_compatible(descr->type, type)) {
            /* The new signature is not compatible enough, ignore the
             * override.
             */
            type = descr->type;
        }

        char* tp = PyMem_Malloc(strlen(type)+2);
        if (tp == NULL) {
            Py_XDECREF(bytes);
            PyErr_NoMemory();
            return -1;
        }

        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);
        PyObjC_Assert(*withoutModifiers != _C_ARY_B, -1);
        if (typeModifier != '\0') {
            /* Skip existing modifiers, we're overriding those */
            strcpy(tp+1, withoutModifiers);
            tp[0] = typeModifier;
        } else {
            strcpy(tp, type);
        }
        PyObjC_Assert(tp != NULL, -1);
        descr->typeOverride = YES;
        descr->type = tp;
        Py_XDECREF(bytes);

    } else {
        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
        PyObjC_Assert(*withoutModifiers != _C_ARY_B, -1);
        if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID &&
                descr->ptrType == PyObjC_kPointerPlain) {

            /* Plain old void*, ignore type modifiers */

        } else if (typeModifier != '\0') {
            if (descr->tmpl) return -2;

            char* tp = PyMem_Malloc(strlen(descr->type)+2);
            if (tp == NULL) {
                PyErr_NoMemory();
                return -1;
            }

            if (descr->typeOverride) {
                PyMem_Free((void*)(descr->type));
                descr->type = NULL;
            }

            /* Skip existing modifiers, we're overriding those */
            strcpy(tp+1, withoutModifiers);
            tp[0]  = typeModifier;
            PyObjC_Assert(tp != NULL, -1);
            descr->typeOverride = YES;
            descr->type = tp;
        }
    }

    return 0;
}

PyObjCMethodSignature*
PyObjCMethodSignature_WithMetaData(const char* signature, PyObject* metadata, BOOL is_native)
{
    PyObjCMethodSignature* methinfo;
    PyObject* v;
    ssize_t i;

    PyObjC_Assert(signature != NULL, NULL);

    methinfo = new_methodsignature(signature);
    if (methinfo == NULL) {
        return NULL;
    }

    if (metadata != NULL && !PyDict_Check(metadata)) {
        metadata = NULL;
    }


    if (metadata) {
        PyObject* retval = PyDict_GetItemString(metadata, "retval");

        if (retval != NULL) {
            int r = setup_meta(methinfo->rettype, retval, is_native);
            if (r == -1) {
                Py_DECREF(methinfo);
                return NULL;

            } else if (r == -2) {
                methinfo->rettype = alloc_meta(methinfo->rettype);
                if (methinfo->rettype == NULL) {
                    Py_DECREF(methinfo);
                    return NULL;
                }
                r = setup_meta(methinfo->rettype, retval, is_native);
                if (r == -1) {
                    Py_DECREF(methinfo);
                    return NULL;
                }
                PyObjC_Assert(r != -2, NULL);
            }

            if (retval != NULL) {
                PyObject* av = PyDict_GetItemString(metadata, "free_result");
                if (av && PyObject_IsTrue(av)) {
                    methinfo->free_result = YES;
                }
                Py_XDECREF(av);
            }
        }
    }

    if (metadata) {
        PyObject* args = PyDict_GetItemString(metadata, "arguments");
        if (args != NULL && !PyDict_Check(args)) {
            args = NULL;
        }

        if (args != NULL) {
            for (i = 0; i < Py_SIZE(methinfo); i++) {
                PyObject* k = PyInt_FromLong(i);
                PyObject* d;
                int r;

                if (args) {
                    d = PyDict_GetItem(args, k);
                    Py_DECREF(k);

                } else {
                    /* No metadata, hence no need to call setup_meta */
                    continue;
                }

                PyObjC_Assert(methinfo->argtype[i]->allowNULL, NULL);
                r = setup_meta(methinfo->argtype[i], d, is_native);
                if (r == -1) {
                    Py_DECREF(methinfo);
                    return NULL;

                } else if (r == -2) {
                    methinfo->argtype[i] = alloc_meta(methinfo->argtype[i]);
                    if (methinfo->argtype[i] == NULL) {
                        Py_DECREF(methinfo);
                        return NULL;
                    }
                    r = setup_meta(methinfo->argtype[i], d, is_native);
                    if (r == -1) {
                        Py_DECREF(methinfo);
                        return NULL;
                    }
                    PyObjC_Assert(r != -2, NULL);
                }

            }
        }

        v = PyDict_GetItemString(metadata, "suggestion");
        if (v) {
            methinfo->suggestion = v;
            Py_INCREF(v);
        }

        methinfo->null_terminated_array = NO;
        v = PyDict_GetItemString(metadata, "c_array_delimited_by_null");
        if (v && PyObject_IsTrue(v)) {
            methinfo->null_terminated_array = YES;
        }

        methinfo->arrayArg = -1;
        v = PyDict_GetItemString(metadata, "c_array_length_in_arg");
        if (v) {
            if (PyLong_Check(v)) {
                methinfo->arrayArg = (int)PyLong_AsLong(v);
                if (PyErr_Occurred()) {
                    return NULL;
                }
            }
#if PY_MAJOR_VERSION == 2
            else if (PyInt_Check(v)) {
                methinfo->arrayArg = (int)PyInt_AsLong(v);
            }
#endif
        }

        methinfo->variadic = NO;
        v = PyDict_GetItemString(metadata, "variadic");
        if (v && PyObject_IsTrue(v)) {
            methinfo->variadic = YES;

            if ((methinfo->suggestion == NULL)
                        && (!methinfo->null_terminated_array)
                        && (methinfo->arrayArg == -1)) {
                for (i = 0; i < Py_SIZE(methinfo); i++) {
                    if (methinfo->argtype[i]->printfFormat) {
                        goto done;
                    }
                }

                /* No printf-format argument, therefore the method is
                 * not supported
                 */
                methinfo->suggestion = PyText_FromString("Variadic functions/methods are not supported");
                if (methinfo->suggestion == NULL) {
                    Py_DECREF(methinfo);
                    return NULL;
                }
            }
        }
    }

done:
#ifdef PyObjC_DEBUG
    for (Py_ssize_t i = 0; i < Py_SIZE(methinfo); i++) {
        PyObjC_Assert(methinfo->argtype[i] != NULL, NULL);
        PyObjC_Assert(methinfo->argtype[i]->type != NULL, NULL);
    }
    PyObjC_Assert(methinfo->rettype != NULL, NULL);
    PyObjC_Assert(methinfo->rettype->type != NULL, NULL);
#endif /* PyObjC_DEBUG */

    if (determine_if_shortcut(methinfo) < 0) {
        Py_DECREF(methinfo);
        return NULL;
    }

    return methinfo;
}


PyObjCMethodSignature* PyObjCMethodSignature_ForSelector(
        Class cls, BOOL isClassMethod, SEL sel, const char* signature,
        BOOL is_native)
{
    PyObjCMethodSignature* methinfo;
    PyObject* metadata;

    metadata = PyObjC_FindInRegistry(registry, cls, sel);

    methinfo =  PyObjCMethodSignature_WithMetaData(signature, metadata, is_native);
    if (isClassMethod) {
        const char* nm  = sel_getName(sel);
        if (strncmp(nm, "new", 3) == 0 && ((nm[3] == 0) || isupper(nm[3]))) {
            if (methinfo->rettype->tmpl) {
                methinfo->rettype = alloc_meta(methinfo->rettype);
                if (methinfo->rettype == NULL) {
                    Py_XDECREF(methinfo);
                    Py_XDECREF(metadata);
                    return NULL;
                }
            }
            methinfo->rettype->alreadyRetained = YES;
        }
    }

#ifdef PyObjC_DEBUG
    for (Py_ssize_t i = 0; i < Py_SIZE(methinfo); i++) {
        PyObjC_Assert(methinfo->argtype[i] != NULL, NULL);
        PyObjC_Assert(methinfo->argtype[i]->type != NULL, NULL);
    }
    PyObjC_Assert(methinfo->rettype != NULL, NULL);
    PyObjC_Assert(methinfo->rettype->type != NULL, NULL);
#endif /* PyObjC_DEBUG */

    Py_XDECREF(metadata);
    return methinfo;
}

static PyObject*
argdescr2dict(struct _PyObjC_ArgDescr* descr)
{
    PyObject* result;
    PyObject* v;
    const char* end;
    int r;

    result = PyDict_New();
    if (result == NULL) return NULL;

    /*
     * FromStringAndSize because the type is a segment of the full
     * method signature.
     */
    end = PyObjCRT_SkipTypeSpec(descr->type) - 1;
    while ((end != descr->type) && isdigit(*end)) {
        end --;
    }
    end ++;
    v = PyBytes_FromStringAndSize(descr->type,  end - descr->type);
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "type", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    if (descr->printfFormat) {
        v = PyBool_FromLong(descr->printfFormat);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "printf_format", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    if (descr->sel_type) {
        v = PyBytes_FromString(descr->sel_type);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "sel_of_type", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    v = PyBool_FromLong(descr->alreadyRetained);
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "already_retained", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    v = PyBool_FromLong(descr->alreadyCFRetained);
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "already_cfretained", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    if (descr->callable) {
        v = PyObjCMethodSignature_AsDict(descr->callable);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "callable", v);
        Py_DECREF(v);
        if (r == -1) goto error;

        v = PyBool_FromLong(descr->callableRetained);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "callable_retained", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    switch (descr->ptrType) {
    case PyObjC_kPointerPlain: break;
    case PyObjC_kNullTerminatedArray:
        r = PyDict_SetItemString(result, "c_array_delimited_by_null",
                Py_True);
        if (r == -1) goto error;
        break;
    case PyObjC_kArrayCountInArg:
        if (descr->arrayArg == descr->arrayArgOut) {
            v = PyInt_FromLong(descr->arrayArg);
        } else {
            v = Py_BuildValue("ii", descr->arrayArg, descr->arrayArgOut);
        }
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
        Py_DECREF(v);
        if (r == -1) goto error;
        break;
    case PyObjC_kFixedLengthArray:
        v = PyInt_FromLong(descr->arrayArg);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "c_array_of_fixed_length", v);
        Py_DECREF(v);
        if (r == -1) goto error;
        break;
    case PyObjC_kVariableLengthArray:
        r = PyDict_SetItemString(result, "c_array_of_variable_length",
                Py_True);
        if (r == -1) goto error;

    }

    if (descr->ptrType != PyObjC_kPointerPlain) {
        v = PyBool_FromLong(descr->arraySizeInRetval);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "c_array_length_in_result", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    if (*PyObjCRT_SkipTypeQualifiers(descr->type) == _C_PTR) {
        v = PyBool_FromLong(descr->allowNULL);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "null_accepted", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    return result;

error:
    Py_DECREF(result);
    return NULL;
}

PyObject*
PyObjCMethodSignature_AsDict(PyObjCMethodSignature* methinfo)
{
    PyObject* result;
    PyObject* v;
    int r;
    Py_ssize_t i;

    result = PyDict_New();
    if (result == NULL) {
        return NULL;
    }
    v = PyBool_FromLong(methinfo->variadic);
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "variadic", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    if (methinfo->variadic && methinfo->null_terminated_array) {
        v = PyBool_FromLong(methinfo->null_terminated_array);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "c_array_delimited_by_null", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    if (methinfo->variadic && methinfo->arrayArg != -1) {
        v = PyInt_FromLong(methinfo->arrayArg);
        if (v == NULL) goto error;
        r = PyDict_SetItemString(result, "c_array_length_in_arg", v);
        Py_DECREF(v);
        if (r == -1) goto error;
    }

    if (methinfo->suggestion) {
        r = PyDict_SetItemString(result, "suggestion",
                methinfo->suggestion);
        if (r == -1) goto error;
    }

    v = argdescr2dict(methinfo->rettype);
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "retval", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    v = PyTuple_New(Py_SIZE(methinfo));
    if (v == NULL) goto error;
    r = PyDict_SetItemString(result, "arguments", v);
    Py_DECREF(v);
    if (r == -1) goto error;

    for (i = 0; i < Py_SIZE(methinfo); i++) {
        PyObject* t;

        t = argdescr2dict(methinfo->argtype[i]);
        if (t == NULL) goto error;

        PyTuple_SET_ITEM(v, i, t);
    }

    return result;

error:
    Py_XDECREF(result);
    return NULL;
}
