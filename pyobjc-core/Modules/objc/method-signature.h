#ifndef PyObjC_METHODSIGNATURE_H
#define PyObjC_METHODSIGNATURE_H
#include "pyobjc.h"

extern PyTypeObject PyObjCMethodSignature_Type;
#define PyObjCMethodSignature_Check(obj) PyObject_TypeCheck(obj, &PyObjCMethodSignature_Type)

enum _PyObjC_PointerType
#if __has_feature(objc_fixed_enum)
	: unsigned char
#endif /* __has_feature(objc_fixed_enum) */
{
    PyObjC_kPointerPlain = 0,
    PyObjC_kNullTerminatedArray = 1,
    PyObjC_kArrayCountInArg = 2,
    PyObjC_kFixedLengthArray = 3,
    PyObjC_kVariableLengthArray = 4,
};

typedef struct _PyObjCMethodSignature PyObjCMethodSignature;

struct _PyObjC_ArgDescr {
    /* If typeOverride the type field should be freed when the descriptor
     * is cleaned up, otherwise is isn't owned by this descriptor.
     */
    const char* type;
    PyObjCMethodSignature* callable;

    const char* sel_type;
    int16_t arrayArg;
    int16_t arrayArgOut;
    enum _PyObjC_PointerType ptrType:3;
    unsigned int allowNULL:1;
    unsigned int typeOverride:1;
    unsigned int arraySizeInRetval:1;
    unsigned int printfFormat:1;
    unsigned int alreadyRetained:1;
    unsigned int alreadyCFRetained:1;
    unsigned int callableRetained:1; /* False iff the closure can be cleaned up after the call */
};

struct _PyObjCMethodSignature {
    PyObject_VAR_HEAD

    const char* signature;
    unsigned char variadic:1;
    unsigned char null_terminated_array:1;
    unsigned char free_result:1;
    unsigned char shortcut_signature:1;
    unsigned int shortcut_argbuf_size:12;
    int16_t arrayArg;
    PyObject* suggestion;
    struct _PyObjC_ArgDescr rettype;
    struct _PyObjC_ArgDescr argtype[1];
};


extern PyObjCMethodSignature* PyObjCMethodSignature_WithMetaData(
    const char* signature, PyObject* metadata, BOOL is_native);

extern PyObjCMethodSignature* PyObjCMethodSignature_ForSelector(
    Class cls, BOOL isClassMethod, SEL sel, const char* signature, BOOL is_native);

extern char*
PyObjC_NSMethodSignatureToTypeString(
    NSMethodSignature* sig, char* buf, size_t buflen);

extern int
PyObjC_registerMetaData(PyObject*, PyObject*, PyObject*);

extern PyObject*
PyObjCMethodSignature_AsDict(PyObjCMethodSignature* methinfo);

#define PyObjCMethodSignature_FromSignature(sig, is_native) \
	PyObjCMethodSignature_WithMetaData((sig), NULL, (is_native))

#endif /* PyObjC_METHODSIGNATURE_H */
