#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

typedef struct {
	PyObject_HEAD
	char* name;      /* Name of the instance variable */
	char* type;      /* Type of the instance variable for definition only */
	int   isOutlet;
	int   isSlot;
	Ivar   ivar;
} PyObjCInstanceVariable;


extern PyTypeObject PyObjCInstanceVariable_Type;
#define PyObjCInstanceVariable_Check(obj) PyObject_TypeCheck((obj), &PyObjCInstanceVariable_Type)

PyObject* PyObjCInstanceVariable_New(char* name);
int	  PyObjCInstanceVariable_SetName(PyObject* self, PyObject* name);

#define PyObjCInstanceVariable_IsOutlet(obj) \
	(((PyObjCInstanceVariable*)(obj))->isOutlet)
#define PyObjCInstanceVariable_IsSlot(obj) \
	(((PyObjCInstanceVariable*)(obj))->isSlot)
#define PyObjCInstanceVariable_GetName(obj) \
	(((PyObjCInstanceVariable*)(obj))->name)
#define PyObjCInstanceVariable_GetType(obj) \
	(((PyObjCInstanceVariable*)(obj))->type)

PyObject* PyObjCIvar_Info(PyObject* self, PyObject* arg);
PyObject* PyObjCIvar_Set(PyObject* self, PyObject* args, PyObject* kwds);
PyObject* PyObjCIvar_Get(PyObject* self, PyObject* args, PyObject* kwds);



#endif /* OBJC_INSTANCE_VAR */
