/*
 * AudioChannelDescription bindings
 *
 * These are basic bindings to the AudioChannelDescription type,
 * basically a buffer with extra attributes.
 */

static PyTypeObject audio_channel_description_type; /* Forward definition */

#define audio_channel_description_check(obj) PyObject_TypeCheck(obj, &audio_channel_description_type)

struct audio_channel_description {
    PyObject_HEAD

    char         acd_owns_storage;
    AudioChannelDescription* acd_description;
};

static PyMemberDef acd_members[] = {
    {
        .name = "_owns_storage",
        .type = T_BOOL,
        .offset = offsetof(struct audio_channel_description, acd_owns_storage),
        .flags = READONLY,
        .doc = "True iff this buffer owns storage for the AudioBufer"
    },

    { .name = NULL } /* Sentinel */
};

static PyObject*
acd_get_mChannelLabel(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("I", self->acd_description->mChannelLabel);
}

static int
acd_set_mChannelLabel(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelLabel'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value, &self->acd_description->mChannelLabel);
}

static PyObject*
acd_get_mChannelFlags(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("I", self->acd_description->mChannelFlags);
}

static int
acd_set_mChannelFlags(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelFlags'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value, &self->acd_description->mChannelFlags);
}

static PyObject*
acd_get_mCoordinates(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("fff", self->acd_description->mCoordinates[0], self->acd_description->mCoordinates[1], self->acd_description->mCoordinates[2]);
}

static int
acd_set_mCoordinates(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mCoordinates'");
        return -1;
    }

    return PyArg_ParseTuple(value, "fff:mCoordinates", self->acd_description->mChannelFlags + 0, self->acd_description->mChannelFlags + 1, self->acd_description->mChannelFlags + 2);
}


static PyGetSetDef acd_getset[] = {
    {
        .name = "mChannelLabel",
        .get = acd_get_mChannelLabel,
        .set = acd_set_mChannelLabel,
        .doc = NULL,
        .closure = NULL
    },
    {
        .name = "mChannelFlags",
        .get = acd_get_mChannelFlags,
        .set = acd_set_mChannelFlags,
        .doc = NULL,
        .closure = NULL
    },
    {
        .name = "mCoordinates",
        .get = acd_get_mCoordinates,
        .set = acd_set_mCoordinates,
        .doc = NULL,
        .closure = NULL
    },

    { .name = NULL } /* Sentinel */
};


static PyObject*
acd_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "mChannelLabel", "mChannelFlags", "mCoordinates", NULL };
    struct audio_channel_description* result;
    unsigned int channel_label = 0;
    unsigned int channel_flags = 0;
    float coordinates[3] = { 0, 0, 0 };

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "|"
#if PY_MAJOR_VERSION == 3
                "$"
#endif
                "II(fff)", keywords, &channel_label, &channel_flags, coordinates, coordinates + 1, coordinates + 2)) {
        return NULL;
    }

    result = PyObject_New(struct audio_channel_description, &audio_channel_description_type);
    if (result == NULL) {
        return NULL;
    }

    result->acd_owns_storage = 1;
    result->acd_description = PyMem_Malloc(sizeof(AudioChannelDescription));
    if (result == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->acd_description->mChannelLabel = channel_label;
    result->acd_description->mChannelFlags = channel_flags;
    result->acd_description->mCoordinates[0] = coordinates[0];
    result->acd_description->mCoordinates[1] = coordinates[1];
    result->acd_description->mCoordinates[2] = coordinates[2];

    return (PyObject*)result;
}

static void
acd_dealloc(PyObject* object)
{
    struct audio_channel_description* self = (struct audio_channel_description*)object;

    if (self->acd_owns_storage) {
        PyMem_Free(self->acd_description);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(acd_doc,
    "AudioChannelDescription(*, num_channels=1, buffer_size=-1)\n"
    CLINIC_SEP
    "Return an audiobuffer. If a buffer size is specified "
    "this will allocate a buffer, otherwise no buffer is "
    "allocated\n");

static PyTypeObject audio_channel_description_type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "CoreAudio.AudioChannelDescription",
    .tp_basicsize   = sizeof(struct audio_channel_description),
    .tp_itemsize    = 0,
    .tp_dealloc     = acd_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = acd_doc,
    .tp_getset      = acd_getset,
    .tp_members     = acd_members,
    .tp_new         = acd_new,
};

static PyObject*
acd_create(AudioChannelDescription* item)
{
    struct audio_channel_description* result;

    result = PyObject_New(struct audio_channel_description, &audio_channel_description_type);
    if (result == NULL) {
        return NULL;
    }

    result->acd_owns_storage = 0;
    result->acd_description = item;

    return (PyObject*)result;
}

static PyObject* pythonify_audio_channel_description(void* pointer)
{
    AudioChannelDescription* buf_pointer = (AudioChannelDescription*)pointer;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return acd_create(*(AudioChannelDescription**)pointer);
}

static int depythonify_audio_channel_description(PyObject* value, void* pointer)
{
    if (value == Py_None) {
        *(AudioChannelDescription**)pointer = NULL;
        return 0;
    }

    if (!audio_channel_description_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioChannelDescription', got '%.100s'",
            Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioChannelDescription**)pointer = ((struct audio_channel_description*)value)->acd_description;
    return 0;
}

static int
init_audio_channel_description(PyObject* module)
{
    int r;

    if (PyType_Ready(&audio_channel_description_type) == -1) return -1;

    r = PyDict_SetItemString(audio_channel_description_type.tp_dict, "__typestr__",
            PyBytes_FromString(@encode(AudioChannelDescription)));
    if (r == -1) return -1;

    Py_INCREF(&audio_channel_description_type);
    r = PyModule_AddObject(module, "AudioChannelDescription", (PyObject*)&audio_channel_description_type);
    if (r == -1) {
        Py_DECREF(&audio_channel_description_type);
        return -1;
    }

    r = PyObjCPointerWrapper_Register(
        "AudioChannelDescription*",
        @encode(AudioChannelDescription*),
        pythonify_audio_channel_description,
        depythonify_audio_channel_description);

    return r;
}
