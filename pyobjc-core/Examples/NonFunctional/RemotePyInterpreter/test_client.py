import fcntl
import os
import socket
import sys
from subprocess import PIPE, Popen

from netrepr import NetRepr, RemoteObjectPool, RemoteObjectReference


IMPORT_MODULES = ["netrepr", "remote_console", "remote_pipe", "remote_bootstrap"]
source = []
for fn in IMPORT_MODULES:
    for line in open(fn + ".py"):
        source.append(line)
    source.append("\n\n")
SOURCE = repr("".join(source)) + "\n"


def bind_and_listen(hostport):
    if isinstance(hostport, str):
        host, port = hostport.split(":")
        hostport = (host, int(port))
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set close-on-exec
    if hasattr(fcntl, "FD_CLOEXEC"):
        old = fcntl.fcntl(serversock.fileno(), fcntl.F_GETFD)
        fcntl.fcntl(serversock.fileno(), fcntl.F_SETFD, old | fcntl.FD_CLOEXEC)
    # allow the address to be re-used in a reasonable amount of time
    if os.name == "posix" and sys.platform != "cygwin":
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    serversock.bind(hostport)
    serversock.listen(5)
    return serversock


def open_connection(executable=sys.executable):
    serversock = bind_and_listen(("127.0.0.1", 0))
    hostport = serversock.getsockname()
    proc = Popen(
        [executable, "tcpinterpreter.py", repr(hostport)],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        close_fds=True,
    )
    clientsock, address = serversock.accept()
    serversock.shutdown(2)
    return clientsock, proc


def start_client(clientsock):
    f = clientsock.makefile("r+b", 0)
    f.write(SOURCE)
    f.flush()
    return f


def client_loop(f):
    def writecode(code):
        # print('[code: %r]' % (code,))
        f.write(repr(code) + "\n")

    pool = RemoteObjectPool(writecode)
    netRepr = NetRepr(pool)
    netrepr = netRepr.netrepr

    def neteval(s):
        return eval(s, pool.namespace, pool.namespace)

    while True:
        code = f.readline().rstrip()
        pool.push()
        try:
            if not code:
                break
            command = eval(code)
            basic = eval(command[0])
            if basic == "expect":
                seq = eval(command[1])
                name = eval(command[2])
                args = map(neteval, command[3:])
                code = None
                rval = None
                if name == "RemoteConsole.input":
                    try:
                        rval = input(*args)
                    except EOFError:
                        code = "raise EOFError"
                elif name == "RemoteConsole.write":
                    sys.stdout.write(args[0])
                elif name == "RemoteConsole.displayhook":
                    pass
                    obj = args[0]
                    if obj is None:
                        pass
                    elif isinstance(obj, RemoteObjectReference):
                        writecode(f'interp.write(repr({netrepr(obj)}) + "\\n")')
                    else:
                        print(repr(obj))
                elif name.startswith("RemoteFileLike."):
                    fh = getattr(sys, args[0])
                    meth = getattr(fh, name[len("RemoteFileLike.") :])  # noqa: E203
                    rval = meth(*args[1:])
                else:
                    print(name, args)
                if code is None:
                    code = f"__result__[{seq!r}] = {rval!r}"
                writecode(code)
        finally:
            pool.pop()


def main():
    clientsock, proc = open_connection()
    f = start_client(clientsock)
    try:
        client_loop(f)
    finally:
        f.close()
        clientsock.close()
        proc.stdin.close()
        print("[stdout]", proc.stdout.read())
        print("[stderr]", proc.stderr.read())


if __name__ == "__main__":
    main()
