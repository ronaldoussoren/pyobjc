#ifndef PyObjC_RUNTIME_COMPAT
#define PyObjC_RUNTIME_COMPAT
/*
 * Objective-C 2.x runtime compatibility.
 *
 * Special:
 *  - PyObjC_class_addMethodList is not a function in the ObjC 2.0 runtime API,
 *    but added here to (a) get semantics that are slightly nicer for what
 *    we do and (b) can be implemented efficiently on the "1.0" runtime.
 *  - Modifying a created but not yet registered class should be done using
 *    the preclass_* functions, not the regular ones because it isn't possible
 *    to emulate the entire ObjC 2.0 API on Tiger.
 */
#include <objc/Protocol.h>
#include <objc/objc-runtime.h>

NS_ASSUME_NONNULL_BEGIN

struct PyObjC_method {
    SEL         name;
    IMP         imp;
    const char* type;
};

#define _C_IN 'n'
#define _C_INOUT 'N'
#define _C_OUT 'o'
#define _C_ONEWAY 'V'
#define _C_BYCOPY 'O'
#define _C_BYREF 'R'

/* From the clang sources...
 *  Both are a prefix for a basic type
 */
#define _C_ATOMIC 'A'
#define _C_COMPLEX 'j' /* XXX: Requires more work to support */

#ifndef _C_LNG_DBL
#define _C_LNG_DBL 'D'
#endif

/* These don't actually exist in the Objective-C runtime, but are used
 * by the bridge to simplify code.
 */
#define _C_UNICHAR 'T'
#define _C_CHAR_AS_TEXT 't'
#define _C_CHAR_AS_INT 'z'
#define _C_NSBOOL 'Z'

/*
 * Vector/maxtrix types don't have a representation
 * in type encoding. PyObjC uses the following convention:
 *
 * vector_float2:  <2f>
 * matrix_float3x3: <3,3f>
 *
 * These encodings are only used for signature-specific
 * dispatching, libffi does not support these types
 */
#define _C_VECTOR_B '<'
#define _C_VECTOR_E '>'

/* Some functions that are missing (oddly enough) */
BOOL PyObjC_class_isSubclassOf(Class child, Class parent);

extern BOOL PyObjC_class_addMethodList(Class, struct PyObjC_method*, unsigned int);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_RUNTIME_COMPAT */
