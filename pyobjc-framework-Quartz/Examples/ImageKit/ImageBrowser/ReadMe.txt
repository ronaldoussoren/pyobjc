This sample demonstrates the ImageKit ``ImageBrowser`` in a basic Cocoa 
application. It uses IB to create a window an ``ImageBrowser`` and a zoom 
slider. 

This sample should present a reasonably complete correctly formed Cocoa 
application which can be used as a starting point for using the ``ImageBrowser``
in a Cocoa applications. 

Usual steps to use the ImageKit image browser in your application:

1. setup your nib file

   Add a custom view and set its class to IKImageBrowserView.
   Connect an IBOutlet from your controller to your image browser view 
   and connect the ``IKImageBrowserView``'s ``_datasource`` ``IBOutlet`` to 
   your controller (if you want your controller to be the data source)

2. Don't forget to import the Quartz package::

	from Quartz import *

3. Create your own data source representation (here using a ``NSMutableArray``)::

	class MyController (NSWindowController):
	    _myImages = objc.ivar()
	    _myImageView = objc.IBOutlet()

4. implement the required methods of the informal data source protocol 
   (``IKImageBrowserDataSource``)::

	def numberOfItemsInImageBrowser_(self, browser):
		return len(self._images)

	def imageBrowser_itemAtIndex_(self, aBrowser, index):
		return self._images[index]


5.  The returned data source object must implement the 3 required 
    methods from the ``IKImageBrowserItemProtocol`` informal protocol:

	def imageUID(self): pass
	def mageRepresentationType(self): pass
	def imageRepresentation(self): pass

    * the id returned by ``imageUID`` MUST be different for each item 
      displayed in the image-view. Moreover, the image browser build it's 
      own internal cache according to this UID. the ``imageUID`` can be for 
      exemple the absolute path of an image existing on the filesystem or 
      another UID based on your own data structures.

    * ``imageRepresentationType`` return one of the following string constant 
      depending of the client's choice of representation::

	IKImageBrowserPathRepresentationType
	IKImageBrowserNSImageRepresentationType
	IKImageBrowserCGImageRepresentationType
	IKImageBrowserNSDataRepresentationType
	IKImageBrowserNSBitmapImageRepresentationType
	IKImageBrowserQTMovieRepresentationType

      (see IKImageBrowserView.h for complete list)

    * ``imageRepresentation`` return an object depending of the representation 
      type:

      *	a ``NSString`` for ``IKImageBrowserPathRepresentationType``
      * a ``NSImage`` for ``IKImageBrowserNSImageRepresentationType``
      * a ``CGImageRef`` for ``IKImageBrowserCGImageRepresentationType``
      * ...

    Here is a sample code of a simple implementation of a data source item::

      class myItemObject (NSObject, IKImageBrowserItem):
	_path = objc.ivar()

	def mageRepresentationType(self):
	    return IKImageBrowserPathRepresentationType;

	def mageRepresentation(self):
            return self._path

        def imageUID(self):
            return self._path

6. Now to see your data displayed in your instance of the image browser view, 
   you have to tell the browser to read your data using your ``IBOutlet`` 
   connected to the browser and invoke ``reloadData`` on it::

    self._myImageView.reloadData()

   Call ``reloadData`` each time you want the image browser to reflect changes 
   of your data source.

That's all for a very basic use.  Then you may need to add a scroller or a 
scrollview and a slider to your interface to let the user to scroll and zoom 
to browser his images. 
