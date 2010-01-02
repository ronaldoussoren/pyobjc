================================================
Converting values between Python and Objective-C
================================================

Introduction
------------

PyObjC provides transparant conversion or proxying of values between Python
and Objective-C. In general this works as expected, this document provides
a detailed guide to how values are converted or proxied.


Basic C types
-------------

The Objective-C language not only has classes and objects, but also has the
basic C types which are not classes. PyObjC converts between those and the
corresponding Python type. 

The C type 'char' does not have a unambigous meaning in C, it is used for
a number of tasks. In the table below the various tasks have been represented
separately: booleans (:ctype:`BOOL`), representing characters in text 
(:ctype:`char`) and represeting small integers (:ctype:`int8_t`).  PyObjC 
uses metadata in the framework wrappers to know when to use which 
representation.

 
=========================== ============================== ========================
C type                      Python 2.x                     Python 3.x
=========================== ============================== ========================
:ctype:`int8_t`             :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`BOOL`               :class:`bool`                  :class:`bool`
--------------------------- ------------------------------ ------------------------
char                        :class:`str` of len(1)         :class:`bytes` of len(1)
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned char`      :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`short`              :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned short`     :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`int`                :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned int`       :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`int`                :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned int`       :class:`int` or :class:`long`  :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`long`               :class:`int`                   :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned long`      :class:`int` or :class:`long`  :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`long long`          :class:`int` or :class:`long`  :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`unsigned long long` :class:`int` or :class:`long`  :class:`int`
--------------------------- ------------------------------ ------------------------
:ctype:`float`              :class:`float`                 :class:`float`
--------------------------- ------------------------------ ------------------------
:ctype:`double`             :class:`float`                 :class:`float`
=========================== ============================== ========================

PyObjC does range checking when converting values to C, and will raise
:exc:`ValueError` when the input value is out of range.

PyObjC will accept negative values when converting a Python numeric value
to an unsigned integer value. This is done due to limitations in the 
metadata creation process, sometimes constant values that are used with 
unsigned integer arguments are represented as negative values in the 
metadata files.  This feature will be fixed in a future version of PyObjC 
and users should therefore not rely on being able to convert negative
values to an unsigned integer type.


Compound C types
----------------

Arrays
......

TDB

Structs
........

TDB

Unions
......

PyObjC cannot convert to and from C union types at the moment.


Classes and instances
---------------------

TBD

Functions and methods
---------------------

TBD
