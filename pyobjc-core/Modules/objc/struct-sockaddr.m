/*
 * Converting socketaddresses to/from Python in a way that is compatible with
 * the socket module.
 *
 * This code reimplements parts of the socket module, sadly enough the socket
 * module doesn't have enough of a public C API to do this otherwise.
 */

#include "pyobjc.h"

#include <arpa/inet.h>
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* socket_error    = NULL;
static PyObject* socket_gaierror = NULL;

int
PyObjC_SockAddr_Setup(PyObject* module __attribute__((__unused__)))
{
    /* XXX: Condider moving setting these through options.m */
    PyObject* mod;

    mod = PyImport_ImportModule("socket");
    if (mod == NULL) { // LCOV_BR_EXCL_LINE
        return -1;     // LCOV_EXCL_LINE
    }

    Py_XDECREF(socket_error);
    socket_error = PyObject_GetAttrString(mod, "error");
    if (socket_error == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(mod);
        return -1;
        // LCOV_EXCL_STOP
    }

    Py_XDECREF(socket_gaierror);
    socket_gaierror = PyObject_GetAttrString(mod, "gaierror");
    if (socket_gaierror == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(mod);
        return -1;
        // LCOV_EXCL_STOP
    }

    Py_DECREF(mod);
    return 0;
}

static void
set_gaierror(int error)
{
    if (error == EAI_SYSTEM) {
        PyErr_SetFromErrno(socket_error);
        return;
    }

    PyObject* v = Py_BuildValue("is", error, gai_strerror(error));
    if (v != NULL) {
        PyErr_SetObject(socket_gaierror, v);
        Py_DECREF(v);
    }
}

static PyObject* _Nullable makeipaddr(struct sockaddr* addr, int addrlen)
{
    char buf[NI_MAXHOST];
    int  r;

    r = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0, NI_NUMERICHOST);
    if (r != 0) { // LCOV_BR_EXCL_LINE
        /*
         * This should never fail due to NI_NUMERICHOST and having
         * a large enough buffer.
         */

        // LCOV_EXCL_START
        set_gaierror(r);
        return NULL;
        // LCOV_EXCL_STOP
    }
    return PyUnicode_FromString(buf);
}

static int
setipaddr(char* name, struct sockaddr* addr_ret, size_t addr_ret_size, int af)
{
    struct addrinfo hints, *res;
    int             error;

    memset((void*)addr_ret, '\0', sizeof(*addr_ret));
    if (name[0] == '\0') {
        int size;
        memset(&hints, 0, sizeof(hints));
        hints.ai_family   = af;
        hints.ai_socktype = SOCK_DGRAM; /*dummy*/
        hints.ai_flags    = AI_PASSIVE;
        error             = getaddrinfo(NULL, "0", &hints, &res);
        if (error) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            set_gaierror(error);
            return -1;
            // LCOV_EXCL_STOP
        }
        switch (res->ai_family) {
        case AF_INET:
            size = 4;
            break;

        case AF_INET6:
            size = 16;
            break;

        default:
            // LCOV_EXCL_START
            freeaddrinfo(res);
            PyErr_SetString(socket_error, "unsupported address family");
            return -1;
            // LCOV_EXCL_STOP
        }
        if (res->ai_next) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            freeaddrinfo(res);
            PyErr_SetString(socket_error, "wildcard resolved to multiple address");
            return -1;
            // LCOV_EXCL_STOP
        }
        if (res->ai_addrlen < addr_ret_size) // LCOV_BR_EXCL_LINE
            addr_ret_size = res->ai_addrlen; // LCOV_EXCL_LINE
        memcpy(addr_ret, res->ai_addr, addr_ret_size);
        freeaddrinfo(res);
        return size;
    }
    if (name[0] == '<' && strcmp(name, "<broadcast>") == 0) {
        struct sockaddr_in* sinaddr;
        if (af != AF_INET) {
            PyErr_SetString(socket_error, "address family mismatched");
            return -1;
        }
        sinaddr = (struct sockaddr_in*)addr_ret;
        memset((void*)sinaddr, '\0', sizeof(*sinaddr));
        sinaddr->sin_family      = AF_INET;
        sinaddr->sin_len         = sizeof(*sinaddr);
        sinaddr->sin_addr.s_addr = INADDR_BROADCAST;
        return sizeof(sinaddr->sin_addr);
    }
    if (inet_pton(AF_INET, name, &(((struct sockaddr_in*)addr_ret)->sin_addr)) == 1) {
        struct sockaddr_in* sinaddr;
        sinaddr             = (struct sockaddr_in*)addr_ret;
        sinaddr->sin_family = AF_INET;
        sinaddr->sin_len    = sizeof(*sinaddr);
        return 4;
    }
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = af;
    error           = getaddrinfo(name, NULL, &hints, &res);
    if (error) {
        set_gaierror(error);
        return -1;
    }
    if (res->ai_addrlen < addr_ret_size) { // LCOV_BR_EXCL_LINE
        addr_ret_size = res->ai_addrlen;   // LCOV_EXCL_LINE
    }
    memcpy((char*)addr_ret, res->ai_addr, addr_ret_size);
    freeaddrinfo(res);
    switch (addr_ret->sa_family) {
    case AF_INET:
        return 4;
    case AF_INET6:
        return 16;
        // LCOV_EXCL_START
    default:
        PyErr_SetString(socket_error, "unknown address family");
        return -1;
        // LCOV_EXCL_STOP
    }
}

PyObject*
PyObjC_SockAddrToPython(const void* value)
{
    switch (((struct sockaddr*)value)->sa_family) {
    case AF_INET: {
        struct sockaddr_in* a       = (struct sockaddr_in*)value;
        PyObject*           addrobj = makeipaddr((struct sockaddr*)a, sizeof(*a));
        if (addrobj == NULL) { // LCOV_BR_EXCL_LINE
            /* see comment in makeipaddr */
            return NULL; // LCOV_EXCL_LINE
        }
        return Py_BuildValue("Ni", addrobj, ntohs(a->sin_port));
    }

    case AF_INET6: {
        struct sockaddr_in6* a       = (struct sockaddr_in6*)value;
        PyObject*            addrobj = makeipaddr((struct sockaddr*)a, sizeof(*a));
        if (addrobj == NULL) { // LCOV_BR_EXCL_LINE
            /* see comment in makeipaddr */
            return NULL; // LCOV_EXCL_LINE
        }
        return Py_BuildValue("Niii", addrobj, ntohs(a->sin6_port), a->sin6_flowinfo,
                             a->sin6_scope_id);
    }

    case AF_UNIX: {
        /* XXX: Check for correctness */
        struct sockaddr_un* a = (struct sockaddr_un*)value;
        return PyUnicode_DecodeFSDefault(a->sun_path);
    }

    default:
        PyErr_Format(PyExc_ValueError, "Don't know how to convert sockaddr family %d",
                     ((struct sockaddr*)value)->sa_family);
        return NULL;
    }
}

int
PyObjC_SockAddrFromPython(PyObject* value, void* buffer)
{
    if (PyUnicode_Check(value) || PyBytes_Check(value)) {
        /* AF_UNIX */
        struct sockaddr_un* addr = (struct sockaddr_un*)buffer;
        char*               path;
        Py_ssize_t          len;

        addr->sun_family = AF_UNIX;

        if (PyUnicode_Check(value)) {
            value = PyUnicode_EncodeFSDefault(value);
            if (value == NULL) {
                return -1;
            }
        } else {
            Py_INCREF(value);
        }

        if (!PyArg_Parse(value, "y#", &path, &len)) {
            Py_DECREF(value);
            return -1;
        }
        /* XXX: Check for correctless (NUL byte at end, embedded NUL?) */
        if (len >= (Py_ssize_t)sizeof(addr->sun_path) - 1) {
            PyErr_SetString(PyExc_OSError, "AF_UNIX path too long");
            Py_DECREF(value);
            return -1;
        }
        memcpy(addr->sun_path, path, len);
        addr->sun_path[len] = 0;
        Py_DECREF(value);
        return 0;

    } else if (PyTuple_Size(value) == 2) {
        /* AF_INET */
        struct sockaddr_in* addr = (struct sockaddr_in*)buffer;
        char*               host;
        int                 port, result;

        if (!PyArg_ParseTuple(value, "eti:getsockaddrarg", "idna", &host, &port)) {
            return -1;
        }
        result = setipaddr(host, (struct sockaddr*)addr, sizeof(*addr), AF_INET);
        PyMem_Free(host);
        if (result < 0) {
            return -1;
        }
        addr->sin_family = AF_INET;
        addr->sin_port   = htons((short)port);
        return 0;

    } else {
        /* AF_INET6 */
        struct sockaddr_in6* addr = (struct sockaddr_in6*)buffer;
        char*                host;
        int                  port, flowinfo, scope_id, result;

        flowinfo = scope_id = 0;
        if (!PyArg_ParseTuple(value, "eti|ii", "idna", &host, &port, &flowinfo,
                              &scope_id)) {

            return -1;
        }
        result = setipaddr(host, (struct sockaddr*)addr, sizeof(*addr), AF_INET6);
        PyMem_Free(host);
        if (result < 0) {
            return -1;
        }
        addr->sin6_family   = AF_INET6;
        addr->sin6_port     = htons((short)port);
        addr->sin6_flowinfo = flowinfo;
        addr->sin6_scope_id = scope_id;
        return 0;
    }
}

NS_ASSUME_NONNULL_END
