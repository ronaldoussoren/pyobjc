/*****************************/
/*** ObjCPointer interface ***/
/*****************************/

/* Python wrapper around C pointer */
typedef struct
{
  PyObject_VAR_HEAD

  void *ptr;
  PyStringObject *type;
  char contents[0];
} ObjCPointer;

/* Corresponding Python type object */
extern PyTypeObject ObjCPointer_Type;

/* Corresponding Python type check macro */
#define ObjCPointer_Check(o) ((o)->ob_type == &ObjCPointer_Type)

extern ObjCPointer *ObjCPointer_new (void *ptr, const char *type);
