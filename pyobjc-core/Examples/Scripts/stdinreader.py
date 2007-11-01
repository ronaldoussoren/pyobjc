from Foundation import *
from PyObjCTools import AppHelper

class FileObserver(NSObject):
    def initWithFileDescriptor_readCallback_errorCallback_(self,
            fileDescriptor, readCallback, errorCallback):
        self = self.init()
        self.readCallback = readCallback
        self.errorCallback = errorCallback
        self.fileHandle = NSFileHandle.alloc().initWithFileDescriptor_(
            fileDescriptor)
        self.nc = NSNotificationCenter.defaultCenter()
        self.nc.addObserver_selector_name_object_(
            self,
            'fileHandleReadCompleted:',
            NSFileHandleReadCompletionNotification,
            self.fileHandle)
        self.fileHandle.readInBackgroundAndNotify()
        return self

    def fileHandleReadCompleted_(self, aNotification):
        ui = aNotification.userInfo()
        newData = ui.objectForKey_(NSFileHandleNotificationDataItem)
        if newData is None:
            if self.errorCallback is not None:
                self.errorCallback(self, ui.objectForKey_(NSFileHandleError))
            self.close()
        else:
            self.fileHandle.readInBackgroundAndNotify()
            if self.readCallback is not None:
                self.readCallback(self, str(newData))

    def close(self):
        self.nc.removeObserver_(self)
        if self.fileHandle is not None:
            self.fileHandle.closeFile()
            self.fileHandle = None
        # break cycles in case these functions are closed over
        # an instance of us
        self.readCallback = None
        self.errorCallback = None

    def __del__(self):
        # Without this, if a notification fires after we are GC'ed
        # then the app will crash because NSNotificationCenter
        # doesn't retain observers.  In this example, it doesn't
        # matter, but it's worth pointing out.
        self.close()

def prompt():
    sys.stdout.write("write something: ")
    sys.stdout.flush()

def gotLine(observer, aLine):
    if aLine:
        print "you wrote:", aLine.rstrip()
        prompt()
    else:
        print ""
        AppHelper.stopEventLoop()

def gotError(observer, err):
    print "error:", err
    AppHelper.stopEventLoop()

if __name__ == '__main__':
    import sys
    observer = FileObserver.alloc().initWithFileDescriptor_readCallback_errorCallback_(
        sys.stdin.fileno(), gotLine, gotError)
    prompt()
    AppHelper.runConsoleEventLoop(installInterrupt=True)
