<?
    $title = "How to wrap an Objective-C class library";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">How to wrap an Objective-C class library</h1>
<!-- :author: Ronald Oussoren -->
<div class="section" id="introduction">
<h3><a name="introduction">Introduction</a></h3>
<p>This document describes how you can wrap on Objective-C class library using
a Python module or package.  This document assumes that your class library is
located in a framework.</p>
<p>Wrapping can be pretty easy for most classes, but you may have to write some
C code for specific methods.</p>
</div>
<div class="section" id="the-basics">
<h3><a name="the-basics">The basics</a></h3>
<p>The code for loading a framework and exporting its classes is pretty simple:</p>
<pre class="literal-block">
import objc
objc.loadBundle(&quot;MyFramework&quot;, globals(), 
   bundle_path='/path/to/MyFramework.framework')
del objc
</pre>
<p>In general you should not load frameworks this way, but you should write a
package or module to do this for you (e.g. place this code in <tt class="docutils literal"><span class="pre">MyFramework.py</span></tt>
or <tt class="docutils literal"><span class="pre">MyFramework/__init__.py</span></tt>. This makes it possible to 
<tt class="docutils literal"><span class="pre">import</span> <span class="pre">MyFramework</span></tt> which is much more convenient.</p>
<p>If your class library does not require helper functions for some methods this
is all that is needed.</p>
<p>It is currently necessary to import the wrapper modules for all frameworks that
are used by your framework. Not doing this may lead to subtle bugs in other
parts of the code. This is a limitation of PyObjC that will be 
lifted in a future version.</p>
</div>
<div class="section" id="wrapping-global-functions-and-constants">
<h3><a name="wrapping-global-functions-and-constants">Wrapping global functions and constants</a></h3>
<p>The code above only provides wrappers for Objective-C classes, if the library
also defines global functions and/or constants you'll have to write an 
extension module to make these available to Python.</p>
<p>You can use the PyObjC C-API (to be documented) when writing this module. With
some luck you can adapt the scripts in <tt class="docutils literal"><span class="pre">Scripts/CodeGenerators</span></tt> to generate
this module for you. These scripts are both very rough and tuned for the Apple
headers, so YMMV.</p>
<p>Note that we currently do not install the <tt class="docutils literal"><span class="pre">pyobjc-api.h</span></tt> header, you'll have
to copy it from the source-tree until we do. This header is not installed 
because the interface is not yet stable, please let us know if you want to
use the API.</p>
</div>
<div class="section" id="pointer-arguments">
<h3><a name="pointer-arguments">Pointer arguments</a></h3>
<p>Methods with pointer arguments (other then arguments that are equivalent to 
an 'id') require more work. If the pointer arguments are used to pass a single 
value to/from a function ('pass-by-reference arguments') you'll just have to 
provide more specific method signatures. In other cases you'll have to write
custom wrappers for these methods.</p>
<p>Check <tt class="docutils literal"><span class="pre">Modules/Foundation</span></tt> for examples of these custom wrappers.</p>
<div class="section" id="pass-by-reference-arguments">
<h4><a name="pass-by-reference-arguments">Pass-by-reference arguments</a></h4>
<p>Pass-by-reference arguments can be 'in' (data passed into the function), 
'out' (data is returned from the function) or 'inout' (data is passed into 
and then returned from  the function).</p>
<p>Given the following class interface:</p>
<pre class="literal-block">
&#64;interface ClassName {}

-(void)selector:(id*)outArgument withArguments:(NSArray*)data;

&#64;end
</pre>
<p>The compiler will generate a method signature for this method and this can 
be accessed from Python using the property 'signature' of Objective-C methods. 
You can also just make up the signature, which is quite easy once you get the
hang of it. The signature for this method is 'v&#64;:^&#64;&#64;'.  See <a class="reference" href="http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/RuntimeOverview/chapter_4_section_6.html">Type Encodings</a>
for the list of valid encoding characters for the Apple Objective-C runtime.</p>
<p>Let's say the first argument is an output parameter. Output parameters are 
denoted in the signature string using the character 'o' before the actual
argument signature. The 'correct' signature for method is therefore 'v&#64;:o^&#64;&#64;'.
The following code tells the bridge about this better method signature:</p>
<pre class="literal-block">
import objc
objc.setSignatureForSelector(&quot;ClassName&quot;, &quot;selector:withArguments:&quot;,
     &quot;v&#64;:o^&#64;:&#64;&quot;)
</pre>
<p>To annotate method signatures you'll have to add a single character before all
'^' characters in the signature of a method. The characters are:</p>
<ul class="simple">
<li>output parameter: o</li>
<li>input parameter: n</li>
<li>input-output parameter: N</li>
</ul>
</div>
<div class="section" id="special-wrappers">
<h4><a name="special-wrappers">special wrappers</a></h4>
<p>If the method has pointer arguments that are not pass-by-reference arguments,
or if the default method wrappers are not suitable for other reasons, you'll
have to write custom wrappers. For every custom wrapper you'll have to write
three functions: 1 to call the method from Python, 1 to call the superclass
implementation of the method from Python and 1 to call a Python implementation
of the method from Objective-C.</p>
<p>You also must write a custom wrapper when the method has a variable number
of arguments. It is often advisable to documented varargs method as 
unsupported, or to support them only using a fixed number of arguments.</p>
<p>For now it is best to check the source code for the wrappers for the Cocoa 
class library for more information. We'll add documentation for this in the
future.</p>
</div>
<div class="section" id="protocols">
<h4><a name="protocols">protocols</a></h4>
<p>If the framework defines any (informal) protocols you should add 
<tt class="docutils literal"><span class="pre">objc.informal_protocol</span></tt> objects for those protocols to your module. These
can be defined in a submodule, as long as you arrange for that module to be
loaded whenever someone imports your package.</p>
<p>See <tt class="docutils literal"><span class="pre">Lib/Foundation/protocols.py</span></tt> for examples of protocol definitions.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>