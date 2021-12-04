#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#include <objc/objc-runtime.h>

#import <SpriteKit/SpriteKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_SpriteKit_protocols.m"

static PyObject*
call_vF3_vF3(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    /* calling of method that returns vector_float3 and has a vector_float3 as an argument
     */
    float             f1, f2, f3;
    struct objc_super super;
    PyObject*         pyvec;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }

    pyvec = PySequence_Fast(arguments[0], "Expecting a 3 tuple of floats");
    if (pyvec == NULL) {
        return NULL;
    }
    if (PySequence_Fast_GET_SIZE(pyvec) != 3) {
        PyErr_SetString(PyExc_ValueError, "Expecting a 3 tuple of floats");
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 0), &f1)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 1), &f2)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 2), &f3)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    Py_DECREF(pyvec);

    vector_float3 vec = (vector_float3){f1, f2, f3};

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);
            vec               = ((vector_float3(*)(struct objc_super*, SEL,
                                     vector_float3))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), vec);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("(fff)", vec[0], vec[1], vec[2]);
}

#if 0
static PyObject*
call_id_vF3(PyObject* method, PyObject* self, PyObject*const* arguments, size_t nargs)
{
    /* calling of method that returns id and has a vector_float3 as an argument */
    float f1, f2, f3;
    struct objc_super super;
    id result;
    PyObject* pyvec;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }

    pyvec = PySequence_Fast(arguments[0], "Expecting a 3 tuple of floats");
    if (pyvec == NULL) {
        return NULL;
    }
    if (PySequence_Fast_GET_SIZE(pyvec) != 3) {
        PyErr_SetString(PyExc_ValueError, "Expecting a 3 tuple of floats");
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 0), &f1) == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 1), &f2) == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 2), &f3) == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    Py_DECREF(pyvec);


    vector_float3 vec = (vector_float3){f1, f2, f3};

    Py_BEGIN_ALLOW_THREADS
            @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver = PyObjCObject_GetObject(self);

        result = ((id(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), vec);

            } @catch (NSException *localException) {
        PyObjCErr_FromObjC(localException);

            }
        Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(result);
}
#endif

static PyObject*
callC_id_vF3(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    /* calling of method that returns id and has a vector_float3 as an argument */
    float             f1, f2, f3;
    struct objc_super super;
    id                result;
    PyObject*         pyvec;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }

    pyvec = PySequence_Fast(arguments[0], "Expecting a 3 tuple of floats");
    if (pyvec == NULL) {
        return NULL;
    }
    if (PySequence_Fast_GET_SIZE(pyvec) != 3) {
        PyErr_SetString(PyExc_ValueError, "Expecting a 3 tuple of floats");
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 0), &f1)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 1), &f2)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 2), &f3)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    Py_DECREF(pyvec);

    vector_float3 vec = (vector_float3){f1, f2, f3};

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = object_getClass(PyObjCSelector_GetClass(method));
            super.receiver    = PyObjCClass_GetClass(self);

            result = ((id(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), vec);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(result);
}

static PyObject*
call_vF3_v(PyObject* method, PyObject* self,
           PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    /* calling of method that returns vector_float3 and has no arguments */
    struct objc_super super;
    vector_float3     vec;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            vec = ((vector_float3(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method));

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("(fff)", vec[0], vec[1], vec[2]);
}

static PyObject*
call_v_vF3(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    /* calling of method that returns void and has a vector_float3 as an argument */
    float             f1, f2, f3;
    struct objc_super super;
    PyObject*         pyvec;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1) {
        return NULL;
    }

    pyvec = PySequence_Fast(arguments[0], "Expecting a 3 tuple of floats");
    if (pyvec == NULL) {
        return NULL;
    }
    if (PySequence_Fast_GET_SIZE(pyvec) != 3) {
        PyErr_SetString(PyExc_ValueError, "Expecting a 3 tuple of floats");
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 0), &f1)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 1), &f2)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(float), PySequence_Fast_GET_ITEM(pyvec, 2), &f3)
        == -1) {
        Py_DECREF(pyvec);
        return NULL;
    }
    Py_DECREF(pyvec);

    vector_float3 vec = (vector_float3){f1, f2, f3};

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            ((void (*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(
                &super, PyObjCSelector_GetSelector(method), vec);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

#define imp_vF3_vF3 PyObjCUnsupportedMethod_IMP
#define imp_v_vF3 PyObjCUnsupportedMethod_IMP
#define imp_vF3_v PyObjCUnsupportedMethod_IMP
#define imp_id_vF3 PyObjCUnsupportedMethod_IMP
#define impC_id_vF3 PyObjCUnsupportedMethod_IMP

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_SpriteKit", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__SpriteKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__SpriteKit(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    {
        Class classSK3DNode = objc_lookUpClass("SK3DNode");
        if (classSK3DNode != NULL) {
            if (PyObjC_RegisterMethodMapping(classSK3DNode, @selector(projectPoint:),
                                             call_vF3_vF3, imp_vF3_vF3)
                < 0) {
                return NULL;
            }

            if (PyObjC_RegisterMethodMapping(classSK3DNode, @selector(unprojectPoint:),
                                             call_vF3_vF3, imp_vF3_vF3)
                < 0) {
                return NULL;
            }
        }
    }

    {
        Class classSKFieldNode = objc_lookUpClass("SKFieldNode");
        if (classSKFieldNode != NULL) {
            if (PyObjC_RegisterMethodMapping(classSKFieldNode, @selector(direction),
                                             call_vF3_v, imp_vF3_v)
                < 0) {
                return NULL;
            }

            if (PyObjC_RegisterMethodMapping(classSKFieldNode, @selector(setDirection:),
                                             call_v_vF3, imp_v_vF3)
                < 0) {
                return NULL;
            }

            if (PyObjC_RegisterMethodMapping(classSKFieldNode,
                                             @selector(linearGravityFieldWithVector:),
                                             callC_id_vF3, impC_id_vF3)
                < 0) {
                return NULL;
            }

            if (PyObjC_RegisterMethodMapping(classSKFieldNode,
                                             @selector(velocityFieldWithVector:),
                                             callC_id_vF3, impC_id_vF3)
                < 0) {
                return NULL;
            }
        }
    }

    {
        Class classSKPhysicsWorld = objc_lookUpClass("SKPhysicsWorld");
        if (classSKPhysicsWorld != NULL) {
            if (PyObjC_RegisterMethodMapping(classSKPhysicsWorld,
                                             @selector(sampleFieldsAt:), call_vF3_vF3,
                                             imp_vF3_vF3)
                < 0) {
                return NULL;
            }
        }

        Class classPKPhysicsWorld = objc_lookUpClass("PKPhysicsWorld");
        if (classPKPhysicsWorld != NULL) {
            if (PyObjC_RegisterMethodMapping(classPKPhysicsWorld,
                                             @selector(sampleFieldsAt:), call_vF3_vF3,
                                             imp_vF3_vF3)
                < 0) {
                return NULL;
            }
        }
    }

    return m;
}
