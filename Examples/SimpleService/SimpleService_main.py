from AppKit import *
from Foundation import *
from ServiceTest import *
from PyObjCTools import AppHelper

def main():
    #NSLog(u"main()")
    serviceProvider = ServiceTest.alloc().init()
    #NSLog(u"serviceProvider = %r" % (serviceProvider,))
    NSRegisterServicesProvider(serviceProvider, u"PyObjCSimpleService")
    #NSLog(u"registered as PyObjCSimpleService")
    AppHelper.runConsoleEventLoop()

if __name__ == '__main__':
    main()
