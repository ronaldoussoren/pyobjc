#
# Using an NSDictionary. 
#
# You can use both the Python and Objective-C interfaces to access a
# dictionary. 
#
import sys
import objc

NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')

obj = NSMutableDictionary.dictionary()
print "An empty NSMutableDictionary:", obj
print "Actual type:", type(obj)

print "Setting key2 the objective-C way"
obj.setObject_forKey_(42, 'key2')
print "Setting key1 the python way"
obj['key1'] = 'value1'

print "key1 = ", obj.objectForKey_('key1')
print "key2 = ", obj['key2']

# Print values
print "all keys:", obj.keys()
print "all values:",  obj.values()
print "A filled NSMutableDictonary:", obj
