/*
 * Objective-C runtime 2.0 compatibility for MacOS X 10.4 and earlier.
 *
 * This code works by poking into the ObjC runtime, which means loads of 
 * warnings on 10.5+ ;-)
 */

#define PYOBJC_COMPAT_IMPL
#include "pyobjc.h"




#if (MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5) &&!defined(__OBJC2__)

BOOL PyObjC_class_isSubclassOf(Class child, Class parent)
{
	if (parent == nil) return YES;

	while (child != nil) {
		if (child == parent) {
			return YES;
		}
		child = PyObjC_class_getSuperclass(child);
	}
	return NO;
}

#import <mach-o/dyld.h>
#import <mach-o/getsect.h>
#import <mach-o/loader.h>

typedef struct _ProtocolTemplate { @defs(Protocol) } ProtocolTemplate;



struct objc10_object {
	Class	isa;
};

struct PyObjC_ivar {
	char* name;
	size_t size;
	uint8_t alignment;
	char* types;
};


static Protocol** compat_objc_copyProtocolList(unsigned int* outCount)
{
	Protocol** protocols = NULL;
	*outCount = 0;

	uint32_t image_count, image_index;
	image_count = _dyld_image_count();
	for (image_index = 0; image_index < image_count; image_index++) {
		uint32_t size = 0;
		const struct mach_header *mh = _dyld_get_image_header(image_index);
		intptr_t slide = _dyld_get_image_vmaddr_slide(image_index);
		ProtocolTemplate *protos = (ProtocolTemplate*)(
			((char *)getsectdatafromheader(mh, SEG_OBJC, "__protocol", &size)) +
			slide);
		uint32_t nprotos = size / sizeof(ProtocolTemplate);
		uint32_t i;

		if (nprotos == 0) continue;

		if (protocols == NULL) {
			protocols = malloc(sizeof(Protocol*) * nprotos);
			if (protocols == NULL) {
				return NULL;
			}
		} else {
			Protocol** tmp = realloc(protocols,
				sizeof(Protocol*) * (*outCount+nprotos));
			if (tmp == NULL) {
				free(protocols);
				return NULL;
			}
			protocols = tmp;
		}

		for (i = 0; i < nprotos; i++) {
			protocols[(*outCount)++] = (Protocol*)&protos[i];
		}
	}
	return protocols;
}

static Protocol*  compat_objc_getProtocol(const char* name)
{
	uint32_t image_count, image_index;
	image_count = _dyld_image_count();
	for (image_index = 0; image_index < image_count; image_index++) {
		uint32_t size = 0;
		const struct mach_header *mh = _dyld_get_image_header(image_index);
		intptr_t slide = _dyld_get_image_vmaddr_slide(image_index);
		ProtocolTemplate *protos = (ProtocolTemplate*)(
			((char *)getsectdatafromheader(mh, SEG_OBJC, "__protocol", &size)) +
			slide);
		uint32_t nprotos = size / sizeof(ProtocolTemplate);
		uint32_t i;

		if (nprotos == 0) continue;

		for (i = 0; i < nprotos; i++) {
			Protocol* p = (Protocol*)&protos[i];
			if (strcmp([p name], name) == 0) {
				return p;
			}
		}
	}
	return nil;
}


static void
compat_objc_registerClassPair(Class cls)
{
	struct objc_method_list* list;

	/* Add the list in the official way, just in case class_addMethods
	 * does something special.
	 */
	list = cls->methodLists[0];
	cls->methodLists[0] = (struct objc_method_list*)-1;
	class_addMethods(cls, list);

	list = cls->isa->methodLists[0];
	cls->isa->methodLists[0] = (struct objc_method_list*)-1;
	class_addMethods(cls->isa, list);

	objc_addClass(cls);
}

static Class
compat_objc_allocateClassPair(Class super_class, const char* name, size_t extra)
{
	struct objc_class* result;
	Class root_class;

	if (objc_getClass(name)) {
		return Nil;
	}

	root_class = super_class;
	while (root_class->super_class) {
		root_class = root_class->super_class;
	}
	
	result = malloc(sizeof(struct objc_class) * 2 + extra);
	if (result == NULL) {
		return Nil;
	}
	memset(result, 0, sizeof(struct objc_class) * 2 + extra);

	result->super_class = super_class;
	result->isa = result + 1;

	result[0].methodLists = NULL;
	result[1].methodLists = NULL;

	result[0].info = CLS_CLASS;
	result[1].info = CLS_META;

	result[0].name = strdup(name);
	if (result[0].name == NULL) goto error_cleanup;

	result[1].name = result[0].name;
	result[0].methodLists = malloc(sizeof(struct objc_method_list*));
	if (result[0].methodLists == NULL) goto error_cleanup;
	memset(result[0].methodLists, 0, sizeof(struct objc_method_list*));

	result[1].methodLists = malloc(sizeof(struct objc_method_list*));
	if (result[1].methodLists == NULL) goto error_cleanup;
	memset(result[1].methodLists, 0, sizeof(struct objc_method_list*));

	/*
	 * This is MacOS X specific, and an undocumented feature (long live
	 * Open Source!).
	 *
	 * The code in the objc runtime assumes that the method lists are
	 * terminated by '-1', and will happily overwite existing data if
	 * they aren't.
	 *
	 * Ronald filed a bugreport for this: Radar #3317376
	 */
	result[0].methodLists[0] = (struct objc_method_list*)-1;
	result[1].methodLists[0] = (struct objc_method_list*)-1;

	result[0].methodLists[0] = malloc(sizeof(struct objc_method_list));
	if (result[0].methodLists[0] == NULL) goto error_cleanup;
	result[0].methodLists[0]->method_count = 0;
	result[0].methodLists[0]->obsolete = NULL;

	result[1].methodLists[0] = malloc(sizeof(struct objc_method_list));
	if (result[1].methodLists[0] == NULL) goto error_cleanup;
	result[1].methodLists[0]->method_count = 0;
	result[1].methodLists[0]->obsolete = NULL;


	result[0].super_class = super_class;
	result[1].super_class = ((struct objc10_object*)super_class)->isa;
	result[1].isa = ((struct objc10_object*)root_class)->isa;

	result[0].instance_size = super_class->instance_size;
	result[1].instance_size = result[1].super_class->instance_size;

	/* Initialize to NULL, otherwise poseAs: won't work */
	result[0].ivars = result[1].ivars = NULL;

	result[0].protocols = result[1].protocols = NULL;

	return result;


error_cleanup:
	if (result) {
		if (result[0].methodLists) {
			if (result[0].methodLists[0] != 0 &&
					result[0].methodLists[0] != 0)  {
				free(result[0].methodLists[0]);
			}
			free(result[0].methodLists);
		}
		if (result[1].methodLists) {
			if (result[1].methodLists[1] != 0 &&
					result[1].methodLists[0] != 0)  {
				free(result[1].methodLists[0]);
			}
			free(result[1].methodLists);
		}

		if (result[0].ivars) {
			free(result[0].ivars);
		}
		if (result[1].ivars) {
			free(result[1].ivars);
		}

		if (result[0].name) {
			free((char*)result[0].name);
		}
		free(result);
	}
	return Nil;

}

static void
compat_objc_disposeClassPair(Class cls)
{
	struct objc_class* val = cls;
	int i;

	for (i = 0; i < 2; i++) {
		if (val[i].methodLists) {
			struct objc_method_list** cur;

			cur = val[i].methodLists;
			if (*cur != (struct objc_method_list*)-1) {
				free(*cur);
				*cur = NULL;
			}
			free(val[i].methodLists);
			val[i].methodLists = NULL;
		}
	}

	free((char*)val[0].name);
	val[0].name = val[1].name = NULL;
	free(val);
}


static size_t 
compat_methodlist_magic(Class cls)
{
	void* iterator = NULL;
	struct objc_method_list* mlist;
	size_t res = 0, cnt = 0;

        if (cls == NULL) return -1;

	while ( (mlist = class_nextMethodList(cls, &iterator )) != NULL ) {
		res += mlist->method_count;
		cnt++;
	}

	return (cnt << 16) | (res & 0xFFFF);
}

#ifndef NO_OBJC2_RUNTIME
static size_t 
objc20_methodlist_magic(Class cls)
{
	Method* methods;
	unsigned int count;
	unsigned int i;
	size_t result;

	methods = class_copyMethodList(cls, &count);
	result = 0;
	for (i = 0; i < count; i++) {
		result = (1000003*result) ^ ((size_t)(
				method_getImplementation(methods[i])) >> 3);
	}
	result = result | (count << 16);
	free(methods);
	return result;
}
#endif

static Class 
compat_object_setClass(id obj, Class cls)
{
	Class prev;
	if (obj == nil) {
		return Nil;
	}
	prev = ((struct objc10_object*)obj)->isa;
	((struct objc10_object*)obj)->isa = cls;
	return prev;
}



static Class 
compat_object_getClass(id obj)
{
	return ((struct objc10_object*)obj)->isa;
}

static const char*
compat_object_getClassName(id obj)
{
	return ((struct objc10_object*)obj)->isa->name;
}



static Method* 
compat_class_copyMethodList(Class cls, unsigned int* outCount)
{
	struct objc_method_list* mlist;
	void* iterator; 
	unsigned int count;
	Method* result;
	Method* tmp;
	
	iterator = NULL;
	count = 0;

	mlist = class_nextMethodList(cls, &iterator);
	result = NULL;
	while (mlist != NULL) {
		int i;

		tmp = realloc(result, (count + mlist->method_count) * sizeof(Method));
		if (tmp == NULL) {
			free(result);
			return NULL;
		} else {
			result = tmp;
		}

		for (i = 0; i < mlist->method_count; i++) {
			result[count] = mlist->method_list + i;
			if (result[count] == NULL) continue;
			count++;
		}
		mlist = class_nextMethodList(cls, &iterator);
	}

	if (outCount != NULL) {
		*outCount = count;
	}
	return result;
}

static Ivar*
compat_class_copyIvarList(Class cls, unsigned int* outCount)
{
	Ivar* list;
	int   i;
	struct objc_ivar_list* ivars = cls->ivars;

	if (ivars) {
		list = malloc(sizeof(Ivar) * ivars->ivar_count);
		if (list == NULL) {
			return NULL;
		}
	

		for (i = 0; i < ivars->ivar_count; i++) {
			list[i] = ivars->ivar_list + i;
		}
		*outCount = ivars->ivar_count;
		return list;

	} else {
		list = malloc(1);
		if (list == NULL) {
			return NULL;
		}

		*outCount = 0;
		return list;
	}

}

static Protocol**
compat_class_copyProtocolList(Class cls, unsigned int* outCount)
{
	Protocol** list;
	unsigned int count = 0;
	struct objc_protocol_list *protocol_list;

	protocol_list = cls->protocols;
	list = malloc(0);

	while (protocol_list != NULL) {
		list = realloc(list, (count + protocol_list->count)*sizeof(Protocol*));
		if (list == NULL) {
			/* Whoops, memory leak */
			*outCount = 0;
			return NULL;
		}
		memcpy(list + count, protocol_list->list, protocol_list->count*sizeof(Protocol*));
		count += protocol_list->count;
		protocol_list = protocol_list->next;
	}

	*outCount = count;
	return list;
}


static const char* 
compat_class_getName(Class cls)
{
	return cls->name;
}

static Class 
compat_class_getSuperclass(Class cls)
{
	return cls->super_class;
}

static BOOL 
compat_class_addMethod(Class cls, SEL name, IMP imp, const char* types)
{
	struct objc_method_list* methodsToAdd;
	struct objc_method* objcMethod;

	methodsToAdd = malloc(sizeof(struct objc_method_list) +
			2*sizeof(struct objc_method));
	methodsToAdd->method_count = 1;
	methodsToAdd->obsolete = NULL;

	objcMethod = methodsToAdd->method_list;
	objcMethod->method_name = name;
	objcMethod->method_imp = imp;
	objcMethod->method_types = (char*)types;

	class_addMethods(cls, methodsToAdd);
	return YES; /* Have to return something ... */
}

static BOOL 
compat_preclass_addMethod(Class cls, SEL name, IMP imp, const char* types)
{
	/* Resize in-place, this is only valid during class construction. */
	struct objc_method_list* new_list;
	struct objc_method* objcMethod;

	new_list = realloc(cls->methodLists[0],
			sizeof(struct objc_method_list) +
			(sizeof(struct objc_method
				)*(cls->methodLists[0]->method_count+1)));
	if (new_list == NULL) {
		return NO;
	}
	cls->methodLists[0] = new_list;
	objcMethod = new_list->method_list + (new_list->method_count)++;

	objcMethod->method_name = name;
	objcMethod->method_imp = imp;
	objcMethod->method_types = strdup(types);
	if (objcMethod == NULL) {
		new_list->method_count--;
		return NO;
	}

	return YES;
}

static BOOL
compat_preclass_addIvar(
		Class cls, 
		const char* name, 
		size_t size, 
		uint8_t align, const char* types)
{
	/* Update the class structure, only valid during class construction */
	struct objc_ivar_list* new_ivars;
	struct objc_ivar* ivar;

	if (cls->ivars) {
		new_ivars = realloc(cls->ivars, 
			sizeof(struct objc_ivar_list) + 
			((cls->ivars->ivar_count+1) * sizeof(struct objc_ivar)));
	} else {
		new_ivars = malloc( 
				sizeof(struct objc_ivar_list) + 
				sizeof(struct objc_ivar));
		new_ivars->ivar_count = 0;
	}
	if (new_ivars == NULL) {
		return NO;
	}
	cls->ivars = new_ivars;
	ivar = new_ivars->ivar_list + new_ivars->ivar_count;
	ivar->ivar_name = strdup(name);
	if (ivar->ivar_name == NULL) {
		return NO;
	}

	ivar->ivar_type = strdup(types);
	if (ivar->ivar_type == NULL) {
		free(ivar->ivar_name);
		return NO;
	}

	ivar->ivar_offset = cls->instance_size;
	if (ivar->ivar_offset % align) {
		ivar->ivar_offset += align - (ivar->ivar_offset % align);
	}

	new_ivars->ivar_count ++;
	cls->instance_size = ivar->ivar_offset + size;
	return YES;
}

static BOOL
compat_preclass_addProtocol(Class cls, Protocol* protocol)
{
	struct objc_protocol_list* protocols;

	if (cls->protocols) {
		protocols = realloc(cls->protocols,
			sizeof(struct objc_protocol_list) +
			  (sizeof(Protocol*)*(cls->protocols->count+1)));
	} else {
		protocols = malloc(sizeof(struct objc_protocol_list)
				+ sizeof(Protocol*));
		protocols->count = 0;
		protocols->next = NULL;
	}
	if (protocols == NULL) {
		return NO;
	}
	cls->protocols = protocols;
	protocols->list[protocols->count] = protocol;
	protocols->count++;
	return YES;
}
	
static SEL 
compat_method_getName(Method m) 
{
	return m->method_name;
}

static IMP 
compat_method_getImplementation(Method m)
{
	return m->method_imp;
}

static IMP 
compat_method_setImplementation(Method m, IMP imp)
{
	IMP result =  m->method_imp;
	m->method_imp = imp;
	return result;
}

static const char *
compat_method_getTypeEncoding(Method m)
{
	return m->method_types;
}

static BOOL 
compat_sel_isEqual(SEL lhs, SEL rhs)
{
	return lhs == rhs;
}

static const char*
compat_ivar_getName(Ivar var)
{
	return var->ivar_name;
}

static const char*
compat_ivar_getTypeEncoding(Ivar var)
{
	return var->ivar_type;
}

static ptrdiff_t
compat_ivar_getOffset(Ivar var)
{
	return var->ivar_offset;
}


#ifndef NO_OBJC2_RUNTIME
static BOOL 
objc20_class_addMethodList(Class cls,
		struct PyObjC_method* list, unsigned int count)
{
	unsigned int i;
	BOOL r;
	Method m;

	for (i = 0; i < count; i++) {
		r = class_addMethod(cls, 
			list[i].name, list[i].imp, list[i].type);
		if (!r) {
			m = class_getInstanceMethod(cls, list[i].name);
			if (m != NULL) {
				method_setImplementation(m, list[i].imp);
			} else {
				return NO;
			}
		}
	}
	return YES;
}
#endif

static BOOL
compat_class_isMetaClass(Class cls)
{
	return CLS_GETINFO(cls, CLS_META) == CLS_META;
}

static BOOL 
compat_class_addMethodList(Class cls,
		struct PyObjC_method* list, unsigned int count)
{
	unsigned int i;
	struct objc_method_list* method_list;

	method_list = malloc(
			sizeof(struct objc_method_list) +
			((count+1) * sizeof(struct objc_method)));
	if (method_list == NULL) {
		return NO;
	}
	memset(method_list, 0, 
			sizeof(struct objc_method_list) +
			((count+1) * sizeof(struct objc_method)));

	method_list->method_count = 0;
	method_list->obsolete = 0;

	for (i = 0; i < count; i++) {
		method_list->method_list[i].method_name = list[i].name;
		method_list->method_list[i].method_types = (char*)list[i].type;
		method_list->method_list[i].method_imp = list[i].imp;
	}
	method_list->method_count = count;
	class_addMethods(cls, method_list);
	return YES;
}

static BOOL 
compat_protocol_conformsToProtocol(Protocol *proto, Protocol *other)
{
	return [proto conformsTo:other];
}

static const char *
compat_protocol_getName(Protocol *p)
{
	return [p name];
}

static struct objc_method_description *
compat_protocol_copyMethodDescriptionList(Protocol *p, BOOL isRequiredMethod, BOOL isInstanceMethod, unsigned int *outCount)
{
	if (!isRequiredMethod) {
		*outCount = 0;
		return NULL;
	}

	struct objc_method_description_list* list;

	if (isInstanceMethod) {
		list = ((ProtocolTemplate*)p)->instance_methods;
	} else {
		list = ((ProtocolTemplate*)p)->class_methods;
	}

	if (list == NULL || list->count == 0) {
		*outCount = 0;
		return NULL;
	}

	*outCount = list->count;
	struct objc_method_description* result;

	result = malloc(sizeof(struct objc_method_description) * list->count);
	if (result == NULL) {
		return NULL;
	}

	int i;
	*outCount = 0;
	for (i = 0; i < list->count; i++) {
		if (list->list[i].name == NULL) continue;
		result[*outCount].name = list->list[i].name;
		result[*outCount].types = list->list[i].types;
		(*outCount)++;
	}
	return result;
}

static Protocol **
compat_protocol_copyProtocolList(Protocol *proto, unsigned int *outCount)
{
	struct objc_protocol_list* list = 
		((ProtocolTemplate*)proto)->protocol_list;

	*outCount = 0;
	
	struct objc_protocol_list* cur;
	for (cur = list; cur != NULL; cur = cur->next) {
		*outCount += cur->count;
	}

	Protocol** result = (Protocol**)malloc(sizeof(Protocol*) * *outCount);
	if (result == NULL) {
		return NULL;
	}

	unsigned curIdx = 0;
	for (cur = list; cur != NULL; cur = cur->next) {
		int i;
		for (i = 0; i < cur->count; i++) {
			if (cur->list[i] != NULL) {
				result[curIdx++] = cur->list[i];
			} else {
				*outCount--;
			}
		}
	}
	return result;
}

static struct objc_method_description 
compat_protocol_getMethodDescription(Protocol *p, SEL aSel, BOOL isRequiredMethod, BOOL isInstanceMethod)
{
static struct objc_method_description empty_description =  { NULL, NULL };
	if (!isRequiredMethod) {
		return empty_description;
	}

	struct objc_method_description* result;

	if (isInstanceMethod) {
		result = [p descriptionForInstanceMethod: aSel];
	} else {
		result = [p descriptionForClassMethod: aSel];
	}

	if (result == NULL) {
		return empty_description;
	} else {
		return *result;
	}
}

static id 
compat_object_getIvar(id obj, Ivar ivar)
{
	return *(id*)(((char*)obj) + ivar->ivar_offset);
}
static void 
compat_object_setIvar(id obj, Ivar ivar, id value)
{
	*(id*)(((char*)obj) + ivar->ivar_offset) = value;
}

/* Dispatch table */
BOOL (*PyObjC_protocol_conformsToProtocol)(Protocol *proto, Protocol *other) = NULL;
const char *(*PyObjC_protocol_getName)(Protocol *p) = NULL;
struct objc_method_description *(*PyObjC_protocol_copyMethodDescriptionList)(Protocol *p, BOOL isRequiredMethod, BOOL isInstanceMethod, unsigned int *outCount) = NULL;
Protocol **(*PyObjC_protocol_copyProtocolList)(Protocol *proto, unsigned int *outCount) = NULL;
struct objc_method_description (*PyObjC_protocol_getMethodDescription)(Protocol *p, SEL aSel, BOOL isRequiredMethod, BOOL isInstanceMethod) = NULL;

id (*PyObjC_object_getIvar)(id obj, Ivar ivar) = NULL;
void (*PyObjC_object_setIvar)(id obj, Ivar ivar, id value) = NULL;



Class (*PyObjC_objc_allocateClassPair)(Class, const char*, size_t) = NULL;
void (*PyObjC_objc_registerClassPair)(Class) = NULL;
void (*PyObjC_objc_disposeClassPair)(Class) = NULL;
Protocol** (*PyObjC_objc_copyProtocolList)(unsigned int*) = NULL;
Protocol*  (*PyObjC_objc_getProtocol)(const char* name) = NULL;

BOOL (*PyObjC_preclass_addMethod)(Class, SEL, IMP, const char*) = NULL;
BOOL (*PyObjC_preclass_addIvar)(Class cls, 
	const char *name, size_t size, uint8_t alignment,
	const char *types) = NULL;
BOOL (*PyObjC_preclass_addProtocol)(Class cls, Protocol *protocol) = NULL;


Class   (*PyObjC_object_getClass)(id obj) = NULL;
Class (*PyObjC_object_setClass)(id obj, Class cls) = NULL;
const char* (*PyObjC_object_getClassName)(id obj) = NULL;

Method* (*PyObjC_class_copyMethodList)(Class, unsigned int*) = NULL;
const char*  (*PyObjC_class_getName)(Class) = NULL;
Class (*PyObjC_class_getSuperclass)(Class) = NULL;
BOOL (*PyObjC_class_addMethod)(Class, SEL, IMP, const char*) = NULL;
BOOL (*PyObjC_class_addMethodList)(Class,
		struct PyObjC_method*, unsigned int) = NULL;
Ivar* (*PyObjC_class_copyIvarList)(Class, unsigned int*) = NULL;
Protocol** (*PyObjC_class_copyProtocolList)(Class, unsigned int*) = NULL;
BOOL (*PyObjC_class_isMetaClass)(Class) = NULL;

SEL (*PyObjC_method_getName)(Method m) = NULL;
IMP (*PyObjC_method_getImplementation)(Method m) = NULL;
IMP (*PyObjC_method_setImplementation)(Method m, IMP imp) = NULL;
const char *(*PyObjC_method_getTypeEncoding)(Method m) = NULL;

BOOL (*PyObjC_sel_isEqual)(SEL, SEL) = NULL;

size_t (*PyObjC_methodlist_magic)(Class cls);

const char*  (*PyObjC_ivar_getName)(Ivar) = NULL;
const char*  (*PyObjC_ivar_getTypeEncoding)(Ivar) = NULL;
ptrdiff_t    (*PyObjC_ivar_getOffset)(Ivar) = NULL;




#else


BOOL PyObjC_class_isSubclassOf(Class child, Class parent)
{
	if (parent == nil) return YES;

	while (child != nil) {
		if (child == parent) {
			return YES;
		}
		child = class_getSuperclass(child);
	}
	return NO;
}

BOOL PyObjC_class_addMethodList(Class cls,
		struct PyObjC_method* list, unsigned int count)
{
	unsigned int i;
	BOOL r;
	Method m;

	for (i = 0; i < count; i++) {
		/*
		 * XXX: First try class_addMethod, if that fails assume this is
		 * because the method already exists in the class.
		 * Strictly speaking this isn't correct, but this is the best
		 * we can do through the 2.0 API (see 4809039 in RADAR)
		 */
		r = class_addMethod(cls, 
			list[i].name, list[i].imp, list[i].type);
		if (!r) {
			m = class_getInstanceMethod(cls, list[i].name);
			if (m != NULL) {
				method_setImplementation(m, list[i].imp);
			} else {
				return NO;
			}
		}
	}
	return YES;
}

size_t PyObjC_methodlist_magic(Class cls)
{
	/* This is likely to be much slower than compat_methodlist_magic,
	 * but should works on the 64-bit runtime. Hopefully a callback will
	 * be added to the 2.0 runtime that will take away the need for this
	 * function...
	 */
	Method* methods;
	unsigned int count;

	methods = class_copyMethodList(cls, &count);
	free(methods);
	return (size_t)count;
}

#endif

#if defined(__x86_64__)

@implementation Protocol (NSOBjectCompat)
- (id)self
{
	return self;
}
@end

#if PyObjC_BUILD_RELEASE < 1008
@implementation Object (NSOBjectCompat)
- (id)self
{
	return self;
}

-doesNotRecognizeSelector:(SEL)sel
{
	printf("--> %s\n", sel_getName(sel));
	abort();
}
@end
#endif
	

#endif

#if (MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_7)
Protocol* (*PyObjC_objc_allocateProtocol)(const char *) = NULL;
void (*PyObjC_objc_registerProtocol)(Protocol*) = NULL;
void (*PyObjC_protocol_addMethodDescription)(Protocol*, SEL, const char*, BOOL, BOOL) = NULL;
void (*PyObjC_protocol_addProtocol)(Protocol*, Protocol*) = NULL;

#ifndef __LP64__
struct Protocol_struct {
	Class _isa;
	char *protocol_name;
	struct objc_protocol_list *protocol_list;
	struct objc_method_description_list *instance_methods, *class_methods;
	struct objc_method_description_list *optional_instance_methods, *optional_class_methods;
	void *instance_properties;
};

static Protocol* compat_objc_allocateProtocol(const char *name)
{
	struct Protocol_struct* result;

	result = (struct Protocol_struct*)NSAllocateObject([Protocol class], 0, NULL);
	if (result == NULL) {
		return NULL;
	}
	result->protocol_name = strdup(name);
	if (result->protocol_name == NULL) {
		/* Leaking object */
		return NULL;
	}
	result->protocol_list = NULL;
	result->instance_methods = NULL;
	result->class_methods = NULL;
	result->optional_instance_methods = NULL;
	result->optional_class_methods = NULL;
	result->instance_properties = NULL;
	return (Protocol*)result;
}

static void compat_objc_registerProtocol(Protocol* proto __attribute__((__unused__)))
{
	/* Don't know how to register a new protocol in classic
	 * runtime. Luckily we don't actually need this.
	 */
}

static void compat_protocol_addMethodDescription(Protocol* proto, SEL sel, const char* types, BOOL required, BOOL instance_method)
{
	struct Protocol_struct* proto_struct = (struct Protocol_struct*)proto;
	struct objc_method_description_list** plist;

	if (!instance_method) {
		if (required) {
			plist = &(proto_struct->class_methods);
		} else {
			plist = &(proto_struct->optional_class_methods);
		}
	} else {
		if (required) {
			plist = &(proto_struct->instance_methods);
		} else {
			plist = &(proto_struct->optional_instance_methods);
		}
	}

	if (*plist == NULL) {
		*plist = malloc(sizeof(struct objc_method_description_list) + (2*sizeof(struct objc_method_description)));
		if (*plist == NULL) {
			/* Cannot report errors */
			abort();
		}
		(*plist)->count = 0;
	} else {
		*plist = realloc(*plist, sizeof(struct objc_method_description_list) + (2+((*plist)->count)*sizeof(struct objc_method_description)));
		if (*plist == NULL) {
			/* Cannot report errors */
			abort();
		}
	}
	(*plist)->list[(*plist)->count].name = sel;
	(*plist)->list[(*plist)->count].types = strdup(types);
	if ((*plist)->list[(*plist)->count].types == NULL) {
		/* Cannot report errors */
		abort();
	}
	(*plist)->count++;

	(*plist)->list[(*plist)->count].name = NULL;
	(*plist)->list[(*plist)->count].types = NULL;
}

static void compat_protocol_addProtocol(Protocol* proto, Protocol* newProto)
{
	struct Protocol_struct* proto_struct = (struct Protocol_struct*)proto;

	if (proto_struct->protocol_list == NULL) {
		proto_struct->protocol_list = malloc(sizeof(struct objc_protocol_list) + 2*sizeof(Protocol*));
		if (proto_struct->protocol_list == NULL) {
			/* Cannot report an error! */
			abort();
		}
		proto_struct->protocol_list->next = NULL;
		proto_struct->protocol_list->count = 0;
	} else {
		proto_struct->protocol_list = realloc(proto_struct->protocol_list,
				sizeof(struct objc_protocol_list) + (2+proto_struct->protocol_list->count)*sizeof(Protocol*));
		if (proto_struct->protocol_list == NULL) {
			/* Cannot report an error! */
			abort();
		}
	}
	proto_struct->protocol_list->list[proto_struct->protocol_list->count] = newProto;
	proto_struct->protocol_list->list[proto_struct->protocol_list->count+1] = NULL;
	proto_struct->protocol_list->count++;
}

#endif
#endif

void PyObjC_SetupRuntimeCompat(void)
{
#if (MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_5)  && !defined(__OBJC2__)

#ifdef NO_OBJC2_RUNTIME
	/* 
	 * Don't use ObjC 2.0 runtime (compiling on 10.4 or earlier), always
	 * use the compat implementation.
	 */
	PyObjC_class_addMethodList  = compat_class_addMethodList;
	PyObjC_methodlist_magic     = compat_methodlist_magic;
	PyObjC_objc_disposeClassPair   = compat_objc_disposeClassPair;
	PyObjC_preclass_addMethod   = compat_preclass_addMethod;
	PyObjC_preclass_addIvar     = compat_preclass_addIvar;
	PyObjC_preclass_addProtocol = compat_preclass_addProtocol;

#   define SETUP(funcname) \
		PyObjC_##funcname = compat_##funcname

#else
	if (class_addMethod) {
		PyObjC_class_addMethodList = objc20_class_addMethodList;
		PyObjC_preclass_addMethod  = class_addMethod;
		PyObjC_preclass_addIvar    = class_addIvar;
		PyObjC_preclass_addProtocol= class_addProtocol;
	} else {
		PyObjC_class_addMethodList = compat_class_addMethodList;
		PyObjC_preclass_addMethod  = compat_preclass_addMethod;
		PyObjC_preclass_addIvar    = compat_preclass_addIvar;
		PyObjC_preclass_addProtocol= compat_preclass_addProtocol;
	}


	if (class_copyMethodList) {
		PyObjC_methodlist_magic = objc20_methodlist_magic;
	} else {
		PyObjC_methodlist_magic = compat_methodlist_magic;
	}

#   define SETUP(funcname) \
	if ((funcname) == NULL) { \
		PyObjC_##funcname = compat_##funcname; \
	} else { \
		PyObjC_##funcname = funcname; \
	} 
#endif
	SETUP(protocol_getName);
	SETUP(protocol_conformsToProtocol);
	SETUP(protocol_copyMethodDescriptionList);
	SETUP(protocol_copyProtocolList);
	SETUP(protocol_getMethodDescription);

	SETUP(objc_allocateClassPair);
	SETUP(objc_registerClassPair);
	SETUP(objc_disposeClassPair);
	SETUP(objc_copyProtocolList);
	SETUP(objc_getProtocol);

	SETUP(object_getClass);
	SETUP(object_setClass);
	SETUP(object_getClassName);
	SETUP(object_getIvar);
	SETUP(object_setIvar);

	SETUP(class_getSuperclass);
	SETUP(class_addMethod);
	SETUP(class_copyIvarList);
	SETUP(class_copyProtocolList);
	SETUP(class_copyMethodList);
	SETUP(class_getName);
	SETUP(class_isMetaClass);

	SETUP(method_getName);
	SETUP(method_getTypeEncoding);
	SETUP(method_getImplementation);
	SETUP(method_setImplementation);

	SETUP(sel_isEqual);

	SETUP(ivar_getName);
	SETUP(ivar_getTypeEncoding);
	SETUP(ivar_getOffset);
#endif /* MIN_REQUIRED < 10.5 && !OBJC2 */

#ifdef SETUP 
#undef SETUP
#endif


#if (MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_7)
	/* Compat definitions for protocol creation
	 *
	 * - Runtime APIs were introduced in OSX 10.7
	 * - Compat functions can only be implemented for 32-bit runtime
	 */

#if PyObjC_BUILD_RELEASE < 1007
	
#ifndef __LP64__
	PyObjC_objc_allocateProtocol = compat_objc_allocateProtocol;
	PyObjC_objc_registerProtocol = compat_objc_registerProtocol;
	PyObjC_protocol_addMethodDescription = compat_protocol_addMethodDescription;
	PyObjC_protocol_addProtocol = compat_protocol_addProtocol;
#endif


#elif defined(__LP64__)
	PyObjC_objc_allocateProtocol = objc_allocateProtocol;
	PyObjC_objc_registerProtocol = objc_registerProtocol;
	PyObjC_protocol_addMethodDescription = protocol_addMethodDescription;
	PyObjC_protocol_addProtocol = protocol_addProtocol;

#else
#   define SETUP(funcname) \
	if ((funcname) == NULL) { \
		PyObjC_##funcname = compat_##funcname; \
	} else { \
		PyObjC_##funcname = funcname; \
	} 
	SETUP(objc_allocateProtocol);
	SETUP(objc_registerProtocol);
	SETUP(protocol_addMethodDescription);
	SETUP(protocol_addProtocol);
#endif

#endif

#undef SETUP
}
