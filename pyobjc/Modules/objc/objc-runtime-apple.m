/*
 * Support code for the Apple runtime
 */
#include "pyobjc.h"

#if defined(APPLE_RUNTIME)

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
	/* Initialize the structure */
	memset(cls, 0, sizeof(*cls));
	memset(metaCls, 0, sizeof(*cls));

	cls->methodLists = NULL;
	metaCls->methodLists = NULL;
	cls->isa = metaCls;

	cls->info = CLS_CLASS; // |CLS_METHOD_ARRAY;
	metaCls->info = CLS_META; // |CLS_METHOD_ARRAY;

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

	cls->methodLists = malloc(sizeof(struct objc_method_list*));
	if (cls->methodLists == NULL) {
		PyErr_NoMemory();
		free((char*)(cls->name)); 
		cls->name = NULL;
		free((char*)(metaCls->name)); 
		metaCls->name = NULL;
		return -1;
	}
	memset(cls->methodLists, 0, sizeof(*(cls->methodLists)));

	metaCls->methodLists = malloc(sizeof(struct objc_method_list*));
	if (cls->methodLists == NULL) {
		PyErr_NoMemory();
		free((char*)(cls->name)); 
		cls->name = NULL;
		free((char*)(metaCls->name)); 
		metaCls->name = NULL;
		free(cls->methodLists);
		cls->methodLists = NULL;
		return -1;
	}
	memset(metaCls->methodLists, 0, sizeof(*(metaCls->methodLists)));

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
        cls->methodLists[0] = (struct objc_method_list*)-1;
        metaCls->methodLists[0] = (struct objc_method_list*)-1;

	cls->super_class = superCls;
	metaCls->super_class = superCls->isa;
	metaCls->isa = rootCls->isa;

	cls->instance_size = ivarSize;
	cls->ivars = ivarList;

	metaCls->instance_size = metaCls->super_class->instance_size;
	metaCls->ivars = NULL;

	cls->protocols = metaCls->protocols = NULL;

	return 0;
}

void PyObjCRT_ClearClass(Class cls)
{
	if (cls->methodLists) {
		if (cls->methodLists) {
			struct objc_method_list** cur;

			cur = cls->methodLists;
			while (*cur != (struct objc_method_list*)-1) {
				if (*cur != NULL) {
					free(*cur);
					*cur = NULL;
				}
				cur++;
			}
			free(cls->methodLists);
			cls->methodLists = NULL;
		}
		cls->methodLists = NULL;
	}

	if (cls->name) {
		free((char*)(cls->name));
	}
}

struct objc_method_list *PyObjCRT_AllocMethodList(int numMethods)
{
        struct objc_method_list *mlist;

        mlist = malloc(sizeof(struct objc_method_list)
                 + ((numMethods+1) * sizeof(struct objc_method)));

        if (mlist == NULL) {
                return NULL;
        }

        mlist->method_count = 0;
        mlist->obsolete = NULL;

        return mlist;
}

#else /* !APPLE_RUNTIME */

static int dummy __attribute__((__unused__));

#endif /* !APPLE_RUNTIME */
