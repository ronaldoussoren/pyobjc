/*
 * Manual wrappers for CoreGraphics
 */
/*#define Py_LIMITED_API 0x03060000*/
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGFontCopyTableTags(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*  py_font;
    CGFontRef  font = NULL;
    CFArrayRef tags = NULL;

    if (!PyArg_ParseTuple(args, "O", &py_font)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGFontRef), py_font, &font) == -1) {
        return NULL;
    }

    tags = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            tags = CGFontCopyTableTags(font);

        } @catch (NSException* localException) {
            tags = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (tags == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (tags == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_ssize_t len = CFArrayGetCount(tags);
    Py_ssize_t i;
    PyObject*  result = PyTuple_New(len);
    if (result == NULL) {
        CFRelease(tags);
        return NULL;
    }

    for (i = 0; i < len; i++) {
        uint32_t  cur = (uint32_t)(uintptr_t)CFArrayGetValueAtIndex(tags, i);
        PyObject* v   = PyObjC_ObjCToPython(@encode(uint32_t), &cur);
        if (v == NULL) {
            CFRelease(tags);
            return NULL;
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    CFRelease(tags);
    return result;
}

static PyObject*
m_CGWindowListCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*          py_option;
    PyObject*          py_relativeToWindow;
    CGWindowListOption option;
    CGWindowID         relativeToWindow;
    CFArrayRef         windowList;

    if (!PyArg_ParseTuple(args, "OO", &py_option, &py_relativeToWindow)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowListOption), py_option, &option) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowID), py_relativeToWindow, &relativeToWindow)
        == -1) {
        return NULL;
    }

    windowList = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            windowList = CGWindowListCreate(option, relativeToWindow);

        } @catch (NSException* localException) {
            windowList = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (windowList == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (windowList == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    Py_ssize_t len = CFArrayGetCount(windowList);
    Py_ssize_t i;
    PyObject*  result = PyTuple_New(len);
    if (result == NULL) {
        CFRelease(windowList);
        return NULL;
    }

    for (i = 0; i < len; i++) {
        CGWindowID cur = (CGWindowID)(NSInteger)CFArrayGetValueAtIndex(windowList, i);
        PyObject*  v   = PyObjC_ObjCToPython(@encode(CGWindowID), &cur);
        if (v == NULL) {
            CFRelease(windowList);
            return NULL;
        }
        PyTuple_SET_ITEM(result, i, v);
    }
    CFRelease(windowList);
    return result;
}

static CFArrayRef
createWindowList(PyObject* items)
{
    PyObject* seq = PySequence_Fast(items, "list of windowIDs");
    if (seq == NULL) {
        return NULL;
    }

    CFMutableArrayRef array =
        CFArrayCreateMutable(NULL, PySequence_Fast_GET_SIZE(seq), NULL);
    if (array == NULL) {
        Py_DECREF(seq);
        PyErr_SetString(PyExc_ValueError, "Cannot create CFArray");
        return NULL;
    }

    Py_ssize_t len = PySequence_Fast_GET_SIZE(seq);
    Py_ssize_t i;
    for (i = 0; i < len; i++) {
        CGWindowID windowID;

        if (PyObjC_PythonToObjC(@encode(CGWindowID), PySequence_Fast_GET_ITEM(seq, i),
                                &windowID)
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
m_CGWindowListCreateDescriptionFromArray(PyObject* self __attribute__((__unused__)),
                                         PyObject* args)
{
    PyObject*  py_windowArray;
    CFArrayRef windowArray;

    if (!PyArg_ParseTuple(args, "O", &py_windowArray)) {
        return NULL;
    }

    windowArray = createWindowList(py_windowArray);
    if (windowArray == NULL) {
        return NULL;
    }

    CFArrayRef descriptions = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            descriptions = CGWindowListCreateDescriptionFromArray(windowArray);

        } @catch (NSException* localException) {
            descriptions = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    CFRelease(windowArray);

    if (descriptions == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (descriptions == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CFArrayRef), &descriptions);
    CFRelease(descriptions);
    return rv;
}

#if defined(MAC_OS_X_VERSION_15_0) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_15_0
static PyObject*
m_CGWindowListCreateImageFromArray(PyObject* self __attribute__((__unused__)),
                                   PyObject* args)
{
    PyObject*           py_screenBounds;
    PyObject*           py_windowArray;
    PyObject*           py_imageOption;
    CGRect              screenBounds;
    CFArrayRef          windowArray;
    CGWindowImageOption imageOption;

    if (!PyArg_ParseTuple(args, "OOO", &py_screenBounds, &py_windowArray,
                          &py_imageOption)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGRect), py_screenBounds, &screenBounds) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CGWindowImageOption), py_imageOption, &imageOption)
        == -1) {
        return NULL;
    }

    windowArray = createWindowList(py_windowArray);
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

        } @catch (NSException* localException) {
            image = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    CFRelease(windowArray);

    if (image == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (image == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CGImageRef), &image);
    CFRelease(image);
    return rv;
}
#endif /* defined(MAC_OS_X_VERSION_15_0) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_15_0 */

static PyObject*
m_CGBitmapContextCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* py_data;
    PyObject* py_width;
    PyObject* py_height;
    PyObject* py_bitsPerComponent;
    PyObject* py_bytesPerRow;
    PyObject* py_colorSpace;
    PyObject* py_bitmapInfo;

    size_t          width;
    size_t          height;
    size_t          bitsPerComponent;
    size_t          bytesPerRow;
    CGColorSpaceRef colorSpace;
    CGBitmapInfo    bitmapInfo;
    Py_buffer       view;

    if (!PyArg_ParseTuple(args, "OOOOOOO", &py_data, &py_width, &py_height,
                          &py_bitsPerComponent, &py_bytesPerRow, &py_colorSpace,
                          &py_bitmapInfo)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), py_width, &width) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_height, &height) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_bitsPerComponent, &bitsPerComponent)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_bytesPerRow, &bytesPerRow) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), py_colorSpace, &colorSpace) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), py_bitmapInfo, &bitmapInfo) == -1) {
        return NULL;
    }

    if (py_data == Py_None) {
        /* pass */

    } else if (PyUnicode_Check(py_data)) {
        PyErr_SetString(PyExc_TypeError, "Cannot use Unicode as backing store");
        return NULL;

    } else {
        if (PyObject_GetBuffer(py_data, &view, PyBUF_CONTIG) == -1) {
            return NULL;
        }
    }

    CGContextRef ctx = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            ctx = CGBitmapContextCreate(py_data == Py_None ? NULL : view.buf, width,
                                        height, bitsPerComponent, bytesPerRow, colorSpace,
                                        bitmapInfo);

        } @catch (NSException* localException) {
            ctx = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (py_data != Py_None) {
        /* This is not safe in general, but there is no way to keep the
         * buffer alive until after the bitmap context is deallocated.
         */
        PyBuffer_Release(&view);
    }

    if (ctx == NULL && PyErr_Occurred()) {
        return NULL;
    }

    if (ctx == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
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
m_CGBitmapContextCreateWithData(PyObject* self __attribute__((__unused__)),
                                PyObject* args)
{
    PyObject* py_data;
    PyObject* py_width;
    PyObject* py_height;
    PyObject* py_bitsPerComponent;
    PyObject* py_bytesPerRow;
    PyObject* py_colorSpace;
    PyObject* py_bitmapInfo;
    PyObject* py_releaseCallback;
    PyObject* py_releaseInfo;

    PyObject*       view = NULL;
    size_t          width;
    size_t          height;
    size_t          bitsPerComponent;
    size_t          bytesPerRow;
    CGColorSpaceRef colorSpace;
    CGBitmapInfo    bitmapInfo;

    if (!PyArg_ParseTuple(args, "OOOOOOOOO", &py_data, &py_width, &py_height,
                          &py_bitsPerComponent, &py_bytesPerRow, &py_colorSpace,
                          &py_bitmapInfo, &py_releaseCallback, &py_releaseInfo)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(size_t), py_width, &width) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_height, &height) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_bitsPerComponent, &bitsPerComponent)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_bytesPerRow, &bytesPerRow) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), py_colorSpace, &colorSpace) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), py_bitmapInfo, &bitmapInfo) == -1) {
        return NULL;
    }

    if (py_data == Py_None) {
        /* pass */

    } else if (PyUnicode_Check(py_data)) {
        PyErr_SetString(PyExc_TypeError, "Cannot use Unicode as backing store");
        return NULL;

    } else {
        view = PyObjCMemView_New();
        if (view == NULL) {
            return NULL;
        }

        if (PyObject_GetBuffer(py_data, PyObjCMemView_GetBuffer(view), PyBUF_CONTIG)
            == -1) {
            Py_DECREF(view);
            return NULL;
        }
    }

    PyObject* releaseInfo = PyTuple_New(4);
    if (releaseInfo == NULL) {
        return NULL;
    }
    PyTuple_SET_ITEM(releaseInfo, 0, py_releaseCallback);
    Py_INCREF(py_releaseCallback);
    PyTuple_SET_ITEM(releaseInfo, 1, py_releaseInfo);
    Py_INCREF(py_releaseInfo);
    PyTuple_SET_ITEM(releaseInfo, 2, py_data);
    Py_INCREF(py_data);
    PyTuple_SET_ITEM(releaseInfo, 3, view);

    CGContextRef ctx = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            ctx = CGBitmapContextCreateWithData(
                view ? PyObjCMemView_GetBuffer(view)->buf : NULL, width, height,
                bitsPerComponent, bytesPerRow, colorSpace, bitmapInfo, m_releasecallback,
                releaseInfo);

        } @catch (NSException* localException) {
            ctx = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (ctx == NULL && PyErr_Occurred()) {
        PyBuffer_Release(PyObjCMemView_GetBuffer(view));
        Py_DECREF(releaseInfo);
        return NULL;
    }

    if (ctx == NULL) {
        PyBuffer_Release(PyObjCMemView_GetBuffer(view));
        Py_DECREF(releaseInfo);
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* rv = PyObjC_ObjCToPython(@encode(CGContextRef), &ctx);
    CFRelease(ctx);
    return rv;
}

static PyObject*
m_CGPDFObjectGetValue(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    bool            res;
    CGPDFObjectRef  obj;
    CGPDFObjectType type;
    PyObject*       p_obj;
    PyObject*       p_type;
    PyObject*       p_val;

    if (!PyArg_ParseTuple(args, "OOO", &p_obj, &p_type, &p_val)) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPDFObjectRef), p_obj, &obj) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPDFObjectType), p_type, &type) == -1) {
        return NULL;
    }
    if (p_val != Py_None && p_val != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "value must be None or objc.NULL");
        return NULL;
    }

    switch (type) {
    case kCGPDFObjectTypeNull: {
        res = CGPDFObjectGetValue(obj, type, NULL);
        return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
    } break;

    case kCGPDFObjectTypeBoolean: {
        if (p_val == Py_None) {
            CGPDFBoolean val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyBool_FromLong(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;

    case kCGPDFObjectTypeInteger: {
        if (p_val == Py_None) {
            CGPDFInteger val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyLong_FromLong(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeReal: {
        if (p_val == Py_None) {
            CGPDFReal val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyFloat_FromDouble(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeName: {
        if (p_val == Py_None) {
            char* val;
            res = CGPDFObjectGetValue(obj, type, &val);
            return Py_BuildValue("NN", PyBool_FromLong(res), PyUnicode_FromString(val));
        } else {
            res = CGPDFObjectGetValue(obj, type, NULL);
            return Py_BuildValue("NO", PyBool_FromLong(res), Py_None);
        }
    } break;
    case kCGPDFObjectTypeString: {
        if (p_val == Py_None) {
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
        if (p_val == Py_None) {
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
        if (p_val == Py_None) {
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
        if (p_val == Py_None) {
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

static PyMethodDef mod_methods[] = {
    {"CGFontCopyTableTags", (PyCFunction)m_CGFontCopyTableTags, METH_VARARGS, NULL},
    {"CGWindowListCreate", (PyCFunction)m_CGWindowListCreate, METH_VARARGS, NULL},
    {"CGWindowListCreateDescriptionFromArray",
     (PyCFunction)m_CGWindowListCreateDescriptionFromArray, METH_VARARGS, NULL},
#if defined(MAC_OS_X_VERSION_15_0) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_15_0
    {"CGWindowListCreateImageFromArray", (PyCFunction)m_CGWindowListCreateImageFromArray,
     METH_VARARGS, NULL},
#endif /* defined(MAC_OS_X_VERSION_15_0) && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_15_0 */
    {"CGBitmapContextCreate", (PyCFunction)m_CGBitmapContextCreate, METH_VARARGS, NULL},
    {"CGBitmapContextCreateWithData", (PyCFunction)m_CGBitmapContextCreateWithData,
     METH_VARARGS, NULL},
    {"CGPDFObjectGetValue", (PyCFunction)m_CGPDFObjectGetValue, METH_VARARGS, NULL},

    {
        0,
        0,
        0,
    }};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_coregraphics", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__coregraphics(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__coregraphics(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (!m)
        return NULL;

    if (PyObjC_ImportAPI(m) < 0)
        return NULL;

    return m;
}
