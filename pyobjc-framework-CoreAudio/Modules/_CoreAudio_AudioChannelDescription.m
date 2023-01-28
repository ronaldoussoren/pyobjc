/*
 * AudioChannelDescription bindings
 *
 * These are basic bindings to the AudioChannelDescription type,
 * basically a buffer with extra attributes.
 */

static PyObject* audio_channel_description_type;

#define audio_channel_description_check(obj)                                             \
    PyObject_TypeCheck(obj, (PyTypeObject*)audio_channel_description_type)

struct audio_channel_description {
    PyObject_HEAD

    char                     acd_owns_storage;
    AudioChannelDescription* acd_description;
};

static PyMemberDef acd_members[] = {
    {.name   = "_owns_storage",
     .type   = T_BOOL,
     .offset = offsetof(struct audio_channel_description, acd_owns_storage),
     .flags  = READONLY,
     .doc    = "True iff this buffer owns storage for the AudioBufer"},

    {.name = NULL} /* Sentinel */
};

static PyObject*
acd_get_mChannelLabel(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("I", self->acd_description->mChannelLabel);
}

static int
acd_set_mChannelLabel(PyObject* _self, PyObject* value,
                      void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelLabel'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value,
                               &self->acd_description->mChannelLabel);
}

static PyObject*
acd_get_mChannelFlags(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("I", self->acd_description->mChannelFlags);
}

static int
acd_set_mChannelFlags(PyObject* _self, PyObject* value,
                      void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mChannelFlags'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value,
                               &self->acd_description->mChannelFlags);
}

static PyObject*
acd_get_mCoordinates(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    return Py_BuildValue("fff", self->acd_description->mCoordinates[0],
                         self->acd_description->mCoordinates[1],
                         self->acd_description->mCoordinates[2]);
}

static int
acd_set_mCoordinates(PyObject* _self, PyObject* value,
                     void* closure __attribute__((__unused__)))
{
    struct audio_channel_description* self = (struct audio_channel_description*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mCoordinates'");
        return -1;
    }

    return PyArg_ParseTuple(value, "fff:mCoordinates",
                            self->acd_description->mChannelFlags + 0,
                            self->acd_description->mChannelFlags + 1,
                            self->acd_description->mChannelFlags + 2);
}

static PyGetSetDef acd_getset[] = {
    {.name    = "mChannelLabel",
     .get     = acd_get_mChannelLabel,
     .set     = acd_set_mChannelLabel,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mChannelFlags",
     .get     = acd_get_mChannelFlags,
     .set     = acd_set_mChannelFlags,
     .doc     = NULL,
     .closure = NULL},
    {.name    = "mCoordinates",
     .get     = acd_get_mCoordinates,
     .set     = acd_set_mCoordinates,
     .doc     = NULL,
     .closure = NULL},

    {.name = NULL} /* Sentinel */
};

static PyObject*
acd_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"mChannelLabel", "mChannelFlags", "mCoordinates", NULL};
    struct audio_channel_description* result;
    unsigned int                      channel_label  = 0;
    unsigned int                      channel_flags  = 0;
    float                             coordinates[3] = {0, 0, 0};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|$II(fff)", keywords, &channel_label,
                                     &channel_flags, coordinates, coordinates + 1,
                                     coordinates + 2)) {
        return NULL;
    }

    result = PyObject_New(struct audio_channel_description,
                          (PyTypeObject*)audio_channel_description_type);
    if (result == NULL) {
        return NULL;
    }

    result->acd_owns_storage = 1;
    result->acd_description  = PyMem_Malloc(sizeof(AudioChannelDescription));
    if (result == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->acd_description->mChannelLabel   = channel_label;
    result->acd_description->mChannelFlags   = channel_flags;
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
             "AudioChannelDescription(*, num_channels=1, buffer_size=-1)\n" CLINIC_SEP
             "Return an audiobuffer. If a buffer size is specified "
             "this will allocate a buffer, otherwise no buffer is "
             "allocated\n");

static PyType_Slot acd_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&acd_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&acd_doc},
    {.slot = Py_tp_getset, .pfunc = (void*)&acd_getset},
    {.slot = Py_tp_members, .pfunc = (void*)&acd_members},
    {.slot = Py_tp_new, .pfunc = (void*)&acd_new},

    {0, NULL} /* sentinel */
};

static PyType_Spec acd_spec = {
    .name      = "CoreAudio.AudioChannelDescription",
    .basicsize = sizeof(struct audio_channel_description),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
    .slots     = acd_slots,
};

static PyObject*
acd_create(AudioChannelDescription* item)
{
    struct audio_channel_description* result;

    result = PyObject_New(struct audio_channel_description,
                          (PyTypeObject*)audio_channel_description_type);
    if (result == NULL) {
        return NULL;
    }

    result->acd_owns_storage = 0;
    result->acd_description  = item;

    return (PyObject*)result;
}

static PyObject*
pythonify_audio_channel_description(void* pointer)
{
    AudioChannelDescription* buf_pointer = (AudioChannelDescription*)pointer;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return acd_create(*(AudioChannelDescription**)pointer);
}

static int
depythonify_audio_channel_description(PyObject* value, void* pointer)
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

    *(AudioChannelDescription**)pointer =
        ((struct audio_channel_description*)value)->acd_description;
    return 0;
}

static int
init_audio_channel_description(PyObject* module)
{
    int r;

    PyObject* tmp = PyType_FromSpec(&acd_spec);
    if (tmp == NULL) {
        return -1;
    }
    audio_channel_description_type = tmp;

    PyObject* ts = PyBytes_FromString(@encode(AudioChannelDescription));
    if (ts == NULL) {
        Py_CLEAR(audio_channel_description_type);
        return -1;
    }

    r = PyObject_SetAttrString(audio_channel_description_type, "__typestr__", ts);
    Py_DECREF(ts);
    if (r == -1) {
        Py_CLEAR(audio_channel_description_type);
        return -1;
    }

    r = PyModule_AddObject(module, "AudioChannelDescription",
                           audio_channel_description_type);
    if (r == -1) {
        Py_CLEAR(audio_channel_description_type);
        return -1;
    }
    Py_INCREF(audio_channel_description_type);

    r = PyObjCPointerWrapper_Register(
        "AudioChannelDescription*", @encode(AudioChannelDescription*),
        pythonify_audio_channel_description, depythonify_audio_channel_description);

    return r;
}
