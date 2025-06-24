/*
 * Manual wrappers for a number of AVAudioBuffer methods
 */

static PyObject*
call_AVAudioPCMBuffer_floatChannelData(PyObject* method, PyObject* self,
                                       PyObject* const* arguments
                                       __attribute__((__unused__)),
                                       size_t nargs)
{
    float**           res;
    AVAudioFormat*    format;
    Py_ssize_t        i, channel_count;
    PyObject*         result;
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                res = ((float** (*)(id, SEL))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                res = ((float** (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(float), res[i]);
        if (t == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SetItem(result, i, t);
    }

    return result;
}

static PyObject*
call_AVAudioPCMBuffer_int16ChannelData(PyObject* method, PyObject* self,
                                       PyObject* const* arguments
                                       __attribute__((__unused__)),
                                       size_t nargs)
{
    int16_t**         res;
    AVAudioFormat*    format;
    Py_ssize_t        i, channel_count;
    PyObject*         result;
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                res = ((int16_t** (*)(id, SEL))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                res = ((int16_t** (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(int16_t), res[i]);
        if (t == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SetItem(result, i, t);
    }

    return result;
}

static PyObject*
call_AVAudioPCMBuffer_int32ChannelData(PyObject* method, PyObject* self,
                                       PyObject* const* arguments
                                       __attribute__((__unused__)),
                                       size_t nargs)
{
    int32_t**         res;
    AVAudioFormat*    format;
    Py_ssize_t        i, channel_count;
    PyObject*         result;
    struct objc_super super;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (PyObjCIMP_Check(method)) {
                res = ((int32_t** (*)(id, SEL))PyObjCIMP_GetIMP(method))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));
            } else {
                super.super_class = PyObjCSelector_GetClass(method);
                super.receiver    = PyObjCObject_GetObject(self);

                res = ((int32_t** (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(int32_t), res[i]);
        if (t == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SetItem(result, i, t);
    }

    return result;
}

static int
init_avaudiobuffer(void)
{
    Class cls = objc_lookUpClass("AVAudioPCMBuffer");
    if (!cls) {
        return 0;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(floatChannelData),
                                     call_AVAudioPCMBuffer_floatChannelData,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(int16ChannelData),
                                     call_AVAudioPCMBuffer_int16ChannelData,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    if (PyObjC_RegisterMethodMapping(cls, @selector(int32ChannelData),
                                     call_AVAudioPCMBuffer_int32ChannelData,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    return 0;
}
