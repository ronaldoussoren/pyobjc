<?
    $title = "Structure of the PyObjC package";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/02/12 20:43:02 $';

    include "header.inc";
?>
<div class="document" id="structure-of-the-pyobjc-package">
<h1 class="title">Structure of the PyObjC package</h1>
<!-- This document is in structured text markup to enable easy translation to 
HTML. -->
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>This document gives an overview of the PyObjC for developers (of the package).</p>
<p>One of the sections describes how all of it works, and some of the limitation.</p>
</div>
<div class="section" id="methods">
<h1><a name="methods">Methods</a></h1>
<p>Classes are scanned for methods when the python wrapper for a class is created.
We then create python wrappers for those methods. This way users can use the
normal python introspection methods to check which methods are available.</p>
<p>Sadly enough some classes in the Cocoa frameworks on Mac OSX grow new methods
when the first instance of those classes is created. We therefore have added 
some additional code that rescans the method tables on several occasions.</p>
</div>
<div class="section" id="subclassing">
<h1><a name="subclassing">Subclassing</a></h1>
<p>It is possible to subclass objective-C classes in python and this results in a hybrid Python/Objective-C class. Instances of these classes consist of a cluster of 2 objects, a Python object and an Objective-C object.</p>
<p>The reference count (or retainCount in objective-C speak) is stored in the 
Python object, mostly because that is the only way to maintain a single 
reference count for the cluster. The pointers from the python half of the 
cluster to the objective-C half, and the pointers the other way around, are
not counted in the reference count. If those would be counted we would
introduce cycles that are not detectable by the cycle-breaking garbage 
collector in python and all python/objective-C hybrids would be immortal.</p>
<p>The first python subclass of an objective-C class introduces a new instance
variable in the objective-C object to store the pointer to the python half of
the cluster. This variable is always referenced by name.  The python half is 
a subclass of objc_object that already contains a pointer to an objective-C 
object.</p>
<p>The first python subclass of an objective-C class also introduces a number of
methods (both class methods and instance methods) that allow us to maintain the
illusion of a single object. Check class-builder.m for details.</p>
</div>
<div class="section" id="directory-structure">
<h1><a name="directory-structure">Directory structure</a></h1>
<dl>
<dt>Doc/</dt>
<dd>Documentation</dd>
<dt>Examples/</dt>
<dd>Example scripts and applets.</dd>
<dt>Lib/</dt>
<dd>Python modules that will be installed in the library. Currently contains
the packages 'objc', 'Cocoa' and 'AddressBook'</dd>
<dt>Modules/</dt>
<dd>Extension modules related to the packages in 'Lib'. This directory contains
both the core module 'objc._objc' and a number of extension modules that
help in wrapping all of Cocoa.</dd>
<dt>Scripts/</dt>
<dd>Scripts used during building and/or development of PyObjC.</dd>
<dt>Tools/</dt>
<dd>Scripts that are usefull for users of PyObjC</dd>
</dl>
</div>
<div class="section" id="reference-counts">
<h1><a name="reference-counts">Reference counts</a></h1>
<p>The Objective-C rules for reference counts are pretty easy: A small number
of class methods (alloc, allocWithZone:, copy, ...) transfer object ownership
to the caller. For all other objects you have to call 'retain' if you want
to keep a reference. This includes all factory methods (e.g. 
[String stringWithCString:&quot;bla&quot;])!</p>
<p>The objc module tries to make the management of reference counts completely
transparent for the user of the module. This is mostly solved in 
[de]pythonify_c_value. Additonal code is needed when calling methods that
transfer ownership of their return value (as described above) and when updating
a instance variable in an Objective-C object (retain new and release old, 
in that order). Both are implemented.</p>
</div>
<div class="section" id="strings">
<h1><a name="strings">Strings</a></h1>
<p>We currently automaticly convert from Python strings to NSStrings (and back). 
This may not be the smartest thing to do because NSString has a number of 
methods that don't have an equivalent in Python.</p>
<p>Converting a Python string to objective-C and back currently converts the 
string to Unicode. If may be usefull to try to convert to a normal string
(using [NSString dataUsingEncoding:allowLossyConversion:]) and only return
a Unicode object if that fails.</p>
<p>When translating from NSString to a Python unicode object (and back) we first 
translate to a UTF8 encoding. This way we don't have to worry about any
differences in the representation of Unicode strings in Python and objective-C
(Python has two different represenations, selection is at compile-time)</p>
</div>
</div>
<?
    include "footer.inc";
?>