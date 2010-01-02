:mod:`objc` -- The PyObjC bridge
================================

.. module:: objc
   :platform: MacOS X
   :synopsis: The PyObjC bridge

.. moduleauthor:: Ronald Oussoren <ronaldoussoren@mac.com>

Introduction
------------

The module :mod:`objc` is the core of PyObjC and provides the automatic 
bridging between Python and Objective-C. It also provides a number of
utility functions and types that make it easier to integrate Python
and Objective-C code.

Accessing classes
.................

.. function:: lookUpClass(classname)


   :param classname: the name of an Objective-C class
   :type classname: string
   :return: the named Objective-C class
   :raise: :exc:`objc.nosuchclass_error` when the class does not exist


Utility functions
.................

.. function:: splitSignature(typestring)

   Split an encoded Objective-C signature string into the
   encoding strings for seperate types.

   :param typestring: an encoded method signature
   :return: list of type signatures
   :type typestring: byte string
   :rtype: list of byte strings



