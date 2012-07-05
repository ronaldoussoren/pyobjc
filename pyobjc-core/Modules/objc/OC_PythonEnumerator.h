
@interface OC_PythonEnumerator : NSEnumerator
{
	PyObject* value;
	BOOL      valid;
}

+(instancetype)enumeratorWithPythonObject:(PyObject*)object;
-(id)initWithPythonObject:(PyObject*)object;

@end
