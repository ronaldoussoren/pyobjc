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

PyAPI_FUNC(int) PyArg_Parse(PyObject*, const char*, ...)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyArg_ParseTuple(PyObject* _Nullable, const char*, ...)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int)
    PyArg_ParseTupleAndKeywords(PyObject* _Nullable, PyObject* _Nullable,
                                const char* _Nullable, char* _Nullable* _Nullable, ...)
        __attribute__((warn_unused_result));

PyAPI_FUNC(PyObject* _Nullable) PyBool_FromLong(long) __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyBuffer_Release(Py_buffer* view);
PyAPI_FUNC(char* _Nullable) PyByteArray_AsString(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyByteArray_FromObject(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyByteArray_FromStringAndSize(const char* _Nullable, Py_ssize_t)
        __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyByteArray_Resize(PyObject*, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyByteArray_Size(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(char* _Nullable) PyBytes_AsString(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyBytes_AsStringAndSize(PyObject*   obj, char* _Nullable* _Nonnull buffer,
                                        Py_ssize_t* _Nullablelength)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyBytes_FromString(const char*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyBytes_FromStringAndSize(const char* _Nullable, Py_ssize_t)
        __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)(PyCFunction_NewEx)(PyMethodDef* ml,
                                                   PyObject* _Nullable self,
                                                   PyObject* module)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    Py_CMethod_New(PyMethodDef* ml, PyObject* _Nullable self, PyObject* _Nullable module,
                   PyTypeObject* _Nullable cls) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyCallable_Check(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(void* _Nullable) PyCapsule_GetPointer(PyObject* capsule, const char* name)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject*) PyCapsule_New(void* _Nullable pointer, const char* _Nullable name,
                                    PyCapsule_Destructor _Nullable destructor)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDescr_IsData(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDictProxy_New(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_Copy(PyObject* mp)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_DelItem(PyObject* mp, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_DelItemString(PyObject* dp, const char* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItem(PyObject* mp, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItemString(PyObject* dp, const char* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) _PyDict_GetItemStringWithError(PyObject*, const char*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_GetItemWithError(PyObject* mp, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_Keys(PyObject* mp)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_New(void) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_Next(PyObject* p, Py_ssize_t* ppos, PyObject* _Nullable* _Nullable,
                            PyObject* _Nullable* _Nullable pvalue)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_SetItem(PyObject* mp, PyObject* key, PyObject* item)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_SetItemString(PyObject* dp, const char* key, PyObject* item)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyDict_Size(PyObject* mp) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyDict_Update(PyObject* mp, PyObject* other)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyDict_Values(PyObject* mp)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) _PyErr_BadInternalCall(const char* filename, int lineno);
PyAPI_FUNC(void) PyErr_Clear(void);
PyAPI_FUNC(void) _PyErr_Clear(PyThreadState* tstate);
PyAPI_FUNC(int) PyErr_ExceptionMatches(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(void)
    PyErr_Fetch(PyObject* _Nullable* _Nullable, PyObject* _Nullable* _Nullable,
                PyObject* _Nullable* _Nullable);
PyAPI_FUNC(PyObject* _Nullable)
    PyErr_Format(PyObject* exception, const char* format, ...);
PyAPI_FUNC(PyObject* _Nullable)
    PyErr_NewException(const char* name, PyObject* _Nullable base,
                       PyObject* _Nullable dict) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyErr_NoMemory(void);
PyAPI_FUNC(void)
    PyErr_NormalizeException(PyObject* _Nullable* _Nonnull, PyObject* _Nullable* _Nonnull,
                             PyObject* _Nullable* _Nonnull);
PyAPI_FUNC(PyObject* _Nullable) PyErr_Occurred(void) __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyErr_Print(void);
PyAPI_FUNC(void)
    PyErr_Restore(PyObject* _Nullable, PyObject* _Nullable, PyObject* _Nullable);
PyAPI_FUNC(PyObject* _Nullable) PyErr_SetFromErrno(PyObject*);
PyAPI_FUNC(void) PyErr_SetObject(PyObject*, PyObject*);
PyAPI_FUNC(void) PyErr_SetString(PyObject* type, const char* message);
PyAPI_FUNC(int) PyErr_WarnEx(PyObject* category, const char* message,
                             Py_ssize_t stack_level) __attribute__((warn_unused_result));
PyAPI_FUNC(int)
    PyErr_WarnFormat(PyObject* category, Py_ssize_t stack_level, const char* format, ...)
        __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyErr_WriteUnraisable(PyObject* _Nullable);
Py_DEPRECATED(3.9) PyAPI_FUNC(void) PyEval_InitThreads(void);
PyAPI_FUNC(double) PyFloat_AsDouble(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyFloat_FromDouble(double)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyFrozenSet_New(PyObject* _Nullable)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyFunction_GetCode(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyGILState_STATE) PyGILState_Ensure(void) __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyGILState_Release(PyGILState_STATE);
PyAPI_FUNC(PyObject* _Nullable) PyImport_Import(PyObject* name)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyImport_ImportModule(const char* name)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyIndex_Check(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyIter_Next(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyList_Append(PyObject*, PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyList_AsTuple(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyList_GetItem(PyObject*, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyList_New(Py_ssize_t size)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyList_Size(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(double) PyLong_AsDouble(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(long) PyLong_AsLong(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(long long) PyLong_AsLongLong(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyLong_AsSsize_t(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(unsigned long) PyLong_AsUnsignedLong(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(unsigned long long) PyLong_AsUnsignedLongLong(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(unsigned long long) PyLong_AsUnsignedLongLongMask(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void*) PyLong_AsVoidPtr(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromLong(long) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromLongLong(long long)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromSize_t(size_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromSsize_t(Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromUnsignedLong(unsigned long)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromUnsignedLongLong(unsigned long long)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyLong_FromVoidPtr(void* _Nullable)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMapping_Keys(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMapping_Values(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void* _Nullable) PyMem_Malloc(size_t size) __attribute__((warn_unused_result));
PyAPI_FUNC(void* _Nullable) PyMem_Realloc(void* _Nullable ptr, size_t new_size)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMember_GetOne(const char*, struct PyMemberDef*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyMember_SetOne(char*, struct PyMemberDef*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMemoryView_FromBuffer(const Py_buffer* info)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMethod_Function(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMethod_Self(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyModule_AddIntConstant(PyObject*, const char*, long)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyModule_AddObject(PyObject* mod, const char*, PyObject* value)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyModule_AddStringConstant(PyObject*, const char*, const char*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyModule_GetDict(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyNumber_AsSsize_t(PyObject* o, PyObject* _Nullable exc)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyNumber_Float(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyNumber_Long(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_Call(PyObject* callable, PyObject* _Nullable args,
                  PyObject* _Nullable kwargs) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_CallFunction(PyObject* callable, const char* format, ...)
        __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyObject_CallFunctionObjArgs(PyObject* callable, ...)
    __attribute__((__sentinel__(0))) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_CallMethod(PyObject* obj, const char* name, const char* format, ...)
        __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_DelItem(PyObject* o, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyObject_Free(void* ptr);
PyAPI_FUNC(void) PyObject_GC_Del(void*);
PyAPI_FUNC(PyObject* _Nullable) _PyObject_GC_New(PyTypeObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyObject_GC_Track(void*);
PyAPI_FUNC(void) PyObject_GC_UnTrack(void*);
PyAPI_FUNC(PyObject* _Nullable) PyObject_GenericGetAttr(PyObject*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_GenericSetAttr(PyObject*, PyObject*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyObject_Init(PyObject*, PyTypeObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_IsInstance(PyObject* object, PyObject* typeorclass)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_IsSubclass(PyObject* object, PyObject* typeorclass)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_IsTrue(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyObject_Length(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(void* _Nullable) PyObject_Malloc(size_t size)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) _PyObject_New(PyTypeObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyVarObject* _Nullable) _PyObject_NewVar(PyTypeObject*, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyObject_Repr(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyObject_RichCompare(PyObject*, PyObject*, int)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_RichCompareBool(PyObject*, PyObject*, int)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_SetAttr(PyObject*, PyObject*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_SetAttrString(PyObject*, const char*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyObject_SetItem(PyObject* o, PyObject* key, PyObject* v)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyObject_Size(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyObject_Str(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyObject_VectorcallMethod(PyObject* name, PyObject* _Nonnull const* _Nonnull args,
                              size_t    nargsf, PyObject* _Nullable kwnames)
        __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySequence_Check(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySequence_Contains(PyObject* seq, PyObject* ob)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySequence_DelItem(PyObject* o, Py_ssize_t i)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PySequence_Fast(PyObject* o, const char* m)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PySequence_GetItem(PyObject* o, Py_ssize_t i)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PySequence_Length(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PySequence_List(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySequence_SetItem(PyObject* o, Py_ssize_t i, PyObject* v)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PySequence_Size(PyObject* o) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PySequence_Tuple(PyObject* o)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySet_Add(PyObject* set, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySet_Clear(PyObject* set) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySet_Discard(PyObject* set, PyObject* key)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PySet_New(PyObject* _Nullable)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PySet_Size(PyObject* anyset) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySlice_Unpack(PyObject* slice, Py_ssize_t* start, Py_ssize_t* stop,
                               Py_ssize_t* step) __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PySlice_AdjustIndices(Py_ssize_t length, Py_ssize_t* start,
                                             Py_ssize_t* stop, Py_ssize_t step);
PyAPI_FUNC(PyObject* _Nullable) PyTuple_GetItem(PyObject*, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyTuple_GetSlice(PyObject*, Py_ssize_t, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyTuple_New(Py_ssize_t size)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyTuple_SetItem(PyObject*, Py_ssize_t, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyTuple_Size(PyObject*) __attribute__((warn_unused_result));
static inline int _PyType_Check(PyObject* op);
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpec(PyType_Spec*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyType_GenericAlloc(PyTypeObject*, Py_ssize_t)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyType_GenericNew(PyTypeObject* type, PyObject* _Nullable args,
                      PyObject* _Nullable kwds) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyType_IsSubtype(PyTypeObject*, PyTypeObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyType_Modified(PyTypeObject*);
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpec(PyType_Spec*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyType_FromSpecWithBases(PyType_Spec*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyType_FromModuleAndSpec(PyObject*, PyType_Spec*, PyObject*)
        __attribute__((warn_unused_result));
PyAPI_DATA(PyTypeObject) PyType_Type; /* built-in 'type' */
PyAPI_FUNC(void) PyUnicode_Append(PyObject* _Nullable* _Nonnull, PyObject*);
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_AsEncodedString(PyObject* unicode, const char* _Nullable encoding,
                              const char* _Nullable errors)
        __attribute__((warn_unused_result));
PyAPI_FUNC(const char* _Nullable) PyUnicode_AsUTF8(PyObject* unicode)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_AsUTF8String(PyObject* unicode)
    __attribute__((warn_unused_result));
PyAPI_FUNC(wchar_t* _Nullable)
    PyUnicode_AsWideCharString(PyObject* unicode, Py_ssize_t* _Nullable size)
        __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_Decode(const char* s, Py_ssize_t size, const char* _Nullable encoding,
                     const char* _Nullable errors) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_DecodeFSDefault(const char* s)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_DecodeUTF16(const char* s, Py_ssize_t size, const char* _Nullable errors,
                          int* _Nullable byteorder) __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_DecodeUTF8(const char* s, Py_ssize_t size, const char* _Nullable errors)
        __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_EncodeFSDefault(PyObject* v)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromFormat(const char* format, ...)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromObject(PyObject* object)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyUnicode_FromString(const char* u)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyUnicode_FromStringAndSize(const char* u, Py_ssize_t size)
        __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PyUnicode_GetLength(PyObject* unicode)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyUnicode_InternInPlace(PyObject* _Nonnull* _Nonnull);
PyAPI_FUNC(Py_UCS4) PyUnicode_ReadChar(PyObject* unicode, Py_ssize_t offset)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable)
    PyVectorcall_Call(PyObject* callable, PyObject* tuple, PyObject* dict)
        __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) Py_BuildValue(const char*, ...)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) _Py_NO_RETURN _Py_FatalErrorFunc(const char* func, const char* message);
PyAPI_FUNC(void) Py_Finalize(void);
PyAPI_FUNC(PyObject* _Nullable) Py_GenericAlias(PyObject*, PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) Py_IsInitialized(void) __attribute__((warn_unused_result));
PyAPI_FUNC(int) Py_ReprEnter(PyObject*) __attribute__((warn_unused_result));
PyAPI_FUNC(void) Py_ReprLeave(PyObject*);
PyAPI_FUNC(int) PyObject_GetBuffer(PyObject* exporter, Py_buffer* view, int flags)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void*) PyBuffer_GetPointer(const Py_buffer* view, const Py_ssize_t* indices)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyBuffer_ToContiguous(void* buf, const Py_buffer* src, Py_ssize_t len,
                                      char order) __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyBuffer_FromContiguous(const Py_buffer* view, const void* buf,
                                        Py_ssize_t len, char fort)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyBuffer_IsContiguous(const Py_buffer* view, char fort)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PyBuffer_FillInfo(Py_buffer* view, PyObject* _Nullable exporter,
                                  void* buf, Py_ssize_t len, int readonly, int flags)
    __attribute__((warn_unused_result));
PyAPI_FUNC(void) PyBuffer_Release(Py_buffer* view);
PyAPI_FUNC(const Py_buffer*) PyPickleBuffer_GetBuffer(PyObject*)
    __attribute__((warn_unused_result));
PyAPI_FUNC(PyObject* _Nullable) PyMemoryView_FromBuffer(const Py_buffer* info)
    __attribute__((warn_unused_result));
PyAPI_FUNC(int) PySlice_Unpack(PyObject* slice, Py_ssize_t* start, Py_ssize_t* stop,
                               Py_ssize_t* step) __attribute__((warn_unused_result));
PyAPI_FUNC(Py_ssize_t) PySlice_AdjustIndices(Py_ssize_t length, Py_ssize_t* start,
                                             Py_ssize_t* stop, Py_ssize_t step)
    __attribute__((warn_unused_result));

NS_ASSUME_NONNULL_END
#endif /* USE_STATIC_ANALYZER */
