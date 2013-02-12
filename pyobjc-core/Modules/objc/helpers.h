#ifndef PyObjC_HELPERS_H

extern int PyObjC_setup_nsdata(void);
extern int PyObjC_setup_nscoder(void);
extern int PyObjC_setup_nsdecimal(PyObject* m);

extern PyObject* pythonify_nsdecimal(void* value);
extern int depythonify_nsdecimal(PyObject* value, void* out);
extern int IS_DECIMAL(const char* typestr);

#endif

