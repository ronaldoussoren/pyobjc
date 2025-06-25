/*
 * AudioValueTranslation bindings
 */

static PyObject* audio_value_translation_type;

#define audio_value_translation_check(obj)                                               \
    PyObject_TypeCheck(obj, (PyTypeObject*)audio_value_translation_type)

struct audio_value_translation {
    PyObject_HEAD

    char                   avt_ownsstorage;
    char                   avt_owns_input_buffer;
    char                   avt_owns_output_buffer;
    void*                  avt_input_buffer;  /* for owned sample storage */
    void*                  avt_output_buffer; /* for owned sample storage */
    AudioValueTranslation* avt_translation;
};

static PyMemberDef avt_members[] = {
    {.name   = "_owns_storage",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_value_translation, avt_ownsstorage),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the AudioBufer"},
    {.name   = "_owns_input_buffer",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_value_translation, avt_owns_input_buffer),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the input buffer"},
    {.name   = "_owns_output_buffer",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_value_translation, avt_owns_output_buffer),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the output buffer"},

    {.name = NULL} /* Sentinel */
};

static PyObject*
avt_get_mInputDataSize(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    PyObject*                       result;

    Py_BEGIN_CRITICAL_SECTION(self);
    result = Py_BuildValue("I", self->avt_translation->mInputDataSize);
    Py_END_CRITICAL_SECTION();
    return result;
}

static PyObject*
avt_get_mOutputDataSize(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    PyObject*                       result;

    Py_BEGIN_CRITICAL_SECTION(self);
    result = Py_BuildValue("I", self->avt_translation->mOutputDataSize);
    Py_END_CRITICAL_SECTION();
    return result;
}

static PyObject*
avt_get_mInputData(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    PyObject*                       result;

    if (self->avt_translation->mInputData == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }
    Py_BEGIN_CRITICAL_SECTION(self);
    result = PyMemoryView_FromMemory(self->avt_translation->mInputData,
                                     self->avt_translation->mInputDataSize, PyBUF_WRITE);
    Py_END_CRITICAL_SECTION();
    return result;
}

static PyObject*
avt_get_mOutputData(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    PyObject*                       result;

    if (self->avt_translation->mOutputData == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    result = PyMemoryView_FromMemory(self->avt_translation->mOutputData,
                                     self->avt_translation->mOutputDataSize, PyBUF_WRITE);
    Py_END_CRITICAL_SECTION();
    return result;
}

static PyGetSetDef avt_getset[] = {
    {.name    = "mInputData",
     .get     = avt_get_mInputData,
     .set     = NULL,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mInputDataSize",
     .get     = avt_get_mInputDataSize,
     .set     = NULL,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mOutputData",
     .get     = avt_get_mOutputData,
     .set     = NULL,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mOutputDataSize",
     .get     = avt_get_mOutputDataSize,
     .set     = NULL,
     .doc     = NULL,
     .closure = NULL},

    {.name = NULL} /* Sentinel */
};

PyDoc_STRVAR(avt_create_input_buffer_doc,
             "create_input_buffer(buffer_size)\n" CLINIC_SEP
             "Create a (new) buffer for storing audio samples. This replaces \n"
             "the previous buffer. After calling this method the memoryview \n"
             "retrieved from the mInputData attribute are no longer valid.");
static PyObject*
avt_create_input_buffer(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"buffer_size", NULL};

    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    unsigned int                    buf_size;
    void*                           new_buf;

    if (PyArg_ParseTupleAndKeywords(args, kwds, "I", keywords, &buf_size) == -1) {
        return NULL;
    }

    new_buf = PyMem_Malloc(buf_size);
    if (new_buf == NULL) {
        return NULL;
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    if (self->avt_owns_input_buffer && self->avt_input_buffer != NULL) {
        PyMem_Free(self->avt_input_buffer);
    }

    self->avt_input_buffer = self->avt_translation->mInputData = new_buf;
    self->avt_owns_input_buffer                                = 1;
    self->avt_translation->mInputDataSize                      = buf_size;
    Py_END_CRITICAL_SECTION();

    Py_INCREF(Py_None);
    return Py_None;
}

PyDoc_STRVAR(avt_create_output_buffer_doc,
             "create_output_buffer(buffer_size)\n" CLINIC_SEP
             "Create a (new) buffer for storing audio samples. This replaces \n"
             "the previous buffer. After calling this method the memoryview \n"
             "retrieved from the mOutputData attribute are no longer valid.");
static PyObject*
avt_create_output_buffer(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"buffer_size", NULL};

    struct audio_value_translation* self = (struct audio_value_translation*)_self;
    unsigned int                    buf_size;
    void*                           new_buf;

    if (PyArg_ParseTupleAndKeywords(args, kwds, "I", keywords, &buf_size) == -1) {
        return NULL;
    }

    new_buf = PyMem_Malloc(buf_size);
    if (new_buf == NULL) {
        return NULL;
    }

    Py_BEGIN_CRITICAL_SECTION(self);
    if (self->avt_owns_output_buffer && self->avt_output_buffer != NULL) {
        PyMem_Free(self->avt_output_buffer);
    }

    self->avt_output_buffer = self->avt_translation->mOutputData = new_buf;
    self->avt_owns_output_buffer                                 = 1;
    self->avt_translation->mOutputDataSize                       = buf_size;

    Py_END_CRITICAL_SECTION();
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef avt_methods[] = {
    {.ml_name  = "create_input_buffer",
     .ml_meth  = (PyCFunction)avt_create_input_buffer,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = avt_create_input_buffer_doc},
    {.ml_name  = "create_output_buffer",
     .ml_meth  = (PyCFunction)avt_create_output_buffer,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = avt_create_output_buffer_doc},

    {.ml_name = NULL} /* Sentinel */
};

static PyObject*
avt_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"input_buffer_size", "output_buffer_size", NULL};
    /* Args: channels (default to 1), size (default: no buffer) */
    struct audio_value_translation* result;
    Py_ssize_t                      input_bufsize  = -1;
    Py_ssize_t                      output_bufsize = -1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|$nn", keywords, &input_bufsize,
                                     &output_bufsize)) {
        return NULL;
    }

    if ((input_bufsize != -1 && input_bufsize < 0)
        || input_bufsize > (Py_ssize_t)UINT_MAX) {
        PyErr_SetString(PyExc_ValueError, "input bufsize out of range");
        return NULL;
    }
    if ((output_bufsize != -1 && output_bufsize < 0)
        || output_bufsize > (Py_ssize_t)UINT_MAX) {
        PyErr_SetString(PyExc_ValueError, "output bufsize out of range");
        return NULL;
    }

    result = PyObject_New(struct audio_value_translation,
                          (PyTypeObject*)audio_value_translation_type);
    if (result == NULL) {
        return NULL;
    }

    result->avt_ownsstorage       = 1;
    result->avt_owns_input_buffer = result->avt_owns_output_buffer = 0;
    result->avt_input_buffer = result->avt_output_buffer = NULL;
    result->avt_translation = PyMem_Malloc(sizeof(AudioValueTranslation));
    if (result->avt_translation == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->avt_translation->mInputData      = NULL;
    result->avt_translation->mInputDataSize  = 0;
    result->avt_translation->mOutputData     = NULL;
    result->avt_translation->mOutputDataSize = 0;

    if (input_bufsize != -1) {
        result->avt_translation->mInputData = PyMem_Malloc(input_bufsize);
        if (result->avt_translation->mInputData == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->avt_translation->mInputDataSize = (unsigned int)input_bufsize;
        result->avt_owns_input_buffer           = 1;
    }

    if (output_bufsize != -1) {
        result->avt_translation->mOutputData = PyMem_Malloc(output_bufsize);
        if (result->avt_translation->mOutputData == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->avt_translation->mOutputDataSize = (unsigned int)output_bufsize;
        result->avt_owns_output_buffer           = 1;
    }

    return (PyObject*)result;
}

static void
avt_dealloc(PyObject* object)
{
    struct audio_value_translation* self = (struct audio_value_translation*)object;

    if (self->avt_owns_input_buffer && self->avt_input_buffer != NULL) {
        PyMem_Free(self->avt_input_buffer);
    }
    if (self->avt_owns_output_buffer && self->avt_output_buffer != NULL) {
        PyMem_Free(self->avt_output_buffer);
    }
    if (self->avt_ownsstorage) {
        PyMem_Free(self->avt_translation);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(
    avt_doc,
    "AudioValueTranslation(*, input_buffer_size=1, output_buffer_size=-1)\n" CLINIC_SEP
    "Return an translation buffer. If a buffer size is specified "
    "this will allocate a buffer, otherwise no buffer is "
    "allocated\n");

static PyType_Slot avt_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&avt_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&avt_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&avt_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&avt_getset},
    {.slot = Py_tp_members, .pfunc = (void*)&avt_members},
    {.slot = Py_tp_new, .pfunc = (void*)&avt_new},

    {0, NULL} /* sentinel */
};

static PyType_Spec avt_spec = {
    .name      = "CoreAudio.AudioValueTranslation",
    .basicsize = sizeof(struct audio_value_translation),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = avt_slots,
};

static PyObject*
pythonify_audio_value_translation(void* pointer)
{
    AudioValueTranslation*          buf_pointer = (AudioValueTranslation*)pointer;
    struct audio_value_translation* result;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    result = PyObject_New(struct audio_value_translation,
                          (PyTypeObject*)audio_value_translation_type);
    if (result == NULL) {
        return NULL;
    }

    result->avt_ownsstorage       = 0;
    result->avt_owns_input_buffer = result->avt_owns_output_buffer = 0;
    result->avt_input_buffer = result->avt_output_buffer = NULL;

    result->avt_translation = buf_pointer;

    return (PyObject*)result;
}

static int
depythonify_audio_value_translation(PyObject* value, void* pointer)
{
    if (value == Py_None) {
        *(AudioValueTranslation**)pointer = NULL;
        return 0;
    }

    if (!audio_value_translation_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioValueTranslation', got '%.100s'",
                     Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioValueTranslation**)pointer =
        ((struct audio_value_translation*)value)->avt_translation;
    return 0;
}

static int
init_audio_value_translation(PyObject* module)
{
    int r;

    PyObject* tmp = PyType_FromSpec(&avt_spec);
    if (tmp == NULL) {
        return -1;
    }
    audio_value_translation_type = tmp;

    PyObject* ts = PyBytes_FromString(@encode(AudioValueTranslation));
    if (ts == NULL) {
        Py_CLEAR(audio_value_translation_type);
        return -1;
    }
    r = PyObject_SetAttrString(audio_value_translation_type, "__typestr__", ts);
    if (r == -1) {
        Py_CLEAR(audio_value_translation_type);
        return -1;
    }

    r = PyModule_AddObject(module, "AudioValueTranslation", audio_value_translation_type);
    if (r == -1) {
        Py_CLEAR(audio_value_translation_type);
        return -1;
    }
    Py_INCREF(audio_value_translation_type);

    r = PyObjCPointerWrapper_Register(
        "AudioValueTranslation*", @encode(AudioValueTranslation*),
        pythonify_audio_value_translation, depythonify_audio_value_translation);

    return r;
}
