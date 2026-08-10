/*
 * Manual wrappers for a number of AVAudioBuffer methods
 */

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable call_AVAudioPCMBuffer_floatChannelData(
    PyObject* method, PyObject* self,
    PyObject* _Nonnull const* _Nonnull arguments __attribute__((__unused__)),
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
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(float), res[i]);
        if (t == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, t);
    }

    return result;
}

static PyObject* _Nullable call_AVAudioPCMBuffer_int16ChannelData(
    PyObject* method, PyObject* self,
    PyObject* _Nonnull const* _Nonnull arguments __attribute__((__unused__)),
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
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(int16_t), res[i]);
        if (t == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, t);
    }

    return result;
}

static PyObject* _Nullable call_AVAudioPCMBuffer_int32ChannelData(
    PyObject* method, PyObject* self,
    PyObject* _Nonnull const* _Nonnull arguments __attribute__((__unused__)),
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
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (res == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    format        = [(AVAudioPCMBuffer*)PyObjCObject_GetObject(self) format];
    channel_count = [format channelCount];

    result = PyTuple_New(channel_count);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    for (i = 0; i < channel_count; i++) {
        PyObject* t = PyObjCVarList_New(@encode(int32_t), res[i]);
        if (t == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, t);
    }

    return result;
}

static int
init_avaudiobuffer(void)
{
    Class cls = objc_lookUpClass("AVAudioPCMBuffer");
    if (!cls) { // LCOV_BR_EXCL_LINE
        /* macOS 10.9 or earlier */
        return 0; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping( // LCOV_ BR_EXCL_LINE
            cls, @selector(floatChannelData), call_AVAudioPCMBuffer_floatChannelData,
            PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
            cls, @selector(int16ChannelData), call_AVAudioPCMBuffer_int16ChannelData,
            PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping( // LCOV_BR_EXCL_LINE
            cls, @selector(int32ChannelData), call_AVAudioPCMBuffer_int32ChannelData,
            PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
