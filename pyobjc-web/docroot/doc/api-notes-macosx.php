<?
    $title = "Notes on supported APIs and classes on Mac OS X";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<div class="document" id="notes-on-supported-apis-and-classes-on-mac-os-x">
<!-- :author: Ronald Oussoren -->
<div class="contents topic" id="contents">
<p class="topic-title first"><a name="contents">Contents</a></p>
<ul class="simple">
<li><a class="reference" href="#introduction" id="id2" name="id2">Introduction</a></li>
<li><a class="reference" href="#core-objective-c-runtime" id="id3" name="id3">Core objective-C runtime</a><ul>
<li><a class="reference" href="#class-protocol" id="id4" name="id4">Class Protocol</a></li>
</ul>
</li>
<li><a class="reference" href="#addressbook-framework" id="id5" name="id5">Addressbook framework</a></li>
<li><a class="reference" href="#appkit-framework" id="id6" name="id6">AppKit framework</a><ul>
<li><a class="reference" href="#class-nsapplication" id="id7" name="id7">Class NSApplication</a></li>
<li><a class="reference" href="#class-nsbezierpath" id="id8" name="id8">Class NSBezierPath</a></li>
<li><a class="reference" href="#class-nsbitmapimagerep" id="id9" name="id9">Class <tt class="literal"><span class="pre">NSBitmapImageRep</span></tt></a></li>
<li><a class="reference" href="#class-nsfont" id="id10" name="id10">Class <tt class="literal"><span class="pre">NSFont</span></tt></a></li>
<li><a class="reference" href="#class-nsgraphicscontext" id="id11" name="id11">Class <tt class="literal"><span class="pre">NSGraphicsContext</span></tt></a></li>
<li><a class="reference" href="#class-nslayoutmanager" id="id12" name="id12">Class <tt class="literal"><span class="pre">NSLayoutManager</span></tt></a></li>
<li><a class="reference" href="#class-nsmatrix" id="id13" name="id13">Class <tt class="literal"><span class="pre">NSMatrix</span></tt></a></li>
<li><a class="reference" href="#class-nsmovie" id="id14" name="id14">Class <tt class="literal"><span class="pre">NSMovie</span></tt></a></li>
<li><a class="reference" href="#class-nsopenglcontext" id="id15" name="id15">Class <tt class="literal"><span class="pre">NSOpenGLContext</span></tt></a></li>
<li><a class="reference" href="#class-nsopenglpixelformat" id="id16" name="id16">Class <tt class="literal"><span class="pre">NSOpenGLPixelFormat</span></tt></a></li>
<li><a class="reference" href="#class-nsquickdrawview" id="id17" name="id17">Class <tt class="literal"><span class="pre">NSQuickDrawView</span></tt></a></li>
<li><a class="reference" href="#class-nssimplehorizontaltypesetter" id="id18" name="id18">Class <tt class="literal"><span class="pre">NSSimpleHorizontalTypesetter</span></tt></a></li>
<li><a class="reference" href="#class-nsview" id="id19" name="id19">Class <tt class="literal"><span class="pre">NSView</span></tt></a></li>
<li><a class="reference" href="#class-nswindow" id="id20" name="id20">Class <tt class="literal"><span class="pre">NSWindow</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#foundation-framework" id="id21" name="id21">Foundation framework</a><ul>
<li><a class="reference" href="#class-nsarray" id="id22" name="id22">Class <tt class="literal"><span class="pre">NSArray</span></tt></a></li>
<li><a class="reference" href="#class-nsautoreleasepool" id="id23" name="id23">Class <tt class="literal"><span class="pre">NSAutoreleasePool</span></tt></a></li>
<li><a class="reference" href="#class-nsbundle" id="id24" name="id24">Class <tt class="literal"><span class="pre">NSBundle</span></tt></a></li>
<li><a class="reference" href="#class-nscoder" id="id25" name="id25">Class <tt class="literal"><span class="pre">NSCoder</span></tt></a></li>
<li><a class="reference" href="#class-nsdata" id="id26" name="id26">Class <tt class="literal"><span class="pre">NSData</span></tt></a></li>
<li><a class="reference" href="#class-nsdecimalnumber-and-the-nsdecimal-type" id="id27" name="id27">Class <tt class="literal"><span class="pre">NSDecimalNumber</span></tt> and the <tt class="literal"><span class="pre">NSDecimal</span></tt> type</a></li>
<li><a class="reference" href="#class-nsdictionary" id="id28" name="id28">Class <tt class="literal"><span class="pre">NSDictionary</span></tt></a></li>
<li><a class="reference" href="#class-nsexception" id="id29" name="id29">Class <tt class="literal"><span class="pre">NSException</span></tt></a></li>
<li><a class="reference" href="#class-nsfault" id="id30" name="id30">Class <tt class="literal"><span class="pre">NSFault</span></tt></a></li>
<li><a class="reference" href="#class-nsindexset" id="id31" name="id31">Class <tt class="literal"><span class="pre">NSIndexSet</span></tt></a></li>
<li><a class="reference" href="#class-nsinvocation" id="id32" name="id32">Class <tt class="literal"><span class="pre">NSInvocation</span></tt></a></li>
<li><a class="reference" href="#class-nsmutablearray" id="id33" name="id33">Class <tt class="literal"><span class="pre">NSMutableArray</span></tt></a></li>
<li><a class="reference" href="#class-nsmutablestring" id="id34" name="id34">Class <tt class="literal"><span class="pre">NSMutableString</span></tt></a></li>
<li><a class="reference" href="#class-nsnetservice" id="id35" name="id35">Class <tt class="literal"><span class="pre">NSNetService</span></tt></a></li>
<li><a class="reference" href="#class-nsobject" id="id36" name="id36">Class <tt class="literal"><span class="pre">NSObject</span></tt></a></li>
<li><a class="reference" href="#class-nsscriptobjectspecifier" id="id37" name="id37">Class <tt class="literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></li>
<li><a class="reference" href="#class-nsset" id="id38" name="id38">Class <tt class="literal"><span class="pre">NSSet</span></tt></a></li>
<li><a class="reference" href="#class-nsstring" id="id39" name="id39">Class <tt class="literal"><span class="pre">NSString</span></tt></a></li>
<li><a class="reference" href="#class-nsthread" id="id40" name="id40">class <tt class="literal"><span class="pre">NSThread</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#interfacebuilder-framework" id="id41" name="id41">InterfaceBuilder framework</a><ul>
<li><a class="reference" href="#class-ibobjcsourceparser" id="id42" name="id42">Class <tt class="literal"><span class="pre">IBObjCSourceParser</span></tt></a></li>
<li><a class="reference" href="#id1" id="id43" name="id43">Class <tt class="literal"><span class="pre">NSView</span></tt></a></li>
<li><a class="reference" href="#class-nsibobjectdata" id="id44" name="id44">Class <tt class="literal"><span class="pre">NSIBObjectData</span></tt></a></li>
<li><a class="reference" href="#class-ibobjectcontainer" id="id45" name="id45">Class <tt class="literal"><span class="pre">IBObjectContainer</span></tt></a></li>
<li><a class="reference" href="#class-ibxmldecoder" id="id46" name="id46">Class <tt class="literal"><span class="pre">IBXMLDecoder</span></tt></a></li>
<li><a class="reference" href="#class-ibsplitscrollview" id="id47" name="id47">Class <tt class="literal"><span class="pre">IBSplitScrollView</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#preferencepanes-framework" id="id48" name="id48">PreferencePanes framework</a></li>
<li><a class="reference" href="#screensaver-framework" id="id49" name="id49">ScreenSaver framework</a><ul>
<li><a class="reference" href="#class-screensaverdefaults" id="id50" name="id50">Class <tt class="literal"><span class="pre">ScreenSaverDefaults</span></tt></a></li>
<li><a class="reference" href="#class-screensaverview" id="id51" name="id51">Class <tt class="literal"><span class="pre">ScreenSaverView</span></tt></a></li>
</ul>
</li>
</ul>
</div>
<p>TODO: Add documentation about weak linking (see intro.txt).</p>
<div class="section" id="introduction">
<h1><a class="toc-backref" href="#id2" name="introduction">Introduction</a></h1>
<p>This document describes the restrictions w.r.t. supported APIs and classes
on Mac OS X. In general you can use classes and global functions just like
in Objective-C (e.g. the Apple developer documentation applies), but in some
cases there are special considerations.</p>
<p>We also do not provide access to global functions that are not useful for
Python programs, those functions are listed below.</p>
<p>This document lists the exceptions to the basic rules. If a method uses pointers
to return additional values, the Python wrapper for that method returns a tuple
containing the original return value and the additional values. You don't have
to pass values for those arguments, unless the method uses the values you
pass in.</p>
<p>This document is targeted at the latest supported version of Mac OS X (currently
Mac OS X 10.3.x); unless specifically noted the same restrictions apply to 
earlier versions of Mac OS X. Earlier versions of the OS have less extensive
APIs, PyObjC does <em>not</em> provide a compatibility layer.</p>
<p>Frameworks not listed below are not wrapped by PyObjC, they can still be
accessed although without access to constants and global functions defined
by those frameworks.</p>
<p>This document is not entirely complete, but does cover the most used APIs.</p>
</div>
<div class="section" id="core-objective-c-runtime">
<h1><a class="toc-backref" href="#id3" name="core-objective-c-runtime">Core objective-C runtime</a></h1>
<div class="section" id="class-protocol">
<h2><a class="toc-backref" href="#id4" name="class-protocol">Class Protocol</a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">descriptionForClassMethod:</span></tt>, <tt class="literal"><span class="pre">descriptionForInstanceMethod</span></tt></p>
<p>These methods are not supported. Protocols are hardly ever used explicitly
in Cocoa therefore this should not be a problem.</p>
</li>
</ul>
</div>
</div>
<div class="section" id="addressbook-framework">
<h1><a class="toc-backref" href="#id5" name="addressbook-framework">Addressbook framework</a></h1>
<p>We do not provide access to the global functions in this framework, because
the same functionality can be accessed by using the object-oriented interface.</p>
</div>
<div class="section" id="appkit-framework">
<h1><a class="toc-backref" href="#id6" name="appkit-framework">AppKit framework</a></h1>
<p>The callback methods for the NSSheet API's have a non-default signature
and no fixed name. You should therefore explicitly specify the signature. This
is done by calling the <tt class="literal"><span class="pre">endSheetMethod</span></tt> function after defining your
callback:</p>
<pre class="literal-block">
class MYClass (NSObject):
        def mysheetDidEnd(self, panel, returnCode, contextInfo):
                &quot;&quot;&quot; Actual implementation goes here &quot;&quot;&quot;
                pass

        mysheetDidEnd = PyObjCTools.AppHelper.endSheetMethod(
                mysheetDidEnd)
</pre>
<p>Unless otherwise noted, all <tt class="literal"><span class="pre">contextInfo</span></tt> arguments are passed as integers,
not as arbitrary pointers.</p>
<div class="section" id="class-nsapplication">
<h2><a class="toc-backref" href="#id7" name="class-nsapplication">Class NSApplication</a></h2>
<p><tt class="literal"><span class="pre">NSModalSession</span></tt> objects are wrapped as opaque values. You can check if
two wrapper objects refer to the same session object by comparing their
<tt class="literal"><span class="pre">ptr</span></tt> attributes.</p>
</div>
<div class="section" id="class-nsbezierpath">
<h2><a class="toc-backref" href="#id8" name="class-nsbezierpath">Class NSBezierPath</a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getLineDash:count:phase:</span></tt></p>
<p>Use <tt class="literal"><span class="pre">getLineDash_count_phase_(0)</span></tt> to get the length of the pattern, and
then use <tt class="literal"><span class="pre">getLineDash_count_phase_(actualCount)</span></tt> to fetch all information.
Both return <tt class="literal"><span class="pre">(pattern,</span> <span class="pre">actualCount,</span> <span class="pre">phase)</span></tt>. The <tt class="literal"><span class="pre">pattern</span></tt> is <tt class="literal"><span class="pre">None</span></tt>
when the input argument is <tt class="literal"><span class="pre">0</span></tt>.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">appendBezierPathWithGlyphs:count:inFont:</span></tt></p>
<p>The first argument is a list of integers, count should be at most the length
of the first argument.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">appendBezierPathWithPoints:count:</span></tt></p>
<p>The first argument is a list of points, count should be at most the length
of the first argument.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setAssociatedPoints:atIndex:</span></tt></p>
<p>Implementing this method in Python is not yet supported.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsbitmapimagerep">
<h2><a class="toc-backref" href="#id9" name="class-nsbitmapimagerep">Class <tt class="literal"><span class="pre">NSBitmapImageRep</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getBitMapDataPlanes</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getTIFFCompressionTypes:count:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">initWithBitmapDataPlanes:pixesWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
</ul>
</div>
<div class="section" id="class-nsfont">
<h2><a class="toc-backref" href="#id10" name="class-nsfont">Class <tt class="literal"><span class="pre">NSFont</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">positionsForCompositeSequence:numberOfGlyphs:pointArray:</span></tt></p>
<p>This method is not supported (yet)</p>
</li>
</ul>
</div>
<div class="section" id="class-nsgraphicscontext">
<h2><a class="toc-backref" href="#id11" name="class-nsgraphicscontext">Class <tt class="literal"><span class="pre">NSGraphicsContext</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">focusStack</span></tt></p>
<p>This method is not supported.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setFocusStack</span></tt></p>
<p>This method is not supported.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">graphicsPort</span></tt></p>
<p>This method is not yet supported, MacPython doesn't wrap <tt class="literal"><span class="pre">CGContextRef</span></tt>
at the moment.</p>
</li>
</ul>
</div>
<div class="section" id="class-nslayoutmanager">
<h2><a class="toc-backref" href="#id12" name="class-nslayoutmanager">Class <tt class="literal"><span class="pre">NSLayoutManager</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getGlyphs:range:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">rectArrayForCharacterRange:withinSelectedCharacterRange:inTextContainer:rectCount:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">rectArrayForGlyphRange:withinSelectedGlyphRange:inTextContainer:rectCount:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmatrix">
<h2><a class="toc-backref" href="#id13" name="class-nsmatrix">Class <tt class="literal"><span class="pre">NSMatrix</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">sortUsingFunction:context:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in Python
is not. The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmovie">
<h2><a class="toc-backref" href="#id14" name="class-nsmovie">Class <tt class="literal"><span class="pre">NSMovie</span></tt></a></h2>
<p>The return value of <tt class="literal"><span class="pre">QTMovie</span></tt> and the sole argument of <tt class="literal"><span class="pre">initWithMovie:</span></tt>
are QT.Movie objects. Using these methods requires the use of MacPython 2.3.</p>
</div>
<div class="section" id="class-nsopenglcontext">
<h2><a class="toc-backref" href="#id15" name="class-nsopenglcontext">Class <tt class="literal"><span class="pre">NSOpenGLContext</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getValues:forParameter:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setValues:forParameter:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">setOffScreen:width:height:rowbytes:</span></tt></p>
<p>This method is not yet supported.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">CGLContextObj</span></tt></p>
<p>This method is not yet supported.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsopenglpixelformat">
<h2><a class="toc-backref" href="#id16" name="class-nsopenglpixelformat">Class <tt class="literal"><span class="pre">NSOpenGLPixelFormat</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getValues:forAttribute:forVirtualScreen:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsquickdrawview">
<h2><a class="toc-backref" href="#id17" name="class-nsquickdrawview">Class <tt class="literal"><span class="pre">NSQuickDrawView</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">qdPort</span></tt></p>
<p>This method returns an instance of type Carbon.QuickDraw. This 
requires MacPython.</p>
</li>
</ul>
</div>
<div class="section" id="class-nssimplehorizontaltypesetter">
<h2><a class="toc-backref" href="#id18" name="class-nssimplehorizontaltypesetter">Class <tt class="literal"><span class="pre">NSSimpleHorizontalTypesetter</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">baseOfTypesetterGlyphInfo</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">layoutGlyphsInHorizontalLineFragment:baseline:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsview">
<h2><a class="toc-backref" href="#id19" name="class-nsview">Class <tt class="literal"><span class="pre">NSView</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">sortSubviewsUsingFunction:context:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in Python
is not. The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nswindow">
<h2><a class="toc-backref" href="#id20" name="class-nswindow">Class <tt class="literal"><span class="pre">NSWindow</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">graphicsPort</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">initWithWindowRef:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">windowRef</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
</div>
<div class="section" id="foundation-framework">
<h1><a class="toc-backref" href="#id21" name="foundation-framework">Foundation framework</a></h1>
<p>NOTE: The list below is mostly based on scripts that find methods that can
not be automatically handled by the bridge. We have not yet performed a manual
search for such methods in the Cocoa documentation.</p>
<p>The <tt class="literal"><span class="pre">-forward::</span></tt> method is not supported. It's functionality can be accessed
using the python function <tt class="literal"><span class="pre">apply</span></tt>. The <tt class="literal"><span class="pre">performv::</span></tt> method is also not
supported, with a similar work-around.</p>
<p>Structs are wrapped using a struct-like type. They can be accessed using the
field-names from Objective-C, or you can access them as sequences. Accessing
them as sequences is necessary for backward compatibility and is deprecated.</p>
<div class="section" id="class-nsarray">
<h2><a class="toc-backref" href="#id22" name="class-nsarray">Class <tt class="literal"><span class="pre">NSArray</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">initWithObjects:</span></tt>, <tt class="literal"><span class="pre">arrayWithObjects:</span></tt></p>
<p>These methods are not supported, use <tt class="literal"><span class="pre">initWithArray:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getObjects:</span></tt></p>
<p>This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getObjects:inRange:</span></tt></p>
<p>This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">sortedArrayUsingFunction:context:</span></tt> and <tt class="literal"><span class="pre">sortedArrayUsingFunction:context:hint</span></tt></p>
<p>These methods can be called from Python, but you cannot override them
from Python. This limitation will be lifted in a future version of PyObjC.</p>
<p>The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">addObserver:toObjectsAtIndexes:forKeyPath:options:context:</span></tt></p>
<p>The context is an integer, not a <tt class="literal"><span class="pre">void*</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsautoreleasepool">
<h2><a class="toc-backref" href="#id23" name="class-nsautoreleasepool">Class <tt class="literal"><span class="pre">NSAutoreleasePool</span></tt></a></h2>
<p>The bridge automatically manages reference counts for you, but you're still 
required to make an autorelease pool available.</p>
<p>In simple, single-threaded GUI programs you don't have to do anything for this,
because NSRunLoop does this for you and PyObjC creates an initial pool for the
main thread.</p>
<p>If you create lots of Cocoa objects in a loop it can be useful to manually create
a pool to reclaim memory as soon as possible. The proper idiom for this is:</p>
<pre class="literal-block">
while &lt;test&gt;:
        pool = NSAutoreleasePool.alloc().init()

        # ... Do work here ...

        del pool
</pre>
<p>That is, you <em>must</em> ensure that the previous pool is deallocated before you create
a new one, the code below will silently leak memory:</p>
<pre class="literal-block">
while &lt;test&gt;:
        pool = NSAutoreleasePool.alloc().init()

        # ... Do work here ...
</pre>
</div>
<div class="section" id="class-nsbundle">
<h2><a class="toc-backref" href="#id24" name="class-nsbundle">Class <tt class="literal"><span class="pre">NSBundle</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">bundleForClass:</span></tt></p>
<p>This method does not work correctly for classes defined in Python, these
all seem be defined in the <tt class="literal"><span class="pre">mainBundle()</span></tt>. As a workaround for plugin
bundles built with py2app, you can declare <tt class="literal"><span class="pre">__bundle_hack__</span> <span class="pre">=</span> <span class="pre">True</span></tt>
on one class in the bundle (probably the NSPrincipalClass).  For this
class, <tt class="literal"><span class="pre">bundleForClass:</span></tt> will return the expected value.  See
Examples/Plugins for examples of this.</p>
</li>
</ul>
</div>
<div class="section" id="class-nscoder">
<h2><a class="toc-backref" href="#id25" name="class-nscoder">Class <tt class="literal"><span class="pre">NSCoder</span></tt></a></h2>
<p>The following methods are not supported in the current version of PyObjC.
This limitation will be lifted in a future version of the bridge.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">encodeValuesOfObjCType:</span></tt></p>
<p>Use multiple calls to <tt class="literal"><span class="pre">encodeValueOfObjCType:at:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">decodeValuesOfObjCType:</span></tt></p>
<p>Use multiple calls to <tt class="literal"><span class="pre">decodeValueOfObjCType:at:</span></tt> instead. Note that
that won't work if your trying to read back data that was written using
<tt class="literal"><span class="pre">encodeValuesOfObjCType:</span></tt>.</p>
</li>
</ul>
<p>The method <tt class="literal"><span class="pre">decodeBytesWithoutReturnedLength:</span></tt> is not supported, use 
<tt class="literal"><span class="pre">decodeBytesWithReturnedLength:</span></tt> instead. It is not possible to safely
represent the return value of this method in Python.</p>
</div>
<div class="section" id="class-nsdata">
<h2><a class="toc-backref" href="#id26" name="class-nsdata">Class <tt class="literal"><span class="pre">NSData</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">initWithBytesNoCopy:length:</span></tt></p>
<p>This method is not supported, use <tt class="literal"><span class="pre">initWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">initWithBytesNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is not supported, use <tt class="literal"><span class="pre">initWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">dataWithBytesNoCopy:length:</span></tt></p>
<p>This method is not supported, use <tt class="literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">dataWithBytesNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is not supported, use <tt class="literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeAlignedBytesLengthAtCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeBytes:length:atCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeDataAt:ofObjCType:atCursor:context:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeIntAtCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeInts:count:atCursor:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">deserializeInts:count:atIndex:</span></tt></p>
<p>This is a deprecated method, see Apple documentation.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getBytes:</span></tt>, <tt class="literal"><span class="pre">getBytes:length:</span></tt>, <tt class="literal"><span class="pre">getBytes:range:</span></tt>
Use <tt class="literal"><span class="pre">bytes</span></tt> instead, and then use subscripting to get the
desired range.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsdecimalnumber-and-the-nsdecimal-type">
<h2><a class="toc-backref" href="#id27" name="class-nsdecimalnumber-and-the-nsdecimal-type">Class <tt class="literal"><span class="pre">NSDecimalNumber</span></tt> and the <tt class="literal"><span class="pre">NSDecimal</span></tt> type</a></h2>
<p>NSDecimal is wrapped by a Python type. This type does not (yet) support
mathematical operators, but does support explicit conversion to and from
Python numbers.</p>
<p>Creating an <tt class="literal"><span class="pre">NSDecimal</span></tt> instance: <tt class="literal"><span class="pre">NSDecimal(value)</span></tt> or 
<tt class="literal"><span class="pre">NSDecimal(mantisssa,</span> <span class="pre">exponent,</span> <span class="pre">isNegative)</span></tt>.  <tt class="literal"><span class="pre">Value</span></tt> can be a string,
int or long (not a float because of the representation issues for floats).</p>
<p>Converting an <tt class="literal"><span class="pre">NSDecimal</span></tt> to a float or int: <tt class="literal"><span class="pre">aDecimal.as_int()</span></tt> and
<tt class="literal"><span class="pre">aDecimal.as_float</span></tt>.</p>
</div>
<div class="section" id="class-nsdictionary">
<h2><a class="toc-backref" href="#id28" name="class-nsdictionary">Class <tt class="literal"><span class="pre">NSDictionary</span></tt></a></h2>
<p>The (undocumented) methods <tt class="literal"><span class="pre">getKeys:</span></tt>, <tt class="literal"><span class="pre">getObjects:</span></tt> and 
<tt class="literal"><span class="pre">getObjects:andKeys:</span></tt> are not supported.</p>
</div>
<div class="section" id="class-nsexception">
<h2><a class="toc-backref" href="#id29" name="class-nsexception">Class <tt class="literal"><span class="pre">NSException</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">raise:format:</span></tt>, <tt class="literal"><span class="pre">raise:format:arguments:</span></tt></p>
<p>These methods are not supported because they accept a variable number of
arguments. Use Python's <tt class="literal"><span class="pre">%</span></tt> operator to format the message.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsfault">
<h2><a class="toc-backref" href="#id30" name="class-nsfault">Class <tt class="literal"><span class="pre">NSFault</span></tt></a></h2>
<p>The <tt class="literal"><span class="pre">extraData</span></tt> argument/return value for <tt class="literal"><span class="pre">-extraData</span></tt> and 
<tt class="literal"><span class="pre">setTargetClassextraData:</span></tt> is represented as an integer.</p>
</div>
<div class="section" id="class-nsindexset">
<h2><a class="toc-backref" href="#id31" name="class-nsindexset">Class <tt class="literal"><span class="pre">NSIndexSet</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getIndexes:maxCount:inIndexRange:</span></tt>
The usage is:</p>
<pre class="literal-block">
(realCount, indices, newRange) = obj.getIndexes_maxCount_inIndexRange(
        maxCount, inRange)              
</pre>
</li>
</ul>
</div>
<div class="section" id="class-nsinvocation">
<h2><a class="toc-backref" href="#id32" name="class-nsinvocation">Class <tt class="literal"><span class="pre">NSInvocation</span></tt></a></h2>
<p>In some versions of Mac OS X, NSInvocation doesn't work properly with structs
that contain padding. Such structs are not used in the Mac OS X API, but may
be present in 3th party code. This leads to problems when <tt class="literal"><span class="pre">forwardInvocation:</span></tt>
is used to call a method that has such a struct as one of its arguments.</p>
</div>
<div class="section" id="class-nsmutablearray">
<h2><a class="toc-backref" href="#id33" name="class-nsmutablearray">Class <tt class="literal"><span class="pre">NSMutableArray</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">sortUsingFunction:context:</span></tt>, <tt class="literal"><span class="pre">sortUsingFunction:context:range:</span></tt></p>
<p>Calling this method from Python is supported, overriding it in a subclass
is not. This limitation will be fixed in a later version of PyObjC.</p>
<p>The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsmutablestring">
<h2><a class="toc-backref" href="#id34" name="class-nsmutablestring">Class <tt class="literal"><span class="pre">NSMutableString</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">appendFormat:</span></tt></p>
<p>This method is not supported because it accepts a variable number of 
arguments. Use Python's <tt class="literal"><span class="pre">%</span></tt> operator to format strings.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsnetservice">
<h2><a class="toc-backref" href="#id35" name="class-nsnetservice">Class <tt class="literal"><span class="pre">NSNetService</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">addresses</span></tt></p>
<p>When calling this from Python this methods returns a tuple of address info
tuples, like the values returned by <tt class="literal"><span class="pre">socket.getpeeraddr()</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsobject">
<h2><a class="toc-backref" href="#id36" name="class-nsobject">Class <tt class="literal"><span class="pre">NSObject</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">observationInfo</span></tt>, <tt class="literal"><span class="pre">setObservationInfo:</span></tt></p>
<p>These methods can be used from Python, but the <tt class="literal"><span class="pre">observationInfo</span></tt> is 
represented by an integer instead of <tt class="literal"><span class="pre">void*</span></tt>. This probably makes it
impossible to do anything useful with these methods.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">addObserver:forKeyPath:options:context:</span></tt></p>
<p>The context is an integer.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">observeValueForKeyPath:ofObject:change:context:</span></tt></p>
<p>The context is an integer</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">methodForSelector:</span></tt>, <tt class="literal"><span class="pre">instanceMethodForSelector:</span></tt></p>
<p>These methods return instances of objc.IMP. The major difference with
Objective-C is that you don't have to, or even can, pass the selector to
the IMP. In other words, the interface is the same as for unbound
instance methods: you have to pass <tt class="literal"><span class="pre">self</span></tt> and the method arguments.</p>
<p>WARNING: This interface is experimental and might change in a future version
of PyObjC.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsscriptobjectspecifier">
<h2><a class="toc-backref" href="#id37" name="class-nsscriptobjectspecifier">Class <tt class="literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">indicesOfObjectsByEvaluatingWithContainer:count:</span></tt></p>
<p>Implementing this in Python is not supported yet. We're looking for a way
to avoid leaking the returned buffer, as we cannot return a pointer to an
internal data-structure.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsset">
<h2><a class="toc-backref" href="#id38" name="class-nsset">Class <tt class="literal"><span class="pre">NSSet</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">initWithObjects:</span></tt>, <tt class="literal"><span class="pre">setWithObjects:</span></tt></p>
<p>This method is not supported, use <tt class="literal"><span class="pre">initWithArray:</span></tt> instead.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsstring">
<h2><a class="toc-backref" href="#id39" name="class-nsstring">Class <tt class="literal"><span class="pre">NSString</span></tt></a></h2>
<p>Objective-C strings are usually represented as instances of a subclass of
the Python type <tt class="literal"><span class="pre">unicode</span></tt>. It is possible to access the &quot;real&quot; Objective-C
string by using the method <tt class="literal"><span class="pre">NSString</span></tt>. This should only be necessary when
dealing with mutable strings, or when you want to access methods that don't
have a Python equivalent.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">initWithCharactersNoCopy:length:freeWhenDone:</span></tt></p>
<p>This method is unsupported because we cannot guarantee that the buffer will
be available as long as the string is. Use <tt class="literal"><span class="pre">initWithCharacters:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getCharacters:</span></tt> and <tt class="literal"><span class="pre">getCharacters:range:</span></tt></p>
<p>These methods are not supported at the moment. This limitation will be lifted
in a future version of the bridge.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getCString:maxLength:range:remainingRange:</span></tt> and <tt class="literal"><span class="pre">getCString:maxLength:</span></tt></p>
<p>Calling these methods from Python is supported, overriding them from 
Python is not. This limitation will be lifted in a future version of the
bridge.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getCString:</span></tt></p>
<p>This method is not supported. Use <tt class="literal"><span class="pre">getCString:maxLength:</span></tt> instead (using
the length of the string as the maximum length). This limitation will be
lifted in a future version of the bridge.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">stringWithFormat:</span></tt>, <tt class="literal"><span class="pre">initWithFormat:</span></tt>, <tt class="literal"><span class="pre">initWithFormat:locale:</span></tt>,
<tt class="literal"><span class="pre">stringByAppendingFormat:</span></tt></p>
<p>These methods are not supported because they accept a variable number of 
arguments. Use Python's <tt class="literal"><span class="pre">%</span></tt> operator to format strings.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">initWithFormat:arguments:</span></tt>, <tt class="literal"><span class="pre">initWithFormat:locale:arguments:</span></tt></p>
<p>These are also not supported, with the same workaround.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsthread">
<h2><a class="toc-backref" href="#id40" name="class-nsthread">class <tt class="literal"><span class="pre">NSThread</span></tt></a></h2>
<p>It is safe to call from Objective-C to Python on any thread.  It is safe to
start new threads using the Python threading API and run non-Cocoa code on
those threads.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">detachNewThreadSelector:toTarget:withObject:</span></tt></p>
<p>Make sure that you've either created a thread from Python using the 
<tt class="literal"><span class="pre">thread</span></tt> or <tt class="literal"><span class="pre">threading</span></tt> module, or called <tt class="literal"><span class="pre">objc.enableThreading</span></tt> before
using this API. This is necessary to enable threading in the Python 
interpreter. We don't do this by default because this has a negative 
performance impact.</p>
</li>
</ul>
</div>
</div>
<div class="section" id="interfacebuilder-framework">
<h1><a class="toc-backref" href="#id41" name="interfacebuilder-framework">InterfaceBuilder framework</a></h1>
<p>I (Ronald) have not found documentation for this framework, therefore the
following methods with a &quot;difficult&quot; signature are not supported.</p>
<p>Please let me know if there is documentation for this framework.</p>
<div class="section" id="class-ibobjcsourceparser">
<h2><a class="toc-backref" href="#id42" name="class-ibobjcsourceparser">Class <tt class="literal"><span class="pre">IBObjCSourceParser</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">parseClass:</span></tt></li>
</ul>
</div>
<div class="section" id="id1">
<h2><a class="toc-backref" href="#id43" name="id1">Class <tt class="literal"><span class="pre">NSView</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">objectAtPoint:rect:</span></tt></p>
<p>Defined in a category on <tt class="literal"><span class="pre">NSView</span></tt>.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsibobjectdata">
<h2><a class="toc-backref" href="#id44" name="class-nsibobjectdata">Class <tt class="literal"><span class="pre">NSIBObjectData</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">restoreFromObjectDataInfo:</span></tt></li>
<li><tt class="literal"><span class="pre">snapshotIntoObjectDataInfo:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibobjectcontainer">
<h2><a class="toc-backref" href="#id45" name="class-ibobjectcontainer">Class <tt class="literal"><span class="pre">IBObjectContainer</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">decodeObjectToIntMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
<li><tt class="literal"><span class="pre">decodeObjectToObjectMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibxmldecoder">
<h2><a class="toc-backref" href="#id46" name="class-ibxmldecoder">Class <tt class="literal"><span class="pre">IBXMLDecoder</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">allocObjectWithClassName:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibsplitscrollview">
<h2><a class="toc-backref" href="#id47" name="class-ibsplitscrollview">Class <tt class="literal"><span class="pre">IBSplitScrollView</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getMinimumX:maximumX:</span></tt></li>
</ul>
</div>
</div>
<div class="section" id="preferencepanes-framework">
<h1><a class="toc-backref" href="#id48" name="preferencepanes-framework">PreferencePanes framework</a></h1>
<p>This framework seems to define useful classes like <tt class="literal"><span class="pre">NSAuthorization</span></tt> and
<tt class="literal"><span class="pre">NSKeychain</span></tt>, but these are not documented and some useful methods have
a hard signature.</p>
<p>The only documented class, <tt class="literal"><span class="pre">NSPreferencePane</span></tt>, is fully supported.</p>
</div>
<div class="section" id="screensaver-framework">
<h1><a class="toc-backref" href="#id49" name="screensaver-framework">ScreenSaver framework</a></h1>
<div class="section" id="class-screensaverdefaults">
<h2><a class="toc-backref" href="#id50" name="class-screensaverdefaults">Class <tt class="literal"><span class="pre">ScreenSaverDefaults</span></tt></a></h2>
<p>This class is fully supported.</p>
</div>
<div class="section" id="class-screensaverview">
<h2><a class="toc-backref" href="#id51" name="class-screensaverview">Class <tt class="literal"><span class="pre">ScreenSaverView</span></tt></a></h2>
<p>This class is fully supported.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>