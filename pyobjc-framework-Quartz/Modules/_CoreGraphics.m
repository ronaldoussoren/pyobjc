/*
 * Manual wrappers for CoreGraphics
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGFontCopyTableTags(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                      size_t    nargs)
{
    CGFontRef  font = NULL;
    CFArrayRef tags = NULL;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGFontRef), args[0], &font) == -1) {
        return NULL;
    }

    tags = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            tags = CGFontCopyTableTags(font);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            tags = NULL;                         // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (tags == NULL && PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;                      // LCOV_EXCL_LINE

    if (tags == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_ssize_t len = CFArrayGetCount(tags);
    Py_ssize_t i;
    PyObject*  result = PyTuple_New(len);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        CFRelease(tags);
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < len; i++) {
        uint32_t  cur = (uint32_t)(uintptr_t)CFArrayGetValueAtIndex(tags, i);
        PyObject* v   = PyObjC_ObjCToPython(@encode(uint32_t), &cur);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            CFRelease(tags);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    CFRelease(tags);
    return result;
}

static PyObject*
m_CGWindowListCreate(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                     size_t    nargs)
{
    CGWindowListOption option;
    CGWindowID         relativeToWindow;
    CFArrayRef         windowList;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowListOption), args[0], &option) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowID), args[1], &relativeToWindow) == -1) {
        return NULL;
    }

    windowList = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            windowList = CGWindowListCreate(option, relativeToWindow);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            windowList = NULL;                   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (windowList == NULL && PyErr_Occurred()) // LCOV_EXCL_LINE
        return NULL;                            // LCOV_EXCL_LINE

    if (windowList == NULL) { // LOV_BR_EXCL_LINE
        /* Cannot reproduce this in testing */
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    Py_ssize_t len = CFArrayGetCount(windowList);
    Py_ssize_t i;
    PyObject*  result = PyTuple_New(len);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        CFRelease(windowList);
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < len; i++) {
        CGWindowID cur = (CGWindowID)(NSInteger)CFArrayGetValueAtIndex(windowList, i);
        PyObject*  v   = PyObjC_ObjCToPython(@encode(CGWindowID), &cur);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            CFRelease(windowList);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    CFRelease(windowList);
    return result;
}

static CFArrayRef
createWindowList(PyObject* items)
{
    PyObject* seq = PySequence_Tuple(items);
    if (seq == NULL) {
        return NULL;
    }

    CFMutableArrayRef array = CFArrayCreateMutable(NULL, PyTuple_GET_SIZE(seq), NULL);
    if (array == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(seq);
        PyErr_SetString(PyExc_ValueError, "Cannot create CFArray");
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_ssize_t len = PyTuple_GET_SIZE(seq);
    Py_ssize_t i;
    for (i = 0; i < len; i++) {
        CGWindowID windowID;

        if (PyObjC_PythonToObjC(@encode(CGWindowID), PyTuple_GET_ITEM(seq, i), &windowID)
            == -1) {
            Py_DECREF(seq);
            CFRelease(array);
            return NULL;
        }
        CFArrayAppendValue(array, (const void*)(NSInteger)windowID);
    }
    Py_DECREF(seq);
    return (CFArrayRef)array;
}

static PyObject*
m_CGWindowListCreateDescriptionFromArray(PyObject* meth,
                                         PyObject* _Nonnull const* _Nonnull args,
                                         size_t nargs)
{
    CFArrayRef windowArray;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    windowArray = createWindowList(args[0]);
    if (windowArray == NULL) {
        return NULL;
    }

    CFArrayRef descriptions = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            descriptions = CGWindowListCreateDescriptionFromArray(windowArray);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            descriptions = NULL;                 // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    CFRelease(windowArray);

    if (descriptions == NULL && PyErr_Occurred()) // LCOV_EXCL_LINE
        return NULL;                              // LCOV_EXCL_LINE

    if (descriptions == NULL) { // LCOV_BR_EXCL_LINE
        /* Cannot reproduce this in testing */
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CFArrayRef), &descriptions);
    CFRelease(descriptions);
    return rv;
}

#if MAC_OS_X_VERSION_MIN_REQUIRED < 150000
static PyObject*
m_CGWindowListCreateImageFromArray(PyObject* meth,
                                   PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CGRect              screenBounds;
    CFArrayRef          windowArray;
    CGWindowImageOption imageOption;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGRect), args[0], &screenBounds) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowImageOption), args[2], &imageOption) == -1) {
        return NULL;
    }

    windowArray = createWindowList(args[1]);
    if (windowArray == NULL) {
        return NULL;
    }

    CGImageRef image = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
            image =
                CGWindowListCreateImageFromArray(screenBounds, windowArray, imageOption);
#pragma clang diagnostic pop

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            image = NULL;                        // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    CFRelease(windowArray);

    if (image == NULL && PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;                       // LCOV_EXCL_LINE

    if (image == NULL) { // LCOV_BR_EXCL_LINE
        /* Cannot reproduce in testing */
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CGImageRef), &image);
    CFRelease(image);
    return rv;
}
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED < 150000 */

static PyObject*
m_CGBitmapContextCreate(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                        size_t    nargs)
{
    size_t          width;
    size_t          height;
    size_t          bitsPerComponent;
    size_t          bytesPerRow;
    CGColorSpaceRef colorSpace;
    CGBitmapInfo    bitmapInfo;
    Py_buffer       view;

    if (PyObjC_CheckArgCount(meth, 7, 7, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), args[1], &width) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[2], &height) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[3], &bitsPerComponent) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[4], &bytesPerRow) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), args[5], &colorSpace) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), args[6], &bitmapInfo) == -1) {
        return NULL;
    }

    if (args[0] == Py_None) {
        /* pass */

    } else if (PyUnicode_Check(args[0])) {
        PyErr_SetString(PyExc_TypeError, "cannot use str as backing store");
        return NULL;

    } else {
        /* XXX: Is the correct
         *      -> There is no guarantee that the buffer stays valid during the lifetime
         *         of the context (e.g. if the backing store is a PyBytesArray object
         *         that gets resized)
         */
        if (PyObject_GetBuffer(args[0], &view, PyBUF_CONTIG) == -1) {
            return NULL;
        }
    }

    CGContextRef ctx = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            ctx = CGBitmapContextCreate(args[0] == Py_None ? NULL : view.buf, width,
                                        height, bitsPerComponent, bytesPerRow, colorSpace,
                                        bitmapInfo);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            ctx = NULL;                          // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (args[0] != Py_None) {
        /* This is not safe in general, but there is no way to keep the
         * buffer alive until after the bitmap context is deallocated.
         */
        PyBuffer_Release(&view);
    }

    if (ctx == NULL && PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;                     // LCOV_EXCL_LINE

    if (ctx == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CGContextRef), &ctx);
    CFRelease(ctx);
    return rv;
}

static void
m_releasecallback(void* releaseInfo, void* data)
{
    PyObject* py_data = (PyObject*)releaseInfo;
    PyObject* view;

    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(releaseInfo, 0) != Py_None) {
        PyObject* r = PyObject_CallFunction(PyTuple_GetItem(py_data, 0), "OO",
                                            PyTuple_GetItem(py_data, 1),
                                            PyTuple_GetItem(py_data, 2));
        Py_XDECREF(r);
    }

    view = PyTuple_GetItem(py_data, 3);
    PyBuffer_Release(PyObjCMemView_GetBuffer(view));

    Py_DECREF(py_data);

    if (PyErr_Occurred()) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyGILState_Release(state);
}

static PyObject*
m_CGBitmapContextCreateWithData(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                                size_t    nargs)
{
    PyObject*       view = NULL;
    size_t          width;
    size_t          height;
    size_t          bitsPerComponent;
    size_t          bytesPerRow;
    CGColorSpaceRef colorSpace;
    CGBitmapInfo    bitmapInfo;

    if (PyObjC_CheckArgCount(meth, 9, 9, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), args[1], &width) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[2], &height) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[3], &bitsPerComponent) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[4], &bytesPerRow) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), args[5], &colorSpace) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), args[6], &bitmapInfo) == -1) {
        return NULL;
    }

    if (args[0] == Py_None) {
        /* pass */

    } else if (PyUnicode_Check(args[0])) {
        PyErr_SetString(PyExc_TypeError, "cannot use str as backing store");
        return NULL;

    } else {
        view = PyObjCMemView_New();
        if (view == NULL) // LCOV_BR_EXCL_LINE
            return NULL;  // LCOV_EXCL_LINE

        if (PyObject_GetBuffer(args[0], PyObjCMemView_GetBuffer(view), PyBUF_CONTIG)
            == -1) {
            Py_DECREF(view);
            return NULL;
        }
    }

    PyObject* releaseInfo = PyTuple_Pack(4, args[7], args[8], args[0], view);
    if (releaseInfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE

    CGContextRef ctx = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            ctx = CGBitmapContextCreateWithData(
                view ? PyObjCMemView_GetBuffer(view)->buf : NULL, width, height,
                bitsPerComponent, bytesPerRow, colorSpace, bitmapInfo, m_releasecallback,
                releaseInfo);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            ctx = NULL;                          // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (ctx == NULL && PyErr_Occurred()) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        PyBuffer_Release(PyObjCMemView_GetBuffer(view));
        Py_DECREF(view);
        Py_DECREF(releaseInfo);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (ctx == NULL) {
        PyBuffer_Release(PyObjCMemView_GetBuffer(view));
        Py_DECREF(releaseInfo);
        Py_DECREF(view);
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_DECREF(view);
    PyObject* rv = PyObjC_ObjCToPython(@encode(CGContextRef), &ctx);
    CFRelease(ctx);
    return rv;
}

static PyObject*
m_CGPDFObjectGetValue(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                      size_t    nargs)
{
    bool            res;
    CGPDFObjectRef  obj;
    CGPDFObjectType type;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGPDFObjectRef), args[0], &obj) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPDFObjectType), args[1], &type) == -1) {
        return NULL;
    }
    if (args[2] != Py_None && args[2] != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "value must be None or objc.NULL");
        return NULL;
    }

    switch (type) {
    case kCGPDFObjectTypeNull: {
        res = CGPDFObjectGetValue(obj, type, NULL);
        return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
    } break;

    case kCGPDFObjectTypeBoolean: {
        if (args[2] == Py_None) {
            CGPDFBoolean val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyBool_FromLong(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;

    case kCGPDFObjectTypeInteger: {
        if (args[2] == Py_None) {
            CGPDFInteger val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyLong_FromLong(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeReal: {
        if (args[2] == Py_None) {
            CGPDFReal val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyFloat_FromDouble(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeName: {
        if (args[2] == Py_None) {
            char* val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyUnicode_FromString(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeString: {
        if (args[2] == Py_None) {
            CGPDFStringRef val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res),
                                 PyObjC_ObjCToPython(@encode(CGPDFStringRef), &val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeArray: {
        if (args[2] == Py_None) {
            CGPDFArrayRef val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res),
                                 PyObjC_ObjCToPython(@encode(CGPDFArrayRef), &val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeDictionary: {
        if (args[2] == Py_None) {
            CGPDFDictionaryRef val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res),
                                 PyObjC_ObjCToPython(@encode(CGPDFDictionaryRef), &val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeStream: {
        if (args[2] == Py_None) {
            CGPDFStreamRef val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res),
                                 PyObjC_ObjCToPython(@encode(CGPDFStreamRef), &val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;

    default:
        PyErr_SetString(PyExc_ValueError, "Invalid object type");
        return NULL;
    }
}

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CGFontCopyTableTags, m_CGFontCopyTableTags)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGWindowListCreate, m_CGWindowListCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGWindowListCreateDescriptionFromArray,
                                      m_CGWindowListCreateDescriptionFromArray)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
#if MAC_OS_X_VERSION_MIN_REQUIRED < 150000
    if (PyObjCRegister_FunctionCaller(CGWindowListCreateImageFromArray,
                                      m_CGWindowListCreateImageFromArray)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED < 150000 */
    if (PyObjCRegister_FunctionCaller(CGBitmapContextCreate, m_CGBitmapContextCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGBitmapContextCreateWithData,
                                      m_CGBitmapContextCreateWithData)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGPDFObjectGetValue, m_CGPDFObjectGetValue)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

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
    .m_name     = "_CoreGraphics",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__CoreGraphics(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__CoreGraphics(void)
{
    return PyModuleDef_Init(&mod_module);
}
