/*
 * AudioChannelLayout bindings
 *
 * These are basic bindings to the AudioChannelLayout type,
 * basically a buffer with extra attributes.
 */

static PyTypeObject audio_channel_layout_type; /* Forward definition */

#define audio_channel_layout_check(obj) PyObject_TypeCheck(obj, &audio_channel_layout_type)

struct audio_channel_layout {
    PyObject_HEAD

    char             avl_ownsstorage;
    PyObject*        avl_items; /* cache for Python version of avl_layout items, needed for
                                 * ownership of buffer pointers.
                                 */
    AudioChannelLayout* avl_layout;
};

static PyMemberDef avl_members[] = {
    {
        .name = "_ownsstorage",
        .type = T_BOOL,
        .offset = offsetof(struct audio_channel_layout, avl_ownsstorage),
        .flags = READONLY,
        .doc = "True iff this buffer owns the underlying storage"
    },

    { .name = NULL } /* Sentinel */
};


static PyObject*
avl_get_mChannelLayoutTag(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_layout* self = (struct audio_channel_layout*)_self;

    return Py_BuildValue("I", self->avl_layout->mChannelLayoutTag);
}

static int
avl_set_mChannelLayoutTag(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_channel_layout* self = (struct audio_channel_layout*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelLayoutTag'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value, &self->avl_layout->mChannelLayoutTag);
}

static PyObject*
avl_get_mChannelBitmap(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_layout* self = (struct audio_channel_layout*)_self;

    return Py_BuildValue("I", self->avl_layout->mChannelBitmap);
}

static int
avl_set_mChannelBitmap(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_channel_layout* self = (struct audio_channel_layout*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelBitmap'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value, &self->avl_layout->mChannelBitmap);
}


static PyGetSetDef avl_getset[] = {
    {
        .name = "mChannelLayoutTag",
        .get = avl_get_mChannelLayoutTag,
        .set = avl_set_mChannelLayoutTag,
        .doc = NULL,
        .closure = NULL
    },
    {
        .name = "mChannelBitmap",
        .get = avl_get_mChannelBitmap,
        .set = avl_set_mChannelBitmap,
        .doc = NULL,
        .closure = NULL
    },


    { .name = NULL } /* Sentinel */
};

static Py_ssize_t
avl_length(PyObject* self)
{
    return ((struct audio_channel_layout*)self)->avl_layout->mNumberChannelDescriptions;
}

static PyObject*
avl_get_item(PyObject* _self, Py_ssize_t idx)
{
    struct audio_channel_layout* self = ((struct audio_channel_layout*)_self);
    PyObject* result;

    if (idx >= (Py_ssize_t)self->avl_layout->mNumberChannelDescriptions) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    if (idx < 0) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }

    if (self->avl_items != NULL) {
        if (PyTuple_GET_ITEM(self->avl_items, idx) != Py_None) {
            Py_INCREF(PyTuple_GET_ITEM(self->avl_items, idx));
            return PyTuple_GET_ITEM(self->avl_items, idx);
        }
    } else {
        Py_ssize_t i;
        self->avl_items = PyTuple_New(self->avl_layout->mNumberChannelDescriptions);
        if (self->avl_items == NULL) {
            return NULL;
        }
        for (i = 0; i < (Py_ssize_t)self->avl_layout->mNumberChannelDescriptions; i++) {
            PyTuple_SET_ITEM(self->avl_items, i, Py_None);
            Py_INCREF(Py_None);
        }
    }

    result = acd_create(self->avl_layout->mChannelDescriptions + idx);
    if (result == NULL) {
        return NULL;
    }

    Py_DECREF(PyTuple_GET_ITEM(self->avl_items, idx));
    PyTuple_SET_ITEM(self->avl_items, idx, result);
    Py_INCREF(result);
    return result;
}

static PySequenceMethods avl_as_sequence = {
    .sq_length = avl_length,
    .sq_item = avl_get_item,
};


static PyObject*
avl_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "num_channels", NULL };
    struct audio_channel_layout* result;
    unsigned int num_channels;
    unsigned int i;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "I", keywords, &num_channels)) {
        return NULL;
    }

    result = PyObject_New(struct audio_channel_layout, &audio_channel_layout_type);
    if (result == NULL) {
        return NULL;
    }

    result->avl_ownsstorage = 1;
    result->avl_items = NULL;
    result->avl_layout = PyMem_Malloc(sizeof(AudioChannelLayout) + (num_channels * sizeof(AudioChannelDescription)));
    if (result->avl_layout == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    result->avl_layout->mChannelLayoutTag = 0;
    result->avl_layout->mChannelBitmap = 0;
    result->avl_layout->mNumberChannelDescriptions = num_channels;

    for (i = 0; i < num_channels; i++) {
        result->avl_layout->mChannelDescriptions[i].mChannelLabel = 0;
        result->avl_layout->mChannelDescriptions[i].mChannelFlags = 0;
        result->avl_layout->mChannelDescriptions[i].mCoordinates[0] = 0.0;
        result->avl_layout->mChannelDescriptions[i].mCoordinates[1] = 0.0;
        result->avl_layout->mChannelDescriptions[i].mCoordinates[2] = 0.0;
    }

    return (PyObject*)result;
}

static void
avl_dealloc(PyObject* object)
{
    struct audio_channel_layout* self = (struct audio_channel_layout*)object;

    if (self->avl_items) {
        Py_DECREF(self->avl_items);
    }

    if (self->avl_ownsstorage) {
        PyMem_Free(self->avl_layout);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(avl_doc,
    "AudioChannelLayout(num_channels)\n"
    CLINIC_SEP
    "Return an audiobuffer list.");

static PyTypeObject audio_channel_layout_type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "CoreAudio.AudioChannelLayout",
    .tp_basicsize   = sizeof(struct audio_channel_layout),
    .tp_itemsize    = 0,
    .tp_dealloc     = avl_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = avl_doc,
    .tp_members     = avl_members,
    .tp_getset      = avl_getset,
    .tp_new         = avl_new,
    .tp_as_sequence = &avl_as_sequence,
};

static PyObject* pythonify_audio_channel_layout(void* pointer)
{
    AudioChannelLayout* buf_pointer = (AudioChannelLayout*)pointer;
    struct audio_channel_layout* result;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    result = PyObject_New(struct audio_channel_layout, &audio_channel_layout_type);
    if (result == NULL) {
        return NULL;
    }

    result->avl_ownsstorage = 0;
    result->avl_items = NULL;
    result->avl_layout = buf_pointer;

    return (PyObject*)result;
}

static int depythonify_audio_channel_layout(PyObject* value, void* pointer)
{
    if (value == Py_None) {
       *(AudioChannelLayout**)pointer = NULL;
       return 0;
    }

    if (!audio_channel_layout_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioChannelLayout', got '%.100s'",
            Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioChannelLayout**)pointer = ((struct audio_channel_layout*)value)->avl_layout;
    return 0;
}

static int
init_audio_channel_layout(PyObject* module)
{
    int r;

    if (PyType_Ready(&audio_channel_layout_type) == -1) return -1;

    r = PyDict_SetItemString(audio_channel_layout_type.tp_dict, "__typestr__",
            PyBytes_FromString(@encode(AudioChannelLayout)));
    if (r == -1) return -1;

    Py_INCREF(&audio_channel_layout_type);
    r = PyModule_AddObject(module, "AudioChannelLayout", (PyObject*)&audio_channel_layout_type);
    if (r == -1) {
        Py_DECREF(&audio_channel_layout_type);
        return -1;
    }

    r = PyObjCPointerWrapper_Register(
        "AudioChannelLayout*",
        @encode(AudioChannelLayout*),
        pythonify_audio_channel_layout,
        depythonify_audio_channel_layout);

    return r;
}
