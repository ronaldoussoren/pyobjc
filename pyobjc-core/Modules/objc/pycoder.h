#ifndef PyObjC_PYCODER_H
#define PyObjC_PYCODER_H
/* 
 * Support code for NSCode-ing a Python object that supports the pickling
 * protocol.
 *
 * The implementation mirrors the pickle protocol to encode a Python object
 * into an NSCoder.
 *
 * NOTE: The current implementation is not tuned for size, but for easy
 * to understand and correct code.
 */
#include "pyobjc.h"

PyObject* PyObjC_decode_object(NSCoder* coder);
int PyObjC_encode_object(NSCoder* coder, PyObject* object);

#endif PyObjC_PYCODER_H
