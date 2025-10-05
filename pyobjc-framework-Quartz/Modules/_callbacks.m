/*
 * Wrappers for callback functions.
 *
 * XXX: Definitely need tests for these.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>
#import <CoreGraphics/CoreGraphics.h>

/*
 *
 * CGDataConsumerCreate
 *
 */

static size_t
m_CGDataConsumerPutBytesCallback(void* _info, const void* buffer, size_t count)
{
    size_t    retval;
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 0), "Oy#l", PyTuple_GetItem(info, 2),
                              buffer, (Py_ssize_t)count, (Py_ssize_t)count);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(size_t), result, &retval) < 0) {
        Py_DECREF(result);
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
    return retval;
}

static void
m_CGDataConsumerReleaseInfoCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 1) != Py_None) {
        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 1), "O",
                                                 PyTuple_GetItem(info, 2));
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }

    Py_DECREF(info);

    PyGILState_Release(state);
}

static CGDataConsumerCallbacks m_CGDataConsumerCallbacks = {
    m_CGDataConsumerPutBytesCallback,   /* putBytes */
    m_CGDataConsumerReleaseInfoCallback /* releaseConsumer */
};

PyDoc_STRVAR(doc_CGDataConsumerCreate,
             "CGDataConsumerCreate(info, (putBytes, release)) -> object\n"
             "\n"
             "putBytes and release are callback functions. Release may be None");
static PyObject*
m_CGDataConsumerCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* info;
    PyObject* putBytes;
    PyObject* release;

    if (!PyArg_ParseTuple(args, "O(OO)", &info, &putBytes, &release)) {
        return NULL;
    }

    if (!PyCallable_Check(putBytes)) {
        PyErr_SetString(PyExc_TypeError, "putBytes is not callable");
        return NULL;
    }
    if (release != Py_None && !PyCallable_Check(release)) {
        PyErr_SetString(PyExc_TypeError, "release is not callable");
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OOO", putBytes, release, info);
    if (real_info == NULL) {
        return NULL;
    }

    CGDataConsumerRef result;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGDataConsumerCreate(real_info, &m_CGDataConsumerCallbacks);

        } @catch (NSException* localException) {
            result = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (result == NULL && PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (result == NULL) {
        Py_DECREF(real_info);
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CGDataConsumerRef), &result);
    /* CGDataConsumerCreate donated a reference, we therefore now have
     * one too many, release a reference.
     */
    CGDataConsumerRelease(result);
    return retval;
}

/*
 *
 * CGDataProviderCreate*
 *
 */

static size_t
m_CGDataProviderGetBytesCallback(void* _info, void* buffer, size_t count)
{
    PyObject* info = (PyObject*)_info;
    PyObject* buf;

    PyGILState_STATE state = PyGILState_Ensure();

    Py_buffer view;
    if (PyBuffer_FillInfo(&view, NULL, buffer, count, 0, PyBUF_WRITABLE) < 0) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    buf = PyMemoryView_FromBuffer(&view);
    if (buf == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 1), "OOl",
                                             PyTuple_GetItem(info, 0), buf, count);
    if (result == NULL) {
        Py_DECREF(result);
        Py_DECREF(buf);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (!PyTuple_Check(result) || PyTuple_GET_SIZE(result) != 2) {
        PyErr_Format(PyExc_TypeError, "Expecting result of type tuple of 2, got %s",
                     result->ob_type->tp_name);
        Py_DECREF(result);
        Py_DECREF(buf);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    size_t c_result;
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GetItem(result, 0), &c_result) < 0) {
        Py_DECREF(result);
        Py_DECREF(buf);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyTuple_GetItem(result, 1) != buf) {
        Py_buffer view;

        if (PyObject_GetBuffer(PyTuple_GetItem(result, 1), &view, PyBUF_CONTIG_RO)
            == -1) {
            Py_DECREF(result);
            Py_DECREF(buf);
            PyObjCErr_ToObjCWithGILState(&state);
        }

        if ((size_t)view.len < c_result || (size_t)view.len > count) {
            PyErr_SetString(PyExc_ValueError, "Inconsistent size");
            PyBuffer_Release(&view);
            Py_DECREF(result);
            Py_DECREF(buf);
            PyObjCErr_ToObjCWithGILState(&state);
        }
        memcpy(buffer, view.buf, c_result);
        PyBuffer_Release(&view);
    } else {
        /* Assume that the user knows what he's doing and has
         * filled the right bit of the buffer.
         */
    }

    Py_DECREF(buf);
    Py_DECREF(result);

    PyGILState_Release(state);
    return c_result;
}

static void
m_CGDataProviderRewindCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 3) != Py_None) {
        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 3), "O",
                                                 PyTuple_GetItem(info, 0));
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }

    PyGILState_Release(state);
}

static void
m_CGDataProviderReleaseInfoCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 4) != Py_None) {
        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 4), "O",
                                                 PyTuple_GetItem(info, 0));
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }

    /* Cleanup up the callback info */
    Py_DECREF(info);

    PyGILState_Release(state);
}

static off_t
m_CGDataProviderSkipForwardCallback(void* _info, off_t count)
{
    PyObject* info = (PyObject*)_info;
    off_t     retval;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 2), "Ol",
                                             PyTuple_GetItem(info, 0), count);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(off_t), result, &retval) < 0) {
        Py_DECREF(result);
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);

    return retval;
}

static CGDataProviderSequentialCallbacks m_CGDataProviderSequentialCallbacks = {
    0,                                   /* version */
    m_CGDataProviderGetBytesCallback,    /* getBytes */
    m_CGDataProviderSkipForwardCallback, /* skipForward */
    m_CGDataProviderRewindCallback,      /* rewind */
    m_CGDataProviderReleaseInfoCallback  /* releaseInfo */

};

PyDoc_STRVAR(doc_CGDataProviderCreateSequential,
             "CGDataConsumerCreateSequential(info, (getBytes, skipForward, rewind, "
             "releaseProvider)) -> object\n"
             "\n"
             "getBytes, skipForward, rewind and release are callback functions. Release "
             "may be None");
static PyObject*
m_CGDataProviderCreateSequential(PyObject* self __attribute__((__unused__)),
                                 PyObject* args)
{
    PyObject* info;
    PyObject* getBytes;
    PyObject* skipForward;
    PyObject* rewind;
    PyObject* release;

    if (!PyArg_ParseTuple(args, "O(OOOO)", &info, &getBytes, &skipForward, &rewind,
                          &release)) {
        return NULL;
    }

    if (!PyCallable_Check(getBytes)) {
        PyErr_SetString(PyExc_TypeError, "getBytes is not callable");
        return NULL;
    }
    if (!PyCallable_Check(skipForward)) {
        PyErr_SetString(PyExc_TypeError, "skipForward is not callable");
        return NULL;
    }
    if (!PyCallable_Check(rewind)) {
        PyErr_SetString(PyExc_TypeError, "rewind is not callable");
        return NULL;
    }
    if (release != Py_None && !PyCallable_Check(release)) {
        PyErr_SetString(PyExc_TypeError, "release is not callable");
        return NULL;
    }

    PyObject* real_info =
        Py_BuildValue("OOOOO", info, getBytes, skipForward, rewind, release);
    if (real_info == NULL) {
        return NULL;
    }

    CGDataProviderRef result;
    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGDataProviderCreateSequential(real_info,
                                                    &m_CGDataProviderSequentialCallbacks);

        } @catch (NSException* localException) {
            result = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (result == NULL && PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (result == NULL) {
        Py_DECREF(real_info);
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CGDataProviderRef), &result);
    /* CGDataProviderCreate donated a reference, we therefore now have
     * one too many, release a reference.
     */
    CGDataProviderRelease(result);
    return retval;
}

/*
 * CGDataProviderCreateWithData
 */

static void
m_releaseData(void* _info, const void* data, size_t size)
{
    PyObject* info = (PyObject*)_info;
    PyObject* view;
    int       tag;

    PyGILState_STATE state = PyGILState_Ensure();

    tag  = PyLong_AsLong(PyTuple_GetItem(info, 2));
    view = PyTuple_GetItem(info, 3);

    if (PyTuple_GetItem(info, 1) != Py_None) {
        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 1), "O",
                                                 PyTuple_GetItem(info, 0));
        if (result == NULL) {
            PyObjC_FreeCArray(tag, PyObjCMemView_GetBuffer(view));
            Py_DECREF(info);
            PyObjCErr_ToObjCWithGILState(&state);
            return;
        }
        Py_DECREF(result);
    }

    PyObjC_FreeCArray(tag, PyObjCMemView_GetBuffer(view));
    Py_DECREF(info);

    PyGILState_Release(state);
}

PyDoc_STRVAR(doc_CGDataProviderCreateWithData,
             "CGDataProviderCreateWithData(info, data, size, release) -> object");
static PyObject*
m_CGDataProviderCreateWithData(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* info;
    PyObject* data;
    long      size;
    PyObject* release;

    if (!PyArg_ParseTuple(args, "OOlO", &info, &data, &size, &release)) {
        return NULL;
    }
    if (release != Py_None && !PyCallable_Check(release)) {
        PyErr_SetString(PyExc_TypeError, "release not callable");
        return NULL;
    }

    int        tag;
    PyObject*  bufobj = NULL;
    PyObject*  view;
    Py_ssize_t sz = (Py_ssize_t)size;
    void*      arr;

    view = PyObjCMemView_New();
    if (view == NULL) {
        return NULL;
    }

    tag = PyObjC_PythonToCArray(NO, YES, @encode(char), data, &arr, &sz, &bufobj,
                                PyObjCMemView_GetBuffer(view));
    if (tag < 0) {
        return NULL;
    }

    PyObject* real_info;
    if (bufobj != NULL) {
        real_info = Py_BuildValue("OOlOO", info, release, (long)tag, view, bufobj);
    } else {
        real_info = Py_BuildValue("OOlO", info, release, (long)tag, view);
    }

    CGDataProviderRef result;

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGDataProviderCreateWithData(real_info, arr, size, m_releaseData);

        } @catch (NSException* localException) {
            result = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        PyObjC_FreeCArray(tag, PyObjCMemView_GetBuffer(view));
        Py_DECREF(info);
        return NULL;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CGDataProviderRef), &result);
    CFRelease(result);
    return retval;
}

/*
 * CGFunctionCreate
 */

static void
m_CGFunctionEvaluateCallback(void* _info, const CGFloat* inData, CGFloat* outData)
{
    PyObject* info = (PyObject*)_info;
    long      domdim;
    long      rangedim;

    PyGILState_STATE state = PyGILState_Ensure();

    domdim   = PyLong_AsLong(PyTuple_GetItem(info, 2));
    rangedim = PyLong_AsLong(PyTuple_GetItem(info, 3));

    PyObject* input;
    if (inData) {
        input = PyObjC_CArrayToPython(@encode(CGFloat), (void*)inData, domdim);
    } else {
        input = Py_None;
        Py_INCREF(Py_None);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 1), "OOO",
                                             PyTuple_GetItem(info, 0), input, Py_None);
    Py_DECREF(input);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_DepythonifyCArray(@encode(CGFloat), rangedim, NO, result, (void*)outData,
                                 NO, NO)
        < 0) {
        Py_DECREF(result);
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGFunctionReleaseInfoCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    Py_DECREF(info);

    PyGILState_Release(state);
}

static CGFunctionCallbacks m_CGFunctionCallbacks = {
    0,                              /* version */
    m_CGFunctionEvaluateCallback,   /* evaluate */
    m_CGFunctionReleaseInfoCallback /* releaseInfo */
};

PyDoc_STRVAR(doc_CGFunctionCreate, "CGFunctionCreate(info, domainDimension, domain, "
                                   "rangeDimension, range, evaluate) -> functionref");
static PyObject*
m_CGFunctionCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*     info;
    PyObject*     domDim;
    PyObject*     domain;
    PyObject*     rangeDim;
    PyObject*     range;
    PyObject*     evaluate;
    size_t        domainDimension;
    size_t        rangeDimension;
    CGFloat*      domainArr;
    CGFloat*      rangeArr;
    CGFunctionRef result    = NULL;
    PyObject*     domainBuf = NULL;
    Py_buffer     domainView;
    PyObject*     rangeBuf = NULL;
    Py_buffer     rangeView;
    int           rangeTag;
    int           domainTag;

    if (!PyArg_ParseTuple(args, "OOOOOO", &info, &domDim, &domain, &rangeDim, &range,
                          &evaluate)) {

        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), domDim, &domainDimension) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), rangeDim, &rangeDimension) < 0) {
        return NULL;
    }
    if (domain == Py_None) {
        domainArr = NULL;
        domainTag = -1;

    } else {
        /* Parse Array */
        Py_ssize_t cnt = domainDimension * 2;
        domainTag =
            PyObjC_PythonToCArray(NO, NO, @encode(CGFloat), domain, (void**)&domainArr,
                                  &cnt, &domainBuf, &domainView);
        if (domainTag < 0) {
            return NULL;
        }
    }

    if (range == Py_None) {
        rangeArr = NULL;
        rangeTag = -1;

    } else {
        Py_ssize_t cnt = rangeDimension * 2;

        /* Parse Array */
        rangeTag = PyObjC_PythonToCArray(NO, NO, @encode(CGFloat), range,
                                         (void**)&rangeArr, &cnt, &rangeBuf, &rangeView);
        if (rangeTag < 0) {
            if (domainTag != -1) {
                PyObjC_FreeCArray(domainTag, &domainView);
                Py_XDECREF(domainBuf);
            }
            return NULL;
        }
    }

    if (!PyCallable_Check(evaluate)) {
        PyErr_Format(PyExc_TypeError, "evaluate not callable, but of type %.80s",
                     Py_TYPE(evaluate)->tp_name);
        if (domainTag != -1) {
            PyObjC_FreeCArray(domainTag, &domainView);
            Py_XDECREF(domainBuf);
        }
        if (rangeTag != -1) {
            PyObjC_FreeCArray(rangeTag, &rangeView);
            Py_XDECREF(rangeBuf);
        }
        return NULL;
    }

    PyObject* real_info;

    real_info = Py_BuildValue("OOll", info, evaluate, domainDimension, rangeDimension);
    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGFunctionCreate(real_info, domainDimension, domainArr,
                                      rangeDimension, rangeArr, &m_CGFunctionCallbacks);

        } @catch (NSException* localException) {
            result = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    /* cleanup domainArr, rangeArr */
    if (domainTag != -1) {
        Py_XDECREF(domainBuf);
        PyObjC_FreeCArray(domainTag, &domainView);
    }
    if (rangeTag != -1) {
        Py_XDECREF(rangeBuf);
        PyObjC_FreeCArray(rangeTag, &rangeView);
    }

    if (result == NULL) {
        Py_DECREF(real_info);
        if (PyErr_Occurred()) {
            return NULL;
        }
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* func = PyObjC_ObjCToPython(@encode(CGFunctionRef), &result);
    CGFunctionRelease(result); /* Adjust reference count */

    return func;
}

/*
 * - CGDisplayRegisterReconfigurationCallback
 * - CGDisplayRemoveReconfigurationCallback
 */

struct callback_struct {
    PyObject* callback;
    PyObject* user_info;
    PyObject* real_info;
};
struct callback_info {
    struct callback_struct* list;
    size_t                  count;
};

#if PY_VERSION_HEX >= 0x030d0000
/*
 * The ``display_reconfig_callback`` variable is shared global state
 * that needs to be protected by a lock in free-threaded mode.
 *
 * Note that the APIs protected by the lock are in general called on
 * the main thread only, we could get away without using a lock but
 * it is better to be safe than sorry.
 */
PyMutex callback_mutex = {0};
#endif
struct callback_info display_reconfig_callback = {NULL, 0};

static int
insert_callback_info(struct callback_info* info, PyObject* callback, PyObject* user_info,
                     PyObject* real_info)
{
    size_t i;

#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Lock(&callback_mutex);
#endif

    for (i = 0; i < info->count; i++) {
        if (info->list[i].callback == NULL) {
            info->list[i].callback  = callback;
            info->list[i].user_info = user_info;
            info->list[i].real_info = real_info;
            Py_INCREF(callback);
            Py_INCREF(user_info);
            Py_INCREF(real_info);

#if PY_VERSION_HEX >= 0x030d0000
            PyMutex_Unlock(&callback_mutex);
#endif

            return 0;
        }
    }

    /* No free space found, increase the list */
    if (info->list == NULL) {
        info->list = PyMem_Malloc(sizeof(*info->list));
        if (info->list == NULL) {
            PyErr_NoMemory();
#if PY_VERSION_HEX >= 0x030d0000
            PyMutex_Unlock(&callback_mutex);
#endif
            return -1;
        }
        info->list[0].callback  = callback;
        info->list[0].user_info = user_info;
        info->list[0].real_info = real_info;
        Py_INCREF(callback);
        Py_INCREF(user_info);
        Py_INCREF(real_info);
        info->count = 1;
    } else {
        struct callback_struct* tmp;

        tmp = PyMem_Realloc(info->list, sizeof(*info->list) * (info->count + 1));
        if (tmp == NULL) {
            PyErr_NoMemory();
#if PY_VERSION_HEX >= 0x030d0000
            PyMutex_Unlock(&callback_mutex);
#endif
            return -1;
        }
        info->list                        = tmp;
        info->list[info->count].callback  = callback;
        info->list[info->count].user_info = user_info;
        info->list[info->count].real_info = real_info;
        Py_INCREF(callback);
        Py_INCREF(user_info);
        Py_INCREF(real_info);
        info->count++;
    }
#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Unlock(&callback_mutex);
#endif
    return 0;
}

static PyObject*
find_callback_info(struct callback_info* info, PyObject* callback, PyObject* user_info)
{
    size_t i;

#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Lock(&callback_mutex);
#endif

    for (i = 0; i < info->count; i++) {
        if (info->list[i].callback == NULL)
            continue;

        if (!PyObject_RichCompareBool(info->list[i].callback, callback, Py_EQ)) {
            continue;
        }
        if (!PyObject_RichCompareBool(info->list[i].user_info, user_info, Py_EQ)) {
            continue;
        }

        Py_INCREF(info->list[i].real_info);
#if PY_VERSION_HEX >= 0x030d0000
        PyMutex_Unlock(&callback_mutex);
#endif
        return info->list[i].real_info;
    }
    PyErr_SetString(PyExc_ValueError, "Cannot find callback info");
#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Unlock(&callback_mutex);
#endif
    return NULL;
}

static void
remove_callback_info(struct callback_info* info, PyObject* callback, PyObject* user_info)
{
    size_t i;

#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Lock(&callback_mutex);
#endif

    for (i = 0; i < info->count; i++) {
        if (info->list[i].callback == NULL)
            continue;

        if (!PyObject_RichCompareBool(info->list[i].callback, callback, Py_EQ)) {
            continue;
        }
        if (!PyObject_RichCompareBool(info->list[i].user_info, user_info, Py_EQ)) {
            continue;
        }

        Py_DECREF(info->list[i].callback);
        Py_DECREF(info->list[i].user_info);
        info->list[i].callback  = NULL;
        info->list[i].user_info = NULL;
    }
#if PY_VERSION_HEX >= 0x030d0000
    PyMutex_Unlock(&callback_mutex);
#endif
}

static void
m_CGDisplayReconfigurationCallBack(CGDirectDisplayID           display,
                                   CGDisplayChangeSummaryFlags flags, void* _userInfo)
{
    PyObject* info = (PyObject*)_userInfo;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_display = PyObjC_ObjCToPython(@encode(CGDirectDisplayID), &display);
    if (py_display == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* py_flags =
        PyObjC_ObjCToPython(@encode(CGDisplayChangeSummaryFlags), &flags);
    if (py_flags == NULL) {
        Py_DECREF(py_display);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "OOO", py_display,
                                             py_flags, PyTuple_GetItem(info, 1));
    Py_DECREF(py_display);
    Py_DECREF(py_flags);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject*
m_CGDisplayRegisterReconfigurationCallback(PyObject* self __attribute__((__unused__)),
                                           PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;
    CGError   err;

    if (!PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, userinfo);

    err = -1;
    Py_BEGIN_ALLOW_THREADS
        @try {
            err = CGDisplayRegisterReconfigurationCallback(
                m_CGDisplayReconfigurationCallBack, real_info);

        } @catch (NSException* localException) {
            err = -1;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (insert_callback_info(&display_reconfig_callback, callback, userinfo, real_info)
        == -1) {
        CGDisplayRemoveReconfigurationCallback(m_CGDisplayReconfigurationCallBack,
                                               real_info);
        Py_DECREF(real_info);
        return NULL;
    }

    return PyObjC_ObjCToPython(@encode(CGError), &err);
}

static PyObject*
m_CGDisplayRemoveReconfigurationCallback(PyObject* self __attribute__((__unused__)),
                                         PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;

    if (!PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }

    PyObject* real_info =
        find_callback_info(&display_reconfig_callback, callback, userinfo);

    if (real_info == NULL) {
        return NULL;
    }

    CGError err = -1;
    Py_BEGIN_ALLOW_THREADS
        @try {
            err = CGDisplayRemoveReconfigurationCallback(
                m_CGDisplayReconfigurationCallBack, real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(real_info);

    if (PyErr_Occurred()) {
        return NULL;
    }

    remove_callback_info(&display_reconfig_callback, callback, userinfo);

    return PyObjC_ObjCToPython(@encode(CGError), &err);
}

/*
 * CGScreenUpdateMove
 */

struct callback_info screen_move_callback = {NULL, 0};

static void
m_CGScreenUpdateMoveCallback(CGScreenUpdateMoveDelta delta, size_t count,
                             const CGRect* rectArray, void* _userInfo)
{
    PyObject* info = (PyObject*)_userInfo;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_delta = PyObjC_ObjCToPython(@encode(CGScreenUpdateMoveDelta), &delta);
    if (py_delta == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyObject* py_rectarray =
        PyObjC_CArrayToPython(@encode(CGRect), (void*)rectArray, count);
    if (py_rectarray == NULL) {
        Py_DECREF(py_delta);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 0), "OlOO", py_delta, (long)count,
                              py_rectarray, PyTuple_GetItem(info, 1));
    Py_DECREF(py_delta);
    Py_DECREF(py_rectarray);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject*
m_CGScreenRegisterMoveCallback(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;

    if (PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, userinfo);

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGScreenRegisterMoveCallback(m_CGScreenUpdateMoveCallback, real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (insert_callback_info(&screen_move_callback, callback, userinfo, real_info) < 0) {
        CGScreenUnregisterMoveCallback(m_CGScreenUpdateMoveCallback, real_info);
        Py_DECREF(real_info);
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
m_CGScreenUnregisterMoveCallback(PyObject* self __attribute__((__unused__)),
                                 PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;

    if (!PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }

    PyObject* real_info = find_callback_info(&screen_move_callback, callback, userinfo);

    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGScreenUnregisterMoveCallback(m_CGScreenUpdateMoveCallback, real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(real_info);
    if (PyErr_Occurred()) {
        return NULL;
    }

    remove_callback_info(&screen_move_callback, callback, userinfo);

    Py_INCREF(Py_None);
    return Py_None;
}

/*
 * CGScreenRefresh
 */

struct callback_info screen_refresh_callback = {NULL, 0};

static void
m_CGScreenRefreshCallback(CGRectCount count, const CGRect* rectArray, void* _userInfo)
{
    PyObject* info = (PyObject*)_userInfo;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_rectarray =
        PyObjC_CArrayToPython(@encode(CGRect), (void*)rectArray, count);
    if (py_rectarray == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "lOO", (long)count,
                                             py_rectarray, PyTuple_GetItem(info, 1));
    Py_DECREF(py_rectarray);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject*
m_CGRegisterScreenRefreshCallback(PyObject* self __attribute__((__unused__)),
                                  PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;

    if (!PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, userinfo);

    CGError err = -1;
    Py_BEGIN_ALLOW_THREADS
        @try {
            err = CGRegisterScreenRefreshCallback(m_CGScreenRefreshCallback, real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (insert_callback_info(&screen_refresh_callback, callback, userinfo, real_info)
        < 0) {
        CGUnregisterScreenRefreshCallback(m_CGScreenRefreshCallback, real_info);
        Py_DECREF(real_info);
        return NULL;
    }

    return PyObjC_ObjCToPython(@encode(CGError), &err);
}

static PyObject*
m_CGUnregisterScreenRefreshCallback(PyObject* self __attribute__((__unused__)),
                                    PyObject* args)
{
    PyObject* callback;
    PyObject* userinfo;

    if (!PyArg_ParseTuple(args, "OO", &callback, &userinfo)) {
        return NULL;
    }

    PyObject* real_info =
        find_callback_info(&screen_refresh_callback, callback, userinfo);

    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGUnregisterScreenRefreshCallback(m_CGScreenRefreshCallback, real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(real_info);
    if (PyErr_Occurred()) {
        return NULL;
    }

    remove_callback_info(&screen_refresh_callback, callback, userinfo);

    Py_INCREF(Py_None);
    return Py_None;
}

/*
 * CGEventTapCreate
 * CGEventTapCreateForPSN
 *
 * Note that these wrappers leak some memory: the 'refcon' info passed to the
 * C code will never be deallocated. This is too bad, but can't be avoided with
 * the current CoreGraphics API.
 */

static CGEventRef
m_CGEventTapCallBack(CGEventTapProxy proxy, CGEventType type, CGEventRef event,
                     void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_proxy;
    PyObject* py_type;
    PyObject* py_event;

    py_proxy = PyObjC_ObjCToPython(@encode(CGEventTapProxy), &proxy);
    if (py_proxy == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    py_type = PyObjC_ObjCToPython(@encode(CGEventType), &type);
    if (py_type == NULL) {
        Py_DECREF(py_proxy);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    py_event = PyObjC_ObjCToPython(@encode(CGEventRef), &event);
    if (py_event == NULL) {
        Py_DECREF(py_proxy);
        Py_DECREF(py_type);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNNO", py_proxy,
                                             py_type, py_event, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(CGEventRef), result, &event) < 0) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyGILState_Release(state);

    return event;
}

static PyObject*
m_CGEventTapCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*           py_tap;
    PyObject*           py_place;
    PyObject*           py_options;
    PyObject*           py_eventsOfInterest;
    PyObject*           callback;
    PyObject*           info;
    CGEventTapLocation  tap;
    CGEventTapPlacement place;
    CGEventTapOptions   options;
    CGEventMask         eventsOfInterest;
    CFMachPortRef       result = NULL;

    if (!PyArg_ParseTuple(args, "OOOOOO", &py_tap, &py_place, &py_options,
                          &py_eventsOfInterest, &callback, &info)) {

        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGEventTapLocation), py_tap, &tap) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventTapPlacement), py_place, &place) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventTapOptions), py_options, &options) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventMask), py_eventsOfInterest, &eventsOfInterest)
        < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, info);
    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGEventTapCreate(tap, place, options, eventsOfInterest,
                                      m_CGEventTapCallBack, (void*)real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CFMachPortRef), &result);
    if (result != NULL) {
        CFRelease(result); /* Compensate for donated ref */
    }
    return retval;
}

static PyObject*
m_CGEventTapCreateForPSN(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*           py_psn;
    PyObject*           py_place;
    PyObject*           py_options;
    PyObject*           py_eventsOfInterest;
    PyObject*           callback;
    PyObject*           info;
    ProcessSerialNumber psn;
    CGEventTapPlacement place;
    CGEventTapOptions   options;
    CGEventMask         eventsOfInterest;
    CFMachPortRef       result = NULL;

    if (!PyArg_ParseTuple(args, "OOOOOO", &py_psn, &py_place, &py_options,
                          &py_eventsOfInterest, &callback, &info)) {

        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(ProcessSerialNumber), py_psn, &psn) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventTapPlacement), py_place, &place) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventTapOptions), py_options, &options) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGEventMask), py_eventsOfInterest, &eventsOfInterest)
        < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, info);
    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGEventTapCreateForPSN((void*)&psn, place, options, eventsOfInterest,
                                            m_CGEventTapCallBack, (void*)real_info);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CFMachPortRef), &result);
    if (result) {
        CFRelease(result); /* Compensate for donated ref */
    }
    return retval;
}

/*
 * CGPatternCreate
 */

static void
m_CGPatternDrawPatternCallback(void* _info, CGContextRef context)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* ctx = PyObjC_ObjCToPython(@encode(CGContextRef), &context);
    if (context == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "ON",
                                             PyTuple_GetItem(info, 1), ctx);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static void
m_CGPatternReleaseInfoCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF(info);

    PyGILState_Release(state);
}

static CGPatternCallbacks m_CGPatternCallbacks = {
    0,
    m_CGPatternDrawPatternCallback, /* drawPattern */
    m_CGPatternReleaseInfoCallback, /* releaseInfo */
};

static PyObject*
m_CGPatternCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*         info;
    PyObject*         py_bounds;
    PyObject*         py_matrix;
    float             xStep, yStep;
    PyObject*         py_tiling;
    PyObject*         py_isColored;
    PyObject*         draw;
    CGRect            bounds;
    CGAffineTransform matrix;
    CGPatternTiling   tiling;
    int               isColored;

    if (!PyArg_ParseTuple(args, "OOOffOOO", &info, &py_bounds, &py_matrix, &xStep, &yStep,
                          &py_tiling, &py_isColored, &draw)) {

        return NULL;
    }
    if (!PyCallable_Check(draw)) {
        PyErr_Format(PyExc_TypeError, "drawPattern of type %.80s is not callable",
                     Py_TYPE(draw)->tp_name);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGRect), py_bounds, &bounds) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGAffineTransform), py_matrix, &matrix) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPatternTiling), py_tiling, &tiling) < 0) {
        return NULL;
    }
    if (PyObject_IsTrue(py_isColored)) {
        isColored = true;
    } else {
        isColored = false;
    }

    PyObject* real_info = Py_BuildValue("OO", draw, info);
    if (real_info == NULL) {
        return NULL;
    }

    CGPatternRef result = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGPatternCreate((void*)real_info, bounds, matrix, xStep, yStep,
                                     tiling, isColored, &m_CGPatternCallbacks);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    PyObject* retval = PyObjC_ObjCToPython(@encode(CGPatternRef), &result);
    CFRelease(result);
    return retval;
}

/*
 * CGPSConverterCreate
 */

static void
m_CGPSConverterBeginDocumentCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 1), "O", PyTuple_GetItem(info, 0));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterBeginPageCallback(void* _info, size_t pageNumber, CFDictionaryRef pageInfo)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result = PyObject_CallFunction(
        PyTuple_GetItem(info, 3), "OlN", PyTuple_GetItem(info, 0), (long)pageNumber,
        PyObjC_ObjCToPython(@encode(CFDictionaryRef), &pageInfo));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterEndDocumentCallback(void* _info, bool success)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 2), "ON", PyTuple_GetItem(info, 0),
                              PyBool_FromLong(success));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterEndPageCallback(void* _info, size_t pageNumber, CFDictionaryRef pageInfo)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result = PyObject_CallFunction(
        PyTuple_GetItem(info, 4), "OlN", PyTuple_GetItem(info, 0), (long)pageNumber,
        PyObjC_ObjCToPython(@encode(CFDictionaryRef), &pageInfo));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterMessageCallback(void* _info, CFStringRef message)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 6), "ON", PyTuple_GetItem(info, 0),
                              PyObjC_ObjCToPython(@encode(CFStringRef), &message));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterProgressCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 5), "O", PyTuple_GetItem(info, 0));

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);

    PyGILState_Release(state);
}

static void
m_CGPSConverterReleaseInfoCallback(void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 7) != Py_None) {
        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 7), "O",
                                                 PyTuple_GetItem(info, 0));

        if (result == NULL) {
            Py_DECREF(info);
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }
    Py_DECREF(info);

    PyGILState_Release(state);
}

static CGPSConverterCallbacks m_CGPSConverterCallbacks = {
    0,
    m_CGPSConverterBeginDocumentCallback, /* beginDocument */
    m_CGPSConverterEndDocumentCallback,   /* endDocument */
    m_CGPSConverterBeginPageCallback,     /* beginPage */
    m_CGPSConverterEndPageCallback,       /* endPage */
    m_CGPSConverterProgressCallback,      /* noteProgress */
    m_CGPSConverterMessageCallback,       /* noteMessage */
    m_CGPSConverterReleaseInfoCallback    /* releaseInfo */
};

static PyObject*
m_CGPSConverterCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*        info;
    PyObject*        py_options;
    PyObject*        beginDocument;
    PyObject*        endDocument;
    PyObject*        beginPage;
    PyObject*        endPage;
    PyObject*        noteProgress;
    PyObject*        noteMessage;
    PyObject*        releaseInfo;
    CFDictionaryRef  options;
    CGPSConverterRef result = NULL;

    if (!PyArg_ParseTuple(args, "O(OOOOOOO)O", &info, &beginDocument, &endDocument,
                          &beginPage, &endPage, &noteProgress, &noteMessage, &releaseInfo,
                          &py_options)) {

        return NULL;
    }

    if (!PyCallable_Check(beginDocument)) {
        PyErr_SetString(PyExc_TypeError, "beginDocument not callable");
        return NULL;
    }
    if (!PyCallable_Check(endDocument)) {
        PyErr_SetString(PyExc_TypeError, "endDocument not callable");
        return NULL;
    }
    if (!PyCallable_Check(beginPage)) {
        PyErr_SetString(PyExc_TypeError, "beginPage not callable");
        return NULL;
    }
    if (!PyCallable_Check(endPage)) {
        PyErr_SetString(PyExc_TypeError, "endPage not callable");
        return NULL;
    }
    if (!PyCallable_Check(noteProgress)) {
        PyErr_SetString(PyExc_TypeError, "noteProgress not callable");
        return NULL;
    }
    if (!PyCallable_Check(noteMessage)) {
        PyErr_SetString(PyExc_TypeError, "noteMessage not callable");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_options, &options) < 0) {
        return NULL;
    }

    PyObject* real_info =
        Py_BuildValue("OOOOOOOO", info, beginDocument, endDocument, beginPage, endPage,
                      noteProgress, noteMessage, releaseInfo);

    Py_BEGIN_ALLOW_THREADS
        @try {
            result = CGPSConverterCreate(real_info, &m_CGPSConverterCallbacks, options);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    PyObject* v = PyObjC_ObjCToPython(@encode(CGPSConverterRef), &result);
    CFRelease(result);
    return v;
}

static PyMethodDef mod_methods[] = {
    {"CGDataConsumerCreate", (PyCFunction)m_CGDataConsumerCreate, METH_VARARGS,
     doc_CGDataConsumerCreate},

    {"CGDataProviderCreateSequential", (PyCFunction)m_CGDataProviderCreateSequential,
     METH_VARARGS, doc_CGDataProviderCreateSequential},
    {"CGDataProviderCreateWithData", (PyCFunction)m_CGDataProviderCreateWithData,
     METH_VARARGS, doc_CGDataProviderCreateWithData},

    {"CGFunctionCreate", (PyCFunction)m_CGFunctionCreate, METH_VARARGS,
     doc_CGFunctionCreate},
    {"CGDisplayRegisterReconfigurationCallback",
     (PyCFunction)m_CGDisplayRegisterReconfigurationCallback, METH_VARARGS, NULL},
    {"CGDisplayRemoveReconfigurationCallback",
     (PyCFunction)m_CGDisplayRemoveReconfigurationCallback, METH_VARARGS, NULL},
    {"CGScreenRegisterMoveCallback", (PyCFunction)m_CGScreenRegisterMoveCallback,
     METH_VARARGS, NULL},
    {"CGScreenUnregisterMoveCallback", (PyCFunction)m_CGScreenUnregisterMoveCallback,
     METH_VARARGS, NULL},
    {"CGRegisterScreenRefreshCallback", (PyCFunction)m_CGRegisterScreenRefreshCallback,
     METH_VARARGS, NULL},
    {"CGUnregisterScreenRefreshCallback",
     (PyCFunction)m_CGUnregisterScreenRefreshCallback, METH_VARARGS, NULL},
    {"CGEventTapCreate", (PyCFunction)m_CGEventTapCreate, METH_VARARGS, NULL},
    {"CGEventTapCreateForPSN", (PyCFunction)m_CGEventTapCreateForPSN, METH_VARARGS, NULL},
    {"CGPatternCreate", (PyCFunction)m_CGPatternCreate, METH_VARARGS, NULL},
    {"CGPSConverterCreate", (PyCFunction)m_CGPSConverterCreate, METH_VARARGS, NULL},

    {
        0,
        0,
        0,
    }};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0)
        return -1;
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_callbacks",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__callbacks(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__callbacks(void)
{
    return PyModuleDef_Init(&mod_module);
}
