#ifndef PyObjC_CLASS_DESCRIPTOR_H
#define PyObjC_CLASS_DESCRIPTOR_H

PyObject* objcclass_descr_get(PyObject* obj, void* closure);
extern char objcclass_descr_doc[];

#define OBJCCLASS_SLOT \
	{ 						\
	"__objc_class__",		/* name */	\
	objcclass_descr_get,		/* get */	\
	0,				/* set */	\
	objcclass_descr_doc,		/* doc */	\
	0,				/* closure */	\
	}

#endif /* PyObjC_CLASS_DESCRIPTOR_H */
