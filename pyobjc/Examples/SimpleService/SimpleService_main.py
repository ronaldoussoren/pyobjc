from Foundation import *
from ServiceTest import *

if __name__ == '__main__':
    serviceProvider = ServiceTest.alloc().init()
    NSRegisterServicesProvider(serviceProvider, u"PyObjCSimpleService")
    try:
        NSRunLoop.currentRunLoop().configureAsServer()
        NSRunLoop.currentRunLoop().run()
    except Exception, localException:
        NSLog(localException)
    
    del serviceProvider
