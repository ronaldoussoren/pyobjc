<?
    $title = "GNUstep support in PyObjC";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">GNUstep support in PyObjC</h1>
<p><strong>WARNING</strong>: GNUStep support is broken.  If you would like to help, let us know.</p>
<p>PyObjC has limited support for GNUstep, the 'objc' and 'Foundation' packages
build and pass some, but by far not all, unittests.  More work is needed to
make the GNUstep port as stable as the Mac OS X &quot;port&quot;.</p>
<p>The GNUstep port was primarily developed on Linux i86 (specifically 
the Debian testing distribution), using python 2.3.3,  gcc 3.3.2 and 
gnustep-base1 1.9.0-1.  The code in setup.py works for this configuration,
but probably not for other configurations.</p>
<p>GNUstep support is <em>very</em> fragile, in some versions of the the selectors for
new classes should be strings, in others they should be SEL objects (as you
would expect).  We also use undocumented private functions to initialize new
classes.</p>
<div class="section" id="todo">
<h3><a name="todo">TODO</a></h3>
<ul>
<li><p class="first">[Serious] Fix linkage problems.  The ObjC runtime doesn't seem to be 
initialized correctly and/or the classes in newly loaded frameworks are
not correctly registered in the runtime.</p>
</li>
<li><p class="first">Fix the odd bug...</p>
<p>I currently get the following text when importing objc:</p>
<pre class="literal-block">
Unable to retrieve information about SIGPIPE
</pre>
<p>This text is not printed by PyObjC and I haven't been able to find who
does print that text...</p>
</li>
<li><p class="first">Fix bugs found using the unittests</p>
<p>runPyObjCTests finds some problems that disappear when those tests 
are run separately...</p>
</li>
<li><p class="first">Extract more CFLAGS and LDFLAGS information from the GNUstep build system,
instead of hard-coding the information</p>
</li>
</ul>
</div>
</div>
<?
    include "footer.inc";
?>