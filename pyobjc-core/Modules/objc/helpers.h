#ifndef PyObjC_HELPERS_H
#define PyObjC_HELPERS_H

extern int PyObjC_setup_nsdata(void);
extern int PyObjC_setup_nscoder(void);
extern int PyObjC_setup_nsdecimal(PyObject* m);
extern int PyObjC_setup_nsobject(void);

extern PyObject* pythonify_nsdecimal(void* value);
extern int depythonify_nsdecimal(PyObject* value, void* out);
extern int IS_DECIMAL(const char* typestr);

extern int PyObjC_number_to_decimal(PyObject* value, NSDecimal* outResult);

extern PyObject* pythonify_authorizationitem(void* value);
extern int depythonify_authorizationitem(PyObject* value, void* out);
extern int IS_AUTHORIZATIONITEM(const char* typestr);

#endif /* PyObjC_HELPERS_H */

