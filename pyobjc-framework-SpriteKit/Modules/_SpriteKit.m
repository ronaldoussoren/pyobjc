#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#include <objc/objc-runtime.h>

#import <SpriteKit/SpriteKit.h>

#include "_SpriteKit_protocols.m"

#if PyObjC_BUILD_RELEASE >= 1012
static vector_float2*
parse_v2f_array(NSInteger vertexCount, PyObject* value)
{
    vector_float2* result;
    NSInteger      i;

    if (!PySequence_Check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting sequence of length %ld", vertexCount);
        return NULL;
    }
    if (PySequence_Length(value) != vertexCount) {
        PyErr_Format(PyExc_TypeError, "Expecting sequence of length %ld", vertexCount);
        return NULL;
    }

    result = PyMem_Malloc(sizeof(vector_float2) * vertexCount);
    if (result == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    for (i = 0; i < vertexCount; i++) {
        PyObject* item = PySequence_GetItem(value, i);
        if (item == NULL) {
            PyMem_Free(result);
            return NULL;
        }
        if (PyObjC_PythonToObjC("<2f>", item, result + i) == -1) {
            Py_DECREF(item);
            PyMem_Free(result);
            return NULL;
        }
    }
    return result;
}

static PyObject* _Nullable mod_SKWarpGeometryGrid_xWithColumns_rows_sourcePositions_destPositions_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    NSInteger         rows;
    NSInteger         columns;
    vector_float2*    srcPos;
    vector_float2*    dstPos;
    NSInteger         vertexCount;
    struct objc_super super;
    NSObject*         rv = nil;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[0], &rows) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(NSInteger), arguments[1], &columns) == -1) {
        return NULL;
    }
    vertexCount = (rows + 1) * (columns + 1);

    if (arguments[2] == Py_None) {
        srcPos = NULL;
    } else {
        srcPos = parse_v2f_array(vertexCount, arguments[2]);
        if (srcPos == NULL) {
            return NULL;
        }
    }

    if (arguments[3] == Py_None) {
        dstPos = NULL;
    } else {
        dstPos = parse_v2f_array(vertexCount, arguments[3]);
        if (dstPos == NULL) {
            if (srcPos != NULL) {
                PyMem_Free(srcPos);
            }
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(id), self, &super.receiver) == -1) {
        PyMem_Free(srcPos);
        PyMem_Free(dstPos);
        return NULL;
    }
    super.super_class = object_getClass(super.receiver);

    SEL sel = PyObjCSelector_GetSelector(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((id (*)(struct objc_super*, SEL, NSInteger, NSInteger, vector_float2*,
                          vector_float2*))objc_msgSendSuper)(&super, sel, rows, columns,
                                                             srcPos, dstPos);

        } @catch (NSException* localException) {
            NSLog(@"failed with %@", localException);
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (srcPos != NULL) {
        PyMem_Free(srcPos);
    }
    if (dstPos != NULL) {
        PyMem_Free(dstPos);
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(rv);
}

static PyObject* _Nullable mod_SKWarpGeometryGrid_gridByReplacingPositions_(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    vector_float2*    pos;
    NSInteger         vertexCount;
    struct objc_super super;
    NSObject*         rv = nil;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            vertexCount = [(SKWarpGeometryGrid*)PyObjCObject_GetObject(self) vertexCount];
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    /* Not Nullable */
    pos = parse_v2f_array(vertexCount, arguments[0]);
    if (pos == NULL) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(id), self, &super.receiver) == -1) {
        PyMem_Free(pos);
        return NULL;
    }
    super.super_class = object_getClass(super.receiver);

    SEL sel = PyObjCSelector_GetSelector(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((id (*)(struct objc_super*, SEL, vector_float2*))objc_msgSendSuper)(
                &super, sel, pos);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (pos != NULL) {
        PyMem_Free(pos);
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(rv);
}

#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

#if PyObjC_BUILD_RELEASE >= 1012
    Class classSKWarpGeometryGrid = objc_lookUpClass("SKWarpGeometryGrid");
    if (classSKWarpGeometryGrid != NULL) {
        if (PyObjC_RegisterMethodMapping(
                classSKWarpGeometryGrid,
                @selector(gridWithColumns:rows:sourcePositions:destPositions:),
                mod_SKWarpGeometryGrid_xWithColumns_rows_sourcePositions_destPositions_,
                PyObjCUnsupportedMethod_IMP)
            == -1) {
            return -1;
        }

        if (PyObjC_RegisterMethodMapping(
                classSKWarpGeometryGrid,
                @selector(initWithColumns:rows:sourcePositions:destPositions:),
                mod_SKWarpGeometryGrid_xWithColumns_rows_sourcePositions_destPositions_,
                PyObjCUnsupportedMethod_IMP)
            == -1) {
            return -1;
        }

        if (PyObjC_RegisterMethodMapping(classSKWarpGeometryGrid,
                                         @selector(gridByReplacingSourcePositions:),
                                         mod_SKWarpGeometryGrid_gridByReplacingPositions_,
                                         PyObjCUnsupportedMethod_IMP)
            == -1) {
            return -1;
        }

        if (PyObjC_RegisterMethodMapping(classSKWarpGeometryGrid,
                                         @selector(gridByReplacingDestPositions:),
                                         mod_SKWarpGeometryGrid_gridByReplacingPositions_,
                                         PyObjCUnsupportedMethod_IMP)
            == -1) {
            return -1;
        }
    }
#endif

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
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
    .m_name     = "_SpriteKit",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__SpriteKit(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__SpriteKit(void)
{
    return PyModuleDef_Init(&mod_module);
}
