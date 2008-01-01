/*
 * VariableLengthList 
 */
#ifndef PyObjC_VARLIST_H
#define  PyObjC_VARLIST_H

extern PyTypeObject PyObjC_VarList_Type;

PyObject* PyObjC_VarList_New(const char* tp, void* array);

#endif /* PyObjC_VARLIST_H */
