#ifndef PyObjC_SELECTOR_H
#define PyObjC_SELECTOR_H

/* We have a small class-tree for selector/objective-C methods: A base type
 * and two subtypes (one for methods implemented in python and one for methods
 * implemented in Objective-C)
 */

#define PyObjCSelector_kCLASS_METHOD 0x000001
#define PyObjCSelector_kHIDDEN 0x000002
#define PyObjCSelector_kREQUIRED 0x000004
#define PyObjCSelector_kRETURNS_UNINITIALIZED 0x000010
#define PyObjCSelector_kNATIVE 0x000020

#include <ffi/ffi.h>

NS_ASSUME_NONNULL_BEGIN

/*!
 * @typedef PyObjC_CallFunc
 * @param meth A selector object
 * @param self The self argument
 * @param args The other arguments
 * @result Returns the return value, or NULL if an exception occurred
 */
typedef PyObject* _Nullable (*PyObjC_CallFunc)(PyObject* meth, PyObject* self,
                                               PyObject* _Nonnull const* _Nonnull args,
                                               size_t nargs);

typedef struct {
    PyObject_HEAD
    const char* sel_python_signature;
    const char* _Nullable sel_native_signature; /* XXX: Make _Nonnull */
    SEL sel_selector;
    PyObject* _Nullable sel_self;
    Class _Nullable sel_class;
    int sel_flags;
    PyObjCMethodSignature* _Nullable sel_methinfo;
    Py_ssize_t sel_mappingcount;
#if PY_VERSION_HEX >= 0x03090000
    vectorcallfunc sel_vectorcall;
#endif
} PyObjCSelector;

typedef struct {
    PyObjCSelector base;
    PyObjC_CallFunc _Nullable sel_call_func;
    ffi_cif* _Nullable sel_cif;
} PyObjCNativeSelector;

typedef struct {
    PyObjCSelector base;
    PyObject*      callable;
    Py_ssize_t     argcount;
    Py_ssize_t     numoutput; /* XXX: To be removed, only set and never read */
} PyObjCPythonSelector;

extern PyObject* PyObjCSelector_Type;
extern PyObject* PyObjCNativeSelector_Type;
extern PyObject* PyObjCPythonSelector_Type;
#define PyObjCSelector_Check(obj)                                                        \
    PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCSelector_Type)
#define PyObjCNativeSelector_Check(obj)                                                  \
    PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCNativeSelector_Type)
#define PyObjCPythonSelector_Check(obj)                                                  \
    PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCPythonSelector_Type)

extern PyObject* _Nullable PyObjCSelector_Copy(PyObject* obj);
extern const char* _Nullable PyObjCSelector_Signature(PyObject* obj);
#define PyObjCSelector_GetNativeSignature(obj)                                           \
    (((PyObjCSelector*)obj)->sel_native_signature)
extern SEL PyObjCSelector_GetSelector(PyObject* obj);
extern int PyObjCSelector_GetFlags(PyObject* obj);
extern Class _Nullable PyObjCSelector_GetClass(PyObject* obj);
extern int PyObjCSelector_Required(PyObject* obj);
extern int PyObjCSelector_IsClassMethod(PyObject* obj);
extern int PyObjCSelector_IsHidden(PyObject* obj);
extern PyObjCMethodSignature* _Nullable PyObjCSelector_GetMetadata(PyObject* _self);
extern PyObject* _Nullable PyObjCSelector_NewNative(Class class, SEL selector,
                                                    const char* signature,
                                                    int         class_method);
extern PyObject* _Nullable PyObjCSelector_FindNative(PyObject* self, const char* name);

#define PyObjCSelector_GET_CLASS(obj) (((PyObjCSelector*)(obj))->sel_class)
#define PyObjCSelector_GET_SELECTOR(obj) (((PyObjCSelector*)(obj))->sel_selector)
#define PyObjCSelector_GET_CIF(obj) (((PyObjCNativeSelector*)(obj))->sel_cif)
#define PyObjCSelector_SET_CIF(obj, cif) (((PyObjCNativeSelector*)(obj))->sel_cif = (cif))

extern PyObject* _Nullable PyObjCSelector_New(PyObject* callable, SEL selector,
                                              const char* _Nullable signature,
                                              int class_method, Class _Nullable class);
extern SEL PyObjCSelector_DefaultSelector(const char* methname);

extern int PyObjCSelector_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_SELECTOR_H */
