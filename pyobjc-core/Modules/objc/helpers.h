#ifndef PyObjC_HELPERS_H
#define PyObjC_HELPERS_H

NS_ASSUME_NONNULL_BEGIN

extern int PyObjC_setup_nsdata(PyObject* m);
extern int PyObjC_setup_nscoder(PyObject* m);
extern int PyObjC_setup_nsdecimal(PyObject* m);
extern int PyObjC_setup_nsobject(PyObject* m);
extern int PyObjC_setup_simd(PyObject* m);
extern int PyObjC_setup_nsinvocation(PyObject* m);

extern PyObject* _Nullable pythonify_nsdecimal(const void* value);
extern int depythonify_nsdecimal(PyObject* value, void* out);
extern int IS_DECIMAL(const char* typestr);

extern int PyObjC_number_to_decimal(PyObject* value, NSDecimal* outResult);

extern PyObject* _Nullable pythonify_authorizationitem(const void* value);
extern int depythonify_authorizationitem(PyObject* value, void* out);
extern int IS_AUTHORIZATIONITEM(const char* typestr);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_HELPERS_H */
