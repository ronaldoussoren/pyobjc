
import pyobjc

__Foundation__ = globals()
__skip__ = [ 'NSInvocationBuilder', 'sel_is_mapped' ]

for _name in dir(pyobjc.runtime):
    if _name[0] <> '_' and _name not in __skip__:
        __Foundation__[_name] =  pyobjc.lookup_class(_name) 

sel_is_mapped = pyobjc.runtime.sel_is_mapped 
del _name




