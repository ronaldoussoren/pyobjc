/*
 * Special wrappers for NSNetService methods with 'difficult' arguments.
 *
 */
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/un.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable makeipaddr(struct sockaddr* addr, int addrlen)
{
    char      buf[NI_MAXHOST];
    int       error;
    PyObject* v;

    error = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0, NI_NUMERICHOST);
    if (error) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        v = Py_BuildValue("(is)", error, gai_strerror(error));
        PyErr_SetObject(PyExc_RuntimeError, v);
        Py_DECREF(v);
        return NULL;
        // LCOV_EXCL_STOP
    }
    return PyUnicode_FromString(buf);
}

static PyObject* _Nullable makesockaddr(struct sockaddr* addr, int addrlen)
{
    assert(addrlen != 0);

    switch (addr->sa_family) {

    case AF_INET: {
        struct sockaddr_in* a;
        PyObject*           addrobj = makeipaddr(addr, sizeof(*a));
        PyObject*           ret     = NULL;
        if (addrobj) {
            a   = (struct sockaddr_in*)addr;
            ret = Py_BuildValue("Oi", addrobj, ntohs(a->sin_port));
            Py_DECREF(addrobj);
        }
        return ret;
    }

    case AF_INET6: {
        struct sockaddr_in6* a;
        PyObject*            addrobj = makeipaddr(addr, sizeof(*a));
        PyObject*            ret     = NULL;
        if (addrobj) {
            a   = (struct sockaddr_in6*)addr;
            ret = Py_BuildValue("Oiii", addrobj, ntohs(a->sin6_port), a->sin6_flowinfo,
                                a->sin6_scope_id);
            Py_DECREF(addrobj);
        }
        return ret;
    }

    default:
        // LCOV_EXCL_START
        // This cannot happen, NSNetService only used IPv4 and IPv6.
        return Py_BuildValue("is#", addr->sa_family, addr->sa_data,
                             sizeof(addr->sa_data));
        // LCOV_EXCL_STOP
    }
}

static PyObject* _Nullable call_NSNetService_addresses(
    PyObject* method, PyObject* self, PyObject* _Nonnull const* _Nonnull arguments,
    size_t nargs)
{
    PyObject*         result;
    struct objc_super super;
    NSArray*          res;
    NSInteger         len, i;
    NSData*           item;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            super.super_class = PyObjCSelector_GetClass(method);
            super.receiver    = PyObjCObject_GetObject(self);

            res = ((id (*)(struct objc_super*, SEL))objc_msgSendSuper)(
                &super, @selector(addresses));
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            res = nil;                           // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (res == nil && PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;                    // LCOV_EXCL_LINE

    if (res == nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    len    = [res count];
    result = PyTuple_New(len);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    for (i = 0; i < len; i++) {

        PyObject* v;

        item = [res objectAtIndex:i];

        v = makesockaddr((struct sockaddr*)[item bytes], [item length]);
        if (v == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        PyTuple_SET_ITEM(result, i, v);
    }

    return result;
}

static int
setup_nsnetservice(PyObject* m __attribute__((__unused__)))
{
    Class classNSNetService = objc_lookUpClass("NSNetService");
    if (classNSNetService == NULL) { // LCOV_BR_EXCL_LINE
        return 0;                    // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterMethodMapping(classNSNetService, @selector(addresses),
                                     call_NSNetService_addresses,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) { // LCOV_BR_EXCL_LINE

        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
