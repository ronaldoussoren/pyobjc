#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

extern PyObject* PyObjC_class_setup_hook;

Class PyObjCClass_BuildClass(
		Class super_class,  
		PyObject* protocols,
		char* name, 
		PyObject* class_dict,
		PyObject* meta_dict,
		PyObject* hiddenSelectors,
		PyObject* hiddenClassSelectors);

int PyObjCClass_UnbuildClass(Class new_class);
int PyObjCClass_FinishClass(Class objc_class);
void PyObjC_RemoveInternalTypeCodes(char* buf);

#endif /* OBJC_CLASS_BUILDER */
