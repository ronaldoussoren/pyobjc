#ifndef PyObjC_registry_H
#define PyObjC_registry_H

extern PyObject* PyObjC_NewRegistry(void);
extern int PyObjC_AddToRegistry(PyObject*, PyObject*, PyObject*, PyObject*);
extern PyObject* PyObjC_FindInRegistry(PyObject*, Class, SEL);

#endif /* PyObjC_registry_H */
