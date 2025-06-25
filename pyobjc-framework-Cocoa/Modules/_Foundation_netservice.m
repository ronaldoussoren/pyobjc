/*
 * Special wrappers for NSNetService methods with 'difficult' arguments.
 *
 */
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/un.h>

static PyObject*
makeipaddr(struct sockaddr* addr, int addrlen)
{
    char      buf[NI_MAXHOST];
    int       error;
    PyObject* v;

    error = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0, NI_NUMERICHOST);
    if (error) {
        v = Py_BuildValue("(is)", error, gai_strerror(error));
        PyErr_SetObject(PyExc_RuntimeError, v);
        Py_DECREF(v);
        return NULL;
    }
    return PyBytes_FromString(buf);
}

static PyObject*
makesockaddr(struct sockaddr* addr, int addrlen)
{
    if (addrlen == 0) {
        /* No address -- may be recvfrom() from known socket */
        Py_INCREF(Py_None);
        return Py_None;
    }

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

    case AF_UNIX: {
        struct sockaddr_un* a = (struct sockaddr_un*)addr;
        return PyBytes_FromString(a->sun_path);
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

        /* More cases here... */

    default:
        /* If we don't know the address family, don't raise an
           exception -- return it as a tuple. */
        return Py_BuildValue("is#", addr->sa_family, addr->sa_data,
                             sizeof(addr->sa_data));
    }
}

static PyObject*
call_NSNetService_addresses(PyObject* method, PyObject* self, PyObject* const* arguments,
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

            res = ((id (*)(struct objc_super*, SEL))objc_msgSendSuper)(&super, @selector
                                                                       (addresses));
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            res = nil;
        }
    Py_END_ALLOW_THREADS

    if (res == nil && PyErr_Occurred()) {
        return NULL;
    }

    if (res == nil) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    len    = [res count];
    result = PyTuple_New(len);
    if (result == NULL) {
        return NULL;
    }

    for (i = 0; i < len; i++) {

        PyObject* v;

        item = [res objectAtIndex:i];

        v = makesockaddr((struct sockaddr*)[item bytes], [item length]);
        if (v == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        PyTuple_SetItem(result, i, v);
    }

    return result;
}

static int
setup_nsnetservice(PyObject* m __attribute__((__unused__)))
{
    Class classNSNetService = objc_lookUpClass("NSNetService");
    if (classNSNetService == NULL) {
        return 0;
    }

    if (PyObjC_RegisterMethodMapping(classNSNetService, @selector(addresses),
                                     call_NSNetService_addresses,
                                     PyObjCUnsupportedMethod_IMP)
        < 0) {

        return -1;
    }

    return 0;
}
