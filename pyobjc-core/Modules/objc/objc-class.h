#ifndef PyObjC_OBJC_CLASS_H
#define PyObjC_OBJC_CLASS_H

NS_ASSUME_NONNULL_BEGIN

/*!
 * @header objc-class.m
 * @abstract Definition of the wrapper for Objective-C classes
 * @discussion
 *    This module implements the wrappers for Objective-C classes, included
 *    subclasses defined in Python.
 *
 *    The class-wrapper maintains a full __dict__ to make it easier to
 *    support introspection, and to make it easier to detect if someone
 *    does a super() call of a method.
 *
 *    Maintaining a full dict is problematic because the Objective-C runtime
 *    is fairly dynamic and does not have hooks to detect these changes. Our
 *    only way to detect changes is to periodicly check the runtime if
 *    something has changed. See the definition for PyObjCClassObject for
 *    an explanation.
 */

/*!
 * @const PyObjCClass_Type
 * @abstract The type objc.objc_class
 */
extern PyTypeObject PyObjCMetaClass_Type;
extern PyTypeObject PyObjCClass_Type;

/*!
 * @function PyObjCClass_Check
 * @abstract Check if an object is an Objective-C class
 * @param obj An object
 * @result Returns True if the object is an Objective-C class, false otherwise
 */
#define PyObjCClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCClass_Type)
#define PyObjCMetaClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCMetaClass_Type)

/*!
 * @struct PyObjCClassObject
 * @abstract The type struct for Objective-C classes (Python 2.3 and later)
 * @field base      Type actual type object
 * @field sel_to_py Mapping to speed up finding the correct Python method
 *                  for a selector.
 * @field dictoffset  Offset in the Objective-C instance for the instance
 *                    __dict__
 * @field delmethod  The method that implements __del__
 * @field hasPythonImpl True if the class is implemented in Python
 * @field generation   The value of PyObjC_MappingCount at the last time
 *                     the method-list was updated.
 * @field useKVO    should the class implement automatic KVO notifications?
 *
 * @discussion
 *      This struct is the type-object for on Objective-C class. It stores
 *      some additional information that is used to manage the interface
 *      with the Objective-C runtime.
 *
 *    dictoffset is used by objc-object.m to find the __dict__ for instances.
 *    If the offset is 0 there is no __dict__.
 *
 *    We store the __del__ implementation here instead of in the type itself
 *    to ensure that our teardown code is correctly called.
 */
typedef struct _PyObjCClassObject {
    PyHeapTypeObject base;
    Class class;
    PyObject* _Nullable sel_to_py;
    PyObject* _Nullable delmethod;
    PyObject* hiddenSelectors;
    PyObject* hiddenClassSelectors;
#ifdef PyObjC_ENABLE_LOOKUP_CACHE
    PyObject* _Nullable lookup_cache;
#endif

    Py_ssize_t               dictoffset;
    PyObjC_ATOMIC Py_ssize_t generation;
    unsigned int             useKVO : 1;
    unsigned int             hasPythonImpl : 1;
    unsigned int             isCFWrapper : 1;
    unsigned int             isFinal : 1;
} PyObjCClassObject;

extern PyObject* _Nullable PyObjCClass_DefaultModule;
extern PyObject* _Nullable PyObjCClass_New(Class objc_class);
extern Class _Nullable PyObjCClass_GetClass(PyObject* object);
extern PyObject* _Nullable PyObjCClass_FindSelector(PyObject* cls, SEL selector,
                                                    BOOL class_method);
extern void       PyObjCClass_MaybeRescan(PyObject* class);
extern int        ObjC_RegisterClassProxy(Class cls, PyObject* classProxy);
extern int        PyObjCClass_CheckMethodList(PyObject* cls, int recursive);
extern Py_ssize_t PyObjCClass_DictOffset(PyObject* cls);
extern PyObject* _Nullable PyObjCClass_GetDelMethod(PyObject* cls);
extern int PyObjCClass_HasPythonImplementation(PyObject* cls);
extern PyObject* _Nullable PyObjCClass_ClassForMetaClass(PyObject* meta);
extern PyObject* _Nullable PyObjCClass_HiddenSelector(
    PyObject* tp, SEL sel, BOOL classMethod); /* returns borrowed */
extern int PyObjCClass_SetHidden(PyObject* tp, SEL sel, BOOL classMethod,
                                 PyObject* metadata);
extern int PyObjCClass_AddMethods(PyObject*  cls, PyObject* _Nonnull* _Nonnull methods,
                                  Py_ssize_t count);
extern PyObject* _Nullable PyObjCClass_ListProperties(PyObject* cls);

/* Returns a borrowed reference or NULL (without necessarily raising an exception) */
extern PyObject* _Nullable PyObjCClass_TryResolveSelector(PyObject* base, PyObject* name,
                                                          SEL sel);
extern PyObject* _Nullable PyObjCMetaClass_TryResolveSelector(PyObject* base,
                                                              PyObject* name, SEL sel);

#ifdef PyObjC_ENABLE_LOOKUP_CACHE
static inline PyObject* _Nullable PyObjCClass_GetLookupCache(PyTypeObject* tp)
{
    PyObject* result = ((PyObjCClassObject*)tp)->lookup_cache;
    Py_XINCREF(result);
    return result;
}

static inline int
PyObjCClass_AddToLookupCache(PyTypeObject* _tp, PyObject* name, PyObject* value)
{
    int                r;
    PyObjCClassObject* tp = (PyObjCClassObject*)_tp;
    if (tp->lookup_cache == NULL) {
#ifdef Py_GIL_DISABLED
        Py_BEGIN_CRITICAL_SECTION(_tp);
        if (tp->lookup_cache == NULL) {
#endif
            tp->lookup_cache = PyDict_New();
            if (tp->lookup_cache == NULL) {
#ifdef Py_GIL_DISABLED
                Py_EXIT_CRITICAL_SECTION();
#endif
                return -1;
            }
#ifdef Py_GIL_DISABLED
        }
        Py_END_CRITICAL_SECTION();
#endif
    }
    r = PyDict_SetItem(tp->lookup_cache, name, value);
    return r;
}
#endif /* PyObjC_ENABLE_LOOKUP_CACHE */

static inline int
PyObjCClass_IsCFWrapper(PyTypeObject* tp)
{
    return ((PyObjCClassObject*)tp)->isCFWrapper;
}

static inline int
PyObjCClass_IsFinal(PyTypeObject* tp)
{
    return ((PyObjCClassObject*)tp)->isFinal;
}

PyObject* _Nullable objc_class_locate(Class objc_class);

extern int PyObjCClass_Setup(PyObject* module);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_OBJC_CLASS_H */
