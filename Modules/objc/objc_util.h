#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Python.h>
#include <Foundation/NSException.h>

extern PyObject* objc_error;
extern PyObject* objc_noclass_error;
extern PyObject* objc_internal_error;

int ObjCUtil_Init(PyObject* module);

extern PyObject* ObjC_class_extender;
int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict);

void ObjCErr_Set(PyObject* exc, char* fmt, ...);
void ObjCErr_FromObjC(NSException* localException);
void ObjCErr_ToObjC(void);

PyObject* ObjC_call_to_python(id self, SEL selector, PyObject* arglist);

char* ObjC_strdup(const char* value);

#endif /* OBJC_UTIL */
