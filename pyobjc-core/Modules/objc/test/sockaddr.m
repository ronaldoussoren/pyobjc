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

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "sockaddr", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* _Nullable PyInit_sockaddr(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_sockaddr(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjCTestSockAddr",
                           PyObjC_IdToPython([PyObjCTestSockAddr class]))
        < 0) {
        return NULL;
    }

    return m;
}

NS_ASSUME_NONNULL_END
