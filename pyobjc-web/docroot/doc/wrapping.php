<?
    $title = "How to wrap an Objective-C class library";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/05/04 12:56:38 $';

    include "header.inc";
?>
<div class="document" id="how-to-wrap-an-objective-c-class-library">
<h1 class="title">How to wrap an Objective-C class library</h1>
<!-- :author: Ronald Oussoren -->
<div class="section" id="introduction">
<h1><a name="introduction">Introduction</a></h1>
<p>This document describes how you can wrap on Objective-C class library using
a Python module or package.  This document assumes that your class library is
located in a framework.</p>
<p>Wrapping can be pretty easy for most classes, but you may have to write some
C code for specific methods.</p>
</div>
<div class="section" id="the-basics">
<h1><a name="the-basics">The basics</a></h1>
<p>The code for loading a framework and exporting its classes is pretty simple:</p>
<pre class="literal-block">
import objc
objc.loadBundle(&quot;MyFramework&quot;, globals(), 
   bundle_path='/path/to/MyFramework.framework')
del objc
</pre>
<p>If your class library does not require helper functions for some methods this
is all that is needed.</p>
</div>
<div class="section" id="wrapping-global-functions-and-constants">
<h1><a name="wrapping-global-functions-and-constants">Wrapping global functions and constants</a></h1>
<p>The code above only provides wrappers for Objective-C classes, if the library
also defines global functions and/or constants you'll have to write an 
extension module to make these available to Python.</p>
<p>You can use the PyObjC C-API (to be documented) when writing this module.</p>
</div>
<div class="section" id="pointer-arguments">
<h1><a name="pointer-arguments">Pointer arguments</a></h1>
<p>Methods with pointer arguments (other then arguments that are equivalent to 
an 'id') require more work. If the pointer arguments are used to pass a single 
value to/from a function ('pass-by-reference arguments') you'll just have to 
provide more specific method signatures. In other cases you'll have to write
custom wrappers for these methods.</p>
<div class="section" id="pass-by-reference-arguments">
<h2><a name="pass-by-reference-arguments">Pass-by-reference arguments</a></h2>
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
hang of it. The signature for this method is 'v&#64;:^&#64;&#64;'.</p>
<p>Let's say the first argument is an output parameter. Output parameters are 
denoted in the signature string using the character 'o' before the actual
argument signature. The 'correct' signature for method is therefore 'v&#64;:o^&#64;&#64;'.
The following code tells the brigde about this better method signature:</p>
<pre class="literal-block">
import objc
objc.set_signature_for_selector(&quot;ClassName&quot;, &quot;selector:withArguments:&quot;,
     &quot;v&#64;:o^&#64;:&#64;&quot;)
</pre>
<p>To anotate method signatures you'll have to add a single character before all
'^' characters in the signature of a method. The characters are:</p>
<ul class="simple">
<li>output parameter: o</li>
<li>input parameter: i</li>
<li>input-output parameter: O</li>
</ul>
</div>
<div class="section" id="special-wrappers">
<h2><a name="special-wrappers">special wrappers</a></h2>
<p>If the method has pointer arguments that are not pass-by-reference arguments,
or if the default method wrappers are not suitable for other reasons, you'll
have to write custom wrappers. For every custom wrapper you'll have to write
three functions: 1 to call the method from Python, 1 to call the superclass
implementation of the method from Python and 1 to call a Python implementation
of the method from Objective-C.</p>
<p>For now it is best to check the source code for the wrappers for the Cocoa 
class library for more information. We'll add documentation for this in the
future.</p>
<p>NOTE: It is likely that there will be changes w.r.t. the special wrappers.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>