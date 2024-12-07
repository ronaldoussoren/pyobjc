#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

static Ivar _Nullable find_ivar(NSObject* base, const char* name)
{
    Class cur = object_getClass((id)base);
    Ivar  ivar;

    while (cur != nil) {
        ivar = class_getInstanceVariable(cur, name);
        if (ivar != nil) {
            return ivar;
        }
        cur = class_getSuperclass(cur);
    }
    return nil;
}

PyObject* _Nullable PyObjCIvar_Info(PyObject* self __attribute__((__unused__)),
                                    PyObject* object)
{
    Class     cur;
    PyObject* v;
    PyObject* result;
    int       r;

    if (PyObjCObject_Check(object)) {
        cur = object_getClass((id)PyObjCObject_GetObject(object));

    } else if (PyObjCClass_Check(object)) {
        cur = PyObjCClass_GetClass(object);

    } else {
        PyErr_Format(PyExc_TypeError, "not an Objective-C class or object");
        return NULL;
    }

    PyObjC_Assert(cur != NULL, NULL);

    result = PyList_New(0);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return result;    // LCOV_EXCL_LINE
    }

    /* Handle 'isa' specially, due to Objective-C 2.0 weirdness */
    v = Py_BuildValue("(sy)", "isa", @encode(Class));
    if (v == NULL) {       // LCOV_BR_EXCL_LINE
        Py_DECREF(result); // LCOV_EXCL_LINE
        return result;     // LCOV_EXCL_LINE
    }

    r = PyList_Append(result, v);
    Py_DECREF(v);
    if (r == -1) {         // LCOV_BR_EXCL_LINE
        Py_DECREF(result); // LCOV_EXCL_LINE
        return result;     // LCOV_EXCL_LINE
    }

    do {
        Ivar     ivar;
        Ivar*    ivarList;
        unsigned i, ivarCount;

        ivarList = class_copyIvarList(cur, &ivarCount);
        if (ivarList == NULL) {
            cur = class_getSuperclass(cur);
            continue;
        }

        for (i = 0; i < ivarCount; i++) {
            ivar                  = ivarList[i];
            const char* ivar_name = ivar_getName(ivar);

            if (ivar == NULL) // LCOV_BR_EXCL_LINE
                continue;     // LCOV_EXCL_LINE

            if (strcmp(ivar_name, "isa") == 0) {
                /* See comment above */
                continue;
            }

            v = Py_BuildValue("(sy)", ivar_name, ivar_getTypeEncoding(ivar));

            if (v == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(ivarList);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            r = PyList_Append(result, v);
            Py_DECREF(v);
            if (r == -1) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                free(ivarList);
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }
        }

        free(ivarList);

        cur = class_getSuperclass(cur);
    } while (cur != NULL); // LCOV_BR_EXCL_LINE

    return result;
}

PyObject* _Nullable PyObjCIvar_Get(PyObject* self __attribute__((__unused__)),
                                   PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"obj", "name", NULL};

    PyObject*   anObject;
    char*       name;
    Ivar        ivar;
    NSObject*   objcValue;
    PyObject*   result;
    const char* ivar_type;
    ptrdiff_t   ivar_offset;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "Os", keywords, &anObject, &name)) {
        return NULL;
    }

    if (!PyObjCObject_Check(anObject)) {
        PyErr_Format(PyExc_TypeError,
                     "Expecting an Objective-C object, got instance of %s",
                     Py_TYPE(anObject)->tp_name);
        return NULL;
    }

    objcValue = PyObjCObject_GetObject(anObject);
    if (objcValue == NULL) {
        PyErr_SetString(PyExc_ValueError, "Getting instance variable of a nil object");
        return NULL;
    }

    /* Shortcut for isa, mostly due to Objective-C 2.0 weirdness */
    if (strcmp(name, "isa") == 0) {
        Class cls = object_getClass(objcValue);
        return pythonify_c_value(@encode(Class), &cls);
    }

    ivar = find_ivar(objcValue, name);
    if (ivar == NULL) {
        PyErr_Format(PyExc_AttributeError, "%s", name);
        return NULL;
    }

    ivar_type   = ivar_getTypeEncoding(ivar);
    ivar_offset = ivar_getOffset(ivar);

    if (strcmp(ivar_type, @encode(PyObject*)) == 0) {
        result = *(PyObject**)(((char*)(objcValue)) + ivar_offset);
        Py_XINCREF(result);

    } else {
        result = pythonify_c_value(ivar_type, ((char*)(objcValue)) + ivar_offset);
    }

    return result;
}

PyObject* _Nullable PyObjCIvar_Set(PyObject* self __attribute__((__unused__)),
                                   PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"obj", "name", "value", "updateRefCounts", NULL};

    PyObject*   anObject;
    char*       name;
    Ivar        ivar;
    PyObject*   value;
    PyObject*   updateRefCounts = NULL;
    NSObject*   objcValue;
    int         result;
    const char* ivar_type;
    ptrdiff_t   ivar_offset;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OsO|O", keywords, &anObject, &name,
                                     &value, &updateRefCounts)) {
        return NULL;
    }

    if (!PyObjCObject_Check(anObject)) {
        PyErr_Format(PyExc_TypeError,
                     "Expecting an Objective-C object, got instance of %s",
                     Py_TYPE(anObject)->tp_name);
        return NULL;
    }

    objcValue = PyObjCObject_GetObject(anObject);
    if (objcValue == NULL) {
        PyErr_SetString(PyExc_ValueError, "Setting instance variable of a nil object");
        return NULL;
    }

    if (strcmp(name, "isa") == 0) {
        /*
         * Change the class of the object, this means we'll have to
         * update the python proxy object as well.
         */
        Class         cls;
        PyObject*     pycls;
        PyTypeObject* curType;

        result = depythonify_c_value(@encode(Class), value, &cls);
        if (result == -1) {
            return NULL;
        }

        (void)object_setClass(objcValue, cls);

        /* Note that 'value' doesn't have to be an instance
         * of PyObjCClass_Type, thanks to the indirection through
         * __pyobjc_object__ when converting to ObjC.
         */
        pycls = PyObjCClass_New(cls);
        if (pycls == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;     // LCOV_EXCL_LINE
        }

        /* XXX: See comment in objc-object.m, change python
         *      type by calling setattr(anObejct, "__class__", pycls)
         */
        curType = Py_TYPE(anObject);
        Py_SET_TYPE(anObject, (PyTypeObject*)pycls);
        Py_DECREF((PyObject*)curType);
        Py_RETURN_NONE;
    }

    ivar = find_ivar(objcValue, name);
    if (ivar == NULL) {
        PyErr_Format(PyExc_AttributeError, "%s", name);
        return NULL;
    }

    ivar_type   = ivar_getTypeEncoding(ivar);
    ivar_offset = ivar_getOffset(ivar);

    if (strcmp(ivar_type, @encode(PyObject*)) == 0) {
        /*
         * Python object, need to handle refcounts
         */
        SET_FIELD_INCREF(*(PyObject**)(((char*)(objcValue)) + ivar_offset), value);

    } else if (ivar_type[0] == _C_ID) {
        /*
         * Objective-C object, need to handle refcounts.
         */

        NSObject* tmpValue;

        if (updateRefCounts == NULL) {
            PyErr_SetString(PyExc_TypeError, "Instance variable is an object, "
                                             "updateRefCounts argument is required");
            return NULL;
        }

        result = depythonify_c_value(ivar_type, value, &tmpValue);
        if (result != 0) {
            return NULL;
        }

        if (PyObject_IsTrue(updateRefCounts)) {
            [tmpValue retain];

            id v = object_getIvar(objcValue, ivar);
            object_setIvar(objcValue, ivar, tmpValue);

            /* This uses -autorelease instead of -release because
             * there's a race between replacing the value here
             * and another thread getting the value. That is not
             * fixable by locking the Python proxy as the other thread
             * might run native ObjC/Swift code.
             *
             * Autoreleasing gives the other thread ample time to
             * call -retain (although there's still a race).
             */
            [v autorelease];
        } else {
            /*
             *   This can cause memory corruption when *tmpValue*
             *   isn't kept alive through other means, in general
             *   by storing it in a Cooa collection (just keeping
             *   the python variable alive isn't good enough when
             *   the *value* isn't a Cocoa object).
             */
            object_setIvar(objcValue, ivar, tmpValue);
        }

    } else {
        /* A simple value */

        result =
            depythonify_c_value(ivar_type, value, ((char*)(objcValue)) + ivar_offset);
        if (result != 0) {
            return NULL;
        }
    }

    Py_RETURN_NONE;
}

NS_ASSUME_NONNULL_END
