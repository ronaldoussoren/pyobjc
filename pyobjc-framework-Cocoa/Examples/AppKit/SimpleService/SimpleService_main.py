from Cocoa import NSRegisterServicesProvider
from PyObjCTools import AppHelper
from ServiceTest import ServiceTest


def main():
    serviceProvider = ServiceTest.alloc().init()
    NSRegisterServicesProvider(serviceProvider, "PyObjCSimpleService")
    AppHelper.runConsoleEventLoop()


if __name__ == "__main__":
    main()
