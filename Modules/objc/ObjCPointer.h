/*****************************/
/*** PyObjCPointer interface ***/
/*****************************/

/* Python wrapper around C pointer */
typedef struct
{
  PyObject_VAR_HEAD

  void *ptr;
  PyStringObject *type;
  char contents[0];
} PyObjCPointer;

/* Corresponding Python type object */
extern PyTypeObject PyObjCPointer_Type;

/* Corresponding Python type check macro */
#define PyObjCPointer_Check(o) ((o)->ob_type == &PyObjCPointer_Type)

extern PyObjCPointer *PyObjCPointer_new (void *ptr, const char *type);
