#ifndef PyObjC_registry_H
#define PyObjC_registry_H
/* Where's the documentation? */

PyObject* PyObjC_NewRegistry(void);
int PyObjC_AddToRegistry(PyObject*, PyObject*, PyObject*, PyObject*);
PyObject* PyObjC_FindInRegistry(PyObject*, Class, SEL);

#endif /* PyObjC_registry_H */
