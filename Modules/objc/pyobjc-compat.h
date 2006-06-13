#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

/* 
 * Compatibilty definitions 
 */


#ifdef MACOSX
#import <AvailabilityMacros.h>
/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define PyObjC_COMPILING_ON_MACOSX_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1
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

#if (PY_VERSION_HEX < 0x02050000)
typedef int Py_ssize_t;
#define PY_FORMAT_SIZE_T ""
#define Py_ARG_SIZE_T "i"
#define PY_SSIZE_T_MAX INT_MAX

#else

#define Py_ARG_SIZE_T "n"
#endif


#endif /* PyObjC_COMPAT_H */
