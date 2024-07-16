#include "Python.h"
#include "pyobjc-api.h"
#include <arpa/inet.h>
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/un.h>

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface PyObjCTestSockAddr : NSObject {
}
@end

static NSString* _Nullable addr2string(void* addr, int addrlen)
{
    char buf[NI_MAXHOST];
    int  error;

    error = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0, NI_NUMERICHOST);
    if (error) {
        return NULL;
    }
    return [NSString stringWithUTF8String:buf];
}

@implementation PyObjCTestSockAddr
+ (NSObject* _Nullable)sockAddrToValue:(struct sockaddr*)addr
{
    NSMutableArray* _Nullable array = [NSMutableArray array];
    NSObject* value;

    switch (addr->sa_family) {
    case AF_INET:
        [array addObject:@"IPv4"];
        value = addr2string(addr, sizeof(struct sockaddr_in));
        if (!value)
            return nil;
        [array addObject:value];

        value = [NSNumber numberWithShort:ntohs(((struct sockaddr_in*)addr)->sin_port)];
        if (!value)
            return nil;
        [array addObject:value];
        return array;
        break;
    case AF_INET6:
        [array addObject:@"IPv6"];
        value = addr2string(addr, sizeof(struct sockaddr_in6));
        if (!value)
            return nil;
        [array addObject:value];

        value = [NSNumber numberWithShort:ntohs(((struct sockaddr_in6*)addr)->sin6_port)];
        if (!value)
            return nil;
        [array addObject:value];

        value = [NSNumber
            numberWithUnsignedLong:(((struct sockaddr_in6*)addr)->sin6_flowinfo)];
        if (!value)
            return nil;
        [array addObject:value];
        value = [NSNumber
            numberWithUnsignedLong:(((struct sockaddr_in6*)addr)->sin6_scope_id)];
        if (!value)
            return nil;
        [array addObject:value];
        return array;
        break;
    case AF_UNIX:
        [array addObject:@"UNIX"];
        value = [NSString stringWithUTF8String:((struct sockaddr_un*)addr)->sun_path];
        if (!value)
            return nil;
        [array addObject:value];
        return array;

    default:
        return NULL;
    }
}

+ (void)getIPv4Addr:(struct sockaddr*)buf
{
    struct sockaddr_in* addr = (struct sockaddr_in*)buf;
    addr->sin_family         = AF_INET;
    addr->sin_port           = htons(80);
    ascii2addr(AF_INET, "127.0.0.1", &addr->sin_addr);
}

+ (void)getIPv6Addr:(struct sockaddr*)buf
{
    struct sockaddr_in6* addr     = (struct sockaddr_in6*)buf;
    addr->sin6_family             = AF_INET6;
    addr->sin6_port               = htons(443);
    addr->sin6_flowinfo           = 2;
    addr->sin6_scope_id           = 3;
    ((char*)&addr->sin6_addr)[0]  = 0;
    ((char*)&addr->sin6_addr)[1]  = 0;
    ((char*)&addr->sin6_addr)[2]  = 0;
    ((char*)&addr->sin6_addr)[3]  = 0;
    ((char*)&addr->sin6_addr)[4]  = 0;
    ((char*)&addr->sin6_addr)[5]  = 0;
    ((char*)&addr->sin6_addr)[6]  = 0;
    ((char*)&addr->sin6_addr)[7]  = 0;
    ((char*)&addr->sin6_addr)[8]  = 0;
    ((char*)&addr->sin6_addr)[9]  = 0;
    ((char*)&addr->sin6_addr)[10] = 0;
    ((char*)&addr->sin6_addr)[11] = 0;
    ((char*)&addr->sin6_addr)[12] = 0;
    ((char*)&addr->sin6_addr)[13] = 0;
    ((char*)&addr->sin6_addr)[14] = 0;
    ((char*)&addr->sin6_addr)[15] = 1;
}

+ (void)getUnixAddr:(struct sockaddr*)buf
{
    struct sockaddr_un* addr = (struct sockaddr_un*)buf;
    addr->sun_family         = AF_UNIX;
    strcpy(addr->sun_path, "/tmp/socket.addr");
    addr->sun_len = sizeof(*addr);
}

+ (void)getSystemAddr:(struct sockaddr*)buf
{
    buf->sa_len    = sizeof(struct sockaddr);
    buf->sa_family = AF_SYSTEM;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "PyObjCTestSockAddr",
                           PyObjC_IdToPython([PyObjCTestSockAddr class]))
        < 0) {
        return -1;
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "sockaddr",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_sockaddr(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_sockaddr(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
