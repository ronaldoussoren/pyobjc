/*
 * AudioBufferList bindings
 *
 * These are basic bindings to the AudioBufferList type,
 * basically a buffer with extra attributes.
 */

static PyTypeObject audio_buffer_list_type; /* Forward definition */

#define audio_buffer_list_check(obj) PyObject_TypeCheck(obj, &audio_buffer_list_type)

struct audio_buffer_list {
    PyObject_HEAD

    char             abl_ownsstorage;
    PyObject*        abl_items; /* cache for Python version of abl_list items, needed for
                                 * ownership of buffer pointers.
                                 */
    AudioBufferList* abl_list;
};

static PyMemberDef abl_members[] = {
    {
        .name = "_ownsstorage",
        .type = T_BOOL,
        .offset = offsetof(struct audio_buffer_list, abl_ownsstorage),
        .flags = READONLY,
        .doc = "True iff this buffer owns the underlying storage"
    },

    { .name = NULL } /* Sentinel */
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
    PyObject* result;

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

static PySequenceMethods abl_as_sequence = {
    .sq_length = abl_length,
    .sq_item = abl_get_item,
};


static PyObject*
abl_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "num_buffers", NULL };
    struct audio_buffer_list* result;
    unsigned int num_buffers;
    unsigned int i;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "I", keywords, &num_buffers)) {
        return NULL;
    }

    result = PyObject_New(struct audio_buffer_list, &audio_buffer_list_type);
    if (result == NULL) {
        return NULL;
    }

    result->abl_ownsstorage = 1;
    result->abl_items = NULL;
    result->abl_list = PyMem_Malloc(sizeof(AudioBufferList) + (num_buffers * sizeof(AudioBuffer)));
    if (result->abl_list == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    result->abl_list->mNumberBuffers = num_buffers;

    for (i = 0; i < num_buffers; i++) {
        result->abl_list->mBuffers[i].mNumberChannels = 0;
        result->abl_list->mBuffers[i].mDataByteSize= 0;
        result->abl_list->mBuffers[i].mData = NULL;
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
    "AudioBufferList(num_buffers)\n"
    CLINIC_SEP
    "Return an audiobuffer list.");

static PyTypeObject audio_buffer_list_type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "CoreAudio.AudioBufferList",
    .tp_basicsize   = sizeof(struct audio_buffer_list),
    .tp_itemsize    = 0,
    .tp_dealloc     = abl_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = abl_doc,
    .tp_members     = abl_members,
    .tp_new         = abl_new,
    .tp_as_sequence = &abl_as_sequence,
};

static PyObject* pythonify_audio_buffer_list(void* pointer)
{
    AudioBufferList* buf_pointer = (AudioBufferList*)pointer;
    struct audio_buffer_list* result;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    result = PyObject_New(struct audio_buffer_list, &audio_buffer_list_type);
    if (result == NULL) {
        return NULL;
    }

    result->abl_ownsstorage = 0;
    result->abl_items = NULL;
    result->abl_list = buf_pointer;

    return (PyObject*)result;
}

static int depythonify_audio_buffer_list(PyObject* value, void* pointer)
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

    if (PyType_Ready(&audio_buffer_list_type) == -1) return -1;

    r = PyDict_SetItemString(audio_buffer_list_type.tp_dict, "__typestr__",
            PyBytes_FromString(@encode(AudioBufferList)));
    if (r == -1) return -1;

    Py_INCREF(&audio_buffer_list_type);
    r = PyModule_AddObject(module, "AudioBufferList", (PyObject*)&audio_buffer_list_type);
    if (r == -1) {
        Py_DECREF(&audio_buffer_list_type);
        return -1;
    }

    r = PyObjCPointerWrapper_Register(
        "AudioBufferList*",
        @encode(AudioBufferList*),
        pythonify_audio_buffer_list,
        depythonify_audio_buffer_list);

    return r;
}
