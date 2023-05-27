#ifndef PyObjC_METHODSIGNATURE_H
#define PyObjC_METHODSIGNATURE_H
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

#define SHORTCUT_MAX_ARGBUF 512

extern PyObject* PyObjCMethodSignature_Type;
#define PyObjCMethodSignature_Check(obj)                                                 \
    PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCMethodSignature_Type)

enum _PyObjC_PointerType
#if __has_feature(objc_fixed_enum)
    : unsigned char
#endif /* __has_feature(objc_fixed_enum) */
{
    PyObjC_kPointerPlain        = 0,
    PyObjC_kNullTerminatedArray = 1,
    PyObjC_kArrayCountInArg     = 2,
    PyObjC_kFixedLengthArray    = 3,
    PyObjC_kVariableLengthArray = 4,
    PyObjC_kDerefResultPointer  = 5,
};

typedef struct _PyObjCMethodSignature PyObjCMethodSignature;

struct _PyObjC_ArgDescr {
    /* If typeOverride the type field should be freed when the descriptor
     * is cleaned up, otherwise is isn't owned by this descriptor.
     */
    const char* _Nullable type;
    PyObjCMethodSignature* _Nullable callable;

    const char* _Nullable sel_type;
    char                     modifier;
    int16_t                  arrayArg;
    int16_t                  arrayArgOut;
    enum _PyObjC_PointerType ptrType : 3;
    unsigned int             allowNULL : 1;
    unsigned int             typeOverride : 1;
    unsigned int             arraySizeInRetval : 1;
    unsigned int             printfFormat : 1;
    unsigned int             alreadyRetained : 1;
    unsigned int             alreadyCFRetained : 1;
    unsigned int
        callableRetained : 1; /* False iff the closure can be cleaned up after the call */
    unsigned int tmpl : 1;
};

struct _PyObjCMethodSignature {
    PyObject_VAR_HEAD

        const char* signature;
    PyObject* _Nullable suggestion;
    unsigned char            variadic : 1;
    unsigned char            null_terminated_array : 1;
    unsigned char            free_result : 1;
    unsigned char            shortcut_signature : 1;
    unsigned int             shortcut_argbuf_size : 10;
    unsigned int             shortcut_result_size : 8;
    int16_t                  arrayArg;
    int                      deprecated;
    struct _PyObjC_ArgDescr* rettype;
    struct _PyObjC_ArgDescr* _Nonnull argtype[1]; /* XXX: [1] to be replaced by [] */
};

extern PyObjCMethodSignature* _Nullable PyObjCMethodSignature_WithMetaData(
    const char* signature, PyObject* _Nullable metadata, BOOL is_native);

extern PyObjCMethodSignature* _Nullable PyObjCMethodSignature_ForSelector(
    Class cls, BOOL isClassMethod, SEL sel, const char* signature, BOOL is_native);

extern char* _Nullable PyObjC_NSMethodSignatureToTypeString(NSMethodSignature* sig,
                                                            char* buf, size_t buflen);

extern int PyObjC_registerMetaData(PyObject*, PyObject*, PyObject*);

extern PyObject* _Nullable PyObjC_copyMetadataRegistry(void);

extern PyObject* _Nullable PyObjCMethodSignature_AsDict(PyObjCMethodSignature* methinfo);

#ifdef PyObjC_DEBUG

/* XXX: Is this used? */
static inline int
PyObjCMethodSignature_Validate(PyObjCMethodSignature* methinfo)
{
    PyObjC_Assert(methinfo->signature != NULL, -1);
    for (Py_ssize_t i = 0; i < Py_SIZE(methinfo); i++) {
        PyObjC_Assert(methinfo->argtype[i] != NULL, -1);
        PyObjC_Assert(methinfo->argtype[i]->type != NULL, -1);
    }
    PyObjC_Assert(methinfo->rettype != NULL, -1);
    PyObjC_Assert(methinfo->rettype->type != NULL, -1);
    return 0;
}
#endif /* PyObjC_DEBUG */

extern PyObjCMethodSignature* PyObjCMethodSignature_GetRegistered(Class cls, SEL sel);

extern int PyObjCMethodSignature_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_METHODSIGNATURE_H */
