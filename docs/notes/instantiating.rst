Instantiating Objective-C objects
=================================


.. versionchanged:: 10.4

   The Pythonic interface for instantiation classes
   was added.

Objective-C uses a two step object instantatin
process, similar to Python's ``__new__`` and
``__init__`` methods, but with explicit invocation
of the methods ``alloc`` and ``init``. By default
this is mirrored in the Python proxies:

.. sourcecode:: python

   some_value = NSObject.alloc().init()

   some_button = NSButton.alloc().initWithFrame_(some_frame)


This looks very foreign in Python, therefore PyObjC
also supports a condensed version of this by directly
calling the class::

.. sourcecode:: python

   some_value = NSObject()

   some_button = NSButton(frame=some_frame)

The generic rules for instantiation objects through calling
the class are:

* Calling the class without arguments in supported unless
  the ``init`` method has been marked with ``NS_UNAVAILABLE``
  in Apple's SDK.

* Every instance selector of the Objective-C with a name starting
  with ``init`` adds a possible set of keyword arguments using
  the following algorithm:

  1. Strip ``initWith`` or ``init`` from the start of the selector;

  2. Lowercase the first character of the result

  3. All segments are now keyword only arguments, in that order.

  For example given, ``-[SomeClass initWithX:y:z]`` the
  following invocation is valid: ``SomeClass(x=1, y=2, z=3)``.
  Using the keywords in a different order is not valid.

* Some classes may have additional sets of keyword arguments,
  whose will be documented in the framework notes. In general
  those will be based on factory class methods for which there
  are no equivalent using the ``alloc().init...(...)`` pattern.
