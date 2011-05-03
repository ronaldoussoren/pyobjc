
@interface OC_PythonEnumerator : NSEnumerator
{
	PyObject* value;
	BOOL      valid;
}

+enumeratorWithPythonObject:(PyObject*)object;
-initWithPythonObject:(PyObject*)object;

@end
