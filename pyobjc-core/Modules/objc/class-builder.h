#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

NS_ASSUME_NONNULL_BEGIN

extern Class _Nullable PyObjCClass_BuildClass(Class, PyObject*, char*, PyObject*,
                                              PyObject*, PyObject*, PyObject*);
extern int PyObjCClass_UnbuildClass(Class);
extern int PyObjCClass_FinishClass(Class);
extern int PyObjC_RemoveInternalTypeCodes(char*);

NS_ASSUME_NONNULL_END

#endif /* OBJC_CLASS_BUILDER */
