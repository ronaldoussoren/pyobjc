<?
    $title = "Userguide for PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:46 $';

    include "header.inc";
?>
<div class="document" id="userguide-for-pyobjc">
<h1 class="title">Userguide for PyObjC</h1>
<!-- This file is formatted using the rules for StructuredText -->
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>This is the user guide for PyObjC. It describes how to use this package to
implement Python scripts that use Objective-C classes and objects. It also
describes the limitations of this Package.</p>
<p>The last section describes the C API of this package and why you may want to
use it.</p>
</div>
<div class="section" id="overview">
<h1><a name="overview">Overview</a></h1>
<p>Using PyObjC is pretty simple, as it strives to make the bridge completely
transparent. On the lowest level you can import the 'objc' module and use that
to locate classes (objc.lookUpClass). For most users it is more usefull to
just import 'Foundation' and 'AppKit' and use the familiar Cocoa classes
and functions.</p>
<p>Objective-C classes are make available as new-style classes, and can be queried
using the normal introspection techniques.</p>
<p>Methodnames for Objective-C classes are constructed as follows: Concatenate all 
elements of the selector and replace colons by underscores.</p>
<p>The order of arguments is the same as in Objective-C, with one exception: If
a method as output-only arguments those arguments are not present in the python
version of the method. If a method has output parameters (either input-output
or output-only) the values of these parameters are passed back in the return
value of the python version. The return value of methods with output parameters
is a tuple where the first element is the return-value of the Objective-C 
method (or None if it is a method returning 'void') and the other elements are
the values of output arguments.</p>
</div>
<div class="section" id="informal-protocols">
<h1><a name="informal-protocols">(Informal) Protocols</a></h1>
<p>Cocoa defines a number of formal and informal protocols that specify the 
methods that should be defined by a class if it wants to be used in particular
roles (such as the data source for an NSTableView).</p>
<p>The type objc.informal_protocol can be used to specify the selectors used by
those (informal) protocols in Objective-C. Instances of objc.informal_protocol 
are used when defineing subclasses of Objective-C classes and signal that the 
class implements the given protocol.</p>
<p>The AppKit and Foundation modules export a number of usefull protocols, 
corresponding to the protocols defined in the Cocoa documentation. It is 
essential to use these protocol definitions as mixins when defining classes that
conform to the protocol. This not only helps catching typos when developing
classes, but also provides information to the bridge that is essential for
correct operation of the bridge.</p>
</div>
<div class="section" id="building-an-application">
<h1><a name="building-an-application">Building an application</a></h1>
<p>There are two different ways to build application bundles. The resulting 
applications are functionally equivalent, although not identical.</p>
<p>If Apple's developer tools are installed you can use one of the PyObjC 
project templates to build your application. (TODO: Add link to documentation
on the templates). The <tt class="literal"><span class="pre">TableModel2</span></tt> example uses Project Builder.</p>
<p>If is also possible to build application bundles using bundlebuilder, using
scripts that are simular to the <tt class="literal"><span class="pre">setup.py</span></tt> script used by distutils. The
<tt class="literal"><span class="pre">TableModel</span></tt> example uses this method. For more documentation, see the
online documentation of module <tt class="literal"><span class="pre">bundlebuilder</span></tt>.</p>
</div>
<div class="section" id="limitations">
<h1><a name="limitations">Limitations</a></h1>
<p>The objc module automaticly wraps classes and objects. This works correctly in
the easy case where there are no methods with variable arguments or 
pass-by-reference arguments. If there are, the core module needs some help.</p>
<p>For this reason it is best to not use just the core API when your working with
this module, but to use packages like 'Foundation' that provide the help 
needed and might also wrap other functionality (constants, functions) in a framework.</p>
<p>The current version of the module does not provide support for threading. It
might be possible to create threads using the 'thread' module if you manually
create an NSAutoreleasePool for the thread. This has not been tested. The
Cocoa threading classes should not be used because they don't update the 
state of the Python interpreter when creating a new thread.</p>
</div>
<div class="section" id="c-api">
<h1><a name="c-api">C API</a></h1>
<div class="section" id="id1">
<h2><a name="id1">Introduction</a></h2>
<p>The PyObjC package provides a C API that can be used when you're wrapping 
functions that deal with Objective-C objects or classes. It can also be used
to provide functions that help to wrap problematic objective-C methods (like 
those that take a variable number of arguments).</p>
<p>This API is used by the 'Cocoa' package (part of the PyObjC distribution) to
wrap the entire Cocoa API.</p>
</div>
<div class="section" id="how-to-use-it">
<h2><a name="how-to-use-it">How to use it</a></h2>
<p>You <tt class="literal"><span class="pre">#include</span></tt> &quot;pyobjc-api.h&quot; in your module implementation. In the module
initialisation function you then call <tt class="literal"><span class="pre">ObjC_ImportModule(mymodule)</span></tt>. After
this you can use the functions and constants defined in the API.</p>
</div>
<div class="section" id="constants">
<h2><a name="constants">Constants</a></h2>
<p>TODO</p>
</div>
<div class="section" id="functions">
<h2><a name="functions">Functions</a></h2>
<p>TODO</p>
</div>
<div class="section" id="id2">
<h2><a name="id2">Limitations</a></h2>
<p>We currently assume that extension module contain at most 1 file that uses
the PyObjC API.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>