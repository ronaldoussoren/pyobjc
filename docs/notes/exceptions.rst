Exceptions in Cocoa code
========================

The Objective-C language supports exceptions and that feature
is fully supported by PyObjC: the bridge will translate between
Python and Objective-C exceptions on transitions in either way
between the two languages.

That said, Objective-C code in general only uses exception for
serious bugs and most code, likely including Apple frameworks,
are not written with exception safety in mind.

In general it is advisable to avoid raising exceptions that will
cross the boundary from Python to Objective-C, for example by
using a decorator that catches and logs exceptions.
