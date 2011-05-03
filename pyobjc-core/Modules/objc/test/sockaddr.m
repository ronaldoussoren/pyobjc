#include <Python.h>
#include "pyobjc-api.h"
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

#import <Foundation/Foundation.h>

@interface PyObjCTestSockAddr : NSObject
{
}
+(NSObject*)sockAddrToValue:(struct sockaddr*)addr;
+(void) getIPv4Addr:(struct sockaddr*)buf;
+(void) getIPv6Addr:(struct sockaddr*)buf;
@end

static NSString*
addr2string(void* addr, int addrlen)
{
	char buf[NI_MAXHOST];
	int error;

	error = getnameinfo(addr, addrlen, buf, sizeof(buf), NULL, 0,
			NI_NUMERICHOST);
	if (error) {
		return NULL;
	}
	return [NSString stringWithUTF8String:buf];
}


@implementation PyObjCTestSockAddr
+(NSObject*)sockAddrToValue:(struct sockaddr*)addr
{
	NSMutableArray* array = [NSMutableArray array];
		
	switch (addr->sa_family) {
	case AF_INET:
		[array addObject:@"IPv4"];
		[array addObject: addr2string(addr, sizeof(struct sockaddr_in))];
		[array addObject:[NSNumber numberWithShort:ntohs(((struct sockaddr_in*)addr)->sin_port)]];
		return array;
		break;
	case AF_INET6:
		[array addObject:@"IPv6"];
		[array addObject: addr2string(addr, sizeof(struct sockaddr_in6))];
		[array addObject: [NSNumber numberWithShort:ntohs(((struct sockaddr_in6*)addr)->sin6_port)]];
		[array addObject: [NSNumber numberWithUnsignedLong:(((struct sockaddr_in6*)addr)->sin6_flowinfo)]];
		[array addObject: [NSNumber numberWithUnsignedLong:(((struct sockaddr_in6*)addr)->sin6_scope_id)]];		
		return array;
		break;
	default:
		return NULL;
	}
}

+(void) getIPv4Addr:(struct sockaddr*)buf
{
	struct sockaddr_in* addr = (struct sockaddr_in*)buf;
	addr->sin_family = AF_INET;
	addr->sin_port = htons(80);
	ascii2addr(AF_INET, "127.0.0.1", &addr->sin_addr);
}

+(void) getIPv6Addr:(struct sockaddr*)buf
{
	struct sockaddr_in6* addr = (struct sockaddr_in6*)buf;
	addr->sin6_family = AF_INET6;
	addr->sin6_port = htons(443);
	addr->sin6_flowinfo = 2;
	addr->sin6_scope_id = 3;
	((char*)&addr->sin6_addr)[0] = 0;
	((char*)&addr->sin6_addr)[1] = 0;
	((char*)&addr->sin6_addr)[2] = 0;
	((char*)&addr->sin6_addr)[3] = 0;
	((char*)&addr->sin6_addr)[4] = 0;
	((char*)&addr->sin6_addr)[5] = 0;
	((char*)&addr->sin6_addr)[6] = 0;
	((char*)&addr->sin6_addr)[7] = 0;
	((char*)&addr->sin6_addr)[8] = 0;
	((char*)&addr->sin6_addr)[9] = 0;
	((char*)&addr->sin6_addr)[10] = 0;
	((char*)&addr->sin6_addr)[11] = 0;
	((char*)&addr->sin6_addr)[12] = 0;
	((char*)&addr->sin6_addr)[13] = 0;
	((char*)&addr->sin6_addr)[14] = 0;
	((char*)&addr->sin6_addr)[15] = 1;
}
@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0}
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"sockaddr",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_sockaddr(void);

PyObject*
PyInit_sockaddr(void)

#else

#define INITERROR() return
#define INITDONE() return

void initsockaddr(void);

void
initsockaddr(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("sockaddr", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjCTestSockAddr",
		PyObjCClass_New([PyObjCTestSockAddr class])) < 0) {
		INITERROR();
	}

	INITDONE();

}
