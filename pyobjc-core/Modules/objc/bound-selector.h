NS_ASSUME_NONNULL_BEGIN
extern PyObject* PyObjCBoundSelector_Type;
#define PyObjCBoundSelector_Check(obj)                                                   \
    Py_IS_TYPE((obj), (PyTypeObject*)PyObjCBoundSelector_Type)

#define PyObjCBoundPythonSelector_Check(obj)                                             \
    (Py_IS_TYPE((obj), (PyTypeObject*)PyObjCBoundSelector_Type)                          \
     && PyObjCPythonSelector_Check(((PyObjCBoundSelector*)obj)->sel_selector))
#define PyObjCBoundNativeSelector_Check(obj)                                             \
    (Py_IS_TYPE((obj), (PyTypeObject*)PyObjCBoundSelector_Type)                          \
     && PyObjCNativeSelector_Check(((PyObjCBoundSelector*)obj)->sel_selector))

#define PyObjCBoundSelector_SELF(obj) (((PyObjCBoundSelector*)(obj))->sel_self)
#define PyObjCBoundSelector_SELECTOR(obj) (((PyObjCBoundSelector*)(obj))->sel_selector)

extern PyObject* _Nullable PyObjCBoundSelector_New(PyObject*       self,
                                                   PyObjCSelector* selector);

extern int PyObjCBoundSelector_Setup(PyObject* module);

NS_ASSUME_NONNULL_END
