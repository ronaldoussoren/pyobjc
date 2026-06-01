#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/* Implementation for: -(PyObject*)__pyobjc_PythonObject__ on the SwiftObject root. We
 * cannot define a category on that type because the class definition isn't public.
 */
static PyObject* _Nullable instance_pyobjc_PythonObject(NSObject* self, SEL _sel
                                                        __attribute__((__unused__)))
{
    PyObject* rval;
    rval = PyObjC_FindPythonProxy(self);
    if (rval == NULL) {
        rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
        if (unlikely(rval == NULL)) { // LCOV_BR_EXCL_LINE
            return NULL;              // LCOV_EXCL_LINE
        }
    }

    PyObject* actual = PyObjC_RegisterPythonProxy(self, rval);
    Py_DECREF(rval);
    return actual;
}

static PyObject* _Nullable class_pyobjc_PythonObject(NSObject* self,
                                                     SEL _sel __attribute__((__unused__)))
{
    return (PyObject*)PyObjCClass_New((Class)self);
}

int
PyObjCSwiftObject_Setup(PyObject* module __attribute__((__unused__)))
{
    static char encodingBuf[128];

    snprintf(encodingBuf, sizeof(encodingBuf), "%s%c%c", @encode(PyObject*), _C_ID,
             _C_SEL);

    Class*       buffer    = NULL;
    unsigned int bufferLen = 0;

    buffer = objc_copyClassList(&bufferLen);
    if (buffer != NULL) {
        for (unsigned int i = 0; i < bufferLen; i++) {
            const char* name = class_getName(buffer[i]);
            const char* n;

            if ((n = strstr(name, "SwiftObject")) != NULL
                && strcmp(n, "SwiftObject") == 0) {
                if (unlikely(!class_addMethod( // LCOV_BR_EXCL_LINE
                        buffer[i], @selector(__pyobjc_PythonObject__),
                        (IMP)instance_pyobjc_PythonObject, encodingBuf))) {

                    // LCOV_EXCL_START
                    PyErr_Format(PyObjCExc_InternalError, "Cannot add category on %s",
                                 name);
                    return -1;
                    // LCOV_EXCL_STOP
                }

                if (unlikely(!class_addMethod( // LCOV_BR_EXCL_LINE
                        object_getClass(buffer[i]), @selector(__pyobjc_PythonObject__),
                        (IMP)class_pyobjc_PythonObject, encodingBuf))) {

                    // LCOV_EXCL_START
                    PyErr_Format(PyObjCExc_InternalError, "Cannot add category on %s",
                                 name);
                    return -1;
                    // LCOV_EXCL_STOP
                }
            }
        }
    }
    return 0;
}

NS_ASSUME_NONNULL_END
