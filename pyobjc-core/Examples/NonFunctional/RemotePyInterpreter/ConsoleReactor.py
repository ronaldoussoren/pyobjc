__all__ = ['ConsoleReactor']

import sys
from netrepr import NetRepr, RemoteObjectPool, RemoteObjectReference
from Foundation import *

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
        self.connection = None
        self.pool = None
        self.netReprCenter = None

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
            self.commands.pop(command[0]),
            command[0],
            map(self.netEval_, command[1:]),
        )

    def sendResult_sequence_(self, rval, seq):
        nr = self.netReprCenter
        code = '__result__[%r] = %s' % (seq, nr.netrepr(rval))
        self.writeCode_(code)

    def sendException_sequence_(self, e):
        nr = self.netReprCenter
        code = 'raise ' + nr.netrepr_exception(e)
        print "forwarding:", code
        self.writeCode_(code)
    
    def doCallback_sequence_args_(self, callback, seq, args):
        nr = self.netReprCenter
        try:
            rval = callback(*args)
        except Exception, e:
            self.sendException_sequence_(e, seq)
        else:
            self.sendResult_sequence_(rval, seq)
    
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
        elif name == 'RemoteConsole.initialize':
            self.doCallback_sequence_args_(lambda *args:None, seq, args)
        else:
            self.doCallback_sequence_args_(NSLog, seq, [u'%r does not respond to expect %r' % (self, command,)])

    def close(self):
        if self.connection is not None:
            self.writeCode_('raise SystemExit')
        self.pool = None
        self.netReprCenter = None
        self.connection = None
        self.commands = None
