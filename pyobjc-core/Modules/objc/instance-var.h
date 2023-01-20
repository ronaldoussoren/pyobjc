#ifndef OBJC_INSTANCE_VAR
#define OBJC_INSTANCE_VAR

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD
    char* _Nullable name; /* Name of the instance variable */
    char* _Nonnull type;  /* Type of the instance variable for definition only */
    Ivar _Nullable ivar;
    unsigned int isOutlet : 1;
    unsigned int isSlot : 1;
} PyObjCInstanceVariable;

extern PyObject* PyObjCInstanceVariable_Type;
#define PyObjCInstanceVariable_Check(obj)                                                \
    PyObject_TypeCheck((obj), (PyTypeObject*)PyObjCInstanceVariable_Type)

extern PyObject* _Nullable PyObjCInstanceVariable_New(const char* name);
extern int PyObjCInstanceVariable_Setup(PyObject* module);

#define PyObjCInstanceVariable_IsOutlet(obj) (((PyObjCInstanceVariable*)(obj))->isOutlet)
#define PyObjCInstanceVariable_IsSlot(obj) (((PyObjCInstanceVariable*)(obj))->isSlot)
#define PyObjCInstanceVariable_GetName(obj) (((PyObjCInstanceVariable*)(obj))->name)
#define PyObjCInstanceVariable_GetType(obj) (((PyObjCInstanceVariable*)(obj))->type)

NS_ASSUME_NONNULL_END

#endif /* OBJC_INSTANCE_VAR */
