#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

typedef struct {
	PyObject_HEAD
	char* name;	/* Name of the instance variable */
	char  type[2];	/* Type of the instance variable for definition only */
	int   isOutlet;
	int   isSlot;
	PyObjCRT_Ivar_t   ivar;
} PyObjCInstanceVariable;


extern PyTypeObject PyObjCInstanceVariable_Type;
#define PyObjCInstanceVariable_Check(obj) PyObject_TypeCheck((obj), &PyObjCInstanceVariable_Type)

PyObject* PyObjCInstanceVariable_New(char* name);

#define PyObjCInstanceVariable_IsOutlet(obj) \
	(((PyObjCInstanceVariable*)(obj))->isOutlet)

#endif /* OBJC_INSTANCE_VAR */
