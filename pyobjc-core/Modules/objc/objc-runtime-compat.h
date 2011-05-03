#ifndef PyObjC_RUNTIME_COMPAT
#define PyObjC_RUNTIME_COMPAT
/*
 * Objective-C 2.0 runtime compatibility.
 *
 * This files makes it possible to use the Objective-C 2.0 API on versions
 * of Mac OS X before 10.5. Use PyObjC_FUNCNAME to access FUNCNAME from the 
 * Objective-C 2.0 API, see the Objective-C 2.0 runtime documentation to see
 * how it should be used.
 *
 * TODO: 
 * - completely move PyObjC to the Objective-C 2.0 API
 * - add more wizardry to ensure that this code compiles on OSX 10.4
 *
 * Special:
 *  - PyObjC_class_addMethodList is not a function in the ObjC 2.0 runtime API,
 *    but added here to (a) get semantics that are slightly nicer for what
 *    we do and (b) can be implemented efficiently on the "1.0" runtime.
 *  - PyObjC_methodlist_magic is meant to be used to determine if a class has
 *    changed in some way (such by loading a category). 
 *  - Modifying a created but not yet registered class should be done using
 *    the preclass_* functions, not the regular ones because it isn't possible
 *    to emulate the entire ObjC 2.0 API on Tiger.
 */
#include <objc/objc-runtime.h>
#include <objc/Protocol.h>

#define _C_CONST    'r'
#define _C_IN       'n'
#define _C_INOUT    'N'
#define _C_OUT      'o'
#define _C_BYCOPY   'O'
#define _C_BYREF   'R'
#define _C_ONEWAY   'V'
#define _C_LNG_LNG   'q'
#define _C_ULNG_LNG  'Q'
#define _C_BOOL     'B'         /* (Objective-)C++ 'bool' */


/* These don't actually exist in the Objective-C runtime, but are used
 * by the bridge to simplify code.
 */
#define _C_UNICHAR	'T'
#define _C_CHAR_AS_TEXT 't'
#define _C_CHAR_AS_INT	'z'
#define _C_NSBOOL	'Z'

struct PyObjC_method {
	SEL	    name;
	IMP	    imp;
	const char* type;
};

#define objc_superSetReceiver(super, val) (super).receiver = (val)
#define objc_superGetReceiver(super) ((super).receiver)

#ifdef __OBJC2__

#define objc_superSetClass(super, cls) (super).super_class = (cls)
#define objc_superGetClass(super) ((super).super_class)

#else

#define objc_superSetClass(super, cls) (super).class = (cls)
#define objc_superGetClass(super) ((super).class)

#endif

/* Some functions that are missing (oddly enough) */
BOOL PyObjC_class_isSubclassOf(Class child, Class parent);
#define class_isSubclassOf PyObjC_class_isSubclassOf

#if (MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5)  && !defined(__OBJC2__)

#define preclass_addIvar		PyObjC_preclass_addIvar
#define preclass_addMethod		PyObjC_preclass_addMethod
#define preclass_addProtocol		PyObjC_preclass_addProtocol

extern void PyObjC_SetupRuntimeCompat(void);

extern BOOL (*PyObjC_preclass_addMethod)(Class, SEL, IMP, const char*);
extern BOOL (*PyObjC_preclass_addIvar)(Class cls, 
		const char *name, size_t size, uint8_t alignment, 
		const char *types);
extern BOOL (*PyObjC_preclass_addProtocol)(Class cls, Protocol *protocol);


extern Class (*PyObjC_objc_allocateClassPair)(Class, const char*, size_t);
extern void (*PyObjC_objc_registerClassPair)(Class);
extern void (*PyObjC_objc_disposeClassPair)(Class cls);


extern Class (*PyObjC_object_getClass)(id obj);
extern Class (*PyObjC_object_setClass)(id obj, Class cls);
extern const char* (*PyObjC_object_getClassName)(id obj);

extern Method* (*PyObjC_class_copyMethodList)(Class, unsigned int*);
extern const char* (*PyObjC_class_getName)(Class);
extern Class (*PyObjC_class_getSuperclass)(Class);
extern BOOL (*PyObjC_class_addMethod)(Class, SEL, IMP, const char*);
extern BOOL (*PyObjC_class_addMethodList)(Class, 
		struct PyObjC_method*, unsigned int);
extern Ivar* (*PyObjC_class_copyIvarList)(Class, unsigned int*);
extern Protocol** (*PyObjC_class_copyProtocolList)(Class, unsigned int*);

extern BOOL (*PyObjC_class_isMetaClass)(Class);

extern SEL (*PyObjC_method_getName)(Method m);
extern const char *(*PyObjC_method_getTypeEncoding)(Method m);
extern IMP (*PyObjC_method_getImplementation)(Method m);
extern IMP (*PyObjC_method_setImplementation)(Method m, IMP imp);

extern BOOL (*PyObjC_sel_isEqual)(SEL, SEL);

extern size_t (*PyObjC_methodlist_magic)(Class cls);

extern const char*  (*PyObjC_ivar_getName)(Ivar);
extern const char*  (*PyObjC_ivar_getTypeEncoding)(Ivar);
extern ptrdiff_t    (*PyObjC_ivar_getOffset)(Ivar);

extern Protocol** (*PyObjC_objc_copyProtocolList)(unsigned int* outCount);
extern Protocol*  (*PyObjC_objc_getProtocol)(char* name);
extern struct objc_method_description_list* (*PyObjC_protocol_copyInstanceMethodDescriptionList)(Protocol* proto);
extern struct objc_method_description_list* (*PyObjC_protocol_copyClassMethodDescriptionList)(Protocol *proto);
extern struct objc_method_description_list* (*PyObjC_protocol_copyOptionalInstanceMethodDescriptionList)(Protocol *proto);
extern struct objc_method_description_list* (*PyObjC_protocol_copyOptionalClassMethodDescriptionList)(Protocol *proto);

extern BOOL (*PyObjC_protocol_conformsToProtocol)(Protocol *proto, Protocol *other);
extern const char *(*PyObjC_protocol_getName)(Protocol *p);
extern struct objc_method_description *(*PyObjC_protocol_copyMethodDescriptionList)(Protocol *p, BOOL isRequiredMethod, BOOL isInstanceMethod, unsigned int *outCount);
extern Protocol **(*PyObjC_protocol_copyProtocolList)(Protocol *proto, unsigned int *outCount);
extern struct objc_method_description (*PyObjC_protocol_getMethodDescription)(Protocol *p, SEL aSel, BOOL isRequiredMethod, BOOL isInstanceMethod);

extern id (*PyObjC_object_getIvar)(id obj, Ivar ivar);
extern void (*PyObjC_object_setIvar)(id obj, Ivar ivar, id value);

#ifndef PYOBJC_COMPAT_IMPL
#define object_getIvar			PyObjC_object_getIvar
#define object_setIvar			PyObjC_object_setIvar
#define protocol_getName		PyObjC_protocol_getName
#define protocol_conformsToProtocol     PyObjC_protocol_conformsToProtocol
#define protocol_copyMethodDescriptionList PyObjC_protocol_copyMethodDescriptionList
#define protocol_copyProtocolList	PyObjC_protocol_copyProtocolList
#define protocol_getMethodDescription   PyObjC_protocol_getMethodDescription

#define objc_allocateClassPair		PyObjC_objc_allocateClassPair
#define objc_registerClassPair		PyObjC_objc_registerClassPair
#define objc_disposeClassPair		PyObjC_objc_disposeClassPair

#define object_getClass 		PyObjC_object_getClass
#define object_setClass 		PyObjC_object_setClass
#define object_getClassName		PyObjC_object_getClassName

#define class_copyMethodList 		PyObjC_class_copyMethodList
#define class_getName 			PyObjC_class_getName
#define class_getSuperclass 		PyObjC_class_getSuperclass
#define class_addMethod	 		PyObjC_class_addMethod
#define class_addMethodList		PyObjC_class_addMethodList
#define class_copyIvarList		PyObjC_class_copyIvarList
#define class_copyProtocolList		PyObjC_class_copyProtocolList
#define class_conformsToProtocol	PyObjC_class_conformsToProtocol
#define class_isMetaClass		PyObjC_class_isMetaClass

#define method_getName 			PyObjC_method_getName
#define method_getTypeEncoding   	PyObjC_method_getTypeEncoding
#define method_getImplementation 	PyObjC_method_getImplementation
#define method_setImplementation 	PyObjC_method_setImplementation

#define sel_isEqual			PyObjC_sel_isEqual

#define ivar_getName			PyObjC_ivar_getName
#define ivar_getTypeEncoding		PyObjC_ivar_getTypeEncoding
#define ivar_getOffset			PyObjC_ivar_getOffset

#define objc_copyProtocolList 					PyObjC_objc_copyProtocolList
#define objc_getProtocol 					PyObjC_objc_getProtocol
#define protocol_copyInstanceMethodDescriptionList 		PyObjC_protocol_copyInstanceMethodDescriptionList
#define protocol_copyClassMethodDescriptionList 		PyObjC_protocol_copyClassMethodDescriptionList
#define protocol_copyOptionalInstanceMethodDescriptionList	PyObjC_protocol_copyOptionalInstanceMethodDescriptionList
#define protocol_copyOptionalClassMethodDescriptionList 	PyObjC_protocol_copyOptionalClassMethodDescriptionList

#endif /* !PYOBJC_COMPAT_IMPL */

#else

/*
 * Compiled for 10.5 or later, use ObjC 2.0 runtime exclusively.
 *
 *
 * Use the preclass_ versions to modify a Class between allocating it and
 * registering it. This is needed for the 10.4 compatibility layer.
 */

#define preclass_addIvar		class_addIvar
#define preclass_addMethod		class_addMethod
#define preclass_addProtocol		class_addProtocol

static inline void PyObjC_SetupRuntimeCompat(void) { }
extern BOOL PyObjC_class_addMethodList(Class class, 
		struct PyObjC_method* list, unsigned int count);


extern size_t PyObjC_methodlist_magic(Class cls);

#define class_addMethodList	PyObjC_class_addMethodList


#endif


#endif /* PyObjC_RUNTIME_COMPAT */
