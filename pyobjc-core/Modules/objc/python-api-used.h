/*
 * This header contains redefinitions of CPython API functions
 * used in pyobjc-core. The redefinitions contain nullablity attributes
 * for better error checking.
 *
 * The definitions are only used when running the static analyzer, to
 * avoid unexpected incompatibilities when performing a regular build.
 *
 * XXX: 'USE_STATIC_ANALYZER' is used because I haven't found another way
 *      to detect that the analyzer is used.
 * XXX: The definitions in this file have been added manually, there should
 *      at least be a test that warns if the file is incomplete.
 */
#ifdef USE_STATIC_ANALYZER

NS_ASSUME_NONNULL_BEGIN

#ifndef PY_SSIZE_T_CLEAN
#error "Requires PY_SSIZE_T_CLEAN"
#endif

PyAPI_FUNC(int) PyArg_Parse(PyObject*, const char*, ...);
PyAPI_FUNC(int) PyArg_ParseTuple(PyObject* _Nullable, const char*, ...);
PyAPI_FUNC(int)
    PyArg_ParseTupleAndKeywords(PyObject* _Nullable, PyObject* _Nullable,
                                const char* _Nullable, char* _Nullable* _Nullable, ...);

PyAPI_FUNC(PyObject* _Nullable) PyBool_FromLong(long);
PyAPI_FUNC(void) PyBuffer_Release(Py_buffer* view);
PyAPI_FUNC(char* _Nullable) PyByteArray_AsString(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyByteArray_FromObject(PyObject*);
PyAPI_FUNC(PyObject* _Nullable)
    PyByteArray_FromStringAndSize(const char* _Nullable, Py_ssize_t);
PyAPI_FUNC(int) PyByteArray_Resize(PyObject*, Py_ssize_t);
PyAPI_FUNC(Py_ssize_t) PyByteArray_Size(PyObject*);
PyAPI_FUNC(char* _Nullable) PyBytes_AsString(PyObject*);
PyAPI_FUNC(int) PyBytes_AsStringAndSize(PyObject*   obj, char* _Nullable* _Nonnull buffer,
                                        Py_ssize_t* _Nullablelength);
PyAPI_FUNC(PyObject* _Nullable) PyBytes_FromString(const char*);
PyAPI_FUNC(PyObject* _Nullable)
    PyBytes_FromStringAndSize(const char* _Nullable, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable)(PyCFunction_NewEx)(PyMethodDef* ml,
                                                   PyObject* _Nullable self,
                                                   PyObject* module);
PyAPI_FUNC(PyObject* _Nullable)
    Py_CMethod_New(PyMethodDef* ml, PyObject* _Nullable self, PyObject* _Nullable module,
                   PyTypeObject* _Nullable cls);
PyAPI_FUNC(int) PyCallable_Check(PyObject* o);
PyAPI_FUNC(void* _Nullable) PyCapsule_GetPointer(PyObject* capsule, const char* name);
PyAPI_FUNC(PyObject*) PyCapsule_New(void* _Nullable pointer, const char* _Nullable name,
                                    PyCapsule_Destructor _Nullable destructor);
PyAPI_FUNC(int) PyDescr_IsData(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyDictProxy_New(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyDict_Copy(PyObject* mp);
PyAPI_FUNC(int) PyDict_DelItem(PyObject* mp, PyObject* key);
PyAPI_FUNC(int) PyDict_DelItemString(PyObject* dp, const char* key);
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItem(PyObject* mp, PyObject* key);
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItemString(PyObject* dp, const char* key);
PyAPI_FUNC(PyObject* _Nullable) _PyDict_GetItemStringWithError(PyObject*, const char*);
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItemWithError(PyObject* mp, PyObject* key);
PyAPI_FUNC(PyObject* _Nullable) PyDict_Keys(PyObject* mp);
PyAPI_FUNC(PyObject* _Nullable) PyDict_New(void);
PyAPI_FUNC(int) PyDict_Next(PyObject* p, Py_ssize_t* ppos, PyObject* _Nullable* _Nullable,
                            PyObject* _Nullable* _Nullable pvalue);
PyAPI_FUNC(int) PyDict_SetItem(PyObject* mp, PyObject* key, PyObject* item);
PyAPI_FUNC(int) PyDict_SetItemString(PyObject* dp, const char* key, PyObject* item);
PyAPI_FUNC(Py_ssize_t) PyDict_Size(PyObject* mp);
PyAPI_FUNC(int) PyDict_Update(PyObject* mp, PyObject* other);
PyAPI_FUNC(PyObject* _Nullable) PyDict_Values(PyObject* mp);
PyAPI_FUNC(void) _PyErr_BadInternalCall(const char* filename, int lineno);
PyAPI_FUNC(void) PyErr_Clear(void);
PyAPI_FUNC(void) _PyErr_Clear(PyThreadState* tstate);
PyAPI_FUNC(int) PyErr_ExceptionMatches(PyObject*);
PyAPI_FUNC(void)
    PyErr_Fetch(PyObject* _Nullable* _Nullable, PyObject* _Nullable* _Nullable,
                PyObject* _Nullable* _Nullable);
PyAPI_FUNC(PyObject* _Nullable)
    PyErr_Format(PyObject* exception, const char* format, ...);
PyAPI_FUNC(PyObject* _Nullable)
    PyErr_NewException(const char* name, PyObject* _Nullable base,
                       PyObject* _Nullable dict);
PyAPI_FUNC(PyObject* _Nullable) PyErr_NoMemory(void);
PyAPI_FUNC(void)
    PyErr_NormalizeException(PyObject* _Nullable* _Nonnull, PyObject* _Nullable* _Nonnull,
                             PyObject* _Nullable* _Nonnull);
PyAPI_FUNC(PyObject* _Nullable) PyErr_Occurred(void);
PyAPI_FUNC(void) PyErr_Print(void);
PyAPI_FUNC(void)
    PyErr_Restore(PyObject* _Nullable, PyObject* _Nullable, PyObject* _Nullable);
PyAPI_FUNC(PyObject* _Nullable) PyErr_SetFromErrno(PyObject*);
PyAPI_FUNC(void) PyErr_SetObject(PyObject*, PyObject*);
PyAPI_FUNC(void) PyErr_SetString(PyObject* type, const char* message);
PyAPI_FUNC(int)
    PyErr_WarnEx(PyObject* category, const char* message, Py_ssize_t stack_level);
PyAPI_FUNC(int)
    PyErr_WarnFormat(PyObject* category, Py_ssize_t stack_level, const char* format, ...);
PyAPI_FUNC(void) PyErr_WriteUnraisable(PyObject* _Nullable);
Py_DEPRECATED(3.9) PyAPI_FUNC(void) PyEval_InitThreads(void);
PyAPI_FUNC(double) PyFloat_AsDouble(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyFloat_FromDouble(double);
PyAPI_FUNC(PyObject* _Nullable) PyFrozenSet_New(PyObject* _Nullable);
PyAPI_FUNC(PyObject* _Nullable) PyFunction_GetCode(PyObject*);
PyAPI_FUNC(PyGILState_STATE) PyGILState_Ensure(void);
PyAPI_FUNC(void) PyGILState_Release(PyGILState_STATE);
PyAPI_FUNC(PyObject* _Nullable) PyImport_Import(PyObject* name);
PyAPI_FUNC(PyObject* _Nullable) PyImport_ImportModule(const char* name);
PyAPI_FUNC(int) PyIndex_Check(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyIter_Next(PyObject*);
PyAPI_FUNC(int) PyList_Append(PyObject*, PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyList_AsTuple(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyList_GetItem(PyObject*, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable) PyList_New(Py_ssize_t size);
PyAPI_FUNC(Py_ssize_t) PyList_Size(PyObject*);
PyAPI_FUNC(double) PyLong_AsDouble(PyObject*);
PyAPI_FUNC(long) PyLong_AsLong(PyObject*);
PyAPI_FUNC(long long) PyLong_AsLongLong(PyObject*);
PyAPI_FUNC(Py_ssize_t) PyLong_AsSsize_t(PyObject*);
PyAPI_FUNC(unsigned long) PyLong_AsUnsignedLong(PyObject*);
PyAPI_FUNC(unsigned long long) PyLong_AsUnsignedLongLong(PyObject*);
PyAPI_FUNC(unsigned long long) PyLong_AsUnsignedLongLongMask(PyObject*);
PyAPI_FUNC(void*) PyLong_AsVoidPtr(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromLong(long);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromLongLong(long long);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromSize_t(size_t);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromSsize_t(Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromUnsignedLong(unsigned long);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromUnsignedLongLong(unsigned long long);
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromVoidPtr(void* _Nullable);
PyAPI_FUNC(PyObject* _Nullable) PyMapping_Keys(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable) PyMapping_Values(PyObject* o);
PyAPI_FUNC(void* _Nullable) PyMem_Malloc(size_t size);
PyAPI_FUNC(void* _Nullable) PyMem_Realloc(void* _Nullable ptr, size_t new_size);
PyAPI_FUNC(PyObject* _Nullable) PyMember_GetOne(const char*, struct PyMemberDef*);
PyAPI_FUNC(int) PyMember_SetOne(char*, struct PyMemberDef*, PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyMemoryView_FromBuffer(Py_buffer* info);
PyAPI_FUNC(PyObject* _Nullable) PyMethod_Function(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyMethod_Self(PyObject*);
PyAPI_FUNC(int) PyModule_AddIntConstant(PyObject*, const char*, long);
PyAPI_FUNC(int) PyModule_AddObject(PyObject* mod, const char*, PyObject* value);
PyAPI_FUNC(int) PyModule_AddStringConstant(PyObject*, const char*, const char*);
PyAPI_FUNC(PyObject* _Nullable) PyModule_GetDict(PyObject*);
PyAPI_FUNC(Py_ssize_t) PyNumber_AsSsize_t(PyObject* o, PyObject* _Nullable exc);
PyAPI_FUNC(PyObject* _Nullable) PyNumber_Float(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable) PyNumber_Long(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_Call(PyObject* callable, PyObject* _Nullable args,
                  PyObject* _Nullable kwargs);
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_CallFunction(PyObject* callable, const char* format, ...);
PyAPI_FUNC(PyObject* _Nullable) PyObject_CallFunctionObjArgs(PyObject* callable, ...)
    __attribute__((__sentinel__(0)));
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_CallMethod(PyObject* obj, const char* name, const char* format, ...);
PyAPI_FUNC(int) PyObject_DelItem(PyObject* o, PyObject* key);
PyAPI_FUNC(void) PyObject_Free(void* ptr);
PyAPI_FUNC(void) PyObject_GC_Del(void*);
PyAPI_FUNC(PyObject* _Nullable) _PyObject_GC_New(PyTypeObject*);
PyAPI_FUNC(void) PyObject_GC_Track(void*);
PyAPI_FUNC(void) PyObject_GC_UnTrack(void*);
PyAPI_FUNC(PyObject* _Nullable) PyObject_GenericGetAttr(PyObject*, PyObject*);
PyAPI_FUNC(int) PyObject_GenericSetAttr(PyObject*, PyObject*, PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyObject_Init(PyObject*, PyTypeObject*);
PyAPI_FUNC(int) PyObject_IsInstance(PyObject* object, PyObject* typeorclass);
PyAPI_FUNC(int) PyObject_IsSubclass(PyObject* object, PyObject* typeorclass);
PyAPI_FUNC(int) PyObject_IsTrue(PyObject*);
PyAPI_FUNC(Py_ssize_t) PyObject_Length(PyObject* o);
PyAPI_FUNC(void* _Nullable) PyObject_Malloc(size_t size);
PyAPI_FUNC(PyObject* _Nullable) _PyObject_New(PyTypeObject*);
PyAPI_FUNC(PyVarObject* _Nullable) _PyObject_NewVar(PyTypeObject*, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable) PyObject_Repr(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyObject_RichCompare(PyObject*, PyObject*, int);
PyAPI_FUNC(int) PyObject_RichCompareBool(PyObject*, PyObject*, int);
PyAPI_FUNC(int) PyObject_SetAttr(PyObject*, PyObject*, PyObject*);
PyAPI_FUNC(int) PyObject_SetAttrString(PyObject*, const char*, PyObject*);
PyAPI_FUNC(int) PyObject_SetItem(PyObject* o, PyObject* key, PyObject* v);
PyAPI_FUNC(Py_ssize_t) PyObject_Size(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable) PyObject_Str(PyObject*);
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_VectorcallMethod(PyObject* name, PyObject* _Nonnull const* _Nonnull args,
                              size_t    nargsf, PyObject* _Nullable kwnames);
PyAPI_FUNC(int) PySequence_Check(PyObject* o);
PyAPI_FUNC(int) PySequence_Contains(PyObject* seq, PyObject* ob);
PyAPI_FUNC(int) PySequence_DelItem(PyObject* o, Py_ssize_t i);
PyAPI_FUNC(PyObject* _Nullable) PySequence_Fast(PyObject* o, const char* m);
PyAPI_FUNC(PyObject* _Nullable) PySequence_GetItem(PyObject* o, Py_ssize_t i);
PyAPI_FUNC(Py_ssize_t) PySequence_Length(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable) PySequence_List(PyObject* o);
PyAPI_FUNC(int) PySequence_SetItem(PyObject* o, Py_ssize_t i, PyObject* v);
PyAPI_FUNC(Py_ssize_t) PySequence_Size(PyObject* o);
PyAPI_FUNC(PyObject* _Nullable) PySequence_Tuple(PyObject* o);
PyAPI_FUNC(int) PySet_Add(PyObject* set, PyObject* key);
PyAPI_FUNC(int) PySet_Clear(PyObject* set);
PyAPI_FUNC(int) PySet_Discard(PyObject* set, PyObject* key);
PyAPI_FUNC(PyObject* _Nullable) PySet_New(PyObject* _Nullable);
PyAPI_FUNC(Py_ssize_t) PySet_Size(PyObject* anyset);
PyAPI_FUNC(int) PySlice_Unpack(PyObject* slice, Py_ssize_t* start, Py_ssize_t* stop,
                               Py_ssize_t* step);
PyAPI_FUNC(Py_ssize_t) PySlice_AdjustIndices(Py_ssize_t length, Py_ssize_t* start,
                                             Py_ssize_t* stop, Py_ssize_t step);
PyAPI_FUNC(PyObject* _Nullable) PyTuple_GetItem(PyObject*, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable) PyTuple_GetSlice(PyObject*, Py_ssize_t, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable) PyTuple_New(Py_ssize_t size);
PyAPI_FUNC(int) PyTuple_SetItem(PyObject*, Py_ssize_t, PyObject*);
PyAPI_FUNC(Py_ssize_t) PyTuple_Size(PyObject*);
static inline int _PyType_Check(PyObject* op);
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpec(PyType_Spec*);
PyAPI_FUNC(PyObject* _Nullable) PyType_GenericAlloc(PyTypeObject*, Py_ssize_t);
PyAPI_FUNC(PyObject* _Nullable)
    PyType_GenericNew(PyTypeObject* type, PyObject* _Nullable args,
                      PyObject* _Nullable kwds);
PyAPI_FUNC(int) PyType_IsSubtype(PyTypeObject*, PyTypeObject*);
PyAPI_FUNC(void) PyType_Modified(PyTypeObject*);
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpec(PyType_Spec*);
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpecWithBases(PyType_Spec*, PyObject*);
PyAPI_FUNC(PyObject* _Nullable)
    PyType_FromModuleAndSpec(PyObject*, PyType_Spec*, PyObject*);
PyAPI_DATA(PyTypeObject) PyType_Type; /* built-in 'type' */
PyAPI_FUNC(void) PyUnicode_Append(PyObject* _Nullable* _Nonnull, PyObject*);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_AsEncodedString(PyObject* unicode, const char* _Nullable encoding,
                              const char* _Nullable errors);
PyAPI_FUNC(const char* _Nullable) PyUnicode_AsUTF8(PyObject* unicode);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_AsUTF8String(PyObject* unicode);
PyAPI_FUNC(wchar_t* _Nullable)
    PyUnicode_AsWideCharString(PyObject* unicode, Py_ssize_t* _Nullable size);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_Decode(const char* s, Py_ssize_t size, const char* _Nullable encoding,
                     const char* _Nullable errors);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_DecodeFSDefault(const char* s);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_DecodeUTF16(const char* s, Py_ssize_t size, const char* _Nullable errors,
                          int* _Nullable byteorder);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_DecodeUTF8(const char* s, Py_ssize_t size, const char* _Nullable errors);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_EncodeFSDefault(PyObject* v);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromFormat(const char* format, ...);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromObject(PyObject* object);
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromString(const char* u);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_FromStringAndSize(const char* u, Py_ssize_t size);
PyAPI_FUNC(Py_ssize_t) PyUnicode_GetLength(PyObject* unicode);
PyAPI_FUNC(void) PyUnicode_InternInPlace(PyObject* _Nonnull* _Nonnull);
PyAPI_FUNC(Py_UCS4) PyUnicode_ReadChar(PyObject* unicode, Py_ssize_t offset);
PyAPI_FUNC(PyObject* _Nullable)
    PyVectorcall_Call(PyObject* callable, PyObject* tuple, PyObject* dict);
PyAPI_FUNC(PyObject* _Nullable) Py_BuildValue(const char*, ...);
PyAPI_FUNC(void) _Py_NO_RETURN _Py_FatalErrorFunc(const char* func, const char* message);
PyAPI_FUNC(void) Py_Finalize(void);
PyAPI_FUNC(PyObject* _Nullable) Py_GenericAlias(PyObject*, PyObject*);
PyAPI_FUNC(int) Py_IsInitialized(void);
PyAPI_FUNC(int) Py_ReprEnter(PyObject*);
PyAPI_FUNC(void) Py_ReprLeave(PyObject*);
PyAPI_FUNC(int) PyObject_GetBuffer(PyObject* exporter, Py_buffer* view, int flags);
PyAPI_FUNC(void*) PyBuffer_GetPointer(Py_buffer* view, Py_ssize_t* indices);
PyAPI_FUNC(int)
    PyBuffer_ToContiguous(void* buf, Py_buffer* src, Py_ssize_t len, char order);
PyAPI_FUNC(int)
    PyBuffer_FromContiguous(Py_buffer* view, void* buf, Py_ssize_t len, char fort);
PyAPI_FUNC(int) PyBuffer_IsContiguous(const Py_buffer* view, char fort);
PyAPI_FUNC(int) PyBuffer_FillInfo(Py_buffer* view, PyObject* _Nullable exporter,
                                  void* buf, Py_ssize_t len, int readonly, int flags);
PyAPI_FUNC(void) PyBuffer_Release(Py_buffer* view);
PyAPI_FUNC(const Py_buffer*) PyPickleBuffer_GetBuffer(PyObject*);
PyAPI_FUNC(PyObject* _Nullable) PyMemoryView_FromBuffer(Py_buffer* info);
NS_ASSUME_NONNULL_END
#endif /* USE_STATIC_ANALYZER */
