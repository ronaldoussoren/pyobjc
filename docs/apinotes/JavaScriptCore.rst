API Notes: JavaScriptCore framework
===================================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/javascriptcore/?preferredLanguage=occ

These bindings are accessed through the ``JavaScriptCore`` package (that is, ``import JavaScriptCore``).

API Notes
---------

The JavaScriptCore library is very low-level and the Python bindings don't change that. This means interacting with JavaScript
through these bindings require a fairly large amount of code.


Reference counting
..................

The various JavaScriptCore types (such as ``JSValueRef`` and ``JSContextRef``) are C types with manual reference counting. PyObjC
does *not* manage the reference counts for you, you'll have to call the correct retain and release functions manually to avoid
leaking memory and/or crashing.


``autoreleasing``
..................

This is a context manager that makes it easier to deal with reference counts::

    with JavaScriptCore.autoreleasing(expression) as value:
       pass

is more or less equivalent to::

     value = expression
     try:
          pass

     finally:
          JavaScriptCore.JSReleaseContext(value)

The actual release function used depends on the type of *value*.



``JSStringGetCharactersPtr``
............................

This function is not supported. Convert the string to a Python type using ``JSStringCopyCFString`` or ``JSStringGetUTF8CString``.

``JSObjectMake``, ``JSObjectGetPrivate``, ``JSObjectSetPrivate``
................................................................

The private data of an object is a ``void*`` in (Objective-)C, and an integer in Python. Use the ``objc.context`` object to attach
arbitrary data to an object::

   anObj = ... #
   JavaScriptCore.JSOObjectSetPrivate(anObject, objc.context.register(aValue))
   aValue = objc.context.get(JavaScriptCore.JSObjectGetPrivate(anObject))


``JSStaticValue``, ``JSStaticFunction``, ``JSClassDefinition``
..............................................................

These structs and functions using them are not yet supported.


``JSClassCreate``, ``kJSClassDefinitionEmpty``
..............................................

Not supported at the moment as this requires manual wrappers (C code).


``JSExport``
............

macOS 10.9 introcuded a ``JSExport`` protocol. The macro ``JSExportAs`` is
available as a function with a slightly more involved interface:

.. sourcecode:: python

   export_proto = objc.formal_protocol(
            "ExportProto",
            (objc.protocolNamed("JSExport"),),
            [
                 JavaScriptCore.JSExportAs("doFoo",
                                           objc.selector(None, selector=b"doFoo:withBar:", signature=b"v@:@@"),
                 ),
                 objc.selector(None, selector=b"method1:", signature=b"v@:@"),
            ]
    )

But sadly, using a protocol defined in Python does not work at this time.

To use the protocol you must use a Python that's build with macOS 10.9 or later
as the deployment target.
