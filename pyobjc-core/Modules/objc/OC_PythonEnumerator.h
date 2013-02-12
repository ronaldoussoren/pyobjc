#ifndef PyObjC_PythonEnumerator_H
#define PyObjC_PythonEnumerator_H

@interface OC_PythonEnumerator : NSEnumerator
{
    PyObject* value;
    BOOL      valid;
}

+(instancetype)enumeratorWithPythonObject:(PyObject*)object;
-(id)initWithPythonObject:(PyObject*)object;

@end

#endif /* PyObjC_PythonEnumerator_H */
