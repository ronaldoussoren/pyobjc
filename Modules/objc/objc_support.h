/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:57
 *
 * Created Tue Sep 10 14:11:38 1996.
 */

#ifndef _objc_support_H
#define _objc_support_H


/* These macros hides as much as possible the differences between the
   GNU Runtime and the NeXT one. */

#ifdef GNU_RUNTIME

#include <Foundation/NSException.h>
#include <Foundation/NSString.h>

#ifndef nil
#define nil NULL
#endif

#ifndef _C_LNGLNG
#define _C_LNGLNG 'q'
#endif

#ifndef _C_ULNGLNG
#define _C_ULNGLNG 'Q'
#endif

extern Ivar_t class_getInstanceVariable(Class aClass, const char *name);
extern Ivar_t object_getInstanceVariable(id obj, const char *name, void **out);
extern struct objc_method_list *class_nextMethodList(Class aClass, void **ptr);
extern Ivar_t object_setInstanceVariable(id obj, const char *name, void *value);
extern void objc_addClass(Class aClass);
extern id objc_msgSendSuper(struct objc_super *super, SEL op, ...);
extern void objc_freeMethodList(struct objc_method_list *list);

#define ISCLASS(o)	((o) && CLS_ISMETA(((struct objc_object *) o)->class_pointer))

#define SELNAME(sel)	sel_get_name(sel)
#define SELUID(str)	sel_get_uid(str)
#define ISSELECTOR(s)	sel_is_mapped(s)
#define NAMEOF(obj)	object_get_class_name(obj)
#define LOOKUPCLASS(n)	objc_lookup_class(n)
#define METHODLISTS     methods
#define METHOD		Method_t
#define IVAR            Ivar_t
#define CLASSMETH(c,s)	class_get_class_method(((struct objc_object *) c)->class_pointer, s)
#define INSTMETH(i,s)	class_get_instance_method(((struct objc_object *) i)->class_pointer, s)
#define METHNARGS(m)	method_get_number_of_arguments(m)
#define METHSARGS(m)	method_get_size_of_arguments(m)
#define GETISA(c)       ((struct objc_object *)(c))->class_pointer
#define CLS_CLASS       _CLS_CLASS
#define CLS_META        _CLS_META
#define RECEIVER(c)     (c).self
#define SELUID(name)    sel_get_uid(name)

static inline const char *
get_selector_encoding (id self, SEL sel)
{
  return sel->sel_types;
}

static inline Method_t class_getClassMethod(MetaClass class, SEL aSel)
{
  return class_get_class_method(class, aSel);
}

static inline Method_t class_getInstanceMethod(Class class, SEL aSel)
{
  return class_get_instance_method(class, aSel);
}

static inline Class objc_lookUpClass(const char *name)
{
  return objc_lookup_class(name);
}

static inline SEL sel_registerName(const char *name)
{
  return sel_register_name(name);
}

static inline void class_addMethods(Class aClass, struct objc_method_list *methods)
{
  class_add_method_list(aClass, methods);
}

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

  while ((mlist = class_nextMethodList(cls, &iterator)))
    {
      res += mlist->method_count;
      cnt ++;
    }

  return (cnt << 16) | (res & 0xFFFF);
}

#else /* NeXTSTEP / Mac OS X */

#import <Foundation/NSObject.h>
#import <Foundation/NSString.h>

#include <objc/objc-runtime.h>

#define ISCLASS(o)	(((Class) (o)) && CLS_GETINFO(((Class) (o))->isa, CLS_META))

#define SELNAME(sel)	sel_getName(sel)
#define LOOKUPCLASS(n)	objc_lookUpClass(n)
#define METHODLISTS     methodLists
#define METHOD		Method
#define IVAR            Ivar
#define CLASSMETH(c,s)	class_getClassMethod((c)->isa, s)
#define INSTMETH(i,s)	class_getInstanceMethod((i)->isa, s)
#define METHNARGS(m)	method_getNumberOfArguments(m)
#define METHSARGS(m)	method_getSizeOfArguments(m)
#define GETISA(c)       (c)->isa
#define RECEIVER(c)     (c).receiver

#define _C_CONST    'r'
#define _C_IN       'n'
#define _C_INOUT    'N'
#define _C_OUT      'o'
#define _C_BYCOPY   'O'
#define _C_ONEWAY   'V'
#define _C_LNGLNG   'q'
#define _C_ULNGLNG   'Q'

static inline const char *
objc_skip_type_qualifiers (const char *type)
{
  while (*type == _C_CONST ||
	 *type == _C_IN ||
	 *type == _C_INOUT ||
	 *type == _C_OUT ||
	 *type == _C_BYCOPY ||
	 *type == _C_ONEWAY)
    type++;
  return type;
}


/* Return a number that is likely to change when the method list changes,
 * and is cheap to compute.
 */
static inline int
objc_methodlist_magic(Class cls)
{
	struct objc_method_list* mlist;
	int res, cnt;
	void* iterator = 0;
	res = cnt = 0;

	if (cls == NULL) return -1;

	while ((mlist = class_nextMethodList(cls, &iterator))) {
		res += mlist->method_count;
		cnt ++;
#if 0
	/* add information about actuall methods, this is expensive and
	 * shouldn't be necessary
	 */ 
	     {
		int i;
		for (i = 0; i < mlist->method_count; i++) {
			int x = (int)(mlist->method_list[i].method_imp);

			res ^= (x >> 16) ^ (x && 0xffff);
		}
	     }
#endif

	}

	return (cnt << 16) | (res & 0xFFFF);
}

extern int objc_sizeof_type (const char *type);
extern const char *objc_skip_typespec (const char *type);
extern void objc_freeMethodList(struct objc_method_list **list);

static inline const char *
get_selector_encoding (id self, SEL sel)
{
  METHOD m = INSTMETH(self, sel); /* sdm7g -- missing arg  */

  if (!m)
    return NULL;
  else
    return m->method_types;
}

#endif /* GNUSTEP */

static inline unsigned int
_count_underscores (const char *s)
{
  unsigned int c = 0;

  while (*s)
    if (*s++ == '_')
      c++;
  return c;
}

#define PYTHONIFIED_LENGTH(selnam,sellen,argc) (sellen+_count_underscores(selnam)*2+1)

/*#F Converts the Python form 'thisIsObjC__message__with__' to the ObjC
  equivalent 'thisIsObjC:message:with:'. You are responsible on
  the size of @var{to}. */
static inline void
depythonify_objc_message (register const char *from, register char *to)
{
  /* Copy initial underscores */
  while (*from == '_')
    *to++ = *from++;
  
  while (*from)
    {
      if (*from == '_' && *(from+1) == '_' && *(from+2) == '_')
	{
	  *to++ = '_';
	  from += 2;
	}
      else if (*from == '_')
	{
	  *to++ = ':';
	}
      else
	*to++ = *from;

      from++;
    }

  *to = 0;
}

/*#F Converts an ObjC message in the form 'thisIsObjC:message:with:' to
  the Python form 'thisIsObjC__message__with__'. You are responsible on
  the size of @var{to}. */
static inline void
pythonify_objc_message (register const char *from, register char *to)
{
  /* Copy initial underscores */
  while (*from == '_')
    *to++ = *from++;
  
  while (*from)
    {
      if (*from == '_')
	{
	  *to++ = '_';
	  *to++ = '_';
	  *to++ = '_';
	}
      else if (*from == ':')
	*to++ = '_';
      else
	*to++ = *from;

      from++;
    }
  
  *to = '\0';
}

/*#F Takes a C value pointed by @var{datum} with its type encoded in
  @var{type}, that should be coming from an ObjC @encode directive,
  and returns an equivalent Python object where C structures and
  arrays are represented as tuples. */
extern PyObject *pythonify_c_value (const char *type,
				    void *datum);

/*#F Takes a Python object @var{arg} and translate it into a C value
  pointed by @var{datum} accordingly with the type specification
  encoded in @var{type}, that should be coming from an ObjC @encode
  directive.
  Returns NULL on success, or a static error string describing the
  error. */
extern const char *depythonify_c_value (const char *type,
					PyObject *arg,
					void *datum);

/*#F Executes the ObjC method wrapped by @var{self}, applying it to
  the arguments in @var{args}, then returns the ``pythonified''
  result. */
extern PyObject *execute_and_pythonify_objc_method (PyObject *meth,
				PyObject* self, PyObject *args);

extern struct objc_method_list *objc_allocMethodList(int numMethods);

#endif /* _objc_support_H */
