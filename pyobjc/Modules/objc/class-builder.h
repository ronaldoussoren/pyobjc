#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

#include <Python.h>
#include <objc/objc.h>

/*
 * The protocol for building a hybrid python&objective-C class
 * 1) Collect the necessary information (name, bases, class_dict)
 * 2) Call ObjC_BuildClass
 * 3) Create the python class
 * 4) Call ObjCClass_SetClass
 *
 * If step 3 fails, call ObjCClass_UnbuildClass.
 *
 * NOTE:
 *   It is _not_ possible to remove classes from the objective-C runtime,
 *   and it is therefore not possible to call 'ObjCClass_UnbuildClass' after
 *   you have called 'ObjCClass_SetClass'
 */
Class ObjCClass_BuildClass(Class super_class,  PyObject* protocols,
				char* name, PyObject* class_dict);
void ObjCClass_UnbuildClass(Class new_class);
int ObjCClass_SetClass(Class objc_class, PyObject* py_class);

int ObjC_HasPythonImplementation(id obj);
PyObject* ObjC_GetPythonImplementation(id obj);

#endif /* OBJC_CLASS_BUILDER */
