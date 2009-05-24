#ifndef PyObjC_COMPAT_H
#define PyObjC_COMPAT_H

#import <Cocoa/Cocoa.h>
#import <Foundation/NSObjCRuntime.h>


#ifndef CGFLOAT_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no CFFloat available???"
#endif

typedef float CGFloat;
#define CGFLOAT_MIN FLT_MIN
#define CGFLOAT_MAX FLT_MAX
#define CGFLOAT_IS_DOUBLE 0
#define CGFLOAT_DEFINED

#endif /* CGFLOAT_DEFINED */


#ifndef NSINTEGER_DEFINED

#ifdef __LP64__
# error "Huh? 64-bit but no NSINTEGER available???"
#endif

typedef int NSInteger;
typedef unsigned int NSUInteger;

#define NSIntegerMax    LONG_MAX
#define NSIntegerMin    LONG_MIN
#define NSUIntegerMax   ULONG_MAX

#define NSINTEGER_DEFINED

#endif


/* 
 * Compatibilty definitions 
 */

#ifdef __GNUC__
#define unlikely(x)	__builtin_expect (!!(x), 0)
#define likely(x)	__builtin_expect (!!(x), 1)
#else
#define likely(x)	x 
#define likely(x)	x 
#endif

#import <AvailabilityMacros.h>
/* On 10.1 there are no defines for the OS version. */
#ifndef MAC_OS_X_VERSION_10_1
#define MAC_OS_X_VERSION_10_1 1010
#define MAC_OS_X_VERSION_MAX_ALLOWED MAC_OS_X_VERSION_10_1

#error "MAC_OS_X_VERSION_10_1 not defined. You aren't running 10.1 are you?"

#endif


#ifndef MAC_OS_X_VERSION_10_2
#define MAC_OS_X_VERSION_10_2 1020
#endif

#ifndef MAC_OS_X_VERSION_10_3
#define MAC_OS_X_VERSION_10_3 1030
#endif

#ifndef MAC_OS_X_VERSION_10_4
#define MAC_OS_X_VERSION_10_4 1040
#endif

#ifndef MAC_OS_X_VERSION_10_5
#define MAC_OS_X_VERSION_10_5 1050
#endif


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

#ifndef Py_ARG_SIZE_T
#define Py_ARG_SIZE_T "n"
#endif

#endif


#endif /* PyObjC_COMPAT_H */
