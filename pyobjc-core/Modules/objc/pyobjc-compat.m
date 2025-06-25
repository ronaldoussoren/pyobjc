#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

int
PyObjC_Cmp(PyObject* o1, PyObject* o2, int* result)
{
    int r;

    r = PyObject_RichCompareBool(o1, o2, Py_EQ);
    if (r == -1) {
        return -1;
    } else if (r == 1) {
        *result = 0;
        return 0;
    }

    r = PyObject_RichCompareBool(o1, o2, Py_LT);
    if (r == -1) {
        return -1;
    } else if (r == 1) {
        *result = -1;
        return 0;
    }

    r = PyObject_RichCompareBool(o1, o2, Py_GT);
    if (r == -1) {
        return 1;
    } else if (r == 1) {
        *result = 1;
        return 0;
    }

    PyErr_Format(PyExc_TypeError, "%R and %R cannot be compared", o1, o2);
    return -1;
}

/* XXX: Can we do without this function, it is a little too intimate with
 * unicode details.
 */
const char* _Nullable PyObjC_Unicode_Fast_Bytes(PyObject* object)
{
    /* Having a unicode string is a precondition, checked manually
     * that callers check the type beforehand.
     */
    assert(PyUnicode_Check(object));

    if (!PyUnicode_IS_ASCII(object)) {
        /* The code below raises the correct error in a roundabout
         * way. That's because UnicodeEncodeError expects more
         * than one argument.
         */
        PyObject* r = PyUnicode_AsASCIIString(object);
        if (unlikely(r != NULL)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_Error, "Raising UnicodeError failed");
            Py_DECREF(r);
            return NULL;
            // LCOV_EXCL_STOP
        }

        assert(r == NULL);
        return NULL;
    }

    return (const char*)(PyUnicode_DATA(object));
}

NS_ASSUME_NONNULL_END
