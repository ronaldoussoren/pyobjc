/*
 * Support code for the GNU runtime
 *
 * NOTE: This file uses some private functions in the GNU runtime as that seems
 * to be the only way to properly interface with that runtime.
 */
#include "pyobjc.h"

#if defined(GNU_RUNTIME)

int PyObjCRT_SetupClass(
	Class cls, 
	Class metaCls, 
	const char*name, 
	Class superCls,
	Class rootCls,
	int ivarSize,
	struct objc_ivar_list* 	ivarList
)

{
	/* This is a private function, but seems to be the only way to
	 * really create the class.
	 */
	extern void __objc_install_premature_dtable (Class);

	/* Initialize the structure */
	memset(cls, 0, sizeof(*cls));
	memset(metaCls, 0, sizeof(*cls));

	cls->version = 0;
	metaCls->version = 0;
	cls->subclass_list = NULL;
	metaCls->subclass_list = NULL;
	cls->sibling_class = NULL;
	metaCls->sibling_class = NULL;
	cls->protocols = NULL;
	metaCls->protocols = NULL;

	cls->methods = NULL;
	metaCls->methods = NULL;
	cls->class_pointer = metaCls;

	cls->info = CLS_CLASS;
	metaCls->info = CLS_META;

	cls->name = strdup(name);
	if (cls->name == NULL) {
		return -1;
	}
	metaCls->name = strdup(name);
	if (metaCls->name == NULL) {
		free((char*)(cls->name));
		cls->name = NULL;
		return -1;
	}

	cls->methods = NULL;
	metaCls->methods = NULL;

	cls->super_class = superCls;
	metaCls->super_class = superCls->class_pointer;
	metaCls->class_pointer = rootCls->class_pointer;
	CLS_SETRESOLV(cls);
	CLS_SETRESOLV(metaCls);

	cls->instance_size = ivarSize;
	cls->ivars = ivarList;

	metaCls->instance_size = metaCls->super_class->instance_size;
	metaCls->ivars = NULL;

	cls->protocols = metaCls->protocols = NULL;

        __objc_install_premature_dtable (metaCls);
	__objc_install_premature_dtable (cls);

	return 0;
}

void PyObjCRT_AddClass(Class cls)
{
	cls->sibling_class = cls->super_class->subclass_list;
	cls->super_class->subclass_list = cls;
	cls->class_pointer->sibling_class = cls->super_class->class_pointer->subclass_list;
	cls->super_class->class_pointer->subclass_list = cls->class_pointer;
	__objc_add_class_to_hash(cls);
}


void PyObjCRT_ClearClass(Class cls)
{
	if (cls->methods) {
		MethodList_t next, cur;

		cur = cls->methods;

		while (cur != NULL) {
			next = cur->method_next;

			objc_free(cur);
			cur = next;
		}
		cls->methods = NULL;
	}

	if (cls->name) {
		free((char*)(cls->name));
		cls->name = NULL;
	}
}

struct objc_method_list *PyObjCRT_AllocMethodList(int numMethods)
{
        struct objc_method_list *mlist;

        mlist = objc_malloc(sizeof(struct objc_method_list)
                 + ((numMethods+1) * sizeof(struct objc_method)));

        if (mlist == NULL) {
                return NULL;
        }

        mlist->method_count = 0;
	mlist->method_next = NULL;

        return mlist;
}

/*
 * XXX: This functions should be renamed to avoid name classes with
 * the actual ObjC runtime
 */

Ivar_t class_getInstanceVariable(Class aClass, const char *name)
{
  if (!aClass || !name)
    return NULL;

  for (; aClass != Nil; aClass = aClass->super_class)
    {
      int i;

      if (!aClass->ivars)
	continue;

      for (i = 0; i < aClass->ivars->ivar_count; i++)
	{
	  if (!strcmp(aClass->ivars->ivar_list[i].ivar_name, name))
	    return &aClass->ivars->ivar_list[i];
	}
    }

  return NULL;
}

Ivar_t object_getInstanceVariable(id obj, const char *name, void **out)
{
  Ivar_t var = NULL;

  if (obj && name)
    {
      void **varIndex = NULL;

      if ((var = class_getInstanceVariable(obj->class_pointer, name)))
	varIndex = (void **)((char *)obj + var->ivar_offset);

      if (out)
	*out = *varIndex;
    }

  return var;
}

Ivar_t object_setInstanceVariable(id obj, const char *name, void *value)
{
  Ivar_t var = NULL;

  if (obj && name)
    {
      void **varIndex;

      if ((var = class_getInstanceVariable(obj->class_pointer, name)))
	{
	  varIndex = (void **)((char *)obj + var->ivar_offset);

	  *varIndex = value;
	}
    }

  return var;
}


#else /* !GNU_RUNTIME */

static int dummy __attribute__((__unused__));

#endif /* !GNU_RUNTIME */
