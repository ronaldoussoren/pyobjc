<span class="news_date">2003-05-02: </span><span class="news_headline">PyObjC 0.9 released</span><?php gray_line(); ?>
 <p>
 PyObjC 0.9 has shipped. A disk image with an installer package and the sources are <a href="http://sourceforge.net/project/showfiles.php?group_id=14534">available</a>. There are many new features and bugfixes, see the <a href="NEWS.txt">NEWS file</a> for details.
 <p>
 The PyObjC installer package installes a number of examples and project builder
 templates as wel as documentation into /Developer. Users of 
 <a href="view-source:http://homepages.cwi.nl/~jack/macpython.html#beta">MacPython 2.3b1</a> can install this release using the 
 PackageManager application.
 <p>

<span class="news_date">2003-01-23: </span><span class="news_headline">Dev News; GNUstep support, FFI, performance, etc...</span><?php gray_line(); ?>
  <p>
<b>Important:</b> If you are working with the cvs based source, please read <a href="http://sourceforge.net/mailarchive/message.php?msg_id=3618225">this message</a>.</p>
<p>
Since the release of 0.8, many features and bug fixes have been introduced.  Some highlights:</p>
<ui>
<li>Startup time has been greatly reduced and further acceleration is in the works.</li>
<li>Support for <a href="http://sources.redhat.com/libffi/">libFFI</a>-- gcc's Foreign Function Interface-- has been added.   This reduces the size of the PyObjC module's binaries from 1MB to 300K while also providing the ability to message <i>any</i> Objective-C method, regardless of whether its signature happens to have been declared in the Foundation or AppKit headers.  Ronald put together a <a href="http://sourceforge.net/project/showfiles.php?group_id=14534">standalone snapshot</a> of libFFI.  libFFI is statically linked into the PyObjC module and does not hamper the ability to create standalone applications.</li>
<li>Two new project templates have been added.  The <i>Cocoa-Python Document-based Application</i> provides a template for multiple document architecture based applications.   The <i>Cocoa-Python-ObjC Application</i> can be used to create projects that contain compiled code in an embedded framework within the app wrapper that is dynamically loaded automatically at application startup.   Both project templates are designed to build standalone applications that are compatible with the stock build of Python that ships with OS X 10.2.  Project templates that use embedded python are in the works.</li>
<li>Support was added for various API that takes or returns buffers of bytes.   Specifically, the developer can now manipulate bitmaps directly via the <i>NSBitmapImageRep</i> class, work with binary data through the <i>NSData</i> class, and very quickly draw points and rects via <i>NSRectFillList()</i>.   More support is on the way as time permits.  More functionality of this nature will be added as time permits.  If you have need for support of a particular API, please file a <a href="http://sourceforge.net/tracker/?atid=364534&group_id=14534&func=browse">Feature Request</a>.</i>
<li>Many bug fixes have been committed.  In many cases, the unit tests were augmented to verify the exact nature of the failure prior to fixing the problem.  As such, the unit tests provide an excellent source of information regarding the capabilities and limitations of the bridge.</li>
<li>Work on documentation has been slow, but is happening.   We are using <a href="http://docutils.sourceforge.net">DocUtils and ReStructured Text</a> for all documentation.</li>
<li>Invoking an instance method through the class when the 'self' argument is a Python type now works.  That is, <code>NSString.localizedCaseInsensitiveCompare_('foo', 'bar')</code> works as expected.  This allows the developer to invoke the instance methods of transparently converted classes such as NSString and NSNumber.</li>
<li>Direct access to class and instance methods is now possible.  As a result, it is now possible to invoke a class method when both a class and instance method of the same name exist.</li>
</ul>
