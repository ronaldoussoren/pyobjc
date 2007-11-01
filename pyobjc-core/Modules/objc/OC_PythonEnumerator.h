
@interface OC_PythonEnumerator : NSEnumerator
{
	PyObject* value;
	BOOL      valid;
}

+newWithPythonObject:(PyObject*)object;
-initWithPythonObject:(PyObject*)object;

@end
