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
        self.connect()
    
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
        

class ConsoleReactor(NSObject):
    def init(self):
        self = super(ConsoleReactor, self).init()
        self.pool = None
        self.netReprCenter = None
        self.connection = None
        self.commands = {}
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

    def handleRespondCommand_(self, command):
        self.doCallback_sequence_args_(
            self.callbacks.pop(command[0]),
            command[0],
            command[1:],
        )

    def doCallback_sequence_args_(self, callback, seq, args):
        nr = self.netReprCenter
        try:
            rval = callback(*args)
        except Exception, e:
            code = 'raise ' + nr.netrepr_exception(e)
        else:
            code = '__result__[%r] = %s' % (seq, nr.netrepr(rval))
        self.writeCode_(code)
    
    def deferCallback_sequence_value_(self, callback, seq, value):
        self.commands[seq] = callback
        self.writeCode_('pipe.respond(%r, netrepr(%s))' % (seq, value))
    
    def handleExpectCommand_(self, command):
        #NSLog(u'handleExpectCommand_')
        seq = command[0]
        name = command[1]
        args = command[2:]
        netrepr = self.netReprCenter.netrepr
        rval = None
        code = None
        if name == 'RemoteConsole.raw_input':
            self.doCallback_sequence_args_(raw_input, seq, args)
        elif name == 'RemoteConsole.write':
            self.doCallback_sequence_args_(sys.stdout.write, seq, args)
        elif name == 'RemoteConsole.displayhook':
            obj = args[0]
            def displayhook_respond(reprobject):
                print reprobject
            def displayhook_local(obj):
                if obj is not None:
                    displayhook_respond(repr(obj))
            if isinstance(obj, RemoteObjectReference):
                self.deferCallback_sequence_value_(displayhook_respond, seq, 'repr(%s)' % (netrepr(obj),))
            else:
                self.doCallback_sequence_args_(displayhook_local, seq, args)
        elif name.startswith('RemoteFileLike.'):
            fh = getattr(sys, args[0])
            meth = getattr(fh, name[len('RemoteFileLike.'):])
            self.doCallback_sequence_args_(meth, seq, args[1:])
        else:
            self.doCallback_sequence_args_(NSLog, seq, [u'%r does not respond to expect %r' % (self, command,)])

def test_console():
    from PyObjCTools import AppHelper
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
