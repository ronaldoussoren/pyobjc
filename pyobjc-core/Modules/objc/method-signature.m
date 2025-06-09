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

static PyObject* _Nullable sig_str(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    PyObject*              v    = PyObjCMethodSignature_AsDict(self);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
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

static void
sig_dealloc(PyObject* _self)
{
    PyObjCMethodSignature* self = (PyObjCMethodSignature*)_self;
    Py_ssize_t             i;

    if (self->signature) {
        PyMem_Free((char*)self->signature);
    }

    if (self->rettype && !self->rettype->tmpl) {
        if (self->rettype->typeOverride) {
            PyMem_Free((char*)self->rettype->type);
        }
        PyMem_Free(self->rettype);
    }

    for (i = 0; i < Py_SIZE(self); i++) {
        if (self->argtype[i] == NULL) // LCOV_BR_EXCL_LINE
            continue; // LCOV_EXCL_LINE
        if (self->argtype[i]->tmpl)
            continue;

        if (self->argtype[i]->typeOverride) {
            PyMem_Free((char*)self->argtype[i]->type);
        }

        if (self->argtype[i]->sel_type != NULL) {
            PyMem_Free((char*)self->argtype[i]->sel_type);
        }
        PyMem_Free(self->argtype[i]);
    }
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(self);
#endif
    PyObject_Free(self);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
}

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable sig_new(PyObject* self __attribute__((__unused__)),
                                   PyObject* args __attribute__((__unused__)),
                                   PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc._method_signature' instances");
    return NULL;
}
#endif

static PyType_Slot sig_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&sig_dealloc},
    {.slot = Py_tp_repr, .pfunc = (void*)&sig_str},
    {.slot = Py_tp_str, .pfunc = (void*)&sig_str},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&sig_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec sig_spec = {
    .name      = "objc._method_signature",
    .basicsize = sizeof(PyObjCMethodSignature),
    .itemsize  = sizeof(struct _PyObjC_ArgDescr*),
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = sig_slots,
};

PyObject* PyObjCMethodSignature_Type;

static int
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
    /* TODO: simple pass-by-reference objects args should work (NSError** arguments) */
    /* FIXME: structs/unions/... also use byref */

    assert(methinfo);
    methinfo->shortcut_signature   = NO;
    methinfo->shortcut_argbuf_size = 0;
    methinfo->shortcut_result_size = 0;

#if PY_VERSION_HEX < 0x03090000
    /* Shortcut not used in older python versions */
    return 0;

#else /*  PY_VERSION_HEX >= 0x03090000 */
    Py_ssize_t byref_in_count = 0, byref_out_count = 0, plain_count = 0, argbuf_len = 0;
    BOOL       variadic_args = NO;

    if (methinfo == NULL || methinfo->variadic) {
        return 0;
    }

    if (methinfo->suggestion != NULL) {
        return 0;
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
            return 0;

        case _C_ID:
            if (methinfo->argtype[i]->type[1] == '?') {
                /* Blocks are not simple */
                return 0;
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
        return 0;
    }

    if (Py_SIZE(methinfo) > MAX_ARGCOUNT_SIMPLE) {
        return 0;
    }

    Py_ssize_t result_size = PyObjCRT_SizeOfReturnType(methinfo->rettype->type);
    if (result_size == -1) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return 0;
        // LCOV_EXCL_STOP
    }
    if (result_size > 128) {
        return 0;
    }

    int r = PyObjCFFI_CountArguments(methinfo, 0, &byref_in_count, &byref_out_count,
                                     &plain_count, &argbuf_len, &variadic_args);
    if (r == -1) {
        PyErr_Clear();
        return 0;
    }

    if (byref_in_count || byref_out_count || variadic_args) {
        return 0;
    }

    if (argbuf_len + result_size >= SHORTCUT_MAX_ARGBUF) {
        return 0;
    }

    if (variadic_args) {
        return 0;
    }

    methinfo->shortcut_signature   = YES;
    methinfo->shortcut_argbuf_size = (unsigned int)argbuf_len;
    methinfo->shortcut_result_size = (unsigned int)result_size;
    return 0;
#endif /* PY_VERSION_HEX >= 0x03090000 */
}

static struct _PyObjC_ArgDescr* _Nullable alloc_descr(
    struct _PyObjC_ArgDescr* _Nullable tmpl)
{
    struct _PyObjC_ArgDescr* retval = PyMem_Malloc(sizeof(*retval));
    if (retval == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }
    memset(retval, 0, sizeof(*retval)); /* XXX */
    /* XXX: Try to refactor this to ensure the type value can be _Nonnull */
    retval->type              = tmpl ? tmpl->type : NULL;
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

static BOOL
is_default_descr(struct _PyObjC_ArgDescr* descr)
{
    if (descr->type != NULL)
        return NO;
    /* ignore modifier */
    if (descr->ptrType != PyObjC_kPointerPlain)
        return NO;
    if (descr->allowNULL != YES)
        return NO;
    if (descr->arraySizeInRetval != NO)
        return NO;
    if (descr->printfFormat != NO)
        return NO;
    if (descr->alreadyRetained != NO)
        return NO;
    if (descr->alreadyCFRetained != NO)
        return NO;
    if (descr->callableRetained != NO)
        return NO;
    if (descr->callable != NULL)
        return NO;
    if (descr->sel_type != NULL)
        return NO;
    return YES;
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
        if (meta->type == NULL) { // LCOV_BR_EXCL_LINE
            return -1;            // LCOV_EXCL_LINE
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

    } else {
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
            cur++;
            while (isdigit(*cur))
                cur++;
        }
        nargs++;
    }
    if (cur == NULL && PyErr_Occurred()) {
        return NULL;
    }

    char* signature_copy = PyObjCUtil_Strdup(signature);
    if (signature_copy == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE
    }

    retval = PyObject_NewVar(PyObjCMethodSignature,
                             (PyTypeObject*)PyObjCMethodSignature_Type, nargs /*+1*/);

    if (retval == NULL) { // LCOV_BR_EXCL_LINE
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
    if (unlikely(cur[0] == _C_ID && cur[1] == _C_UNDEF)) {
        retval->rettype = (__typeof__(retval->rettype))&block_template;
    } else if (unlikely(cur[0] == _C_PTR)) {
        retval->rettype =
            (__typeof__(retval->rettype))&ptr_templates[*(unsigned char*)(cur + 1)];

    } else if (unlikely(cur[0] == _C_IN && cur[1] == _C_PTR)) {
        retval->rettype =
            (__typeof__(retval->rettype))&ptr_in_templates[*(unsigned char*)(cur + 2)];

    } else if (unlikely(cur[0] == _C_OUT && cur[1] == _C_PTR)) {
        retval->rettype =
            (__typeof__(retval->rettype))&ptr_out_templates[*(unsigned char*)(cur + 2)];

    } else if (unlikely(cur[0] == _C_INOUT && cur[1] == _C_PTR)) {
        retval->rettype =
            (__typeof__(retval->rettype))&ptr_inout_templates[*(unsigned char*)(cur + 2)];

    } else {
        retval->rettype =
            (__typeof__(retval->rettype))&descr_templates[*(unsigned char*)(cur)];
    }

    if (unlikely(retval->rettype->type == NULL)) {
        retval->rettype = alloc_descr(NULL);
        if (retval->rettype == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }

        /* Ignore type specifiers for methods returning void. Mostly needed
         * to avoid crapping out one (oneway void) methods.
         */
        assert(retval->signature != NULL);
        if (setup_type(retval->rettype, cur) < 0) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(retval);
            return NULL;
            // LCOV_EXCL_STOP
        }
        assert(retval->rettype->type != NULL);
    }
    assert(retval->rettype->type != NULL);

    cur = PyObjCRT_SkipTypeSpec(retval->signature);
    if (cur && *cur == '"') {
        cur++;
        while (*cur != '\0' && *cur != '"') {
            cur++;
        }
        cur++;
        while (isdigit(*cur))
            cur++;
    }
    nargs = 0;
    while (cur && *cur) {
        if (unlikely(*cur == _C_CONST)) {
            /* Ignore a 'const' qualifier, not used by the bridge */
            cur++;
        }
        if (unlikely(cur[0] == _C_ID && cur[1] == _C_UNDEF)) {
            retval->argtype[nargs] = (__typeof__(retval->argtype[nargs]))&block_template;
        } else {
            retval->argtype[nargs] =
                (__typeof__(retval
                                ->argtype[nargs]))&descr_templates[*(unsigned char*)cur];
        }
        if (unlikely(retval->argtype[nargs]->type == NULL)) {
            retval->argtype[nargs] = alloc_descr(NULL);
            if (unlikely(retval->argtype[nargs] == NULL)) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(retval);
                return NULL;
                // LCOV_EXCL_STOP
            }
            assert(cur != NULL);
            if (setup_type(retval->argtype[nargs], cur) < 0) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(retval);
                return NULL;
                // LCOV_EXCL_STOP
            }
            assert(retval->argtype[nargs]->type != NULL);
        }

        cur = PyObjCRT_SkipTypeSpec(cur);
        if (cur && *cur == '"') {
            cur++;
            while (*cur != '\0' && *cur != '"') {
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

    if (determine_if_shortcut(retval) < 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(retval);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return retval;
}

char* _Nullable PyObjC_NSMethodSignatureToTypeString(NSMethodSignature* sig, char* buf,
                                                     size_t buflen)
{
    char*      result = buf;
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
setup_descr(struct _PyObjC_ArgDescr* descr, PyObject* _Nullable meta, BOOL is_native)
{
    PyObject* d;
    int r;
    char      typeModifier = 0;

    if (meta == Py_None) {
        return 0;
    }

    if (meta != NULL && !PyDict_Check(meta)) {
        PyErr_Format(PyExc_TypeError, "metadata of type %s: %R", Py_TYPE(meta)->tp_name,
                     meta);

        return -1;
    }

    assert(meta == NULL || PyDict_Check(meta));
    assert(descr == NULL || descr->allowNULL);

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_null_accepted, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1; // LCOV_EXCL_LINE
        /* case 0: pass */
       case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (!r) {
                if (descr == NULL || descr->tmpl)  {
                    Py_DECREF(d);
                    return -2;
                }
                descr->allowNULL = NO;
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_already_retained, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1; // LCOV_EXCL_LINE
        case 0:
            if (descr == NULL || (descr->tmpl && descr->alreadyRetained))
                return -2;
            // descr may be loaded into read-only memory, so only
            // write if truly necessary
            if (descr->alreadyRetained) // LCOV_BR_EXCL_LINE
                descr->alreadyRetained = NO; // LCOV_EXCL_LINE
            break;
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || (descr->tmpl && !descr->alreadyRetained)) {
                    Py_DECREF(d);
                    return -2;
                }
                // descr may be loaded into read-only memory, so only
                // write if truly necessary
                if (!descr->alreadyRetained)
                    descr->alreadyRetained = YES;
            }
            Py_CLEAR(d);
            break;
        }
    }

    assert(descr == NULL || !descr->alreadyCFRetained);
    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_already_cfretained, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE

        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }
                descr->alreadyCFRetained = YES;
                Py_CLEAR(d);
            }
        }
    }

    assert(descr == NULL || !descr->callableRetained);
    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_callable_retained, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
       case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }
                descr->callableRetained = YES;
            }
            Py_CLEAR(d);
        }
    }

    assert(descr == NULL || descr->sel_type == NULL);
    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_sel_of_type, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyUnicode_Check(d)) {
                PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
                if (bytes == NULL) {
                    Py_DECREF(d);
                    return -1;
                }

                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    Py_DECREF(bytes);
                    return -2;
                }

                descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
                Py_DECREF(bytes);
                if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
                    Py_DECREF(d);
                    return -1;                 // LCOV_EXCL_LINE
                }

            } else if (PyBytes_Check(d)) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->sel_type = PyObjCUtil_Strdup(PyBytes_AsString(d));
                if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
                    Py_DECREF(d);
                    return -1;                 // LCOV_EXCL_LINE
                }
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_callable, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
       case 1:
            if (descr == NULL || descr->tmpl) {
                Py_DECREF(d);
                return -2;
            }

            /* Make up a dummy signature, will be overridden by
             * the metadata.
             */
            char      buffer[128];
            PyObject* a = NULL;
            Py_ssize_t i, len;

            switch (PyDict_GetItemRef(d, PyObjCNM_arguments, &a)) { // LCOV_BR_EXCL_LINE
            case -1:
                Py_DECREF(d);
                return -1;                       // LCOV_EXCL_LINE
            case 0:
                buffer[0] = _C_ID;
                buffer[1] = '\0';
                break;
            case 1:
                len = PyDict_Size(a);
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
    }

    assert(descr == NULL || !descr->arraySizeInRetval);
    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_c_array_length_in_result, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->arraySizeInRetval = YES;
            }
            Py_CLEAR(d);
        }
    }

    assert(descr == NULL || !descr->printfFormat);
    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_printf_format, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /*case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->printfFormat = YES;
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_c_array_delimited_by_null, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->ptrType = PyObjC_kNullTerminatedArray;
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_c_array_of_fixed_length, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyLong_Check(d)) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
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
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_c_array_of_variable_length, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->ptrType  = PyObjC_kVariableLengthArray;
                descr->arrayArg = 0;
                descr->arrayArg = 0;
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_deref_result_pointer, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = PyObject_IsTrue(d);
            if (r == -1) {
                return -1;
            }
            if (r) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->ptrType  = PyObjC_kDerefResultPointer;
                descr->arrayArg = 0;
                descr->arrayArg = 0;
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_c_array_length_in_arg, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyLong_Check(d)) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                descr->ptrType  = PyObjC_kArrayCountInArg;
                descr->arrayArg = PyLong_AsLong(d);
                if (descr->arrayArg == -1 && PyErr_Occurred()) {
                    Py_DECREF(d);
                    return -1;
                }
                descr->arrayArgOut = descr->arrayArg;

            } else if (PyTuple_Check(d)) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
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
                        PyErr_SetString(PyExc_TypeError,
                                        "array_out argument not integer");
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
                        PyErr_SetString(PyExc_TypeError,
                                        "array_out argument not integer");
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
                        PyErr_SetString(PyExc_TypeError,
                                        "array_out argument not integer");
                        return -1;
                    }
                }
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_type_modifier, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (PyUnicode_Check(d)) {
                PyObject* bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
                if (bytes == NULL) {
                    Py_DECREF(d);
                    return -1;
                }

                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    Py_DECREF(bytes);
                    return -2;
                }

                typeModifier = *PyBytes_AsString(bytes);
                assert(!PyErr_Occurred());
                Py_CLEAR(bytes);
            } else if (PyBytes_Check(d)) {
                if (descr == NULL || descr->tmpl) {
                    Py_DECREF(d);
                    return -2;
                }

                typeModifier = *PyBytes_AsString(d);
                assert(!PyErr_Occurred());
            }
            Py_CLEAR(d);
        }
    }

    if (meta) {
        switch (PyDict_GetItemRef(meta, PyObjCNM_type, &d)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        /* case 1: pass */
        }

    } else {
        d = NULL;
    }

    if (d && (PyBytes_Check(d) || PyUnicode_Check(d))) {

        PyObject* bytes = NULL;

        if (descr == NULL || descr->tmpl) {
            Py_XDECREF(d);
            return -2;
        }

        descr->modifier = typeModifier;

        if (PyUnicode_Check(d)) {
            bytes = PyUnicode_AsEncodedString(d, NULL, NULL);
            if (bytes == NULL) {
                Py_XDECREF(d);
                return -1;
            }

        } else if (PyBytes_Check(d)) {
            bytes = d;
            d = NULL;

        } else {
            PyErr_Format(PyExc_TypeError, "key %R value %R is not a (byte) string", PyObjCNM_type, d);
            Py_XDECREF(d);
            return -1;
        }

        const char* type = PyBytes_AsString(bytes);

        /* XXX: This assertion is not really useful and needs to be more clear */
        assert(!is_native || descr->type != NULL);

        if (is_native && !PyObjC_signatures_compatible(descr->type, type)) {
            /* The new signature is not compatible enough, ignore the
             * override.
             */
            type = descr->type;
        }

        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(type);
        size_t bufsize = strlen(withoutModifiers) + 2;
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
            strlcpy(tp + 1, withoutModifiers, bufsize-1);
            tp[0] = typeModifier;
        } else {
            strlcpy(tp, type, bufsize);
        }
        assert(tp != NULL);
        descr->typeOverride = YES;
        descr->type         = tp;
        Py_XDECREF(bytes);

    } else if (descr != NULL && descr->type == NULL) {
        if (typeModifier != '\0') {
            if (descr->tmpl) {
                Py_XDECREF(d);
                return -2;
            }
        }
        descr->modifier = typeModifier;

    } else if (descr != NULL && descr->type != NULL) {
        /* XXX: Is this case still needed? */
        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
        assert(*withoutModifiers != _C_ARY_B);
        if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID
            && descr->ptrType == PyObjC_kPointerPlain) {

            /* Plain old void*, ignore type modifiers */

        } else if (typeModifier != '\0') {
            if (descr->tmpl) {
                Py_XDECREF(d);
                return -2;
            }

            size_t bufsize = strlen(withoutModifiers) + 2;
            char* tp = PyMem_Malloc(bufsize);
            if (tp == NULL) { // LCOV_BR_EXCL_START
                // LCOV_EXCL_START
                Py_XDECREF(d);
                PyErr_NoMemory();
                return -1;
                // LCOV_EXCL_STOP
            }

            tp[0] = typeModifier;
            strlcpy(tp + 1, withoutModifiers, bufsize-1);

            if (descr->typeOverride) {
                PyMem_Free((void*)(descr->type));
            }

            /* Skip existing modifiers, we're overriding those */
            descr->typeOverride = YES;
            descr->type         = tp;
        }
    }
    Py_CLEAR(d);
    return 0;
}

static int
process_metadata_dict(PyObjCMethodSignature* methinfo, PyObject* _Nullable metadata,
                      BOOL                   is_native)
{
    PyObject* v;
    int r;

    if (metadata != NULL && !PyDict_Check(metadata)) {
        PyErr_Format(PyExc_TypeError,
                     "Metadata dictionary is of type '%s' instead of 'dict'",
                     Py_TYPE(metadata)->tp_name);
        return -1;
    }

    if (metadata) {
        PyObject* retval;
        PyObject* av;
        int r;

        switch (PyDict_GetItemRef(metadata, PyObjCNM_retval, &retval)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                            // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            r = setup_descr(methinfo->rettype, retval, is_native);
            if (r == -1) {
                Py_DECREF(retval);
                return -1;

            } else if (r == -2) {
                methinfo->rettype = alloc_descr(methinfo->rettype);
                if (methinfo->rettype == NULL) { // LCOV_BR_EXCL_LINE
                    Py_DECREF(retval);
                    return -1;                   // LCOV_EXCL_LINE
                }
                r = setup_descr(methinfo->rettype, retval, is_native);
                if (r == -1) {
                    Py_DECREF(retval);
                    return -1;
                }
                assert(r != -2);
            }

            switch (PyDict_GetItemRef(metadata, PyObjCNM_free_result, &av)) { // LCOV_BR_EXCL_LINE
            case -1:
                // LCOV_EXCL_START
                Py_DECREF(retval);
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
            Py_CLEAR(retval);
        }
    }

    if (metadata) {
        PyObject* args;

        switch (PyDict_GetItemRef(metadata, PyObjCNM_arguments, &args)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                          // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            if (!PyDict_Check(args)) {
                Py_CLEAR(args);
            }

            Py_ssize_t i;
            for (i = 0; i < Py_SIZE(methinfo); i++) {
                PyObject* k = PyLong_FromLong(i);
                PyObject* d = NULL;
                int       r;

                if (args) {
                    switch(PyDict_GetItemRef(args, k, &d)) { // LCOV_BR_EXCL_LINE
                    case -1:
                        // LCOV_EXCL_START
                        Py_DECREF(k);
                        Py_DECREF(args);
                        return -1;
                        // LCOV_EXCL_STOP
                    /* case 0: pass */
                    /* case 1: pass */
                    }
                    Py_CLEAR(k);

                } else {
                    /* No metadata, hence no need to call setup_descr */
                    assert(methinfo->argtype[i] == NULL);
                    continue;
                }

                r = setup_descr(methinfo->argtype[i], d, is_native);
                if (r == -1) {
                    Py_XDECREF(d);
                    Py_DECREF(args);
                    return -1;

                } else if (r == -2) {
                    methinfo->argtype[i] = alloc_descr(methinfo->argtype[i]);
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

        switch (PyDict_GetItemRef(metadata, PyObjCNM_suggestion, &v)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
        /* case 0: pass */
        case 1:
            methinfo->suggestion = v;
            v = NULL;
        }

        switch (PyDict_GetItemRef(metadata, PyObjCNM_deprecated, &v)) { // LCOV_BR_EXCL_LINE
        case -1:;
            return -1;                       // LCOV_EXCL_LINE
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
        switch(PyDict_GetItemRef(metadata, PyObjCNM_c_array_delimited_by_null, &v)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
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
        switch (PyDict_GetItemRef(metadata, PyObjCNM_c_array_length_in_arg, &v)) { // LCOV_BR_EXCL_LINE
        case -1:
            return -1;                       // LCOV_EXCL_LINE
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
            return -1;                       // LCOV_EXCL_LINE
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
                    methinfo->suggestion =
                        PyUnicode_FromString("Variadic functions/methods are not supported");
                    if (methinfo->suggestion == NULL) {
                        Py_DECREF(v);
                        Py_DECREF(methinfo);
                        return -1;
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
    switch (PyDict_GetItemRef(metadata, PyObjCNM_arguments, &arguments)) { // LCOV_BR_EXCL_LINE
    case -1:
        return NULL;                             // LCOV_EXCL_LINE
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
                        PyErr_Clear();
                    }
                    if (k > max_idx) {
                        max_idx = k;
                    }
                }
            }
            Py_END_CRITICAL_SECTION();

            max_idx += 1;
        }
    }

    result = PyObject_NewVar(PyObjCMethodSignature,
                             (PyTypeObject*)PyObjCMethodSignature_Type, max_idx);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    Py_SET_SIZE(result, max_idx);
    /* XXX: This will be set to a non-null value in all non-error paths */
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
    /* XXX: This will be set to a non-null value in all non-error paths */
    result->rettype = (struct _PyObjC_ArgDescr* _Nonnull)NULL;
    for (i = 0; i < max_idx; i++) {
        result->argtype[i] = NULL;
    }

    switch (PyDict_GetItemRef(metadata, PyObjCNM_full_signature, &value)) { // LCOV_BR_EXCL_LINE
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

    if (result->rettype != NULL && !result->rettype->tmpl) {
        result->rettype->tmpl = YES;
    }
    for (i = 0; i < max_idx; i++) {
        if (result->argtype[i] == NULL)
            continue;
        if (!result->argtype[i]->tmpl) {
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
     * Leak a reference to 'compiled' to ensure it stays alive
     * even when someone registers new metadata for the same
     * selector.
     *
     * XXX: Why is this needed?
     * -- Py_DECREF(compiled); --
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

    if (determine_if_shortcut(methinfo) < 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(methinfo);
        return NULL;
        // LCOV_EXCL_STOP
    }

    return methinfo;
}

static struct _PyObjC_ArgDescr* _Nullable merge_descr(struct _PyObjC_ArgDescr* descr,
                                                      struct _PyObjC_ArgDescr* meta,
                                                      BOOL                     is_native)
{
    if (meta == NULL) {
        return descr;
    }
    if (meta->type != NULL) {
        if (!is_native || PyObjC_signatures_compatible(descr->type, meta->type)) {
            if (!descr->tmpl) {
                if (descr->typeOverride) {
                    PyMem_Free((void*)descr->type);
                }
                PyMem_Free(descr);
            }
            return meta;
        }
    }

    /* Copy argdescr, assume there is no trivial metadata */
    BOOL copied = NO;

    if (descr->tmpl) {
        descr = alloc_descr(descr);
        if (descr == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;     // LCOV_EXCL_LINE
        }
        copied = YES;
    }
    if (meta->callable) {
        Py_XINCREF(meta->callable);
        Py_XDECREF(descr->callable);
        descr->callable = meta->callable;
    }

    if (descr->sel_type) {
        PyMem_Free((void*)descr->sel_type);
    }
    if (meta->sel_type) {
        descr->sel_type = PyObjCUtil_Strdup(meta->sel_type);
        if (descr->sel_type == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            if (copied) {
                PyMem_Free(descr);
            }
            PyErr_NoMemory();
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
        const char* withoutModifiers = PyObjCRT_SkipTypeQualifiers(descr->type);
        assert(*withoutModifiers != _C_ARY_B);
        if (descr->type[0] == _C_PTR && descr->type[1] == _C_VOID
            && descr->ptrType == PyObjC_kPointerPlain) {

            /* Plain old void*, ignore type modifiers */

        } else { // LCOV_EXCL_LINE
            size_t bufsize = strlen(withoutModifiers) + 2;
            char* tp      = PyMem_Malloc(bufsize);
            char* to_free = NULL;
            if (tp == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                if (copied) {
                    PyMem_Free(descr);
                }
                PyErr_NoMemory();
                return NULL;
                // LCOV_EXCL_STOP
            }

            if (descr->typeOverride) {
                to_free = (char*)(descr->type);
            }

            /* Skip existing modifiers, we're overriding those */
            assert(tp != NULL);
            strlcpy(tp + 1, withoutModifiers, bufsize-1);
            tp[0]               = meta->modifier;
            descr->typeOverride = YES;
            descr->type         = tp;

            if (to_free) {
                PyMem_Free(to_free);
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

    if (methinfo->rettype->tmpl && metadata->rettype != NULL
        && metadata->rettype->modifier != '\0' && is_default_descr(metadata->rettype)) {
        const char* withoutModifiers =
            PyObjCRT_SkipTypeQualifiers(methinfo->rettype->type);
        if (withoutModifiers[0] == _C_PTR) {
            switch (metadata->rettype->modifier) {
            case _C_IN:
                metadata->rettype = (struct _PyObjC_ArgDescr*)&ptr_in_templates[(
                    unsigned char)(withoutModifiers[1])];
                break;
            case _C_OUT:
                metadata->rettype = (struct _PyObjC_ArgDescr*)&ptr_out_templates[(
                    unsigned char)(withoutModifiers[1])];
                break;
            case _C_INOUT:
                metadata->rettype = (struct _PyObjC_ArgDescr*)&ptr_inout_templates[(
                    unsigned char)(withoutModifiers[1])];
                break;
            }
        }
        /* No 'else': the metadata is default and hence won't update what we already have
         */

    } else {
        tmp = merge_descr(methinfo->rettype, metadata->rettype, is_native);
        if (tmp == NULL) {
            return -1;
        }
        methinfo->rettype = tmp;
    }

    len = Py_SIZE(methinfo);
    if (Py_SIZE(metadata) < Py_SIZE(methinfo)) {
        len = Py_SIZE(metadata);
    }

    for (i = 0; i < len; i++) {
        if (methinfo->argtype[i]->tmpl && metadata->argtype[i] != NULL
            && metadata->argtype[i]->modifier != '\0'
            && is_default_descr(metadata->argtype[i])) {
            const char* withoutModifiers =
                PyObjCRT_SkipTypeQualifiers(methinfo->argtype[i]->type);
            if (withoutModifiers[0] == _C_PTR) {
                switch (metadata->argtype[i]->modifier) {
                case _C_IN:
                    metadata->argtype[i] = (struct _PyObjC_ArgDescr*)&ptr_in_templates[(
                        unsigned char)(withoutModifiers[1])];
                    break;
                case _C_OUT:
                    metadata->argtype[i] = (struct _PyObjC_ArgDescr*)&ptr_out_templates[(
                        unsigned char)(withoutModifiers[1])];
                    break;
                case _C_INOUT:
                    metadata->argtype[i] =
                        (struct _PyObjC_ArgDescr*)&ptr_inout_templates[(
                            unsigned char)(withoutModifiers[1])];
                    break;
                }
            }
            /* No 'else': the metadata is default and hence won't update what we already
             * have */

        } else {
            tmp = merge_descr(methinfo->argtype[i], metadata->argtype[i], is_native);
            if (tmp == NULL) {
                return -1;
            }
            methinfo->argtype[i] = tmp;
        }
    }

    return determine_if_shortcut(methinfo);
}

PyObjCMethodSignature*
PyObjCMethodSignature_GetRegistered(Class cls, SEL sel)
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

    if (metadata != NULL && ((PyObjCMethodSignature*)metadata)->signature) {
        methinfo = new_methodsignature(((PyObjCMethodSignature*)metadata)->signature);
    } else {
        methinfo = new_methodsignature(signature);
    }
    if (methinfo == NULL) {
        return NULL;
    }

    if (process_metadata_object(methinfo, (PyObjCMethodSignature*)metadata, is_native)
        == -1) {
        Py_DECREF(methinfo);
        Py_XDECREF(metadata);
        return NULL;
    }


    if (isClassMethod) {
        const char* nm = sel_getName(sel);
        if (strncmp(nm, "new", 3) == 0 && ((nm[3] == 0) || isupper(nm[3]))) {
            if (methinfo->rettype->tmpl) {
                methinfo->rettype = alloc_descr(methinfo->rettype);
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

    if (methinfo->rettype != NULL && methinfo->rettype->type != NULL && methinfo->rettype->type[0] == _C_ID) {
        const char* nm = sel_getName(sel);
        // The check below matches the calculation of the default objc_method_family in clang
        // (other than the special casing of NSAutoreleasePool)
        if (sel_isEqual(sel, @selector(init)) ||
            ((strncmp(nm, "init", 4) == 0) && isupper(nm[4]))) {
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
    }

    if (descr->printfFormat) {
        r = PyDict_SetItem(result, PyObjCNM_printf_format, descr->printfFormat?Py_True:Py_False);
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
        r = PyDict_SetItem(result, PyObjCNM_already_retained, descr->alreadyRetained?Py_True:Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->alreadyCFRetained) {
        r = PyDict_SetItem(result, PyObjCNM_already_cfretained, descr->alreadyCFRetained?Py_True:Py_False);
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

        r = PyDict_SetItem(result, PyObjCNM_callable_retained, descr->callableRetained?Py_True:Py_False);
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
        r = PyDict_SetItem(result, PyObjCNM_c_array_length_in_result, descr->arraySizeInRetval?Py_True:Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (descr->type == NULL || *PyObjCRT_SkipTypeQualifiers(descr->type) == _C_PTR) {
        r = PyDict_SetItem(result, PyObjCNM_null_accepted, descr->allowNULL?Py_True:Py_False);
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
        r = PyDict_SetItem(result, PyObjCNM_free_result, methinfo->free_result?Py_True:Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->initializer) {
        r = PyDict_SetItem(result, PyObjCNM_initializer, methinfo->initializer?Py_True:Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->variadic) {
        r = PyDict_SetItem(result, PyObjCNM_variadic, methinfo->variadic?Py_True:Py_False);
        if (r == -1)    // LCOV_BR_EXCL_LINE
            goto error; // LCOV_EXCL_LINE
    }

    if (methinfo->variadic && methinfo->null_terminated_array) {
        r = PyDict_SetItem(result, PyObjCNM_c_array_delimited_by_null, methinfo->null_terminated_array?Py_True:Py_False);
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
        return -1; // LCOV_EXCL_LINE
    }
    PyObjCMethodSignature_Type = tmp;

    tmp = PyObjC_NewRegistry();
    if (tmp == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    registry = tmp;
    return 0;
}

NS_ASSUME_NONNULL_END
