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

IMPORT_MODULES = ['netrepr', 'remote_console', 'remote_pipe']
RUN_CODE = """
__file__ = "<test-client>"
import sys
pool = ObjectPool()
netrepr = NetRepr(pool).netrepr
namespace = globals()
namespace.update(pool.namespace)
__main__ = sys.modules['__main__']
assert namespace is not __main__.__dict__
pipe = RemotePipe(__runsocketcode__, __clientfile__, netrepr, namespace, pool)
interp = RemoteConsole(pipe, locals=__main__.__dict__)
interp.interact()
"""
source = StringIO()
for fn in IMPORT_MODULES:
    for line in file(fn+'.py', 'rU'):
        source.write(line)
    source.write('\n\n')
source.write(RUN_CODE)
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

    def initWithHost_port_interpreterPath_scriptPath_commandReactor_(self, host, port, interpreterPath, scriptPath, commandReactor):
        self = super(AsyncPythonInterpreter, self).init()
        self.host = host
        self.port = port
        self.interpreterPath = interpreterPath
        self.scriptPath = scriptPath
        self.commandReactor = commandReactor
        self.serverSocket = None
        self.serverFileHandle = None
        self.buffer = ''
        self.serverFileHandle = None
        self.remoteFileHandle = None
        self.childTask = None
        return self

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

    def close(self):
        #NSLog(u'close')
        if self.commandReactor is not None:
            self.commandReactor.connectionClosed_(self)
        NSNotificationCenter.defaultCenter().removeObserver_(self)
        self.closeServerFileHandle()
        self.closeRemoteFileHandle()
        self.childTask.terminate()
        # XXX
        from PyObjCTools import AppHelper
        AppHelper.stopEventLoop()
    
    def __del__(self):
        self.close()
        

class ConsoleReactor(NSObject):
    def init(self):
        self = super(ConsoleReactor, self).init()
        self.pool = None
        self.netReprCenter = None
        self.connection = None
        return self
    
    def connectionEstablished_(self, connection):
        #NSLog(u'connectionEstablished_')
        self.connection = connection
        self.pool = RemoteObjectPool(self.writeCode_)
        self.netReprCenter = NetRepr(self.pool)

    def connectionClosed_(self, connection):
        #NSLog(u'connectionClosed_')
        pass

    def writeCode_(self, code):
        #NSLog(u'writeCode_')
        self.connection.writeBytes_(repr(code) + '\n')
    
    def netEval_(self, s):
        #NSLog(u'netEval_')
        return eval(s, self.pool.namespace, self.pool.namespace)

    def lineReceived_fromConnection_(self, lineReceived, connection):
        #NSLog(u'lineReceived_fromConnection_')
        code = lineReceived.rstrip()
        if not code:
            return
        self.pool.push()
        command = map(self.netEval_, eval(code))
        try:
            self.handleCommand_(command)
        finally:
            self.pool.pop()

    def handleCommand_(self, command):
        #NSLog(u'handleCommand_')
        basic = command[0]
        sel = 'handle%sCommand:' % (basic.capitalize())
        cmd = command[1:]
        if not self.respondsToSelector_(sel):
            NSLog(u'%r does not respond to %r' % (self, command))
        else:
            # XXX - this crashes PyObjC??
            # self.performSelector_withObject_(sel, cmd)
            getattr(self, sel.replace(':', '_'))(cmd)

    def handleExpectCommand_(self, command):
        #NSLog(u'handleExpectCommand_')
        seq = command[0]
        name = command[1]
        args = command[2:]
        netrepr = self.netReprCenter.netrepr
        rval = None
        code = None
        if name == 'RemoteConsole.raw_input':
            try:
                rval = raw_input(*args)
            except EOFError:
                code = 'raise EOFError'
        elif name == 'RemoteConsole.write':
            sys.stdout.write(*args)
        elif name == 'RemoteConsole.displayhook':
            obj = args[0]
            if obj is None:
                pass
            elif isinstance(obj, RemoteObjectReference):
                # XXX - this should be fetched async?
                self.writeCode_('interp.write(repr(%s) + "\\n")' % (netrepr(obj),))
            else:
                print repr(obj)
        elif name.startswith('RemoteFileLike.'):
            fh = getattr(sys, args[0])
            meth = getattr(fh, name[len('RemoteFileLike.'):])
            rval = meth(*args[1:])
        else:
            NSLog(u'%r does not respond to expect %r' % (self, command,))
        if code is None:
            code = '__result__[%r] = %s' % (seq, netrepr(rval))
        self.writeCode_(code)

def test_console():
    from PyObjCTools import AppHelper
    host = '127.0.0.1'
    port = 0
    interpreterPath = sys.executable
    scriptPath = unicode(os.path.abspath('tcpinterpreter.py'))
    commandReactor = ConsoleReactor.alloc().init()
    interp = AsyncPythonInterpreter.alloc().initWithHost_port_interpreterPath_scriptPath_commandReactor_(host, port, interpreterPath, scriptPath, commandReactor)
    interp.connect()
    AppHelper.runConsoleEventLoop(installInterrupt=True)

def main():
    test_console()

if __name__ == '__main__':
    main()
