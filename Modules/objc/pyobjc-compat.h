#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H


/* 
 * Compatibilty definitions 
 */

/* Earlier versions of Python don't define PyDoc_STRVAR */
#ifndef PyDoc_STR
#define PyDoc_VAR(name)	        static char name[]
#define PyDoc_STR(str)	        (str)
#define PyDoc_STRVAR(name, str) PyDoc_VAR(name) = PyDoc_STR(str)
#endif


#if PY_VERSION_HEX >= 0x0203000A /* Python 2.3a0 or later */

#define PyObjCBool_Check(x) PyBool_Check(x)
#define PyObjCBool_FromLong(x) PyBool_FromLong(x)

#else /* Python 2.2 */

typedef PyIntObject PyObjCBoolObject;
extern  PyTypeObject PyObjCBool_Type;

#define PyObjCBool_Check(x) ((x)->ob_type == &PyObjCBool_Type)

/* Function to return a bool from a C long */
PyObject * PyObjCBool_FromLong(long);

#endif /* Python 2.2 */

#if PY_VERSION_HEX < 0x020300b0 

#ifndef PyObjC_API_H

typedef int PyGILState_STATE;

#define PyGILState_Ensure(void)  (0)
static inline void PyGILState_Release(
	PyGILState_STATE state __attribute__((__unused__))) 
{
	/* EMPTY */
}

#endif 

#endif

#ifdef MACOSX
#import <AvailabilityMacros.h>
/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define PyObjC_COMPILING_ON_MACOSX_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1
#error "No 10.1?"
#endif


#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif

#ifndef MAC_OS_X_VERSION_10_3
#define MAC_OS_X_VERSION_10_3 1030
#endif

#endif /* MACOSX */

/* On some versions of GCC <limits.h> defines LONG_LONG_MAX but not LLONG_MAX,
 * compensate.
 */
#ifndef LLONG_MIN
#ifdef LONG_LONG_MIN
#define LLONG_MIN LONG_LONG_MIN
#define LLONG_MAX LONG_LONG_MAX
#define ULLONG_MAX ULONG_LONG_MAX
#endif
#endif


#endif /* PyObjC_COMPAT_H */
