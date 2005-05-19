<?
    $title = "Notes on supported APIs and classes on Mac OS X";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<h1 class="title">Notes on supported APIs and classes on Mac OS X</h1>
<!-- :author: Ronald Oussoren -->
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#introduction" id="id2" name="id2">Introduction</a></li>
<li><a class="reference" href="#core-objective-c-runtime" id="id3" name="id3">Core Objective-C runtime</a></li>
<li><a class="reference" href="#addressbook-framework" id="id4" name="id4">Addressbook framework</a></li>
<li><a class="reference" href="#appkit-framework" id="id5" name="id5">AppKit framework</a><ul>
<li><a class="reference" href="#class-nsapplication" id="id6" name="id6">Class NSApplication</a></li>
<li><a class="reference" href="#class-nsbezierpath" id="id7" name="id7">Class NSBezierPath</a></li>
<li><a class="reference" href="#class-nsbitmapimagerep" id="id8" name="id8">Class <tt class="docutils literal"><span class="pre">NSBitmapImageRep</span></tt></a></li>
<li><a class="reference" href="#class-nsfont" id="id9" name="id9">Class <tt class="docutils literal"><span class="pre">NSFont</span></tt></a></li>
<li><a class="reference" href="#class-nsgraphicscontext" id="id10" name="id10">Class <tt class="docutils literal"><span class="pre">NSGraphicsContext</span></tt></a></li>
<li><a class="reference" href="#class-nslayoutmanager" id="id11" name="id11">Class <tt class="docutils literal"><span class="pre">NSLayoutManager</span></tt></a></li>
<li><a class="reference" href="#class-nsmatrix" id="id12" name="id12">Class <tt class="docutils literal"><span class="pre">NSMatrix</span></tt></a></li>
<li><a class="reference" href="#class-nsmovie" id="id13" name="id13">Class <tt class="docutils literal"><span class="pre">NSMovie</span></tt></a></li>
<li><a class="reference" href="#class-nsopenglcontext" id="id14" name="id14">Class <tt class="docutils literal"><span class="pre">NSOpenGLContext</span></tt></a></li>
<li><a class="reference" href="#class-nsopenglpixelformat" id="id15" name="id15">Class <tt class="docutils literal"><span class="pre">NSOpenGLPixelFormat</span></tt></a></li>
<li><a class="reference" href="#class-nsquickdrawview" id="id16" name="id16">Class <tt class="docutils literal"><span class="pre">NSQuickDrawView</span></tt></a></li>
<li><a class="reference" href="#class-nssimplehorizontaltypesetter" id="id17" name="id17">Class <tt class="docutils literal"><span class="pre">NSSimpleHorizontalTypesetter</span></tt></a></li>
<li><a class="reference" href="#class-nsview" id="id18" name="id18">Class <tt class="docutils literal"><span class="pre">NSView</span></tt></a></li>
<li><a class="reference" href="#class-nswindow" id="id19" name="id19">Class <tt class="docutils literal"><span class="pre">NSWindow</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#foundation-framework" id="id20" name="id20">Foundation framework</a><ul>
<li><a class="reference" href="#class-nsarray" id="id21" name="id21">Class <tt class="docutils literal"><span class="pre">NSArray</span></tt></a></li>
<li><a class="reference" href="#class-nsautoreleasepool" id="id22" name="id22">Class <tt class="docutils literal"><span class="pre">NSAutoreleasePool</span></tt></a></li>
<li><a class="reference" href="#class-nscoder" id="id23" name="id23">Class <tt class="docutils literal"><span class="pre">NSCoder</span></tt></a></li>
<li><a class="reference" href="#class-nsdata" id="id24" name="id24">Class <tt class="docutils literal"><span class="pre">NSData</span></tt></a></li>
<li><a class="reference" href="#class-nsdecimalnumber-and-the-nsdecimal-type" id="id25" name="id25">Class <tt class="docutils literal"><span class="pre">NSDecimalNumber</span></tt> and the <tt class="docutils literal"><span class="pre">NSDecimal</span></tt> type</a></li>
<li><a class="reference" href="#class-nsdictionary" id="id26" name="id26">Class <tt class="docutils literal"><span class="pre">NSDictionary</span></tt></a></li>
<li><a class="reference" href="#class-nsexception" id="id27" name="id27">Class <tt class="docutils literal"><span class="pre">NSException</span></tt></a></li>
<li><a class="reference" href="#class-nsfault" id="id28" name="id28">Class <tt class="docutils literal"><span class="pre">NSFault</span></tt></a></li>
<li><a class="reference" href="#class-nsindexset" id="id29" name="id29">Class <tt class="docutils literal"><span class="pre">NSIndexSet</span></tt></a></li>
<li><a class="reference" href="#class-nsinvocation" id="id30" name="id30">Class <tt class="docutils literal"><span class="pre">NSInvocation</span></tt></a></li>
<li><a class="reference" href="#class-nsmutablearray" id="id31" name="id31">Class <tt class="docutils literal"><span class="pre">NSMutableArray</span></tt></a></li>
<li><a class="reference" href="#class-nsmutablestring" id="id32" name="id32">Class <tt class="docutils literal"><span class="pre">NSMutableString</span></tt></a></li>
<li><a class="reference" href="#class-nsnetservice" id="id33" name="id33">Class <tt class="docutils literal"><span class="pre">NSNetService</span></tt></a></li>
<li><a class="reference" href="#class-nsobject" id="id34" name="id34">Class <tt class="docutils literal"><span class="pre">NSObject</span></tt></a></li>
<li><a class="reference" href="#class-nsscriptobjectspecifier" id="id35" name="id35">Class <tt class="docutils literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></li>
<li><a class="reference" href="#class-nsstring" id="id36" name="id36">Class <tt class="docutils literal"><span class="pre">NSString</span></tt></a></li>
<li><a class="reference" href="#class-nsthread" id="id37" name="id37">class <tt class="docutils literal"><span class="pre">NSThread</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#interfacebuilder-framework" id="id38" name="id38">InterfaceBuilder framework</a><ul>
<li><a class="reference" href="#class-ibobjcsourceparser" id="id39" name="id39">Class <tt class="docutils literal"><span class="pre">IBObjCSourceParser</span></tt></a></li>
<li><a class="reference" href="#id1" id="id40" name="id40">Class <tt class="docutils literal"><span class="pre">NSView</span></tt></a></li>
<li><a class="reference" href="#class-nsibobjectdata" id="id41" name="id41">Class <tt class="docutils literal"><span class="pre">NSIBObjectData</span></tt></a></li>
<li><a class="reference" href="#class-ibobjectcontainer" id="id42" name="id42">Class <tt class="docutils literal"><span class="pre">IBObjectContainer</span></tt></a></li>
<li><a class="reference" href="#class-ibxmldecoder" id="id43" name="id43">Class <tt class="docutils literal"><span class="pre">IBXMLDecoder</span></tt></a></li>
<li><a class="reference" href="#class-ibsplitscrollview" id="id44" name="id44">Class <tt class="docutils literal"><span class="pre">IBSplitScrollView</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#preferencepanes-framework" id="id45" name="id45">PreferencePanes framework</a></li>
</ul>
</div>
<p>TODO: Add documentation about weak linking (see intro.txt).</p>
<div class="section" id="introduction">
<h3><a class="toc-backref" href="#id2" name="introduction">Introduction</a></h3>
<p>This document describes the restrictions with regard to supported APIs and
classes on Mac OS X.  In general, classes and global functions are used just
as they are in Objective-C (e.g. the Apple developer documentation applies),
but in some cases there are special considerations.</p>
<p>Global functions that are not useful for Python programs are not callable from
Python, as listed below.</p>
<p>This document lists the exceptions to the basic rules.  If a method uses pointers
to return additional values, the Python wrapper for that method returns a tuple
containing the original return value and the additional values.  It is not necessary
to provide values for pointer arguments unless their initial value is used by the
method.  Additionally, <tt class="docutils literal"><span class="pre">objc.NULL</span></tt> can be passed to denote that these arguments
should be <tt class="docutils literal"><span class="pre">NULL</span></tt> rather than a pointer to allocated memory.</p>
<p>This document is targeted at the latest supported version of Mac OS X (currently
Mac OS X 10.4.x).  Unless specifically noted, the same restrictions apply to 
earlier versions of Mac OS X.  Earlier versions of Mac OS X have less extensive
APIs, and PyObjC does <em>not</em> provide a compatibility layer except when necessary
to support its own operation.</p>
<p>This document is not entirely complete, but does cover the most used APIs.
Classes not mentioned in this document may very well work properly.</p>
<p>Frameworks that do not have PyObjC wrappers can be loaded at runtime using
the <tt class="docutils literal"><span class="pre">objc.loadBundle</span></tt>, <tt class="docutils literal"><span class="pre">objc.loadBundleFunctions</span></tt> and
<tt class="docutils literal"><span class="pre">objc.loadBundleVariables</span></tt> functions.  In a future version of PyObjC,
there will be an Objective-C header parser that can be used to automate this
process and to generate wrappers.</p>
</div>
<div class="section" id="core-objective-c-runtime">
<h3><a class="toc-backref" href="#id3" name="core-objective-c-runtime">Core Objective-C runtime</a></h3>
</div>
<div class="section" id="addressbook-framework">
<h3><a class="toc-backref" href="#id4" name="addressbook-framework">Addressbook framework</a></h3>
<p>The global functions in this framework are not wrapped, as the same 
functionality can be accessed by using the object-oriented interface.</p>
</div>
<div class="section" id="appkit-framework">
<h3><a class="toc-backref" href="#id5" name="appkit-framework">AppKit framework</a></h3>
<p>The callback methods for the <tt class="docutils literal"><span class="pre">NSSheet</span></tt> API's have a non-default signature
and no fixed name. You should therefore explicitly specify the signature. This
is done by calling the <tt class="docutils literal"><span class="pre">endSheetMethod</span></tt> function after defining your
callback:</p>
<pre class="literal-block">
class MyClass(NSObject):
        def mySheetDidEnd(self, panel, returnCode, contextInfo):
                &quot;&quot;&quot; Actual implementation goes here &quot;&quot;&quot;
                pass

        mySheetDidEnd = PyObjCTools.AppHelper.endSheetMethod(
                mySheetDidEnd)
</pre>
<p>In Python 2.4, this may be written using a decorator as such:</p>
<pre class="literal-block">
class MyClass(NSObject):
        &#64;PyObjCTools.AppHelper.endSheetMethod
        def mySheetDidEnd(self, panel, returnCode, contextInfo):
                &quot;&quot;&quot; Actual implementation goes here &quot;&quot;&quot;
                pass
</pre>
<p>Unless otherwise noted, all <tt class="docutils literal"><span class="pre">contextInfo</span></tt> arguments are passed as integers,
not as arbitrary pointers.</p>
<div class="section" id="class-nsapplication">
<h4><a class="toc-backref" href="#id6" name="class-nsapplication">Class NSApplication</a></h4>
<p><tt class="docutils literal"><span class="pre">NSModalSession</span></tt> objects are wrapped as opaque values.  Two wrapper objects
refer to the same session object if their <tt class="docutils literal"><span class="pre">ptr</span></tt> attributes are equal.</p>
</div>
<div class="section" id="class-nsbezierpath">
<h4><a class="toc-backref" href="#id7" name="class-nsbezierpath">Class NSBezierPath</a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getLineDash:count:phase:</span></tt></p>
<p>Use <tt class="docutils literal"><span class="pre">getLineDash_count_phase_(0)</span></tt> to get the length of the pattern, and
then use <tt class="docutils literal"><span class="pre">getLineDash_count_phase_(actualCount)</span></tt> to fetch all information.
Both return <tt class="docutils literal"><span class="pre">(pattern,</span> <span class="pre">actualCount,</span> <span class="pre">phase)</span></tt>. The <tt class="docutils literal"><span class="pre">pattern</span></tt> is <tt class="docutils literal"><span class="pre">None</span></tt>
when the input argument is <tt class="docutils literal"><span class="pre">0</span></tt>.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">appendBezierPathWithGlyphs:count:inFont:</span></tt></p>
<p>The first argument is a list of integers, count should be at most the length
of the first argument.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">appendBezierPathWithPoints:count:</span></tt></p>
<p>The first argument is a list of points, count should be at most the length
of the first argument.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">setAssociatedPoints:atIndex:</span></tt></p>
<p>Implementing this method in Python is not yet supported.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsbitmapimagerep">
<h4><a class="toc-backref" href="#id8" name="class-nsbitmapimagerep">Class <tt class="docutils literal docutils literal"><span class="pre">NSBitmapImageRep</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getBitMapDataPlanes</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getTIFFCompressionTypes:count:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithBitmapDataPlanes:pixesWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
</ul>
</div>
<div class="section" id="class-nsfont">
<h4><a class="toc-backref" href="#id9" name="class-nsfont">Class <tt class="docutils literal docutils literal"><span class="pre">NSFont</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">positionsForCompositeSequence:numberOfGlyphs:pointArray:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
</ul>
</div>
<div class="section" id="class-nsgraphicscontext">
<h4><a class="toc-backref" href="#id10" name="class-nsgraphicscontext">Class <tt class="docutils literal docutils literal"><span class="pre">NSGraphicsContext</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">focusStack</span></tt></p>
<p>This method is not supported.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">setFocusStack</span></tt></p>
<p>This method is not supported.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">graphicsPort</span></tt></p>
<p>This method is not yet supported, MacPython doesn't wrap <tt class="docutils literal"><span class="pre">CGContextRef</span></tt>
at the moment.</p>
</li>
</ul>
</div>
<div class="section" id="class-nslayoutmanager">
<h4><a class="toc-backref" href="#id11" name="class-nslayoutmanager">Class <tt class="docutils literal docutils literal"><span class="pre">NSLayoutManager</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getGlyphs:range:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">rectArrayForCharacterRange:withinSelectedCharacterRange:inTextContainer:rectCount:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">rectArrayForGlyphRange:withinSelectedGlyphRange:inTextContainer:rectCount:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmatrix">
<h4><a class="toc-backref" href="#id12" name="class-nsmatrix">Class <tt class="docutils literal docutils literal"><span class="pre">NSMatrix</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">sortUsingFunction:context:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in Python
is not. The <tt class="docutils literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmovie">
<h4><a class="toc-backref" href="#id13" name="class-nsmovie">Class <tt class="docutils literal docutils literal"><span class="pre">NSMovie</span></tt></a></h4>
<p>The return value of <tt class="docutils literal"><span class="pre">QTMovie</span></tt> and the sole argument of <tt class="docutils literal"><span class="pre">initWithMovie:</span></tt>
are <tt class="docutils literal"><span class="pre">Carbon.Qt.Movie</span></tt> objects.</p>
</div>
<div class="section" id="class-nsopenglcontext">
<h4><a class="toc-backref" href="#id14" name="class-nsopenglcontext">Class <tt class="docutils literal docutils literal"><span class="pre">NSOpenGLContext</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getValues:forParameter:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">setValues:forParameter:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">setOffScreen:width:height:rowbytes:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">CGLContextObj</span></tt></p>
<p>This method is not yet supported.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsopenglpixelformat">
<h4><a class="toc-backref" href="#id15" name="class-nsopenglpixelformat">Class <tt class="docutils literal docutils literal"><span class="pre">NSOpenGLPixelFormat</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getValues:forAttribute:forVirtualScreen:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsquickdrawview">
<h4><a class="toc-backref" href="#id16" name="class-nsquickdrawview">Class <tt class="docutils literal docutils literal"><span class="pre">NSQuickDrawView</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">qdPort</span></tt></p>
<p>This method returns an instance of type <tt class="docutils literal"><span class="pre">Carbon.Qd.GrafPort</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nssimplehorizontaltypesetter">
<h4><a class="toc-backref" href="#id17" name="class-nssimplehorizontaltypesetter">Class <tt class="docutils literal docutils literal"><span class="pre">NSSimpleHorizontalTypesetter</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">baseOfTypesetterGlyphInfo</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">layoutGlyphsInHorizontalLineFragment:baseline:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsview">
<h4><a class="toc-backref" href="#id18" name="class-nsview">Class <tt class="docutils literal docutils literal"><span class="pre">NSView</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">sortSubviewsUsingFunction:context:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in Python
is not. The <tt class="docutils literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nswindow">
<h4><a class="toc-backref" href="#id19" name="class-nswindow">Class <tt class="docutils literal docutils literal"><span class="pre">NSWindow</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">graphicsPort</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithWindowRef:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">windowRef</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
</div>
<div class="section" id="foundation-framework">
<h3><a class="toc-backref" href="#id20" name="foundation-framework">Foundation framework</a></h3>
<p>NOTE: The list below is mostly based on scripts that find methods that can
not be automatically handled by the bridge. We have not yet performed a manual
search for such methods in the Cocoa documentation.</p>
<p>The <tt class="docutils literal"><span class="pre">-forward::</span></tt> and <tt class="docutils literal"><span class="pre">performv::</span></tt> methods are not supported.  Normal Python
function invocation can be used instead.</p>
<p>Structs are wrapped using a struct-like type.  Struct members can be accessed
using the field names as attributes, or they can be accessed as sequences for
backwards compatibility.</p>
<div class="section" id="class-nsarray">
<h4><a class="toc-backref" href="#id21" name="class-nsarray">Class <tt class="docutils literal docutils literal"><span class="pre">NSArray</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getObjects:</span></tt></p>
<p>This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getObjects:inRange:</span></tt></p>
<p>This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">sortedArrayUsingFunction:context:</span></tt> and <tt class="docutils literal"><span class="pre">sortedArrayUsingFunction:context:hint</span></tt></p>
<p>These methods can be called from Python, but Python can not override them.
This limitation will be lifted in a future version of PyObjC.</p>
<p>The <tt class="docutils literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">addObserver:toObjectsAtIndexes:forKeyPath:options:context:</span></tt></p>
<p>The context is an integer, not a <tt class="docutils literal"><span class="pre">void*</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsautoreleasepool">
<h4><a class="toc-backref" href="#id22" name="class-nsautoreleasepool">Class <tt class="docutils literal docutils literal"><span class="pre">NSAutoreleasePool</span></tt></a></h4>
<p>The bridge automatically manages reference counts for you, but it is still 
required to make an autorelease pool available.</p>
<p>In single-threaded programs that use <tt class="docutils literal"><span class="pre">NSRunLoop</span></tt> or are not long-lived,
it is not necessary to explicitly manage <tt class="docutils literal"><span class="pre">NSAutoreleasePool</span></tt>, as
<tt class="docutils literal"><span class="pre">NSRunLoop</span></tt> will push and pop one for each iteration, and PyObjC creates
a <tt class="docutils literal"><span class="pre">NSAutoreleasePool</span></tt> in the thread it is imported in.</p>
<p>When creating a large amount of objects in a loop, it may be useful to
manually create a pool to reclaim memory as soon as possible. The proper
idiom for this is:</p>
<pre class="literal-block">
while &lt;test&gt;:
        pool = NSAutoreleasePool.alloc().init()

        # ... Do work here ...

        del pool
</pre>
<p>The previous pool <em>must</em> be deallocated before a new one is
created.  For example, the code below will <em>silently leak memory</em>:</p>
<pre class="literal-block">
while &lt;test&gt;:
        # This pool is allocated BEFORE the previous is
        # garbage collected, so the stack grows!
        pool = NSAutoreleasePool.alloc().init()

        # ... Do work here ...
</pre>
<p>In threads other than the main thread, as with Objective-C applications, it
is necessary to create an <tt class="docutils literal"><span class="pre">NSAutoreleasePool</span></tt> as soon as possible before
using other Objective-C objects.</p>
</div>
<div class="section" id="class-nscoder">
<h4><a class="toc-backref" href="#id23" name="class-nscoder">Class <tt class="docutils literal docutils literal"><span class="pre">NSCoder</span></tt></a></h4>
<p>The following methods are not supported in the current version of PyObjC.
This limitation will be lifted in a future version of the bridge.</p>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">encodeValuesOfObjCType:</span></tt></p>
<p>Use multiple calls to <tt class="docutils literal"><span class="pre">encodeValueOfObjCType:at:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">decodeValuesOfObjCType:</span></tt></p>
<p>Use multiple calls to <tt class="docutils literal"><span class="pre">decodeValueOfObjCType:at:</span></tt> instead.
Note that this will not read back data that was written using
<tt class="docutils literal"><span class="pre">encodeValuesOfObjCType:</span></tt>.</p>
</li>
</ul>
<p>The method <tt class="docutils literal"><span class="pre">decodeBytesWithoutReturnedLength:</span></tt> is not supported, use 
<tt class="docutils literal"><span class="pre">decodeBytesWithReturnedLength:</span></tt> instead.  It is not possible to safely
represent the return value of this method in Python.</p>
</div>
<div class="section" id="class-nsdata">
<h4><a class="toc-backref" href="#id24" name="class-nsdata">Class <tt class="docutils literal docutils literal"><span class="pre">NSData</span></tt></a></h4>
<p>NSData subclasses support the Python buffer protocol, and any Python
object that implements the Python buffer protocol (except str and unicode)
are wrapped as an NSData subclass.</p>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithBytesNoCopy:length:</span></tt></p>
<p>This method is not supported, use <tt class="docutils literal"><span class="pre">initWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithBytesNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is not supported, use <tt class="docutils literal"><span class="pre">initWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">dataWithBytesNoCopy:length:</span></tt></p>
<p>This method is not supported, use <tt class="docutils literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">dataWithBytesNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is not supported, use <tt class="docutils literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeAlignedBytesLengthAtCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeBytes:length:atCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeDataAt:ofObjCType:atCursor:context:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeIntAtCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeInts:count:atCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">deserializeInts:count:atIndex:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getBytes:</span></tt>, <tt class="docutils literal"><span class="pre">getBytes:length:</span></tt>, <tt class="docutils literal"><span class="pre">getBytes:range:</span></tt></p>
<p>Use <tt class="docutils literal"><span class="pre">bytes</span></tt> instead, and then use subscripting to get the
desired range.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsdecimalnumber-and-the-nsdecimal-type">
<h4><a class="toc-backref" href="#id25" name="class-nsdecimalnumber-and-the-nsdecimal-type">Class <tt class="docutils literal docutils literal"><span class="pre">NSDecimalNumber</span></tt> and the <tt class="docutils literal docutils literal"><span class="pre">NSDecimal</span></tt> type</a></h4>
<p>NSDecimal is wrapped by a Python type.</p>
<p>Creating an <tt class="docutils literal"><span class="pre">NSDecimal</span></tt> instance: <tt class="docutils literal"><span class="pre">NSDecimal(value)</span></tt> or 
<tt class="docutils literal"><span class="pre">NSDecimal(mantisssa,</span> <span class="pre">exponent,</span> <span class="pre">isNegative)</span></tt>.  <tt class="docutils literal"><span class="pre">Value</span></tt> can be a string,
int or long (not a float because of the representation issues for floats).</p>
<p>Converting an <tt class="docutils literal"><span class="pre">NSDecimal</span></tt> to a float or int: <tt class="docutils literal"><span class="pre">aDecimal.as_int()</span></tt> and
<tt class="docutils literal"><span class="pre">aDecimal.as_float</span></tt>.</p>
</div>
<div class="section" id="class-nsdictionary">
<h4><a class="toc-backref" href="#id26" name="class-nsdictionary">Class <tt class="docutils literal docutils literal"><span class="pre">NSDictionary</span></tt></a></h4>
<p>The (undocumented) methods <tt class="docutils literal"><span class="pre">getKeys:</span></tt>, <tt class="docutils literal"><span class="pre">getObjects:</span></tt> and 
<tt class="docutils literal"><span class="pre">getObjects:andKeys:</span></tt> are not supported.</p>
</div>
<div class="section" id="class-nsexception">
<h4><a class="toc-backref" href="#id27" name="class-nsexception">Class <tt class="docutils literal docutils literal"><span class="pre">NSException</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">raise:format:</span></tt>, <tt class="docutils literal"><span class="pre">raise:format:arguments:</span></tt></p>
<p>These methods are not supported because they accept a variable number of
arguments.  Use Python's <tt class="docutils literal"><span class="pre">%</span></tt> operator to format the message.  A future
version of PyObjC may be able to parse format strings and do the right
thing.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsfault">
<h4><a class="toc-backref" href="#id28" name="class-nsfault">Class <tt class="docutils literal docutils literal"><span class="pre">NSFault</span></tt></a></h4>
<p>The <tt class="docutils literal"><span class="pre">extraData</span></tt> argument/return value for <tt class="docutils literal"><span class="pre">-extraData</span></tt> and 
<tt class="docutils literal"><span class="pre">setTargetClassextraData:</span></tt> is represented as an integer.</p>
</div>
<div class="section" id="class-nsindexset">
<h4><a class="toc-backref" href="#id29" name="class-nsindexset">Class <tt class="docutils literal docutils literal"><span class="pre">NSIndexSet</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">getIndexes:maxCount:inIndexRange:</span></tt>
The usage is:</p>
<pre class="literal-block">
(realCount, indices, newRange) = obj.getIndexes_maxCount_inIndexRange(
        maxCount, inRange)              
</pre>
</li>
</ul>
</div>
<div class="section" id="class-nsinvocation">
<h4><a class="toc-backref" href="#id30" name="class-nsinvocation">Class <tt class="docutils literal docutils literal"><span class="pre">NSInvocation</span></tt></a></h4>
<p>In some versions of Mac OS X, <tt class="docutils literal"><span class="pre">NSInvocation</span></tt> doesn't work properly with structs
that contain padding for alignment.  Such structs are not used in the Mac OS X API,
but may be present in 3rd party code.  This leads to problems when
<tt class="docutils literal"><span class="pre">forwardInvocation:</span></tt> is used to call a method that has such a struct as one of
its arguments.</p>
</div>
<div class="section" id="class-nsmutablearray">
<h4><a class="toc-backref" href="#id31" name="class-nsmutablearray">Class <tt class="docutils literal docutils literal"><span class="pre">NSMutableArray</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">sortUsingFunction:context:</span></tt>, <tt class="docutils literal"><span class="pre">sortUsingFunction:context:range:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in a subclass
is not.  This limitation will be fixed in a later version of PyObjC.</p>
<p>The <tt class="docutils literal"><span class="pre">context</span></tt> can be an arbitrary Python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmutablestring">
<h4><a class="toc-backref" href="#id32" name="class-nsmutablestring">Class <tt class="docutils literal docutils literal"><span class="pre">NSMutableString</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">appendFormat:</span></tt></p>
<p>This method is not supported because it accepts a variable number of 
arguments. Use Python's <tt class="docutils literal"><span class="pre">%</span></tt> operator to format strings.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsnetservice">
<h4><a class="toc-backref" href="#id33" name="class-nsnetservice">Class <tt class="docutils literal docutils literal"><span class="pre">NSNetService</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">addresses</span></tt></p>
<p>When calling this from Python this methods returns a tuple of address info
tuples, like the values returned by <tt class="docutils literal"><span class="pre">socket.getpeeraddr()</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsobject">
<h4><a class="toc-backref" href="#id34" name="class-nsobject">Class <tt class="docutils literal docutils literal"><span class="pre">NSObject</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">observationInfo</span></tt>, <tt class="docutils literal"><span class="pre">setObservationInfo:</span></tt></p>
<p>These methods can be used from Python, but the <tt class="docutils literal"><span class="pre">observationInfo</span></tt> is 
represented by an integer instead of <tt class="docutils literal"><span class="pre">void*</span></tt>. This probably makes it
impossible to do anything useful with these methods.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">addObserver:forKeyPath:options:context:</span></tt></p>
<p>The context is an integer.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">observeValueForKeyPath:ofObject:change:context:</span></tt></p>
<p>The context is an integer</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">methodForSelector:</span></tt>, <tt class="docutils literal"><span class="pre">instanceMethodForSelector:</span></tt></p>
<p>These methods return instances of <tt class="docutils literal"><span class="pre">objc.IMP</span></tt>.  The major difference from
Objective-C is that the selector argument is omitted.  In other words,
using an <tt class="docutils literal"><span class="pre">objc.IMP</span></tt> is the same as using an unbound selector; <tt class="docutils literal"><span class="pre">self</span></tt>
must be passed explicitly as the first argument, and the other arguments
are passed as usual.</p>
<p>WARNING: This interface is experimental and might change in a future version
of PyObjC.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsscriptobjectspecifier">
<h4><a class="toc-backref" href="#id35" name="class-nsscriptobjectspecifier">Class <tt class="docutils literal docutils literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">indicesOfObjectsByEvaluatingWithContainer:count:</span></tt></p>
<p>Implementing this in Python is not supported yet. We're looking for a way
to avoid leaking the returned buffer, as we cannot return a pointer to an
internal data-structure.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsstring">
<h4><a class="toc-backref" href="#id36" name="class-nsstring">Class <tt class="docutils literal docutils literal"><span class="pre">NSString</span></tt></a></h4>
<p>Objective-C strings are represented as instances of a subclass of
the Python type <tt class="docutils literal"><span class="pre">unicode</span></tt>.  Since Python <tt class="docutils literal"><span class="pre">unicode</span></tt> objects are immutable,
working with <tt class="docutils literal"><span class="pre">NSMutableString</span></tt> can be tricky.  If you need to update the
Python representation of the string, use <tt class="docutils literal"><span class="pre">aString.self()</span></tt>, which will be a
new Python proxy for the same <tt class="docutils literal"><span class="pre">NSMutableString</span></tt> instance.</p>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithCharactersNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is unsupported because we can not guarantee that the buffer will
be available as long as the string is. Use <tt class="docutils literal"><span class="pre">initWithCharacters:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getCharacters:</span></tt> and <tt class="docutils literal"><span class="pre">getCharacters:range:</span></tt></p>
<p>These methods are not supported at the moment.  This limitation will be lifted
in a future version of the bridge.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getCString:maxLength:range:remainingRange:</span></tt> and <tt class="docutils literal"><span class="pre">getCString:maxLength:</span></tt></p>
<p>Calling these methods from Python is supported, overriding them from 
Python is not. This limitation will be lifted in a future version of the
bridge.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">getCString:</span></tt></p>
<p>This method is not supported. Use <tt class="docutils literal"><span class="pre">getCString:maxLength:</span></tt> instead (using
the length of the string as the maximum length).  This limitation will be
lifted in a future version of the bridge.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">stringWithFormat:</span></tt>, <tt class="docutils literal"><span class="pre">initWithFormat:</span></tt>, <tt class="docutils literal"><span class="pre">initWithFormat:locale:</span></tt>,
<tt class="docutils literal"><span class="pre">stringByAppendingFormat:</span></tt></p>
<p>These methods are not supported because they accept a variable number of 
arbitrarily typed arguments.  Use Python's <tt class="docutils literal"><span class="pre">%</span></tt> operator to format strings.
A future version of PyObjC may be able to parse format strings and do the
right thing here.</p>
</li>
<li><p class="first"><tt class="docutils literal"><span class="pre">initWithFormat:arguments:</span></tt>, <tt class="docutils literal"><span class="pre">initWithFormat:locale:arguments:</span></tt></p>
<p>These are also not supported, with the same workaround.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsthread">
<h4><a class="toc-backref" href="#id37" name="class-nsthread">class <tt class="docutils literal docutils literal"><span class="pre">NSThread</span></tt></a></h4>
<p>It is safe to call from Objective-C to Python on any thread.  It is safe to
start new threads using the Python threading API and run non-Cocoa code on
those threads.</p>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">detachNewThreadSelector:toTarget:withObject:</span></tt></p>
<p>As with Objective-C, make sure to create an <tt class="docutils literal"><span class="pre">NSAutoreleasePool</span></tt> in this
the detached thread.</p>
</li>
</ul>
</div>
</div>
<div class="section" id="interfacebuilder-framework">
<h3><a class="toc-backref" href="#id38" name="interfacebuilder-framework">InterfaceBuilder framework</a></h3>
<p>I (Ronald) have not found documentation for this framework, therefore the
following methods with a &quot;difficult&quot; signature are not supported.</p>
<p>Please let me know if there is documentation for this framework.</p>
<div class="section" id="class-ibobjcsourceparser">
<h4><a class="toc-backref" href="#id39" name="class-ibobjcsourceparser">Class <tt class="docutils literal docutils literal"><span class="pre">IBObjCSourceParser</span></tt></a></h4>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">parseClass:</span></tt></li>
</ul>
</div>
<div class="section" id="id1">
<h4><a class="toc-backref" href="#id40" name="id1">Class <tt class="docutils literal docutils literal"><span class="pre">NSView</span></tt></a></h4>
<ul>
<li><p class="first"><tt class="docutils literal"><span class="pre">objectAtPoint:rect:</span></tt></p>
<p>Defined in a category on <tt class="docutils literal"><span class="pre">NSView</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsibobjectdata">
<h4><a class="toc-backref" href="#id41" name="class-nsibobjectdata">Class <tt class="docutils literal docutils literal"><span class="pre">NSIBObjectData</span></tt></a></h4>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">restoreFromObjectDataInfo:</span></tt></li>
<li><tt class="docutils literal"><span class="pre">snapshotIntoObjectDataInfo:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibobjectcontainer">
<h4><a class="toc-backref" href="#id42" name="class-ibobjectcontainer">Class <tt class="docutils literal docutils literal"><span class="pre">IBObjectContainer</span></tt></a></h4>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">decodeObjectToIntMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
<li><tt class="docutils literal"><span class="pre">decodeObjectToObjectMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibxmldecoder">
<h4><a class="toc-backref" href="#id43" name="class-ibxmldecoder">Class <tt class="docutils literal docutils literal"><span class="pre">IBXMLDecoder</span></tt></a></h4>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">allocObjectWithClassName:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibsplitscrollview">
<h4><a class="toc-backref" href="#id44" name="class-ibsplitscrollview">Class <tt class="docutils literal docutils literal"><span class="pre">IBSplitScrollView</span></tt></a></h4>
<ul class="simple">
<li><tt class="docutils literal"><span class="pre">getMinimumX:maximumX:</span></tt></li>
</ul>
</div>
</div>
<div class="section" id="preferencepanes-framework">
<h3><a class="toc-backref" href="#id45" name="preferencepanes-framework">PreferencePanes framework</a></h3>
<p>This framework seems to define useful classes like <tt class="docutils literal"><span class="pre">NSAuthorization</span></tt> and
<tt class="docutils literal"><span class="pre">NSKeychain</span></tt>, but these are not documented and some useful methods have
a hard signature.</p>
<p>The only documented class, <tt class="docutils literal"><span class="pre">NSPreferencePane</span></tt>, is fully supported.</p>
</div>
</div>
<?
    include "footer.inc";
?>