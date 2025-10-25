:mod:`objc` -- The PyObjC bridge
================================

.. module:: objc
   :synopsis: The PyObjC bridge

Introduction
------------

The module :mod:`objc` is the core of PyObjC and provides the automatic
bridging between Python and Objective-C. It also provides a number of
utility functions and types that make it easier to integrate Python
and Objective-C code.

The module :mod:`objc` defines a number of functions whose names start with
an underscore. Those functions are private and should not be used, they can
be removed from release without warning.

Bridge options
..............

.. data:: options

   Attributes of this object contain configuration settings for the bridge.

   Attributes whose names start with an underscore are private
   and can appear or disappear with every release of PyObjC.

   .. versionadded:: 3.0


   .. attribute:: verbose
      :type: bool

      When the value is :const:`True` the bridge will log more information.

      This currently results in output on the standard error stream whenever
      an exception is translated from Python to Objective-C.

   .. attribute:: use_kvo
      :type: bool

      The default value for the *__useKVO__* attribute on
      classes.

      When the *__useKVO__* attribute of a class is true instances
      of the class will generate Key-Value Observation notifications when
      setting attributes from Python.

   .. attribute:: unknown_pointer_raises
      :type: bool

      When True (the default) the bridge will raise an exception when
      it encounters a pointer value that cannot be converted to Python,
      otherwise it it creates instances of :class:`ObjCPointer`.

   .. attribute:: deprecation_warnings
      :type: str | None

      When ``"0.0"`` (the default) the bridge will not emit deprecation warnings,
      otherwise the value should be a platform version in the form
      of a string (e.g. ``"10.15"``)
      and the bridge will emit a deprecation warning for APIs
      that were deprecated in the SDK (or earlier).

      Set to :data:`None` or ``"0.0"`` to disable warnings.

      Deprecation warnings are emitted using the :mod:`warnings` module,
      using the warning :class:`objc.ApiDeprecationWarning`.

      .. versionadded:: 3.3

      .. versionchanged:: 10.0

         The value for this option is now a string instead of an integer.

   .. attribute:: structs_indexable
      :type: bool

      When True (the default) PyObjC's wrappers for C structs can be indexed
      as if they are (writable) tuples. When False this isn't possible.

      .. note:: This is primarily an experimental option.

   .. attribute:: structs_writable
      :type: bool

      When True (the default) PyObjC's wrappers for C structs are writable,
      otherwise they are read-only.

     .. note:: This is an experimental option.


Deprecated functions for changing options
.........................................

.. function:: setVerbose(yesOrNo)

   :param bool yesOrNo: Whether or not to enable verbose mode.

   When the argument is :const:`True` the bridge will log more information.

   This currently results in output on the standard error stream whenever
   an exception is translated from Python to Objective-C.

   .. deprecated:: 3.0 Use :data:`objc.options` instead


.. function:: getVerbose()

   :return: Current value of the verbose flag.
   :rtype: bool

   .. deprecated:: 3.0 Use :data:`objc.options` instead


.. function:: setUseKVOForSetattr(yesOrNo)

   :param bool yesOrNo: Default value for the *__useKVO__* attribute of classes defined after this call.
   :return: The previous value
   :rtype: bool

   Sets the default value for the *__useKVO__* attribute on
   classes defined after this call. Returns the previous value.

   .. deprecated:: 3.0 Use :data:`objc.options` instead

.. function:: getUseKVOForSetattr()

   :return: The default value for the *__useKVO__* attribute on classes.
   :rtype: bool

   .. deprecated:: 3.0 Use :data:`objc.options` instead

Weak references
---------------

.. class:: WeakRef(object)
   :final:

   :param objc.objc_object object: Value to create a weak reference to.

   This class creates weak references to an Objective-C value. The reference
   is cleared when the last reference to the native Objective-C value is
   released, even when that reference is an Objective-C reference.

   Instances of this class behave similar to ``__weak`` variables in Objective-C.

   The *object* must be a Cocoa object, and must not be a CoreFoundation
   object (unless the CoreFoundation type is transparently bridged to Cocoa).

   .. versionadded: 3.0

   .. method:: __call__()

      :return: The weakly references object when that is still alive, or :data:`None`.

    .. warning::

       Some Cocoa classes do not support weak references, see Apple's
       documentation for more information. Creating a weak reference
       to instances of such classes can be a hard error (that is,
       the interpreter crashes, you won't get a nice exception).

Associated Objects
------------------

On macOS 10.6 or later the Objective-C runtime has an API for
associated objects, which are more or less additional instance variables
for objects.

.. function:: setAssociatedObject(object, key, value, policy)

   :param objc.objc_object object object: the base object (a Cocoa instance)
   :param object key: an arbitrary object, the same object must be used to
               retrieve the value.
   :param object value: value for the associated object
   :param int policy: policy for the association (see below)

   Associate *assoc* with *object* under name *name*.

.. function:: getAssociatedObject(object, key)

   :param objc.objc_object object: an object (a Cocoa instance)
   :param object key: the key object that was used with :func:`setAssociatedObject`
   :return: the value for the key, or :data:`None`.

.. function:: removeAssociatedObjects(object)

   :param objc.objc_object object: an object (a Cocoa instance)

   Remove all associations for *object*. It is generally a bad idea to
   use this function, because other libraries might have set associations
   as well.

.. data:: OBJC_ASSOCIATION_ASSIGN
   :type: int

   Policy for creating a weak reference to the associated object

   .. note:: Don't use this when the value is a pure python object, unless
             you arrange to keep the proxy object alive some other way.

.. data:: OBJC_ASSOCIATION_RETAIN_NONATOMIC
   :type: int

   Policy for creating a strong reference to the associated object.

.. data:: OBJC_ASSOCIATION_COPY_NONATOMIC
   :type: int

   Policy for creating a strong reference to a copy of the associated object.

.. data:: OBJC_ASSOCIATION_RETAIN
   :type: int

   Policy for creating a strong reference to the associated object, the
   association is made atomically.

.. data:: OBJC_ASSOCIATION_COPY
   :type: int

   Policy for creating a strong reference to a copy of the associated object,
   the association is made atomically.

Utilities
---------

.. function:: macos_available(major, minor=0, patch=0)

   :param int major: Major version
   :param int minor: Minor version
   :param int patch: Patch level
   :return: True iff the current macOS version is at least the version
            specified. Use this like the "@available" construct in Objective-C.
   :rtype: bool


   .. versionchanged:: 10.4

      There is now a default for *minor*.

.. function:: allocateBuffer(length)

   :param int length: Length of the buffer
   :return: A writable buffer object of *length* bytes.
   :rtype: bytearray

   .. deprecated:: 8.2 Use :class:`bytearray` instead

Accessing classes and protocols
-------------------------------

.. function:: lookUpClass(classname)

   :param classname: the name of an Objective-C class
   :type classname: str
   :return: the named Objective-C class
   :rtype: objc.objc_class
   :raises objc.nosuchclass_error: when the class does not exist


.. function:: getClassList(ignore_invalid_identifiers=True)

   :param bool ignore_invalid_identifiers: If true the result only contains
                                           classes whose name is a valid Python
                                           identifier.
   :return: a list of a classes known to the Objective-C runtime
   :rtype: list[objc.objc_class]


   .. versionchanged: 10.0

      Added the *ignore_invalid_identifiers* argument.

.. function:: protocolsForClass(cls)

   :param objc.objc_class cls: The class to introspect
   :return: A list of protocols the class claims to implement directly.
   :rtype: list[objc.formal_protocol]

.. function:: protocolsForProcess

   Introspect the formal protocols known to the Objective-C runtime.

   :return: A list of all protocols known to the Objective-C runtime.
   :rtype: list[objc.formal_protocol]

.. function:: propertiesForClass(objcClass)

   :param objc.objc_class|objc.formal_protocol objcClass: an Objective-C class or formal protocol
   :return: a list of properties from the Objective-C runtime
   :rtype: list[dict]

   The return value is a list with information about
   properties on this class or protocol from the Objective-C runtime. This
   does not include properties defined in superclasses.

   Every entry in the list is dictionary with the following keys:

   =========== ============== ===================================================
   Key           Type          Description
   =========== ============== ===================================================
   name        :class:`str`   Name of the property
   ----------- -------------- ---------------------------------------------------
   raw_attr    :class:`bytes` Raw value of the attribute string
   ----------- -------------- ---------------------------------------------------
   typestr     :class:`bytes` The type string for this attribute
   ----------- -------------- ---------------------------------------------------
   classname   :class:`str`   When the type string is ``objc._C_ID`` this is the
                              name of the Objective-C class.
   ----------- -------------- ---------------------------------------------------
   readonly    :class:`bool`  True iff the property is read-only.
   ----------- -------------- ---------------------------------------------------
   copy        :class:`bool`  True iff the property is copying the value.
   ----------- -------------- ---------------------------------------------------
   retain      :class:`bool`  True iff the property is retaining the value.
   ----------- -------------- ---------------------------------------------------
   nonatomic   :class:`bool`  True iff the property is not atomic.
   ----------- -------------- ---------------------------------------------------
   dynamic     :class:`bool`  True iff the property is dynamic.
   ----------- -------------- ---------------------------------------------------
   weak        :class:`bool`  True iff the property is weak.
   ----------- -------------- ---------------------------------------------------
   collectable :class:`bool`  True iff the property is collectable.
   ----------- -------------- ---------------------------------------------------
   getter      :class:`bytes` Non-standard selector for the getter method.
   ----------- -------------- ---------------------------------------------------
   setter      :class:`bytes` Non-standard selector for the setter method.
   =========== ============== ===================================================

   All values but *name* and *raw_attr* are optional. The other attributes
   contain a decoded version of the *raw_attr* value. The boolean attributes
   should be interpreted as :data:`False` when the aren't present.

   The documentation for the Objective-C runtime contains more information about
   property definitions.

   This function only returns information about properties as they are defined
   in the Objective-C runtime, that is using ``@property`` definitions in an
   Objective-C interface. Not all properties as they are commonly used  in
   Objective-C are defined using that syntax, especially properties in classes
   that were introduced before macOS 10.5.

   .. versionadded:: 2.3

.. function:: listInstanceVariables(classOrInstance)

   :param classOrInstance: The class or instance to introspect, must be a subclass
                           of :class:`NSObject` or an instance of such a class.
   :type classOrInstance: objc.objc_object | objc.objc_class
   :returns: A list of information about all instance variables for
             a class or instance.

             The elements of the list are tuples with two elements: a string with
             the name of the instance variable and a byte string with the type encoding
             of the instance variable.

.. function:: getInstanceVariable(object, name)

   :param classOrInstance: The class or instance to introspect, must be a subclass
                           of :class:`NSObject` or an instance of such a class.
   :type classOrInstance: objc.objc_object | objc.objc_class
   :param str name: Name of the attribute.
   :returns: The value of the instance variable *name*.

   .. warning::

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.

.. function:: setInstanceVariable(object, name, value[ ,updateRefCounts])

   :param classOrInstance: The class or instance to introspect, must be a subclass
                           of :class:`NSObject` or an instance of such a class.
   :type classOrInstance: objc.objc_object | objc.objc_class
   :param str name: Name of the attribute.
   :param value: The new value for the attribute
   :param bool updateRefCounts: If true the ``retainCount`` of the old an new value or updated.
                                Must be specified when the instance variable is an object.

   .. warning::

      Direct access of instance variables should only be used as a debugging
      tool and could negatively affect the invariants that a class tries to
      maintain.

   .. warning::

      It is very easy to introduce memory corruption when  *updateRefCounts* is false.
      In particular the caller of this method must ensure that the Objective-C
      representation of *value* is kept alive, when *value* is not a Cocoa object
      just keeping *value* alive isn't good enough.

.. function:: protocolNamed(name)

   :param str name: Name of a protocol
   :returns: The protocol object for the named protocol.
   :rtype: objc.formal_protocol
   :raises ProtocolError: The protocol doesn't exist.


   This is the equivalent of ``@protocol(name)`` in Objective-C.

.. exception:: ProtocolError

   Raised by :func:`protocolNamed` when looking up a protocol that does not
   exist.


Dynamic modification of classes
-------------------------------

.. function:: classAddMethods(cls, methods)

   Add a sequence of methods to the given class.

   :param objc_class cls: The class to update
   :param list[typing.Callable] methods: Sequence of methods to add to *cls*.

                                  The objects in *methods* should be one of:

                                  * :class:`selector` instances with a callable
                                    (that is, the first argument to :class:`selector`
                                    must not be :data:`None`).

                                  * :func:`classmethod` or :func:`staticmethod`
                                    instances that wrap a function object.

                                  * functions

                                  * unbound methods

                                  * instances for :class:`objc_method`

                                  For the last two the method selector is calculated
                                  using the regular algorithm for this (e.g. as if
                                  ``selector(item)`` was called). The last two are
                                  instance methods by default, but automatically made
                                  class methods when the class (or a superclass) has a
                                  class method with the same selector.

.. function:: classAddMethod(cls, name, method)

   Adds function *method* as selector *name* to the given class. When *method*
   is a selector the signature and class-method-ness are copied from the selector.

   :param objc.objc_class cls: The class to update
   :param bytes name: The selector name
   :param typing.Callable method: The method implementation. The implementation should
                                  be a callable that's accepted as a selector implementation
                                  in class definitions.

   .. note::

      Adding a selector that's defined in Objective-C to another class will raise
      an exception.

.. class:: Category

   A helper class for adding a category to an existing Objecive-C class (subclass
   of :class:`NSObject`).

   Usage:

   .. sourcecode:: python

       class NSObject (Category(NSObject)):
          def method(self):
              pass

   The metaclass uses :func:`classAddMethods` to add the methods in the category
   body to the base class.

   The name of the class must be the same as the argument to :class:`Category`.

   This will only add new methods to existing Objective-C classes, it is in
   particular not possible to add new members/slots to existing classes.


Plugin bundles
--------------

.. function:: currentBundle()

   During module initialization this function returns an NSBundle object for
   the current bundle. This works for application as well as plug-ins created
   using `py2app <https://pypi.org/project/py2app/>`_.

   After module initialization use ``NSBundle.bundleForClass_(ClassInYourBundle)``
   to get the bundle.

Memory management
-----------------

PyObjC automatically manages Cocoa reference counts for you, the functions
in this section help in finetuning this behaviour.

.. function:: recycleAutoreleasePool()

   Flush the NSAutoreleasePool that PyObjC creates on import. Use this
   before entering the application main loop when you do a lot of work
   before starting the main loop.

.. function:: removeAutoreleasePool()

   Use this in plugin bundles to remove the release pool that PyObjC creates
   on import. In plugins this pool will interact in unwanted ways with the
   embedding application.

.. function:: autorelease_pool()

   A context manager that runs the body of the block with a fresh autorelease
   pool. The actual release pool is not accessible.

   Usage::

        with autorelease_pool():
            pass

   This context manager is used to control when autoreleased values are
   released, and is mostly useful when accessing or calculating many values
   without reentering a run loop.

Test support
------------

The functions in this section are present as support code for PyObjC's
unittests and are not part of the stable API. Please let us know if you
use these functions in your code.

.. function:: splitSignature(typestring)

   Split an encoded Objective-C signature string into the
   encoding strings for separate types.

   :param bytes typestring: an encoded method signature
   :return: list of type signatures
   :rtype: list[bytes]


.. function:: splitStructSignature(typestring)

   :param bytes typestr: and encoded signature for a struct
   :return: ``(structname, fields)``. *Structname* is a string or :data:`None` and
            *fields* is a list of (name, typestr) values. The *name* is a string or
            :data:`None` and the *typestr* is a byte string.
   :rtype: tuple[str|None, list[tuple[str|None, bytes]]]
   :raise ValueError: The *typestring* is not the encoding of a C struct

.. function:: repythonify(object, type=b"@")

   Convert *object* to an Objective-C value and back to Python.

   :param object: Value to pass to the bridge
   :param bytes type: The C type that should be used as the intermediate.
   :return: The value of *object* after converting it to Objective-C and
            back again into Python.


Framework wrappers
------------------

.. function:: pyobjc_id(obj)

   Equivalent to :func:`id` for the Objective-C object proxied by PyObjC.

   :param objc.objc_object obj: Value to query
   :return: The ``NSObject*`` value for *obj* as an integer
   :rtype: int


Types
-----

.. class:: objc_class

   This class is the metatype for Objective-C classes and provides no user-visible
   behavior.

.. class:: objc_object(*, cobject=None, c_void_p=None)

   This class is the root class for Objective-C classes, that is all wrappers for
   Objective-C classes are a subclass of this class. It is not possible to instantiate
   instances of Objective-C classes by using the class as a callable, instances are
   created using the standard Objective-C mechanisms instead.

   The *cobject* and *c_void_p* arguments should always be passed as keyword arguments,
   and at most one of them should be provided. This will construct a proxy object of the
   right subclass of :class:`objc_object` for the Cocoa object that the passed in value
   refers to. *Cobject* should be a Python capsule created using the :meth:`__cobject__`
   method, *c_void_p* should be a :class:`ctypes.c_void_p`.

   .. attribute:: pyobjc_ISA
      :type: objc.objc_class

      Read-only property with the current Objective-C classes of an object. The value
      ``value.pyobjc_ISA`` is the same as ``type(value)``.

      .. deprecated:: 11.1 Use ``type(value)`` instead.

   .. attribute:: pyobjc_instanceMethods


      Read-only property that provides explicit access to just the instance methods
      of an object.

   .. attribute:: __block_signature__

      Property with the type signature for calling a block, or :data:`None`.

   .. attribute:: __hasdict__

      True if instances of this class have a ``__dict__`` and false otherwise.

   .. method:: __cobject__()

      Returns a capsule object with identifier "objc.__object__" and the a reference
      to the Objective-C object as the value.

   .. method:: __c_void_p__()

      Returns a :class:`ctypes.c_void_p` instance for this object.

   .. method:: __reduce__()

      Raises :exc:`TypeError`. This ensures that Objective-C objects cannot used
      with :mod:`pickle` (because the Cocoa and Python serialization protocols are
      not compatible).

   .. method:: __class_getitem__(*args)
      :classmethod:

      Return an object representing the specialization of a generic class by type arguments found in key.

   .. note::

      The wrapper classes for the :class:`NSString` class cluster aren't subclasses
      of :class:`objc_object`, but are subclasses of the builtin :class:`str` type.

.. class:: pyobjc_unicode

   This class is used to wrap instances of the :class:`NSString` class cluster and is
   a subclass of :class:`str`.

   Methods of the underlying :class:`NSString` class can be accessed at as methods
   of the python type, unless they have the same name as a method of the built-in Unicode
   type.

   .. method:: nsstring

      Returns an instance of a subclass of :class:`objc_object` that represents the
      string. This provides full access to the Cocoa string API, but without easy
      interoperability with Python APIs.

   .. note::

      Instances of *NSString* can be mutable. Mutations to mutable Cocoa
      strings are not reflected in instances of :class:`pyobjc_unicode`, use
      :meth:`nsstring` and explicit conversion to the built-in :class:`str` type when
      you work with mutable *NSString* values.

   .. note::

      Cocoa strings are wrapped using a subclass of the built-in :class:`str` type
      to get better interaction between Python and Cocoa. Because Cocoa strings are
      instances of the built-in :class:`str` type they can be passed to functions in
      extension modules that expect string arguments (in particular the file
      system access APIs such as :func:`open`).


.. class:: selector(function[, selector[, signature[, isClassMethod[, returnType[, argumentTypes[, isRequired]]]]]])

   This type is used to represent an Objective-C method.

   :param function:  The Python callable that is used for the method. Can be a :class:`classmethod` , but not a :class:`staticmethod`.
   :param selector:  The Objective-C selector for the method. The default is calculated from the \__name__ attribute for *function*
   :param signature: The type encoding for the method, the default signature assumes that all arguments and the result are objects
                     (or 'void' when the function does not contain a return statement with a value).
   :param isClassMethod: Used to specify if a method is a class method (default is :data:`True` if *function* is a :class:`classmethod`
                     and :data:`False` otherwise)
   :param isRequired:    Specify if the method is required (defaults to :data:`True`), used in the definition of protocols.

   .. attribute:: callable

      Read-only property with access to the underlying callable (the *function* argument to the constructor).

   .. attribute:: __doc__

      Documentation string for the selector

   .. attribute:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0


   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.

   .. attribute:: isHidden

      True when the selector is hidden, and false otherwise.

   .. attribute:: isRequired

      True when the selector is required, and false otherwise. Only used for
      conformance checking in protocols.

   .. attribute:: isClassMethod

      True when the selector is a class method, and false otherwise.

   .. attribute:: definingClass

      The class that defines this selector.


    .. attribute:: __objclass__

       Alias for *definingClass*.

    .. attribute:: signature

       Byte string with the Objective-C signature for the selector.

    .. attribute:: native_signature

       Byte string with the Objective-C signature for the selector, without post processing
       or applying metadata.

    .. attribute:: self

       The *self* value for a bound selector.

    .. attribute:: selector

       Byte string with the Objective-C selector name.

.. class:: objc_method(callable, *, selector=None, signature=None, isclass=None)

   Use this as a decorator in a Cococa class definition to signal that the
   method should definitely be converted to on Objective-C selector, and optional
   set a non-default selector or signature, or signal that the method should or
   should-not be a class method.

   :param selector:  The Objective-C selector name (byte string)
   :param signature: The Obejctive-C method signature
   :param isclass:   If true the method is a class method, if false the
                     method is an instance method, if ``None`` use the
                     default algorithm.


   Usage:

   .. sourcecode:: python

      class MyClass(NSObject):
          @objc_method()
          def myAction_(self, sender):
              pass

          @objc_method(selector="buttonClicked:")
          def button_clicked(self, sender):
              pass


.. class:: python_method(callable)


   Use this as a decorator in a Cocoa class definition to avoid creating a
   selector object for a method.

   This is used to add "normal" python methods to a class that's inheriting
   from a Cocoa class and makes it possible to use normal Python idioms in
   the part of the class that does not have to interact with the Objective-C
   world.

   For example:


   .. sourcecode:: python

       class MyClass (NSObject):

          @python_method
          @classmethod
          def fromkeys(self, keys):
              pass

          @python_method
          def items(self):
              pass

   In this example class *MyClass* has a Python classmethod "fromkeys" and
   a normal method "items", neither of which are converted to a selector object
   and neither of which are registered with the Objective-C runtime.

   Instances of this type have an attribute named *callable* containing the wrapped
   callable, but are themselves not callable.

   .. versionadded:: 3.0

   .. versionadded: 9.1

      The decorator can now also be used with parenthesis while decorating:

      .. sourcecode:: python

           class MyClass (NSObject):

              @python_method()
              @classmethod
              def fromkeys(self, keys):
                  pass

   .. note::

      If you use multiple decorators the :class:`python_method` decorator should be
      the outermost decorator (that is, the first one in the list of decorators).

.. class:: ivar([name[, type[, isOutlet]]])

   Creates a descriptor for accessing an Objective-C instance variable. This should only
   be used in the definition of an Objective-C subclass, the bridge will use this information
   to create an instance variable with the same name on the Objective-C class itself.

   :param name: Name of the instance variable. The name defaults to the name the instance
                variable is bound to in a class definition.

   :param type: Type encoding for the instance variable. Defaults to :data:`_C_ID` (that is,
                an object)

   :param isOutlet: If :data:`True` the instance variable is used as an outlet, by default
                the instance variable is not an outlet.

   .. note::
      Sharing an ivar object between multiple class definitions is not supported.


   Instances of :class:`ivar` have a number of attributes that help with introspection:

   .. attribute:: __typestr__

      The type encoding of the Objective-C type of the variable. See
      :ref:`type-encodings` for more information.

   .. attribute:: __name__

      The Objective-C name of the variable

   .. attribute:: __isOutlet__

      True if the variable is an :func:`IBOutlet`, false otherwise.

   .. attribute:: __isSlot__

      True if the variable is a Python slot, false otherwise.


   The :class:`ivar` has convenience class methods for creating :class:`ivar` objects
   for specific C types:

   .. method:: bool([name])

      Create an instance variable that stores a value of C type ``bool``. See the
      class description for a description of the *name* argument.

   .. method:: char([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. In general it
      is better to use :meth:`char_text` or :meth:`char_int`.

   .. method:: int([name])

      Create an instance variable that stores a value of C type ``int``. See the
      class description for a description of the *name* argument.

   .. method:: short([name])

      Create an instance variable that stores a value of C type ``short``. See the
      class description for a description of the *name* argument.

   .. method:: long([name])

      Create an instance variable that stores a value of C type ``long``. See the
      class description for a description of the *name* argument.

   .. method:: long_long([name])

      Create an instance variable that stores a value of C type ``long long``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_char([name])

      Create an instance variable that stores a value of C type ``unsigned char``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_int([name])

      Create an instance variable that stores a value of C type ``unsigned int``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_short([name])

      Create an instance variable that stores a value of C type ``unsigned short``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_long([name])

      Create an instance variable that stores a value of C type ``unsigned long``. See the
      class description for a description of the *name* argument.

   .. method:: unsigned_long_long([name])

      Create an instance variable that stores a value of C type ``unsigned long long``. See the
      class description for a description of the *name* argument.

   .. method:: float([name])

      Create an instance variable that stores a value of C type ``float``. See the
      class description for a description of the *name* argument.

   .. method:: double([name])

      Create an instance variable that stores a value of C type ``double``. See the
      class description for a description of the *name* argument.

   .. method:: BOOL([name])

      Create an instance variable that stores a value of C type ``BOOL``. See the
      class description for a description of the *name* argument.

   .. method:: UniChar([name])

      Create an instance variable that stores a value of C type ``UniChar``. See the
      class description for a description of the *name* argument. Values are
      (unicode) strings of length 1.

   .. method:: char_text([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. Values are
      byte-strings of length 1.

   .. method:: char_int([name])

      Create an instance variable that stores a value of C type ``char``. See the
      class description for a description of the *name* argument. Values are
      integers in the range of a ``signed char`` in C.

   Framework bindings introduce new class methods for creating instance variables whose type
   is a particular C struct, as an example the Foundation bindings introduce a class method
   named ``NSRange`` with the same signature as the methods mentioned earlier.

   .. note::

      You cannot access these attributes  through an Objective-C instance, you have to access
      them through the class object. That's because :class:`ivar` is a data descriptor.

.. class:: informal_protocol(name, selector_list)

   This class is used to specify which methods are part of an informal protocol
   in Objective-C. Informal protocols are a documentation construct in Objective-C and
   as such are not present in the Objective-C runtime (as opposed to formal protocols).

   Informal protocols are used by the bridge to automatically update method signatures when
   a class appears to implement an informal protocol. This makes it possible the define
   a large subset of Cocoa functionality without manually setting method signatures.

   :param name: Name of the protocol
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. attribute:: __name__

      Read-only property with the protocol name

   .. attribute:: selectors

      Read-only property with the sequence of selectors for this protocol


.. class:: formal_protocol(name, supers, selector_list)

   This class is used to represent formal protocols in Python, and is comparabile with the
   "@protocol" construct in Objective-C.

   :param name:     The name of the protocol
   :param supers:   A list of protocols this protocol inherits from
   :param selector_list: A sequence of :class:`selector` instances, all of which should have no callable.

   .. warning::

      The protocols created by PyObjC are not compatible with NSXPCInterface because that
      class needs information ("extended method signature") that cannot be registered through
      the public API for the Objective-C runtime. See :doc:`../notes/using-nsxpcinterface` for
      more information.

   .. attribute:: __name__

      Read-only property with the name of the protocol

   .. attribute:: name

      Returns the name of the protocol

   .. attribute:: conformsTo_(proto)

      Returns :data:`True` if this protocol conforms to protocol *proto*, returns :data:`False` otherwise.

   .. method:: descriptionForInstanceMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: descriptionForClassMethod_(selector)

      Returns a tuple with 2 byte strings: the selector name and the type signature for the selector.

      Returns :data:`None` when the selector is not part of the protocol.

   .. method:: instanceMethods()

      Returns a list of instance methods in this protocol.

   .. method:: classMethods()

      Returns a list of instance methods in this protocol.

   .. note::

      The interface of this class gives the impression that a protocol instance is an Objective-C
      object. That was true in earlier versions of macOS, but not in more recent versions.


.. class:: varlist

   A C array of unspecified length. Instances of this type cannot be created in Python code.

   This type is used when the API does not specify the amount of items in an array in a way
   that is usable by the bridge.

   .. warning::

      Access through a :class:`varlist` object can easily read or write beyond the end
      of the wrapped C array.  Read the Apple documentation for APIs that return a
      varlist to determine how many elements you can safely access and whether or not the
      array is mutable.

      The C array might also be freed by C code before the :class:`varlist` instance
      is garbage collected. The Apple documentation for the API should mention how long
      the reference is safe to use.

   .. attribute:: __typestr__

      The type encoding for elements of the array. See :ref:`type-encodings` for more
      information.

   .. method:: as_tuple(count)

      Returns a tuple containing the first *count* elements of the array.

   .. method:: as_buffer(count)

      Returns a writable :class:`memoryview` referencing the memory for the first *count*
      elements of the array.

      .. note::

         The returned :class:`memoryview` is currently always a byte view, future
         versions might return a view with a *format* attribute that's appropriate
         for the :data:`__typestr__` of the varlist object.

   .. method:: __getitem__(index)

      Returns the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices with step 1 and a specified stop index.

      Negative indexes are not supported because these objects have an unspecified length.

   .. method:: __setitem__(index, value)

      Sets the value of the *index*-th element of the array. Supports numeric
      indexes as well as slices with step 1 and a specified stop index  (but assigning
      to a slice is only possible when that does not resize the array).

      Negative indexes are not supported because these objects have an unspecified length.

      .. warning::

         When underlying data type is :data:`objc._C_ID` (that is, an array of Cocoa
         objects it is very likely that the retain count of the object needs to be
         adjusted. The :meth:`__setitem__` method stores a reference to the object
         *without* adjusting any reference counts.

         The correct behavior depends on the kind of array used, when the array is
         documented as containing strong references you should increase the retain count
         of the new value and lower the retain of the old value (in that order).


.. class:: function

   Instances of this class represent global functions from Cocoa frameworks. These
   objects are created using :func:`loadBundleFunctions` and :func:`loadFunctionList`.

   .. attribute:: __doc__

      Read-only property with the documentation string for the function.

   .. attribute:: __name__

      Read-only property with the name of the function

   .. attribute:: __module__

      Read-write property with the module that defined the function

   .. attribute:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.


.. class:: IMP

   This class is used to represent the actual implementation of an Objective-C
   method (basically a C function). Instances behave the same as unbound methods:
   you can call them but need to specify the "self" argument.

   .. attribute:: isAlloc

      Read-only attribute that specifies if the IMP is an allocator (that is,
      the implementation of "+alloc" or one of its variant)

      .. deprecated:: 11.1 Is always :data:`False` and will be removed in PyObjC 12.

   .. attribute:: isClassMethod

      Read-only attribute that specified if the IMP is for a class method.

   .. attribute:: signature

      Read-only attribute with the type encoding for the IMP.

   .. attribute:: selector

      Read-only attribute with the selector for the method that this IMP
      is associated with.

   .. attribute:: __name__

      Alias for :data:`selector`.

   .. attribute:: __signature__

      An :class:`inspect.Signature` for the object

      .. versionadded:: 3.0

   .. method:: __metadata__

      Returns a copy of the metadata dictionary for the selector.  See the
      :doc:`metadata system documentation </metadata/manual>` for more information.


.. class:: super

   This is a subclass of :class:`super <__builtin__.super>` that works
   properly for Objective-C classes as well as regular Python classes.

   The regular :class:`super <__builtin__.super>` does *not* work correctly
   for Cocoa classes, the default function doesn't support custom attribute
   getters as used by PyObjC.

   Always import this method in a way that shadows the builtin super when
   using *super* in class definitions, that is always import like this:

   .. sourcecode:: python

      from objc import super


Constants
---------

.. data:: nil

   Alias for :const:`None`, for easier translation of existing Objective-C
   code.

.. data:: YES

   Alias for :const:`True`, for easier translation of existing Objective-C
   code.

.. data:: NO

   Alias for :const:`False`, for easier translation of existing Objective-C
   code.

.. data:: NULL

   Singleton that tells the bridge to pass a :c:data:`NULL` pointer as
   an argument when the (Objective-)C type of that argument is a pointer.

   This behavior of the bridge is slightly different from using :data:`None`:
   with :data:`None` the bridge will allocate some memory for output
   parameters and pass a pointer to that buffer, with :data:`NULL` the
   bridge will always pass a :c:data:`NULL` pointer.

.. data:: PyObjC_BUILD_RELEASE

   The version number of the SDK used to build PyObjC, the value
   is ``major * 100  + minor`` (e.g. ``1305`` for macOS 13.5).

.. data:: platform

   This always has the value "MACOSX".


.. _type-encodings:

Objective-C type strings
------------------------

The Objective-C runtime and the PyObjC bridge represent the types of
instance variables and methods arguments and return values as a byte string
with a compact representation.

Basic types
............

The representation for basic types is a single character, the table below
lists symbolic constants in the for those constants.

======================== =================================================
Name                     Objective-C type
======================== =================================================
:const:`_C_ID`           *id* (an Objective-C instance)
------------------------ -------------------------------------------------
:const:`_C_CLASS`        an Objective-C class
------------------------ -------------------------------------------------
:const:`_C_SEL`          a method selector
------------------------ -------------------------------------------------
:const:`_C_CHR`          *char*
------------------------ -------------------------------------------------
:const:`_C_UCHR`         *unsigned char*
------------------------ -------------------------------------------------
:const:`_C_SHT`          *short*
------------------------ -------------------------------------------------
:const:`_C_USHT`         *unsigned short*
------------------------ -------------------------------------------------
:const:`_C_BOOL`         *bool*  (or *_Bool*)
------------------------ -------------------------------------------------
:const:`_C_INT`          *int*
------------------------ -------------------------------------------------
:const:`_C_UINT`         *unsigned int*
------------------------ -------------------------------------------------
:const:`_C_LNG`          *long*
------------------------ -------------------------------------------------
:const:`_C_ULNG`         *unsigned long*
------------------------ -------------------------------------------------
:const:`_C_LNG_LNG`      *long long*
------------------------ -------------------------------------------------
:const:`_C_ULNG_LNG`     *unsigned long long*
------------------------ -------------------------------------------------
:const:`_C_FLT`          *float*
------------------------ -------------------------------------------------
:const:`_C_DBL`          *double*
------------------------ -------------------------------------------------
:const:`_C_LNG_DBL`      *long double*
------------------------ -------------------------------------------------
:const:`_C_VOID`         *void*
------------------------ -------------------------------------------------
:const:`_C_UNDEF`        "other" (such a function)
------------------------ -------------------------------------------------
:const:`_C_CHARPTR`      C string (*char**)
------------------------ -------------------------------------------------
:const:`_C_NSBOOL`       *BOOL*
------------------------ -------------------------------------------------
:const:`_C_UNICHAR`      *UniChar*
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_TEXT` *char* when uses as text or a byte array
------------------------ -------------------------------------------------
:const:`_C_CHAR_AS_INT`  *int8_t* (or *char* when
                         used as a number)
======================== =================================================

.. versionadded: 11.1.1 The value ``_C_LNG_DBL``.

The values :const:`_C_NSBOOL`, :const:`_C_UNICHAR`, :const:`_C_CHAR_AS_TEXT`,
and :const:`_C_CHAR_AS_INT` are inventions of PyObjC and are not used in
the Objective-C runtime.

The value :const:`_C_NSBOOL` is deprecated as of PyObjC 9, use :const:`_C_BOOL`
instead. The two constants are treated exactly the same in PyObjC now that
the corresponding C types have the same representation (which wasn't true
for PowerPC).

Complex types
..............

More complex types can be represented using longer type strings:

* a pointer to some type is :const:`_C_PTR` followed by the type string
  of the pointed-to type.

* a bitfield in a structure is represented as :const:`_C_BFLD` followed
  by an integer with the number of bits.

  Note that PyObjC cannot convert bitfields at this time.

* a C structure is represented as :const:`_C_STRUCT_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_STRUCT_E`. The field name (including the
  closing equals sign) is optional.

  Structures are assumed to have the default field alignment, although
  it is possible to use a custom alignment when creating a custom type
  for a struct using :func:`objc.createStructType`.


* a C union is represented as :const:`_C_UNION_B` followed by the
  struct name, followed by :const:`'='`, followed by the encoded types of
  all fields followed by :const:`_C_UNION_E`. The field name (including the
  closing equals sign) is optional.

  Note that PyObjC cannot convert C unions at this time.

* a C array is represented as :const:`_C_ARY_B` followed by an integer
  representing the number of items followed by the encoded element type,
  followed by :const:`_C_ARY_E`.

* The C construct 'const' is mapped to :const:`_C_CONST`, that is a
  *const char\** is represented as :const:`_C_CONST` + :const:`_C_CHARPTR`.

* A C SIMD vector type (e.g. ``vector_float3``)
  is represented as follows:  :const:`_C_VECTOR_B` *N* *type* :const:`_C_VECTOR_E`.

  Matrix types (e.g. ``matrix_float2x3``) are C structs containing SIMD vectors,
  and are represented in the usual way.

  These representations are not supported in the Objective-C runtime, but are
  inventions by PyObjC. Because libffi does not support the corresponding
  C types these encodings are supported in limited subset of possible
  method signatures (basically only those signatures that are used by
  Apple system libraries).

Additional prefixes
...................

* :const:`_C_ATOMIC` can prefix any basic C type and denotes that the value
  should be accessed using atomic instructions.

  This value is currently ignored by PyObjC.

* :const:`_C_COMPLEX` can prefix any basic C type and denotes a C complex
  type.

  This value is currently not supported by PyObjC (and is not used
  in frameworks).

Additional annotations for method and function arguments
........................................................

Method arguments can have prefixes that closer describe their functionality.
Those prefixes are inherited from Distributed Objects are not used by the
Objective-C runtime, but are used by PyObjC.

* When a pointer argument is an input argument it is prefixed by
  :const:`_C_IN`.

* When a pointer argument is an output argument it is prefixed by
  :const:`_C_OUT`.

* When a pointer argument is an input and output argument it is prefixed
  by :const:`_C_INOUT`.

* Distributed objects uses the prefix :const:`_C_BYCOPY` to tell that a
  value should be copied to the other side instead of sending a proxy
  reference. This is not used by PyObjC.

* Distributed objects uses the prefix :const:`_C_ONEWAY` on the method return
  type to tell that the method result is not used and the caller should not
  wait for a result from the other side. This is not used by PyObjC.

When a pointer argument to a function prefixed by :const:`_C_IN`,
:const:`_C_OUT` or :const:`_C_INOUT` the bridge assumes that it is a pass by
reference argument (that is, a pointer to a single value), unless other
information is provided to the bridge.

The :const:`_C_IN`, :const:`_C_INOUT` and :const:`_C_OUT` encodings
correspond to the keyword ``in``, ``inout`` and ``out`` in Objective-C
code. This can be used to add the right information to the Objective-C
runtime without using :doc:`the metadata system </metadata/index>`. For
example:

.. sourcecode:: objective-c

   @interface OCSampleClass

   -(void)copyResourceOfName:(NSString*)name error:(out NSError**)error;

   @end

This tells the compiler that *error* is an output argument, which doesn't
affect code generation or compiler warnings but does result in :const:`_C_OUT`
being present in the type encoding for the argument.


Special encoded types
.....................

The table below shows constants for a number of C types that are used
in Cocoa but are not basic C types.

  ======================= ==============================
  Constant                Objective-C type
  ======================= ==============================
  :const:`_C_CFTYPEID`    *CFTypeID*
  ----------------------- ------------------------------
  :const:`_C_NSInteger`   *NSInteger*
  ----------------------- ------------------------------
  :const:`_C_NSUInteger`  *NSUInteger*
  ----------------------- ------------------------------
  :const:`_C_CFIndex`     *CFIndex*
  ----------------------- ------------------------------
  :const:`_C_CGFloat`     *CGFloat*
  ----------------------- ------------------------------
  :const:`_C_NSRange`     *NSRange*
  ----------------------- ------------------------------
  :const:`_C_CFRange`     *CFRange*
  ----------------------- ------------------------------
  :const:`_sockaddr_type` *struct sockaddr*
  ======================= ==============================

..versionadded:: 8.3

  _C_NSRange, _C_CFRange


Context pointers
----------------

A number of Objective-C APIs have one argument that is a context pointer,
which is a *void\**. In Objective-C your can pass a pointer to an
arbitrary value, in Python this must be an integer.

PyObjC provides a :data:`context` object that can be used to allocate
unique integers and map those to objects.

.. function:: context.register(value)

   Add a value to the context registry.

   :param value: An arbitrary object
   :return: A unique integer that's suitable to be used as a context pointer
            (the handle).

.. function:: context.unregister(value):

   Remove an object from the context registry, this object must be have
   been added to the registry before.

   :param value: An object in the context registry

.. function:: context.get(handle)

   Retrieve an object from the registry given the return value from
   :func:`context.register`.


Descriptors
-----------

.. function:: IBOutlet([name])

   Creates an instance variable that can be used as an outlet in
   Interface Builder. When the name is not specified the bridge will
   use the name from the class dictionary.

   The code block below defines an instance variable named "button" and
   makes that available as an outlet in Interface Builder.

   .. code-block:: python

      class SomeObject (NSObject):

          button = IBOutlet()

   .. note::

      The IBOutlet function is recognized by Interface Builder when it
      reads Python code.

.. function:: IBAction(function)

   Mark an method as an action for use in Interface Builder.  Raises
   :exc:`TypeError` when the argument is not a function.

   Usage:

   .. code-block:: python

      class SomeObject (NSObject):

         @IBAction
         def saveDocument_(self, sender):
             pass

   .. note::

      The IBOutlet decorator is recognized by Interface Builder when it
      reads Python code. Beyond that the decoerator has no effect.

.. function:: IBInspectable(prop)

   Mark a property as a value that can be introspected in IB.

   See `the Xcode documentation <https://developer.apple.com/library/ios/recipes/xcode_help-IB_objects_media/chapters/CreatingaLiveViewofaCustomObject.html>` for more information on this decorator.

.. function:: IB_DESIGNABLE(cls)

   Class decorator to tell IB that the class can be used in IB designs.

   See `the Xcode documentation <https://developer.apple.com/library/ios/recipes/xcode_help-IB_objects_media/chapters/CreatingaLiveViewofaCustomObject.html>` for more information on this decorator.

.. function:: instancemethod

   Explicitly mark a method as an instance method. Use this when
   PyObjC incorrectly deduced that a method should be a class method.

   Usage:

   .. code-block:: python

        class SomeObject (NSObject):

           @instancemethod
           def alloc(self):
               pass

   .. note::

      There is no function named *objc.classmethod*, use
      :func:`classmethod <__builtin__.classmethod>` to explicitly mark a function
      as a class method.


.. function:: accessor

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The conventions for accessor names that can be used with Key-Value Coding
   is described in the `Apple documentation for Key-Value Coding`_

   The table below describes the convention for methods for a property named '<property>',
   with a short description and notes. The `Apple documentation for Key-Value Coding`_
   contains more information.

   ================================================== =================================== =========================================
   Name                                               Description                         Notes
   ================================================== =================================== =========================================
   *property*                                         Getter for a basic property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   is\ *Property*                                     Likewise, for a boolean             PyObjC won't automatically set the
                                                      property.                           correct property type, use
                                                                                          :func:`typeAccessor` instead of
                                                                                          :func:`accessor`.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   set\ *Property*\ _                                 Setter for a basic property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   countOf\ *Property*                                Returns the number of
                                                      items in a indexed
                                                      property, or unordered
                                                      property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   objectIn\ *Property*\ AtIndex\_                    Returns the object at a specific
                                                      index for an indexed property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   *property*\ AtIndexes\_                            Returns an array of                 Don't use this with
                                                      object values at specific           :func:`typedAccessor`.
                                                      indexes for an indexed
                                                      property. The argument
                                                      is an *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   get\ *Property*\ _range_                           Optimized accessor                  Not supported by PyObjC, don't use
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   insertObject_in\ *Property*\ AtIndex\_             Add an object to an indexed
                                                      property at a specific index.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   insert\ *Property*\ _atIndexes_                    Insert the values from a list of    Don't use this with
                                                      at specific indices. The            :func:`typedAccessor`.
                                                      arguments are an *NSArray*
                                                      and an *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   removeObjectFrom\ *Property*\ AtIndex\_            Remove the value
                                                      at a specific index of an
                                                      indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ AtIndexes\_                    Remove the values at specific
                                                      indices of an indexed property. The
                                                      argument is an
                                                      *NSIndexSet*.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   replaceObjectIn\ *Property*\ AtIndex_withObject\_  Replace the value at a specific
                                                      index of an indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   replace\ *Property*\ AtIndexes_with\ *Property*\_  Replace the values at specific      Don't use with :func:`typedAccessor`
                                                      indices of an indexed property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   enumeratorOf\ *Property*                            Returns an *NSEnumerator*
                                                       for an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   memberOf\ *Property*\ _                             Returns True if the value is
                                                       a member of an unordered property
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   add\ *Property*\ Object\_                           Insert a specific object in
                                                       an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   add\ *Property*\ _                                  Add a set of new values
                                                       to an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ Object\_                        Remove an object
                                                       from an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   remove\ *Property*\ _                               Remove a set of objects
                                                       from an unordered property.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   intersect\ *Property*\ _                            Remove all objects from
                                                       an unordered property that
                                                       are not in the set argument.
   -------------------------------------------------- ----------------------------------- -----------------------------------------
   validate\ *Property*\ _error_                       Validate the new value of a         For typed accessor's the value
                                                       property                            is wrapped in an *NSValue*
                                                                                           (but numbers and booleans are automatically
                                                                                           unwrapped by the bridge)
   ================================================== =================================== =========================================

   PyObjC provides another mechanism for defining properties: :class:`object_property`.

   .. versionchanged:: 2.5
      Added support for unordered properties. Also fixed some issues for 64-bit
      builds.

.. _`Apple documentation for Key-Value Coding`: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html

.. function:: typedAccessor(valueType)

   Use this decorator on the definition of accessor methods to ensure
   that it gets the right method signature in the Objective-C runtime.

   The *valueType* is the encoded string for a single value.

   .. note::

      When you use a typed accessor you must also implement "setNilValueForKey\_",
      as described in the `Apple documentation for Key-Value Coding`_

.. function:: typedSelector(signature)

   Use this decorator to explicitly set the type signature for a method.

   An example:

   .. code-block:: python

        @typedSelector(b'I@:d')
        def makeUnsignedIntegerOfDouble_(self, d):
           return d


   .. versionchanged:: 8.3

      The decorated function can now also be a :func:`classmethod`

.. function:: namedSelector(name [, signature])

   Use this decorator to explicitly set the Objective-C method name instead
   of deducing it from the Python name. You can optionally set the method
   signature as well.

   .. versionchanged:: 8.3

      The decorated function can now also be a :func:`classmethod`

.. function:: callbackFor(callable[, argIndex=])

   Use this decorator to tell that this function is the callback for
   an (Objective-C) API that stores a reference to the callback
   function.

   You only *have* to use this API when the Objective-C API can store
   the callback function for later usage. For other functions the
   bridge can create a temporary callback stub.

   Using this decorator for methods is not supported

   Usage:

   .. code-block:: python

       @objc.callbackFor(NSArray.sortedArrayUsingFunction_context\_)
       def compare(left, right, context):
           return 1

   This tells the bridge that 'compare' is used as the sort function
   for NSArray, and ensures that the function will get the correct
   Objective-C signature.

   .. note::

      The example will also work without the decorator because
      NSArray won't store a reference to the compare function that
      is used after 'sortedArrayUsingFunction_context\_' returns.

.. function:: callbackPointer(closure)

   Returns a value that can be passed to a function expecting
   a ``void *`` argument. The value for *closure* must be a function
   that's decorated with :func:`callbackFor`.

   .. versionadded:: 3.1

.. function:: selectorFor(callable[, argIndex])

   Decorator to tell that this is the "callback" selector for another
   API.

   Usage:

   .. code-block:: python

      @objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_)
      def sheetDidEnd_returnCode_contextInfo_(self, sheet, returnCode, info):
          pass

   This will tell the bridge that this method is used as the end method
   for a sheet API, and will ensure that the method is registered with
   the correct Objective-C signature.


.. function:: synthesize(name[, copy[, readwrite[, type[, ivarName]]]])

   :param name:  name of the property
   :param copy:  if false (default) values are stored as is, otherwise
                 new values are copied.
   :param readwrite: If true (default) the property is read-write
   :param type:  an encoded type for the property, defaults to
                 :data:`_C_ID`.
   :param iVarName: Name of the instance variable used to store
                    the value. Default to the name of the property
                    prefixed by and underscore.

   This synthensizes a getter, and if necessary, setter method with
   the correct signature. The getter and setter provide access to
   an instance variable.

   This can be used when specific semantics are required (such as
   copying values before storing them).

   The class :class:`object_property` provides similar features with
   a nicer python interface: with that class the property behaves
   itself like a property for python code, with this function you
   still have to call accessor methods in your code.

Interacting with ``@synchronized`` blocks
-----------------------------------------

PyObjC provides an API that implements locking in the same way as the
``@synchronized`` statement in Objective-C.

.. code-block:: python

  with object_lock(anNSObject):
      pass

.. class:: object_lock(value)

   This class represents the mutex that protects an Objective-C object
   for the ``@synchronized`` statement. This can be used as a context
   manager for the ``with`` statement, but can also be used standalone.

   .. method:: lock

      Acquire the object mutex

   .. method:: unlock

      Release the object mutex


Properties
----------

Introduction
............

Both Python and Objective-C have support for properties, which are object attributes
that are accessed using attribute access syntax but which result in a method call.

The Python built-in :class:`property <__builtin__.property__` is used to define new
properties in plain Python code. These properties don't full interoperate with
Objective-C code though because they do not necessarily implement the Objective-C
methods that mechanisms like Key-Value Coding use to interact with a class.

PyObjC therefore has a number of property classes that allow you to define new
properties that do interact fully with the Key-Value Coding and Observation
frameworks.

.. class:: object_property(name=None, read_only=False, copy=False, dynamic=False, ivar=None, typestr=_C_ID, depends_on=None)


   :param name: Name of the property, the default is to extract the name from the class dictionary
   :param read_only: Is this a read-only property? The default is a read-write property.
   :param copy: Should the default setter method copy values? The default retains the new value without copying.
   :param dynamic: If this argument is :data:`True` the property will not generate default accessor,
     but will rely on some external process to create them.
   :param ivar: Name of the instance variable that's used to store the value. When this value is :data:`None`
     the name will be calculated from the property name. If it is :data:`NULL` there will be no instance variable.
   :param typestr: The Objective-C type for this property, defaults to an arbitrary object.
   :param depends_on: A sequence of names of properties the value of this property depends on.

During the class definition you can add accessor methods by using the property as a decorator


.. method:: object_property.getter

   Decorator for defining the getter method for a property. The name of the method should be the
   same as the property::

       class MyObject (NSObject):

           prop = objc.object_property()

           @prop.getter
           def prop(self):
              return 42


.. method:: object_property.setter

   Decorator for defining the setter method for a property. The name of the method should be the
   same as the property.


.. method:: object_property.validate

   Decorator for defining a Key-Value Coding validator for this property.


It is possible to override property accessor in a subclass::

   class MySubclass (MyObject):
       @MyObject.prop.getter
       def getter(self):
           return "the world"

This can also be used to convert a read-only property to a read-write one
by adding a setter accessor.


Properties for structured types
...............................

Key-Value Coding is slightly different for structured types like sets and
lists (ordered and unordered collections). For this reason PyObjC also provides
subclasses of :class:`object_property` that are tuned for these types.

.. class:: array_property

   This property implements a list-like property. When you access the property
   you will get an object that implements the :class:`MutableSequence` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: set_property

   This property implements a set-like property. When you access the property
   you will get an object that implements the :class:`MutableSet` ABC, and
   that will generate the correct Key-Value Observation notifications when
   the datastructure is updated.

.. class:: dict_property

   This property is like an :class:`object_property`, but has an empty
   NSMutableDictionary object as its default value. This type is mostly
   provided to have a complete set of property types.

These collection properties are at this time experimental and do not yet
provide proper hooks for tweaking their behavior. Future versions of PyObjC
will provide such hooks (for example a method that will be called when an
item is inserted in an array property).


Unconvertible pointer values
----------------------------

With incomplete metadata the bridge can run into pointer values that
it cannot convert to normal Python values. When
:data:`options.unknown_pointer_raises <objc.options.unknown_pointer_raises>`
is false such pointer values are bridged as instances of :class:`ObjCPointer`.

The bridge will unconditionally emit a warning before creating such instances,
the reason for this is that the use of :class:`ObjCPointer` is unwanted.

.. class:: ObjCPointer

   .. data:: typestr

      A bytes string with the Objective-C type encoding for
      the pointed to value.

      .. versionadded: 8.5

   .. data:: pointerAsInteger

      An integer value with the raw pointer value.

"FILE*" support
---------------

PyObjC provides a limited wrapper for C's ``FILE*`` type. This wrapper
is not a full replacement for the :mod:`io` module, but is only provided
to make it easier to use a limited set of Cocoa APIs that use this
C type.

.. class:: FILE

   This class represents ``FILE*`` values.

   This types provides a fairly limited file-like API for binary
   I/O. Instances of this type don't close the stream automatically and
   do not implement a contextmanager.

   .. method:: at_eof()

      :return: If the stream is at the EOF marker
      :rtype: bool

   .. method:: has_errors()

      :return: If the stream has errors
      :rtype: bool

   .. method:: close()

      Closes the stream.

   .. method:: flush()

      Flushes the file buffers.

      .. versionadded: 8.1

   .. method:: readline()

      :return: Next line in the file, or an empty string at the end of file
      :rtype: bytes

   .. method:: read(buffer_size)

      :param int buffer_size: Number of bytes to read
      :return: The data that was read, which can be less than the requested amount
               and will be an empty string at the enf of file.
      :rtype: bytes

   .. method:: write(buffer)

      :param bytes buffer: Data to write.
      :return: Amount of bytes that were written.
      :rtype: int

   .. method:: tell()

      :return: the current offset of the stream.
      :rtype: int

   .. method:: seek(offset, whence)

      :param int offset: Offset to seek to
      :param int whence: Base for the offset (of one :data:`os.SEEK_SET`,
                         :data:`os.SEEK_CUR`, :data:`os.SEEK_END`).

   .. method:: fileno()

      :return: The file descriptor associated with the ``FILE`` object
      :rtype: int
