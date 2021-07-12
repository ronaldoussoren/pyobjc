import itertools


def type_string(obj):
    if isinstance(obj, type):
        objType = obj.__class__
    else:
        objType = type(obj)
    return getattr(objType, "__module__", "-") + "." + objType.__name__


class NetRepr:
    def __init__(self, objectPool):
        self.objectPool = objectPool
        self.cache = {}
        self._identfactory = itertools.count()

    def clear(self):
        self.cache.clear()
        self._identfactory = itertools.count()

    def netrepr_tuple(self, obj):
        return repr(tuple(itertools.imap(self.netrepr, obj)))

    def netrepr_list(self, obj):
        return repr(map(self.netrepr, obj))

    def netrepr_exception(self, e):
        cls = e.__class__
        if cls.__module__ == "exceptions":
            rval = cls.__name__ + self.netrepr_tuple(e.args)
        else:
            rval = "Exception({!r})".format(
                f"[Remote] {cls.__module__}.{cls.__name__} {e}",
            )
        return rval

    def netrepr(self, obj):
        if obj is None:
            return "None"
        objtype = type(obj)
        if objtype is int or objtype is float:
            return repr(obj)
        elif objtype is str:
            if True:
                return repr(obj)
            else:
                # "intern" these
                obj_id = id(obj)
                cached = self.get(self.cache, obj_id, None)
                if cached is None:
                    # ident = next(self._identfactory)
                    self.cache[obj_id] = f"__cached__({obj_id!r})"
                    cached = f"__cache__({obj_id!r}, {obj!r})"
                return cached
        return self.netrepr_default(obj)

    def netrepr_default(self, obj):
        method = getattr(obj, "__netrepr__", None)
        if method is None:
            method = self.objectPool.referenceForObject(obj).__netrepr__
        return method()


class BaseObjectPool:
    def __init__(self):
        self.idents = {}
        self.refs = {}
        self.pools = []

    def referenceForIdent(self, ident):
        return self.idents[ident]

    def base_alloc(self, ref, ident):
        self.refs[ref] = ident
        self.idents[ident] = ref

    def base_dealloc(self, ref, ident):
        del self.refs[ref]
        del self.idents[ident]

    def autorelease(self, ref):
        if not self.pools:
            raise RuntimeError(f"no autoreleasepool for {ref!r}")
        pool = self.pools[-1]
        pool[ref] = pool.get(ref, 0) + 1

    def push(self):
        # print "pushed pool"
        self.pools.append({})

    def pop(self):
        if not self.pools:
            raise RuntimeError("popped too many pools")
        # print "popped pool"
        pool = self.pools.pop()
        for ref, count in pool.items():
            ref.release(count)

    def referenceForObject(self, obj):
        raise TypeError(
            f"Can not create a reference to {obj!r}, the bridge is unidirectional"
        )


class RemoteObjectPool(BaseObjectPool):
    def __init__(self, writecode):
        BaseObjectPool.__init__(self)
        self.writecode = writecode
        self.namespace = {"None": None, "__ref__": self.referenceForRemoteIdent}

    def referenceForRemoteIdent(self, ident, type_string):
        rval = self.idents.get(ident)
        if rval is None:
            rval = RemoteObjectReference(self, ident, type_string)
        return rval


class ObjectPool(BaseObjectPool):
    def __init__(self):
        BaseObjectPool.__init__(self)
        self._identfactory = itertools.count()
        self.obj_ids = {}
        self.namespace = {"__obj__": self.objectForIdent}

    def object_alloc(self, ref, obj_id):
        self.obj_ids[obj_id] = ref

    def object_dealloc(self, ref, obj_id):
        del self.obj_ids[obj_id]

    def objectForIdent(self, ident):
        return self.referenceForIdent(ident).obj

    def referenceForObject(self, obj):
        obj_id = id(obj)
        rval = self.obj_ids.get(obj_id)
        if rval is None:
            ident = next(self._identfactory)
            rval = ObjectReference(self, ident, type_string(obj), obj, obj_id)
            rval = rval.alloc().autorelease()
        return rval


class BaseObjectReference:
    def __init__(self, objectPool, ident, type_string):
        self.ident = ident
        self.type_string = type_string
        self.objectPool = objectPool
        self.retainCount = 1

    def retain(self, count=1):
        # print "%r.retain(%d)" % (self, count)
        self.retainCount += count
        return self

    def alloc(self):
        self.objectPool.base_alloc(self, self.ident)
        return self

    def dealloc(self):
        self.objectPool.base_dealloc(self, self.ident)
        self.retainCount = -1

    def release(self, count=1):
        # print "%r.release(%d)" % (self, count)
        newCount = self.retainCount - count
        # print "  newCount = %d" % (newCount,)
        if newCount == 0:
            self.dealloc()
        elif newCount < 0:
            raise ValueError(
                "Reference %r over-released (%r -> %r)"
                % (self, self.retainCount, newCount)
            )
        self.retainCount = newCount
        return self

    def autorelease(self):
        # print "%s.autorelease()" % (self,)
        self.objectPool.autorelease(self)
        return self

    def __repr__(self):
        return f"{type(self).__name__}({self.ident!r}, {self.type_string!r})"


class RemoteObjectReference(BaseObjectReference):
    def __netrepr__(self):
        return f"__obj__({self.ident!r})"


class ObjectReference(BaseObjectReference):
    def __init__(self, objectPool, ident, type_string, obj, obj_id):
        BaseObjectReference.__init__(self, objectPool, ident, type_string)
        self.obj = obj
        self.obj_id = id(obj)

    def alloc(self):
        self = BaseObjectReference.alloc(self)
        self.objectPool.object_alloc(self, self.obj_id)
        return self

    def dealloc(self):
        self.objectPool.object_dealloc(self, self.obj_id)
        self.obj = None
        self.obj_id = -1
        BaseObjectReference.dealloc(self)

    def __netrepr__(self):
        return f"__ref__({self.ident!r}, {self.type_string!r})"


def test_netrepr():
    pool = ObjectPool()
    pool.push()
    netrepr = NetRepr(pool).netrepr
    assert netrepr("foo") == repr("foo")
    ref = pool.referenceForObject(object)
    assert ref.obj is object
    assert ref is pool.referenceForObject(object)
    assert ref.retainCount == 1
    refrepr = netrepr(ref)
    assert refrepr == netrepr(ref)
    ref.retain()
    assert ref.retainCount == 2
    pool.pop()
    pool.push()
    assert ref.retainCount == 1

    def __ref__(ident, type_string):
        return pool.referenceForIdent(ident)

    netref = eval(refrepr)
    assert netref is ref
    assert netref.obj is object
    ref.release()
    pool.pop()
    assert ref.obj is None
