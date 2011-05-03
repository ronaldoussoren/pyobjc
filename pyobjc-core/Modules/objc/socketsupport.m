/*
 * Converting socketaddresses to/from Python in a way that is compatible with
 * the socket module.
 *
 * This code reimplements parts of the socket module, sadly enough the socket
 * module doesn't have enough of a public C API to do this otherwise.
 */

#include "pyobjc.h"

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>

static PyObject* socket_error = NULL;
static PyObject* socket_gaierror = NULL;

static int
setup_exceptions(void)
{
	PyObject* mod;

	mod = PyImport_ImportModule("socket");
	if (mod == NULL) {
		return -1;
	}

	Py_XDECREF(socket_error);
	socket_error = PyObject_GetAttrString(mod, "error");
	if (socket_error == NULL) {
		Py_DECREF(mod);
		return -1;
	}

	Py_XDECREF(socket_gaierror);
	socket_gaierror = PyObject_GetAttrString(mod, "gaierror");
	if (socket_gaierror == NULL) {
		Py_DECREF(mod);
		return -1;
	}

	Py_DECREF(mod);
	return 0;
}

static PyObject* 
set_gaierror(int error)
{
	if (error == EAI_SYSTEM) {
		if (socket_error == NULL) {
			if (setup_exceptions() == -1) {
				return NULL;
			}
		}
		PyErr_SetFromErrno(socket_error);
		return NULL;
	}

	PyObject* v = Py_BuildValue("is", error, gai_strerror(error));
	if (v != NULL) {
		if (socket_gaierror == NULL) {
			if (setup_exceptions() == -1) {
				return NULL;
			}
		}
		PyErr_SetObject(socket_gaierror, v);
		Py_DECREF(v);
		return NULL;
	}
	return NULL;
}

static PyObject*
makeipaddr(struct sockaddr* addr, int addrlen)
{
	char buf[NI_MAXHOST];
	int r;

	r = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0,
			NI_NUMERICHOST);
	if (r) {
		return set_gaierror(r);
	}
	return PyBytes_FromString(buf);
}

static int 
setipaddr(char* name, struct sockaddr* addr_ret, size_t addr_ret_size, int af)
{
	struct addrinfo hints, *res;
	int error;
	int d1, d2, d3, d4;
	char ch;

	memset((void *) addr_ret, '\0', sizeof(*addr_ret));
	if (name[0] == '\0') {
		int siz;
		memset(&hints, 0, sizeof(hints));
		hints.ai_family = af;
		hints.ai_socktype = SOCK_DGRAM;	/*dummy*/
		hints.ai_flags = AI_PASSIVE;
		error = getaddrinfo(NULL, "0", &hints, &res);
		/* We assume that those thread-unsafe getaddrinfo() versions
		   *are* safe regarding their return value, ie. that a
		   subsequent call to getaddrinfo() does not destroy the
		   outcome of the first call. */
		if (error) {
			set_gaierror(error);
			return -1;
		}
		switch (res->ai_family) {
		case AF_INET:
			siz = 4;
			break;
		case AF_INET6:
			siz = 16;
			break;
		default:
			freeaddrinfo(res);
			PyErr_SetString(socket_error,
				"unsupported address family");
			return -1;
		}
		if (res->ai_next) {
			freeaddrinfo(res);
			PyErr_SetString(socket_error,
				"wildcard resolved to multiple address");
			return -1;
		}
		if (res->ai_addrlen < addr_ret_size)
			addr_ret_size = res->ai_addrlen;
		memcpy(addr_ret, res->ai_addr, addr_ret_size);
		freeaddrinfo(res);
		return siz;
	}
	if (name[0] == '<' && strcmp(name, "<broadcast>") == 0) {
		struct sockaddr_in *sinaddr;
		if (af != AF_INET && af != AF_UNSPEC) {
			PyErr_SetString(socket_error,
				"address family mismatched");
			return -1;
		}
		sinaddr = (struct sockaddr_in *)addr_ret;
		memset((void *) sinaddr, '\0', sizeof(*sinaddr));
		sinaddr->sin_family = AF_INET;
		sinaddr->sin_len = sizeof(*sinaddr);
		sinaddr->sin_addr.s_addr = INADDR_BROADCAST;
		return sizeof(sinaddr->sin_addr);
	}
	if (sscanf(name, "%d.%d.%d.%d%c", &d1, &d2, &d3, &d4, &ch) == 4 &&
	    0 <= d1 && d1 <= 255 && 0 <= d2 && d2 <= 255 &&
	    0 <= d3 && d3 <= 255 && 0 <= d4 && d4 <= 255) {
		struct sockaddr_in *sinaddr;
		sinaddr = (struct sockaddr_in *)addr_ret;
		sinaddr->sin_addr.s_addr = htonl(
			((long) d1 << 24) | ((long) d2 << 16) |
			((long) d3 << 8) | ((long) d4 << 0));
		sinaddr->sin_family = AF_INET;
		sinaddr->sin_len = sizeof(*sinaddr);
		return 4;
	}
	memset(&hints, 0, sizeof(hints));
	hints.ai_family = af;
	error = getaddrinfo(name, NULL, &hints, &res);
	if (error) {
		set_gaierror(error);
		return -1;
	}
	if (res->ai_addrlen < addr_ret_size)
		addr_ret_size = res->ai_addrlen;
	memcpy((char *) addr_ret, res->ai_addr, addr_ret_size);
	freeaddrinfo(res);
	switch (addr_ret->sa_family) {
	case AF_INET:
		return 4;
	case AF_INET6:
		return 16;
	default:
		PyErr_SetString(socket_error, "unknown address family");
		return -1;
	}
}

PyObject*
PyObjC_SockAddrToPython(void* value)
{
	switch (((struct sockaddr*)value)->sa_family) {
	case AF_INET:
		{
			struct sockaddr_in* a = (struct sockaddr_in*)value;
			PyObject* addrobj = makeipaddr((struct sockaddr*)a, sizeof(*a));
			if (addrobj != NULL) {
				return Py_BuildValue("Ni", addrobj,
						ntohs(a->sin_port));
			}
			return NULL;
		}
	
	case AF_INET6:
		{
			struct sockaddr_in6* a = (struct sockaddr_in6*)value;
			PyObject* addrobj = makeipaddr((struct sockaddr*)a, sizeof(*a));
			if (addrobj != NULL) {
				return Py_BuildValue("Niii", addrobj,
						ntohs(a->sin6_port),
						a->sin6_flowinfo,
						a->sin6_scope_id);
			}
			return NULL;
		}

	default:
		PyErr_Format(PyExc_ValueError,
			"Don't know how to convert sockaddr family %d",
			((struct sockaddr*)value)->sa_family
		);
		return NULL;
	}
}

int
PyObjC_SockAddrFromPython(PyObject* value, void* buffer)
{
	if (PyTuple_Size(value) == 2) {
		/* IPv4 address */
		struct sockaddr_in* addr = (struct sockaddr_in*)buffer;
		char* host;
		int port, result;

		if (!PyArg_ParseTuple(value, "eti:getsockaddrarg",
				"idna", &host, &port)) {
			return -1;
		}
		result = setipaddr(host, (struct sockaddr*)addr,
				sizeof(*addr), AF_INET);
		PyMem_Free(host);
		if (result < 0) {
			return -1;
		}
		addr->sin_family = AF_INET;
		addr->sin_port = htons((short)port);
		return 0;
	
	} else {
		/* Must be a IPv6 address */
		struct sockaddr_in6* addr = (struct sockaddr_in6*)buffer;
		char* host;
		int port, flowinfo, scope_id, result;

		flowinfo = scope_id = 0;
		if (!PyArg_ParseTuple(value, "eti|ii",
			"idna", &host, &port, &flowinfo, &scope_id))  {

			return -1;
		}
		result = setipaddr(host, (struct sockaddr*)addr,
				sizeof(*addr), AF_INET6);
		PyMem_Free(host);
		if (result < 0) {
			return -1;
		}
		addr->sin6_family = AF_INET6;
		addr->sin6_port = htons((short)port);
		addr->sin6_flowinfo = flowinfo;
		addr->sin6_scope_id = scope_id;
		return 0;
	}
}
