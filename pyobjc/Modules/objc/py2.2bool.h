/*
 *  A boolean type for python 2.2, this is basicly a copy of boolobject.h from
 *  Python 2.3. The python license applies.
 *
 *  Copyright PSF.
 */

/* Boolean object interface */

#ifndef PyObjC_BOOLOBJECT_H
#define PyObjC_BOOLOBJECT_H

#if PY_VERSION_HEX >= 0x0203000A /* Python 2.3a0 or later */

#define PyObjCBool_Check(x) PyBool_Check(x)
#define PyObjCBool_FromLong(x) PyBool_FromLong(x)

#else /* Python 2.2 */

typedef PyIntObject PyObjCBoolObject;

extern PyTypeObject PyObjCBool_Type;

#define PyObjCBool_Check(x) ((x)->ob_type == &PyObjCBool_Type)

/* Function to return a bool from a C long */
PyObject * PyObjCBool_FromLong(long);

#endif /* Python 2.2 */

#endif /* PyObjC_BOOLOBJECT_H */
