__all__ = ['AsyncPythonInterpreter']

try:
    import fcntl
except:
    fcntl = None
import os
import sys
import socket
from StringIO import StringIO
from netrepr import NetRepr, RemoteObjectPool, RemoteObjectReference
from Foundation import *

IMPORT_MODULES = ['netrepr', 'remote_console', 'remote_pipe', 'remote_bootstrap']
source = StringIO()
for fn in IMPORT_MODULES:
    for line in file(fn+'.py', 'rU'):
        source.write(line)
    source.write('\n\n')
SOURCE = repr(source.getvalue()) + '\n'

def bind_and_listen(hostport):
    if isinstance(hostport, str):
        host, port = hostport.split(':')
        hostport = (host, int(port))
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set close-on-exec
    if hasattr(fcntl, 'FD_CLOEXEC'):
        old = fcntl.fcntl(serversock.fileno(), fcntl.F_GETFD)
        fcntl.fcntl(serversock.fileno(), fcntl.F_SETFD, old | fcntl.FD_CLOEXEC)
    # allow the address to be re-used in a reasonable amount of time
    if os.name == 'posix' and sys.platform != 'cygwin':
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    serversock.bind(hostport)
    serversock.listen(5)
    return serversock

class AsyncPythonInterpreter(NSObject):

    def init(self):
        self = super(AsyncPythonInterpreter, self).init()
        self.host = None
        self.port = None
        self.interpreterPath = None
        self.scriptPath = None
        self.commandReactor = None
        self.serverSocket = None
        self.serverFileHandle = None
        self.buffer = ''
        self.serverFileHandle = None
        self.remoteFileHandle = None
        self.childTask = None
        return self

    def initWithHost_port_interpreterPath_scriptPath_commandReactor_(self, host, port, interpreterPath, scriptPath, commandReactor):
        self = self.init()
        self.host = host
        self.port = port
        self.interpreterPath = interpreterPath
        self.scriptPath = scriptPath
        self.commandReactor = commandReactor
        self.serverSocket = None
        return self

    def bundleForClass(cls):
        # XXX - do something intelligent here
        return NSBundle.mainBundle()
    bundleForClass = classmethod(bundleForClass)
    
    def awakeFromNib(self):
        defaults = NSUserDefaults.standardUserDefaults()
        def default(k, v, typeCheck=None):
            rval = defaults.objectForKey_(k)
            if typeCheck is not None and rval is not None:
                if not isinstance(rval, typeCheck):
                    NSLog(u'%s failed type check %s with value %r' % (k, typeCheck.__name__, rval))
                    rval = None
            if rval is None:
                defaults.setObject_forKey_(v, k)
                rval = v
            return rval
        self.host = default(u'AsyncPythonInterpreterInterpreterHost', u'127.0.0.1', str)
        self.port = default(u'AsyncPythonInterpreterInterpreterPort', 0, int)
        self.interpreterPath = default(u'AsyncPythonInterpreterInterpreterPath', u'/usr/bin/python', unicode)
        self.scriptPath = type(self).bundleForClass().pathForResource_(u'tcpinterpreter.py')
    
    def connect(self):
        #NSLog(u'connect')
        self.serverSocket = bind_and_listen((self.host, self.port))
        self.serverFileHandle = NSFileHandle.alloc().initWithFileDescriptor_(self.serverSocket.fileno())
        nc = NSNotificationCenter.defaultCenter()
        nc.addObserver_selector_name_object_(
            self,
            'remoteSocketAccepted:',
            NSFileHandleConnectionAcceptedNotification,
            None)
        self.serverFileHandle.acceptConnectionInBackgroundAndNotify()
        self.remoteFileHandle = None
        self.childTask = NSTask.launchedTaskWithLaunchPath_arguments_(self.interpreterPath, [self.scriptPath, repr(self.serverSocket.getsockname())])
        nc.addObserver_selector_name_object_(
            self,
            'childTaskTerminated:',
            NSTaskDidTerminateNotification,
            None)
        return self

    def remoteSocketAccepted_(self, notification):
        #NSLog(u'remoteSocketAccepted_')
        self.serverFileHandle.closeFile()
        self.serverFileHandle = None
        ui = notification.userInfo()
        self.remoteFileHandle = ui.objectForKey_(NSFileHandleNotificationFileHandleItem)
        nc = NSNotificationCenter.defaultCenter()
        nc.addObserver_selector_name_object_(
            self,
            'remoteFileHandleReadCompleted:',
            NSFileHandleReadCompletionNotification,
            None)
        self.writeBytes_(SOURCE)
        self.remoteFileHandle.readInBackgroundAndNotify()
        self.commandReactor.connectionEstablished_(self)
        NSNotificationCenter.defaultCenter().postNotificationName_object_(u'AsyncPythonInterpreterOpened', self)

    def remoteFileHandleReadCompleted_(self, notification):
        #NSLog(u'remoteFileHandleReadCompleted_')
        ui = notification.userInfo()
        newData = ui.objectForKey_(NSFileHandleNotificationDataItem)
        if newData is None:
            self.close()
            NSLog(u'Error: %r' % (ui.objectForKey_(NSFileHandleError),))
            return
        bytes = newData.bytes()[:]
        if len(bytes) == 0:
            self.close()
            return
        self.remoteFileHandle.readInBackgroundAndNotify()
        start = len(self.buffer)
        buff = self.buffer + newData.bytes()[:]
        #NSLog(u'current buffer: %r' % (buff,))
        lines = []
        while True:
            linebreak = buff.find('\n', start) + 1
            if linebreak == 0:
                break
            lines.append(buff[:linebreak])
            buff = buff[linebreak:]
            start = 0
        #NSLog(u'lines: %r' % (lines,))
        self.buffer = buff
        for line in lines:
            self.commandReactor.lineReceived_fromConnection_(line, self)

    def writeBytes_(self, bytes):
        #NSLog(u'Writing bytes: %r' % (bytes,))
        self.remoteFileHandle.writeData_(NSData.dataWithBytes_length_(bytes, len(bytes)))
        #NSLog(u'bytes written.')
    
    def childTaskTerminated_(self, notification):
        #NSLog(u'childTaskTerminated_')
        self.close()

    def closeServerFileHandle(self):
        #NSLog(u'closeServerFileHandle')
        if self.serverFileHandle is not None:
            self.serverFileHandle.closeFile()
            self.serverFileHandle = None

    def closeRemoteFileHandle(self):
        #NSLog(u'closeRemoteFileHandle')
        if self.remoteFileHandle is not None:
            self.remoteFileHandle.closeFile()
            self.remoteFileHandle = None
    
    def terminateChildTask(self):
        #NSLog(u'terminateChildTask')
        if self.childTask is not None:
            self.childTask.terminate()
            self.childTask = None

    def close(self):
        #NSLog(u'close')
        if self.commandReactor is not None:
            self.commandReactor.connectionClosed_(self)
        NSNotificationCenter.defaultCenter().removeObserver_(self)
        self.closeServerFileHandle()
        self.closeRemoteFileHandle()
        self.terminateChildTask()
        NSNotificationCenter.defaultCenter().postNotificationName_object_(u'AsyncPythonInterpreterClosed', self)
    
    def __del__(self):
        self.close()
        
def test_console():
    from PyObjCTools import AppHelper
    from ConsoleReactor import ConsoleReactor
    host = '127.0.0.1'
    port = 0
    interpreterPath = sys.executable
    scriptPath = unicode(os.path.abspath('tcpinterpreter.py'))
    commandReactor = ConsoleReactor.alloc().init()
    interp = AsyncPythonInterpreter.alloc().initWithHost_port_interpreterPath_scriptPath_commandReactor_(host, port, interpreterPath, scriptPath, commandReactor)
    interp.connect()
    class ThisEventLoopStopper(NSObject):
        def interpFinished_(self, notification):
            AppHelper.stopEventLoop()
    stopper = ThisEventLoopStopper.alloc().init()
    NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(stopper, 'interpFinished:', u'AsyncPythonInterpreterClosed', interp)
    AppHelper.runConsoleEventLoop(installInterrupt=True)

def main():
    test_console()

if __name__ == '__main__':
    main()
