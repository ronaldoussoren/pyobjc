=========================
An introduction to PyObjC
=========================

..	:authors: Ronald Oussoren, Bob Ippolito
	:contact: pyobjc-dev@lists.sourceforge.net
	:URL: http://pyobjc.sourceforge.net/
	:copyright: 2003-2013 The PyObjC Project

Preface
-------

PyObjC is a bridge between Python and Objective-C.  It allows Python 
scripts to use and extend existing Objective-C class libraries;
most importantly the `Cocoa libraries`_ by `Apple`_.

This document describes how to use Objective-C class libraries from Python
scripts and how to interpret the documentation of those libraries from the 
point of view of a Python programmer.

.. _`Apple`: http://www.apple.com/

First Steps
-----------

When dealing with the Objective-C runtime, there are certain patterns
you need to learn when writing Python code.  If you're not already an
Objective-C programmer, some of them will seem strange or even
"un-pythonic" at first.  However, you will get used to it, and the way
that PyObjC works is quite compliant with the :pep:`20` (the Zen of Python,
``import this``).  In fact, Ronald is Dutch ;)

With no further ado, here are the three most important things you
*must* know before embarking on any PyObjC voyage:

Underscores, and lots of them
.............................

Objective-C objects communicate with each other by sending messages.
The syntax for messages is somewhere in-between Python's positional and
keyword arguments.  Specificlaly, Objective-C message dispatch uses
positional arguments, but parts of the message name (called "selector"
in Objective-C terminology) are interleaved with the arguments.

An Objective-C message looks like this:

  .. sourcecode:: objective-c

      [someObject doSomething:arg1 withSomethingElse:arg2];

The selector (message name) for the above snippet is this (note the colons):

  .. sourcecode:: objective-c

      doSomething:withSomethingElse:

In order to have a lossless and unambiguous translation between Objective-C
messages and Python methods, the Python method name equivalent is simply
the selector with colons replaced by underscores.  Since each colon in an
Objective-C selector is a placeholder for an argument, the number of
underscores in the PyObjC-ified method name is the number of arguments
that should be given.

The PyObjC translation of the above selector is (note the underscores):

  .. sourcecode:: python

      doSomething_withSomethingElse_

The message dispatch, translated to PyObjC, looks like this:

  .. sourcecode:: python

      someObject.doSomething_withSomethingElse_(arg1, arg2)

*Methods that take one argument will have a trailing underscore*.

It may take a little while to get used to, but PyObjC does not ever
rename selectors.  The trailing underscore will seem strange at first,
especially for cases like this:

  .. sourcecode:: python

      # note the trailing underscore
      someObject.setValue_(aValue)

There are a few additional rules regarding message dispatch, see the 
`Overview of the bridge`_ for the complete rundown.

Two-phase instantiation
.......................

Objective-C, being a low-level runtime, separates the two concepts required
to instantiate an object.

allocation:
    Reserve a chunk of memory large enough to hold the new object, and make
    sure that all of its declared instance variables are set to "zero"
    (this means nil pointers to objects, 0 for integers, etc.).

initialization:
    Fill in the blank slate allocated by the allocation phase.

In Objective-C, the convention is for allocation to be performed by a class
method called ``alloc``, and initialization is done with method
*beginning with* the word ``init``.  For example, here is the syntax for
instantiating an ``NSObject``:

  .. sourcecode:: python

     myObject = NSObject.alloc().init()

And here is an example for creating an ``NSData`` instance given a few bytes:

  .. sourcecode:: python

     myData = NSData.alloc().initWithBytes_length_('the bytes', 9)

You must also follow this convention when subclassing Objective-C classes.
When initializing, an object must always (directly or indirectly) call the
designated initializer of its ``super``.  The designated initializer is the
"most basic" initializer through which all initialization eventually ends up.
The designated initializer for ``NSObject`` is ``init``.  To find the
designated initializer for other classes, consult the documentation for that
class.  Here is an example of an ``NSObject`` subclass with a customized
initialization phase:

  .. sourcecode:: python
     :linenos:

     class MyClass(NSObject):

        def init(self):
            """
            Designated initializer for MyClass
            """
            # ALWAYS call the super's designated initializer.
            # Also, make sure to re-bind "self" just in case it
            # returns something else, or even None!
            self = super(MyClass, self).init()
	    if self is None: return None

            self.myVariable = 10

            # Unlike Python's __init__, initializers MUST return self,
            # because they are allowed to return any object!
            return self


     class MyOtherClass(MyClass):

        def initWithOtherVariable_(self, otherVariable):
            """
            Designated initializer for MyOtherClass
            """
            self = super(MyOtherClass, self).init()
	    if self is None: return None

            self.otherVariable = otherVariable
            return self

     myInstance = MyClass.alloc().init()
     myOtherInstance = MyOtherClass.alloc().initWithOtherVariable_(20)

Many Objective-C classes provide class methods that perform two-phase
instantiation for you in one step.  Several examples of this are:

 .. sourcecode:: python
    :linenos:

    # This is equivalent to:
    #
    #   myObject = NSObject.alloc().init()
    #
    myObject = NSObject.new()

    # This is equivalent to:
    #
    #   myDict = NSDictionary.alloc().init()
    #
    myDict = NSDictionary.dictionary()

    # This is equivalent to:
    #
    #   myString = NSString.alloc().initWithString_(u'my string')
    #
    myString = NSString.stringWithString_(u'my string')

Objective-C uses accessors everywhere
.....................................

Unlike Python, Objective-C convention says to use accessors rather than
directly accessing instance variables of other objects.  This means
that in order to access an instance variable ``value`` of an object
``valueContainer`` you will have to use the following syntax:

 .. sourcecode:: python
    :linenos:

    # Getting
    #
    # notice the method call
    #
    myValue = valueContainer.value()

    # Setting
    #
    # notice the naming convention and trailing underscore
    #
    valueContainer.setValue_(myNewValue)

When writing your own classes from Python, this is a bit harder since
Python only has one namespace for all attributes, even methods.  If you
choose to implement accessors from Python, then you will have to name
the instance variable something else:

 .. sourcecode:: python
    :linenos:

    class MyValueHolder(NSObject):

        def initWithValue_(self, value):
            self = super(MyValueHolder, self).init()
            # It's recommended not to use typical Python convention here,
            # as instance variables prefixed with underscores are reserved
            # by the Objective-C runtime.  It still works if you use
            # underscores, however.
            self.ivar_value = value
            return self

        def value(self):
            return self.ivar_value

        def setValue_(self, value):
            self.ivar_value = value

It's also possible to use `Key-Value Coding`_ in some cases, which eliminates
the need for writing most accessors, but only in scenarios where the rest of
the code is using it.

Objective-C for PyObjC users
----------------------------

It is recommended that you take the time to understand a little bit about
Objective-C before jumping into PyObjC development.  The class libraries
that you will be using from Cocoa are not documented in Python, and their
documentation will be confusing without a grasp on the semantics and syntax
of Objective-C.

Objective-C is an object-oriented programming language implemented as a
superset of C that borrows heavily in concept and syntax from Smalltalk.
of C and borrows heavily from Smalltalk.  It features single inheritance with
dynamic dispatch and (in theory) multiple root classes.  This is basically the
same as Python with single inheritance.

An important difference between Python and Objective-C is that the latter is
not a pure object-oriented language.  Some values are not objects, but values
of plain C types, such as ``int`` and ``double``.  These basic C types can 
be used as the types of arguments and the return value of methods. 

Object allocation and initialization are explicit and separate actions in 
Objective-C.  The former is done by the class-method ``alloc``, while the
latter is done by instance methods whose name customarily starts with ``init``.

Objective-C code looks just like plain C code, with some easily recognizable
Smalltalk-like extensions for the object-oriented parts of the language.  An
example class declaration (usually found in ``.h`` files) and implementation
(usually found in ``.m`` files) are listed below.  Class declarations are easily
recognized as blocks of code between ``@interface`` and ``@end``, and similarly
the implementation is between ``@implementation`` and ``@end``.  An expression
enclosed in brackets in Objective-C is called a message, and is the equivalent
to an instance method invocation in Python.  For example, this Objective-C
code:

 .. sourcecode:: objective-c

    [aMutableArray addObject:@"constant string"];

Is equivalent in intent to the following in Python:

 .. sourcecode:: python

    aList.append(u"constant string")

Objective-C messages have three components: a target, a selector, and zero or
more arguments.  The target, ``aMutableArray``, is the object or class
receiving the message.  The selector, ``addObject:`` uniquely identifies the
kind of message that is being sent.  Finally, the arguments,
``@"constant string"`` are used by the implementation of the method upon
receipt of the message.  The syntax of Objective-C message dispatch is
deceptively similar to keyword arguments in Python, but they are actually
quite different.  Objective-C messages can not have default arguments, and all
arguments are passed in a specific order.  The components of a selector may not
be reordered.  Syntactically, one argument must be interleaved at every colon in
the selector.  The message:

 .. sourcecode:: objective-c

    [anArray indexOfObject:someObject inRange:someRange]
    
Target:
    ``anArray``

Selector:
    ``indexOfObject:inRange:``
    
Arguments:
    ``someObject``, ``someRange``

As documented later, the straightforward translation of such a message to
Python is:

 .. sourcecode:: python

    anArray.indexOfObject_inRange_(someObject, someRange)
    
This may be awkward and "unpythonic" at first, however this syntax is necessary
to preserve the semantics of Objective-C message dispatch.

A class declaration:

 .. sourcecode:: objective-c
    :linenos:

    @interface MyClass : MySuperClass
    {
        id  anInstanceVariable;
        int anotherInstanceVariable;
    }

    // A class method that returns an initialized instance of this class.
    // Similar to an implementation of __call__ on the metaclass.
    +instanceWithObject:(id)anObject andInteger:(int)anInteger;

    // An instance method, the designated initializer for MyClass.
    // Similar to an implementation of __new__ on MyClass.
    -initWithObject:(id)anObject andInteger:(int)anInteger;

    // An accessor, instance variables (attributes) are in a separate
    // namespace and are considered "private" in Objective-C.  Conventionally,
    // there is nothing similar to this in Python.
    -(int)anotherInstanceVariable;
    @end

A class implementation:

 .. sourcecode:: objective-c
    :linenos:

    @implementation MyClass

    // Note that a type is not declared for the return value.  Undeclared types
    // are assumed to be "id", which means any kind of instance.
    +instanceWithObject:(id)anObject andInteger:(int)anInteger
    {
        // 1. Create an instance of MyClass.
        // 2. Initialize it with its designated initializer
        //    "initWithObject:andInteger:".
        // 3. Autorelease it, so that it does not leak memory.
        // 4. Return the new instance.
        //
        // NOTE:
        //   By convention,initializers (such as +new, -init, -copy)
        //   are the only methods that should return retained objects.
        //
        // NOTE:
        //   Since this is a class method, "self" refers to the class!
        //
        // Very roughly similar to:
        //   return self.__new__(anObject, anInteger)
        return [[[self alloc] initWithObject:anObject andInteger:anInteger] autorelease];
    }

    // Note that a type is not declared for the return value.  Undeclared types
    // are assumed to be "id", which means any kind of instance.
    -initWithObject:(id)anObject andInteger:(int)anInteger
    {
        // Call the designated initializer of the superclass.
        // Similar to:
        //     self = super(MyClass, self).__new__()
        self = [super init];

        // Bail if initialization of the superclass failed.
        // Similar to:
        //     if self is None:
        //         return None
        if (!self) {
            return nil;
        }

        // Set the instance variable (attribute).  The argument must be
        // retained, since it will persist as long as the instance does.
        // Similar to:
        //     # Reference counting is automatic in Python
        //     self.anInstanceVariable = anObject
        anInstanceVariable = [anObject retain];

        // Set the other instance variable.  Note that since anInteger is
        // a primitive "C" type, not an object, no reference counting takes
        // place.
        // Similar to:
        //     # Everything is an object in Python
        //     self.anotherInstanceVariable = anInteger
        anotherInstanceVariable = anInteger;

        // Like __new__ in Python, initializers in Objective-C must
        // explicitly return self.  Note that this is different from
        // __init__.
        // Similar to:
        //     return self
        return self;
    }
        

    // an accessor, instance variables (attributes) are in a separate
    // namespace and are considered "private"
    -(int)anotherInstanceVariable
    {
        return anotherInstanceVariable;
    }

    // Since objects were retained as instance variables on this object,
    // they must be freed when the object is.  This is similar to an
    // implementation of __del__ in Python.  Since Objective-C has no
    // cyclic garbage collection, this isn't discouraged like it is in
    // Python.
    -(void)dealloc
    {
        // Very roughly similar to:
        //     del self.instanceVariable
        [instanceVariable release];

        // Very roughly similar to:
        //     super(MyClass, self).__del__()
        [super dealloc];
    }

    @end

Objective-C also features exceptions, but they are typically only used for
disaster recovery, not error handling, so you will not encounter them very
often.  Read `The Objective-C Programming Language`_ if you want to
know more about exceptions in Objective-C. 

One thing to keep in mind when translating Objective-C snippets to Python is
that any message can be sent to ``nil``, and the return value of that message
will be ``nil``.  PyObjC translates ``nil`` to ``None`` when crossing the
bridge, so any such attempt will raise an ``AttributeError``.

For more information about Objective-C see:

* `The Objective-C Programming Language`_ at `Apple`_.

.. _`The Objective-C Programming Language`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html

   The link is not correct, but the actual document is not online at the  moment.


Overview of the bridge
----------------------

Classes
.......

Objective-C classes are visible as (new-style) Python classes and can be 
subclassed just like normal Python classes.  All the usual introspection
mechanisms work as well, as do ``__slots__`` and descriptors.  The major 
differences between normal Python classes and Objective-C classes are the way 
that instances are created and initialized, and the fact that Objective-C
selectors look strange when translated to Python methods.

Multiple inheritance may be used when subclassing an Objective-C class, so
long as the Objective-C class is the first base class and there is only one
Objective-C base class.  The Objective-C runtime does not support multiple
inheritance.  These mix-in classes should not contain different
implementations for Objective-C methods.  To achieve this behavior, Categories
should be used instead.

Another thing to keep in mind is that the names of Objective-C classes must
be globally unique per process, including across Python modules.  That is,
it is *not* possible to have two Python modules that define a class with the
same name.  It is conventional to choose class names with a short prefix that
uniquely identify your project or company.  For example, Apple uses ``NS``
as the prefix for all classes in the `Cocoa libraries`_.  Note that the ``NS``
prefix made much more sense when it was called NeXTstep, but persists to this
day for compatibility reasons.

As described in `Objective-C for PyObjC users`_ the creation of Objective-C 
objects is a two-stage process.  To initialize objects, first call a
class method to allocate the memory (typically ``alloc``), and then call an
initializer (typically starts with ``init``).  Some classes have class methods
which perform this behind the scenes, especially classes that create cached,
immutable, or singleton instances.

Messages and Functions
......................

Objective-C methods are bridged to Python methods.  Because Objective-C
message dispatch syntax can not be translated directly to Python, a few
simple translations must take place.  The rules for these translations are:

1. Replace all colons in the selector with underscores:
  
    - ``someMethod:withFoo:andBar:`` translates to ``someMethod_withFoo_andBar_``

2. If the result ``class`` or ``raise`` (Python keywords), append two underscores:
  
    - ``class`` translates to ``class__``
    - ``raise`` translates to ``raise__``

3. Use this translated selector as a normal Python method.
   The arguments must be passed in the same order, and the number of
   arguments passed will normally be equal to the number of underscores
   in the method name; exceptions to this rule and the behavior of "result"
   are mentioned below.

   .. sourcecode:: objective-c
      :linenos:

      result = [someObject someMethod:firstArg withFoo:foo andBar:bar];

   translates to

   .. sourcecode:: python
      :linenos:

      result = someObject.someMethod_withFoo_andBar_(firstArg, foo, bar)

Note that it is currently not possible to support methods with a variable
number of arguments from Python.  These selectors must be wrapped by
custom Objective-C code in order to be accessible by Python.

Wrapped/bridged methods (and functions) have the same number of arguments
as the corresponding Objective-C method or function, unless otherwise noted
in the documentation (:doc:`Notes on supported APIs and classes on Mac OS X </apinotes>` for
Cocoa on Mac OS X).

Most methods or functions that take or return pointers to values will be an
exception to this rule if it is callable from Python at all.  In Objective-C
terminology, there are three kinds of pointers that can be used in a method:

``in``:
    Used to pass data by reference to the function.  This is not a special
    case from Python.

    Instead of a regular value you may also pass in the value ``objc.NULL``, 
    when you do that the Objective-C method will receive a NULL pointer instead
    of a pointer to your value.

``out``:
    Used to pass data from the function (e.g. an additional return value).

    Pass in either ``None`` or ``objc.NULL`` for output arguments.
    to the method. If the value is ``objc.NULL`` the Objective-C code will
    receive a NULL pointer for this argument, otherwise it will receive a 
    valid pointer. 

``inout``:
    A combination of in and out (a value is passed by reference, and mutated
    upon return).  Unlike ``out``, these arguments remain in the argument list,
    and thus do not have an effect on the number of arguments a method expects.
    See below for notes on how ``inout`` arguments change the return value.

    Instead of a regular value you may also pass in the value ``objc.NULL``, 
    when you do that the Objective-C method will receive a NULL pointer instead
    of a pointer to your value.

In order to determine what the return value of such an exceptional message will
look like, you must "make a list" of the return values with the following rules:

1. If the return type of the method or function is not ``void``, add it to the
   list.

2. For each argument in the method or function, add it to the list if it is
   ``out`` or ``inout``. When ``objc.NULL`` was used as the argument value it
   will also be used as the result value.

After creating this list, you will have one of three cases:

Empty:
    The return value of this call will always be ``None``.

One element:
    The return value of this call will correspond to the one element of the list.

More than one element:
    The return value of this call will be a tuple in the same order as the list.
    
The rules for pass by reference arguments may look quite complicated, but
it turns out this is very straightforward when working with them.

As an example of a method with two output arguments, ``NSMatrix`` implements a
selector named ``getNumberOfRows:columns:`` with the following signature:


 .. sourcecode:: objective-c

   -(void)getNumberOfRows:(int *)rowCount columns:(int *)columnCount

This method is used from Python like this:

 .. sourcecode:: python

   rowCount, columnCount = matrix.getNumberOfRows_columns_(None, None)

When a function or method has an array of values and the length of that array
as arguments, ``None`` may be passed as the length to specify that the length
of the given sequence should be used.

Python's ``array.array`` type may be used to represent a C array if the
typestr and size match what is expected by the selector.  Numeric, numarray,
and other third party array types are not supported at the moment.

When defining methods in an Objective-C subclass, the bridge must provide
type signatures for each method to the Objective-C runtime.  The default
type signature is for all arguments as well as the return value to be objects (just
like with normal Python methods).  If there is no return statement in the implementation,
then the return value will be void.  The bridge will automatically pick a better 
signature when it has more information available.  Specifically, a method overrides 
an existing method, the bridge will assume you want to use the same
method signature.  Furthermore, if the method is implemented in an (informal)
protocol known to the bridge it will use the signature from the corresponding
method in that signature.

The end result is that it is rarely necessary to explicitly add information about
the signature of methods.  For the two most common cases where this is necessary,
we have provided convenience decorators (used like ``staticmethod`` or
``classmethod``):

``objc.accessor``:
    Use this to wrap a `Key-Value Coding`_ or `Key-Value Observing`_ compliant
    accessor.

``PyObjCTools.AppHelper.endSheetMethod``:
    Use this to wrap the implementation of a sheet's "didEndSelector" callback.

For complete control of the mapping to Objective-C you can use the function
``objc.selector`` to create custom descriptors.  See the documentation of the
``objc`` module for the arguments you can use with this function.  It is
normally used like this:

 .. sourcecode:: python
    :linenos:

	class MyObject(NSObject):

		# -(void)someMethod:(float)arg
		def someMethod_(self, arg):
			pass

		someMethod_ = objc.selector(someMethod_, signature='v@:f')

In Python 2.4 or later there is a decorator for this purpose:

 .. sourcecode:: python
    :linenos:

	class MyObject(NSObject):

		@objc.signature('v@:f')
		def someMethod_(self, arg):
			pass


Reference counting
..................

The Cocoa libraries, and most (if not all) other class libraries for 
Objective-C use explicit reference counting to manage memory.  The methods
``retain``, ``release`` and ``autorelease`` are used to manage these 
reference counts.  You won't have to manage reference counts in Python, the
bridge does all that work for you (but see :doc:`Notes on supported APIs and classes 
on Mac OS X </apinotes>` for some advanced issues).

The only reasons reference counts are mentioned at all are to tell you about
ignoring them, and more importantly to introduce you to some issues w.r.t. 
reference counting.

It turns out that Cocoa uses a primitive form of :mod:`weak references <weakref>`.  Those 
are not true :mod:`weak references <weakref>` as in Python, but use-cases where an object 
stores a reference to another object without increasing the reference count
for that other object.  The bridge cannot solve the issues this introduces
for you, which means that you get hard crashes when you're not careful when
dealing with those :mod:`weak references <weakref>`.

The basic rule to deal with weak references is: make sure objects stays
alive as long as someone might have a weak reference to them.  Due to the way
the bridge works, this means that you must make sure that you don't create
weak references from Objective-C to a plain Python object.  The Python
object stays alive, but the proxy object as seen by the Objective-C code is
actually an autoreleased object that will be cleaned up unless the Objective-C
code increases its reference count.

The document :doc:`Notes on supported APIs and classes on Mac OS X </apinotes>` contains 
information about classes that work with weak references.  The most important
are notification centers and ``NSOutlineView``, to be exact: the outline view
stores weak references to the objects return by the method 
``outlineView:child:ofItem:`` of its data source.  The easiest way to avoid
crashes with outline views is to make sure that you model for the view uses
subclasses of ``NSObject`` to represent the nodes in the outline view.

Another gotcha is that ``obj.setDelegate_()`` often does *not* retain the
delegate, so a reference should be maintained elsewhere.

Protocols
.........

Cocoa defines a number of formal and informal protocols that specify methods
that should be implemented by a class if it is to be used in a specific role,
such as the data source for an ``NSTableView``.

Those protocols are represented by instances of ``objc.informal_protocol``,
and ``objc.formal_protocol``.  The only ones that have to care about these
objects are the maintainers of wrappers around Objective-C frameworks: they
have to keep these protocol wrappers up-to-date.

PyObjC will automatically use the information in the ``informal_protocol`` 
objects to add the right method signatures to methods, and to warn about
classes that partially implement a protocol.

See :doc:`PyObjC protocol support <protocols>` for more information.

Cocoa Bindings
..............

In Mac OS X 10.3 Apple introduced `Cocoa Bindings`_, a method to make it easier
to create and use *Controller* objects using `Key-Value Observing`_ and
`Key-Value Coding`_.  In order to create accessors compatible with this, you
must use ``objc.accessor`` to create an appropriate selector descriptor.

PyObjC automaticly emits the right `Key-Value Observing`_ notifications when 
you set attributes on an Objective-C class. This is however not supported for
pure python objects. You should therefore use ``NSMutableArray`` instances 
instead of Python lists for instance variables that will be observed and contain
a sequence of values (and simularly for ``NSMutableDictionary`` instead of
``dict``).

.. _`Cocoa Bindings`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html
.. _`Key-Value Coding`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/KeyValueCoding/Articles/KeyValueCoding.html
.. _`Key-Value Observing`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html

NOTE: Key-Value Observing is not supported for "pure" python objects, that
is instances of classes that don't inherit from ``NSObject``. Adding such 
support is not possible adding a KVO-like interface to the Python interpreter.

Categories
..........

Objective-C has a mechanism for modularize a class definition, it is possible
to add methods to an existing class in a separate compilation unit and even
a separate library.  This mechanism is named categories and is used to enhance
existing classes, for splitting classes in several parts and to document
informal protocols.

An example of a category definition:

 .. sourcecode:: objective-c
    :linenos:

	@interface NSObject (MyCategory)
	- (NSSize)objectFootprint;
	@end

This declares an additional category on ``NSObject``.  This category contains
a single method.

The function ``objc.classAddMethods`` can be used to get the same effect in
Python:

 .. sourcecode:: python
    :linenos:

	def objectFootprint(self):
		pass

	objc.classAddMethods(NSObject, [objectFootprint])

This is not very clear, PyObjC therefore also provides the following 
mechanism, implemented on top of ``objc.classAddMethods``:

 .. sourcecode:: python
    :linenos:

	class NSObject(objc.Category(NSObject)):
		def objectFootprint(self):
			pass

To make it clear that ``objc.Category`` performs a special task the name in
the class definition must be the same as the ``__name__`` of the argument
to ``objc.Category``.

Accessing Python objects from Objective-C
-----------------------------------------

All Python objects can be accessed from Objective-C through proxy objects.
Whenever a Python object crosses the line from Python to Objective-C a proxy
object is created (of class ``OC_PythonObject``, a subclass of ``NSProxy``).
This proxy object will forward all method calls from Objective-C to Python, and
will return the results back to Objective-C.

See the section 'Method protocol' for a description of how PyObjC translates
between Python and Objective-C method calls.

A number of Python types/classes are treated specially:

- Python numbers (``int``, ``float``, ``long``) are translated into
  ``NSNumber`` instances.  Their identity is not preserved across the bridge.

- Python ``str`` is proxied using ``OC_PythonString``, a subclass of
  ``NSString``.  A Python ``str`` may be used anywhere a ``NSString`` is
  expected, but ``unicode`` should be used whenever possible.
  ``OC_PythonString`` will use the default encoding of ``NSString``, which is
  normally MacRoman but could be something else.

- Python ``unicode`` is proxied using ``OC_PythonUnicode``, a subclass of
  ``NSString``.  A Python ``unicode`` may be used anywhere a ``NSString``
  is expected.

- Python ``dict`` is proxied using ``OC_PythonDictionary``, a subclass of
  ``NSMutableDictionary``.  A Python ``dict`` may be used anywhere
  an ``NSDictionary`` is expected.

- Python ``list`` and ``tuple`` are proxied using ``OC_PythonArray``, a
  subclass of ``NSMutableArray``.  Python ``list`` or ``tuple`` objects
  may be used anywhere an ``NSArray`` is expected.

- Python objects that implement the Python buffer API, except for ``str``
  and ``unicode``, are proxied using ``OC_PythonData``, a ``NSData`` subclass.
  Objects that implement the Python buffer API such as ``buffer``,
  ``array.array``, ``mmap.mmap``, etc. may be used anywhere a ``NSData`` is
  expected.

These special cases allow for more transparent bridging between Python and
Objective-C.

Cocoa for Python programmers
----------------------------

Cocoa frameworks are mapped onto Python packages with the same name; that is
the classes, constants and functions from the AppKit framework are available
after you import ``AppKit`` in your Python script. 

These helper modules contain *only* functions, constants and classes that 
wrap items in the corresponding framework.  All utility functions and classes 
are located in the ``PyObjCTools`` package and ``objc`` module.  Note that it
is possible to use ``pydoc`` (or the ``help()``) function with the framework
wrappers, but that this is not very useful for the entire module due to the
size of these modules.

This makes it easier to find documentation for an item: if you import it 
from the wrapper module for an Objective-C framework the documentation for
that item can be found in the documentation for the framework; otherwise the
item is documented in the PyObjC documentation.

The module ``PyObjCTools.NibClassBuilder`` can be used to make working with 
NIB files more convenient.  This module can be used to extract information 
about classes from NIB files, both as a standalone tool generating source code 
and during runtime.  See the online documentation for this module for more
information.

PyObjC includes a number of examples that show how to use Cocoa from
Python.  The :doc:`PyObjC Example index </examples/index>` contains an overview of those examples.

More information on Cocoa programming can be found at:

* `Cocoa documentation at the Apple developer website`_

* `Cocoa examples at the Apple developer website`_

* Your local bookstore or library

.. :doc:`PyObjC Example index </examples/index>`:

..  _`Cocoa libraries`: https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/CocoaFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002974

..  _`Cocoa documentation at the Apple developer website`: https://developer.apple.com/library/mac/navigation/index.html#section=Frameworks&topic=Cocoa%20Layer

.. _`Cocoa examples at the Apple developer website`: https://developer.apple.com/library/mac/navigation/index.html#section=Resource%20Types&topic=Sample%20Code

Notes on specific tasks
-----------------------

Working with threads
....................

Most of Cocoa, and thus PyObjC, requires an ``NSAutoreleasePool`` in order to function
properly.  PyObjC does this automatically on the first thread it is imported from,
but other threads will require explicit ``NSAutoreleasePool`` management.  The following
practice for working with ``NSAutoreleasePool`` is recommended:

 .. sourcecode:: python
    :linenos:

	pool = NSAutoreleasePool.alloc().init()
	...
	del pool

Typically this will be done at the beginning and end of the thread.  It is important
to use ``del`` before rebinding the ``pool`` local to another ``NSAutoreleasePool``
instance, otherwise it will not have the intended effect.

For long running threads and tight loops, it can also be useful to use this pattern
in the body of the loop in order to optimize memory usage.  For example, ``NSRunLoop``
will be create a new ``NSAutoreleasePool`` at the beginning of each run loop iteration
and release it at the end.

Finalizers
..........

In normal Python, there are two methods for writing finalizers: implementing
``__del__``, and using ``weakref.ref`` callbacks.  Generally, ``__del___`` is
discouraged as it does not allow the object to participate in cyclic garbage
collection and create uncollectible garbage if not implemented properly.
``weakref.ref`` callbacks avoid this restriction as they do not provide a real
reference to the object.

In Objective-C, there is no cyclic garbage collection, so all Objective-C
objects (including subclasses from Python) are already subject to these
restrictions.  When subclassing an Objective-C class, you may implement
``dealloc`` or ``__del__``.  If you implement ``dealloc``, ensure that
you call the super ``dealloc`` at the end.  If you implement both 
``__del__`` and ``dealloc``, the order in which they are called is
undefined.

It is not currently possible to create a ``weakref.ref`` for any Objective-C
object.  It is probably technically possible to do, but tricky, so it
may eventually be implemented in a future version of PyObjC (especially
if a future Objective-C runtime supports it).

Copying
.......

It is possible for a Python subclass of an Objective-C class to implement
the ``NSCopying`` protocol.  Some care must be taken when the superclass
already implements the protocol. 

Some ``NSCopying`` compliant Objective-C classes copy the template object
manually.  In those cases the Python subclass must also copy the additional
ivars manually.

Other ``NSCopying`` compliant Objective-C classes use a convenience function
that creates a shallow copy of the object and all of its ivars.  In those
cases the Python subclass will not have to explicitly copy all of the ivars.
However, the ivars in the copy will refer to the same objects as the original,
and will thus share some state.  As with shallow copies in Python, if any of
the ivars refer to mutable objects (``list``, ``dict``, etc.) it may be
desirable to explicitly make shallow or deep copies of the mutable ivars.

NOTE: PyObjC might introduce a helper class when you inherit from a class
that implements ``NSCopying`` as an internal implementation detail.
External code should not rely on the existance of this class.

NOTE2: ``SomeClass.copyWithZone_`` should not be implemented unless a
superclass already implements ``copyWithZone:``, or else the behavior
will be undefined (memory corruption, crashes, etc.).

Building applications
---------------------

There are two different recommended ways to build applications with PyObjC.

"py2app" :  setup.py
....................

The PyObjC installer includes a copy of the ``py2app`` package.  This package
offers a way to build distutils scripts for building (standalone)
applications and plugin bundles.

An example ``setup.py`` script:

 .. sourcecode:: python
    :linenos:

    from distutils.core import setup
    import py2app

    setup(
        app = ["iClass.py"],
        data_files = ["English.lproj"],
    )
	
During development you typically invoke it from the command line like this:

 .. sourcecode:: sh

     $ python setup.py py2app -A

This will build an application bundle in a folder named ``dist`` in the
current folder. The ``-A`` option tells ``py2app`` to add symbolic
links for data folders and files and an Alias to your main script,
allowing you quickly rebuild the application without doing a full dependency
scan, with the additional bonus that you can edit them without rebuild. To
build a standalone application, simply do not use the ``-A`` option.
Note that if you are using a version of Python shipped with your operating
system, it will not be included in the application.  Otherwise, your
application will include stripped down version of the Python runtime that
you ran setup.py with.

For more information about ``py2app`` usage, read through some of the
``setup.py`` scripts used by the examples in the :doc:`Examples </examples/index>` folder.
On any ``setup.py`` script that imports ``py2app``, you can use the
following command to see the list of options:

 .. sourcecode:: sh

    $ python setup.py py2app --help



.. 
        This section is disabled for now because the Xcode templates aren't maintained.

        "IDE approach" : Xcode
        ......................

        PyObjC includes a number of Xcode templates that can be used to 
        develop applications, using the same underlying functionality that
        is in py2app.  These templates are used like any other Xcode template,
        but there are some organizational rules about the template.

        See `the documentation for the templates` for more details.

        .. Xcode-Templates.html
