#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

#include <Python.h>

typedef struct {
	PyObject_HEAD
	char* name;	/* Name of the instance variable */
	char  type[2];	/* Type of the instance variable for definition only */
} PyObjCInstanceVariable;


extern PyTypeObject PyObjCInstanceVariable_Type;
#define PyObjCInstanceVariable_Check(obj) PyObject_TypeCheck((obj), &PyObjCInstanceVariable_Type)

PyObject* PyObjCInstanceVariable_New(char* name);

#endif /* OBJC_INSTANCE_VAR */
