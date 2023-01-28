/*
 * AudioBufferList bindings
 *
 * These are basic bindings to the AudioBufferList type,
 * basically a buffer with extra attributes.
 */

static PyObject* audio_buffer_list_type;

#define audio_buffer_list_check(obj)                                                     \
    PyObject_TypeCheck(obj, (PyTypeObject*)audio_buffer_list_type)

struct audio_buffer_list {
    PyObject_HEAD

    char      abl_ownsstorage;
    PyObject* abl_items; /* cache for Python version of abl_list items, needed for
                          * ownership of buffer pointers.
                          */
    AudioBufferList* abl_list;
};

static PyMemberDef abl_members[] = {
    {.name   = "_ownsstorage",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_buffer_list, abl_ownsstorage),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns the underlying storage"},

    {.name = NULL} /* Sentinel */
};

static Py_ssize_t
abl_length(PyObject* self)
{
    if ((((struct audio_buffer_list*)self)->abl_list) == NULL) {
        return 0;
    }
    return ((struct audio_buffer_list*)self)->abl_list->mNumberBuffers;
}

static PyObject*
abl_get_item(PyObject* _self, Py_ssize_t idx)
{
    struct audio_buffer_list* self = ((struct audio_buffer_list*)_self);
    PyObject*                 result;

    if (self->abl_list == NULL) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }

    if (idx >= (Py_ssize_t)self->abl_list->mNumberBuffers) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    if (idx < 0) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }

    if (self->abl_items != NULL) {
        if (PyTuple_GET_ITEM(self->abl_items, idx) != Py_None) {
            Py_INCREF(PyTuple_GET_ITEM(self->abl_items, idx));
            return PyTuple_GET_ITEM(self->abl_items, idx);
        }
    } else {
        Py_ssize_t i;
        self->abl_items = PyTuple_New(self->abl_list->mNumberBuffers);
        if (self->abl_items == NULL) {
            return NULL;
        }
        for (i = 0; i < (Py_ssize_t)self->abl_list->mNumberBuffers; i++) {
            PyTuple_SET_ITEM(self->abl_items, i, Py_None);
            Py_INCREF(Py_None);
        }
    }

    result = ab_create(self->abl_list->mBuffers + idx);
    if (result == NULL) {
        return NULL;
    }

    Py_DECREF(PyTuple_GET_ITEM(self->abl_items, idx));
    PyTuple_SET_ITEM(self->abl_items, idx, result);
    Py_INCREF(result);
    return result;
}

static PyObject*
abl_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
    static char*              keywords[] = {"num_buffers", NULL};
    struct audio_buffer_list* result;
    unsigned int              num_buffers;
    unsigned int              i;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "I", keywords, &num_buffers)) {
        return NULL;
    }

    if (audio_buffer_list_type == NULL)
        abort();
    result =
        PyObject_New(struct audio_buffer_list, (PyTypeObject*)audio_buffer_list_type);
    if (result == NULL) {
        return NULL;
    }

    result->abl_ownsstorage = 1;
    result->abl_items       = NULL;
    result->abl_list =
        PyMem_Malloc(sizeof(AudioBufferList) + (num_buffers * sizeof(AudioBuffer)));
    if (result->abl_list == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    result->abl_list->mNumberBuffers = num_buffers;

    for (i = 0; i < num_buffers; i++) {
        result->abl_list->mBuffers[i].mNumberChannels = 0;
        result->abl_list->mBuffers[i].mDataByteSize   = 0;
        result->abl_list->mBuffers[i].mData           = NULL;
    }

    return (PyObject*)result;
}

static void
abl_dealloc(PyObject* object)
{
    struct audio_buffer_list* self = (struct audio_buffer_list*)object;

    if (self->abl_items) {
        Py_DECREF(self->abl_items);
    }

    if (self->abl_ownsstorage) {
        PyMem_Free(self->abl_list);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(abl_doc,
             "AudioBufferList(num_buffers)\n" CLINIC_SEP "Return an audiobuffer list.");

static PyType_Slot abl_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&abl_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&abl_doc},
    {.slot = Py_tp_members, .pfunc = (void*)&abl_members},
    {.slot = Py_tp_new, .pfunc = (void*)&abl_new},
    {.slot = Py_sq_length, .pfunc = (void*)&abl_length},
    {.slot = Py_sq_item, .pfunc = (void*)&abl_get_item},

    {0, NULL} /* sentinel */
};

static PyType_Spec abl_spec = {
    .name      = "CoreAudio.AudioBufferList",
    .basicsize = sizeof(struct audio_buffer_list),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = abl_slots,
};

static PyObject*
pythonify_audio_buffer_list(void* pointer)
{
    AudioBufferList*          buf_pointer = (AudioBufferList*)pointer;
    struct audio_buffer_list* result;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    result =
        PyObject_New(struct audio_buffer_list, (PyTypeObject*)audio_buffer_list_type);
    if (result == NULL) {
        return NULL;
    }

    result->abl_ownsstorage = 0;
    result->abl_items       = NULL;
    result->abl_list        = buf_pointer;

    return (PyObject*)result;
}

static int
depythonify_audio_buffer_list(PyObject* value, void* pointer)
{
    if (value == Py_None) {
        *(AudioBufferList**)pointer = NULL;
        return 0;
    }

    if (!audio_buffer_list_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioBufferList', got '%.100s'",
                     Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioBufferList**)pointer = ((struct audio_buffer_list*)value)->abl_list;
    return 0;
}

static int
init_audio_buffer_list(PyObject* module)
{
    int r;

    PyObject* tmp = PyType_FromSpec(&abl_spec);
    if (tmp == NULL) {
        return -1;
    }
    audio_buffer_list_type = tmp;

    PyObject* ts = PyBytes_FromString(@encode(AudioBufferList));
    if (ts == NULL) {
        Py_CLEAR(audio_buffer_list_type);
        return -1;
    }
    r = PyObject_SetAttrString(audio_buffer_list_type, "__typestr__", ts);
    Py_DECREF(ts);
    if (r == -1) {
        Py_CLEAR(audio_buffer_list_type);
        return -1;
    }

    r = PyModule_AddObject(module, "AudioBufferList", audio_buffer_list_type);
    if (r == -1) {
        Py_CLEAR(audio_buffer_list_type);
        return -1;
    }
    Py_INCREF(audio_buffer_list_type);

    r = PyObjCPointerWrapper_Register("AudioBufferList*", @encode(AudioBufferList*),
                                      pythonify_audio_buffer_list,
                                      depythonify_audio_buffer_list);

    return r;
}
