#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

#include <Python.h>

typedef struct {
	PyObject_HEAD
	char* name;	/* Name of the instance variable */
	char  type[2];	/* Type of the instance variable for definition only */
} ObjCIvar;


extern PyTypeObject ObjCIvar_Type;
#define ObjCIvar_Check(obj) PyObject_TypeCheck((obj), &ObjCIvar_Type)

PyObject* ObjCInstanceVar_New(char* name);

#endif /* OBJC_INSTANCE_VAR */
