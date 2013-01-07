==================
Currency Converter
==================

Introduction
------------

This is a port of the "Currency Converter" example from the Cocoa tutorial
to Python (via PyObjC).  Development is done in "standalone" mode.  That is,
the setup.py script is used to build an application wrapper that can be
launched like any other Cocoa application.

Building the App
----------------

To build the app, invoke the setup.py script::

   python setup.py py2app

This will build the CurrencyConverter application in the directory *dist*
within the current working directory as *CurrencyConverter.app*.
