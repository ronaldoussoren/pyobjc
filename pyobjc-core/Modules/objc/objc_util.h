#ifndef OBJC_UTIL
#define OBJC_UTIL

NS_ASSUME_NONNULL_BEGIN

extern PyObject* _Nullable PyObjCDict_GetItemStringWithError(PyObject*   dict,
                                                             const char* key);
#define PyDict_GetItemStringWithError PyObjCDict_GetItemStringWithError

extern PyObject* PyObjCExc_Error;
extern PyObject* PyObjCExc_NoSuchClassError;
extern PyObject* PyObjCExc_UnInitDeallocWarning;
extern PyObject* PyObjCExc_ObjCRevivalWarning;
extern PyObject* PyObjCExc_LockError;
extern PyObject* PyObjCExc_BadPrototypeError;
extern PyObject* PyObjCExc_UnknownPointerError;
extern PyObject* PyObjCExc_DeprecationWarning;
extern PyObject* PyObjCExc_ObjCPointerWarning;
extern PyObject* PyObjCExc_ObjCSuperWarning;

extern int PyObjC_CheckArgCount(PyObject* callable, size_t min_args, size_t max_args,
                                size_t nargsf);
extern int PyObjC_CheckNoKwnames(PyObject* callable, PyObject* _Nullable kwnames);

extern PyObject* _Nullable PyObjC_MakeCVoidP(void* _Nullable ptr);

extern int PyObjCUtil_Init(PyObject* module);

extern void PyObjCErr_FromObjC(NSObject* localException);

extern void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* _Nonnull state)
    __attribute__((__noreturn__));

extern char* _Nullable PyObjCUtil_Strdup(const char* value);

extern NSMapTableKeyCallBacks   PyObjCUtil_PointerKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks;

extern void PyObjC_FreeCArray(int, Py_buffer*);
extern int  PyObjC_PythonToCArray(BOOL, BOOL, const char*, PyObject*,
                                  void* _Nullable* _Nonnull, Py_ssize_t* _Nullable,
                                  PyObject* _Nullable* _Nonnull, Py_buffer*);
extern PyObject* _Nullable PyObjC_CArrayToPython(const char*, const void*, Py_ssize_t);

/* XXX: the '2' at the end of the name should be replaced by something more useful */
extern PyObject* _Nullable PyObjC_CArrayToPython2(const char*, const void*, Py_ssize_t,
                                                  bool already_retained,
                                                  bool already_cfretained);
extern int PyObjC_IsPythonKeyword(const char* word) __attribute__((__pure__));

extern int PyObjCRT_SimplifySignature(const char* signature, char* buf, size_t buflen);

extern int PyObjCObject_Convert(PyObject* object, void* pvar);
extern int PyObjCClass_Convert(PyObject* object, void* pvar);

extern int PyObjC_is_ascii_string(PyObject* unicode_string, const char* ascii_string)
    __attribute__((__pure__));
extern int PyObjC_is_ascii_prefix(PyObject* unicode_string, const char* ascii_string,
                                  size_t n) __attribute__((__pure__));

extern PyObject* _Nullable PyObjC_ImportName(const char* name);

extern PyObject* _Nullable PyObjC_AdjustSelf(PyObject* object);

extern PyObject* _Nullable PyObjC_FindSELInDict(PyObject*, SEL);
extern int PyObjCRT_SignaturesEqual(const char*, const char*) __attribute__((__pure__));

extern char* _Nullable PyObjC_SELToPythonName(SEL, char*, size_t);

extern bool version_is_deprecated(int version);

static inline Py_ssize_t
align(Py_ssize_t offset, Py_ssize_t alignment)
{
    Py_ssize_t rest = offset % alignment;
    if (rest == 0)
        return offset;
    return offset + (alignment - rest);
}

/*
 * SET_FIELD(op, value):
 *    macro for updating the value of 'op' to 'value',
 *    steals a reference to 'value'.
 *
 *    use this instead of 'Py_XDECREF(op); op = value'
 */
#define SET_FIELD(op, value)                                                             \
    do {                                                                                 \
        PyObject* _py_tmp = (PyObject*)(op);                                             \
        (op)              = value;                                                       \
        Py_XDECREF(_py_tmp);                                                             \
    } while (0)

/*
 * SET_FIELD_INCREF(op, value):
 *    macro for updating the value of 'op' to 'value'.
 *
 *    use this instead of 'Py_XDECREF(op); Py_INCREF(value); op = value'
 */
#define SET_FIELD_INCREF(op, value)                                                      \
    do {                                                                                 \
        PyObject* _py_tmp = (PyObject*)(op);                                             \
        PyObject* _py_val = (PyObject*)(value);                                          \
        Py_XINCREF(_py_val);                                                             \
        (op) = _py_val;                                                                  \
        Py_XDECREF(_py_tmp);                                                             \
    } while (0)

extern PyObject* PyObjCNM_insert;
extern PyObject* PyObjCNM_append;
extern PyObject* PyObjCNM_extend;
extern PyObject* PyObjCNM_timestamp;
extern PyObject* PyObjCNM_fromtimestamp;
extern PyObject* PyObjCNM_strftime;
extern PyObject* PyObjCNM_keys;
extern PyObject* PyObjCNM_clear;
extern PyObject* PyObjCNM_discard;
extern PyObject* PyObjCNM_add;
extern PyObject* PyObjCNM_values;
extern PyObject* PyObjCNM_description;
extern PyObject* PyObjCNM___get__;
extern PyObject* PyObjCNM_date_format_string;
extern PyObject* PyObjCNM_objc_memview_object;
extern PyObject* PyObjCNM_objc_NULL;
extern PyObject* PyObjCNM___new__;

extern PyObject* _Nullable PyObjC_CallCopyFunc(PyObject* arg);
extern PyObject* _Nullable PyObjC_CallDecoder(PyObject* cdr, PyObject* setValue);
extern PyObject* _Nullable PyObjC_TransformAttribute(PyObject*, PyObject*, PyObject*,
                                                     PyObject*);
extern int PyObjC_RemoveInternalTypeCodes(char*);

NS_ASSUME_NONNULL_END

#endif /* OBJC_UTIL */
