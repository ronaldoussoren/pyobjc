<?
    $title = "The PyObjC release process";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>
<div class="document" id="the-pyobjc-release-process">
<!-- :author: Ronald Oussoren -->
<p>This document gives an exhaustive overview of what needs to be done when 
building and releasing a new version of PyObjC. It is meant for the project
administrators, and not of much use for users of PyObjC.</p>
<p>The timeframe is a guideline only and should be taken with a grain of salt.</p>
<div class="section" id="release-date-2-weeks">
<h1><a name="release-date-2-weeks">Release date -2 weeks</a></h1>
<p>Full feature freeze, documentation updates and critical bug-fixes only. At
this time:</p>
<ul class="simple">
<li>Check if the NEWS file is up-to-date</li>
<li>Tests the tutorial(s)
Read the tutorial(s) and follow the instructions exactly, the tutorials
should be completely bug-free.</li>
<li>Proofread the documentation</li>
<li>Update the announcement messages.</li>
</ul>
</div>
<div class="section" id="release-date-3-days">
<h1><a name="release-date-3-days">Release-date -3 days</a></h1>
<p>Build the release tarball and dmg:</p>
<ul class="simple">
<li>Add the correct date to the NEWS file, and set the right version in
<tt class="literal"><span class="pre">Modules/objc/pyobjc.h</span></tt>.</li>
<li>Run <tt class="literal"><span class="pre">python</span> <span class="pre">setup.py</span> <span class="pre">sdist</span></tt> to build the source tarball.</li>
<li>Run <tt class="literal"><span class="pre">python</span> <span class="pre">setup.py</span> <span class="pre">bdist_dmg</span></tt> to build a binary installer.  This should
be done for each supported version combination of Mac OS X and Python.</li>
</ul>
<p>Trash you existing PyObjC installation and reinstall from the new release. Test
that the new release is working correctly. Installing and testing should be
done for the binary installer and for the source archive. The latter should
be done for all supported configurations.  Also test to make sure that an
upgrade from a previous release works as expected.</p>
<p>If the package works as expected, upload to a convenient location and ask some
other people (like the other maintainers) to test the new release.</p>
</div>
<div class="section" id="release-date">
<h1><a name="release-date">Release-date</a></h1>
<ul>
<li><p class="first">Upload the release files to sourceforge</p>
</li>
<li><p class="first">add a news item to the website and update the download page</p>
</li>
<li><p class="first">add the latest documentation to the website (run scripts/doc2php in
the pyobjc-web tree).</p>
</li>
<li><dl class="first">
<dt>announce the new version at ADC news: </dt>
<dd><p class="first last"><a class="reference" href="http://developer.apple.com/devnews/submit.html">http://developer.apple.com/devnews/submit.html</a></p>
</dd>
</dl>
<ul>
<li><p class="first">Organization: PyObjC Team</p>
</li>
<li><p class="first">Name of Product... : PyObjC</p>
</li>
<li><p class="first">URL: <a class="reference" href="http://pyobjc.sourceforge.net">http://pyobjc.sourceforge.net</a></p>
</li>
<li><p class="first">Describe your product... :</p>
<p>PyObjC is a bridge between Python and Objective-C and allows development
of full-fledged Cocoa programs in pure Python.</p>
</li>
</ul>
</li>
<li><p class="first">update the information at a number of software databases:</p>
<ul class="simple">
<li>versiontracker.com (bbum knows how)</li>
<li>macupdate.com</li>
<li>freshmeat.net (ronald knows how)</li>
<li>PyPI database at python.org (run <tt class="literal"><span class="pre">python2.3</span> <span class="pre">setup.py</span> <span class="pre">register</span></tt>)</li>
</ul>
</li>
<li><p class="first">send the announcement text to:</p>
<ul class="simple">
<li><a class="reference" href="mailto:python-list&#64;python.org">python-list&#64;python.org</a></li>
<li><a class="reference" href="mailto:python-announce-list&#64;python.org">python-announce-list&#64;python.org</a></li>
<li><a class="reference" href="mailto:macosx-dev&#64;omnigroup.com">macosx-dev&#64;omnigroup.com</a></li>
<li><a class="reference" href="mailto:pyobjc-dev&#64;sourceforge.net">pyobjc-dev&#64;sourceforge.net</a></li>
<li><a class="reference" href="mailto:pythonmac-sig&#64;python.org">pythonmac-sig&#64;python.org</a></li>
<li><a class="reference" href="mailto:cocoa-dev&#64;lists.apple.com">cocoa-dev&#64;lists.apple.com</a></li>
</ul>
</li>
</ul>
</div>
</div>
<?
    include "footer.inc";
?>