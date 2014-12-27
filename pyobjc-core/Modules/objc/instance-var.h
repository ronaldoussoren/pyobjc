#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

typedef struct {
    PyObject_HEAD
    char* name; /* Name of the instance variable */
    char* type;  /* Type of the instance variable for definition only */
    Ivar ivar;
    unsigned int isOutlet:1;
    unsigned int isSlot:1;
} PyObjCInstanceVariable;


extern PyTypeObject PyObjCInstanceVariable_Type;
#define PyObjCInstanceVariable_Check(obj) PyObject_TypeCheck((obj), &PyObjCInstanceVariable_Type)

extern PyObject* PyObjCInstanceVariable_New(char* name);
extern int PyObjCInstanceVariable_SetName(PyObject* self, PyObject* name);

#define PyObjCInstanceVariable_IsOutlet(obj) \
    (((PyObjCInstanceVariable*)(obj))->isOutlet)
#define PyObjCInstanceVariable_IsSlot(obj) \
    (((PyObjCInstanceVariable*)(obj))->isSlot)
#define PyObjCInstanceVariable_GetName(obj) \
    (((PyObjCInstanceVariable*)(obj))->name)
#define PyObjCInstanceVariable_GetType(obj) \
    (((PyObjCInstanceVariable*)(obj))->type)

#endif /* OBJC_INSTANCE_VAR */
