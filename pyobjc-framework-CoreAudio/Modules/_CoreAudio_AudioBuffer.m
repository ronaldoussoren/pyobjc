/*
 * AudioBuffer bindings
 *
 * These are basic bindings to the AudioBuffer type,
 * basically a buffer with extra attributes.
 */

static PyObject* audio_buffer_type;

#define audio_buffer_check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)audio_buffer_type)

struct audio_buffer {
    PyObject_HEAD

    char         ab_owns_storage;
    char         ab_owns_buffer;
    void*        ab_buf_pointer; /* for owned sample storage */
    AudioBuffer* ab_buf;
};

static PyMemberDef ab_members[] = {
    {.name   = "_owns_storage",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_buffer, ab_owns_storage),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the AudioBufer"},
    {.name   = "_owns_buffer",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_buffer, ab_owns_buffer),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the audio samples"},

    {.name = NULL} /* Sentinel */
};

static PyObject*
ab_get_mNumberChannels(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    return Py_BuildValue("I", self->ab_buf->mNumberChannels);
}

static int
ab_set_mNumberChannels(PyObject* _self, PyObject* value,
                       void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mNumberChannels'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value,
                               &self->ab_buf->mNumberChannels);
}

static PyObject*
ab_get_mDataByteSize(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    return Py_BuildValue("I", self->ab_buf->mDataByteSize);
}

static PyObject*
ab_get_data(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    if (self->ab_buf->mData == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return PyMemoryView_FromMemory(self->ab_buf->mData, self->ab_buf->mDataByteSize,
                                   PyBUF_WRITE);
}

static PyGetSetDef ab_getset[] = {
    {.name    = "mNumberChannels",
     .get     = ab_get_mNumberChannels,
     .set     = ab_set_mNumberChannels,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mDataByteSize",
     .get     = ab_get_mDataByteSize,
     .set     = NULL,
     .doc     = NULL,
     .closure = NULL},
    {.name = "mData", .get = ab_get_data, .set = NULL, .doc = NULL, .closure = NULL},

    {.name = NULL} /* Sentinel */
};

PyDoc_STRVAR(ab_create_buffer_doc,
             "create_buffer(buffer_size)\n" CLINIC_SEP
             "Create a (new) buffer for storing audio samples. This replaces \n"
             "the previous buffer. After calling this method the memoryview \n"
             "retrieved from the mData attribute are no longer valid.");
static PyObject*
ab_create_buffer(PyObject* _self, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"buffer_size", NULL};

    struct audio_buffer* self = (struct audio_buffer*)_self;
    unsigned int         buf_size;
    void*                new_buf;

    if (PyArg_ParseTupleAndKeywords(args, kwds, "I", keywords, &buf_size) == -1) {
        return NULL;
    }

    new_buf = PyMem_Malloc(buf_size);
    if (new_buf == NULL) {
        return NULL;
    }

    if (self->ab_owns_buffer && self->ab_buf_pointer != NULL) {
        PyMem_Free(self->ab_buf_pointer);
    }

    self->ab_buf_pointer = self->ab_buf->mData = new_buf;
    self->ab_owns_buffer                       = 1;
    self->ab_buf->mDataByteSize                = buf_size;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef ab_methods[] = {
    {.ml_name  = "create_buffer",
     .ml_meth  = (PyCFunction)ab_create_buffer,
     .ml_flags = METH_VARARGS | METH_KEYWORDS,
     .ml_doc   = ab_create_buffer_doc},

    {.ml_name = NULL} /* Sentinel */
};

static PyObject*
ab_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"num_channels", "buffer_size", NULL};
    /* Args: channels (default to 1), size (default: no buffer) */
    struct audio_buffer* result;
    Py_ssize_t           bufsize      = -1;
    unsigned int         num_channels = 1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|$In", keywords, &num_channels,
                                     &bufsize)) {
        return NULL;
    }

    if ((bufsize != -1 && bufsize < 0) || bufsize > (Py_ssize_t)UINT_MAX) {
        PyErr_Format(PyExc_ValueError, "bufsize %ld out of range", (long)bufsize);
        return NULL;
    }

    result = PyObject_New(struct audio_buffer, (PyTypeObject*)audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_owns_storage = 1;
    result->ab_owns_buffer  = 0;
    result->ab_buf_pointer  = NULL;
    result->ab_buf          = PyMem_Malloc(sizeof(AudioBuffer));
    if (result == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->ab_buf->mNumberChannels = num_channels;
    result->ab_buf->mDataByteSize   = 0;
    result->ab_buf->mData           = NULL;

    if (bufsize != -1) {
        result->ab_buf->mData = result->ab_buf_pointer = PyMem_Malloc(bufsize);
        if (result->ab_buf->mData == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->ab_buf->mDataByteSize = (unsigned int)bufsize;
        result->ab_owns_buffer        = 1;
    }

    return (PyObject*)result;
}

static void
ab_dealloc(PyObject* object)
{
    struct audio_buffer* self = (struct audio_buffer*)object;

    if (self->ab_owns_buffer && self->ab_buf_pointer != NULL) {
        PyMem_Free(self->ab_buf_pointer);
    }
    if (self->ab_owns_storage) {
        PyMem_Free(self->ab_buf);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(ab_doc, "AudioBuffer(*, num_channels=1, buffer_size=-1)\n" CLINIC_SEP
                     "Return an audiobuffer. If a buffer size is specified "
                     "this will allocate a buffer, otherwise no buffer is "
                     "allocated\n");

static PyType_Slot ab_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&ab_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&ab_doc},
    {.slot = Py_tp_methods, .pfunc = (void*)&ab_methods},
    {.slot = Py_tp_getset, .pfunc = (void*)&ab_getset},
    {.slot = Py_tp_members, .pfunc = (void*)&ab_members},
    {.slot = Py_tp_new, .pfunc = (void*)&ab_new},

    {0, NULL} /* sentinel */
};

static PyType_Spec ab_spec = {
    .name      = "CoreAudio.AudioBuffer",
    .basicsize = sizeof(struct audio_buffer),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = ab_slots,
};

static PyObject*
ab_create(AudioBuffer* item)
{
    struct audio_buffer* result;

    result = PyObject_New(struct audio_buffer, (PyTypeObject*)audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_owns_storage = 0;
    result->ab_owns_buffer  = 0;
    result->ab_buf_pointer  = NULL;
    result->ab_buf          = item;

    return (PyObject*)result;
}

static PyObject*
pythonify_audio_buffer(void* pointer)
{
    AudioBuffer* buf_pointer = (AudioBuffer*)pointer;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return ab_create(*(AudioBuffer**)pointer);
}

static int
depythonify_audio_buffer(PyObject* value, void* pointer)
{
    if (value == Py_None) {
        *(AudioBuffer**)pointer = NULL;
        return 0;
    }

    if (!audio_buffer_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioBuffer', got '%.100s'",
                     Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioBuffer**)pointer = ((struct audio_buffer*)value)->ab_buf;
    return 0;
}

static int
init_audio_buffer(PyObject* module)
{
    int r;

    PyObject* tmp = PyType_FromSpec(&ab_spec);
    if (tmp == NULL) {
        return -1;
    }
    audio_buffer_type = tmp;

    PyObject* ts = PyBytes_FromString(@encode(AudioBuffer));
    if (ts == NULL) {
        Py_CLEAR(audio_buffer_type);
        return -1;
    }
    r = PyObject_SetAttrString(audio_buffer_type, "__typestr__", ts);
    Py_DECREF(ts);
    if (r == -1) {
        Py_CLEAR(audio_buffer_type);
        return -1;
    }

    r = PyModule_AddObject(module, "AudioBuffer", audio_buffer_type);
    if (r == -1) {
        Py_CLEAR(audio_buffer_type);
        return -1;
    }
    Py_INCREF(audio_buffer_type);

    r = PyObjCPointerWrapper_Register("AudioBuffer*", @encode(AudioBuffer*),
                                      pythonify_audio_buffer, depythonify_audio_buffer);

    return r;
}
