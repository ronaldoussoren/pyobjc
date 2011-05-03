from objc._objc import _setClassSetUpHook, selector, ivar

__all__ = ()

FunctionType = type(lambda:1)

def class_setup_hook(name, 
        super_class, class_dict, instance_vars, instance_methods, 
        class_methods):
    """
    This function is called during the construction of a Python subclass
    of an Objective-C class.
    """
    class_keys = class_dict.keys()

    for k in class_keys:
        v = class_dict[k]

        if isinstance(v, ivar):
            instance_vars.append(v)

        elif isinstance(v, selector):
            if v.isClassMethod:
                if v not in class_methods:
                    class_methods.append(v)
            else:
                if v not in instance_methods:
                    instance_methods.append(v)

        elif isinstance(v, FunctionType):
            if k.startswith('__') and k.endswith('__'):
                # Skip special methods
                continue










#_setClassSetUpHook(class_setup_hook)
