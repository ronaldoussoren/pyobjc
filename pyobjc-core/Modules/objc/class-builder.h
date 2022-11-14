#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

NS_ASSUME_NONNULL_BEGIN

extern Class _Nullable PyObjCClass_BuildClass(Class, PyObject*, char*, PyObject*,
                                              PyObject*, PyObject*, PyObject*);
extern int PyObjCClass_UnbuildClass(Class);
extern int PyObjCClass_FinishClass(Class);
extern int PyObjC_RemoveInternalTypeCodes(char*);
extern int transform_class_dict(PyObject* py_superclas, PyObject* class_dict,
                                PyObject* meta_dict, PyObject* protocols,
                                int* _Nonnull needs_intermediate,
                                PyObject* _Nullable* _Nullable instance_variables,
                                PyObject* _Nullable* _Nullable instance_methods,
                                PyObject* _Nullable* _Nullable class_methods);

NS_ASSUME_NONNULL_END

#endif /* OBJC_CLASS_BUILDER */
