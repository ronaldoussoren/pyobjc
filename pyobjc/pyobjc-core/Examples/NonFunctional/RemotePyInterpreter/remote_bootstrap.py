__file__ = "<RemotePyInterpreterClient>"
import sys
import os
pool = ObjectPool()
netReprCenter = NetRepr(pool)
netrepr = netReprCenter.netrepr
netrepr_tuple = netReprCenter.netrepr_tuple
netrepr_list = netReprCenter.netrepr_list
netrepr_exception = netReprCenter.netrepr_exception
namespace = globals()
namespace.update(pool.namespace)
__main__ = sys.modules['__main__']
assert namespace is not __main__.__dict__
pipe = RemotePipe(__runsocketcode__, __clientfile__, netReprCenter, namespace, pool)
interp = RemoteConsole(pipe, locals=__main__.__dict__)
interp.interact()
