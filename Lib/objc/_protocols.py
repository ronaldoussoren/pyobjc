import _objc

__all__ = ['protocolNamed', 'ProtocolError']

class ProtocolError(_objc.error):
    __module__ = 'objc'

PROTOCOL_CACHE = {}
def protocolNamed(name):
    """
    Returns a Protocol object for the named protocol. This is the
    equivalent of @protocol(name) in Objective-C.
    Raises objc.ProtocolError when the protocol does not exist.
    """
    name = unicode(name)
    try:
        return PROTOCOL_CACHE[name]
    except KeyError:
        pass
    for cls in _objc.getClassList():
        for p in _objc.protocolsForClass(cls):
            PROTOCOL_CACHE.setdefault(p.name(), p)
    try:
        return PROTOCOL_CACHE[name]
    except KeyError:
        raise ProtocolError("protocol %r does not exist" % (name,), name)
