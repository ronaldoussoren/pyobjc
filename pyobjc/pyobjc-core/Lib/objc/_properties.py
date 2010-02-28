__all__ = ('object_property', 'bool_property', )
        #'array_property', 'set_property')

from objc import ivar, selector, _C_ID, _C_NSBOOL, _C_BOOL, NULL
from objc import lookUpClass

NSSet = lookUpClass('NSSet')

def attrsetter(prop, name, copy):
    if copy:
        def func(self, value):
            setattr(self, name, value.copy())
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
        m = getatrr(object.pyobjc_instanceMethods, name)
        return m()
    return getter

def _dynamic_setter(name):
    def setter(object, value):
        m = getatrr(object.pyobjc_instanceMethods, name)
        return m(value)
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

        v.__getprop = self.__getter
        v.__setprop = self.__setter
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
            setterName = 'set%s%s:'%(name[0].upper(), name[1:])
            signature = 'v@:' + self._typestr
            if self._setter is None:
                if self.__inherit:
                    pass

                elif self._dynamic:
                    self.__setprop = _dynamic_setter(setterName)

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
            getterName = 'is%s%s'%(name[0].upper(), name[:1])
        else:
            getterName = self._name

        if self._getter is None:
            if self.__inherit:
                pass

            elif self._dynamic:
                self.__getprop = _dynamic_getter(getterName)

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
            selName = 'validate%s%s:error:'%(
                    self._name[0].upper(), self._name[1:])
            signature = _NSBOOL + '@:N^@o^@'
            validate = selector(
                    self.validate,
                    selector=selName,
                    signature=signature)
            validate.isHidden = True
            instance_methods.add(validate)

        if self._depends_on is not None:
            if self.__parent is not None:
                if self.__parent._depends_on:
                    self._depends_on.update(self.__parent._depends_on.copy())

            self._depends_on = self._depends_on

            affecting = selector(
                    _return_value(NSSet.setWithArray_(list(self._depends_on))),
                    selector = 'keyPathsForValuesAffecting%s%s'%(
                        self._name[0].upper(), self._name[1:]),
                    signature = '@@:',
                    isClassMethod=True)
            #affecting.isHidden = True
            class_dict[affecting.selector] = affecting
            class_methods.add(affecting)
                   

    def __get__(self, object, owner):
        return self.__getprop(object)

    def __set__(self, object, value):
        if self.__setprop is None:
            raise ValueError("setting read-only property %r"%(self._name,))

        return self.__setprop(object, value)

    def __delete__(self, object):
        raise TypeError("cannot delete property %r"%(self._name))

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
        if self._ro:
            raise ValueError("Defining settter for read-only property")

        if self.__created:
            v = self._clone()
            v._setter = function
            return v

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
