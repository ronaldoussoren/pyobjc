/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: ObjC.h,v
 * Revision: 1.30
 * Date: 1998/08/18 15:35:53
 *
 * Created Thu Sep 5 16:04:09 1996.
 */

#ifndef _ObjC_H
#define _ObjC_H

/* Version of the module. Should be bumped at each release.
   Versions < 1.0 are to be considered buggy, incomplete and
   NOT stable */
#define PyObjC_VERSION 0.55

/* Foundation headers */
#import <Foundation/Foundation.h>

/* Python header file */
#include "Python.h"

/* Exception raised for ObjC specific errors */
extern PyObject *ObjC_Error;
extern NSString *PyObjCException;

/****************************/
/*** ObjCObject interface ***/
/****************************/

/* Python wrapper around ObjC id (instance or class) */
typedef struct
{
  PyObject_HEAD
    
  id        oc_object;          // The real ObjC object
  PyObject *methods;            // Methods cache
} ObjCObject;

/* Corresponding Python type object */
extern PyTypeObject ObjCObject_Type;

/* Corresponding Python type check macro */
#define ObjCObject_Check(o) ((o)->ob_type->tp_name == ObjCObject_Type.tp_name)
#define ObjCSequenceObject_Check(o) (ObjCObject_Check (o) && (o)->ob_type->tp_as_sequence)
#define ObjCMappingObject_Check(o) (ObjCObject_Check (o) && (o)->ob_type->tp_as_mapping)

extern ObjCObject *ObjCObject_new (id obj);

#define ObjCObject_OBJECT(o) (((ObjCObject *)(o))->oc_object)

/****************************/
/*** ObjCMethod interface ***/
/****************************/

/* Python wrapper around ObjC SEL */
typedef struct
{
  PyObject_HEAD

  NSInvocation *inv;
} ObjCMethod;

/* Corresponding Python type object */
extern PyTypeObject ObjCMethod_Type;

/* Corresponding Python type check macro */
#define ObjCMethod_Check(o) ((o)->ob_type == &ObjCMethod_Type)

extern ObjCMethod *ObjCMethod_new_with_name (ObjCObject *obj, const char *meth_name);
extern ObjCMethod *ObjCMethod_new_with_selector (ObjCObject *obj, SEL sel);


/*****************************/
/*** ObjCPointer interface ***/
/*****************************/

/* Python wrapper around C pointer */
typedef struct
{
  PyObject_VAR_HEAD

  void *ptr;
  PyStringObject *type;
  char contents[0];
} ObjCPointer;

/* Corresponding Python type object */
extern PyTypeObject ObjCPointer_Type;

/* Corresponding Python type check macro */
#define ObjCPointer_Check(o) ((o)->ob_type == &ObjCPointer_Type)

extern ObjCPointer *ObjCPointer_new (void *ptr, const char *type);

/*****************************/
/*** ObjCRuntime interface ***/
/*****************************/

typedef struct
{
  PyObject_HEAD

  PyObject *classes;                          // classes cache
} ObjCRuntime;

/* Corresponding Python type object */
extern PyTypeObject ObjCRuntime_Type;

/* Corresponding Python type check macro */
#define ObjCRuntime_Check(o) ((o)->ob_type == &ObjCRuntime_Type)

extern ObjCRuntime *ObjCRuntime_new (void);

#define FUNDESCR(s) s "\n"
#define FUNSYN(s) "\nSynopsis:\t" s "\n"
#define FUNARGS(s) "Arguments:\t" s "\n"
#define FUNRET(s) "Returns:\t" s "\n"
#define FUNDOC(d,s,a,r) FUNDESCR(d) FUNSYN(s) FUNARGS(a) FUNRET(r)

#endif /* _ObjC_H */
