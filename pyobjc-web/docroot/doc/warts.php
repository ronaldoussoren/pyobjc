<?
    $title = "Odd features";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/05/04 12:56:38 $';

    include "header.inc";
?>
<div class="document" id="odd-features">
<h1 class="title">Odd features</h1>
<!-- :author: Ronald Oussoren -->
<p>The mapping from Objective-C onto Python is almost complete, but the following
things should be kept in mind:</p>
<ul class="simple">
<li>Objective-C only has single inheritance. You can use multiple inheritance in
the python code, but only to mix in 'fully python' classes. Do <em>not</em> use 
multiple inheritance, this feature may not survive beyond 0.9.</li>
<li>In objective-C it is valid to call methods on nil, these calls will be
ignored. The nil 'object' is mapped to None and None will not ignore method
calls, but will most likely raise an AttributeError. You'll have to remember
this when translating from Objective-C to python.</li>
<li>Some Cocoa classes store references to objects while not increasing the 
reference count. One of those is NSOutlineView. A side-effect of this is that
you <em>must</em> use subclasses of NSObject in your NSOutlineView model, and you
<em>must</em> keep a reference to the objects you pass to NSOutlineView.</li>
</ul>
</div>
<?
    include "footer.inc";
?>