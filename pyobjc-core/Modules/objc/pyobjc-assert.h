#ifndef PyObjC_ASSERT_H
#define PyObjC_ASSERT_H

NS_ASSUME_NONNULL_BEGIN

/*
 * XXX: Move assertions to crash instead of raising exceptions (and
 *      check that assertions actually check code invariants).
 */

/* XXX: defined in pyobjc_util.m, move declaration */
extern PyObject* PyObjCExc_InternalError;

#ifdef PyObjC_DEBUG

#ifdef PyObjC_ERROR_ABORT
#define _PyObjC_InternalError_Bailout(args...)                                           \
    do {                                                                                 \
        fprintf(stderr, args);                                                           \
        abort();                                                                         \
    } while (0)

#else /* !PyObjC_ERROR_ABORT */
#define _PyObjC_InternalError_Bailout(args...) ((void)0)

#endif /* !PyObjC_ERROR_ABORT */

/* XXX: Always abort here because continuing is not really possible */
#define PyObjCErr_InternalError()                                                        \
    do {                                                                                 \
        (void)PyErr_Format(PyObjCExc_InternalError,                                      \
                           "PyObjC: internal error in %s at %s:%d", __FUNCTION__,        \
                           __FILE__, __LINE__);                                          \
        _PyObjC_InternalError_Bailout("PyObjC: internal error in %s at %s:%d\n",         \
                                      __FUNCTION__, __FILE__, __LINE__);                 \
        abort();                                                                         \
    } while (0)

#define PyObjCErr_InternalErrorMesg(msg)                                                 \
    do {                                                                                 \
        (void)PyErr_Format(PyObjCExc_InternalError,                                      \
                           "PyObjC: internal error in %s at %s:%d: %s", __FUNCTION__,    \
                           __FILE__, __LINE__, msg);                                     \
        _PyObjC_InternalError_Bailout("PyObjC: internal error in %s at %s:%d: %s\n",     \
                                      __FUNCTION__, __FILE__, __LINE__, msg);            \
    } while (0)

#define PyObjC_Assert(expr, retval)                                                      \
    do {                                                                                 \
        if (unlikely(!(expr))) {                                                         \
            PyObjCErr_InternalErrorMesg("assertion failed: " #expr);                     \
            return (retval);                                                             \
        }                                                                                \
    } while (0)
#else

#define PyObjCErr_InternalError() ((void)0)
#define PyObjCErr_InternalErrorMesg(mesg) ((void)0)

#define PyObjC_Assert(expr, retval) ((void)0)

#endif

NS_ASSUME_NONNULL_END

#endif /* PyObjC_ASSERT_H */
