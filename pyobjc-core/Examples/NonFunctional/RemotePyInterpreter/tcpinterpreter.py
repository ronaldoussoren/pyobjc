#! /usr/bin/env python

"""
    start socket based minimal readline exec server
"""
import socket
import sys


def runsocketcode(clientfile, g):
    try:
        source = clientfile.readline().rstrip()
    except Exception:
        raise SystemExit
    if not source:
        raise SystemExit
    source = eval(source)
    co = compile(source + "\n", "<remote-source>", "exec")
    exec(co, g)


def serveonce(clientsock, name="stdin"):
    clientfile = clientsock.makefile("r+b", 0)
    g = {
        "__name__": "__socketclient__",
        "__file__": f"<{name}>",
        "__clientsock__": clientsock,
        "__clientfile__": clientfile,
        "__runsocketcode__": runsocketcode,
    }
    try:
        runsocketcode(clientfile, g)
    finally:
        clientfile.close()
        clientsock.close()


def real_main():
    import sys

    hostport = eval(sys.argv[1])
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsock.connect(hostport)
    serveonce(clientsock)


def main():
    newglobals = {
        "__builtins__": sys.modules["__builtin__"],
        "__doc__": None,
        "__name__": "__main__",
    }
    sourcefile = __file__
    g = globals()
    g.clear()
    g.update(newglobals)
    serverglobals = {"__name__": "__socketclient__"}
    with open(sourcefile) as fp:
        sourcecode = fp.read()
    exec(sourcecode, serverglobals, serverglobals)


if __name__ == "__main__":
    main()
elif __name__ == "__socketclient__":
    real_main()
