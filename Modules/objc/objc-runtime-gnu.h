#ifndef PyObjC_RUNTIME_GNU_H
#define PyObjC_RUNTIME_GNU_H

/* 
 * Specific support for the GNU Objective-C runtime
 */

#include <Foundation/NSException.h>
#include <Foundation/NSString.h>

#define objc_msgSendSuper(super, op, args...) \
	((super)->self == NULL                           \
	 	? 0                                      \
		: (                                      \
			class_get_instance_method(       \
				(super)->class, (op)     \
			)->method_imp)(                  \
				(super)->self,           \
				(op) ,##args))


/* 
 * XXX: AFAIK as I (Ronald) know, there should be an include named 
 * <objc/runtime.h> on systems with the GNU runtime. However, this file 
 * not present on my Linux playmachine (running Debian testing)...
 *
 * The alternative is to declare some prototypes ourselves...
 */
#if 0
#   include <objc/runtime.h>
#else
   extern void class_add_method_list(Class, MethodList_t);
   extern void __objc_add_class_to_hash(Class);
#endif


#ifndef nil
#define nil NULL
#endif

/* What we call _C_LNGLNG is actually _C_LNG_LNG in the GNU runtime */
#define _C_LNGLNG _C_LNG_LNG
#define _C_ULNGLNG _C_ULNG_LNG

/* XXX: names don't conform to the coding-style! */
extern Ivar_t class_getInstanceVariable(Class aClass, const char *name);
extern Ivar_t object_getInstanceVariable(id obj, const char *name, void **out);
extern Ivar_t object_setInstanceVariable(id obj, const char *name, void *value);
extern void objc_addClass(Class aClass);
//extern id objc_msgSendSuper(struct objc_super *super, SEL op, ...);
extern void objc_freeMethodList(struct objc_method_list *list);

static inline int PyObjCRT_SameSEL(SEL a, SEL b)
{
	return sel_eq(a, b);
}


static inline const char* 
PyObjCRT_SELName(SEL sel)
{
	return sel_get_name(sel);
}

static inline SEL 
PyObjCRT_SELUID(const char* str)
{
	return sel_get_uid(str);
}

static inline void
PyObjCRT_ClassAddMethodList(Class cls, MethodList_t lst)
{
	int i;

	/* First convert the method_names to strings, class_add_method_list
	 * assumes the method_names are strings and converts these back
	 * to selectors.
	 */
	for (i = 0; i < lst->method_count; i++) {
		lst->method_list[i].method_name = (SEL)PyObjCRT_SELName(lst->method_list[i].method_name);
	}

	class_add_method_list(cls, lst);
}

static inline Class 
PyObjCRT_LookUpClass(const char* name)
{
	return objc_lookup_class(name);
}

static inline struct objc_method_list *
PyObjCRT_NextMethodList(Class c, void ** p)
{
	if (*p == 0) {
		*p = c->methods;
	} else {
		*p = (*((MethodList_t*)p))->method_next;
	}
	return *(MethodList_t*)p;
}

static inline void 
PyObjCRT_InitMethod(Method_t m, SEL name, const char* types, IMP imp)
{
	/* XXX: With some versions of the GNU runtime, the runtime assumes
	 * that method_name is initialy a string instead of a selector, other
	 * versions do not. The version on my development box currently 
	 * doesn't.
	 *
	 * m->method_name = (SEL)PyObjCRT_SELName(name);
	 */
	m->method_name = name;
	m->method_types = types;
	m->method_imp = imp;
}


extern MethodList_t PyObjCRT_AllocMethodList(int);


typedef Method_t PyObjCRT_Method_t;
typedef Ivar_t PyObjCRT_Ivar_t;

static inline Class GETISA(id obj)
{
	return obj->class_pointer;
}

//#define GETISA(c)       (*((struct objc_object**)&(c))->class_pointer)
#define CLS_CLASS       _CLS_CLASS
#define CLS_META        _CLS_META
#define RECEIVER(c)     (c).self

static inline const char *
get_selector_encoding (id self, SEL sel)
{
  return sel->sel_types;
}



extern void PyObjCRT_AddClass(Class cls);
#define objc_addClass	PyObjCRT_AddClass

/* Return a number that is likely to change when the method list changes,
 * and is cheap to compute.
 */
static inline int
objc_methodlist_magic(Class cls)
{
  struct objc_method_list *mlist;
  int res, cnt;
  void *iterator = 0;

  res = cnt = 0;

  if (cls == NULL)
    return -1;

  while ((mlist = PyObjCRT_NextMethodList(cls, &iterator)))
    {
      res += mlist->method_count;
      cnt ++;
    }

  return (cnt << 16) | (res & 0xFFFF);
}



#endif /* PyObjC_RUNTIME_GNU_H */
