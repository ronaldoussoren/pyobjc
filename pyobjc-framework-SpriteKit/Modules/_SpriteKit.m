#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#include <objc/objc-runtime.h>

#import <SpriteKit/SpriteKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_SpriteKit_protocols.m"

static PyObject*
call_vF3_vF3(PyObject* method, PyObject* self, PyObject* arguments)
{
    /* calling of method that returns vector_float3 and has a vector_float3 as an argument */
    float f1, f2, f3;
    struct objc_super super;


    if (!PyArg_ParseTuple(arguments, "(fff)", &f1, &f2, &f3)) {
        return 0;
    }

    vector_float3 vec = (vector_float3){f1, f2, f3};

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));
        vec = ((vector_float3(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), vec);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("(fff)", vec[0], vec[1], vec[2]);
}

#if 0
static PyObject*
call_id_vF3(PyObject* method, PyObject* self, PyObject* arguments)
{
    /* calling of method that returns id and has a vector_float3 as an argument */
    float f1, f2, f3;
    struct objc_super super;
    id result;


    if (!PyArg_ParseTuple(arguments, "(fff)", &f1, &f2, &f3)) {
        return 0;
    }

    vector_float3 vec = (vector_float3){f1, f2, f3};

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        result = ((id(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), vec);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(result);
}
#endif

static PyObject*
callC_id_vF3(PyObject* method, PyObject* self, PyObject* arguments)
{
    /* calling of method that returns id and has a vector_float3 as an argument */
    float f1, f2, f3;
    struct objc_super super;
    id result;


    if (!PyArg_ParseTuple(arguments, "(fff)", &f1, &f2, &f3)) {
        return 0;
    }

    vector_float3 vec = (vector_float3){f1, f2, f3};

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            object_getClass(PyObjCSelector_GetClass(method)),
            PyObjCClass_GetClass(self));

        result = ((id(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), vec);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_IdToPython(result);
}

static PyObject*
call_vF3_v(PyObject* method, PyObject* self, PyObject* arguments)
{
    /* calling of method that returns vector_float3 and has no arguments */
    struct objc_super super;
    vector_float3 vec;

    if (!PyArg_ParseTuple(arguments, "")) {
        return 0;
    }


    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        vec = ((vector_float3(*)(struct objc_super*, SEL))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method));

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    return Py_BuildValue("(fff)", vec[0], vec[1], vec[2]);
}

static PyObject*
call_v_vF3(PyObject* method, PyObject* self, PyObject* arguments)
{
    /* calling of method that returns void and has a vector_float3 as an argument */
    float f1, f2, f3;
    struct objc_super super;


    if (!PyArg_ParseTuple(arguments, "(fff)", &f1, &f2, &f3)) {
        return 0;
    }

    vector_float3 vec = (vector_float3){f1, f2, f3};

    PyObjC_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        ((void(*)(struct objc_super*, SEL, vector_float3))objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), vec);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};

#define imp_vF3_vF3 PyObjCUnsupportedMethod_IMP
#define imp_v_vF3 PyObjCUnsupportedMethod_IMP
#define imp_vF3_v PyObjCUnsupportedMethod_IMP
#define imp_id_vF3 PyObjCUnsupportedMethod_IMP
#define impC_id_vF3 PyObjCUnsupportedMethod_IMP

/* Python glue */
PyObjC_MODULE_INIT(_SpriteKit)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_SpriteKit)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    {
        Class classSK3DNode = objc_lookUpClass("SK3DNode");
        if (classSK3DNode != NULL) {
            if (PyObjC_RegisterMethodMapping(
                    classSK3DNode,
                    @selector(projectPoint:),
                    call_vF3_vF3,
                    imp_vF3_vF3) < 0) {
                PyObjC_INITERROR();
            }

            if (PyObjC_RegisterMethodMapping(
                    classSK3DNode,
                    @selector(unprojectPoint:),
                    call_vF3_vF3,
                    imp_vF3_vF3) < 0) {
                PyObjC_INITERROR();
            }
        }
    }

    {
        Class classSKFieldNode = objc_lookUpClass("SKFieldNode");
        if (classSKFieldNode != NULL) {
            if (PyObjC_RegisterMethodMapping(
                    classSKFieldNode,
                    @selector(direction),
                    call_vF3_v,
                    imp_vF3_v) < 0) {
                PyObjC_INITERROR();
            }

            if (PyObjC_RegisterMethodMapping(
                    classSKFieldNode,
                    @selector(setDirection:),
                    call_v_vF3,
                    imp_v_vF3) < 0) {
                PyObjC_INITERROR();
            }

            if (PyObjC_RegisterMethodMapping(
                    classSKFieldNode,
                    @selector(linearGravityFieldWithVector:),
                    callC_id_vF3,
                    impC_id_vF3) < 0) {
                PyObjC_INITERROR();
            }

            if (PyObjC_RegisterMethodMapping(
                    classSKFieldNode,
                    @selector(velocityFieldWithVector:),
                    callC_id_vF3,
                    impC_id_vF3) < 0) {
                PyObjC_INITERROR();
            }
        }
    }

    {
        Class classSKPhysicsWorld = objc_lookUpClass("SKPhysicsWorld");
        if (classSKPhysicsWorld != NULL) {
            if (PyObjC_RegisterMethodMapping(
                    classSKPhysicsWorld,
                    @selector(sampleFieldsAt:),
                    call_vF3_vF3,
                    imp_vF3_vF3) < 0) {
                PyObjC_INITERROR();
            }
        }

        Class classPKPhysicsWorld = objc_lookUpClass("PKPhysicsWorld");
        if (classPKPhysicsWorld != NULL) {
            if (PyObjC_RegisterMethodMapping(
                    classPKPhysicsWorld,
                    @selector(sampleFieldsAt:),
                    call_vF3_vF3,
                    imp_vF3_vF3) < 0) {
                PyObjC_INITERROR();
            }
        }
    }

    PyObjC_INITDONE();
}
