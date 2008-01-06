============
Contributors
============

This page gives a small overview of the history of PyObjC, and lists some of the people that are 
involved in its development. The page is incomplete and chaotic.

Core developers
---------------

In recent times the core development team is very small, just one person really: Ronald Oussoren.

Bill Bumgarner maintains the XCode templates for PyObjC development from XCode.

Contributors
------------

Many, many people have contributed to the PyObjC module in the recent months.  The mailing list 
should be parsed to complete this list.

* Just van Rossum contributed numerous bits of python that both simplified the use of PyObjC and 
  increased its power.

* Jack Jansen has provided constant technical assistance and direction based on his wealth of 
  experience as the primary developer of the MacPython project.

* Jim Tittsler provided a significant chunk of the look/feel of this web site, including the 
  PyDog graphic.

History
--------

In 2007 Apple shipped PyObjC 2.0 as a component of Mac OS X 10.5 (Leopard).

In the fall of 2002, Bill Bumgarner <bbum@codefab.com> added support for non-Framework builds of 
python.  Ronald and Bill subsequently added support for the Apple supplied build of Python. Bill 
created the Project Builder template that allows for building standalone Cocoa applications that are implemented in Project Builder.

Ronald Oussoren <ronaldoussoren@mac.com> rewrote most of the module in 2002.  Ronald made it 
possible to subclass Objective-C classes from Python and added nearly complete support for the 
Foundation, the AppKit and the AddressBook frameworks.

Steve Majewski <sdm7g@minsky.med.virginia.edu> and Bill Bumgarner <bbum@codefab.com> picked up 
Lele's work in early November, 2000. Steve significanlty improved compatibility with OS X.

History prior to 2000 is a bit fuzzy.  Jeff Sickel contributed numerous patches and features over 
the years.

Lele Gaifax built the original module which dates back to September 1996.  Lele's original list of contributors/motivators was as follows:

::

   I should say "Grazie" to many persons that made this possible, but to some in particular:

   * Guido van Rossum <guido@CNRI.Reston.VA.US>:
     Long list of motivation omitted ;-)
   * Thomas Breuel <tmb@best.com>:
     He first inspired me with good ideas.
   * Ted Horst <ted_horst@il.us.swissbank.com>:
     His own ObjC module and kind comments helped me a lot.
   * Bill Bumgarner <bbum@friday.com>:
     He contributed the standalone packaging setup, good comments and his own implementation of 
     the Streams and Pasteboards support. He  maintained also several Python-related packages for 
     NeXTSTEP: see <ftp://ftp.thoughtport.net/pub/next/lang> 
     [long gone;  see http://www.friday.com/software/python/]

  ...and of course to the entire ObjC-SIG community.

My (bbum's) memory</a> is far from perfect.  Please feel free to send corrections and updates to the
pyobjc-dev list!  In particular, I believe that the objc module was shipped with the core python 
distribution at one point, but I can't find any information about that.

I (ronald) did some some digging, and there has been an ``objc`` module that was part of the core 
python distribution. This was part of the 1.3 release of python (released in 1995) and claims to be 
written by Jon M. Kutemeier and maintained by Guido van Rossum. It was removed in the 1.4 release 
of Python.
