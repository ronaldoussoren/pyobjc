<?
    $title = "Notes on supported APIs and classes on MacOS X";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/10/08 17:30:40 $';

    include "header.inc";
?>
<div class="document" id="notes-on-supported-apis-and-classes-on-macos-x">
<h1 class="title">Notes on supported APIs and classes on MacOS X</h1>
<!-- :author: Ronald Oussoren -->
<div class="contents topic" id="contents">
<p class="topic-title"><a name="contents">Contents</a></p>
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
<li><a class="reference" href="#class-nsbundle" id="id23" name="id23">Class <tt class="literal"><span class="pre">NSBundle</span></tt></a></li>
<li><a class="reference" href="#class-nscoder" id="id24" name="id24">Class <tt class="literal"><span class="pre">NSCoder</span></tt></a></li>
<li><a class="reference" href="#class-nsdata" id="id25" name="id25">Class <tt class="literal"><span class="pre">NSData</span></tt></a></li>
<li><a class="reference" href="#class-nsdictionary" id="id26" name="id26">Class <tt class="literal"><span class="pre">NSDictionary</span></tt></a></li>
<li><a class="reference" href="#class-nsfault" id="id27" name="id27">Class <tt class="literal"><span class="pre">NSFault</span></tt></a></li>
<li><a class="reference" href="#class-nsmutablearray" id="id28" name="id28">Class <tt class="literal"><span class="pre">NSMutableArray</span></tt></a></li>
<li><a class="reference" href="#class-nsnetservice" id="id29" name="id29">Class <tt class="literal"><span class="pre">NSNetService</span></tt></a></li>
<li><a class="reference" href="#class-nsscriptobjectspecifier" id="id30" name="id30">Class <tt class="literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></li>
<li><a class="reference" href="#class-nsset" id="id31" name="id31">Class <tt class="literal"><span class="pre">NSSet</span></tt></a></li>
<li><a class="reference" href="#class-nsstring" id="id32" name="id32">Class <tt class="literal"><span class="pre">NSString</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#interfacebuilder-framework" id="id33" name="id33">InterfaceBuilder framework</a><ul>
<li><a class="reference" href="#class-ibobjcsourceparser" id="id34" name="id34">Class <tt class="literal"><span class="pre">IBObjCSourceParser</span></tt></a></li>
<li><a class="reference" href="#id1" id="id35" name="id35">Class <tt class="literal"><span class="pre">NSView</span></tt></a></li>
<li><a class="reference" href="#class-nsibobjectdata" id="id36" name="id36">Class <tt class="literal"><span class="pre">NSIBObjectData</span></tt></a></li>
<li><a class="reference" href="#class-ibobjectcontainer" id="id37" name="id37">Class <tt class="literal"><span class="pre">IBObjectContainer</span></tt></a></li>
<li><a class="reference" href="#class-ibxmldecoder" id="id38" name="id38">Class <tt class="literal"><span class="pre">IBXMLDecoder</span></tt></a></li>
<li><a class="reference" href="#class-ibsplitscrollview" id="id39" name="id39">Class <tt class="literal"><span class="pre">IBSplitScrollView</span></tt></a></li>
</ul>
</li>
<li><a class="reference" href="#preferencepanes-framework" id="id40" name="id40">PreferencePanes framework</a></li>
<li><a class="reference" href="#screensaver-framework" id="id41" name="id41">ScreenSaver framework</a><ul>
<li><a class="reference" href="#class-screensaverdefaults" id="id42" name="id42">Class <tt class="literal"><span class="pre">ScreenSaverDefaults</span></tt></a></li>
<li><a class="reference" href="#class-screensaverview" id="id43" name="id43">Class <tt class="literal"><span class="pre">ScreenSaverView</span></tt></a></li>
</ul>
</li>
</ul>
</div>
<p>TODO: Add documentation about weak linking (see intro.txt).</p>
<div class="section" id="introduction">
<h1><a class="toc-backref" href="#id2" name="introduction">Introduction</a></h1>
<p>This document describes the restrictions w.r.t. supported APIs and classes
on MacOS X. In general you can use classes and global functions just like
in Objective-C (e.g. the Apple developer documentaton applies), but in some
cases there are special considerations.</p>
<p>We also do not provide access to global functions that are not usefull for
Python programs, those functions are listed below.</p>
<p>This document list the examples to the basic rules. If a method uses pointers
to return additional values, the Python wrapper for that method returns a tuple
containing the original return value and the additional values. You don't have
to pass values for those arguments, unless the method uses the values you
pass in.</p>
<p>This document is target at the latest supported version of MacOS X (currenlty
MacOS X 10.2.x), unless specifically noted the same restrictions apply to 
earlier versions of MacOS X. Earlier versions of the OS have less extensive
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
<ul class="simple">
<li><tt class="literal"><span class="pre">descriptionForClassMethod:</span></tt>, <tt class="literal"><span class="pre">descriptionForInstanceMethod</span></tt>
These methods are not supported, protocols are hardly ever used explicitly
in Cocoa therefore this should not be a problem.</li>
</ul>
</div>
</div>
<div class="section" id="addressbook-framework">
<h1><a class="toc-backref" href="#id5" name="addressbook-framework">Addressbook framework</a></h1>
<p>We do not provide access to the global functions in that framework, because
the same functionality can be accessed by using the object-oriented interface.</p>
</div>
<div class="section" id="appkit-framework">
<h1><a class="toc-backref" href="#id6" name="appkit-framework">AppKit framework</a></h1>
<p><tt class="literal"><span class="pre">NSPoint</span></tt> is a tuple of 2 floats, or use <tt class="literal"><span class="pre">AppKit.NSMakePoint(x,</span> <span class="pre">y)</span></tt>.</p>
<p><tt class="literal"><span class="pre">NSSize</span></tt> is a tuple of 2 floats, or use <tt class="literal"><span class="pre">AppKit.NSMakeSize(h,</span> <span class="pre">w)</span></tt>.</p>
<p><tt class="literal"><span class="pre">NSRect</span></tt> is a tuple of an <tt class="literal"><span class="pre">NSPoint</span></tt> and an <tt class="literal"><span class="pre">NSSize</span></tt>, or 
use <tt class="literal"><span class="pre">AppKit.NSMakeRect(x,</span> <span class="pre">y,</span> <span class="pre">h,</span> <span class="pre">w)</span></tt>.</p>
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
<div class="section" id="class-nsapplication">
<h2><a class="toc-backref" href="#id7" name="class-nsapplication">Class NSApplication</a></h2>
<p><tt class="literal"><span class="pre">NSModalSession</span></tt> objects are wrapped as opaque values. You can check if
two wrapper objects refer to the same session object by comparing their
<tt class="literal"><span class="pre">ptr</span></tt> attributes.</p>
</div>
<div class="section" id="class-nsbezierpath">
<h2><a class="toc-backref" href="#id8" name="class-nsbezierpath">Class NSBezierPath</a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getLineDash:count:phase:</span></tt>
This method is not supported, I (Ronald) could not find a way to detect the
required size for the pattern buffer.</li>
<li><tt class="literal"><span class="pre">appendBezierPathWithGlyphs:count:inFont:</span></tt>
The first argument is a list of integers, count should be at most the lenght
of the first argument.</li>
<li><tt class="literal"><span class="pre">appendBezierPathWithPoints:count:</span></tt>
The first argument is a list of points, count should be at most the lenght
of the first argument.</li>
<li><tt class="literal"><span class="pre">setAssociatedPoints:atIndex:</span></tt>
Implementing this method in Python is not yet supported.</li>
</ul>
</div>
<div class="section" id="class-nsbitmapimagerep">
<h2><a class="toc-backref" href="#id9" name="class-nsbitmapimagerep">Class <tt class="literal"><span class="pre">NSBitmapImageRep</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getBitMapDataPlanes</span></tt>
This method is not supported (yet)</li>
<li><tt class="literal"><span class="pre">getTIFFCompressionTypes:count:</span></tt>
This method is not supported (yet)</li>
<li><tt class="literal"><span class="pre">initWithBitmapDataPlanes:pixesWide:pixelsHigh:bitPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:</span></tt>
This method is not supported (yet)</li>
</ul>
</div>
<div class="section" id="class-nsfont">
<h2><a class="toc-backref" href="#id10" name="class-nsfont">Class <tt class="literal"><span class="pre">NSFont</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">positionsForCompositeSequence:numberOfGlyphs:pointArray:</span></tt>
This method is not supported (yet)</li>
</ul>
</div>
<div class="section" id="class-nsgraphicscontext">
<h2><a class="toc-backref" href="#id11" name="class-nsgraphicscontext">Class <tt class="literal"><span class="pre">NSGraphicsContext</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">focusStack</span></tt>
This method is not supported.</li>
<li><tt class="literal"><span class="pre">setFocusStack</span></tt>
This method is not supported.</li>
<li><tt class="literal"><span class="pre">graphicsPort</span></tt>
This method is not yet supported.</li>
</ul>
</div>
<div class="section" id="class-nslayoutmanager">
<h2><a class="toc-backref" href="#id12" name="class-nslayoutmanager">Class <tt class="literal"><span class="pre">NSLayoutManager</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getGlyphs:range:</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">rectArrayForCharacterRange:withinSelectedCharacterRange:inTextContainer:rectCount:</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">rectArrayForGlyphRange:withinSelectedGlyphRange:inTextContainer:rectCount:</span></tt>
This method is not yet supported</li>
</ul>
</div>
<div class="section" id="class-nsmatrix">
<h2><a class="toc-backref" href="#id13" name="class-nsmatrix">Class <tt class="literal"><span class="pre">NSMatrix</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">sortUsingFunction:context</span></tt>
Calling this method from Python is supported, overriding it in Python
is not. The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</li>
</ul>
</div>
<div class="section" id="class-nsmovie">
<h2><a class="toc-backref" href="#id14" name="class-nsmovie">Class <tt class="literal"><span class="pre">NSMovie</span></tt></a></h2>
<p>The return value of <tt class="literal"><span class="pre">QTMovie</span></tt> and the sole argument of <tt class="literal"><span class="pre">initWithMovie:</span></tt>
are QT.Movie objects. Using these methods requires the use of MacPython 2.3.</p>
</div>
<div class="section" id="class-nsopenglcontext">
<h2><a class="toc-backref" href="#id15" name="class-nsopenglcontext">Class <tt class="literal"><span class="pre">NSOpenGLContext</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getValues:forParameter:</span></tt>
This method is not yet supported.</li>
<li><tt class="literal"><span class="pre">setValues:forParameter:</span></tt>
This method is not yet supported.</li>
<li><tt class="literal"><span class="pre">setOffScreen:width:height:rowbytes:</span></tt>
This method is not yet supported.</li>
</ul>
</div>
<div class="section" id="class-nsopenglpixelformat">
<h2><a class="toc-backref" href="#id16" name="class-nsopenglpixelformat">Class <tt class="literal"><span class="pre">NSOpenGLPixelFormat</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">getValues:forAttribute:forVirtualScreen:</span></tt></p>
<p>This method is not yet supported</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">initWithAttributes:</span></tt></p>
<p>This method is not yet supported</p>
</li>
</ul>
</div>
<div class="section" id="class-nsquickdrawview">
<h2><a class="toc-backref" href="#id17" name="class-nsquickdrawview">Class <tt class="literal"><span class="pre">NSQuickDrawView</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">qdPort</span></tt></p>
<p>This method returns an instance from a type Carbon.QuickDraw. This 
requires MacPython.</p>
</li>
</ul>
</div>
<div class="section" id="class-nssimplehorizontaltypesetter">
<h2><a class="toc-backref" href="#id18" name="class-nssimplehorizontaltypesetter">Class <tt class="literal"><span class="pre">NSSimpleHorizontalTypesetter</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">baseOfTypesetterGlyphInfo</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">layoutGlyphsInHorizontalLineFragment:baseline:</span></tt>
This method is not yet supported</li>
</ul>
</div>
<div class="section" id="class-nsview">
<h2><a class="toc-backref" href="#id19" name="class-nsview">Class <tt class="literal"><span class="pre">NSView</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">sortSubviewsUsingFunction:context:</span></tt>
Calling this method from Python is supported, overriding it in Python
is not. The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</li>
</ul>
</div>
<div class="section" id="class-nswindow">
<h2><a class="toc-backref" href="#id20" name="class-nswindow">Class <tt class="literal"><span class="pre">NSWindow</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">graphicsPort</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">initWithWindowRef:</span></tt>
This method is not yet supported</li>
<li><tt class="literal"><span class="pre">windowRef</span></tt>
This method is not yet supported</li>
</ul>
</div>
</div>
<div class="section" id="foundation-framework">
<h1><a class="toc-backref" href="#id21" name="foundation-framework">Foundation framework</a></h1>
<p>NOTE: The list below is mostly based on scripts that find methods that can
not be automaticly handled by the bridge. We have not yet performed a manual
search for such methods in the Cocoa documentation.</p>
<p>The <tt class="literal"><span class="pre">-forward::</span></tt> method is not supported. It's functionality can be accessed
using the python function <tt class="literal"><span class="pre">apply</span></tt>. The <tt class="literal"><span class="pre">performv::</span></tt> method is also not
supported, with a simular work-around.</p>
<div class="section" id="class-nsarray">
<h2><a class="toc-backref" href="#id22" name="class-nsarray">Class <tt class="literal"><span class="pre">NSArray</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">initWithObjects:</span></tt>, <tt class="literal"><span class="pre">arrayWithObjects:</span></tt>
These methods are not supported, use <tt class="literal"><span class="pre">initWithArray:</span></tt> instead.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getObjects:</span></tt>
This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">getObjects:inRange:</span></tt>
This method is not supported, accessing the objects using the usual
accessor methods is just as efficient as using this method.</p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">sortedArrayUsingFunction:context:</span></tt> and <tt class="literal"><span class="pre">sortedArrayUsingFunction:context:hint</span></tt>
These methods can be called from Python, but you cannot override them
from Python. This limitation will be lifted in a future version of PyObjC.</p>
<p>The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsbundle">
<h2><a class="toc-backref" href="#id23" name="class-nsbundle">Class <tt class="literal"><span class="pre">NSBundle</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">bundleForClass:</span></tt>
This method does not work correctly for classes defined in Python, these
all seem be defined in the <tt class="literal"><span class="pre">mainBundle()</span></tt>. As a workaround you can use
the function <tt class="literal"><span class="pre">objc.pluginBundle(name)</span></tt> to find the NSBundle for your
Python based bundle. See Examples/PrefPane for an example of its usage.</li>
</ul>
</div>
<div class="section" id="class-nscoder">
<h2><a class="toc-backref" href="#id24" name="class-nscoder">Class <tt class="literal"><span class="pre">NSCoder</span></tt></a></h2>
<p>The following methods are not supported in the current version of PyObjC.
This limitation will be lifted in a future version of the bridge.</p>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">decodeBytesWithReturnedLength:</span></tt></p>
</li>
<li><p class="first"><tt class="literal"><span class="pre">decodeBytesForKey:returnedLength:</span></tt></p>
</li>
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
<h2><a class="toc-backref" href="#id25" name="class-nsdata">Class <tt class="literal"><span class="pre">NSData</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">initWithBytesNoCopy:length:</span></tt>
This method is not supported, use <tt class="literal"><span class="pre">initWithBytes:length:</span></tt> instead.</li>
<li><tt class="literal"><span class="pre">initWithBytesNoCopy:length:freeWhenDone:</span></tt>
This method is not supported, use <tt class="literal"><span class="pre">initWithBytes:length:</span></tt> instead.</li>
<li><tt class="literal"><span class="pre">dataWithBytesNoCopy:length:</span></tt>
This method is not supported, use <tt class="literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</li>
<li><tt class="literal"><span class="pre">dataWithBytesNoCopy:length:freeWhenDone:</span></tt>
This method is not supported, use <tt class="literal"><span class="pre">dataWithBytes:length:</span></tt> instead.</li>
<li><tt class="literal"><span class="pre">deserializeAlignedBytesLengthAtCursor:</span></tt>
This is a depricated method, see Apple documentation.</li>
<li><tt class="literal"><span class="pre">deserializeBytes:length:atCursor:</span></tt>
This is a depricated method, see Apple documentation.</li>
<li><tt class="literal"><span class="pre">deserializeDataAt:ofObjCType:atCursor:context:</span></tt>
This is a depricated method, see Apple documentation.</li>
<li><tt class="literal"><span class="pre">deserializeIntAtCursor:</span></tt>
This is a depricated method, see Apple documentation.</li>
<li><tt class="literal"><span class="pre">deserializeInts:count:atCursor:</span></tt>
This is a depricated method, see Apple documentation.</li>
<li><tt class="literal"><span class="pre">deserializeInts:count:atIndex:</span></tt>
This is a depricated method, see Apple documentation.</li>
</ul>
</div>
<div class="section" id="class-nsdictionary">
<h2><a class="toc-backref" href="#id26" name="class-nsdictionary">Class <tt class="literal"><span class="pre">NSDictionary</span></tt></a></h2>
<p>The (undocumented) methods <tt class="literal"><span class="pre">getKeys:</span></tt>, <tt class="literal"><span class="pre">getObjects:</span></tt> and 
<tt class="literal"><span class="pre">getObjects:andKeys:</span></tt> are not supported.</p>
</div>
<div class="section" id="class-nsfault">
<h2><a class="toc-backref" href="#id27" name="class-nsfault">Class <tt class="literal"><span class="pre">NSFault</span></tt></a></h2>
<p>The <tt class="literal"><span class="pre">extraData</span></tt> argument/return value for <tt class="literal"><span class="pre">-extraData</span></tt> and 
<tt class="literal"><span class="pre">setTargetClassextraData:</span></tt> is represented as an integer.</p>
</div>
<div class="section" id="class-nsmutablearray">
<h2><a class="toc-backref" href="#id28" name="class-nsmutablearray">Class <tt class="literal"><span class="pre">NSMutableArray</span></tt></a></h2>
<ul>
<li><p class="first"><tt class="literal"><span class="pre">sortUsingFunction:context:</span></tt>, <tt class="literal"><span class="pre">sortUsingFunction:context:range:</span></tt>
Calling this method from Python is supported, overriding it in a subclass
is not. This limitation will be fixed in a later version of PyObjC.</p>
<p>The <tt class="literal"><span class="pre">context</span></tt> can be an arbitrary python object.</p>
</li>
</ul>
</div>
<div class="section" id="class-nsnetservice">
<h2><a class="toc-backref" href="#id29" name="class-nsnetservice">Class <tt class="literal"><span class="pre">NSNetService</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">addresses</span></tt>
When calling this from Python this methods returns a tuple of adress-info
tuples, like the values returned by <tt class="literal"><span class="pre">socket.getpeeraddr()</span></tt>.</li>
</ul>
</div>
<div class="section" id="class-nsscriptobjectspecifier">
<h2><a class="toc-backref" href="#id30" name="class-nsscriptobjectspecifier">Class <tt class="literal"><span class="pre">NSScriptObjectSpecifier</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">indicesOfObjectsByEvaluatingWithContainer:count:</span></tt>
Implementing this in Python is not supported yet. We're looking for a way
to avoid leaking the returned buffer, as we cannot return a pointer to an
internal datastructure.</li>
</ul>
</div>
<div class="section" id="class-nsset">
<h2><a class="toc-backref" href="#id31" name="class-nsset">Class <tt class="literal"><span class="pre">NSSet</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">initWithObjects:</span></tt>, <tt class="literal"><span class="pre">setWithObjects:</span></tt>
This method is not supported, use <tt class="literal"><span class="pre">initWithArray:</span></tt> instead.</li>
</ul>
</div>
<div class="section" id="class-nsstring">
<h2><a class="toc-backref" href="#id32" name="class-nsstring">Class <tt class="literal"><span class="pre">NSString</span></tt></a></h2>
<p>Objective-C strings are usually represented as instances of a subclass of
the Python type <tt class="literal"><span class="pre">unicode</span></tt>. It is possible to access the &quot;real&quot; Objective-C
string by using the method <tt class="literal"><span class="pre">NSString</span></tt>. This should only be necessary when
dealing with mutable strings, or when you want to access methods that don't
have a Python equivalent.</p>
<ul class="simple">
<li><tt class="literal"><span class="pre">initWithCharactersNoCopy:length:freeWhenDone:</span></tt> 
This method is unsupported because we cannot guarantee that the buffer wil
be available as long as the string is. Use <tt class="literal"><span class="pre">initWithCharacters:</span></tt> instead.</li>
<li><tt class="literal"><span class="pre">getCharacters:</span></tt> and <tt class="literal"><span class="pre">getCharacters:range:</span></tt>
These methods are not supported at the moment. This limitation will be liften
in a future version of the bridge.</li>
<li><tt class="literal"><span class="pre">getCString:maxLength:range:remainingRange:</span></tt> and <tt class="literal"><span class="pre">getCString:maxLength:</span></tt>
Calling these methods from Python is supported, overriding them from 
Python is not. This limitation will be liften in a future version of the
bridge.</li>
<li><tt class="literal"><span class="pre">getCString:</span></tt>
This method is not supported. Use <tt class="literal"><span class="pre">getCString:maxLength:</span></tt> instead (using
the length of the string as the maximum length). This limitation will be
liften in a future version of the bridge.</li>
</ul>
</div>
</div>
<div class="section" id="interfacebuilder-framework">
<h1><a class="toc-backref" href="#id33" name="interfacebuilder-framework">InterfaceBuilder framework</a></h1>
<p>I (Ronald) have not found documentation for this framework, therefore the
following methods with a &quot;difficult&quot; signature are not supported.</p>
<p>Please let me know if there is documentation for this framework.</p>
<div class="section" id="class-ibobjcsourceparser">
<h2><a class="toc-backref" href="#id34" name="class-ibobjcsourceparser">Class <tt class="literal"><span class="pre">IBObjCSourceParser</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">parseClass:</span></tt></li>
</ul>
</div>
<div class="section" id="id1">
<h2><a class="toc-backref" href="#id35" name="id1">Class <tt class="literal"><span class="pre">NSView</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">objectAtPoint:rect:</span></tt>
Defined in a catagory on <tt class="literal"><span class="pre">NSView</span></tt>.</li>
</ul>
</div>
<div class="section" id="class-nsibobjectdata">
<h2><a class="toc-backref" href="#id36" name="class-nsibobjectdata">Class <tt class="literal"><span class="pre">NSIBObjectData</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">restoreFromObjectDataInfo:</span></tt></li>
<li><tt class="literal"><span class="pre">snapshotIntoObjectDataInfo:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibobjectcontainer">
<h2><a class="toc-backref" href="#id37" name="class-ibobjectcontainer">Class <tt class="literal"><span class="pre">IBObjectContainer</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">decodeObjectToIntMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
<li><tt class="literal"><span class="pre">decodeObjectToObjectMapTableForKey:fromCoder:alwaysCreate:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibxmldecoder">
<h2><a class="toc-backref" href="#id38" name="class-ibxmldecoder">Class <tt class="literal"><span class="pre">IBXMLDecoder</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">allocObjectWithClassName:</span></tt></li>
</ul>
</div>
<div class="section" id="class-ibsplitscrollview">
<h2><a class="toc-backref" href="#id39" name="class-ibsplitscrollview">Class <tt class="literal"><span class="pre">IBSplitScrollView</span></tt></a></h2>
<ul class="simple">
<li><tt class="literal"><span class="pre">getMinimumX:maximumX:</span></tt></li>
</ul>
</div>
</div>
<div class="section" id="preferencepanes-framework">
<h1><a class="toc-backref" href="#id40" name="preferencepanes-framework">PreferencePanes framework</a></h1>
<p>This framework seems to define usefull classes like <tt class="literal"><span class="pre">NSAuthorization</span></tt> and
<tt class="literal"><span class="pre">NSKeychain</span></tt>, but these are not documented and some usefull methods have
a hard signature.</p>
<p>The only documented class, <tt class="literal"><span class="pre">NSPreferencePane</span></tt> is fully supported.</p>
</div>
<div class="section" id="screensaver-framework">
<h1><a class="toc-backref" href="#id41" name="screensaver-framework">ScreenSaver framework</a></h1>
<div class="section" id="class-screensaverdefaults">
<h2><a class="toc-backref" href="#id42" name="class-screensaverdefaults">Class <tt class="literal"><span class="pre">ScreenSaverDefaults</span></tt></a></h2>
<p>This class is fully supported.</p>
</div>
<div class="section" id="class-screensaverview">
<h2><a class="toc-backref" href="#id43" name="class-screensaverview">Class <tt class="literal"><span class="pre">ScreenSaverView</span></tt></a></h2>
<p>This class is fully supported.</p>
</div>
</div>
</div>
<?
    include "footer.inc";
?>