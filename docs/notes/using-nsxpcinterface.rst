Using NSXPCInterface from Python
================================

The Foundation class ``NSXPCInterface`` requires an Objective-C
protocol to define the API of the interface. Those protocols
cannot be defined in Python using :class:`objc.formal_protocol`
because the Cocoa class requires some data ("extended method sigantures")
that cannot be registered using the public API for the Objectie-C
runtime.

If you do try to use a protocol defined in Python with ``NSXPCInterface``
you'll get an error similar to this:

::
       NSInvalidArgumentException - NSXPCInterface: Unable to get extended method signature from Protocol data (MyProtocol / runCommand:withReply:). Use of clang is required for NSXPCInterface.


This means that any custom protocols that will be used
with ``NSXPCInterface`` need to be defined in a C extension which
is compiled using the clang compiler (the compiler used by Xcode).

The compiler will elide protocol information from the binary for
all protocols that aren't actually used. To ensure that the protocol
information is included add an (unused) function that appears to
use the protocol, for example:

.. sourcecode:: Objective-C

   static void use_protocol(void) __attribute__((__unused__))
   {
       printf("%p\n", @protocol(MyProtocol));
   }
