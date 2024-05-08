#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

NS_ASSUME_NONNULL_BEGIN

extern Class _Nullable PyObjCClass_BuildClass(Class, PyObject*, char*, PyObject*,
                                              PyObject*, PyObject*, PyObject*, int*);
extern int PyObjCClass_UnbuildClass(Class);
extern int PyObjCClass_FinishClass(Class);

NS_ASSUME_NONNULL_END

#endif /* OBJC_CLASS_BUILDER */
