#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static PyObjCMethodSignature* _Nullable new_methodsignature(const char*);

/*
 * Define static strings and struct _PyObjC_ArgDescr values that
 * are used to share compiled metadata for basic types. These
 * shared "template" structures reduce the amount of memory used
 * by metadata structures, at a slight cost in static read-only
 * data and slightly more complicated code.
 */
#define TC(VAL) [VAL] = {_C_IN, _C_PTR, VAL, 0}
static const char _ptr_in_typecodes[256][4] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL) [VAL] = {_C_OUT, _C_PTR, VAL, 0}
static const char _ptr_out_typecodes[256][4] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL) [VAL] = {_C_INOUT, _C_PTR, VAL, 0}
static const char _ptr_inout_typecodes[256][4] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

static const char _block_typecode[] = {_C_ID, _C_UNDEF, 0};

#define TC(VAL) [VAL] = {.type = _ptr_in_typecodes[VAL] + 2, .tmpl = 1, .allowNULL = 1}
static const struct _PyObjC_ArgDescr descr_templates[256] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL) [VAL] = {.type = _ptr_in_typecodes[VAL] + 1, .tmpl = 1, .allowNULL = 1}
static const struct _PyObjC_ArgDescr ptr_templates[256] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL)                                                                          \
    [VAL] = {.type      = _ptr_in_typecodes[VAL],                                        \
             .tmpl      = 1,                                                             \
             .allowNULL = 1,                                                             \
             .modifier  = _C_IN,                                                         \
             .ptrType   = PyObjC_kPointerPlain}
static const struct _PyObjC_ArgDescr ptr_in_templates[256] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL)                                                                          \
    [VAL] = {.type      = _ptr_out_typecodes[VAL],                                       \
             .tmpl      = 1,                                                             \
             .allowNULL = 1,                                                             \
             .modifier  = _C_OUT,                                                        \
             .ptrType   = PyObjC_kPointerPlain}
static const struct _PyObjC_ArgDescr ptr_out_templates[256] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

#define TC(VAL)                                                                          \
    [VAL] = {.type      = _ptr_inout_typecodes[VAL],                                     \
             .tmpl      = 1,                                                             \
             .allowNULL = 1,                                                             \
             .modifier  = _C_INOUT,                                                      \
             .ptrType   = PyObjC_kPointerPlain}
static const struct _PyObjC_ArgDescr ptr_inout_templates[256] = {
    TC(_C_VOID),     TC(_C_ID),   TC(_C_CLASS), TC(_C_SEL),          TC(_C_BOOL),
    TC(_C_NSBOOL),   TC(_C_CHR),  TC(_C_UCHR),  TC(_C_SHT),          TC(_C_USHT),
    TC(_C_INT),      TC(_C_UINT), TC(_C_LNG),   TC(_C_ULNG),         TC(_C_LNG_LNG),
    TC(_C_ULNG_LNG), TC(_C_FLT),  TC(_C_DBL),   TC(_C_CHAR_AS_TEXT), TC(_C_CHAR_AS_INT),
    TC(_C_UNICHAR),
};
#undef TC

static const struct _PyObjC_ArgDescr block_template = {
    .type      = _block_typecode,
    .tmpl      = 1,
    .allowNULL = 1,
};

static const struct _PyObjC_ArgDescr in_template = {
    .tmpl      = 1,
    .allowNULL = 1,
    .modifier  = _C_IN,
};

static const struct _PyObjC_ArgDescr out_template = {
    .tmpl      = 1,
    .allowNULL = 1,
    .modifier  = _C_OUT,
};

static const struct _PyObjC_ArgDescr inout_template = {
    .tmpl      = 1,
    .allowNULL = 1,
    .modifier  = _C_INOUT,
};

static struct _PyObjC_ArgDescr* _Nullable default_descr(const char* _Nullable typestr,
                                                        const char modifier)
{
    struct _PyObjC_ArgDescr* result;

    if (typestr == NULL) {
        switch (modifier) {
        case _C_IN:
            return (struct _PyObjC_ArgDescr*)&in_template;
        case _C_OUT:
            return (struct _PyObjC_ArgDescr*)&out_template;
        case _C_INOUT:
            return (struct _PyObjC_ArgDescr*)&inout_template;
        default:
            return NULL;
        }
    }

    if (unlikely(typestr[0] == _C_ID && typestr[1] == _C_UNDEF)) {
        return (struct _PyObjC_ArgDescr*)&block_template;

    } else if (unlikely(typestr[0] == _C_PTR)) {
        switch (modifier) {
        case _C_IN:
            result = (struct _PyObjC_ArgDescr*)&ptr_in_templates[*(unsigned char*)(typestr
                                                                                   + 1)];
            break;

        case _C_OUT:
            result = (struct _PyObjC_ArgDescr*)&ptr_out_templates[*(
                unsigned char*)(typestr + 1)];
            break;

        case _C_INOUT:
            result = (struct _PyObjC_ArgDescr*)&ptr_inout_templates[*(
                unsigned char*)(typestr + 1)];
            break;

        default:
            result =
                (struct _PyObjC_ArgDescr*)&ptr_templates[*(unsigned char*)(typestr + 1)];
        }

    } else {
        result = (struct _PyObjC_ArgDescr*)&descr_templates[*(unsigned char*)(typestr)];
    }
    if (result->type == NULL) {
        return NULL;
    } else {
        return result;
    }
}

static PyObject* _Nullable sig_str(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    PyObject*              v    = PyObjCMethodSignature_AsDict(self);
    if (unlikely(v == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return PyUnicode_FromString(self->signature);
        // LCOV_EXCL_STOP

    } else {
        PyObject* r = PyObject_Repr(v);
        Py_DECREF(v);
        return r;
    }
}

static struct _PyObjC_ArgDescr* _Nullable alloc_argdescr(
    struct _PyObjC_ArgDescr* _Nullable tmpl)
{
    struct _PyObjC_ArgDescr* retval = PyMem_Malloc(sizeof(*retval));
    if (unlikely(retval == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    memset(retval, 0, sizeof(*retval));
    if (tmpl && tmpl->type) {
        retval->type = PyObjCUtil_Strdup(tmpl->type);
        if (retval->type == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyMem_Free(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }
    } else {
        retval->type = NULL;
    }
    retval->typeOverride      = NO;
    retval->modifier          = '\0';
    retval->ptrType           = PyObjC_kPointerPlain;
    retval->allowNULL         = YES;
    retval->arraySizeInRetval = NO;
    retval->printfFormat      = NO;
    retval->alreadyRetained   = NO;
    retval->alreadyCFRetained = NO;
    retval->callableRetained  = NO;
    retval->tmpl              = NO;
    retval->callable          = NULL;
    retval->sel_type          = NULL;
    retval->arrayArg          = 0;
    retval->arrayArgOut       = 0;
    return retval;
}

static void
free_argdescr(struct _PyObjC_ArgDescr* descr)
{
    if (descr == NULL || descr->tmpl) {
        return;
    }

    if (descr->typeOverride) {
        PyMem_Free((char*)descr->type);
        descr->type = NULL;
    }

    if (descr->sel_type != NULL) {
        PyMem_Free((char*)descr->sel_type);
        descr->sel_type = NULL;
    }
    PyMem_Free(descr);
}

static void
sig_dealloc(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    Py_ssize_t             i;

    if (self->signature) {
        PyMem_Free((char*)self->signature);
    }

    free_argdescr(self->rettype);

    for (i = 0; i < Py_SIZE(self); i++) {
        free_argdescr(self->argtype[i]);
    }
    PyTypeObject* tp = Py_TYPE(self);
    PyObject_Free(self);
    Py_DECREF(tp);
}

static PyType_Slot sig_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&sig_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&sig_str},
    {.slot = Py_tp_str, .pfunc = (void*)&sig_str},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {0, NULL} /* sentinel */
};

static PyType_Spec sig_spec = {
    .name      = "objc._method_signature",
    .basicsize = sizeof(PyObjCMethodSignature),
    .itemsize  = sizeof(struct _PyObjC_ArgDescr*),
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = sig_slots,
};

PyObject* PyObjCMethodSignature_Type;

static void
determine_if_shortcut(PyObjCMethodSignature* methinfo)
{
    /*
     * Set shortcut_signature and shortcut_argbuf_size if appropriate,
     * clear otherwise
     *
     * These should be set if all arguments are basic types (no functions, no byreference,
     * ...) and method parts of the function setup code can be skipped.
     *
     * Note that shortcut_argbuf_size has a limited size, this will also not work when
     * there are a lot, or large, arguments/return values.
     */

    assert(methinfo);
    methinfo->shortcut_signature   = NO;
    methinfo->shortcut_argbuf_size = 0;
    methinfo->shortcut_result_size = 0;

    Py_ssize_t byref_in_count = 0, byref_out_count = 0, plain_count = 0, argbuf_len = 0;
    BOOL       variadic_args = NO;

    if (methinfo->variadic) {
        return;
    }

    if (methinfo->suggestion != NULL) {
        return;
    }

    PyObjCMethodSignature_Validate(methinfo);

    for (Py_ssize_t i = 0; i < Py_SIZE(methinfo); i++) {
        switch (*methinfo->argtype[i]->type) {
        /* Pointer-like return values aren't "simple" */
        case _C_CONST:
        case _C_OUT:
        case _C_IN:
        case _C_INOUT:
        case _C_PTR:
        case _C_CHARPTR:
            return;

        case _C_ID:
            if (methinfo->argtype[i]->type[1] == '?') {
                /* Blocks are not simple */
                /* XXX: Remove this limitation */
                return;
            }
        }
    }

    switch (*methinfo->rettype->type) {
    /* Pointer-like return values aren't "simple" */
    case _C_OUT:
    case _C_IN:
    case _C_INOUT:
    case _C_PTR:
    case _C_CHARPTR:
        return;
    }

    if (Py_SIZE(methinfo) > MAX_ARGCOUNT_SIMPLE) {
        return;
    }

    Py_ssize_t result_size = PyObjCRT_SizeOfReturnType(methinfo->rettype->type);
    if (unlikely(result_size == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return;
        // LCOV_EXCL_STOP
    }

    int r = PyObjCFFI_CountArguments(methinfo, 0, &byref_in_count, &byref_out_count,
                                     &plain_count, &argbuf_len, &variadic_args);
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        /* Setting up the methinfo already validated the type
         * encodings, which means the function cannot fail.
         */
        // LCOV_EXCL_START
        PyErr_Clear();
        return;
        // LCOV_EXCL_STOP
    }

    /*
     * All of these were checked before the call to CountArguments.
     */
    assert(!byref_in_count);
    assert(!byref_out_count);
    assert(!variadic_args);

    if (argbuf_len + result_size >= SHORTCUT_MAX_ARGBUF) {
        return;
    }

    methinfo->shortcut_signature   = YES;
    methinfo->shortcut_argbuf_size = (unsigned int)argbuf_len;
    methinfo->shortcut_result_size = (unsigned int)result_size;
}

static int
setup_type(struct _PyObjC_ArgDescr* meta, const char* type)
{
    const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);

    if (unlikely(*withoutModifiers == _C_ARY_B)) {
        meta->ptrType  = PyObjC_kFixedLengthArray;
        meta->arrayArg = 0;
        const char* c  = withoutModifiers + 1;
        const char* e;
        while (isdigit(*c)) {
            meta->arrayArg *= 10;
            meta->arrayArg += *c - '0';
            c++;
        }

        e                  = PyObjCRT_SkipTypeSpec(c);
        meta->typeOverride = YES;
        meta->type         = PyMem_Malloc((withoutModifiers - type) + (e - c) + 3);
        if (unlikely(meta->type == NULL)) { // LCOV_BR_EXCL_LINE
            return -1;                      // LCOV_EXCL_LINE
        }

        char* cur;
        if (unlikely(type != withoutModifiers)) {
            memcpy((void*)(meta->type), type, withoutModifiers - type);
            cur = (char*)(meta->type + (withoutModifiers - type));
        } else {
            cur    = (char*)(meta->type);
            *cur++ = _C_IN;
        }
        *cur++ = _C_PTR;
        memcpy(cur, c, e - c);
        cur[e - c] = '\0';
#ifdef PyObjC_DEBUG
        /* XXX: Why is this in a DEBUG block? */
        meta->type =
            PyMem_Realloc((void*)(meta->type), (withoutModifiers - type) + (e - c) + 4);
#endif /* PyObjC_DEBUG */

    } else { // LCOV_BR_EXCL_LINE
        meta->type         = type;
        meta->typeOverride = NO;
    }
    return 0;
}

static PyObjCMethodSignature* _Nullable new_methodsignature(const char* signature)
{
    Py_ssize_t             nargs, i;
    const char*            cur;
    PyObjCMethodSignature* retval;

    assert(signature != NULL);

    /* Skip return-type */
    cur = PyObjCRT_SkipTypeSpec(signature);
    if (cur && *cur == '"') {
        cur++;
        while (*cur != '\0' && *cur != '"') {
            cur++;
        }
        if (*cur != '"') {
            PyErr_Format(PyObjCExc_Error, "Invalid encoding: %s", signature);
            return NULL;
        }
        cur++;
        while (isdigit(*cur))
            cur++;
    }

    nargs = 0;
    while (cur && *cur) {
        cur = PyObjCRT_SkipTypeSpec(cur);
        if (cur && *cur == '"') {
            cur++;
            while (*cur != '\0' && *cur != '"') {
                cur++;
            }
            if (*cur != '"') {
                PyErr_Format(PyObjCExc_Error, "Invalid encoding: %s", signature);
                return NULL;
            }
            cur++;
            while (isdigit(*cur))
                cur++;
        }
        nargs++;
    }
    if (cur == NULL) {
        assert(PyErr_Occurred());
        return NULL;
    }

    char* signature_copy = PyObjCUtil_Strdup(signature);
    if (unlikely(signature_copy == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                        // LCOV_EXCL_LINE
    }

    retval = PyObject_NewVar(PyObjCMethodSignature,
                             (PyTypeObject*)PyObjCMethodSignature_Type, nargs /*+1*/);

    if (unlikely(retval == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(signature_copy);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < nargs; i++) {
        retval->argtype[i] = NULL;
    }

    Py_SET_SIZE(retval, nargs);
    retval->signature             = signature_copy;
    retval->suggestion            = NULL;
    retval->variadic              = NO;
    retval->null_terminated_array = NO;
    retval->free_result           = NO;
    retval->initializer           = NO;
    retval->shortcut_signature    = NO;
    retval->shortcut_argbuf_size  = 0;
    retval->shortcut_result_size  = 0;
    retval->arrayArg              = 0;
    retval->deprecated            = 0;
    retval->rettype               = (struct _PyObjC_ArgDescr* _Nonnull)NULL;

    cur = PyObjCRT_SkipTypeQualifiers(retval->signature);
    assert(cur != NULL);
    retval->rettype = default_descr(cur, *retval->signature);
    if (unlikely(retval->rettype == NULL)) {
        retval->rettype = alloc_argdescr(NULL);
        if (unlikely(retval->rettype == NULL)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }

        /* Ignore type specifiers for methods returning void. Mostly needed
         * to avoid crapping out one (oneway void) methods.
         */
        assert(retval->signature != NULL);
        if (unlikely(setup_type(retval->rettype, cur) < 0)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }
        assert(retval->rettype->type != NULL);
    }
    assert(retval->rettype->type != NULL);

    cur = PyObjCRT_SkipTypeSpec(retval->signature);
    assert(cur);
    if (*cur == '"') {
        /* Second pass over the signature, which therefore
         * must be valid.
         */
        cur++;
        while (*cur != '"') {
            cur++;
        }
        cur++;
        while (isdigit(*cur))
            cur++;
    }
    nargs = 0;
    while (*cur) {
        if (unlikely(*cur == _C_CONST)) {
            /* Ignore a 'const' qualifier, not used by the bridge */
            cur++;
        }
        retval->argtype[nargs] = default_descr(PyObjCRT_SkipTypeQualifiers(cur), *cur);
        if (unlikely(retval->argtype[nargs] == NULL)) {
            retval->argtype[nargs] = alloc_argdescr(NULL);
            if (unlikely(retval->argtype[nargs] == NULL)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(retval);
                return NULL;
                // LCOV_EXCL_STOP
            }
            assert(cur != NULL);
            if (unlikely( // LCOV_BR_EXCL_LINE
                    setup_type(retval->argtype[nargs], cur) < 0)) {
                // LCOV_EXCL_START
                Py_DECREF(retval);
                return NULL;
                // LCOV_EXCL_STOP
            }
            assert(retval->argtype[nargs]->type != NULL);
        }

        cur = PyObjCRT_SkipTypeSpec(cur);
        if (cur == NULL) { // LCOV_BR_EXCL_LINE
            /* Cannot fail because this is the second pass
             * over the type encoding.
             */
            // LCOV_EXCL_START
            Py_CLEAR(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (*cur == '"') {
            cur++;
            while (*cur != '"') {
                cur++;
            }
            cur++;
            while (isdigit(*cur))
                cur++;
        }
        nargs++;
    }

    assert(Py_SIZE(retval) == nargs);
    PyObjCMethodSignature_Validate(retval);

    return retval;
}

char* _Nullable PyObjC_NSMethodSignatureToTypeString(NSMethodSignature* sig, char* buf,
                                                     size_t buflen)
{
    char*      result    = buf;
    NSUInteger arg_count = [sig numberOfArguments];
    NSUInteger i;
    size_t     r;

    r = strlcpy(buf, [sig methodReturnType], buflen);
    if (r >= buflen) {
        PyErr_Format(PyObjCExc_InternalError, "NSMethodsignature too large (%ld)", r);
        return NULL;
    }

    for (i = 0; i < arg_count; i++) {
        r = strlcat(buf, [sig getArgumentTypeAtIndex:i], buflen);
        if (r >= buflen) {
            PyErr_Format(PyObjCExc_InternalError, "NSMethodsignature too large (%ld)", r);
            return NULL;
        }
    }

    return result;
}

/*
 * Return values:
 *  0: OK
 * -1: error
 * -2: 'descr' is template, but would have to be updated.
 *
 *  XXX: Use warnings to warn about invalid metadata, with a specific warning that
 *       can be easility turned into an error.
 */
static int
setup_descr(struct _PyObjC_ArgDescr* _Nullable descr, PyObject* meta, BOOL is_native)
{
    PyObject* d;
    int       r;
    char      typeModifier = 0;

    if (meta == Py_None) {
        return 0;
    }

    if (!PyDict_Check(meta)) {
        PyErr_Format(PyExc_TypeError, "metadata of type %s: %R", Py_TYPE(meta)->tp_name,
                     meta);

        return -1;
    }

    assert(meta != NULL);

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_null_accepted, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
                   /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (descr == NULL || !!descr->allowNULL != !!r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }
            descr->allowNULL = r;
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_already_retained, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }
            descr->alreadyRetained = YES;
            Py_CLEAR(d);
        }
    }

    assert(descr == NULL || !descr->alreadyCFRetained);
    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_already_cfretained, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE

    /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }
            descr->alreadyCFRetained = YES;
            Py_CLEAR(d);
        }
    }

    assert(descr == NULL || !descr->callableRetained);
    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_callable_retained, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
                   /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }
            descr->callableRetained = YES;
        }
        Py_CLEAR(d);
    }

    assert(descr == NULL || descr->sel_type == NULL);
    switch (PyDict_GetItemRef(meta, PyObjCNM_sel_of_type, &d)) { // LCOV_BR_EXCL_LINE
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        if (PyUnicode_Check(d)) {
            PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
            if (bytes == NULL) {
                Py_DECREF(d);
                return -1;
            }

            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                Py_DECREF(bytes);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
            Py_DECREF(bytes);
            if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -1;
                // LCOV_EXCL_STOP
            }

        } else if (PyBytes_Check(d)) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(d));
            if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -1;
                // LCOV_EXCL_STOP
            }
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef(meta, PyObjCNM_callable, &d)) { // LCOV_BR_EXCL_LINE
    case -1:
        return -1; // LCOV_EXCL_LINE
                   /* case 0: pass */
    case 1:
        if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(d);
            return -2;
            // LCOV_EXCL_STOP
        }

        if (!PyDict_Check(d)) {
            PyErr_Format(PyExc_ValueError, "expecting dict for 'callable', got %R", d);
            return -1;
        }

        /* Make up a dummy signature, will be overridden by
         * the metadata.
         */
        char       buffer[128];
        PyObject*  a = NULL;
        Py_ssize_t i, len;

        switch (PyDict_GetItemRef(d, PyObjCNM_arguments, &a)) { // LCOV_BR_EXCL_LINE
        case -1:
            // LCOV_EXCL_START
            Py_DECREF(d);
            return -1;
            // LCOV_EXCL_STOP
        case 0:
            buffer[0] = _C_ID;
            buffer[1] = '\0';
            break;
        case 1:
            len = PyObject_Length(a);
            if (len == -1) {
                Py_DECREF(a);
                Py_DECREF(d);
                return -1;
            }
            if ((size_t)len >= sizeof(buffer) - 2) {
                Py_DECREF(a);
                Py_DECREF(d);
                PyErr_SetString(PyObjCExc_Error,
                                "Callable metadata with too many arguments");
                return -1;
            }

            for (i = 0; i < len; i++) {
                buffer[i] = _C_ID;
            }
            buffer[len]     = _C_ID;
            buffer[len + 1] = '\0';
            Py_CLEAR(a);
        }

        descr->callable = PyObjCMethodSignature_WithMetaData(buffer, d, NO);
        if (descr->callable == NULL) {
            Py_DECREF(d);
            return -1;
        }
        Py_CLEAR(d);
    }

    assert(descr == NULL || !descr->arraySizeInRetval);
    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_c_array_length_in_result, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->arraySizeInRetval = YES;
        }
        Py_CLEAR(d);
    }

    assert(descr == NULL || !descr->printfFormat);
    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_printf_format, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /*case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->printfFormat = YES;
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_c_array_delimited_by_null, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->ptrType = PyObjC_kNullTerminatedArray;
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_c_array_of_fixed_length, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        if (PyLong_Check(d)) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->ptrType     = PyObjC_kFixedLengthArray;
            descr->arrayArg    = PyLong_AsLong(d);
            descr->arrayArgOut = descr->arrayArg;
            if (descr->arrayArg == -1 && PyErr_Occurred()) {
                Py_DECREF(d);
                return -1;
            }
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_c_array_of_variable_length, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->ptrType  = PyObjC_kVariableLengthArray;
            descr->arrayArg = 0;
            descr->arrayArg = 0;
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_deref_result_pointer, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        r = PyObject_IsTrue(d);
        if (r == -1) {
            return -1;
        }
        if (r) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->ptrType  = PyObjC_kDerefResultPointer;
            descr->arrayArg = 0;
            descr->arrayArg = 0;
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_c_array_length_in_arg, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        if (PyLong_Check(d)) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            descr->ptrType  = PyObjC_kArrayCountInArg;
            descr->arrayArg = PyLong_AsLong(d);
            if (descr->arrayArg == -1 && PyErr_Occurred()) {
                Py_DECREF(d);
                return -1;
            }
            descr->arrayArgOut = descr->arrayArg;

        } else if (PyTuple_Check(d)) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            if (PyTuple_GET_SIZE(d) == 1) {
                descr->ptrType = PyObjC_kArrayCountInArg;
                if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
                    descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
                    if (descr->arrayArg == -1 && PyErr_Occurred()) {
                        return -1;
                    }
                } else {
                    Py_DECREF(d);
                    PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
                    return -1;
                }
                descr->arrayArgOut = descr->arrayArg;
            } else if (PyTuple_GET_SIZE(d) >= 2) {
                descr->ptrType = PyObjC_kArrayCountInArg;
                if (PyLong_Check(PyTuple_GET_ITEM(d, 0))) {
                    descr->arrayArg = PyLong_AsLong(PyTuple_GET_ITEM(d, 0));
                    if (descr->arrayArg == -1 && PyErr_Occurred()) {
                        Py_DECREF(d);
                        return -1;
                    }
                } else {
                    Py_DECREF(d);
                    PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
                    return -1;
                }

                if (PyLong_Check(PyTuple_GET_ITEM(d, 1))) {
                    descr->arrayArgOut = PyLong_AsLong(PyTuple_GET_ITEM(d, 1));
                    if (descr->arrayArgOut == -1 && PyErr_Occurred()) {
                        Py_DECREF(d);
                        return -1;
                    }
                } else {
                    Py_DECREF(d);
                    PyErr_SetString(PyExc_TypeError, "array_out argument not integer");
                    return -1;
                }
            }
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        meta, PyObjCNM_type_modifier, &d)) {
    case -1:
        return -1; // LCOV_EXCL_LINE
    /* case 0: pass */
    case 1:
        if (PyUnicode_Check(d)) {
            PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
            if (bytes == NULL) {
                Py_DECREF(d);
                return -1;
            }

            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                Py_DECREF(bytes);
                return -2;
                // LCOV_EXCL_STOP
            }

            typeModifier = *PyBytes_AsString(bytes);
            assert(!PyErr_Occurred());
            Py_CLEAR(bytes);
        } else if (PyBytes_Check(d)) {
            if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(d);
                return -2;
                // LCOV_EXCL_STOP
            }

            typeModifier = *PyBytes_AsString(d);
            assert(!PyErr_Occurred());
        }
        Py_CLEAR(d);
    }

    switch (PyDict_GetItemRef(meta, PyObjCNM_type, &d)) { // LCOV_BR_EXCL_LINE
    case -1:
        return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        /* case 1: pass */
    }

    if (d && (PyBytes_Check(d) || PyUnicode_Check(d))) {

        PyObject* bytes = NULL;

        if (descr == NULL || descr->tmpl) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_XDECREF(d);
            return -2;
            // LCOV_EXCL_STOP
        }

        descr->modifier = typeModifier;

        if (PyUnicode_Check(d)) {
            bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
            if (bytes == NULL) {
                Py_XDECREF(d);
                return -1;
            }

        } else {
            assert(PyBytes_Check(d));
            bytes = d;
            d     = NULL;
        }

        const char* type = PyBytes_AsString(bytes);

        /* XXX: This assertion is not really useful and needs to be more clear */
        assert(!is_native || descr->type != NULL);
        assert(type != NULL);

        if (is_native                                           // LCOV_BR_EXCL_LINE
            && !PyObjC_signatures_compatible(descr->type, type) // LCOV_BR_EXCL_LINE
        ) {
            /* Note: 'is_native' is never true, all callers that pass a true value
             * don't pass a metadata dict.
             *
             * The new signature is not compatible enough, ignore the
             * override.
             */
            type = descr->type; // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE

        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);
        size_t      bufsize          = strlen(withoutModifiers) + 2;
        char*       tp               = PyMem_Malloc(bufsize);
        if (tp == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_XDECREF(d);
            Py_XDECREF(bytes);
            PyErr_NoMemory();
            return -1;
            // LCOV_EXCL_STOP
        }

        if (typeModifier != '\0') {
            /* Skip existing modifiers, we're overriding those */
            strlcpy(tp + 1, withoutModifiers, bufsize - 1);
            tp[0] = typeModifier;
        } else {
            strlcpy(tp, type, bufsize);
        }
        assert(tp != NULL);
        descr->typeOverride = YES;
        descr->type         = tp;
        Py_XDECREF(bytes);

    } else if (descr != NULL) {
        if (descr->type == NULL) {
            if (typeModifier != '\0') {
                if (descr->modifier != typeModifier) { // LCOV_BR_EXCL_LINE
                    if (descr->tmpl) {                 // LCOV_BR_EXCL_LINE
                        // LCOV_EXCL_START
                        Py_XDECREF(d);
                        return -2;
                        // LCOV_EXCL_STOP
                    }
                }
                descr->modifier = typeModifier;
            }
        } else {
            const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
            assert(*withoutModifiers != _C_ARY_B);
            if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID
                && descr->ptrType == PyObjC_kPointerPlain) {

                /* Plain old void*, ignore type modifiers */

            } else if (typeModifier != '\0' && withoutModifiers[0] == _C_PTR) {
                if (descr->tmpl) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_XDECREF(d);
                    return -2;
                    // LCOV_EXCL_STOP
                }

                size_t bufsize = strlen(withoutModifiers) + 2;
                char*  tp      = PyMem_Malloc(bufsize);
                if (tp == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_XDECREF(d);
                    PyErr_NoMemory();
                    return -1;
                    // LCOV_EXCL_STOP
                }

                tp[0] = typeModifier;
                strlcpy(tp + 1, withoutModifiers, bufsize - 1);

                assert(!descr->typeOverride);

                descr->typeOverride = YES;
                descr->type         = tp;
            }
        }
    }
    Py_CLEAR(d);
    return 0;
}

static struct _PyObjC_ArgDescr* _Nullable default_descr_from_meta(PyObject* metadata)
{
    /* Try to find a static definition of the encoded type */
    int                      r;
    PyObject*                type;
    const char*              typestr;
    PyObject*                modifier;
    const char*              modifierstr;
    struct _PyObjC_ArgDescr* result = NULL;

    r = PyDict_GetItemRef(metadata, PyObjCNM_type, &type);
    if (r != 1) {
        typestr = NULL;
    } else {
        if (unlikely(PyUnicode_Check(type))) {
            PyObject* tmp = PyUnicode_AsEncodedString(type, NULL, NULL);
            if (tmp == NULL) {
                PyErr_Clear();
                return NULL;
            }
            Py_CLEAR(type);
            type = tmp;
        }

        if (likely(PyBytes_Check(type))) {
            typestr = PyBytes_AsString(type);
            if (typestr == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_Clear();
                return NULL;
                // LCOV_EXCL_STOP
            }
        } else {
            Py_CLEAR(type);
            return NULL;
        }
    }

    r = PyDict_GetItemRef(metadata, PyObjCNM_type_modifier, &modifier);
    if (r != 1) {
        PyErr_Clear();
        modifierstr = "";
    } else {
        if (unlikely(PyUnicode_Check(modifier))) {
            PyObject* tmp = PyUnicode_AsEncodedString(modifier, NULL, NULL);
            if (tmp == NULL) {
                PyErr_Clear();
                return NULL;
            }
            Py_CLEAR(modifier);
            modifier = tmp;
        }

        if (likely(PyBytes_Check(modifier))) {
            modifierstr = PyBytes_AsString(modifier);
            if (modifierstr == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyErr_Clear();
                return NULL;
                // LCOV_EXCL_STOP
            }
        } else {
            modifierstr = "";
        }
    }

    result = default_descr(typestr, *modifierstr);

    Py_CLEAR(type);
    Py_CLEAR(modifier);
    return result;
}

static int
process_metadata_dict(PyObjCMethodSignature* methinfo, PyObject* _Nullable metadata,
                      BOOL                   is_native)
{
    PyObject* v;
    int       r;

    if (metadata != NULL && !PyDict_Check(metadata)) {
        PyErr_Format(PyExc_TypeError,
                     "Metadata dictionary is of type '%s' instead of 'dict'",
                     Py_TYPE(metadata)->tp_name);
        return -1;
    }

    if (metadata) {
        PyObject* retval;
        PyObject* av;
        int       r;

        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(metadata, PyObjCNM_retval, &retval)) {
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (methinfo->rettype == NULL) {
                methinfo->rettype = default_descr_from_meta(retval);
            }

            r = setup_descr(methinfo->rettype, retval, is_native);
            if (r == -1) {
                Py_DECREF(retval);
                return -1;

            } else if (r == -2) {
                methinfo->rettype = alloc_argdescr(methinfo->rettype);
                if (methinfo->rettype == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_DECREF(retval);
                    return -1;
                    // LCOV_EXCL_STOP
                }
                r = setup_descr(methinfo->rettype, retval, is_native);
                if (r == -1) {
                    Py_DECREF(retval);
                    return -1;
                }
                assert(r != -2);
            }
        }
        Py_CLEAR(retval);

        switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
            metadata, PyObjCNM_free_result, &av)) {
        case -1:
            // LCOV_EXCL_START
            return -1;
            // LCOV_EXCL_STOP
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(av);
            if (r == -1) {
                return -1;
            }
            if (r) {
                methinfo->free_result = YES;
            }
            Py_CLEAR(av);
        }
    }

    if (metadata) {
        PyObject* args = NULL;

        switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
            metadata, PyObjCNM_arguments, &args)) {
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (!PyDict_Check(args)) {
                Py_CLEAR(args);
            } else {
                Py_ssize_t i;
                for (i = 0; i < Py_SIZE(methinfo); i++) {
                    PyObject* k = PyLong_FromLong(i);
                    PyObject* d = NULL;
                    int       r;

                    switch (PyDict_GetItemRef(args, k, &d)) { // LCOV_BR_EXCL_LINE
                    case -1:
                        // LCOV_EXCL_START
                        Py_DECREF(k);
                        Py_DECREF(args);
                        return -1;
                        // LCOV_EXCL_STOP
                        /* case 0: pass */
                        /* case 1: pass */
                    case 0:
                        Py_CLEAR(k);
                        break;
                    case 1:
                        Py_CLEAR(k);

                        if (methinfo->argtype[i] == NULL) {
                            methinfo->argtype[i] = default_descr_from_meta(d);
                        }

                        r = setup_descr(methinfo->argtype[i], d, is_native);
                        if (r == -1) {
                            Py_XDECREF(d);
                            Py_DECREF(args);
                            return -1;

                        } else if (r == -2) {
                            methinfo->argtype[i] = alloc_argdescr(methinfo->argtype[i]);
                            if (methinfo->argtype[i] == NULL) { // LCOV_BR_EXCL_LINE
                                // LCOV_EXCL_START
                                Py_XDECREF(d);
                                Py_DECREF(args);
                                Py_DECREF(methinfo);
                                return -1;
                                // LCOV_EXCL_STOP
                            }
                            r = setup_descr(methinfo->argtype[i], d, is_native);
                            if (r == -1) {
                                Py_XDECREF(d);
                                Py_DECREF(args);
                                return -1;
                            }
                            assert(r != -2);
                        }
                        Py_CLEAR(d);
                    }
                }
                Py_CLEAR(args);
            }
        }

        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(metadata, PyObjCNM_suggestion, &v)) {
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            methinfo->suggestion = v;
            v                    = NULL;
        }

        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(metadata, PyObjCNM_deprecated, &v)) {
        case -1:;
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyLong_Check(v)) {
                methinfo->deprecated = (int)PyLong_AsLong(v);
                if (methinfo->deprecated == -1 && PyErr_Occurred()) {
                    return -1;
                }
            }
            Py_CLEAR(v);
        }

        methinfo->null_terminated_array = NO;
        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(metadata, PyObjCNM_c_array_delimited_by_null, &v)) {
        case -1:
            return -1; // LCOV_EXCL_LINE
        /*case 0: pass */
        case 1:
            r = PyObject_IsTrue(v);
            if (r == -1) {
                return -1;
            }
            if (r) {
                methinfo->null_terminated_array = YES;
            }
            Py_CLEAR(v);
        }

        methinfo->arrayArg = -1;
        switch ( // LCOV_BR_EXCL_LINE
            PyDict_GetItemRef(metadata, PyObjCNM_c_array_length_in_arg, &v)) {
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyLong_Check(v)) {
                methinfo->arrayArg = (int)PyLong_AsLong(v);
                if (methinfo->arrayArg == -1 && PyErr_Occurred()) {
                    Py_DECREF(v);
                    return -1;
                }
            }
            Py_CLEAR(v);
        }

        methinfo->variadic = NO;

        switch (PyDict_GetItemRef(metadata, PyObjCNM_variadic, &v)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(v);
            if (r == -1) {
                return -1;
            }
            if (r) {
                methinfo->variadic = YES;

                if ((methinfo->suggestion == NULL) && (!methinfo->null_terminated_array)
                    && (methinfo->arrayArg == -1)) {
                    Py_ssize_t i;
                    for (i = 0; i < Py_SIZE(methinfo); i++) {
                        if (methinfo->argtype[i] == NULL)
                            continue;
                        if (methinfo->argtype[i]->printfFormat) {
                            Py_DECREF(v);
                            return 0;
                        }
                    }

                    /* No printf-format argument, therefore the method is
                     * not supported
                     */
                    methinfo->suggestion = PyUnicode_FromString(
                        "Variadic functions/methods are not supported");
                    if (methinfo->suggestion == NULL) { // LCOV_BR_EXCL_LINE
                        // LCOV_EXCL_START
                        Py_DECREF(v);
                        Py_DECREF(methinfo);
                        return -1;
                        // LCOV_EXCL_STOP
                    }
                }
            }
            Py_CLEAR(v);
        }
    }
    return 0;
}

static PyObject* registry = NULL;

static PyObjCMethodSignature* _Nullable compiled_metadata(PyObject* metadata)
{
    PyObjCMethodSignature* result;
    PyObject*              key;
    PyObject*              value;
    Py_ssize_t             max_idx;
    Py_ssize_t             pos;
    Py_ssize_t             i;

    assert(metadata != NULL);
    assert(PyDict_Check(metadata));

    PyObject* arguments;
    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        metadata, PyObjCNM_arguments, &arguments)) {
    case -1:
        return NULL; // LCOV_EXCL_LINE
    case 0:
        max_idx = 0;
        break;
    default: /* case 1: */
        if (!PyDict_Check(arguments)) {
            max_idx = 0;
        } else {
            pos     = 0;
            max_idx = -1;
            Py_BEGIN_CRITICAL_SECTION(arguments);
            while (PyDict_Next(arguments, &pos, &key, &value)) {
                if (PyLong_Check(key)) {

                    Py_ssize_t k = PyLong_AsSsize_t(key);
                    if (k == -1 && PyErr_Occurred()) {
                        max_idx = -1;
                        break;
                    }
                    if (k > max_idx) {
                        max_idx = k;
                    }
                }
            }
            Py_END_CRITICAL_SECTION();
            if (max_idx == -1 && PyErr_Occurred()) {
                return NULL;
            }

            max_idx += 1;
        }
        if (max_idx > MAX_ARGCOUNT) {
            PyErr_Format(PyObjCExc_Error,
                         "Maximum argument index is metadata is larger than %d in %R",
                         MAX_ARGCOUNT, arguments);
            Py_CLEAR(arguments);
            return NULL;
        }
        Py_CLEAR(arguments);
    }

    result = PyObject_NewVar(PyObjCMethodSignature,
                             (PyTypeObject*)PyObjCMethodSignature_Type, max_idx);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    Py_SET_SIZE(result, max_idx);
    result->signature             = (const char* _Nonnull)NULL;
    result->suggestion            = NULL;
    result->variadic              = NO;
    result->null_terminated_array = NO;
    result->free_result           = NO;
    result->initializer           = NO;
    result->shortcut_signature    = NO;
    result->shortcut_argbuf_size  = 0;
    result->shortcut_result_size  = 0;
    result->arrayArg              = 0;
    result->deprecated            = 0;
    result->rettype               = (struct _PyObjC_ArgDescr* _Nonnull)NULL;
    for (i = 0; i < max_idx; i++) {
        result->argtype[i] = NULL;
    }

    switch (PyDict_GetItemRef( // LCOV_BR_EXCL_LINE
        metadata, PyObjCNM_full_signature, &value)) {
    case -1:
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    /* case 0: pass */
    case 1:
        if (PyBytes_Check(value)) {
            result->signature = PyObjCUtil_Strdup(PyBytes_AsString(value));
        }
        Py_CLEAR(value);
    }

    if (process_metadata_dict(result, metadata, NO) < 0) {
        Py_DECREF(result);
        return NULL;
    }

    /*
     * Treat compiled metadata as templates because entries
     * can be reused when applying the metadata.
     */
    if (result->rettype != NULL && !result->rettype->tmpl) { // LCOV_BR_EXCL_LINE
        result->rettype->tmpl = YES;
    }
    for (i = 0; i < max_idx; i++) {
        if (result->argtype[i] == NULL)
            continue;
        if (!result->argtype[i]->tmpl) { // LCOV_BR_EXCL_LINE
            result->argtype[i]->tmpl = YES;
        }
    }
    return result;
}

int
PyObjC_registerMetaData(PyObject* class_name, PyObject* selector, PyObject* metadata)
{
    PyObject* compiled;
    int       r;

    assert(registry != NULL);
    assert(PyBytes_Check(class_name));
    assert(PyBytes_Check(selector));
    if (!PyDict_Check(metadata)) {
        PyErr_SetString(PyExc_TypeError, "metadata should be a dictionary");
        return -1;
    }

    compiled = (PyObject*)compiled_metadata(metadata);
    if (compiled == NULL) {
        return -1;
    }

    r = PyObjC_AddToRegistry(registry, class_name, selector, compiled);

    /*
     * This leaks a reference to 'compiled', and that's intentional.
     *
     * The compiled metadata is assumed to live "forever", this
     * file reuses 'struct _ArgDescr' references when building full
     * metadata objects for selectors to reduce memory usage.
     *
     * In practice this is not a problem because PyObjC itself does
     * not duplicate metadata registrations and the PyObjC extension
     * module cannot be unloaded because it affects process-global state.
     *
     * XXX: This needs to be benchmarked.
     */
    return r;
}

PyObjCMethodSignature* _Nullable PyObjCMethodSignature_WithMetaData(
    const char* signature, PyObject* _Nullable metadata, BOOL is_native)
{
    PyObjCMethodSignature* methinfo;

    assert(signature != NULL);

    methinfo = new_methodsignature(signature);
    if (methinfo == NULL) {
        return NULL;
    }

    if (process_metadata_dict(methinfo, metadata, is_native) < 0) {
        Py_DECREF(methinfo);
        return NULL;
    }

    PyObjCMethodSignature_Validate(methinfo);
    determine_if_shortcut(methinfo);

    return methinfo;
}

static struct _PyObjC_ArgDescr* _Nullable merge_descr(
    struct _PyObjC_ArgDescr* _Nonnull descr, struct _PyObjC_ArgDescr* _Nonnull meta,
    BOOL is_native __attribute__((__unused__)))
{
    assert(descr != meta);
    if (meta->type != NULL) {
        assert(descr->type != NULL);
        assert(meta->type != NULL);
        if (!is_native || PyObjC_signatures_compatible(descr->type, meta->type)) {
            return meta;
        }
    }

    /* Copy argdescr, assume there is no trivial metadata */
    descr = alloc_argdescr(descr);
    if (descr == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;     // LCOV_EXCL_LINE
    }
    if (meta->callable) {
        Py_XINCREF(meta->callable);
        Py_XDECREF(descr->callable);
        descr->callable = meta->callable;
    }

    assert(descr->sel_type == NULL);
    if (meta->sel_type) {
        descr->sel_type = PyObjCUtil_Strdup(meta->sel_type);
        if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyMem_Free(descr);
            return NULL;
            // LCOV_EXCL_STOP
        }
    } else {
        descr->sel_type = NULL;
    }

    if (meta->arrayArg != 0) {
        descr->arrayArg = meta->arrayArg;
    }
    if (meta->arrayArgOut != 0) {
        descr->arrayArgOut = meta->arrayArgOut;
    }
    if (meta->ptrType != PyObjC_kPointerPlain) {
        descr->ptrType = meta->ptrType;
    }
    descr->allowNULL         = meta->allowNULL;
    descr->arraySizeInRetval = meta->arraySizeInRetval;
    descr->printfFormat      = meta->printfFormat;
    descr->alreadyRetained   = meta->alreadyRetained;
    descr->alreadyCFRetained = meta->alreadyCFRetained;
    descr->callableRetained  = meta->callableRetained;

    if (meta->modifier != '\0') {
        assert(descr->type != NULL);
        if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID
            && descr->ptrType == PyObjC_kPointerPlain) {

            /* Plain old void*, ignore type modifiers */

        } else { // LCOV_EXCL_LINE
            const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
            assert(*withoutModifiers != '\0' && *withoutModifiers != _C_ARY_B);

            size_t bufsize = strlen(withoutModifiers) + 2;
            char*  tp      = PyMem_Malloc(bufsize);
            if (tp == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyMem_Free(descr);
                return NULL;
                // LCOV_EXCL_STOP
            }

            assert(!descr->typeOverride);

            /* Skip existing modifiers, we're overriding those */
            assert(tp != NULL);
            switch (*withoutModifiers) {
            case _C_PTR:
            case _C_CHARPTR:
                strlcpy(tp + 1, withoutModifiers, bufsize - 1);
                tp[0]               = meta->modifier;
                descr->typeOverride = YES;
                descr->type         = tp;
                break;
            default:
                strlcpy(tp, withoutModifiers, bufsize);
                descr->type = tp;
            }
        }
    }

    return descr;
}

static int
process_metadata_object(PyObjCMethodSignature* methinfo, PyObjCMethodSignature* metadata,
                        BOOL is_native)
{
    Py_ssize_t               i, len;
    struct _PyObjC_ArgDescr* tmp;
    if (metadata == NULL) {
        return 0;
    }

    if (metadata->suggestion) {
        methinfo->suggestion = metadata->suggestion;
        Py_INCREF(metadata->suggestion);
    }
    methinfo->variadic              = metadata->variadic;
    methinfo->null_terminated_array = metadata->null_terminated_array;
    methinfo->free_result           = metadata->free_result;
    methinfo->initializer           = metadata->initializer;
    methinfo->arrayArg              = metadata->arrayArg;
    methinfo->deprecated            = metadata->deprecated;

    assert(methinfo->rettype);
    if (metadata->rettype) {
        tmp = merge_descr(methinfo->rettype, metadata->rettype, is_native);
        if (tmp == NULL) { // LCOV_BR_EXCL_LINE
            return -1;     // LCOV_EXCL_LINE
        }
        free_argdescr(methinfo->rettype);
        methinfo->rettype = tmp;
    }

    len = Py_SIZE(methinfo);
    if (Py_SIZE(metadata) < Py_SIZE(methinfo)) {
        len = Py_SIZE(metadata);
    }

    for (i = 0; i < len; i++) {
        assert(methinfo->argtype[i]);
        if (metadata->argtype[i] != NULL) {
            tmp = merge_descr(methinfo->argtype[i], metadata->argtype[i], is_native);
            if (tmp == NULL) { // LCOV_BR_EXCL_LINE
                return -1;     // LCOV_EXCL_LINE
            }
            assert(methinfo->argtype[i]->type);
            free_argdescr(methinfo->argtype[i]);
            methinfo->argtype[i] = tmp;
        }
    }

    PyObjCMethodSignature_Validate(methinfo);
    return 0;
}

PyObjCMethodSignature* _Nullable PyObjCMethodSignature_GetRegistered(Class cls, SEL sel)
{
    return (PyObjCMethodSignature*)PyObjC_FindInRegistry(registry, cls, sel);
}

PyObjCMethodSignature* _Nullable PyObjCMethodSignature_ForSelector(
    Class cls, BOOL isClassMethod, SEL sel, const char* signature,
    BOOL is_native __attribute__((__unused__)))
{
    PyObjCMethodSignature* methinfo;
    PyObject*              metadata;

    metadata = PyObjC_FindInRegistry(registry, cls, sel);
    assert(metadata == NULL || PyObjCMethodSignature_Check(metadata));

    if (metadata == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;                            // LCOV_EXCL_LINE
    }

    if (metadata != NULL && ((PyObjCMethodSignature*)metadata)->signature) {
        methinfo = new_methodsignature(((PyObjCMethodSignature*)metadata)->signature);
    } else {
        methinfo = new_methodsignature(signature);
    }
    if (methinfo == NULL) {
        return NULL;
    }

    if (process_metadata_object( // LCOV_BR_EXCL_LINE
            methinfo, (PyObjCMethodSignature*)metadata, is_native)
        == -1) {
        // LCOV_EXCL_START
        Py_DECREF(methinfo);
        Py_XDECREF(metadata);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (isClassMethod) {
        const char* nm = sel_getName(sel);
        if (strncmp(nm, "new", 3) == 0 && ((nm[3] == 0) || isupper(nm[3]))) {
            if (methinfo->rettype->tmpl) {
                methinfo->rettype = alloc_argdescr(methinfo->rettype);
                if (methinfo->rettype == NULL) { // LCOV_BR_EXCL_LINE
                    // LCOV_EXCL_START
                    Py_XDECREF(methinfo);
                    Py_XDECREF(metadata);
                    return NULL;
                    // LCOV_EXCL_STOP
                }
            }
            methinfo->rettype->alreadyRetained = YES;
        }
    }

    assert(methinfo->rettype);
    assert(methinfo->rettype->type);
    if (methinfo->rettype->type[0] == _C_ID) {
        const char* nm = sel_getName(sel);
        // The check below matches the calculation of the default objc_method_family in
        // clang (other than the special casing of NSAutoreleasePool)
        if (sel_isEqual(sel, @selector(init))
            || ((strncmp(nm, "init", 4) == 0) && isupper(nm[4]))) {
            /* Mark 'init' methods, except for NSAutoreleasePool
             * which crashes when the reference count is manipulated
             * manually.
             */
            if (cls != [NSAutoreleasePool class]) {
                methinfo->initializer = YES;
            }
        }
    }

    PyObjCMethodSignature_Validate(methinfo);
    determine_if_shortcut(methinfo);

    Py_XDECREF(metadata);
    return methinfo;
}

static PyObject* _Nullable argdescr2dict(struct _PyObjC_ArgDescr* descr)
{
    PyObject*   result;
    PyObject*   v;
    const char* end;
    int         r;

    result = PyDict_New();
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

    if (descr->tmpl) {
        /* Add _template to the metadata, mostly for the testsuite */
        r = PyDict_SetItem(result, PyObjCNM__template, Py_True);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    /*
     * FromStringAndSize because the type is a segment of the full
     * method signature.
     */
    if (descr->type != NULL) {
        end = PyObjCRT_SkipTypeSpec(descr->type);
        if (unlikely(end == NULL)) {
            /* This can happen when the registry contains invalid
             * data. Don't error out when this happens to make it
             * possible to debug the issue.
             */
            PyErr_Clear();
            v = PyBytes_FromString(descr->type);
        } else {
            end--;
            while ((end != descr->type) && isdigit(*end)) {
                end--;
            }
            end++;
            v = PyBytes_FromStringAndSize(descr->type, end - descr->type);
        }
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_type, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    } else if (descr->modifier != '\0') {
        v = PyBytes_FromStringAndSize(&descr->modifier, 1);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        r = PyDict_SetItem(result, PyObjCNM_type_modifier, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->printfFormat) {
        r = PyDict_SetItem(result, PyObjCNM_printf_format,
                           descr->printfFormat ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->sel_type) {
        v = PyBytes_FromString(descr->sel_type);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_sel_of_type, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->alreadyRetained) {
        r = PyDict_SetItem(result, PyObjCNM_already_retained,
                           descr->alreadyRetained ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->alreadyCFRetained) {
        r = PyDict_SetItem(result, PyObjCNM_already_cfretained,
                           descr->alreadyCFRetained ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->callable) {
        v = PyObjCMethodSignature_AsDict(descr->callable);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_callable, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        r = PyDict_SetItem(result, PyObjCNM_callable_retained,
                           descr->callableRetained ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    switch (descr->ptrType) {
    case PyObjC_kPointerPlain:
        break;
    case PyObjC_kNullTerminatedArray:
        r = PyDict_SetItem(result, PyObjCNM_c_array_delimited_by_null, Py_True);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        break;
    case PyObjC_kArrayCountInArg:
        if (descr->arrayArg == descr->arrayArgOut) {
            v = PyLong_FromLong(descr->arrayArg);
        } else {
            v = Py_BuildValue("ii", descr->arrayArg, descr->arrayArgOut);
        }
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_c_array_length_in_arg, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        break;
    case PyObjC_kFixedLengthArray:
        v = PyLong_FromLong(descr->arrayArg);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_c_array_of_fixed_length, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        break;
    case PyObjC_kVariableLengthArray:
        r = PyDict_SetItem(result, PyObjCNM_c_array_of_variable_length, Py_True);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

    case PyObjC_kDerefResultPointer:
        r = PyDict_SetItem(result, PyObjCNM_deref_result_pointer, Py_True);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->ptrType != PyObjC_kPointerPlain && descr->arraySizeInRetval) {
        r = PyDict_SetItem(result, PyObjCNM_c_array_length_in_result,
                           descr->arraySizeInRetval ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->type == NULL || *PyObjCRT_SkipTypeQualifiers(descr->type) == _C_PTR) {
        r = PyDict_SetItem(result, PyObjCNM_null_accepted,
                           descr->allowNULL ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    return result;

error:
    // LCOV_EXCL_START
    Py_DECREF(result);
    return NULL;
    // LCOV_EXCL_STOP
}

PyObject* _Nullable PyObjCMethodSignature_AsDict(PyObjCMethodSignature* methinfo)
{
    PyObject*  result;
    PyObject*  v;
    int        r;
    Py_ssize_t i;

    result = PyDict_New();
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    if (methinfo->signature) {
        v = PyBytes_FromString(methinfo->signature);
        r = PyDict_SetItem(result, PyObjCNM_full_signature, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->free_result) {
        r = PyDict_SetItem(result, PyObjCNM_free_result,
                           methinfo->free_result ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->initializer) {
        r = PyDict_SetItem(result, PyObjCNM_initializer,
                           methinfo->initializer ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->variadic) {
        r = PyDict_SetItem(result, PyObjCNM_variadic,
                           methinfo->variadic ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->variadic && methinfo->null_terminated_array) {
        r = PyDict_SetItem(result, PyObjCNM_c_array_delimited_by_null,
                           methinfo->null_terminated_array ? Py_True : Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->variadic && methinfo->arrayArg != -1) {
        v = PyLong_FromLong(methinfo->arrayArg);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
        r = PyDict_SetItem(result, PyObjCNM_c_array_length_in_arg, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->suggestion) {
        r = PyDict_SetItem(result, PyObjCNM_suggestion, methinfo->suggestion);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->deprecated != 0) {
        v = PyLong_FromLong(methinfo->deprecated);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE

        r = PyDict_SetItem(result, PyObjCNM_deprecated, v);
        Py_DECREF(v);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->rettype == NULL) {
        v = Py_None;
        Py_INCREF(Py_None);
    } else {
        v = argdescr2dict(methinfo->rettype);
        if (v == NULL)  // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }
    r = PyDict_SetItem(result, PyObjCNM_retval, v);
    Py_DECREF(v);
    if (r == -1)    // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    v = PyTuple_New(Py_SIZE(methinfo));
    if (v == NULL)  // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE
    r = PyDict_SetItem(result, PyObjCNM_arguments, v);
    Py_DECREF(v);
    if (r == -1)    // LCOV_BR_EXCL_LINE
        goto error; // LCOV_EXCL_LINE

    for (i = 0; i < Py_SIZE(methinfo); i++) {
        PyObject* t;

        if (methinfo->argtype[i] == NULL) {
            t = Py_None;
            Py_INCREF(Py_None);
        } else {
            t = argdescr2dict(methinfo->argtype[i]);
            if (t == NULL)  // LCOV_BR_EXCL_LINE
                goto error; // LCOV_EXCL_LINE
        }

        PyTuple_SET_ITEM(v, i, t);
    } // LCOV_BR_EXCL_LINE

    return result;

    // LCOV_EXCL_START
error:
    Py_XDECREF(result);
    return NULL;
    // LCOV_EXCL_STOP
}

PyObject* _Nullable PyObjC_copyMetadataRegistry(void)
{
    return PyObjC_CopyRegistry(registry,
                               (PyObjC_ItemTransform)PyObjCMethodSignature_AsDict);
}

int
PyObjCMethodSignature_Setup(PyObject* module __attribute__((__unused__)))
{
    PyObject* tmp = PyType_FromSpec(&sig_spec);
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    PyObjCMethodSignature_Type = tmp;

    tmp = PyObjC_NewRegistry();
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }
    registry = tmp;
    return 0;
}

NS_ASSUME_NONNULL_END
