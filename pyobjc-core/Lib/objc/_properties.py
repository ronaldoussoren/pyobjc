__all__ = ('object_property', 'bool_property',
        'array_property', 'set_property', 'dict_property')

from objc import ivar, selector, _C_ID, _C_NSBOOL, _C_BOOL, NULL, _C_NSUInteger
from objc import lookUpClass
import collections
from copy import copy as copy_func
import sys

NSSet = lookUpClass('NSSet')
NSObject = lookUpClass('NSObject')


def attrsetter(prop, name, copy):
    if copy:
        def func(self, value):
            if isinstance(value, NSObject):
                setattr(self, name, value.copy())
            else:
                setattr(self, name, copy_func(value))
    else:
        def func(self, value):
            setattr(self, name, value)
    return func

def attrgetter(name):
    def func(self):
        return getattr(self, name)
    return func

def _return_value(value):
    def func(self):
        return value

    return func

def _dynamic_getter(name):
    def getter(object):
        m = getattr(object.pyobjc_instanceMethods, name)
        return m()
    getter.__name__ = name
    return getter

def _dynamic_setter(name):
    def setter(object, value):
        m = getattr(object.pyobjc_instanceMethods, name)
        return m(value)
    setter.__name__ = name
    return setter

class object_property (object):
    def __init__(self, name=None, 
            read_only=False, copy=False, dynamic=False, 
            ivar=None, typestr=_C_ID, depends_on=None):
        self.__created = False
        self.__inherit = False
        self._name = name
        self._typestr = typestr
        self._ro = read_only
        self._copy = copy
        self._dynamic = dynamic
        self._ivar = ivar
        self._getter = None
        self._setter = None
        self._validate = None
        if depends_on is None:
            self._depends_on = ()
        else:
            self._depends_on = list(depends_on)

        self.__getprop = None
        self.__setprop = None
        self.__parent = None

    def _clone(self):
        v = type(self)(name=self._name, 
                read_only=self._ro, copy=self._copy, dynamic=self._dynamic,
                ivar=self._ivar, typestr=self._typestr, depends_on=None)
        v.__inherit = True

        v.__getprop = self.__getprop
        v.__setprop = self.__setprop
        v.__parent = self

        return v

    def __pyobjc_class_setup__(self, name, class_dict, instance_methods, class_methods):
        self.__created = True
        if self._name is None:
            self._name = name

        if self._ivar is not NULL:
            if self._ivar is None:
                ivname = '_' + self._name
            else:
                ivname = self._ivar

            if self.__parent is None:
                ivar_ref = ivar(name=ivname, type=self._typestr)
                class_dict[ivname] = ivar_ref

        if self._ro:
            self._setter = None

        else:
            setterName = b'set' + name[0].upper().encode('latin1') + name[1:].encode('latin1') + b':'
            signature = b'v@:' + self._typestr
            if self._setter is None:
                if self.__inherit:
                    pass

                elif self._dynamic:
                    dynSetterName = 'set' + name[0].upper() + name[1:] + '_'
                    self.__setprop = _dynamic_setter(dynSetterName)
                    instance_methods.add(setterName)

                else:

                    if self._ivar is NULL:
                        raise ValueError(
                            "Cannot create default setter for property "
                            "without ivar")

                    self.__setprop = selector(
                        attrsetter(self._name, ivname, self._copy),
                        selector=setterName,
                        signature=signature
                    )
                    self.__setprop.isHidden = True
                    instance_methods.add(self.__setprop)
            else:
                self.__setprop = selector(
                    self._setter,
                    selector=setterName,
                    signature=signature
                )
                self.__setprop.isHidden = True
                instance_methods.add(self.__setprop)

        if self._typestr in (_C_NSBOOL, _C_BOOL):
            getterName = b'is' + name[0].upper().encode('latin1') + name[:1].encode('latin1')
        else:
            getterName = self._name.encode('latin1')

        if self._getter is None:
            if self.__inherit:
                pass

            elif self._dynamic:
                if self._typestr in (_C_NSBOOL, _C_BOOL):
                    dynGetterName = 'is' + name[0].upper() + name[:1]
                else:
                    dynGetterName = self._name

                self.__getprop = _dynamic_getter(dynGetterName)
                instance_methods.add(getterName)

            else:
                if self._ivar is NULL:
                    raise ValueError(
                        "Cannot create default getter for property without ivar")

                self.__getprop = selector(
                        attrgetter(ivname),
                        selector=getterName,
                        signature=self._typestr + b'@:')
                self.__getprop.isHidden=True
                instance_methods.add(self.__getprop)

        else:
            self.__getprop = selector(
                    self._getter,
                    selector=getterName,
                    signature=self._typestr + b'@:')
            self.__getprop.isHidden=True
            instance_methods.add(self.__getprop)

        if self._validate is not None:
            selName = b'validate' + self._name[0].upper().encode('latin') + self._name[1:].encode('latin') + b':error:'
            signature = _C_NSBOOL + b'@:N^@o^@'
            validate = selector(
                    self._validate,
                    selector=selName,
                    signature=signature)
            validate.isHidden = True
            instance_methods.add(validate)

        if self._depends_on:
            if self.__parent is not None:
                if self.__parent._depends_on:
                    self._depends_on.update(self.__parent._depends_on.copy())

            self._depends_on = self._depends_on

            affecting = selector(
                    _return_value(NSSet.setWithArray_(list(self._depends_on))),
                    selector = b'keyPathsForValuesAffecting' + self._name[0].upper().encode('latin1') + self._name[1:].encode('latin1'),
                    signature = b'@@:',
                    isClassMethod=True)
            affecting.isHidden = True
            class_dict[affecting.selector] = affecting
            class_methods.add(affecting)


    def __get__(self, object, owner):
        if object is None:
            return self
        return self.__getprop(object)

    def __set__(self, object, value):
        if self.__setprop is None:
            raise ValueError("setting read-only property " + self._name)

        return self.__setprop(object, value)

    def __delete__(self, object):
        raise TypeError("cannot delete property " + self._name)

    def depends_on(self, keypath):
        if self._depends_on is None:
            self._depends_on = set()
        self._depends_on.add(keypath)

    def getter(self, function):
        if self.__created:
            v = self._clone()
            v._getter = function
            return v

        self._getter = function
        return self

    def setter(self, function):

        if self.__created:
            v = self._clone()
            v._ro = False
            v._setter = function
            return v

        if self._ro:
            raise ValueError("Defining settter for read-only property")

        self._setter = function
        return self

    def validate(self, function):
        if self._ro:
            raise ValueError("Defining validator for read-only property")

        if self.__created:
            v = self._clone()
            v._validate = function
            return v

        self._validate = function
        return self

class bool_property (object_property):
    def __init__(self, name=None, 
            read_only=False, copy=False, dynamic=False, 
            ivar=None, typestr=_C_NSBOOL):
        super(bool_property, self).__init__(
                name, read_only, copy, dynamic, ivar, typestr)



def _id(value):
    return value

NSIndexSet = lookUpClass('NSIndexSet')
NSMutableIndexSet = lookUpClass('NSMutableIndexSet')
NSKeyValueChangeSetting = 1
NSKeyValueChangeInsertion = 2
NSKeyValueChangeRemoval = 3
NSKeyValueChangeReplacement = 4

# FIXME: split into two: array_proxy and mutable_array_proxy
class array_proxy (collections.MutableSequence):
    # XXX: The implemenation should be complete, but is currently not
    # tested.
    __slots__ = ('_name', '_wrapped', '_parent', '_ro')

    def __init__(self, name, parent, wrapped, read_only):
        self._wrapped = wrapped
        self._name = name
        self._parent = parent
        self._ro = read_only


    def __indexSetForIndex(self, index):
        if isinstance(index, slice):
            result = NSMutableIndexSet.alloc().init()
            start, stop, step = index.indices(len(self._wrapped))
            for i in xrange(start, stop, step):
                result.addIndex_(i)

            return result

        else:
            if index < 0:
                v = len(self) + index
                if v < 0:
                    raise IndexError(index)
                return NSIndexSet.alloc().initWithIndex_(v)

            else:
                return NSIndexSet.alloc().initWithIndex_(index)
        


    def __repr__(self):
        return '<array proxy for property ' + self._name + repr(self._wrapped) + '>'

    def __reduce__(self):
        # Ensure that the proxy itself doesn't get stored
        # in pickles.
        return _id, self._wrapped

    def __getattr__(self, name):
        # Default: just defer to wrapped list
        return getattr(self._wrapped, name)

    def __len__(self):
        return self._wrapped.__len__()

    def __getitem__(self, index):
        return self._wrapped[index]

    def __setitem__(self, index, value):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        indexes = self.__indexSetForIndex(index)
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeSetting,
                indexes, self._name)
        try:
            self._wrapped[index] = value
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeReplacement,
                indexes, self._name)

    def __delitem__(self, index):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        indexes = self.__indexSetForIndex(index)
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeRemoval,
                indexes, self._name)
        try:
            del self._wrapped[index]
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeRemoval,
                indexes, self._name)

    def append(self, value):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        index = len(self)
        indexes = NSIndexSet.alloc().initWithIndex_(index)
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)
        try:
            self._wrapped.append(value)
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)

    def insert(self, index, value):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        if isinstance(index, slice):
            raise ValueError("insert argument 1 is a slice")

        indexes = self.__indexSetForIndex(index)
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)
        try:
            self._wrapped.insert(index, value)
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)

    def pop(self, index=-1):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        if isinstance(index, slice):
            raise ValueError("insert argument 1 is a slice")

        indexes = self.__indexSetForIndex(index)
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeRemoval,
                indexes, self._name)
        try:
            return self._wrapped.pop(index)
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeRemoval,
                indexes, self._name)

    def extend(self, values):
        # XXX: This is suboptimal but correct
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        values = list(values)

        indexes = NSIndexSet.alloc().initWithIndexesInRange_((len(self), len(values)))

        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)
        try:
            for item in values:
                self._wrapped.append(item)
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)

    def __iadd__(self, value):
        self._wrapped.extend(value)
        return self

    def __imul__(self, count):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))
        if not isinstance(count, (int, long)):
            raise ValueError(count)

        indexes = NSIndexSet.alloc().initWithIndexesInRange_((len(self), len(self)*count))
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)
        try:
            self._wrapped *= count
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeInsertion,
                indexes, self._name)

        return self

    
    def __eq__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped == other._wrapped

        else:
            return self._wrapped == other

    def __ne__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped != other._wrapped

        else:
            return self._wrapped != other

    def __lt__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped < other._wrapped

        else:
            return self._wrapped < other

    def __le__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped <= other._wrapped

        else:
            return self._wrapped <= other

    def __gt__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped > other._wrapped

        else:
            return self._wrapped > other

    def __ge__(self, other):
        if isinstance(other, array_proxy):
            return self._wrapped >= other._wrapped

        else:
            return self._wrapped >= other


    if sys.version_info[0] == 2:
        def __cmp__(self, other):
            if isinstance(other, array_proxy):
                return cmp(self._wrapped, other._wrapped)

            else:
                return cmp(self._wrapped, other)

    def sort(self, cmp=None, key=None, reverse=False):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        indexes = NSIndexSet.alloc().initWithIndexesInRange_(
                (0, len(self._wrapped)))
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeReplacement,
                indexes, self._name)
        try:
            self._wrapped.sort(cmp=cmp, key=key, reverse=reverse)
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeReplacement,
                indexes, self._name)

    def reverse(self):
        if self._ro:
            raise ValueError("Property '%s' is read-only"%(self._name,))

        indexes = NSIndexSet.alloc().initWithIndexesInRange_(
                (0, len(self._wrapped)))
        self._parent.willChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeReplacement,
                indexes, self._name)
        try:
            self._wrapped.reverse()
        finally:
            self._parent.didChange_valuesAtIndexes_forKey_(
                NSKeyValueChangeReplacement,
                indexes, self._name)

def makeArrayAccessors(name):
    
    def countOf(self):
        return len(getattr(self, name))

    def objectIn(self, idx):
        return getattr(self, name)[idx]

    def insert(self, value, idx):
        getattr(self, name).insert(idx, value)

    def replace(self, idx, value):
        getattr(self, name)[idx] = value

    def remove(self, idx):
        del getattr(self, name)[idx]

    return countOf, objectIn, insert, remove, replace

class array_property (object_property):
    def __init__(self, name=None, 
            read_only=False, copy=True, dynamic=False, 
            ivar=None, depends_on=None):
        super(array_property, self).__init__(name, 
                read_only=read_only, 
                copy=copy, dynamic=dynamic,
                ivar=ivar, depends_on=depends_on)

    def __pyobjc_class_setup__(self, name, class_dict, instance_methods, class_methods):
        super(array_property, self).__pyobjc_class_setup__(name, class_dict, instance_methods, class_methods)


        # Insert (Mutable) Indexed Accessors
        # FIXME: should only do the mutable bits when we're actually a mutable property

        name = self._name
        Name = name[0].upper() + name[1:]

        countOf, objectIn, insert, remove, replace = makeArrayAccessors(self._name)

        countOf = selector(countOf, 
                selector  = 'countOf%s'%(Name,),
                signature = _C_NSUInteger + '@:',
        )
        countOf.isHidden = True
        instance_methods.add(countOf)

        objectIn = selector(objectIn, 
                selector  = 'objectIn%sAtIndex:'%(Name,),
                signature = '@@:' + _C_NSUInteger,
        )
        objectIn.isHidden = True
        instance_methods.add(objectIn)

        insert = selector(insert, 
                selector  = 'insertObject:in%sAtIndex:'%(Name,),
                signature = 'v@:@' + _C_NSUInteger,
        )
        insert.isHidden = True
        instance_methods.add(insert)

        remove = selector(remove, 
                selector  = 'removeObjectFrom%sAtIndex:'%(Name,),
                signature = 'v@:' + _C_NSUInteger,
        )
        remove.isHidden = True
        instance_methods.add(remove)

        replace = selector(replace, 
                selector  = 'replaceObjectIn%sAtIndex:withObject:'%(Name,),
                signature = 'v@:' + _C_NSUInteger + '@',
        )
        replace.isHidden = True
        instance_methods.add(replace)


    def __set__(self, object, value):
        if isinstance(value, array_property):
            print "set1", object, value
            value = list(value)
            print "set2", object, value

        super(array_property, self).__set__(object, value)

    def __get__(self, object, owner):
        v = object_property.__get__(self, object, owner)
        if v is None:
            v = list()
            object_property.__set__(self, object, v)
        return array_proxy(self._name, object, v, self._ro)

NSKeyValueUnionSetMutation = 1,
NSKeyValueMinusSetMutation = 2,
NSKeyValueIntersectSetMutation = 3,
NSKeyValueSetSetMutation = 4
             

class set_proxy (object):
    __slots__ = ('_name', '_wrapped', '_parent', '_ro')

    def __init__(cls, name, parent, wrapped, read_only):
        v = cls.alloc().init()
        v._name = name
        v._wrapped = wrapped
        v._parent = parent
        v._ro = read_only

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

    def add(self, item):
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueUnionSetMutation,
                set(item),
        )
        try:
            self._wrapped.add(item)
        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueUnionSetMutation,
                set(item),
            )

    def clear(self):
        object = set(self._wrapped)
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                object
        )
        try:
            self._wrapped.clear()
        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                object
            )

    def difference_update(self, *others):
        s = set()
        s.update(*others)
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                s
        )
        try:
            self._wrapped.difference_update(s)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                s
            )


    def discard(self, item):
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                set(item)
        )
        try:
            self._wrapped.discard(s)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                set(item)
            )
        
    def intersection_update(self, other):
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueIntersectSetMutation,
                set(item)
        )
        try:
            self._wrapped.intersection_update(s)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueIntersectSetMutation,
                set(item)
            )

    def pop(self):
        try:
            v = iter(self).next()
        except KeyError:
            raise KeyError("Empty set")
        
        self.remove(v)


    def remove(self, item):
        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                set(item)
        )
        try:
            self._wrapped.remove(s)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                set(item)
            )

    def symmetric_difference_update(self, other):
        other = set(other)
        s = set()
        for item in other:
            if item in self:
                s.add(item)

        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                s
        )
        try:
            self._wrapped.symmetric_difference_update(other)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueMinusSetMutation,
                s
            )

    def update(self, *others):
        s = set()
        s.update(*others)

        self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueUnionSetMutation,
                s
        )
        try:
            self._wrapped.update(s)

        finally:
            self._parent.willChangeValueForKey_withSetMutation_usingObjects_(
                self._name,
                NSKeyValueUnionSetMutation,
                s
            )


    def __ior__(self, other):
        return self|other

    def __isub__(self, other):
        return self-other

    def __ixor__(self, other):
        return self^other

    def __iand__(self, other):
        return self&other



class set_property (object_property):
    def __get__(self):
        v = object_property.__get__(self)
        if v is None:
            v = set()
            object_property.__set__(self, v)
        return set_proxy(self._name, v, self._ro)


NSMutableDictionary = lookUpClass('NSMutableDictionary')

class dict_property (object_property):
    def __get__(self):
        v = object_property.__get__(self)
        if v is None:
            v = NSMutableDictionary.alloc().init()
            object_property.__set__(self, v)
        return dict_proxy(self._name, v, self._ro)
