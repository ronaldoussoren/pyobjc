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

#ifndef TEST_PYTHONIFICATION

#include "ObjC.h"
#include "OC_PythonObject.h"
#include "OC_PythonString.h"
#include "OC_PythonInt.h"

/* These macros hides as much as possible the differences between the
   GNU Runtime and the NeXT one. */

#ifdef GNU_RUNTIME

#include <gnustep/base/mframe.h>
#include <Foundation/NSException.h>
#include <Foundation/NSString.h>

#define ISCLASS(o)	((o) && CLS_ISMETA(((struct objc_object *) o)->class_pointer))

#define SELNAME(sel)	sel_get_name(sel)
#define SELUID(str)	sel_get_uid(str)
#define ISSELECTOR(s)	sel_is_mapped(s)
#define NAMEOF(obj)	object_get_class_name(obj)
#define LOOKUPCLASS(n)	objc_lookup_class(n)
#define METHOD		Method_t
#define CLASSMETH(c,s)	class_get_class_method(((struct objc_object *) c)->class_pointer, s)
#define INSTMETH(i,s)	class_get_instance_method(((struct objc_object *) i)->class_pointer, s)
#define METHNARGS(m)	method_get_number_of_arguments(m)
#define METHSARGS(m)	method_get_size_of_arguments(m)

static inline const char *
get_selector_encoding (id self, SEL sel)
{
  return sel->sel_types;
}

#else /* NeXTSTEP */

#import <Foundation/Foundation.h>

#include <objc/objc-runtime.h>

#warning this may not work on OSXS.  in any case, it should be made to go away as soon as we get rid of
#warning all references to NXHashTable
#include <objc/hashtable.h>


#define ISCLASS(o)	(((Class) (o)) && CLS_GETINFO(((Class) (o))->isa, CLS_META))

#define SELNAME(sel)	sel_getName(sel)
#define LOOKUPCLASS(n)	objc_lookUpClass(n)
#define METHOD		Method
#define CLASSMETH(c,s)	class_getClassMethod(c->isa, s)
#define INSTMETH(i,s)	class_getInstanceMethod(i->isa, s)
#define METHNARGS(m)	method_getNumberOfArguments(m)
#define METHSARGS(m)	method_getSizeOfArguments(m)

#define _C_CONST    'r'
#define _C_IN       'n'
#define _C_INOUT    'N'
#define _C_OUT      'o'
#define _C_BYCOPY   'O'
#define _C_ONEWAY   'V'

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

extern int objc_sizeof_type (const char *type);
extern const char *objc_skip_typespec (const char *type);

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

#endif /* TEST_PYTHONIFICATION */

#define WITH_SINGLE_UNDERSCORE 0
#define WITH_DOUBLE_UNDERSCORE 1
#define WITH_BOTH 2

/* By setting this to 0 or 1 you select a different translation from
   ObjC selector names to Python method names. If it is set to 0, or
   not set at all, you get:
     __privately:setName:forObject::
     	-> __privately_setName_forObject__
     thisIs:a:Method:with:some:arguments:
     	-> thisIs_a_Method_with_some_arguments_
     andThisIsNot
     	-> andThisIsNot
     __this_A_Mixed_Style_Method:withArguments::several:of_them:
     	-> __this___A___Mixed___Style___Method_withArguments__several_of___them_
   that is: underscore characters, not at beginning of the name, gets tripled;
   colon characters, denoting an argument in ObjC, are replaced with a single
   underscore.

   If set to 1, you get the currently default behaviour:
     __privately:setName:forObject::
     	-> __privately__setName__forObject____
     thisIs:a:Method:with:some:arguments:
	-> thisIs__a__Method__with__some__arguments__
     andThisIsNot
	-> andThisIsNot
     __this_A_Mixed_Style_Method:withArguments::several:of_them:
       -> __this_A_Mixed_Style_Method__withArguments____several__of_them__
   where only colon characters are replaced with a double underscore.

   If set to 2, the module will check with both methods. See
   PYTHONIFY_FIRST_TRY. This latter mode is obviously SLOWER. */
#define PYTHONIFICATION_METHOD WITH_BOTH

#if PYTHONIFICATION_METHOD == WITH_BOTH

/* By setting this to 0 or 1 you select the order that will be used to
   do the pythonification of ObjC selector's names: when set to 0 the
   code will try "single underscore" substition first, then "double
   underscore"; when set to 1, the other way around. */
#define PYTHONIFICATION_FIRST_TRY WITH_SINGLE_UNDERSCORE

#endif

#if PYTHONIFICATION_METHOD == WITH_DOUBLE_UNDERSCORE
#define PYTHONIFIED_LENGTH(selnam,sellen,argc) (sellen+argc+1)
#else
static inline unsigned int
_count_underscores (const char *s)
{
  unsigned int c = 0;

  while (*s)
    if (*s++ == '_')
      c++;
  return c;
}

#if PYTHONIFICATION_METHOD == WITH_SINGLE_UNDERSCORE

#define PYTHONIFIED_LENGTH(selnam,sellen,argc) (sellen+_count_underscores(selnam)*2+1)

#else /* WITH_BOTH */

#define PYTHONIFIED_LENGTH(selnam,sellen,argc) MAX((sellen+argc+1),\
						   (sellen+_count_underscores(selnam)*2+1))

#endif

#endif

/*#F Converts the Python form 'thisIsObjC__message__with__' to the ObjC
  equivalent 'thisIsObjC:message:with:'. You are responsible on
  the size of @var{to}. */
static inline void
#if PYTHONIFICATION_METHOD == WITH_BOTH
depythonify_objc_message (register const char *from, register char *to, int method)
#else
depythonify_objc_message (register const char *from, register char *to)
#endif
{
  /* Copy initial underscores */
  while (*from == '_')
    *to++ = *from++;
  
#if PYTHONIFICATION_METHOD == WITH_BOTH
  if (method == WITH_DOUBLE_UNDERSCORE)
#endif

#if PYTHONIFICATION_METHOD != WITH_SINGLE_UNDERSCORE
  while (*from)
    {
      if (*from == '_' && *(from+1) == '_')
	{
	  *to++ = ':';
	  from++;
	}
      else
	*to++ = *from;

      from++;
    }
#endif

#if PYTHONIFICATION_METHOD == WITH_BOTH
  else 
#endif

#if PYTHONIFICATION_METHOD != WITH_DOUBLE_UNDERSCORE
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
#endif

  *to = 0;
}

/*#F Converts an ObjC message in the form 'thisIsObjC:message:with:' to
  the Python form 'thisIsObjC__message__with__'. You are responsible on
  the size of @var{to}. */
static inline void
#if PYTHONIFICATION_METHOD == WITH_BOTH
pythonify_objc_message (register const char *from, register char *to, int method)
#else
pythonify_objc_message (register const char *from, register char *to)
#endif
{
  /* Copy initial underscores */
  while (*from == '_')
    *to++ = *from++;
  
#if PYTHONIFICATION_METHOD == WITH_BOTH
  if (method == WITH_DOUBLE_UNDERSCORE)
#endif

#if PYTHONIFICATION_METHOD != WITH_SINGLE_UNDERSCORE
  while (*from)
    {
      if (*from == ':')
	{
	  *to++ = '_';
	  *to++ = '_';
	}
      else
	*to++ = *from;

      from++;
    }
#endif

#if PYTHONIFICATION_METHOD == WITH_BOTH
  else
#endif

#if PYTHONIFICATION_METHOD != WITH_DOUBLE_UNDERSCORE
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
#endif
  
  *to = '\0';
}

#ifndef TEST_PYTHONIFICATION

/*#F Takes a C value pointed by @var{datum} with its type encoded in
  @var{type}, that should be coming from an ObjC @encode directive,
  and returns an equivalent Python object where C structures and
  arrays are represented as tuples. */
extern PyObject *pythonify_c_value (const char *type,
				    void *datum,
				    ObjCMethod *self);

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
extern PyObject *execute_and_pythonify_objc_method (ObjCMethod *self,
						    PyObject *args);

#else /* we are testing the pythonification */

#if PYTHONIFICATION_METHOD == WITH_BOTH

main()
{
  const char *sel1 = "__privately:setName:forObject::";
  const char *sel2 = "thisIs:a:Method:with:some:arguments:";
  const char *sel3 = "andThisIsNot";
  const char *sel4 = "__this_A_Mixed_Style_Method:withArguments::several:of_them:";
  char pythonified_ss[1000], pythonified_ds[1000];
  char depythonified_ss[1000], depythonified_ds[1000];

#define P(sel) \
  pythonify_objc_message (sel,pythonified_ss,WITH_SINGLE_UNDERSCORE); \
  pythonify_objc_message (sel,pythonified_ds,WITH_DOUBLE_UNDERSCORE); 
#define T(sel) \
  P(sel)									       \
  printf ("%s\n\t->%s\n", sel, pythonified_ss);					       \
  depythonify_objc_message (pythonified_ss, depythonified_ss, WITH_SINGLE_UNDERSCORE); \
  depythonify_objc_message (pythonified_ss, depythonified_ds, WITH_DOUBLE_UNDERSCORE); \
  printf ("\t\t->%s\n\t\t->%s\n", depythonified_ss, depythonified_ds);		       \
  printf ("\t->%s\n", pythonified_ds);						       \
  depythonify_objc_message (pythonified_ds, depythonified_ss, WITH_SINGLE_UNDERSCORE); \
  depythonify_objc_message (pythonified_ds, depythonified_ds, WITH_DOUBLE_UNDERSCORE); \
  printf ("\t\t->%s\n\t\t->%s\n\t%s\n", depythonified_ss, depythonified_ds,	       \
	  (!strcmp (sel, depythonified_ss) ||					       \
	   !strcmp (sel, depythonified_ds)) ? "Ok" : "WRONG!")

  T(sel1);
  T(sel2);
  T(sel3);
  T(sel4);
}

#else

main()
{
  const char *sel1 = "__privately:setName:forObject::";
  const char *sel2 = "thisIs:a:Method:with:some:arguments:";
  const char *sel3 = "andThisIsNot";
  const char *sel4 = "__this_A_Mixed_Style_Method:withArguments::several:of_them:";
  char pythonified[1000], depythonified[1000];

#define P(sel) pythonify_objc_message (sel,pythonified); \
               depythonify_objc_message (pythonified, depythonified);
#define T(sel) P(sel) printf ("%s\n\t-> %s\n\t-> %s\n\t%s\n", sel, pythonified, depythonified, \
			      (strcmp (sel, depythonified) == 0 ? "Ok" : "WRONG!"))

  T(sel1);
  T(sel2);
  T(sel3);
  T(sel4);
}

#endif

#endif /* TEST_PYTHONIFICATION */

#endif /* _objc_support_H */
