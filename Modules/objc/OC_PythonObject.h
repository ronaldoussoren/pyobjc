/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonObject.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:51
 *
 * Created Wed Sep  4 18:36:15 1996.
 */

/* This is basically the implementation of the Python Abstract Layer
   API in Objective-C. */
   
#ifndef _OC_PythonObject_H
#define _OC_PythonObject_H

#include <Python.h>
#import <Foundation/NSProxy.h>
#import <Foundation/NSMethodSignature.h>

@protocol PythonObject

/*#M Return the wrapped Python object. */
- (PyObject *) pyObject;
- (PyObject *) __pyobjc_PythonObject__;


/*#M Print the PythonObject on file @var{fp}.  Returns -1 on
  error.  The @var{flags} argument is used to enable certain printing
  options. The only option currently supported is @code{Py_Print_RAW}. */
- (int) print:(FILE *) fp flags:(int) flags;

/*#M Returns 1 if the PythonObject has the attribute @var{attr_name},
  and 0 otherwise.

  This is equivalent to the Python expression:  hasattr (o,attr_name). */
- (int) hasAttrCString:(char *) attr_name;
- (int) hasAttrString:(NSString *) attr_name;

/*#M Retrieve an attributed named @var{attr_name} from object o.
  Returns the attribute value on success, or NULL on failure.

  This is the equivalent of the Python expression: o.attr_name. */
- (id <PythonObject>) getAttrCString:(char *) attr_name;
- (id <PythonObject>) getAttrString:(NSString *) attr_name;

/*#M Returns 1 if o has the attribute attr_name, and 0 otherwise.
  This is equivalent to the Python expression:  hasattr(o,attr_name). */
- (int) hasAttr:(id <PythonObject>) attr_name;

/*#M Retrieve an attributed named attr_name form object o.
  Returns the attribute value on success, or NULL on failure.
  This is the equivalent of the Python expression: o.attr_name. */
- (id <PythonObject>) getAttr:(id <PythonObject>) attr_name;

/*#M Set the value of the attribute named attr_name, for object o,
  to @var{value}. Returns -1 on failure.  This is
  the equivalent of the Python statement: o.attr_name=value. */
- (int) setAttrCString:(char *) attr_name value:(id <PythonObject>) value;
- (int) setAttrString:(NSString *) attr_name value:(id <PythonObject>) value;

/*#M Set the value of the attribute named attr_name, for object o,
  to the @var{value}. Returns -1 on failure.  This is
  the equivalent of the Python statement: o.attr_name=value. */
- (int) setAttr:(id <PythonObject>) attr_name value:(id <PythonObject>) value;

/*#M Delete attribute named attr_name, for object o. Returns
  -1 on failure.  This is the equivalent of the Python
  statement: del o.attr_name. */
- (int) delAttrCString:(char *) attr_name;
- (int) delAttrString:(NSString *) attr_name;

/*#M Delete attribute named attr_name, for object o. Returns
  -1 on failure.  This is the equivalent of the Python
  statement: del o.attr_name. */
- (int) delAttr:(id <PythonObject>) attr_name;

/*#M Compare the values of o1 and o2 using a routine provided by
  o1, if one exists, otherwise with a routine provided by o2.
  The result of the comparison is returned in result.  Returns
  -1 on failure.  This is the equivalent of the Python
  statement: result=cmp(o1,o2). */
- (int) cmp:(id <PythonObject>) o2 result:(int *) result;

/*#M Compare the values of o1 and o2 using a routine provided by
  o1, if one exists, otherwise with a routine provided by o2.
  Returns the result of the comparison on success.  On error,
  the value returned is undefined. This is equivalent to the
  Python expression: cmp(o1,o2). */
- (int) compare:(id <PythonObject>) o2;

/*#M Compute the string representation of object, o.  Returns the
  string representation on success, NULL on failure.  This is
  the equivalent of the Python expression: repr(o). */
- (id <PythonObject>) repr;

/*#M Compute the string representation of object, o.  Returns the
  string representation on success, NULL on failure.  This is
  the equivalent of the Python expression: str(o). */
- (id <PythonObject>) str;

/*#M Compute and return the hash, hash_value, of an object, o.  On
  failure, raise an Exception.  This is the equivalent of the Python
  expression: hash(o). */
- (unsigned int) hash;

/*#M Returns 1 if the object, o, is considered to be true, and
  0 otherwise. This is equivalent to the Python expression:
  not not o */
- (int) isTrue;

/*#M On success, returns a type object corresponding to the object
  type of object o. On failure, returns NULL.  This is
  equivalent to the Python expression: type(o). */
- (id <PythonObject>) type;

/*#M Return the length of object o.  If the object, o, provides
  both sequence and mapping protocols, the sequence length is
  returned. Raise an Exception On error.  This is the equivalent
  to the Python expression: len(o). */
- (unsigned int) length;

/*#M Equivalent to @code{-length}. */
- (unsigned int) count;

/*#M Return element of o corresponding to the object, key, or NULL
  on failure. This is the equivalent of the Python expression:
  o[key]. */
- (id <PythonObject>) getItem:(id <PythonObject>) key;

/*#M Map the object, key, to the value, v.  Returns
  -1 on failure.  This is the equivalent of the Python
  statement: o[key]=v. */
- (int) setItem:(id <PythonObject>) key value:(id <PythonObject>) v;

/*#M Delete the mapping for key from *o.  Returns -1 on failure.
  This is the equivalent of the Python statement: del o[key]. */
- (int) delItem:(id <PythonObject>) key;

@end /* PythonObject protocol */

@protocol PythonNumbering

/*#M Returns 1 if the object, o, provides numeric protocols, and
  false otherwise. */
- (int) numberCheck;

/*#M Returns the result of adding o1 and o2, or null on failure.
  This is the equivalent of the Python expression: o1+o2. */
- (id <PythonObject>) numberAdd:(id <PythonObject>) o2;

/*#M Returns the result of subtracting o2 from o1, or null on
  failure.  This is the equivalent of the Python expression: o1-o2. */
- (id <PythonObject>) numberSubtract:(id <PythonObject>) o2;

/*#M Returns the result of multiplying o1 and o2, or null on
  failure.  This is the equivalent of the Python expression: o1*o2. */
- (id <PythonObject>) numberMultiply:(id <PythonObject>) o2;

/*#M Returns the result of dividing o1 by o2, or null on failure.
  This is the equivalent of the Python expression: o1/o2. */
- (id <PythonObject>) numberDivide:(id <PythonObject>) o2;

/*#M Returns the remainder of dividing o1 by o2, or null on
  failure.  This is the equivalent of the Python expression: o1%o2. */
- (id <PythonObject>) numberRemainder:(id <PythonObject>) o2;

/*#M See the built-in function divmod.  Returns NULL on failure.
  This is the equivalent of the Python expression: divmod(o1,o2). */
- (id <PythonObject>) numberDivmod:(id <PythonObject>) o2;

/*#M See the built-in function pow.  Returns NULL on failure.
  This is the equivalent of the Python expression: pow(o1,o2,o3),
  where o3 is optional. */
- (id <PythonObject>) numberPower:(id <PythonObject>) o2
                                 :(id <PythonObject>) o3;

/*#M Returns the negation of o on success, or null on failure.
  This is the equivalent of the Python expression: -o. */
- (id <PythonObject>) numberNegative;

/*#M Returns the (what?) of o on success, or NULL on failure.
  This is the equivalent of the Python expression: +o. */
- (id <PythonObject>) numberPositive;

/*#M Returns the absolute value of o, or null on failure.  This is
  the equivalent of the Python expression: abs(o). */
- (id <PythonObject>) numberAbsolute;

/*#M Returns the bitwise negation of o on success, or NULL on
  failure.  This is the equivalent of the Python expression: ~o. */
- (id <PythonObject>) numberInvert;

/*#M Returns the result of left shifting o1 by o2 on success, or
  NULL on failure.  This is the equivalent of the Python
  expression: o1 << o2. */
- (id <PythonObject>) numberLshift:(id <PythonObject>) o2;

/*#M Returns the result of right shifting o1 by o2 on success, or
  NULL on failure.  This is the equivalent of the Python
  expression: o1 >> o2. */
- (id <PythonObject>) numberRshift:(id <PythonObject>) o2;

/*#MReturns the result of bitwise and of o1 and o2 on success, or
  NULL on failure. This is the equivalent of the Python
  expression: o1&o2. */
- (id <PythonObject>) numberAnd:(id <PythonObject>) o2;

/*#M Returns the bitwise exclusive or of o1 by o2 on success, or
  NULL on failure.  This is the equivalent of the Python
  expression: o1^o2. */
- (id <PythonObject>) numberXor:(id <PythonObject>) o2;

/*#M Returns the result of bitwise or of o1 and o2 on success, or
  NULL on failure.  This is the equivalent of the Python
  expression: o1|o2. */
- (id <PythonObject>) numberOr:(id <PythonObject>) o2;

/* XXX COERCE IS MISSING:
        int PyNumber_Coerce(PyObject **o1, PyObject **o2);

         This function takes the addresses of two variables of type
         PyObject*.

         If the objects pointed to by *p1 and *p2 have the same type,
         increment their reference count and return 0 (success).
         If the objects can be converted to a common numeric type,
         replace *p1 and *p2 by their converted value (with 'new'
         reference counts), and return 0.
         If no conversion is possible, or if some other error occurs,
         return -1 (failure) and don't increment the reference counts.
         The call PyNumber_Coerce(&o1, &o2) is equivalent to the Python
         statement o1, o2 = coerce(o1, o2).

       */

/*#M Returns the o converted to an integer object on success, or
  NULL on failure.  This is the equivalent of the Python
  expression: int(o). */
- (id <PythonObject>) numberInt;

/*#M Returns the o converted to a long integer object on success,
  or NULL on failure.  This is the equivalent of the Python
  expression: long(o). */
- (id <PythonObject>) numberLong;

/*#M Returns the o converted to a float object on success, or NULL
  on failure.  This is the equivalent of the Python expression:
  float(o). */
- (id <PythonObject>) numberFloat;

@end /* PythonNumbering protocol */

@protocol PythonSequencing

/*#M Return 1 if the object provides sequence protocol, and zero
  otherwise. */
- (int) sequenceCheck;

/*#M Return the length of sequence object o, or -1 on failure. */
- (int) sequenceLength;

/*#M Return the concatination of o1 and o2 on success, and NULL on
  failure.   This is the equivalent of the Python
  expression: o1+o2. */
- (id <PythonObject>) sequenceConcat:(id <PythonObject>) o2;

/*#M Return the result of repeating sequence object o count times,
  or NULL on failure.  This is the equivalent of the Python
  expression: o1*count. */
- (id <PythonObject>) sequenceRepeat:(int) count;

/*#M Return the ith element of o, or NULL on failure. This is the
  equivalent of the Python expression: o[i]. */
- (id <PythonObject>) sequenceGetItem:(int) i;

/*#M Return the slice of sequence object o between i1 and i2, or
  NULL on failure. This is the equivalent of the Python
  expression: o[i1:i2]. */
- (id <PythonObject>) sequenceGetSliceFrom:(int) i1 to:(int) i2;

/*#M Assign object v to the ith element of o.  Returns
  -1 on failure.  This is the equivalent of the Python
  statement: o[i]=v. */
- (int) sequenceSetItem:(int) i value:(id <PythonObject>) v;

/*#M Delete the ith element of object v.  Returns
  -1 on failure.  This is the equivalent of the Python
  statement: del o[i]. */
- (int) sequenceDelItem:(int) i;

/*#M Assign the sequence object, v, to the slice in sequence
  object, o, from i1 to i2.  Returns -1 on failure. This is the
  equivalent of the Python statement: o[i1:i2]=v. */
- (int) sequenceSetSliceFrom:(int) i1
                          to:(int) i2
                       value:(id <PythonObject>) v;

/*#M Delete the slice in sequence object, o, from i1 to i2.
  Returns -1 on failure. This is the equivalent of the Python
  statement: del o[i1:i2]. */
- (int) sequenceDelSliceFrom:(int) i1 to:(int) i2;

/*#M Returns the sequence, o, as a tuple on success, and NULL on failure.
  This is equivalent to the Python expression: tuple(o) */
- (id <PythonObject>) sequenceTuple;

/*#M Returns the sequence, o, as a list on success, and NULL on failure.
  This is equivalent to the Python expression: list(o). */
- (id <PythonObject>) sequenceList;

/*#M Return the number of occurrences on value on o, that is,
  return the number of keys for which o[key]==value.  On
  failure, return -1.  This is equivalent to the Python
  expression: o.count(value). */
- (int) sequenceCount:(id <PythonObject>) value;

/*#M Determine if o contains value.  If an item in o is equal to
  X, return 1, otherwise return 0.  On error, return -1.  This
  is equivalent to the Python expression: value in o. */
- (int) sequenceIn:(id <PythonObject>) value;

/*#M Return the first index for which o[i]=value.  On error,
  return -1.    This is equivalent to the Python
  expression: o.index(value). */
- (int) sequenceIndex:(id <PythonObject>) value;

@end /* PythonSequencing protocol */

@protocol PythonCalling

/*#M Determine if the object, o, is callable.  Return 1 if the
  object is callable and 0 otherwise. */
- (int) callableCheck;

/*#M Call a callable Python object, callable_object, with
  arguments given by the tuple, args.  If no arguments are
  needed, then args may be NULL.  Returns the result of the
  call on success, or NULL on failure.  This is the equivalent
  of the Python expression: apply(o,args). */
- (id <PythonObject>) callableCall:(id <PythonObject>) args;

/*#M Call a callable Python object, callable_object, with a
  variable number of C arguments. The C arguments are described
  using a mkvalue-style format string. The format may be NULL,
  indicating that no arguments are provided.  Returns the
  result of the call on success, or NULL on failure.  This is
  the equivalent of the Python expression: apply(o,args). */
- (id <PythonObject>) callableCallFunction:(char *) format, ...;
//XXX How should be called the following?
//- (id <PythonObject>) callableCallFunction:(NSString *) format, ...;

/*#M Call the method named m of object o with a variable number of
  C arguments.  The C arguments are described by a mkvalue
  format string.  The format may be NULL, indicating that no
  arguments are provided. Returns the result of the call on
  success, or NULL on failure.  This is the equivalent of the
  Python expression: o.method(args). */
- (id <PythonObject>) callableCallMethod:(char *) m
                                withArgs:(char *) format, ...;
//XXX and what about this?
//- (id <PythonObject>) callableCallMethod:(NSString *) m
//                                withArgs:(NSString *) format, ...;

@end /* PythonCalling protocol */

@protocol PythonMapping

/*#M Return 1 if the object provides mapping protocol, and zero
  otherwise. */
- (int) mappingCheck;

/*#M Returns the number of keys in object o on success, and -1 on
  failure.  For objects that do not provide sequence protocol,
  this is equivalent to the Python expression: len(o). */
- (int) mappingLength;

/*#M Remove the mapping for object, key, from the object *o.
  Returns -1 on failure.  This is equivalent to
  the Python statement: del o[key]. */
- (int) mappingDelItemCString:(char *) key;
- (int) mappingDelItemString:(NSString *) key;

/*#M Remove the mapping for object, key, from the object *o.
  Returns -1 on failure.  This is equivalent to
  the Python statement: del o[key]. */
- (int) mappingDelItem:(id <PythonObject>) key;

/*#M On success, return 1 if the mapping object has the key, key,
  and 0 otherwise.  This is equivalent to the Python expression:
  o.has_key(key).  */
- (int) mappingHasKeyCString:(char *) key;
- (int) mappingHasKeyString:(NSString *) key;

/*#M Return 1 if the mapping object has the key, key,
  and 0 otherwise.  This is equivalent to the Python expression:
  o.has_key(key).  */
- (int) mappingHasKey:(id <PythonObject>) key;

/*#M On success, return a list of the keys in object o.  On
  failure, return NULL. This is equivalent to the Python
  expression: o.keys(). */
- (id <PythonObject>) mappingKeys;

/*#M On success, return a list of the values in object o.  On
  failure, return NULL. This is equivalent to the Python
  expression: o.values(). */
- (id <PythonObject>) mappingValues;

/*#M On success, return a list of the items in object o, where
  each item is a tuple containing a key-value pair.  On
  failure, return NULL. This is equivalent to the Python
  expression: o.items(). */
- (id <PythonObject>) mappingItems;

/*#M Return element of o corresponding to the object, key, or NULL
  on failure. This is the equivalent of the Python expression:
  o[key]. */
- (id <PythonObject>) mappingGetItemCString:(char *) key;
- (id <PythonObject>) mappingGetItemString:(NSString *) key;

/*#M Map the object, key, to the value, v.  Returns 
  -1 on failure.  This is the equivalent of the Python
  statement: o[key]=v. */
- (int) mappingSetItemCString:(char *) key value:(id <PythonObject>) value;
- (int) mappingSetItemString:(NSString *) key value:(id <PythonObject>) value;

@end /* PythonMapping protocol */

/*#C This is the Objective-C wrapper around a Python Object.
  Whenever a Python Object is passed as argument to an Objective-C method,
  it is wrapped in an instance of this class, that supports all the
  Python Abtract Layer API. */
@interface OC_PythonObject : NSProxy <PythonObject, PythonNumbering,
                                      PythonCalling, PythonSequencing,
                                      PythonMapping>
{
  PyObject *pyObject;
}

//#M Returns a new autoreleased instance of this class.
+ (id <PythonObject>) newWithObject:(PyObject *) obj;

/*#M Initializes a new instance of this class by wrapping @var{obj}.
  The Python object is INCREF'ed. Returns self. */
- (id <PythonObject>) initWithObject:(PyObject *) obj;

/*#M XXX Out of date.
  Tries to execute the given selector as a method on the object.
  You should never call this method: it is performed by the runtime when
  we receive a message we don't understand, so that we have the possibility
  of forwarding it to some other object, in this case to the Python object.
  
  !! This is not a bullet-proof implementation, since you can easily
  !! jump on trouble passing wrong parameter!

  The strategy we follow is: first of all we check to see if the Python
  Object responds to the method we are forwarding (as usual, the ObjC
  selector name gets pythonified by replacing colons denoting parameters
  with double underscore) with the same number of arguments. If it does
  not we execute @code{-doesNotRecognize:} and return @code{nil}.

  Then we look for an implementation of the selector in the ObjC runtime:
  if we found it, the we can relay on its arguments description to choose
  the right type for their conversion to Python objects; otherwise we make
  a strong assumption: the user knows what it is doing, and he is giving us
  the right number of arguments, and ALL of them are instances of
  @code{OC_PythonObject} class or a subclass of it.
  Anyway, we build a Python tuple with these arguments, and perform a
  @code{PyObject_CallObject} with it. Its result is returned to our caller. */
- (void) forwardInvocation:(NSInvocation *) invocation;

/*#M Returns TRUE if ourself or the Python object can respond to the given
  selector. */
- (BOOL) respondsToSelector:(SEL) aSelector;

- (NSMethodSignature *) methodSignatureForSelector:(SEL) selector;

/*#M Raises an ObjC_Error exception with the name of the selector @var{aSelector}
  and returns @code{nil}. */
- (void) doesNotRecognizeSelector:(SEL) aSelector;

@end /* OC_PythonObject class interface */


#endif /* _OC_PythonObject_H */
