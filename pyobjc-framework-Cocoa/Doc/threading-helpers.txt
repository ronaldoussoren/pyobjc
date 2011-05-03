=============================
Utility methods for threading
=============================

``NSObject`` has a number of methods for calling selectors in different 
contexts, such as after a delay or on another thread.

These methods can be called from Python (of course), but you need to be a bit
carefull because the implementation of these methods won't catch exceptions
for you and therefore an uncaught exception in your python code can cause 
the runloop to stop due to an exception, which might terminate your program.

To make matters worse, due to a bug in Python 2.5 this will cause a hard
crash (segmentation fault) when this happens with 
``performSelectorOnMainThread:withObject:waitUntilDone:``.

Because of this PyObjC 2.1 provides a category on ``NSObject`` that implements
safe alternatives to the stock ``NSObject`` methods.

Safe replacements for stock ``NSObject`` methods
------------------------------------------------

These safe replacements have the same signature as the stock ``NSObject`` 
methods, but will log exceptions instead of letting them escape into the rest
of your program.

* ``pyobjc_performSelector_onThread_withObject_waitUntilDone_``

  This is the safe alternative for 
  ``performSelector_onThread_withObject_waitUntilDone_``.

  (Introduced in Mac OS X 10.5)

* ``pyobjc_performSelector_onThread_withObject_waitUntilDone_modes_``

  This is the safe alternative for 
  ``performSelector_onThread_withObject_waitUntilDone_modes_``.

  (Introduced in Mac OS X 10.5)

* ``pyobjc_performSelector_withObject_afterDelay_``

  This is the safe alternative for 
  ``performSelector_withObject_afterDelay_``.

* ``pyobjc_performSelector_withObject_afterDelay_inModes_``

  This is the safe alternative for 
  ``performSelector_withObject_afterDelay_inModes_``.

* ``pyobjc_performSelectorInBackground_withObject_``

  This is the safe alternative for 
  ``performSelectorInBackground_withObject_``.

  (Introduced in Mac OS X 10.5)

* ``pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_``

  This is the safe alternative for 
  ``performSelectorOnMainThread_withObject_waitUntilDone_``.

* ``pyobjc_performSelectorOnMainThread_withObject_waitUntilDone_modes_``

  This is the safe alternative for 
  ``performSelectorOnMainThread_withObject_waitUntilDone_modes_``.


Enhanced methods
----------------

The stock methods are quite useful, but at times it is usefull to get the
result back from the other thread. The methods below will call the selector
on another thread and will return the result from that call in the current
thread. If the call on the "other" thread raises an exception this exception
will be reraised in the current thread.

Note: these methods are synchronous, that is, they block the current thread
until the call on the "other" thread is done. 

As an example:

  .. sourcecode:: python
      :linenos:

	class MyClass (NSObject):

	   def divideByZero_(self, arg):
	   	return arg/0

	   def doit(self):
	       try:
	           result = self.performSelectorOnMainThread_withObject_(
		        'divideByZero:', 55)
		   print result

	       except:
	           print "Division failed"

The available methods are:

* ``pyobjc_performSelector_onThread_withObject_(selector, thread, arg)``

  (Introduced in Mac OS X 10.5)

* ``pyobjc_performSelector_onThread_withObject_modes_(selector, thread, arg, modes)``

  (Introduced in Mac OS X 10.5)

* ``pyobjc_performSelectorOnMainThread_withObject_(selector, arg)``

* ``pyobjc_performSelectorOnMainThread_withObject_modes_(selector, arg, modes)``
