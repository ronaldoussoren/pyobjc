/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonObject.m,v
 * Revision: 1.23
 * Date: 1998/08/18 15:35:52
 *
 * Created Wed Sep  4 19:57:44 1996.
 */

#include "objc_support.h"
#include "abstract.h"

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION == 2 && PY_MICRO_VERSION == 0
 /* Python 2.2.0 forgets to define PyMapping_DelItem */
#undef PyMapping_DelItem
#define PyMapping_DelItem(O,K) PyDict_DelItem((O),(K))
#undef PyMapping_DelItemString
#define PyMapping_DelItemString(O,K) PyDict_DelItemString((O),(K))
#endif

#include "compile.h"

#include <stdarg.h>

#import  <Foundation/NSObject.h>  
#import  <Foundation/NSMethodSignature.h>  /* sdm7g- chg #include to #import */
#import  <Foundation/NSInvocation.h>       /* sdm7g */

#define CLASS_VERSION 0

#ifndef MAX
#define MAX(x,y) ({ unsigned int __x=(x), __y=(y); (__x > __y ? __x : __y); })
#define MIN(x,y) ({ unsigned int __x=(x), __y=(y); (__x < __y ? __x : __y); })
#endif

@implementation OC_PythonObject

#if 0 /* NSProxy doesn't seem to define +setVersion, making this useless */
+ (void) initialize
{
  if (self == [OC_PythonObject class])
    {
      [OC_PythonObject setVersion:CLASS_VERSION];
    }
}
#endif

+ newWithObject:(PyObject *) obj
{
  if (ObjCObject_Check (obj)) 
    {
    // YYYY Ronald: If Jack is right (see below), we should 'retain' the 
    // wrapped object to maintain the correct refcount
    id objc_obj = ObjCObject_GetObject(obj);
    
    //[objc_obj retain];
    return objc_obj;
    }
  else
    {
      id instance = [[self alloc] initWithObject:obj];
      
      // XXXX Jack thinks this shouldn't be done. And because these wrapper
      // objects used to be released as soon as we get back into the mainloop
      // he's strengthened in that belief:-)
      [instance autorelease];

      return instance;
    }
}

- initWithObject:(PyObject *) obj
{
  //Py_XDECREF(pyObject);
  pyObject = obj;
  Py_XINCREF(obj);

  return self;
}

#if 1
- (void)dealloc
{
  Py_XDECREF(pyObject);
  [super dealloc];
}
#else
// XXX Jack thinks this is a bad idea: this ObjC object is exactly one reference
// to the Python object (to be decreffed in dealloc)
- retain
{
  Py_XINCREF (pyObject);
  return [super retain];
}

- (oneway void) release
{
  [super release];
  Py_XDECREF (pyObject);
}
#endif

- (NSString *) description
{
  PyStringObject *repr = (PyStringObject *) PyObject_Repr (pyObject);
  if (repr)
    {
      NSString *result = [NSString stringWithCString:PyString_AS_STRING (repr)
				   length:PyString_GET_SIZE (repr)];

      Py_DECREF (repr);
      return result;
    }
  else
    {
      PyErr_Clear();
      return [super description];
    }
}
  
#define RETURN_RESULT(result) do {                                      \
  if (result)                                                           \
    {                                                                   \
      OC_PythonObject *ret = [[self class] newWithObject:result];       \
                                                                        \
      Py_DECREF (result);                                               \
      return ret;                                                       \
    }                                                                   \
  else {                                                                \
    PySys_WriteStderr("Error in Python call from ObjC:\n");             \
    PyErr_Print();                                                      \
    return nil;                                                         \
    }                                                                   \
} while(0)

- (void) doesNotRecognizeSelector:(SEL) aSelector
{
#define ERRORMSG " does not recognize -"
  const char *whoiam = [[super description] cString];
  const char *selname = [NSStringFromSelector (aSelector) cString];
  char buffer[strlen (whoiam) + sizeof ERRORMSG + strlen (selname) + 1];

  strcpy (buffer, whoiam);
  strcat (buffer, ERRORMSG);
  strcat (buffer, selname);
  PyErr_SetString (objc_error, buffer);
}


/*#F Check the argument count of the method/function @var{pymethod},
  returning the method itself if it matches @var{argcount}, NULL
  otherwise. */
static inline PyObject *
check_argcount (PyObject *pymethod, unsigned int argcount)
{
  if (pymethod && (PyFunction_Check (pymethod) || PyMethod_Check (pymethod)))
    {
      PyCodeObject *func_code;
      
      if (PyMethod_Check (pymethod))
        {
          func_code = (PyCodeObject *) PyFunction_GetCode (PyMethod_Function (pymethod));
          argcount++;           // for `self'
        }
      else
        func_code = (PyCodeObject *) PyFunction_GetCode (pymethod);
      
      if (func_code->co_argcount == argcount)
        return pymethod;
    }

  return NULL;
}


/*#F If the Python object @var{obj} implements a method whose name matches
  the Objective-C selector @var{aSelector} and accepts the correct number
  of arguments, return that method, otherwise NULL. */
static PyObject *
get_method_for_selector (PyObject *obj, SEL aSelector)
{
  if (aSelector)
    {
      const char *meth_name = [NSStringFromSelector (aSelector) cString];
      int len = strlen (meth_name);
      char *pymeth_name;
      unsigned int argcount;
      PyObject *pymethod;
      register const char *p;
      
      for (argcount=0, p=meth_name; *p; p++)
        if (*p == ':')
          argcount++;
  
      pymeth_name = alloca (PYTHONIFIED_LENGTH(meth_name, len, argcount));
#if PYTHONIFICATION_METHOD != WITH_BOTH
      pythonify_objc_message (meth_name, pymeth_name);

      pymethod = PyObject_GetAttrString (obj, pymeth_name);
      return check_argcount (pymethod, argcount);
#else
      {
        PyObject *meth;

        pythonify_objc_message (meth_name, pymeth_name, PYTHONIFICATION_FIRST_TRY);
        pymethod = PyObject_GetAttrString (obj, pymeth_name);
        meth = check_argcount (pymethod, argcount);
        if (meth)
          return meth;

#if PYTHONIFICATION_FIRST_TRY == WITH_DOUBLE_UNDERSCORE
        pythonify_objc_message (meth_name, pymeth_name, WITH_SINGLE_UNDERSCORE);
#else
        pythonify_objc_message (meth_name, pymeth_name, WITH_DOUBLE_UNDERSCORE);
#endif
        pymethod = PyObject_GetAttrString (obj, pymeth_name);
        meth = check_argcount (pymethod, argcount);
        if (meth)
          {
            if (Py_VerboseFlag)
              {
                char faster_name[200];
                
                fprintf (stderr, "PyObjC Warning: method `%s' matches `%s',\n\t", pymeth_name, meth_name);
                
                pythonify_objc_message (meth_name, faster_name, PYTHONIFICATION_FIRST_TRY);
                
                fprintf (stderr, "but `%s' would be faster.\n", faster_name);
              }

            return meth;
          }
      }
#endif /* PYTHONIFICATION_METHOD != WITH_BOTH */
    }
  return NULL;    
}


- (BOOL) respondsToSelector:(SEL) aSelector
{
  
  if ([super respondsToSelector:aSelector])
    {
    return YES;
    }
  else
    {
      PyObject *m;
    
      m = get_method_for_selector ([self pyObject], aSelector);

      if (m) {
        return YES;
      } else
        {
          PyErr_Clear();
          return NO;
        }
    }
}

- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel
{

  NSMethodSignature *result = nil;

  fflush(stdout);

  NS_DURING
    result = [super methodSignatureForSelector:sel];
  NS_HANDLER
    result = nil;
    NSLog( [localException name]);
    NSLog( [localException reason] );
  NS_ENDHANDLER
  
  if (!result)
    {
      const char *encoding = get_selector_encoding (self, sel);

      if (!encoding) {
	  PyObject *pymethod;

	  pymethod = get_method_for_selector ([self pyObject], sel);
	  if (pymethod) {
	      PyCodeObject *func_code;
	      int argcount;
		  
	      if (PyMethod_Check (pymethod))
		{
		  func_code = (PyCodeObject *) PyFunction_GetCode (PyMethod_Function (pymethod));
		  argcount = func_code->co_argcount-1; // adjust for `self'
		}
	      else
		{
		  func_code = (PyCodeObject *) PyFunction_GetCode (pymethod);
		  argcount = func_code->co_argcount;
		}

		/* XXXX Jack thinks we may be able to handle getting the signatures
		** if we make our Python classes subclass the corresponding ObjC
		** classes: we should be able to use instanceMethodSignatureForSelector
		*/
		/*
		** Hack by Jack: if our underlying Python object has a getObjCSignatureString
		** method we call that.
		*/
		if (PyObject_HasAttrString([self pyObject], "getObjCSignatureString")) {
			PyObject *sigstr;
			
			sigstr = PyObject_CallMethod([self pyObject], "getObjCSignatureString",
					"s", [NSStringFromSelector (sel) cString]);
			if (sigstr == NULL) {
				fprintf(stderr, "Exception in getObjCSignatureString()\n");
				PyErr_Clear();
			} else if (PyString_Check(sigstr)) {
				char *sigcstr = PyString_AsString(sigstr);
				
				id rv = [NSMethodSignature signatureWithObjCTypes:sigcstr];
				
				Py_DECREF(sigstr);
				return rv;
			} else {
				fprintf(stderr, "getObjCSignatureString() did not return a string\n");
				PyErr_Clear();
			}
		}
	  }
	/* Returning nil is not allowed here, crashes later in 
	** [NSInvocation newInvocationWithMethodSignature:]
	** XXXX For now we abort().
	*/
	abort();
	return nil;
      } else {
	return [NSMethodSignature signatureWithObjCTypes:encoding];
    }
    }
  return result;
}

- (void) forwardInvocation:(NSInvocation *) invocation
{
  NSMethodSignature *msign = [invocation methodSignature];
  SEL aSelector = [invocation selector];
  PyObject *pymethod;
  
  pymethod = get_method_for_selector ([self pyObject], aSelector);

  if (pymethod)
    {
      PyObject *args = NULL;
      unsigned int i, argcount;      
      PyCodeObject *func_code;
          
      if (PyMethod_Check (pymethod))
        {
          func_code = (PyCodeObject *) PyFunction_GetCode (PyMethod_Function (pymethod));
          argcount = func_code->co_argcount-1; // adjust for `self'
        }
      else
        {
          func_code = (PyCodeObject *) PyFunction_GetCode (pymethod);
          argcount = func_code->co_argcount;
        }
      
      args = PyTuple_New (argcount);
      if (args)
        {
          PyObject *result;

	  /*for (i=argcount+2; i>=2; i--) */
	  for (i=argcount+1; i>1; i--) 
	    {
	      const char *argtype;
	      char *argbuffer;
	      PyObject *pyarg;

	      NS_DURING
#ifdef NOTOSX
		argtype = [msign argumentInfoAtIndex:i].type;
#else
	      argtype = [msign getArgumentTypeAtIndex:i];
#endif
	      NS_HANDLER
		Py_DECREF(args);
	        fprintf (stderr, "error getting type of arg %d\n", i);
	        /* XXX Jack thinks this shouldn't happen */abort();
		[super forwardInvocation:invocation];
		return;
	      NS_ENDHANDLER
		
	      argbuffer = alloca (objc_sizeof_type (argtype));
	      [invocation getArgument:argbuffer atIndex:i];
	      pyarg = pythonify_c_value (argtype, argbuffer);

	      PyTuple_SET_ITEM (args, i-2, pyarg);
	    }
          result = PyObject_CallObject (pymethod, args);
  
          Py_DECREF(args);

	  if (result)
	    {
	      const char *rettype = [msign methodReturnType];
	      char *retbuffer = alloca (objc_sizeof_type (rettype));
	      const char *error;
	      
	      error = depythonify_c_value (rettype, result, retbuffer);
	      if (error)
		{
		  fprintf (stderr, "error depythonifying: %s\n", error);
		  /* XXX Jack thinks this shouldn't happen */abort();
		}
	      else
		[invocation setReturnValue:retbuffer];
	    }
	  else
	    {
                PySys_WriteStderr("Error in Python call from ObjC:\n");
                PyErr_Print();  /* this also clears the error */
            }
	      
        }
// XXXX Jack thinks that commenting out the super call is not the right thing to do.
// But if we enable it we get an exception.
//    } else {
//    	printf("WARNING: forwardInvocation: no Python method for %s\n", SELNAME(aSelector));
//    	fflush(stdout);
//    	[super forwardInvocation:invocation];
	}
	/*
  [super forwardInvocation:invocation];
  */
}    


// NUMBER PROTOCOL

- (int) numberCheck
{
  return PyNumber_Check ([self pyObject]);
}

- (id <PythonObject>) numberAdd:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Add (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberSubtract:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Subtract (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberMultiply:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Multiply (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberDivide:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Divide (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberRemainder:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Remainder (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberDivmod:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Divmod (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberPower:(id <PythonObject>) o2
                                 :(id <PythonObject>) o3
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *pyo3 = [o3 pyObject];
  PyObject *result = PyNumber_Power (pyo1, pyo2, pyo3);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberNegative
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Negative (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberPositive
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Positive (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberAbsolute
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Absolute (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberInvert
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Invert (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberLshift:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Lshift (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberRshift:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Rshift (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberAnd:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_And (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberXor:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Xor (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberOr:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PyNumber_Or (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberInt
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Int (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberLong
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Long (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) numberFloat
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PyNumber_Float (pyo);

  RETURN_RESULT(result);
}

// SEQUENCE PROTOCOL

- (int) sequenceCheck
{
  return PySequence_Check ([self pyObject]);
}

- (int) sequenceLength
{
  return PySequence_Length ([self pyObject]);
}

- (id <PythonObject>) sequenceConcat:(id <PythonObject>) o2
{
  PyObject *pyo1 = [self pyObject];
  PyObject *pyo2 = [o2 pyObject];
  PyObject *result = PySequence_Concat (pyo1, pyo2);

  RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceRepeat:(int) count
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PySequence_Repeat (pyo, count);

  RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceGetItem:(int) count
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PySequence_GetItem (pyo, count);

  RETURN_RESULT(result);
}
  
- (id <PythonObject>) sequenceGetSliceFrom:(int) i1 to:(int) i2
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PySequence_GetSlice (pyo, i1, i2);

  RETURN_RESULT(result);
}

- (int) sequenceSetItem:(int) i value:(id <PythonObject>) v
{
  
  PyObject *pyo = [self pyObject];
  PyObject *pyv = [v pyObject];

  return PySequence_SetItem (pyo, i, pyv);
}

- (int) sequenceDelItem:(int) i
{
  
  PyObject *pyo = [self pyObject];

  return PySequence_DelItem (pyo, i);
}

- (int) sequenceSetSliceFrom:(int) i1
                          to:(int) i2
                       value:(id <PythonObject>) v
{
  PyObject *pyo = [self pyObject];
  PyObject *pyv = [v pyObject];

  return PySequence_SetSlice (pyo, i1, i2, pyv);
}

- (int) sequenceDelSliceFrom:(int) i1
                          to:(int) i2
{
  PyObject *pyo = [self pyObject];

  return PySequence_DelSlice (pyo, i1, i2);
}

- (id <PythonObject>) sequenceTuple
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PySequence_Tuple (pyo);

  RETURN_RESULT(result);
}

- (id <PythonObject>) sequenceList
{
  PyObject *pyo = [self pyObject];
  PyObject *result = PySequence_List (pyo);

  RETURN_RESULT(result);
}

- (int) sequenceCount:(id <PythonObject>) value
{
  PyObject *pyo = [self pyObject];
  PyObject *pyv = [value pyObject];

  return PySequence_Count (pyo, pyv);
}

- (int) sequenceIn:(id <PythonObject>) value
{
  PyObject *pyo = [self pyObject];
  PyObject *pyv = [value pyObject];

  return PySequence_In (pyo, pyv);
}

- (int) sequenceIndex:(id <PythonObject>) value
{
  PyObject *pyo = [self pyObject];
  PyObject *pyv = [value pyObject];

  return PySequence_Index (pyo, pyv);
}

// CALLING PROTOCOL

- (int) callableCheck
{
  return PyCallable_Check ([self pyObject]);
}

- (id <PythonObject>) callableCall:(id <PythonObject>) args
{
  PyObject *pyo = [self pyObject];
  PyObject *pyargs = [args pyObject];
  PyObject *result = PyObject_CallObject (pyo, pyargs);

  RETURN_RESULT(result);
}

- (id <PythonObject>) callableCallFunction:(char *) format, ...
{
  va_list va;
  PyObject *args;
  PyObject *result;

  va_start (va, format);

  if (format)
    args = Py_VaBuildValue (format, va);
  else
    args = PyTuple_New (0);
  
  va_end(va);
  
  if (! args)
    return nil;

  if(! PyTuple_Check (args))
    {
      PyObject *a = PyTuple_New (1);

      if (!a)
        return nil;
      PyTuple_SET_ITEM (a, 0, args);

      args = a;
    }

  result = PyObject_CallObject ([self pyObject], args);
  
  Py_DECREF(args);
  
  RETURN_RESULT(result);
}

- (id <PythonObject>) callableCallMethod:(char *) m
                                withArgs:(char *) format, ...
{
  va_list va;
  PyObject *args;
  PyObject *method;
  PyObject *result;

  method = PyObject_GetAttrString ([self pyObject], m);
  if (! method)
    {
      PyErr_SetString (PyExc_AttributeError, m);
      return nil;
    }
  else if (! PyCallable_Check (method))
    {
      PyErr_SetString(PyExc_TypeError,"call of non-callable attribute");
      return nil;
    }
  
  va_start (va, format);

  if (format)
    args = Py_VaBuildValue (format, va);
  else
    args = PyTuple_New (0);
  
  va_end(va);
  
  if (! args)
    return nil;

  if(! PyTuple_Check (args))
    {
      PyObject *a = PyTuple_New (1);

      if (!a)
        return nil;
      PyTuple_SET_ITEM (a, 0, args);

      args = a;
    }

  result = PyObject_CallObject (method, args);
  
  Py_DECREF(args);
  
  RETURN_RESULT(result);
}


// MAPPING PROTOCOL

- (int) mappingCheck
{
  return PyMapping_Check ([self pyObject]);
}

- (int) mappingLength
{
  return PyMapping_Length ([self pyObject]);
}

- (int) mappingDelItemCString:(char *) key
{
  return PyMapping_DelItemString ([self pyObject], key);
}

- (int) mappingDelItemString:(NSString *) key
{
  return PyMapping_DelItemString ([self pyObject], (char *) [key cString]);
}

- (int) mappingDelItem:(id <PythonObject>) key
{
  return PyMapping_DelItem ([self pyObject], [key pyObject]);
}

- (int) mappingHasKeyCString:(char *) key
{
  return PyMapping_HasKeyString ([self pyObject], key);
}

- (int) mappingHasKeyString:(NSString *) key
{
  return PyMapping_HasKeyString ([self pyObject], (char *) [key cString]);
}

- (int) mappingHasKey:(id <PythonObject>) key
{
  return PyMapping_HasKey ([self pyObject], [key pyObject]);
}

- (id <PythonObject>) mappingKeys
{
  PyObject *pykeys = PyMapping_Keys ([self pyObject]);

  RETURN_RESULT(pykeys);
}

- (id <PythonObject>) mappingItems
{
  PyObject *pyitems = PyMapping_Items ([self pyObject]);

  RETURN_RESULT(pyitems);
}

- (id <PythonObject>) mappingValues
{
  PyObject *pyvalues = PyMapping_Values ([self pyObject]);

  RETURN_RESULT(pyvalues);
}

- (id <PythonObject>) mappingGetItemCString:(char *) key
{
  PyObject *result = PyMapping_GetItemString ([self pyObject], key);

  RETURN_RESULT(result);
}

- (id <PythonObject>) mappingGetItemString:(NSString *) key
{
  PyObject *result = PyMapping_GetItemString ([self pyObject], (char *) [key cString]);

  RETURN_RESULT(result);
}

- (int) mappingSetItemCString:(char *) key value:(id <PythonObject>) value
{
  return PyMapping_SetItemString ([self pyObject], key, [value pyObject]);
}

- (int) mappingSetItemString:(NSString *) key value:(id <PythonObject>) value
{
  return PyMapping_SetItemString ([self pyObject],
				  (char *) [key cString], [value pyObject]);
}


// PYTHON OBJECT PROTOCOL

- (PyObject *) pyObject
{
  return pyObject;
}

- (int) print:(FILE *) fp flags:(int) flags
{
  return PyObject_Print ([self pyObject], fp, flags);
}

- (int) hasAttrCString:(char *) attr_name
{
  return PyObject_HasAttrString ([self pyObject], attr_name);
}

- (int) hasAttrString:(NSString *) attr_name
{
  return PyObject_HasAttrString ([self pyObject], (char *) [attr_name cString]);
}

- (id <PythonObject>) getAttrCString:(char *) attr_name
{
  PyObject *result = PyObject_GetAttrString ([self pyObject], attr_name);

  RETURN_RESULT(result);
}

- (id <PythonObject>) getAttrString:(NSString *) attr_name
{
  PyObject *result = PyObject_GetAttrString ([self pyObject], (char *) [attr_name cString]);

  RETURN_RESULT(result);
}

- (int) hasAttr:(id <PythonObject>) attr_name
{
  return PyObject_HasAttr ([self pyObject], [attr_name pyObject]);
}

- (id <PythonObject>) getAttr:(id <PythonObject>) attr_name
{
  PyObject *result = PyObject_GetAttr ([self pyObject], [attr_name pyObject]);

  RETURN_RESULT(result);
}

- (int) setAttrCString:(char *) attr_name value:(id <PythonObject>) value
{
  return PyObject_SetAttrString ([self pyObject], attr_name, [value pyObject]);
}

- (int) setAttrString:(NSString *) attr_name value:(id <PythonObject>) value
{
  return PyObject_SetAttrString ([self pyObject], (char *) [attr_name cString], [value pyObject]);
}

- (int) setAttr:(id <PythonObject>) attr_name value:(id <PythonObject>) value
{
  return PyObject_SetAttr ([self pyObject], [attr_name pyObject], [value pyObject]);
}

- (int) delAttrCString:(char *) attr_name
{
  return PyObject_DelAttrString ([self pyObject], attr_name);
}

- (int) delAttrString:(NSString *) attr_name
{
  return PyObject_DelAttrString ([self pyObject], (char *) [attr_name cString]);
}

- (int) delAttr:(id <PythonObject>) attr_name
{
  return PyObject_DelAttr ([self pyObject], [attr_name pyObject]);
}

- (int) cmp:(id <PythonObject>) o2 result:(int *) result
{
  return PyObject_Cmp ([self pyObject], [o2 pyObject], result);
}

- (int) compare:(id <PythonObject>) o2
{
  return PyObject_Compare ([self pyObject], [o2 pyObject]);
}

- (id <PythonObject>) repr
{
  RETURN_RESULT(PyObject_Repr ([self pyObject]));
}

- (id <PythonObject>) str
{
  RETURN_RESULT(PyObject_Str ([self pyObject]));
}

- (unsigned int) hash
{
  return PyObject_Hash ([self pyObject]);
}

- (int) isTrue
{
  return PyObject_IsTrue ([self pyObject]);
}

- (id <PythonObject>) type
{
  RETURN_RESULT(PyObject_Type ([self pyObject]));
}

- (unsigned int) length
{
  int len = PyObject_Length ([self pyObject]);

#if 0
  if (len < 0)
    [NSException raise:PyObjCException format:@"PyObject_Length() returned -1"];
#endif

  return len;
}

- (unsigned int) count
{
  return [self length];
}

- (id <PythonObject>) getItem:(id <PythonObject>) key
{
  RETURN_RESULT(PyObject_GetItem ([self pyObject], [key pyObject]));
}

- (int) setItem:(id <PythonObject>) key value:(id <PythonObject>) v
{
  return PyObject_SetItem ([self pyObject],
                           [key pyObject],
                           [v pyObject]);
}

- (int) delItem:(id <PythonObject>) key
{
  return PyObject_DelItem ([self pyObject], [key pyObject]);
}


@end /* OC_PythonObject class implementation */
