==================
Currency Converter
==================

:author: Ronald Oussoren
:contact: ronaldoussoren@mac.com

.. contents:

Introduction
------------

This is a port of the `Currency Converter`_ example from the Cocoa tutorial
to Python (via PyObjC).  Development is done in "standalone" mode.  That is,
the buildapp.py script is used to build an application wrapper that can be
launched like any other Cocoa application.

Building the App
----------------

To build the app, invoke the buildapp.py script::

   python buildapp.py build

This will build the CurrencyConverter application in the directory build
within the current working directory as *CurrencyConverter.app*.

.. _`Currency Converter`: file:///Developer/Documentation/Cocoa/ObjCTutorial/index.html 
