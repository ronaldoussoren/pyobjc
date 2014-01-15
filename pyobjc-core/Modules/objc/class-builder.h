#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

extern Class PyObjCClass_BuildClass(Class, PyObject*, char*,
        PyObject*, PyObject*, PyObject*, PyObject*);
extern int PyObjCClass_UnbuildClass(Class);
extern int PyObjCClass_FinishClass(Class);
extern void PyObjC_RemoveInternalTypeCodes(char*);

#endif /* OBJC_CLASS_BUILDER */
