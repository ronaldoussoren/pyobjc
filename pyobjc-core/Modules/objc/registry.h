#ifndef PyObjC_registry_H
#define PyObjC_registry_H

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable PyObjC_NewRegistry(void);
extern int PyObjC_AddToRegistry(PyObject*, PyObject*, PyObject*, PyObject*);
extern PyObject* _Nullable PyObjC_FindInRegistry(PyObject*, Class, SEL);

typedef PyObject* _Nullable (*PyObjC_ItemTransform)(PyObject*);
extern PyObject* _Nullable PyObjC_CopyRegistry(PyObject*, PyObjC_ItemTransform);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_registry_H */
