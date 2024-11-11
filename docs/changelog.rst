What's new in PyObjC
====================

An overview of the relevant changes in new, and older, releases.

Version 10.3.2
--------------

* Fix a number of test failures on the first macOS 15 beta. These are
  all documentation and test updates.

* :issue:`593`: PyObjCTools.AppHelper.runConsoleEventLoop no longer
  exits the process on macOS 14 or later when stopping the event loop.

* :issue:`613`: Actually expose protocols ``KHTTPCookieStoreObserver``,
  ``WKURLSchemeTask``, and ``WKURLSchemeHandler`` in the WebKit bindings.

* Remove workaround for a linker problem in early versions of Xcode 15,
  which restores support for building with Xcode Command Line tools.

* The release contains wheels for the free-threaded build of Python 3.13.

  Note that PyObjC does not support running without the GIL at this time.

* Fix for running test suite with recent versions of setuptools

  Recent versions of setuptools broke the "test" command, the full command
  has been reimplemented as part of PyObjC.

* :issue:`627`: Fix build issue when deployment target is 15.0 or later.

* :issue:`623`: Don't lowercase the first character of the first keyword
   argument for ``__new__`` when the segment only contains upper case
   characters.

   Before this change ``initWithURL:`` mapped to an ``uRL`` keyword argument,
   with this fix the keyword argument is named ``URL``.

   Fix by user rndblnch on github

* :issue:`625`: Fix crash for calling ``NSIndexSet.alloc().initWithIndex_(0)``

  This "fix" is a workaround for what appears to be a bug in Foundation.

* :issue:`569`: Actually remove the workaround for Xcode 15.0

* :issue:`619`: Fix race condition in creating proxy objects for Objective-C
  classes.

Version 10.3.1
--------------

* :issue:`610`: Ensure ``__init__`` can be used when user implements ``__new__``.

  Version 10.3 dropped support for calling ``__init__``, but that breaks
  a number of popular projects. Reintroduce the ability to use ``__init__``
  when a class or one of its super classes contains a user implemenentation
  of ``__new__``.

  Code relying on the ``__new__`` provided by PyObjC still cannot use
  ``__init__`` for the reason explained in the 10.3 release notes.


Version 10.3
------------

* The release contains binary wheels for Python 3.13

  PyObjC does at this time not support the experimental free threading
  support in Python 3.13.

* :issue:`569`: Removed the workaround for a bug in Xcode 15.0

  The workaround is no longer necessary, and caused problems when
  building with the Command Line Tools development tools from Apple.

* Updated SDK bindings for macOS 14.5

* A minor change in the (currently private) tooling I use for
  collecting the raw metadata resulted in minor fixes to the framework
  bindings, in particular for metadata for a number of block and function
  typed arguments and return values.

* :issue:`275`: It is now possible to create instances of Objective-C
  classes by calling the class, e.g. ``NSObject()`` instead of
  ``NSObject.alloc().init()``.

  The implementation of ``__new__`` forwards calls to the underlying
  ``SomeClass.alloc().init...()`` pattern. In particular, all public init
  methods are translated into sets of keyword arguments:

  - Remove `init` or `initWith` from the start of the selector name
  - Lowercase the first character of what's left over
  - The strings before colons are acceptable keywords, in that order

  For example, given a selector ``initWithX:y:`` the ``__new__`` method
  will accept ``x, y`` as keyword arguments, in that order.

  Framework bindings have been updated with additional metadata to support
  this pattern, and the sets of keyword arguments are automatically calculated
  for subclasses in written in Python.

  The limitation on the order of keyword arguments may be lifted in a future
  version, it is currently present to keep the code closer to the Objective-C
  spelling which should make it easier to look up documentation on Apple's
  website.

* For some Objective-C classes some of the `init` and `new` methods are not
  available even if they are available in super classes. Those methods are
  marked with ``NS_UNAVAILABLE`` in Apple's headers.

  As of this version these methods are also not available in Python code,
  trying to call them will result in an exception.

  To make methods unavailable in Python classes set these methods to ``None``,
  e.g.:

  ```python

  class MyObject(NSObject):
     init = None # NS_UNAVAILABLE
  ```

* Added :func:`objc.registerUnavailableMethod`,
  :func:`objc.registerNewKeywordsFromSelector` and
  :func:`objc.registerNewKeywords` to support the generic ``__new__``
  in framework bindings.

  A limitation for ``registerUnavailableMethod`` is that it is currently
  not supported to reintroduce the method in a subclass, primarily because
  that functionality is not needed for framework bindings.

* Instantiating an Objective-C class by calling the class (e.g. invoking
  ``__new__``) will not call ``__init__`` even if one is defined.

  The implementation of a subclass of ``NSObject`` should always follow
  the Objective-C convention for initializing using one or more
  methods with a name starting with ``init``.

  This can affect code that manually defines a ``__new__`` method for
  an Objective-C class, in previous versions that was the only way
  to create instances in a Pythontic way.

  The primairy reason for this change is that the new default ``__new__``
  implementation resulted in calling ``__init__`` for some code paths and
  not others due to the python semantics for creating instances, e.g.:

  .. sourcecode:: python3

     class MyDocument(NSDocument):
         def __init__(self, *args, **kwds): pass

     document = MyDocument()   # __init__ gets called
     document, error = MyDocument(type="mytype", error=None). # __init__ does not get called

  In the last statement ``__init__`` does not get called because
  ``__new__`` does not return an instance of ``MyDocument``.

* ``NSArray``, ``NSMutableArray``, ``NSSet`` and ``NSMutableSet`` accepted
  a ``sequence`` keyword argument in previous versions. This is no longer supported.

  It is still supported to create instances using a positional argument
  for a sequence, e.g.  ``NSArray([1, 2, 3])``.

* ``NSData``, ``NSMutableData``, ``NSDecimal``, ``NSString`` and ``NSMutableString``
   accepted a ``value`` keyword argument in previous versions. This is no longer supported.

  It is still supported to create instances using a positional argument,
  e.g.  ``NSData(b"hello")``.

* ``NSDictionary`` and ``NSMutableDictionary`` do *not* support the
  generic new interface because this conflicts with having a similar
  interface to ``dict`` for creating instances.

  That is, ``NSDictionary(a=4, b=5)`` is the same as ``NSDictionary({"a":4, "b":5})``,
  and not like ``NSDictionary.alloc().initWithA_b_(4, 5)``.

Version 10.2.1
--------------

* Fix possible memory corruption in the implementation of ``forwardInvocation:``
  for Python classes.

* Fix build error when building with a python configured with ``--with-pydebug``.

* Don't override ``tp_dealloc`` slot in :class:`objc.super` but use the one
  inherited from :class:`super`. This makes sure construction and deallocation
  are consistent with each other (found while testing with ``--with-pydebug``).

* Fix deprecation warning while compiling ``pyobjc-framework-Quartz``.

Version 10.2
------------

* Fix a number of warnings found by adding ``-Wpendantic`` to the CFLAGS for
  pyobjc-core

* Fix undefined behaviour warnings:

  - Suppress the undefined behaviour warning about out of range values in
    double to (unsigned) long long in the ``OC_PythonNumber`` implementation
    as these are unavoidable when matching ``NSNumber`` behaviour.

  - Switch to using ``memcpy`` instead of direct assignment in converting
    plain C values to/from Python because "packed" structs might result
    in accessing values through unaligned pointers.

* Updated bindings for the macOS 14.4 SDK (Xcode 15.3)

* Added bindings for the "BrowserEngineKit" framework on macOS 14.4 or later.

* Add :func:`obj.registerPathType` to register a Python type as a path like
  type with PyObjC. By default only :class:`pathlib.Path` is registered as such.

  A minor backward compatibility issue is that instances of the registered types
  will be written to ``NSArchive`` and ``NSKeyArchive`` archives as instances
  of ``NSURL`` and won't roundtrip back to the original Python type. This might
  change in future versions of PyObjC, at least for :class:`pathlib.Path`.

* :issue:`589`: Instances of :class:`pathlib.Path` (and other types registered with
  `objc.registerPathType`) are bridged into Objective-C as instances of ``NSURL``.

  This means that these types can be used as values passed to APIs expecting
  a filesystem URL, e.g.:

  ```python

  path = pathlib.Path("/Applications/Numbers.app")
  bundle = NSBundle.bundleWithURL_(path)
  ```

* Fix some warnings in pyobjc-core when testing with Python 3.13a4.

* Add support for ``NSBezierPathElementQuadraticCurveTo`` in ``NSBezierPath.elementAtIndex_associatedPoints_``.

* :issue:`595`: Fix compilation error in ``pyobjc-framework-Cocoa`` with a recent
  deployment target.

Version 10.1
------------

* Upgrade framework bindings for the macOS 14.2 SDK

* :issue:`579`: Make sure the ``install.py`` and ``develop.py`` scripts in the
  repository work when run out of tree.

* :issue:`577`: ``os.fspath(someURL)`` will not work with Cocoa URLs (NSURL, CFURLRef) that
  refer to local filesystem paths. ``TypeError`` will be raised for other URLs.

  This enables using regular Python filesystem APIs with URLs that refer to
  local filesystem paths.

* :issue:`572`: Fix compilation issue when building on macOS 13 or earlier

* Fix build error on ancient macOS versions where clang doesn't support
  ``-flto=thin``.

* Add a workaround for a crash in pyobjc-core when running the testsuite
  on macOS 10.14.

* Fix some issues found while running the testsuite on macOS 10.9 to
  macOS 13, instead of only testing on the latest macOS version. Most
  issues found where problems in the testsuite itself, but not all.

  Some of the changes skip tests on older macOS versions (10.12, 10.13
  and 10.14) due to running into what appears to be crashing
  platform bugs.

* :issue:`581`: Fix dependencies between framework binding packages

* Fix build error with the current Python 3.13 alpha release (3.13a2).

Version 10.0
------------

* Update bindings for macOS 14

  Symbols newly introduced in macOS 14 were added to the existing bindings,
  and the following new bindings were introduced:

  * Cinematic

  * MediaExtension

  * SensitiveContentAnalysis

  * Symbols

* The "IMServicePlugIn" bindings are no longer available

  The entire framework was deprecated in macOS 10.13 and removed in macOS 14.
  The bindings can not be build using the latest SDK, and had (at best) limited
  use.

* :issue:`542`: PyObjC 10 requires Python 3.8 and no longer supports Python 3.7

* :issue:`547`: Removed all ``MAC_OS_X_VERSION*`` constants from ``objc``.

  These constants are needed in practice (switch to :func:`objc.available` to
  check for platform availability), and caused unnecessary code churn.

* The value for ``objc.options.deprecation_warnings`` is now a string
  instead of an integer.

* :issue:`555`: Fix unintended incompatibility with pytest in PyObjCTools.TestSupport

* :issue:`295`: The lazy loading machinery by default no longer uses
  :class:`objc.ObjCLazyModule`, but uses module level ``__dir__`` and
  ``__getattr__`` instead. The class :class:`objc.ObjCLazyModule` is still
  available, but is deprecated

  As a side effect of this ``objc`` is no longer an attribute of framework
  binding packages (e.g ``Foundation.objc`` is no longer a valid attribute).

  Another side effect of this is that all attributes added by the import system
  are now correctly present in the packages for framework bindings.

  And a final side effect is that private symbols (prefixed with underscore) are
  no longer imported from dependencies of framework bindings (more closely matching
  the ``from dependency import *`` behaviour that the lazy importer emulates.

* Add attribute ``__framework_identifier__`` to all framework bindings with the
  identifier of the corresponding system framework.

* :issue:`295`: Introduce :func:`objc.createFrameworkDirAndGetattr` to
  create module level ``__dir__`` and ``__getattr__`` for use by
  framework bindings.

* :issue:`561`: Tests now validate the bundle identifier value used in framework bindings.

  This resulted in a number of changes to framework bindings with incorrect
  bundle identifier values. This shouldn't affect user code because the
  bundle loader falls back on the framework path when the identifier cannot be found.

* :issue:`559`: Avoid test failures in pyobjc-core when pyobjc-framework-Quartz is
  not installed.

* A number of classes can no longer be subclasses in Python because they are marked as non-subclassable
  in the macOS 14 SDK (either directly or as "subclassing is deprecated":

  ``CKAllowedSharingOptions``,
  ``CKAsset``,
  ``CKContainer``,
  ``CKDatabase``,
  ``CKDatabaseNotification``,
  ``CKDatabaseSubscription``,
  ``CKFetchRecordZoneChangesConfiguration``,
  ``CKNotification``,
  ``CKNotificationID``,
  ``CKNotificationInfo``,
  ``CKOperationConfiguration``,
  ``CKOperationGroup``,
  ``CKQuery``,
  ``CKQueryCursor``,
  ``CKQueryNotification``,
  ``CKQuerySubscription``,
  ``CKRecord``,
  ``CKRecordID``,
  ``CKRecordZone``,
  ``CKRecordZoneID``,
  ``CKRecordZoneNotification``,
  ``CKRecordZoneSubscription``,
  ``CKReference``,
  ``CKServerChangeToken``,
  ``CKShare``,
  ``CKShareMetadata``,
  ``CKShareParticipant``,
  ``CKSubscription``,
  ``CKSyncEngine``,
  ``CKSyncEngineAccountChangeEvent``,
  ``CKSyncEngineConfiguration``,
  ``CKSyncEngineDidFetchChangesEvent``,
  ``CKSyncEngineDidFetchRecordZoneChangesEvent``,
  ``CKSyncEngineDidSendChangesEvent``,
  ``CKSyncEngineEvent``,
  ``CKSyncEngineFailedRecordSave``,
  ``CKSyncEngineFailedZoneSave``,
  ``CKSyncEngineFetchChangesOptions``,
  ``CKSyncEngineFetchedDatabaseChangesEvent``,
  ``CKSyncEngineFetchedRecordDeletion``,
  ``CKSyncEngineFetchedRecordZoneChangesEvent``,
  ``CKSyncEngineFetchedZoneDeletion``,
  ``CKSyncEnginePendingDatabaseChange``,
  ``CKSyncEnginePendingRecordZoneChange``,
  ``CKSyncEnginePendingZoneDelete``,
  ``CKSyncEnginePendingZoneSave``,
  ``CKSyncEngineRecordZoneChangeBatch``,
  ``CKSyncEngineSendChangesContext``,
  ``CKSyncEngineSendChangesOptions``,
  ``CKSyncEngineSentDatabaseChangesEvent``,
  ``CKSyncEngineSentRecordZoneChangesEvent``,
  ``CKSyncEngineState``,
  ``CKSyncEngineStateSerialization``,
  ``CKSyncEngineStateUpdateEvent``,
  ``CKSyncEngineWillFetchChangesEvent``,
  ``CKSyncEngineWillFetchRecordZoneChangesEvent``,
  ``CKSyncEngineWillSendChangesEvent``,
  ``CKSystemSharingUIObserver``,
  ``CKUserIdentity``,
  ``CKUserIdentityLookupInfo``.

* The encoding of a number of basic types changes, in particular those
  of CoreFoundation struct types and SIMD struct types. None of this
  should affect user code.

* ``objc.getClassList`` now has an optional positional argument to
  ignore classes with a name that aren't identifiers.

* Some of the functionality in CoreFoundation was rewritten in Swift
  in macOS 14, with Swift subclasses of ``NSArray`` and ``NSDictionary``.
  Those classes break an invariant of PyObjC: the superclass of the root
  of the Swift class hierarchy changes when the class is instantiated
  for the first time (from ``NSObject`` to the correct superclass).

  PyObjC 10 contains a workaround for this by ignoring these classes
  unless they are needed to create a proxy for an instance (FB12286520).

* Fix crash when the method signature retrieved from the Objective-C runtime
  contains the class name for a method returning ``id``.

* Remove old 32-bit support in metadata override files.

* Restructure ``objc.simd``: The matrix types are now named ``simd_float3x3``
  instead of ``matrix_float3x3``, with the older name as an alias (to match
  older system headers).

* Fix crash when loading the libdispatch bindings on recent macOS versions
  (at least macOS 13, possibly earlier)

* ``dispatch.dispatch_source_t`` is renamed to ``dispatch.dispatch_source_type_t``
  to match the type name in C code.

* :issue:`569`: Xcode 15 has a bug when using weak symbols and targeting older macOS
  versions. Switch to the old linker when detecting Xcode 15.

Version 9.2.1
-------------

* :issue:`563`: Fix incompatibility with macOS 14 beta 1


Version 9.2
-----------

* :issue:`549`: Added warning ``objc.ObjCSuperWarning`` that is used
  to warn about classes that use argument-less super without binding that
  name to ``objc.super``.

  The correct code pattern is:


  .. sourcecode:: python3

     from Foundation import NSObject
     from objc import super


     class MyObject(NSObject):
         def init(self):
             self = super().init()
             if self is None:
                 return None

             ...
             return self


* :issue:`549`: Document that ``objc.super`` must be used instead of
  ``builtin.super`` when calling superclass methods in a Cocoa subclass.

  See `the documentation <(https://pyobjc.readthedocs.io/core/super.html>`_
  for more details.

* :issue:`550`: Add minimal ``pyproject.toml`` to all subprojects

  Recent versions of pip give a deprecation warning for projects without
  a ``pyproject.toml``, and version 23.1 enabled the ``pyproject.toml``
  backend by default. Add a minimal ``pyproject.toml`` to get a consistent
  build regardless of the version of pip

* :issue:`551`: Fix crash in pyobjc-core when using Python 3.12a7.

* :issue:`449`: Added explicit tests for dealing with Objective-C categories
  that are loaded while using classes from Python.

* :issue:`552`: Fix the version of macOS where the SafariServices framework is
  present.

* :issue:`552`: Fixed some issues found by testing on a macOS 10.11 system

* Trying to implement a method with SIMD types as arguments or return value
  will now give a more useful error when the bridge does not support the
  signature.

* :issue:`554`: Fix incomplete metadata for ``CoreMediaIO.CMIOObjectSetPropertyData``

* Fix incorrect metadata for
  ``xpc.xpc_uuid_create``,
  ``xpc.xpc_dictionary_set_uuid`` ,
  ``xpc.xpc_array_set_uuid``,
  ``JavaScriptCore.JSObjectMakeDeferredPromise``,
  ``JavaScriptCore.JSValueIsEqual``,
  ``JavaScriptCore.JSValueIsInstanceOfConstructor``,
  ``JavaScriptCore.JSValueCreateJSONString``,
  ``JavaScriptCore.JSValueToNumber``,
  ``JavaScriptCore.JSValueToStringCopy``,
  ``JavaScriptCore.JSValueToObject``,
  ``Quartz.CGImageCreateWithJPEGDataProvider``,
  ``Quartz.CGImageCreateWithPNGDataProvider``,
  ``Quartz.CGImageMaskCreate``,
  ``Quartz.CVBufferCopyAttachment``,
  ``Quartz.CVMetalTextureCacheCreate``,
  ``Quartz.CVMetalTextureCacheCreateFromImage``,
  ``Quartz.CVOpenGLTextureCacheCreate``,
  ``CoreMedia.CMAudioClockCreate``,
  ``CoreMedia.CMAudioFormatDescriptionCreate``,
  ``CoreMedia.CMBlockBufferGetDataPointer``,
  ``CoreMedia.CMBlockBufferAccessDataBytes``,
  ``CoreMedia.CMBlockBufferGetDataPointer``,
  ``CoreMedia.CMAudioFormatDescriptionGetMostCompatibleFormat``,
  ``CoreMedia.CMAudioFormatDescriptionGetRichestDecodableFormat``,
  ``CoreMedia.CMSampleBufferCreateWithMakeDataReadyHandler``,
  ``CoreMedia.CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler``,
  ``CFNetwork.CFNetServiceBrowserSearchForDomains``,
  ``CFNetwork.CFNetServiceBrowserStopSearch``,
  ``CFNetwork.CFNetServiceMonitorStop``,
  ``CFNetwork.CFNetServiceRegister``,
  ``CFNetwork.CFNetServiceResolve``,
  ``CoreText.CTFontCreateCopyWithSymbolicTraits``,
  ``CoreText.CTFontCreateCopyWithFamily``,
  ``CoreText.CTFontCreateCopyWithAttributes``,
  ``CoreMIDI.MIDISourceCreateWithProtocol``,
  ``CoreMIDI.MIDISourceCreate``,
  ``CoreMIDI.MIDISetupCreate``,
  ``CoreMIDI.MIDIDestinationCreate``,
  ``CoreMIDI.MIDIClientCreate``,
  ``CoreMIDI.MIDIClientCreateWithBlock``,
  ``CoreMIDI.MIDIOutputPortCreate``,
  ``CoreMIDI.MIDIObjectGetStringProperty``,
  ``CoreMIDI.MIDIObjectGetProperties``,
  ``CoreMIDI.MIDIObjectGetIntegerProperty``,
  ``CoreMIDI.MIDIObjectGetDictionaryProperty``,
  ``CoreMIDI.MIDIObjectGetDataProperty``,
  ``CoreMIDI.MIDIObjectFindByUniqueID``,
  ``CoreMIDI.MIDIDestinationCreateWithProtocol``,
  ``CoreMIDI.MIDIEndpointGetEntity``,
  ``CoreMIDI.MIDIEntityGetDevice``,
  ``CoreMIDI.MIDIEntityGetRefCons``,
  ``CoreMIDI.MIDIEntitySetRefCons``,
  ``DVDPlayback.DVDRegisterEventCallBack``,
  ``DiskArbitration.DADiskMountWithArguments``,
  ``GameController.NSDataFromGCExtendedGamepadSnapShotDataV100``,
  ``HealthKit.HKAppleWalkingSteadinessClassificationForQuantity``,
  ``IOSurface.IOSurfaceSetPurgeable``,
  ``Network.nw_ethernet_channel_send``,

* Removed ``Quartz.CGColorConversionInfoCreateFromListWithArguments``. This function
  was already documented as unsupported, but was still present in the framework
  wrapper.

* Removed ``Quartz.CVPixelBufferCreateWithPlanarBytes``. This function requires a
  manual binding, but was still present with a generic (and non-working) binding.

* Removed ``CoreMedia.CMBufferQueueCreate``, ``CoreMedia.CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS``,
  ``CoreMedia.CMBufferQueueGetCallbacksForUnsortedSampleBuffers``, ``CoreMedia.CMVideoFormatDescriptionGetH264ParameterSetAtIndex``,
  ``CoreMedia.CMVideoFormatDescriptionGetHVECParameterSetAtIndex``,
  These functions require a manual binding, but were still present with a generic (and non-working) binding.

* Explicitly exclude definitions from ``CMIOHardwarePlugIn.h`` from the CoreMediaIO
  bindings.

* Added ``deref_result_pointer`` key to the metadata for a return value. Use this
  when a callable returns a pointer to a single value (for example ``CMAudioFormatDescriptionGetMostCompatibleFormat``)

* Removed unsupported functions from the ApplicationServices bindings (not named individually
  due to the size of the list). Also fixed annotations for other ApplicationServices bindings.

* Add manual binding for ``CFNetwork.CFNetServiceBrowserCreate``, ``CFNetwork.CFNetServiceSetClient``,
  and ``CFNetwork.CFNetServiceMonitorCreate``.

* Fix incompatibility with Python 3.12 beta 1.

  .. warning::

     Due to changes to the bytecode compiler the bridge will (incorrectly)
     deduce that a method does not return a value (``void`` return in Objective-C)
     when a method only contains ``return None`` statements and no return
     statements that return some other value (expressions or constants).

     That is the following method is implied to return ``id`` for Python 3.11 or
     earlier, but is implied to return ``void`` in Python 3.12.

     .. sourcecode:: python

         def mymethod(self):
             return None


Version 9.1.1
-------------

* :issue:`548`: Fix unexpected error when using mix-in classes

Version 9.1
------------

* Fix handling ``python_method(native_selector)`` when assigning to a class
  attribute. That is, the following was broken in 9.1b1:

  .. sourcecode:: python

     import Foundation, objc

     NSArray.makeArray = objc.python_method(NSArray.arrayWithArray_)

* :issue:`535`: Reverted ome of the speedups in ``assertCallableMetadataIsSane``

  A new sanity check required reverting some of the speedups in
  ``assertCallableMetadataIsSane``.

Version 9.1b1
-------------

This is a fairly large larger update due to rewriting part of the core
logic in Python (where the previous version used C). This does result in
some minor semantic changes, but those should only affect edge cases and
not normal user code.

These changes were done because it simplifies the code base, and makes it
easier to evolve the code (which has already led to a number of easy-of-use
improvements as described below).

* :issue:`306`: The code that converts a Python callable into an ``objc.selector``
  when creating an Objective-C class is now written in Python instead of
  Objective-C.

  Note that the interface that the C extension uses to invoke Python
  code is not a public API and can change in minor releases.

  The rewrite found a number of edge cases where the older implementation
  in C was incorrect or inconsistent. Those problems have been fixed as
  part of this effort (see below for details).

* The BadPrototypeError raised when a method is not compatible with number
  of arguments expected by Objective-C now mentions the number of
  arguments excluding the "self" argument, instead of including it.

* The new code will accept callables other than functions and bound
  method as a possible source of ``objc.selector`` objects, this
  can affect code storing a callable object (other than types) as
  a class attribute.

  Wrap these in an ``objc.python_method`` to avoid conversion.

* Added ``objc_objc_method`` that can be used to decorate functions
  that must be converted to an ``objc.selector``. The decorator has
  optional keyword arguments to affect the conversion.

* ``objc.python_method`` is now implemented in Python.

  The ``callable`` attribute is deprecated, use ``__wrapped__`` instead
  to access the wrapped callable.

  The new implementation requires that the wrapped value is either
  a callable or a classmethod and won't work with arbitrary values.

* Coroutines (generators, async method) are no longer wrapped in
  an ``objc.selector`` by default.

* Using a callable that's not compatible with use a selector due
  to having the wrong number of positional arguments or having
  keyword-only arguments will now raise consistently during
  class construction.

* objc.python_method is now implemewnted in Python. Due to the
  reimplementation the ``callable`` attribute has been renamed
  to the more standard ``__wrapped__`` attribute.

* For native selectors the ``signature`` attribute no longer
  contains the raw signature, but a cleaned up copy.

* Added private function to look for an informal protocol related
  to a selector name.

* Added private function to look registered metadata for a
  selector name.

* PEP-8 compatible multi-word method names are no longer converted
  to selectors, e.g.:

  .. sourcecode:: python

    class MyObject(NSObject):
       def some_method(self, a, b):
           pass

  In previous versions this required using the ``@objc.python_method``
  decorator.

* Method names containing double underscores are no longer converted
  to selectors, e.g:

  .. sourcecode:: python

    class MyObject(NSObject):
      def spam__(self, a, b):
          pass

      def spam__ham_(self, a, b, c):
          pass

  In previous versions these were converted to, nonsensical,
  selectors: ``spam::`` and ``spam::ham:``.

* Introduce a new optional subkey in ``__metadata__()``: ``full_signature``
  contains the complete signature for a method.

* Setting dunder names in a class will no longer create a selector:

  .. sourcecode:: python

     def __dir__(self):
         return []

     NSObject.__dir__ = __dir__

  In PyObjC 9.0 or earlier this resulted in a new selector on
  ``NSObject``, in PyObjC 9.1 this results a new Python-only method.

  This matches the behaviour of defining dunder methods in a class
  definition.

* Wrapping a python_method in a classmethod now works:

  .. sourcecode:: python

      class MyClass(NSObject):
          @classmethod
          @python_method
          def spam_spam(self):
              pass

* Method definitions with varargs are now accepted for selectors
  when the number of arguments expected in Objective-C "fits":

  .. sourcecode:: python

      class MyClass(NSObject):
         def correctMethod_(self, *args):
             # Args will be a 1-tuple when called
             # from Objective-C
             pass

         def correctMethod2_(self, value, *args):
             # 'args' will always be empty when
             # called from Objective-C
             pass


         def incorrectMethod2_(self, value, value2, *args):
             # Objective-C will pass exactly one argument,
             # this method needs at least 2.
             pass

* If a python class overrides a method in the superclass it will
  now use the selector of the superclass method instead of
  defaulting to a transformation of the method name.

  .. sourcecode:: python

      class SuperClass(NSObject):
          @objc.selector(selector=b"buttonPressed:")
          def pressed(self):
              ...


      class SubClass(SuperClass):
          def pressed(self):
              ...

  In previous versions of PyObjC ``SubClass.pressed`` would have
  been a selector with name ``b"pressed"``, in PyObjC 9.1 the
  selector name is inherited from the super class (``b"buttonPressed:"``).

* Subclassing an ``NSCoder`` has an incompatible change. In previous
  version of PyObjC the "at" argument for, for example ``-[NSCoder decodeValueOfObjCType:at:]``
  was not passed to Python, e.g.:

  .. sourcecode:: python

     class MyCoder(NSCoder):
         def decodeValueOfObjCType_at_(self, encoding):
             ...

  As of PyObjC 9.1 the "at" argument must be present in the
  the python argument list, and will always be passed None:

  .. sourcecode:: python

     class MyCoder(NSCoder):
         def decodeValueOfObjCType_at_(self, encoding, at):
            ...

  The same is also true for ``-[NSCoder decodeBytesWithReturnedLength:]``.

  This makes these methods consistent with the general convention
  for implementing Objective-C method. This change was missed
  at earlier cleanups because implementing these NSCoder methods
  uses custom logic in C.

* Added ``objc._C_PythonObject`` with the encoding for ``PyObject*``.

  This is primarily for internal use by PyObjC, using PyObjC
  as an FFI tool for callin CPython APIs is not supported.

* Added ``isSlot`` argument to ``objc.ivar`` to define Python variable
  slots.

  This is primairly here for internal use of the bridge, use
  ``__slots__`` to define slots.

* ``objc.ivar`` instances can now be compared for equality. Two
  instances are considered equal if the tuple ``(name, type, isOutlet, isSlot)``
  for the two values are equal.

* When ``__slots__`` is a string the class will have a single slot
  with that name. In previous versions the class would have a number
  of slots with single-character names.

  The new behaviour matches that of regular Python classes.

* The ``objc.objc_class`` type now has a ``__hasdict__`` attribute that is
  True if instances of the class have a ``__dict__`` attribute and is
  False otherwise.

* It is now an error when two instance variables (``objc.ivar``, including those
  defined through ``__slots__``) have the same Objective-C name, and that includes
  redefining a slot in a superclass.

  In previous versions this was not an error and the two ``objc.ivar`` objects
  would use the same memory in the instance, which could lead to crashes if
  the two did not have the same type encoding.

* Fix longstanding bug in class construction:

  .. sourcecode:: python

     class MyClass(NSObject):
        @objc.objc_method(selector="foobar")
        def method(self):
           pass

  In previous versions only ``MyClass.method`` is defined, whereas the
  code in the bridge intended to define ``MyClass.foobar`` as well.

* Fix type encoding for ``respondsToSelector:`` method that's implicitly defined
  by the bridge.

* In previous versions accessing a hidden selector showed an ``objc.native_selector``
  instead of an ``objc.selector`` for hidden selectors implemented in Python, and those
  objects did not have the ``isHidden`` attribute set to true.

* :issue:`506`: Code no longer uses ``PySlice_GetIndicesEx``, which was deprecated
  by CPython in 3.6.

* Tweak pyobjc_setup.py to re-enable the error message when trying to install
  framework bindings on systems other than macOS.

* "Hidden" selectors implemented in Python can now be introspected though ``pyobjc_instanceMethods`` and
  ``pyobjc_classMethod``. In previous versions the following assertion would fail:

  .. sourcecode:: python

       class MyClass(NSObject):
           def hidden(self):
               pass

           hidden = objc.selector(hidden, isHidden=True)

       assert isinstance(MyClass.pyobjc_instanceMethods.hidden)

  A side effect of this is that calling hidden methods implemented in Python from
  Python now uses the "python to python" code path and won't translate argument and
  return values from Python to Objective-C and back again.

  Also note that (as usual) Key-Value Observing (KVO) complicates the picture, if
  the hidden method is a property accessor (for KVO) and the object is observed accessing
  the method will result in a "native" selector, not the original one due to the
  way KVO is implemented in the system.

* :issue:`522`: Remove the implementation of ``respondsToSector:`` and ``methodSignatureForSelector:``.

  In previous versions PyObjC included custom implementation of these methods for
  subclasses of ``NSObject`` implemented in Python, but the default implementation
  in ``NSObject`` works just as well for Python classes.

* Creating an ``objc.ivar`` will now raise an exception if the specified type encoding
  is not valid. Previous versions would raise on the first use of the instance variable.

* :issue:`522`: Reimplemented ``objc.informal_protocol`` in Python

  The new implementation adds a number of new methods to give ``objc.informal_protocol`` the
  same interface as ``objc.formal_protocol``, which simplifies the implementation of
  code using protocols.

  That said, ``objc.informal_protocol`` still has a ``selectors`` attribute that is not
  present on ``objc.formal_protocol``. This will not change.

* :issue:`522`: The code that validates if a new class conforms to all protocols it claims to
  conform to is now written in Python.

  As a side effect of this the error message for an invalid protocol conformance definition
  no longer mentions with definition was invalid (the ``protocols`` keyword or the
  ``__pyobjc_protocols__`` class attribute).

  The new implementation is also more strict in the values of selectors that are accepted,
  all selectors not be instances of ``objc.native_selector`` and must have a ``callable``
  attribute that is not ``None``.

* :issue:`523`: PyObjC's default implementation for ``-forwardInvocation:`` now calls the
  method stub (``IMP``) through libffi, instead of trying to reproduce the logic
  of the method stub in the implementation for ``-forwardInvocation:``. This removes about
  300 lines of C code and makes sure the semantics of message forwarding match that of
  regular method calls.

  This only affects subclasses of ``NSObject`` implemented in Python, the bridge contains
  a second implementation of ``forwardInvocation:`` for regular Python class with limited
  functionality (and very low performance).

* In previous versions PyObjC would introduce an intermediate class between a pure Objective-C
  super class and the first Python sub class when this was needed for correctness. This class
  is now always introduced.

  There are two reasons for this:

  1. Adding some methods (such as ``copyWithZone_``) to a class after it was constructed
     caused problems in older version because the intermediate class wasn't present.

  2. Simplifies the code for building a class

  The intermediate class is named ``_PyObjCIntermediate_{NAME}`` where ``{NAME}`` is the name
  of the super class, in previous versions it was named ``_PyObjCCopying_{NAME}``.

* Fix ``objc.listInstanceVariables`` failure when one of the classes in the class hierarchy
  does not have instance variables.

* Fix crash when the filter for the ``UninitializedDeallocWarning`` warning is set to "error".

* Fix conversion of float subclasses with custom ``__repr__`` to ``objc.NSDecimal``.

* Fix handling ``objc.NSDecimal`` in boolean contexts: In previous versions
  ``objc.NSDecimal(0)`` was interpreted as true-ish in boolean contexts, it now
  is interpreted as false-ish just like other number types.

* :issue:`381`: Add bindings for the IOBluetooth and IOBluetoothUI frameworks

* Add bindings for the PHASE framework

* #363: Support possible buffer overrun in NSCoder API helpers

  The implementations for NSCoder APIs that have a type encoding argument assumed
  that the ``Py_buffer`` representation of the type encoding is a NUL-terminated string.

  This is a valid assumption for the ``bytes`` and ``bytesarray`` types, but is
  not guaranteed by the buffer API and could result in reading past the end of the
  buffer when an incomplete type encoding is passed to these APIs.

  As a side effect of this fix there is minor change in the API for these methods:
  - Type encodings containing unions and bitfields now error out early;
  - Type encodings for structs cannot contain embedded field names;
  - The APIs are slightly slower due to validating the type encoding.

* Calling ``-[SFAuthorizationView authorizationRights]`` now works, in previous
  version the support code was present but enabled for a non-existing method name.

* :issue:`527`: The type of ``objc.NULL`` is now created with ``PyType_FromSpec``.

  This has the unfortunate side effect of making it possible to change type
  attributes on Python 3.9 or earlier. Do not do this, the type is immutable
  in Python 3.10 or later.

* :issue:`527`: A number of types are now created with ``PyType_FromSpec``:

  * ``objc.PyObjCPointer``

  * ``objc.FILE``

  * ``objc.formal_protocol``

  * ``objc.function``

  * ``objc.NSDecimal``

  * ``objc.varlist``

  * ``objc.WeakRef``

  * ``objc.super``

  * ``objc.IMP``

  * ``objc.FSRef``

  * ``objc.selector``

  * ``objc.native_selector``

  * ``objc.python_selector``

  * all types created by ``objc.createStructType``

  * ``CoreAudio.AudioBuffer``

  * ``CoreAudio.AudioBufferList``

  * ``CoreAudio.AudioChannelDescription``

  * ``CoreAudio.AudioChannelLayout``

  * ``CoreAudio.AudioValueTranslation``

  For these types the class can be changed in Python 3.9 earlier, but not
  in 3.10 or later. The ability to change class attributes in Python 3.9 and earlier
  is due to a limitation in ``PyType_FromSpec`` in those versions, don't rely on this.

  This is a small step towards supporting subinterpreters, although it is unclear at
  this time when PyObjC will support this in part due to CPython missing some API
  functionality required by the implementation of ``objc.objc_object`` and ``objc.objc_class``
  when using ``PyType_FromSpec``.

* :issue:`423`: ``objc.ivar`` is now created with ``PyType_FromSpec``. Because of
  that the private method ``objc.ivar._add_attribute`` has been removed.

* The creation of ``objc.super`` is now less hacky although it still
  relies on implementation details of ``builtins.super``.

* Fixed bug that could result in a crash when the proxy for a Python iterator
  ended up being deallocated after the Python interpreter is finalized.

* Code cleanup for ``objc._objc`` continues, in this version the module initialisation
  code was much simplified, most of it is now table-driven. This has no user visible
  effects.

* Types created by ``objc.createStructType`` now have a (read-only) ``__packed__`` attribute
  that's ``-1`` if the C struct has default packing, and positive integer when
  the C struct has some other packing.

* :issue:`382`: Add bindings for APIs defined in header ``xpc/xpc.h``

  This is a low-level API to perform RPCs using the XPC protocol on macOS.

* :issue:`376`: Updated libdispatch bindings, fixing a number of issues with automatic
  retaincount management.

* The python package name in ``pyobjc-framework-libdispatch`` is now ``dispatch`` instead
  of ``libdispatch``. The old name also works, with no plans to remove it.

* :issue:`113`: Implement ``JavaScriptCore.JSExportAs``

  This required some change to pyobjc-core as well. The exact interface used
  by ``JSExportAs`` is for now considered a private implementation detail.

  XXX: As this time actually using JSExportAs doesn't work, even though
  the shape of the protocol looks correctly.

* The ``Metal`` bindings now contain definitions for ``MTLPackedFloat3``,
  ``MTLPackedFloat4x3``, ``MTLAccelerationStructureInstanceDescriptor``
  and ``MTLPackedFloat3Make``.

* Upgraded framework bindings for Xcode 14.3 (macOS 13.3 SDK)

* Dropped custom implementation of ``protocol_getMethodDescription``

  FB11984735: In earlier versions of macOS there were problems with actually
  registering protocols in some cases. A custom implementation of this
  function allowed tests to pass. Turns out that debugging code that uses
  ``protocol_getMethodDescription`` during protocol construction caused problems...

* :issue:`535`: Speed up standalone tests with ``assertCallableMetadataIsSane``

  This assertion method is very slow because it looks at all callable attributes,
  sped up considerably for standalone tests by only looking at attribute names
  that might be callable (by poking in implementation details of the lazy loader).

  This halves the time needed to run the check for the Cocoa bindings (from
  over 200 seconds to just over 100 seconds). That's still too slow, but does help.

  The method is also smarter about iterating over methods, shaving another 20 seconds
  from this test.

* :issue:`539`: Fix incorrect metadata for ``IOSurfaceCreate`` that resulted in a crash
  when that API was used.

* :issue:`537`: Switch from ``pkg_resources`` to ``importlib`` in the support for
  bridgesupport XML files because the setuptools project has deprecated the
  ``pkg_resources`` module.

Version 9.0.1
-------------

* :issue:`512`: Fix metadata for ``webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame:completionHandler:`` and
  ``webView:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedByFrame:completionHandler:`` in the WebKit
  bindings.

* :issue:`508`: Reintroduce support for bridgesupport files that was dropped in 9.0.

  There are external users for this interface and the replacement used by PyObjC itself
  is not yet in a state where it can be used by other projects.

* Framework bindings were updated for the SDK included in Xcode 14.1

* :issue:`517`: Fix bad markup in overview of wrapped frameworks

* :issue:`519`: Fix compile error with Python 3.12

Version 9.0
-----------

* Support for macOS 13 (Xcode 14 beta 4)

* Updated framework bindings for macOS 13

  The list below lists the frameworks that have
  API changes that affect the framework bindings.

* Added bindings for the following frameworks
  (all new in macOS 13):

  - AVRouting
  - BackgroundAssets
  - ExtensionKit
  - HealthKit
  - MetalFX
  - SafetyKit
  - SharedWithYou
  - SharedWithYouCore
  - ThreadNetwork

* The definition of a number of basic structs has moved in the SDK for
  macOS 13 and PyObjC conforms to this change on all platforms.

  In particular:

  - ``CGPoint``, ``CGSize``, ``CGVector``, ``CGRect``, ``CGAffineTransform`` and ``CGAffineTransformComponents``
    are now defined in the ``CoreFoundation`` module.
  - ``NSPoint``, ``NSSize`` and ``NSRect`` are now aliases for the corresponding ``CG*`` types
     (instead of the other way around in previous versions of PyObjC).

  Both changes should require no changes to scripts, unless code relies on the
  particular ``__name__`` of a type.

* The extension API ("pyobjc-api.h") now has nullability annotations, which may lead to compilation
  errors or warnings when compiling 3th-party extensions using this API.

* The extension API ("pyobjc-api.h") has a changed interface for creating method IMPs, because
  of this extensions for older versions of PyObjC cannot be used with PyObjC 9.

* :issue:`416`: PyObjC 9.0 requires Python 3.7 or later

* :issue:`384`: Remove support for BridgeSupport files

  The bridge itself hasn't used these files for a long time, and system
  bridgesupport files are basically unusable.

* :issue:`415`: Remove ``objc._setClassExtender``

  This was an internal function that's no longer used by PyObjC itself.

* :issue:`429`: Remove ``-[OC_PythonNumber getValue:forType:]``

  This method is never actually used by the system and is not
  part of the ``NSNumber`` interface (but possibly was in the past)

* :issue:`438`: Removed bindings for the ``Message`` and ``ServerNotification``
  frameworks.

  Both frameworks were removed in macOS 10.9 and hence cannot be
  used on a platform that's still supported by PyObjC.

* :issue:`451`: Removed the ``type`` attribute for ``ObjCPointer``

  The ``typestr`` attribute contains the same value and has
  more consistent naming with the rest of PyObjC.

* :issue:`436`: ``Quarrtz.CVPixelBufferCreateWithBytes`` now conforms to the
  PyObjC standard for returning values: it returns a tuple of two
  values, the C return value and the value return through ``pixelBufferOut``.

  In older versions the return value was only the value return through
  ``pixelBufferOut``.

* 464: The encodings ``objc._C_NSBOOL`` and ``objc._C_BOOL`` are now treated
  exactly the same as the types ``BOOL`` and ``bool`` have the same size
  and representation on arm64 and x86_64.

* :issue:`94`: Add support for SIMD types in APIs (types such as ``vector_float3``)

  The python representation of these types are types with the same name in
  defined in :mod:`objc.simd`.

  Because the FFI library used by PyObjC (libffi) does not support these types
  the bridge only supports the method signatures found in system frameworks,
  other signatures will result in exceptions at runtime.

  The relevant libffi issue for this is `#408 <https://github.com/libffi/libffi/issues/408>`_.
  But note that even if that issue were to be fixed PyObjC likely won't use
  SIMD support in libffi until that's merged in the system version on macOS.

* Because of the previous change APIs that have a SIMD type are now callable
  from Python.

* Changes due to generic implementation for SIMD types:

  - ``SpriteKit.SK3DNode.projectPoint_``: The result is now ``objc.simd.vector_float3`` instead of a tuple
  - ``SpriteKit.SK3DNode.unprojectPoint_``: The result is now ``objc.simd.vector_float3`` instead of a tuple
  - ``SpriteKit.SKFieldNode.direction``: The result is now ``objc.simd.vector_float3`` instead of a tuple
  - ``SpriteKit.SKPhysicsWorld.sampleFieldsAt_``: The result is now ``objc.simd.vector_float3`` instead of a tuple

* Still not supported (requires some more infrastructure):

  - ``SpriteKit.SKFieldNode.customFieldWithEvaluationBlock_``

* The registered metadata can now contain a key ``full_signature`` with the
  full encoding type signature for a method. This is used to replace the
  encoding extracted from the Objective-C runtime when one or more types have
  an empty encoding in the Objective-C runtime (such as the SIMD types mentioned
  earlier)

* The Objective-C proxy for Python methods that require a custom
  helper (instead of using libffi) now use ``imp_implementationWithBlock``.

* :issue:`492`: For a number of classes in ``AVFoundation``  the system actually uses
  instances from a parallel class hierarchy with ``_Tundra`` as a suffix of the
  class name.

  Updated the metadata generator to automatically register the same metadata updates
  for these classes as for the original classes.

* :issue:`493`: Fix typos in CoreMedioIO metadata for CoreFoundation types

* :issue:`495`: Added two new assertions to ``PyObjCTools.TestSupport.TestCase``:

  - ``assertArgIsIDLike``
  - ``assertResultIsIDLike``

  These assert that the type of an argument or return value is
  a Objective-C or CoreFoundation object, or a pointer to one.

* Fix internal error when an object that cannot be used in a boolean context
  is used for an ObjC argument that expects a ``bool`` or ``BOOL`` value.

* :issue:`502`: Fix incompatibility with Nuitka.

  Earlier version of PyObjC failed when compiled using Nuitka, this
  version does work when using Nuitka 1.1.6 or later.

  Limitations:

  - The automatic calculation of the method signature in ``selector()``
    assumes that methods return ``id`` for Nuitka compiled code.

    That should not be a problem in practice.

  As a side effect of this builtin functions are accepted as
  the callable for a selector, even when not specifying a
  signature (e.g. ``objc.selector(dir)`` now works).

* Fixed crash in objc.selector due to uninitialized memory.

* Move helpers for NSInvocation from pyobjc-framework-Cocoa to
  pyobjc-core.

* :issue:`505`: Don't use static buffer during creation of "native" selector objects

  This can avoid an ``objc.error`` exception when introspecting existing
  Cocoa classes.

* :issue:`479`: Revert change that made it impossible to replace a method
  with a property.

Version 8.6
-----------

* :issue:`468`: Fix setup.py for framework bindings to ensure that
  ``python setup.py build_ext`` works for bindings that don't
  contain a C extension.

* Fix incompatibilities with Python 3.11 (beta 1)

  - Switch to ``PyCode_GetCode`` instead of accessing
    the ``co_code`` field on Python 3.11.
  - Add definition for ``PassKit.PKPaymentNetworkAppleStoredValue``
    (actually using this won't work as the constant is not
    present on macOS 12.4 even though the SDK seems to suggest
    otherwise)

* Add definition for ``objc.MAC_OS_X_VERSION_12_4``

Version 8.5
-----------

This release continues the work on test coverage in pyobjc-core,
resulting in a number of minor bug fixes.

* Added two options to the ``build_ext`` command in the ``setup.py``
  of pyobjc-core:

  - ``--no-lto``: Disable link time optimization

  - ``--no-warnings-as-errors``: Disable ``-Werror``

* For struct bindings in frameworks the "in" operator no longer
  swallows exceptions raised by the ``__eq__`` method.

* Improved handing of invalid type encodings for struct types.

* Fix crash while handling a struct wrapper with an invalid
  type encoding.

* Fix handling of empty structs (such as ``struct foo { };`` in
  :func:`objc.repythonify`.

* The type for ``NSObject.pyobjc_instanceMethod`` and
  ``NSObject.pyobjc_classMethods`` now supports the GC protocol
  to avoid garbage collection issues when the value for these
  properties is stored as an attribute (which introduces a
  reference cycle)

* PyObjC should work with Python 3.11 alpha release, starting
  at alpha 6. Earlier alpha's are not supported due to reverting
  a workaround for a bug that was fixed in alpha 6.

* ``NSObject.alloc = 42`` now fails. It was already impossible
  to replace a selector by something else through instances
  (``NSObject.new().description = 42`` raises).

* Added :data:`objc.ObjCPointer.typestr` with the same
  value as :data:`objc.ObjCPonter.type`. The latter is now
  deprecated and will be removed in PyObjC 9.

* Better error messages when a class implementing a protocol
  inherits a method of the wrong kind ("class" vs. "instance").

* The value of ``__slots__`` in a class definition is now
  kept in the created class (previous versions always set
  the attribute to an empty tuple).

  This is primarily useful when ``__slots__`` is a :class:`dict`
  that is used to document attributes.

* Raise the correct exception when the name of a method is
  not an ASCII string.

* :func:`objc.loadSpecialVar` now better enforces that the
  *module_globals* argument is a Python dictionary.

* Fixed a crash in :func:`objc.loadSpecialVar` due to a
  missing pointer dereference.

* ``pip install pyobjc-framework-...`` for a framework
  that is not present on the current machine will now
  give a better error message when the "wheel" package
  is not installed.

* Setting an integer option in :data:`objc.options` to
  a value of an incompatible type (such as a string) will
  now raise an exception as intended, instead of breaking
  the interpreter.

* Trying to delete an attribute from ``objc.options``
  now raises ``AttributeError`` instead of ``TypeError``.

* :class:`objc.selector` now copies the default signature
  from its argument when that argument is another :class:`objc.selector`.

  Until now this would raise an exception.

* Added some missing error checking in calls to :c:func:`PyObject_New`
  and :c:func:`PyObject_GC_New`.

* It is now possible to create an :class:`objc.selector` from
  a callable that is not a function or bound method. This may
  require specifying the method signature in the call
  to :class:`objc.selector`.

* For pyobjc-core the ``build_ext`` command in ``setup.py``
  now includes the command-line option from the standaard
  command, which means ``python setup.py build_ext -j 4``
  can now be used for parallel builds.

  On my M1 laptop using ``python setup.py build_ext -j 8``
  halves the time needed to build the extension.

* The ``test`` command ``setup.py`` now supports
  the ``-v`` option to print test cases while they are run,
  in previoius versions this required using the ``--verbosity``
  option.

* Improve error handling when dealing with "isHidden" selectors.

* Added ``pyobjc_hiddenSelectors(classmethods)`` to :class:`objc.objc_class`

  This method returns a copy of the dictionary with "hidden" selectors,
  that is Objective-C selectors that are hidden from view.

  The method is primarily a debugging aid for development of
  PyObjC itself.

* :issue:`456`: ``ApplicationServices.AXIsProcessTrustedWithOptions`` and
  ``Quartrz.CGPDFArrayGetObject`` had incorrect metadata.

  The testsuites for the various framework bindings now have a test
  that does some basic checks on function and selector metadata. This
  test found the problem with ``CGPDFArrayGetObject``.

* Added :data:`objc._C_ATOMIC` and :data:`objc._C_COMPLEX`, both
  extracted from the clang sources after finding some type encodings
  that PyObjC could not decode.

  :data:`objc._C_ATOMIC` is ignored by PyObjC (for now), and
  :data:`objc._C_COMPLEX` is not yet supported.

* :issue:`456`: Fix internal error for ``_C_OUT`` argument markup on
  arguments that are CoreFoundation types.

  This can only happen with invalid metadata definitions in framework
  bindings, and earlier versions this resulted in an internal
  assertion error. With this change the "output" argument is always
  ``None`` in the result.

* :issue:`463`: Fix metadata for a number of functions with a C string argument

  The metadata for the following functions was changed to have
  the correct type encoding for string argument, to fix issues with
  using non-ASCII (byte) strings.

  - ApplicationServices.PMWorkflowSubmitPDFWithOptions
  - CoreServices.LocaleRefGetPartString
  - Foundation.NSGetSizeAndAlignment
  - Network.nw_advertise_descriptor_create_bonjour_service
  - Network.nw_browse_descriptor_create_bonjour_service
  - Network.nw_browse_descriptor_get_bonjour_service_domain
  - Network.nw_browse_descriptor_get_bonjour_service_type
  - Network.nw_connection_copy_description
  - Network.nw_content_context_create
  - Network.nw_content_context_get_identifier
  - Network.nw_endpoint_copy_address_string
  - Network.nw_endpoint_copy_port_string
  - Network.nw_endpoint_create_bonjour_service
  - Network.nw_endpoint_create_host
  - Network.nw_endpoint_create_url
  - Network.nw_endpoint_get_bonjour_service_domain
  - Network.nw_endpoint_get_bonjour_service_name
  - Network.nw_endpoint_get_bonjour_service_type
  - Network.nw_endpoint_get_hostname
  - Network.nw_framer_create_definition
  - Network.nw_framer_message_access_value
  - Network.nw_framer_message_copy_object_value
  - Network.nw_framer_message_set_object_value
  - Network.nw_framer_message_set_value
  - Network.nw_framer_options_set_object_value
  - Network.nw_listener_create_with_port
  - Network.nw_privacy_context_create
  - Network.nw_quic_get_application_error_reason
  - Network.nw_quic_set_application_error
  - Network.nw_txt_record_access_key
  - Network.nw_ws_options_add_additional_header
  - Network.nw_ws_options_add_subprotocol
  - Quartz.CGContextSelectFont
  - Quartz.CGContextShowText
  - Quartz.CGContextShowTextAtPoint
  - Quartz.CGDataProviderCreateWithFilename
  - Quartz.CGPDFArrayGetName
  - Quartz.CGPDFContentStreamGetResource
  - Quartz.CGPDFDictionaryGetArray
  - Quartz.CGPDFDictionaryGetBoolean
  - Quartz.CGPDFDictionaryGetName
  - Quartz.CGPDFDocumentUnlockWithPassword
  - Quartz.CGPDFScannerPopName
  - Quartz.CGPDFTagTypeGetName

  While fixing this issue I found problems with the metadata for these functions:

  - CoreMIDI.MIDIExternalDeviceCreate
  - CoreMedia.CMBlockBufferAccessDataBytes
  - CoreMedia.CMBlockBufferGetDataPointer
  - CoreMedia.CMBufferQueueInstallTriggerHandler
  - CoreMedia.CMBufferQueueInstallTriggerHandlerWithIntegerThreshold
  - CoreMedia.CMTextFormatDescriptionGetJustification
  - CoreServices.TECGetTextEncodingFromInternetNameOrMIB
  - DVDPlayback.DVDGetScanRate
  - MediaAccessibility.MACaptionAppearanceAddSelectedLanguage

  There's also a new test that checks for this problem in all
  exposed functions.

* Fix incorrect reset of the "inline_list" attribute of the lazy importer,
  this could result in an incorrect TypeError when trying to access
  an non-existing attribute after looking at ``__all__``.

* Fix uniqueness of symbols exposed in the OpenDirectory bindings.

* Unhide manual bindings for Security.SecKeychainFindGenericPassword and
  Security.SecKeychainFindInternetPassword.

Version 8.4.1
-------------

* :issue:`455`: ``pip install pyobjc`` on a macOS 12.2 machine tried
  to install ``pyobjc-framework-ScreenCaptureKit``, which is
  only can be installed on macOS 12.3 or later.

* :issue:`456`: Fix bad metadata for ``HIServices.AXIsProcessTrustedWithOptions``

* Wheels were build with Xcode 13.3 RC

  There are no changes in framework bindings relative to
  PyObjC 8.4 because there are no relevant API changes in
  Xcode 13.3 RC.

Version 8.4
-----------

..note::

   The bindings for the Message and ServerNotification frameworks,
   which were removed in macOS 10.9, will be removed in PyObjC 9.

* Added bindings for ScreenCaptureKit (new in macOS 12.3)

* Updated framework bindings for the macOS 12.3 SDK.

  Based on Xcode 13.3 beta 3


* Reverted a change in 8.3: It is once again not possible to
  use the "is" operator to check if two proxies for an NSString
  refer to the same Cocoa object.

  The change in 8.3 changed long standng behaviour for mutable
  strings and may have caused unintended problems.

* :issue:`418`: Added :class:`typing.NewType` definitions to the
  various framework bindings for all enum types in Cocoa
  (such as ``NSComparisonResult``).

  Using this it is now possible to annotate methods returning
  such types, although it is not yet possible to type check
  this.

  For example:

  .. sourcecode:: python

     class MyObject(NSObject):
         def compare_(self, other: NSObject) -> NSComparisonResult:
             return NSOrderSame

  The actual representation of enum types is provisional
  and might change in the future.

* :issue:`440`: Added :class:`typing.NewType` definitions to the
  various framework bindings for all ``NS_STRING_ENUM``,
  ``NS_TYPED_ENUM`` and ``NS_TYPED_EXTENSIBLE_ENUM`` types in Cocoa.

* :issue:`432`: Fix compatibility check when a class implements protocol ``NSObject``.

  The following code used to fail the protocol implementation check:

  .. sourcecode:: python

     class AppDelegate( Cocoa.NSObject, protocols=[objc.protocolNamed("NSApplicationDelegate")]):
         pass

  The reason for this is that the type encodings for (at least) ``-[NSObject respondsToSelector:]``
  in the Objective-C runtime doesn't match the type encoding in ``@protocol(NSObject)`` (the
  former returns ``char``, the latter ``bool``).  The compatibility check now handles trivial
  differences like this.

* :issue:`428`: Class ``NSData`` now implements the API from :class:`bytes`. The methods that
  return bytes in :class:`bytes` also return bytes in ``NSData``. This may change in a
  future version.

  Class ``NSMutableData`` now implements the API from :class:`bytearray` as far as this
  doesn't conflict with the native API. In particular, ``NSMutableData.copy()`` returns
  an immutable copy (instance of ``NSData``), use ``NSMutableData.mutableCopy()`` to
  create a mutable copy.

  .. note::

     The implementation is mostly suitable for fairly small amounts of data as
     the Cocoa value is first copied into a Python value.

* ``NSData([1,2,3])`` and ``NSMutableData([1,2,3])`` now work the same
  as ``bytes([1,2,3])`` and ``bytearray([1,2,3])``.

* :issue:`334`: Workaround for catetory on NSMutableArray that introduces a conflicting pop method

  Some class in Cocoa can at times introduce an (undocumented) selector ``-pop``
  on subclasses of ``NSArray``, which conflicts with a convenience method that
  emulates :meth:`list.pop`. The version introduces a workaround for this by
  adding the convenience method to all (statically known) subclasses of NSArray.

  This is far from perfect, but fixes the problem for now.

* Fix memory manager API misuse

  PyObjC's :class:`str` subclass used the python allocator API incorrectly,
  causing an assertion failure when running tests with "``python3 -Xdev``",
  as well as a hard crash due to using the API without holding the GIL.

* :issue:`445`: Workaround for Python 3.11 support

  Workaround for `BPO-46891 <https://bugs.python.org/issue46891>`_, which causes
  a hard crash in the PyObjC testsuite. With this workaround the tests for
  pyobjc-core pass with python 3.11a5, but this does result into adding some
  implementation internals to the ``__dict__`` of framework wrappers when using
  Python 3.11

* Fix build error on macOS 10.9

* Fix :class:`str` implementation invariant in the :class:`objc.pyobjc_unicode`
  subclass.  With this fix the string consistency checks in debug builds of
  CPython pass.

* Fix exception handling when passing a bytes object to a C function
  with a byte buffer "inout" argument.

Version 8.3
-----------

This release contains a lot of small fixes dueo to the continued improvement
of test coverage for the C code in pyobjc-core.

* Backward incompatible change:

  ``-[OC_PythonDictionary setObject:value forKey:[NSNull null]]`` now sets
  key :data:`None` in the Python dictionary instead of ``NSNull.null()``.

  This is for consistency with ``-[OC_PythonDictionary objectForKey:]`` and
  other collection classes. Getting and setting key ``[NSNull null]`` now
  actually works.

* Backward incompatible change:

  ``-[OC_PythonDictionary removeObjectForKey:]`` now raises ``NSInvalidArgumentException``
  instead of Python's ``KeyError`` for missing keys. This matches the documented
  behaviour of ``NSDictionary``.

* Backward incompatible change:

  ``-[Protocol descriptionForClassMethod:]`` now only accepts selector names
  (such as ``b"description"``) as its argument, not instances of
  :class:`objc.selector`. This matches the behaviour of other methods
  with an argument of the C type ``SEL``.

* :func"`objc.namedSelector` and :func:`objc.typedSelector` now also work when
  the decorated function is a :func:`classmethod`.

* Fix build problem on macOS 10.14 or earlier

* The Objective-C proxy for a python :class:`int` is now always ``OC_PythonNumber``,
  in previous versions instances were proxied as ``NSNumber`` when the
  value was in the range of an ``unsigned long long`` that's outside of the
  range of a (signed) ``long long`` (that is, a value between
  ``2**63`` and ``2**64``).

* Two ``NSString*`` values in Objective-C are now proxied to the
  same :class:`objc.pyobjc_unicode` instance when the two pointers are
  equal in Objective-C.

  That is, given ``NSString* value1`` and ``NSString* value2``
  ``value1 == value2`` in Objective-C can be replaced by
  ``value1 is value2`` in Python.  In older versions of PyObjC
  this invariant was not maintained, requiring more involved code to
  check if two strings represent the same object.

  This invariant was already maintained for other instances of other
  Objective-C classes.

* The proxy for python's :class:`bytearray` (and other writable buffers) now
  supports the ``mutableBytes`` method in Objective-C.

  As a side effect of this ``OC_PythonData`` is now a subclass of
  ``NSMutableData`` instead of ``NSData``.

* Fixed retrieving an :class:`bytearray` value from a Cocoa archive

  In previous versions this resulted in garbage data.

* Instances of :class:`bytearray` can now be included in "secure" Cocoa archives

* Remove ``-[OC_PythonArray getObjects:inRange:]``, it is not part of the
  regular ``NSArray`` interface and was never used.

* The proxy for python datetime objects was rewritten to be a lot simpler.

  User visible changes:

  * The new implementation is more correct, the old implementation truncated
    timestamps at whole seconds.

  * Calculating in Objective-C (such as calling ``-[NSDate dateByAddingTimeInterval:]``
    will now always result in an ``NSDate`` value, not a Python value.

  * The proxy code now calls the "timestamp" method instead of "strftime" during
    conversion from Python to Objective-C.

* Adding :class:`datetime.datetime` and :class:`datetime.date`  instances to an
  archive now works, both for keyed and classic archives.

  For the exact types :class:`datetime.datetime` and :class:`datetime.date` the encoding
  is compatible with that of ``NSDate`` and supports ``NSSecureCoding`` as long as the
  values are not timezone aware.

  When communicating with pure Objective-C code any timezone information will be lost.

  Note that both :class:`datetime.datetime` and :class:`datetime.date` are
  represented as an ``NSDate`` in Objective-C land, even though this Objective-C has
  semantics of the latter class don't fully match that of the Cocoa class.

* Fix python internal error when the "module_globals" argument to
  :func:`objc.loadBundleFunctions` is not a :class:`dict`.

* Fix the result of :func:`inspect.signature` for :class:`objc.IMP`.

  In previous versions this included the implicit "selector" argument that isn't used
  by Python callers.

* Avoid crash when trying to load a "magic" cookie CoreFoundation value for a
  type unknown to the PyObjC bridge.

* Removed ``-[OC_PythonObject pyObject]``.

  The method is no longer used by PyObjC itself, and these proxy objects are considered
  a private API that may change at any time.

* Removed ``+[OC_PythonObject classForUnarchiver]``

  This method was present for compatibility with the ``NSObject`` interface, but isn't
  actually part of Cocoa.

* ``-[OC_PythonObject methodSignatureForSelector:]`` and
  ``+[OC_PythonObject methodSignatureForSelector:]`` now return ``nil`` instead of
  raising an exception when the queried selector does not exist. This matches
  the behaviour of ``NSObject``.

* Fix the metadata in the bindings for DiscRecording, Intents, SceneKit, and libdispatch
  to ensure that the ``__all__`` variable actually works.

* Eliminated usage of sscanf in pyobjc-core

  A possible user visible change is that the use of sscanf
  to parse an IPv4 address has been replaced by a call
  to ``inet_pton()``, which may affect different representations
  of an IPv4 address.

* ``OC_PythonSet`` now epxlictly calls set related methods instead
  of using C-API functions like :func:`PySet_Clear`. This simplifies
  the pyobjc-core code, and gives fewer problems with set subclasses.

* Fix the buffer size used to for "struct sockaddr" arguments

* Added ``objc._C_CFRange`` and ``objc._C_NSRange`` with the type
  encodings of the C types ``CFRange`` and ``NSRange``.

* Functions and methods where the length of a C array argument is passed
  in another argument (such as ``int function(int* buffer, size_t bufsize)``)
  now also work when the argument with the size is a pointer to
  a ``CFRange`` or a pointer to a ``char``.

* A :class:`memoryview` of an ``NSMutableData`` instance is now writable.

* Fix crash when trying to create an :class:`objc.informal_protocol` with
  a sequence of selectors that contains a value that isn't an instance
  of :class:`objc.selector`.

* :issue:`435`: Fix build problem with Xcode 13.3

  Xcode 13.3 introduces a new warning in ``-Wall``: ``-Wunused-but-set-variable``,
  and this found some code quality issues with PyObjC.

Version 8.2
-----------

This release contains a lot of little fixes due to improving
test coverage of the C code in pyobjc-core. These are mostly fixes
for edge cases that don't happen in normal programs.

* Reintroduce binary wheels for Python 3.6

  PyObjC 8.x still supports Python 3.6, but I didn't ship binary wheels
  until now.

  I plan to explicitly remove support for Python 3.6 in PyObjC 9, which
  will include updating package metadata to ensure that users of Python 3.6
  will keep using PyObjC 8.x.

* :issue:`414`: [Python 3.10] The representation for C structures, like
  ``Foundation.NSPoint`` now have a ``__match_args__`` attribute, which means
  it is now possible to use positional arguments to these types in match expressions.

  For example:

  .. sourcecode:: python

     from Foundation import NSPoint

     value = ...

     match value:
         case NSPoint(0, _):
             print("On the Y axis")

* The internal extension API between framework bindings and pyobjc-core has
  been cleaned up a little. Because of this extensions need to be
  recompiled for this version.

* :func:`objc.allocateBuffer` is deprecated, use :class:`bytearray` instead

  This function has always returned a bytearray object in Python 3 and it
  no longer necessary.

  As a side effect of this change the function is now implemented in Python
  instead of C.

* The private function ``objc._dyld_shared_cache_contains_path`` is now
  always available, and unconditionally returns :data:`False` on systems without
  a shared library cache.

* The private function ``objc._setClassExtender`` is now implemented in Python
  and will be removed in PyObjC 9.

* Removed private function ``objc._typestr2typestr``.

  This function was untested and is no longer used by PyObjC.

* Removed the selector ``supportsWeakPointers`` from a number of classes.

  This method may have been needed during Apple's transition to ARC, but is
  no longer document and I've never seen it called during testing on recent
  versions of the OS.

  Furthermore the custom implementation of ``retain`` and ``release`` in PyObjC
  is a thin wrapper around the default one with additional locking to avoid
  race conditions during deallocation.

* :func:`objc.recylceAutoReleasePool` will now restore the global release pool
  when called after calling :func:`objc.removeAutoreleasePool`.

* Removed ``objc.FSSpec``

  This is a wrapper for a C type that's only usable in 32-bit code, PyObjC
  no longer supports 32-bit.

* The default implementation of ``-copy`` for subclasses of Objective-C
  classes that implemented ``-copy`` (needed to adjust Python attributes)
  didn't consider that the superclass implementation of ``-copy`` may
  return an instance of a different class.  This caused a hard crash.

  The easiest way to trigger this bug: Create a subclass of NSMutableData
  in Python, create an instance of that class and call the ``copy`` method.

* The module ``PyObjCTools.TestSupport`` was modernized a little

  This most visible part of this is that a number of functions and assertion
  method have been removed because they have a better alternative in the
  :mod:`unittest` library.

* :issue:`404`: Instances of the Python representation of C structs can now be pickled.

  That is, instances of ``AppKit.NSPoint``, ``Foundation.NSRange``, etc. can
  be pickled. The exception are a number of types in the CoreAudio bindings
  that have manual wrapper types instead of the generic support in pyobjc-core.

* Switch to :c:func:`PyCapsule_Import` to load the PyObjC API object in
  extension modules.

* Fix crash when calling ``objc.FSRef.from_pathname()`` with a path
  that cannot be encoded in the filesystem encoding (UTF-8).

* Fix name of opaque pointer type wrappers (such as ``Foundation.NSZonePtr``)

  The "__name__" and "__qualname__" attributes were correct, but the
  corresponding slot in the C struct of the type could point to
  no longer valid memory.

* Function :func:`objc.registerABCForClass` now actually works

* Fix bug in lazyloader where fetching the module's ``__all__`` could
  raise :exc:`AttributeError` for some particular constants.

* :issue:`317`: Cleanup code dealing with libffi closures APIs on various versions
  of macOS.

* If fetching the ``__pyobjc_object__`` attribute during conversion from
  Python to Objective-C raisea an exception other than :exc:`AttributeError`
  the conversion will fail.

  In previous versions the attribute was ignored when this happens.

* Fix error in ``__str__`` and ``__repr__`` of an Objective-C instance
  when the class' ``description`` selector returns ``nil``.

* Fixed crash in conversion of an Objective-C exception to a Python
  exception when the exception name is ``NULL``.

* Type encoding that ends with an incomplete pointer definition will
  now raise an error earlier, in particular before the first time the
  callable is used.

* Using a value for the metadata dict of functions and selectors that
  is not a :class:`dict` now raises an exception instead of being silently
  ignored.

* The "suggestion" function metadata was ignored for :class:`objc.function`
  instances using the fast FFI variant.

* Deprecating the function returned by an API exposed through :class:`objc.function`
  would cause a crash.

* Fix value of the "deprecated" key in the result of ``__metadata__()`` for
  callables that are deprecated in a macOS version.

* Loading metadata for a function with more than 63 arguments would
  crash the interpreter.

  Note that calling such function is not supported even with this bugfix.

* :issue:`406`: The "docstring" field in the function list argument for
  :func:`objc.loadBundleFunctions` was effectively ignored. It is now
  part of the document string (``__doc__``) of the :class:`objc.function`
  object.

* Actually implemented cyclic GC support in :class:`objc.python_method`.

* Fix crash when calling ``-[NSObject dealloc]``, ``-[NSObject retain]``
  or ``-[NSObject release]`` though an :class:`objc.IMP`, for example:

  .. sourcecode:: python

     anObject = NSObject.alloc().init()
     retain = anObject.methodForSelector_("retain")
     retain(anObject)

* Tests in pyobjc-core better check the message of raised exceptions

  This resulted in some minor changes in messages, this should not affect
  code using PyObjC.

* Fix the ``__name__`` and ``__repr__`` result for the exact class
  :class:`objc.objc_object`.

* Fix use of uninitialized variable in the code that converts a C struct
  from Objective-C to a Python tuple.

* Added :func:`PyObjCTools.TestSupport.no_autorelease_pool` to disable
  autorelease pool management by the test runnner for a specific test.

* ``NSMutableArray.insert(idx, value)`` would fail when ``idx`` is beyond
  the length of the array. It now behaves the same as :meth:`list.insert`,
  the item will be appended to the array.

* Change the way type specific class methods are added to :class:`objc.ivar`.

  This changes the way class methods are added to :class:`objc.ivar` to
  be more correct in the CPython interpreter.

* :issue:`425`: Fix CoreMIDI bindings

  The CoreMIDI is a wheel with a limited ABI tag, but one of the two
  extensions was build without using the limited ABI, resulting in a wheel
  that worked only for one python version.

Version 8.1
-----------

* Added a "flush" method to :class:`objc.FILE`

* :meth:`objc.FILE.readline` would crash if the file is closed in Python.

* Instance variable descriptors can now be retrieved from a class. That
  is, given:

  .. sourcecode:: python

     class SomeClass(NSobject):
         myvar = objc.ivar("myvar")

  It is now possible to access ``SomeClass.myvar``, in previous versions
  this raised :exc:`TypeError`.

* ``SomeClass.alloc()`` would raise an internal error in PyObjC 8 when
  this method returned ``nil``.

* :issue:`399`: Fix error message when passing wrong number of arguments in a
  call of an Objective-C method

* :issue:`399`: Disable support for ``Py_TPFLAGS_METHOD_DESCRIPTOR`` in
  :class:`objc.selector` and :class:`objc.python_method`.

  I'm looking for a better solutions, but for now this is needed
  to avoid problems in code that stores a bound selector as class
  attribute.

* :issue:`401`: ``AppKit.NSCenterTextAlignment`` and ``AppKit.NSRightTextAlignment``
  had a wrong value for arm64 systems.

* Update framework bindings for Xcode 13.2 (macOS 12.1 SDK)

* PyObjC now works correctly on macOS 11 or later when compiled on macOS 10.15
  or earlier.

* All messages from the deprecated module PyObjCTools.Signals are now
  printed on stderr.

* PyObjCTools.MachSignals won't cause an interpreter error when the
  signal dictionary doesn't contain a handler for a signal.

* ``value in someNSPoint`` works again, instead of hanging the interpreter.

Version 8.0
-----------

Backward incompatible changes
.............................

* In PyObjC 7 and earlier it was possible to leave out "output" arguments when
  calling a method with a Python implementation:

  .. sourcecode:: python

      class MyClass(NSObject):

          @objc.typedSelector(b"@@:o^@")
          def methodWithOutput_(self, a):
              return 1, 2


      o = MyClass.alloc().init()
      print(o.methodWithOutput_())

  This no longer works, it is always necessary to pass in all arguments, which
  was already true for methods implemented in Objective-C. That is:

  .. sourcecode:: python

     print(o.methodWithOutput_(None))

  This change both simplifies the PyObjC code base and was required to cleanly
  implement vectorcall support (see the section on performance below).

* Removed bindings for ``InterfaceBuilderKit``. This was a way to integrate
  with InterfaceBuilder in old versions of Xcode, but support for that was
  dropped before the release of Mac OS X 10.8.

* Bindings for the Objective-C runtime API related to "associated objects" is
  now enabled unconditionally. This will cause problems when running or building
  on macOS 10.6 or earlier.

* It is no longer possible to deploy to macOS 10.7 or earlier when you attempt to
  create a formal protocol. Protocol creation already failed on those platform
  due to lack of the required runtime API, and that will now result in a crash
  because PyObjC no longer checks for availability of that runtime API.

* :issue:`371`: Remove manual bindings for a number of old CoreGraphics APIs

  The following functions are no longer available:

  * ``CGDataProviderCreate``

  * ``CGDataProviderCreateDirectAccess``

  These functions were removed as a public API in macOS 10.8, but were still
  available through PyObjC through old backward compatibility code. That code has
  now been removed.

* For compatibility with Python's socket APIs functions that return a
  "struct sockaddr" (either by reference or as a function result) will now
  encode the IP address as a string and not a bytes object.

* The (undocumented) API in pyobjc-api.h (used in some framework bindings to
  integratie with pyobjc-core) has changed in an incompatible way, in particular
  the API for "caller" functions now mostly mirrors the vectorcall convention.

* Adding a method with a double underscore name will now raise an exception at
  class definition time instead of silently not creating the Objective-C method.

  .. sourcecode::

        class AClass (NSObject):
            ...

        def __foo_bar__(self, a, b, c):
            pass

        MethodNamesClass.__foo_bar__ = __foo_bar__


   Before PyObjC 8 this would add a ``__foo_bar__`` selector to the Python
   representation of the class without adding a selector to the Objective-C class.

   Use :func:`objc.python_method` to mark this as a python-only function.

Upcoming incompatible changes
.............................

* The module :mod:`PyObjCTools.Signals` is deprecated and will be removed
  in PyObjC 9.

* :func:`objc.initFrameworkWrapper` and :func:`objc.parseBridgeSupport`
  are deprecated and will be removed in PyObjC 9.

  These functions implement support for ".bridgesupport" XML files,
  something that PyObjC hasn't used itself in a number of releases (in
  part because system versions of those files are at best incomplete).


Performance
...........

Most performance changes use features introduced in Python 3.9, performance
in older Python versions is unchanged except for the effects of general cleanup.

* Implement the "vectorcall" protocol for :class:`objc.function`, :class:`objc.WeakRef`,
  :class:`objc.selector`, :class:`objc.IMP`, :class:`objc.python_method`.

  This reduces the interpreter overhead for calling instances of these objects.

* Implement Py_TPFLAGS_METHOD_DESCRIPTOR for :class:`objc.selector`,
  :class:`objc.python_method`.

* Use vectorcall in the method stub that forwards Objective-C calls to Python.

* Convert internal calls into Python to the vectorcall protocol (pyobjc-core)

* Add more optimized vectorcall implementation to :class:`objc.function`,
  :class:`objc.IMP` and :class:`objc.selector` for simpler callables.

  In the current version "simpole enough" callables have a 8 or fewer
  arguments, and none of those arguments are pass by reference. This will
  change over time.

Generic Implementation Quality
..............................

* :issue:`391`: Fix some spelling errors found by the
  `codespell <https://pypi.org/project/codespell/>`_ tool.

  The codespell tool is also run as part of pre-commit hooks.

* :issue:`296`: use clang-format for Objective-C code

  The Objective-C code for the various extensions has been reformatted
  using clang-format, and this enforced by a pre-commit hook.

* :issue:`374`: Use pyupgrade to modernize the code base

  This is enforced by a pre-commit hook.

* :issue:`388`: Added "nullability" attributes to Objectice-C sources for pyobjc-core.

  This gives the compiler and clang static analyzer more information
  that can be used to pinpoint possible bugs in the implementation. As a
  side effect of this a number of internal checks were strengthened, although
  most of them were for error conditions that should never happen.

  That said, this change also found a number of places where Python reference
  counts weren't updated properly, which may have led to refcount overflows
  in long running programs.

* Add more error checking to pyobjc-core to catch (very) unlikely error conditions.

  This is a side effect of the previous item.

New features
............

* Updated framework bindings for macOS 12

* New framework bindings for the following frameworks:

  - AudioVideoBridging (introduced in macOS 10.8)

  - DataDetection (introduced in macOS 12.0)

  - IntentsUI (introduced in macOS 12.0)

  - LocalAuthenticationEmbeddedUI (introduced in macOS 12.0)

  - MailKit (introduced in macOS 12.0)

  - MetricKit (introduced in macOS 12.0)

  - ShazamKit (introduced in macOS 12.0)


* :issue:`318`: Implement support for ``__class_getitem__`` for Objective-C classes

  The result of this is that effectively all Objective-C classes can be used
  as generic classes, without runtime type checking. This is meant to be used
  with optional type checking (for example MyPy)

  Usage:

  .. sourcecode:: python

        def create_integers(count: int) -> NSArray[int]:
            return NSArray[int].arrayWithArray_([i for i in range(count)])

  .. note::

     This requires typing stubs for framework bindings to be really useful,
     and those do not yet exist.


* :issue:`354`: Add an option to install all framework bindings, including those not
  relevant for the current platform. To use this:

  .. sourcecode:: sh

     $ pip install 'pyobjc[allbindings]'


Other changes and bugfixes
..........................

* :issue:`390`: pyobjc-core is no longer linked with the Carbon framework.

  Due to implicit dependencies this also required a change to the Metal
  bindings: those now import AppKit instead of Foundation.

* PyObjC only ships "Universal 2" wheels for Python 3.8 and later. Those work
  with single-architecture builds of Python as well.

* PyObjC 8 only ships with source archives and "univeral2" binary
  wheels (Python 3.? and later). There are no longer "x86_64" binary wheels.

* The *AVFoundation* bindings (in ``pyobjc-framework-AVFoundation``) now have
  an install dependency on the *CoreAudio* bindings (``pyobjc-framework-CoreAudio``).

  This is needed for a new API introduced in macOS 12.

* :issue:`371`: Link extensions in the Quartz bindings to the Quartz frameworks

  A number of C extensions in the Quartz bindings package were not
  linked to a framework. Those now link to the Quartz framework.

* :issue:`378`: Fix raising ``ImportError`` when doing ``from ApplicationServices import *``

  The root cause for this were private classes in system frameworks that contain
  a dot in their name (for example ``Swift.DispatchQueueShim``. Those names are
  both private and invalid attribute names.

* Creating protocols that contain methods that have a method signature containing
  PyObjC custom type encodings now works (those encodings are translated to
  the corresponding Objective-C encoding.

* Fix bindings for ``SKIndexCopyDocumentRefsForDocumentIDs``, that binding
  didn't work due to a typo in the metadata.

* :issue:`365`: The ``PyObjCTools`` namespace package no longer has an ``__init__.py``
  file in the source tree (that is, the tree switches to implicit namespace
  packages instead of the older setuptools style for namespace packages).

  This primarily affects testing with recent versions of pip/setuptools (which
  seem to no longer install the ``__init__.py`` file for namespace packages).

* ``development-support/run-testsuite`` now uses ``venv`` instead of
  ``virtualenv``. This removes a development dependency.

* :pr:`367`: Tweak the code that calculates ``PyObjC_BUILD_RELEASE`` in
  the various setup.py files to deal with versions with more than two
  labels (can happen when building using Xcode 13 beta)

  PR by Eric Lin (Tzu Hsiang Lin), github user eric100lin.

* ``PyObjCTest.TestSupport`` now never uses "10.16" as the
  OS release but always uses the actual platform version, even
  when Python was compiled using an old SDK.

* Adjusted PyObjC testcases to check for 11.0 instead of 10.16
  now that testsupport uses the real platform version.

* :issue:`385`: Fix race condition the lazy importer

  When two threads simultaneously try to get an attribute from a framework
  binding one of them might fail with an attribute error because information
  for resolving the name was removed before actually resolving the name.

* Fix various issues with invalid indices in :class:`objc.varlist`

* Fix support for ``AF_UNIX`` in the support code for ``struct sockaddr``.

* The implementation for opaque pointer types (such as the proxy for
  ``NSZone*``) has switched to :c:func:`PyType_FromSpec`.

* The :meth:`objc.FSRef.from_path` and :meth:`objc.FSRef.as_pathname`,
  methods now use the filesystem encoding instead of the default encoding.
  C string.  This shouldn't affect any code, both encoding default to UTF-8 on macOS.

* Inheriting directly from :class:`objc.objc_object` now raises :class:`TypeError`
  instead of :class:`objc.InternalError`. User code should always inherit from
  a Cocoa class.

Version 7.3
-----------

* :issue:`356`: Explicitly error out when building for unsupported architectures

  "python setup.py build" will now fail with a clear error when
  trying to build PyObjC for a CPU architecture that is no longer
  supported (such as 32-bit Intel)

* :issue:`319`: Use memset instead of bzero in C code to clear memory

  Based on a PR by GitHub user stbdang.

* :issue:`348`: Fix platform version guard for using protocols in
  MetalPerformanceShaders bindings

* :issue:`344`: Fix test for CFMessagePortCreateLocal

  The tests didn't actually test calling the callback function
  for CFMessagePortCreateLocal.

* :issue:`349`: Change calls to htonl in pyobjc-core to avoid compiler warning

  The original code had a 32-bit assumption (using 'long' to represent
  a 32-bit value), and that causes problems for some users build from
  source.

* :issue:`315`: Fix binding for ``SecAddSharedWebCredential`` (Security framework)

  Trying to use this function will no longer crash Python.

* :issue:`357`: Calling ``Metal.MTLCopyAllDevices()`` no longer crashes

  The reference count of the result of this function was handled incorrect,
  causing access to an already deallocated value when the Python reference
  was garbage collected.

* :issue:`260`: Add manual bindings for AXValueCreate and AXValueGetValue in ApplicationServices

  Calling these crashed in previous versions.

* :issue:`320`, :issue:`324`: Fix the type encoding for a number of CoreFoundation types in the Security bindings

* :issue:`336`: Add core support for 'final' classes

  It is now possible to mark Objective-C classes as final,
  that is to disable subclassing for such classes.

  This is primarily meant to be used in framework bindings for
  matching Objective-C semantics.

  This adds two new APIs:

  1. A keyword argument "final" when defining a new class::

        class MyClass (NSObject, final=True):
            pass

  2. An read-write attribute "__objc_final__" on all subclasses
     of NSObject.

  Note that this is a separate concept from :func:`typing.final`.

Version 7.2
-----------

* Update bindings for the macOS 11.3 SDK

  This SDK introduces a separate ``AVFAudio`` framework, but
  PyObjC continues to expose these APIs through the
  ``AVFoundation`` bindings.

Version 7.1
-----------

* Update bindings for the macOS 11.1 SDK

* Add bindings for framework "AdServices" (new in macOS 11.1)

* :issue:`333`: Improve SDK version detection in framework bindings

Version 7.0.1
-------------

* :issue:`337`: PyObjC doesn't work on Catalina or earlier

  Fix by Lawrence D'Anna.

Version 7.0
-----------

* This version drops support for 32-bit executables, both
  the core bridge and the framework wrappers only support
  64-bit executables going forward

* PyObjC is now always build with the system libffi.

* Removed metadata for 32-bit systems

* Existing framework bindings were updated for the macOS 11 SDK

* Added bindings for the following frameworks:
  - Accessibility (introduced in macOS 11.0)
  - AppTrackingTransparency (introduced in macOS 11.0)
  - CallKit (introduced in macOS 11.0)
  - ClassKit (introduced in macOS 11.0)
  - KernelManagement (introduced in macOS 11.0)
  - MetalPerformanceShaders (introduced in macOS 10.13)
  - MetalPerformanceShadersGraph (introduced in macOS 11.0)
  - MLCompute (introduced in macOS 11.0)
  - PassKit (introduced in macOS 11.0)
  - ReplayKit (introduced in macOS 11.0)
  - ScreenTime (introduced in macOS 11.0)
  - UniformTypeIdentifiers (introduced in macOS 11.0)
  - UserNotificationsUI (introduced in macOS 11.0)
  - Virtualization (introduced in macOS 11.0)

* Dropped the bindings to the QTKit framework

  This framework was removed in macOS 10.15.

  These bindings contained a C extension and cannot be build with recent
  versions of Xcode.


* Dropped the bindings for the XgridFoundation framework

  This framework was removed in macOS 10.8.

* Updated ``objc.dyld_library`` and ``objc.dyld_framework`` to return
  a sane result on macOS 11 where system libraries are no longer at
  the expected location, but in a shared cache.

* Another attempt at giving a nice error message when trying to install on
  platforms other than macOS.

Version 6.2.2
-------------

* :issue:`311`: Build for the Metal bindings failed on macOS 10.14

* :issue:`309`: Fix incompatibility with macOS 11 in framework loader

* The classifiers now correctly identify supported Python versions

* :pr:`301`: pyobjc-framework-Metal build failed on macOS mojave

* Python 3.10 support: Don't assume the result of Py_REFCNT, Py_SIZE and Py_TYPE are an lvalue.

* Python 3.10 support: Completely phase out use of old buffer API, which will
  be removed in Python 3.10.

  As a side effect of this a number of extensions that used the limited ABI once again
  use the regular ABI.

* Removed remnants of support for i386, ppc and ppc64 from pyobjc-core.

* Added type to manage ``Py_buffer`` lifetimes to the internal API in pyobjc-core, to be used
  by framework wrappers.

* Add ``objc._C_BYREF``. This definition was missing, but isn't used in modern ObjC code.

* :pr:`323`: Remove leading slashes from detected SDK patch to avoid miscalculating the version.

  Patch by GitHub user linuxfood.

* :pr:`322`: Avoid *None* error in PyObjCTools.AppHelper

  Patch by github user mintho

* :pr:`321`: Fix typo in documentation

  Patch by github user russeldavis

Version 6.2.1
-------------

* :issue:`299`: Ensure package 'pyobjc' won't try to build the PubSub bindings on macOS 10.15

  Reported by Thomas Buchberger

* Minor tweaks to build and pass tests on macOS 10.14 with the latest Xcode
  that can be installed on that version of macOS.

* :issue:`300`: Fix SystemError in block edge case

  PyObjC raised a SystemError when converting a callable into
  an ObjC block when the callable is a bound method without
  positional arguments.

* :issue:`275`: Fix crash on catalina caused by writing to read-only memory.

   Patch by Dan Villiom Podlaski Christiansen

* :pr:`302`: Make sure the SDK detection works when the version is not in the SDK name

  Patch by Joshua Root

* There were no SDK updates in Xcode 11.5 and Xcode 11.6 (beta)

Version 6.2
-----------

* The project has moved from Bitbucket to Github

* Remove most remnants of Python 2 support

* Clean up code quality issues found using flake8

* Add pre-commit hook to run black on all Python code.

* :issue:`290`: Fix protocol conformance testing when explicitly implementing a protocol

  Before this bugfix a class explicitly conforming to a protocol could not
  implement any method that wasn't declared in the protocol, the bridge would
  erroneously raise an exception when checking the additional method.

  Issue reported by Georg Seifert.

* :issue:`289`: Fix Python 3 issues in ``PyObjCTools.Conversion``

  Reported by vinolin asokan.

* ``PyObjCTools.Conversio.propertyListFromPythonCollection`` didn't
   recursively convert members of lists and tuples.

* ``PyObjCTools.Conversio.propertyListFromPythonCollection`` and
  ``PyObjCTools.Conversio.pythonCollectionFromPropertyList`` now
  support sets.

* Update metadata for Xcode 11.4 (beta 2)

* Added bindings for framework ``AutomaticAssessmentConfiguration.framework``
  introduced in macOS 10.15.4

* :issue:`298`: In some cases the compiler uses the type encoding "^{NSObject=#}"
  instead of "@".

  Reported by Georg Seifert.

* :issue:`264`: Added bindings for the Metal framework (new in macOS 10.11)

* Most framework bindings now use the limited ABI for the included C extensions,
  reducing the number of wheels that are needed. The exception are
  the bindings for Cocoa, Quartz and libdispatch, those use functionality not
  available in the limited ABI.

  The bridge itself (pyobjc-core) still uses the full CPython API.

  The CoreAudio bindings also don't use the limited ABI for now, those
  need more work to work with that ABI.

Version 6.1
-----------

* Updated for the macOS 10.15.1 SDK (Xcode 11.2)

* Fix reference counting in -[OC_PythonData length], which resulted
  in use-after-free.

* :issue:`281`: Fix problems found in pyobjc-core by the clang static analyser

Version 6.0.1
-------------

* :issue:`277`: Remove debug print accidentally left in production

* :issue:`278`: Suppress "-Wunguarded-availability" warnings in the extension
  AppKit._inlines


Version 6.0
-----------

* Removed Python 2 support from the C extension in pyobjc-core

* Reformatted code in pyobjc-core:

  - Use "black" for Python code
  - Use "clang-format" for Objective-C code

    As a side-effect of this all usage of "NS_DURING" and "PyObjC_DURING"
    has been replaced by the expansion of those macros, mostly because
    "clang-format" doesn't understand these kinds of blocks.

    Replacing "PyObjC_DURING" by its expansion also reduces the knowledge
    needed to understand what's going on w.r.t. the Python GIL.

    The macro "PyObjC_DURING", and its siblings, have been removed as well.

* Updated bindings for macOS 10.15 (Xcode 11.0)

* The userspace driver frameworks introduced in macOS 10.15
  (DriverKit and related frameworks) will not be exposed through
  PyObjC. Please let me know if you have a good
  use case for using these frameworks with Python.

* Add new framework wrappers for all other new frameworks
  in macOS 10.15:

  - AuthenticationServices
  - CoreHaptics
  - CoreMotion
  - DeviceCheck
  - ExecutionPolicy
  - FileProvider

    ``FileProvider.NSFileProviderItemFieldTrashed`` and ``NSFileProviderErrorVersionOutOfDate`` were dropped
    from the framework in macOS 11.

  - FileProviderUI
  - LinkPresentation
  - OSLog
  - PencilKit
  - PushKit
  - QuickLookThumbnailing
  - Speech
  - SoundAnalysis
  - SystemExtensions

* Add new framework wrappers for a number of older
  frameworks:

  - MetalKit (new in macOS 10.11)

* :issue:`271`: Fix crash when creating NSData objects on macOS 10.15

Version 5.3
-----------

* :issue:`21`: Switch xcodebuild invocation to xcrun for sdk path

  Patch by Clément Bouvier

* :issue:`271`: Fix crash when creating NSData objects on macOS 10.15

* Fix compile error on macOS 10.15

Version 5.2
-----------

* Updated metadata for Xcode 10.2

* :issue:`252`: ``objc.registerStructAlias`` no longer emits a deprecation
  warning because it is still used by the framework wrappers.

  The function is still deprecated though, the deprecation will reappear
  once the metadata has been updated.

* :issue:`75`: The core bridge now uses :func:`PyDict_GetItemWithError`, which
  may result in exceptions being raised that were previously swallowed.

* :issue:`247`: Partially switch to the new buffer API instead of the older
  Python 2 buffer API.

  The new implementation is more correct, but may keep Python objects
  alive longer than the previous implementation, and also affects
  buffer related functionality of Python objects. In particular, calling
  ``[someData bytes]`` on a Python object keeps the ``Py_buffer`` alive
  until the next flush of the autoreleasepool.

* :issue:`257`: Fix incorrect metadata for the callback argument to
  ``-[AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:]``.

* :issue:`258`: Add bindings to the "PrintCore" APIs from the ApplicationServices framework.

* Python 2: UserDict.UserDict instances are now bridged to instances of
  a subclass of NSDictionary.

Version 5.1.2
-------------

* :issue:`254`: Fix compile error on macOS 10.9 or earlier

* :issue:`255`: Calling completion handler failed due to incomplete runtime info

  PyObjC's metadata system didn't automatically set the call signature
  for blocks passed into a method implemented in Python. This causes problems
  when the ObjC or Swift block does not have signature information in the
  ObjC/blocks runtime.

* Use MAP_JIT when allocating memory for the executable stubs for Python
  methods.

  With the "restricted" runtime you'll have to add the "com.apple.security.cs.allow-jit"
  entitlement to use this flag, in earlier versions you'd have to use
  a different entitlement: "com.apple.security.cs.allow-unsigned-executable-memory".

  The MAP_JIT flag is only used on macOS 10.14 or later.

* Ensure that PyObjC can be built using /usr/bin/python on macOS 10.14

  This failed due the problems with header files in the SDK included with Xcode 10.


Version 5.1.1
-------------

* Update metadata for Xcode 10.1

Version 5.1
-----------

* Xcode 10 "GM" contains one difference from the last beta: the constant MLComputeUnitsCPUAndGPU
  in the CoreML bindings.

* :issue:`222`: Add a proxy for C's "FILE*" type on Python 3. This is not necessary on Python 2 because
  the default IO stack on Python 2 already uses FILE* internally.

  This proxy type is very minimal and shouldn't not be used for general I/O.

* Bindings are up-to-date w.r.t. Xcode 10.1 (beta)

* Updated the support code for framework wrappers to be able to emit deprecation warnings on
  the first import of a deprecated constants (functions and methods will only raise a deprecation
  warning when called).

  This is just an infrastructure change, the actual framework bindings do not yet contain the
  information used to emit deprecation warnings.

* Add metadata for deprecation warnings to the "Contacts" framework

* :issue:`252`: Import ABCs from ``collections.abc`` instead of ``collections`` because the latter is deprecated.

* :issue:`180`, :issue:`251`: Instances of most builtin value types and sequences (int, float, str, unicode, tuple,
  list, set, frozenset and dict) can now be written to archives that require secureCoding.

Version 5.0
-----------

Version 5.0 of PyObjC primarily adds support for macOS 10.14 (mojave), and
also adds support for a couple of older frameworks that weren't supported before.

Version 5.0b2
-------------

* Added manual bindings for MTAudioProcessingTapCreate and MTAudioProcessingTapGetStorage
  in the MediaToolbox bindings.

* Added manual bindings for CMIODeviceProcessAVCCommand and CMIODeviceProcessRS422Command
  in the CoreMediaIO bindings

* Added bindings for the VideoToolbox framework introduced in macOS 10.8

* Finished bindings for CoreMedia, I noticed during review that the bindings were
  far from finished.

* Fixed problem with uninitialized memory in pyobjc-core

* The CarbonCore bindings included a number of symbols that shouldn't be exposed

Version 5.0b1
-------------

* Bindings updated for Xcode 10 beta 6.

* Add a custom binding for a number of structure types in
  CoreAudio:

  - AudioBuffer
  - AudioBufferList
  - AudioChannelDescription
  - AudioChannelLayout
  - AudioValueTranslation

  With this patch using APIs with these types should actually
  work.

* :issue:`19`: Fix deprecation warning in bridgesupport support module

  Patch by: Mickaël Schoentgen

* Creating objc.ObjCPointer instances now results in a
  Python warning, instead of an unconditional message on
  stdout.

  .. note::

     The creation of these objects is a sign that APIs are
     not wrapped correctly, these objects are created for
     pointers where the bridge doesn't know how to handle
     them properly.

* System bridgesupport XML files (normally not used by PyObjC)
  can contain constant numbers with value "inf", PyObjC now
  knows how to handle those.

* Added bindings for the "Metadata" subframework of the
  "CoreServices" framework.

* Added bindings for the "CarbonCore" subframework of the
  "CoreServices" framework.

  Most APIs in this subframework are not available to Python,
  only those APIs that are not deprecated and seem interesting
  are exposed.

* The separate framework wrappers DictionaryServices,
  LaunchServices and SearchKit are deprecated, use
  the CoreServices bindings instead.

  These framework wrappers still exists, but are effectively
  aliases for CoreServices with this release. Because of this
  these bindings can expose more symbols than previously.

* Fix unexpected exception when trying to call getattr
  on a framework wrapped with a name that isn't a valid
  identifier.

* :issue:`244`: Bad metadata for CGPDFOperatorTableSetCallback

* :issue:`247`: Fix crash in regression test case

  One specific test in pyobjc-core crashed the interpreter
  when run separately. Because of this I've disabled an
  optimization that uses alloca instead of PyMem_Malloc to
  allocate memory for now.


Version 5.0a0
-------------

* Adds support for macOS 10.14 (Mojave)

  This release updates the framework wrappers with support
  for new APIs in macOS 10.14 and adds bindings for the following
  new frameworks:

  - AdSupport
  - CoreAudio (new in macOS 10.0)
  - CoreAudioKit (new in macOS 10.4)
  - CoreMedia (new in macOS 10.7)
  - CoreMediaIO (new in macOS 10.7)
  - DiscRecording (new in macOS 10.2)
  - DiscRecordingUI (new in macOS 10.2)
  - DVDPlayback (new in macOS 10.3)
  - MediaToolbox
  - NaturalLanguage
  - Network
  - OSAKit (new in macOS 10.4)
  - UserNotifications
  - VideoSubscriberAccount

- Support for CoreAudio, CoreMedia and MediaToolbox is limited
  in this release due to missing manual wrappers.

- Added two features that can help with gating code on the
  version of macos:

  1) The constants "objc.MAC_OS_X_VERSION_CURRENT" can be
     compared with one of the "objc.MAC_OS_X_VERSION\_..." constants.

  2) The function "objc.macos_avaiable(major, minor[, patch])"
     returns true if the current macOS version is at least the
     specified version, comparable with "@available" in Swift.

Version 4.2.2
-------------

* Update metadata for Xcode 9.4

* The binary release now includes wheels for both variants for the
  Python.org installer for python 3.6 and 3.7: 32- and 64-bit for
  macOS 10.6 or later, and 64-bit only for macOS 10.9 or later.

* Ensure the context manager for ``NSAnimationContext`` defined in
  ``PyObjCTools.AppCategories`` actually works.

* Fix convenience wrappers for ``Foundation.NSCache``.

* Fix convenience wrappers for ``Foundation.NSHashTable``.


Version 4.2.1
-------------

* Update metadata for Xcode 9.4 beta 2 (no changes)

* Restore autodetection of --with-system-ffi, but ignore this python setting
  for /usr/bin/python because Apple doesn't ship libffi headers.

Version 4.2
-----------

* Add bindings to the BusinessChat framework introduced in macOS 10.13.4

* Update metadata for Xcode 9.3

* :issue:`233`: Fix crash in Security.AuthorizationCopyRights() wrapper

* :issue:`234`: Fix crash in AuthorizationExecuteWithPrivileges() wrapper

  Reported by Vangelis Koukis

* Ensure doctest can work with modules containing subclasses of NSObject

  Reported by Just van Rossum

* :issue:`236`: Importing can sometimes fail in multi-threaded scenarios

  Fix by Max Bélanger

* Undeprecate treating struct wrappers as sequences. Removing this feature would
  break too much existing code, hence deprecating is not really an option. Furthermore,
  this would also break some nice idioms.


* :issue:`17`: Fix python 3 issues in PyObjCTools.AppHelper and PyObjCTools.Conversion

  Fix by Max Bélanger

Version 4.1
-----------

* Protection against buffer overflow and negative indexes in
  ``__getitem__`` and ``__setitem__`` for ``objc.varlist`` instances.

* Fix incorrect metadata for ``+[NSEvent addLocalMonitorForEventsMatchingMask:handler:]``

* Fix incorrect and misleading error message in the exception
  that is raised when return a value from a block that should not
  return a value.

* :issue:`223`: Fix hard crash when executing ``help(Cocoa)``

  Fetching the help for PyObjC framework wrappers isn't very useful due
  to the sheer size of the output (4.5 million lines of output for
  ``help(Cocoa)`` at the moment), but shouldn't cause a hard crash of
  the interpreter.

  Reported by Dave Fuller

* :issue:`218`: Explicitly cause an ImportError when reloading ```objc._objc```

  Reloading the PyObjC core extension now raises an ImportError because
  this cannot work and used to raise a rather vague error.

* Updated metadata for Xcode 9.2

* Added missing ```MAC_OS_X_VERSION_*``` constants

* Fix memory error in struct wrappers which resulted in
  a use-after-free error in the initializer for structs.

* :issue:`135`: Add bindings for frameworks :doc:`Security </apinotes/Security>`,
  :doc:`SecurityFoundation </apinotes/SecurityFoundation>` and
  and :doc:`SecurityInterface </apinotes/SecurityInterface>`.

  The bindings for the Security framework don't expose a
  number of older APIs that were deprecated in macOS 10.7.

* :issue:`129`: Add bindings to libdispatch.

  These bindings require macOS 10.8 or later, libdispatch was
  available earlier but macOS 10.8 changed the API in such a
  way that wrapping became a lot easier.

  .. note::

     Blocks scheduled using libdispatch are still subject to the
     Python GIL: just one block implemented in Python can run
     at any one time.

Version 4.0.1
-------------

* :issue:`213`: Fix signature for ```-[NSObject forwardInvocation:]```

  Reported by user "pyrocat"

* Updated metadata for Xcode 9.1

* Changes to PyObjCTools.TestSupport to be able to include/exclude tests
  based on the minor release of macOS.

* Some tweaks to fix test failures when running on OSX 10.5, 10.6, 10.9.

.. note::

   The stacktrace formatting of in ``PyObjCTools.Debugging`` (from the
   ExceptionHandling bindings) don't work for PPC binaries because symbol
   resolution doesn't work.

   This is a known issue that won't be fixed.

Version 4.0
-----------

* :issue:`204`: Metadata for CGPDFDictionaryGetObject was wrong

  Reported by Nickolas Pohilets.

* Updated metadata for Xcode 9 GM.

* :issue:`202`: Add bindings for ``CGPDFDictionaryRef``, ``CGPDFScannerRef``
  ``CGPDFStreamRef`` and ``CGPDFStringRef`` to the Quartz bindings (including
  some minor updates to function metadata)

  Reported by Nickolas Pohilets.

* :issue:`205`: Add ability to read bytes from ``objc.varlist``

  Instances of ``objc.varlist`` now have a method to return a memoryview
  that refers to the first section of the list::

     def as_buffer(self, count : int) -> memoryview

  This returns a memoryview the references the underlying memory for
  the first *count* elements in the list.

  Reported by Nickolas Pohilets.

* Added bindings for the :doc:`GameKit </apinotes/GameKit>` framework introduced in macOS 10.8.

* Added bindings for the :doc:`GameplayKit </apinotes/GameplayKit>` framework introduced in macOS 10.11.

  Note that these bindings are less useful than they could be because
  PyObjC currently does not support "vector" types that are used in
  some APIs.


Version 4.0b1
-------------

* Removed PyObjCTools.TestSupport.filterWarnings, use warnings.catch_warnings
  instead.

* Building pyobjc-core using "python setup.py develop" will use 'ccache'
  when available.

* Building pyobjc-core will compile the source files from new to old files,
  to speed up feedback while working on the source code.

* Legacy BridgeSupport files on macOS 10.13 (which aren't used by default
  by PyObjC) can contain junk data in typestring data. Cleanup that data
  before using it.

* Deal with loading bundle variables of a C string type, that used to crash
  to do an oddity of locating that information.

* Using wrappers for C structs as sequences is deprecated, this
  feature was introduced a long while ago when the framework wrappers
  were very incomplete and is no longer useful.

* Add ``objc.options.structs_indexable``. When this option is True
  (the default) wrappers for C structs behave as before, when the
  option is False these wrappers can no longer be used as writable
  tuples, that is all "sequence" methods will raise ``TypeError``.

* Add ``objc.options.structs_writable``. When this option is True
  (the default) wrappers for C structs behave as before, when the
  option is False these wrappers can no longer be modified.

* Add availability macro ``MAC_OS_X_VERSION_10_13`` to ``objc``.

* New framework wrappers:

  - :doc:`ColorSync </apinotes/ColorSync>` (new in macOS 10.13)
  - :doc:`CoreML </apinotes/CoreML>`  (new in macOS 10.13)
  - :doc:`ExternalAccessory </apinotes/ExternalAccessory>`  (new in macOS 10.13)
  - :doc:`CoreSpotlight </apinotes/CoreSpotlight>`  (new in macOS 10.13)
  - :doc:`Vision </apinotes/Vision>`  (new in macOS 10.13)

* metadata updates:

  - :doc:`Accounts </apinotes/Accounts>`
  - :doc:`AddressBook </apinotes/AddressBook>`
  - :doc:`AppKit </apinotes/AppKit>`
  - :doc:`ApplicationServices </apinotes/ApplicationServices>`
  - :doc:`Automator </apinotes/Automator>`
  - :doc:`AVKit </apinotes/AVKit>`
  - :doc:`CalendarStore </apinotes/CalendarStore>`
  - :doc:`CFNetwork </apinotes/CFNetwork>`
  - :doc:`CloudKit </apinotes/CloudKit>`
  - :doc:`Contacts </apinotes/Contacts>`
  - :doc:`CoreBluetooth </apinotes/CoreBluetooth>`
  - :doc:`CoreData </apinotes/CoreData>`
  - :doc:`CoreFoundation </apinotes/CoreFoundation>`
  - :doc:`CoreGraphics </apinotes/CoreGraphics>`
  - :doc:`CoreImage </apinotes/CoreImage>`
  - :doc:`CoreLocation </apinotes/CoreLocation>`
  - :doc:`CoreServices </apinotes/CoreServices>`
  - :doc:`CoreText </apinotes/CoreText>`
  - :doc:`CoreVideo </apinotes/CoreVideo>`
  - :doc:`CoreWLAN </apinotes/CoreWLAN>`
  - :doc:`CryptoTokenKit </apinotes/CryptoTokenKit>`
  - :doc:`EventKit </apinotes/EventKit>`
  - :doc:`FinderSync </apinotes/FinderSync>`
  - :doc:`Foundation </apinotes/Foundation>`
  - :doc:`FSEvents </apinotes/FSEvents>`
  - :doc:`GameController </apinotes/GameController>`
  - :doc:`IMServicePlugIn </apinotes/IMServicePlugIn>`
  - :doc:`ImageCaptureCore </apinotes/ImageCaptureCore>`
  - :doc:`ImageIO </apinotes/ImageIO>`
  - :doc:`Intents </apinotes/Intents>`
  - :doc:`IOSurface </apinotes/IOSurface>`
  - :doc:`JavaScriptCore </apinotes/JavaScriptCore>`
  - :doc:`LocalAuthentication </apinotes/LocalAuthentication>`
  - :doc:`MapKit </apinotes/MapKit>`
  - :doc:`MediaLibrary </apinotes/MediaLibrary>`
  - :doc:`MediaPlayer </apinotes/MediaPlayer>`
  - :doc:`ModelIO </apinotes/ModelIO>`
  - :doc:`MultipeerConnectivity </apinotes/MultipeerConnectivity>`
  - :doc:`NetFS </apinotes/NetFS>`
  - :doc:`NetworkExtension </apinotes/NetworkExtension>`
  - :doc:`OpenDirectory </apinotes/OpenDirectory>`
  - :doc:`Photos </apinotes/Photos>`
  - :doc:`PhotosUI </apinotes/PhotosUI>`
  - QTKit
  - :doc:`Quartz </apinotes/Quartz>`
  - :doc:`QuartzCore </apinotes/QuartzCore>`
  - :doc:`QuickLook </apinotes/QuickLook>`
  - :doc:`SafariServices </apinotes/SafariServices>`
  - :doc:`SceneKit </apinotes/SceneKit>`
  - :doc:`ScreenSaver </apinotes/ScreenSaver>`
  - :doc:`Social </apinotes/Social>`
  - :doc:`SpriteKit </apinotes/SpriteKit>`
  - :doc:`SystemConfiguration </apinotes/SystemConfiguration>`
  - :doc:`WebKit </apinotes/WebKit>`

Version 3.3
-----------

New features:

* :issue:`15`: Fix crash when handling stack blocks

  Patch by Max Bélanger.  Fixes a crash when a stackbased block is passed
  into python.

  Later updated with tests and a different implementation.

* :issue:`192`: 32/64-bit issue with AppHelper.endSheetMethod

  This helper decorator used the wrong signature string, which happens to
  work on 32-bit systems but not on 64-bit ones.

* "pip install pyobjc" should now fail with a better error message when
  installing on a system that isn't running macOS.

* Updated framework wrappers for the API changes in the SDK shipped with
  Xcode 8.3.2.

* Added new framework wrapper: "pyobjc-framework-CoreServices".

  This exposes no new functionality for now, but makes it possible to access
  the functionality exposed by the "CoreServices" framework by using "import
  CoreServices", instead of directly importing the name of the subframework.

* Added new framework wrapper: "pyobjc-framework-iTunesLibrary"

  This is a wrapper for the iTunesLibrary framework located in
  "/Library/Frameworks", which is a framework installed by iTunes that
  can be used to (read-only) access information about an iTunes library.

* :issue:`178`: Add basic example for the Contacts framework

  The Contacts framework now contains a very simple example that shows how
  to fetch contacts from the contact store.  Apple's documentation on
  the framework contains more comprehensive sample code, which should make
  it clear how to use the framework.

* Add initial support for deprecation warnings in metadata

  Metadata files can now contain information for deprecation warnings for
  methods and functions. Users can turn on deprecation warnings using::

    import objc
    objc.deprecation_warnings = objc.MAC_OS_X_VERSION_10_6

  This will emit deprecation warnings for APIs that were deprecated in
  macOS 10.6 (or earlier).

  Note that this version does have metadata that uses the new functionality,
  that will be added in a future release.

Bugfixes:

* The OC_Python* Objective-C classes used to expose Python objects to
  Objective-C don't support secure coding, added a
  "supportsSecureCoding" implementation to make this explicit.

* :issue:`182`: The block signature registered in the ObjC runtime
  datastructures for Python blocks was wrong, which confuses Objective-C
  code that looks at the runtime data.

* Fix requirement info in Collaboration setup.py.

  Patch by Alex Chekunkov.

* :issue:`189`: Invalid invocation of "atos" command on recent macOS versions

  The Objective-C exception logging code in pyobjc-framework-ExceptionHandling
  calls out to the "atos" command to get readable stack traces, that
  invocation caused problems on recent macOS versions.


Version 3.2.2
-------------

Bugfixes:

* :issue:`162`: Fix conversion of unicode python string to Objective-C "UniChar"
  array, it used to do the wrong thing when converting characters outside of
  the BMP.

  Fix by Ted Morin and Benoit Pierre.

Version 3.2.1
-------------

Updates:

* Small change to the shared setup.py code for framework wrappers to allow
  building wheels for wrappers without a C exention on any system.

  This was mostly done to make it easier to provide wheels in future releases.

Bugfixes:

* Avoid build error with Python 2.7 when using the OSX 10.12 SDK, triggered
  when Python was build using MacPython support.

* Compatibility definitions for MAC_OS_X_VERSION_10_10, MAC_OS_X_VERSION_10_11
  and MAC_OS_X_VERSION_10_12 were wrong, adjusted these.

* Fix obscure crash in test suite of pyobjc-core: the definition of a class
  that claims to conform to a protocol but didn't actually conform could
  result in having a partial class definition in the Objective-C runtime.

* Updated implementation for ``NSMutableArray.extend``. This both avoids an
  error with the list interface tests in Python 3.6, and avoids unnecessary
  memory usage with large arguments.


Version 3.2
-----------

**Backward compatibility note:** Due to a change in the way the default
method signature is calculated PyObjC is now more strict in enforcing
the Python<->Objective-C mapping for selectors and a number of code patterns
that were allowed before are no longer allowed, in particular the following
method definitions raise ``objc.BadPrototypeError``::

   class MyObject (NSObject):
      def mymethod(self, a, b): ...
      def method_arg_(self, a, b, c): ...

If these methods are only used from Python and are never used from Objective-C
the error can be avoided by decorating these methods with ``objc.python_method``::

   class MyObject (NSObject):
      @objc.python_method
      def mymethod(self, a, b): ...

This cannot be used for methods used from Objective-C, for those you will
have to rename the method or you will have to provide an appropriate selector
explicitly.

* Fix crash when using some APIs in the LaunchServices framework.

* :issue:`100`: Building with the Command Line Tools for Xcode installed caused build errors
  on OSX 10.10

* Python 3.6 made a change to the bytecode format that affected the way
  PyObjC calculates the default method signature for Python methods.

  Earlier versions of PyObjC will therefore not work properly with Python 3.6.

* Update metadata for macOS 10.12.1

  Note: Building PyObjC on macOS 10.12 requires Xcode 8.1 (or a later version)

* Added bindings for the SafariServices and Intents frameworks, both introduced in macOS 10.12.

* Added bindings for the MediaPlayer framework, introduced in macOS 10.12.1.

* Add bindings for the ModelIO framework, introduced in OSX 10.11.

* :issue:`153`: Add missing metadata file to ApplicationServices bindings

* :issue:`157`: Bad reference to "_metadata" in ApplicationServices bindings

* ApplicationServices framework didn't do "from ... import \*" as was intended.

* Don't force the installation of py2app.

* Fix build failure using the OSX 10.10 SDK.

* :issue:`21`: Tweak build procedure for PyObjC to avoid building pyobjc-core
  multiple times when using ``pip install pyobjc``.

* :issue:`123`: Use Twisted's cfreactor module in the examples using Twisted.

* :issue:`148`: Fix build issue for the MapKit bindings on a case
  sensitive filesystem.

* Added bindings for the IOSurface framework (pyobjc-framework-IOSurface)

* Added bindings for the NetworkExtension framework (pyobjc-framework-NetworkExtension)

* :issue:`149`: Fix compile problems with Anaconda

* Fix SystemError for accessing a method whose ``__metadata__`` cannot be calculated,
  found while researching issue :issue:`122`.

* :issue:`146`: Don't hang when running ``python setup.py build`` using PyPy.

  Note that PyPy still doesn't work, this just ensures that the build fails instead
  of hanging indefinely.

* :issue:`143`: Fix calculation of default type signature for selectors

  Due to this change it is possible to use decorators like this:

  .. sourcecode:: python

     def decorator(func):
        @functools.wraps(func)
	def wrapper(*args, **kwds):
	    return func(*args, **kwds)
	return decorator

  Before this patch PyObjC gave an error due to the signature of ``wrapper``,
  and if ``wrapper`` was defined with an explicit ``self`` argument PyObjC would
  not give an error but would calculate the wrong method signature for wrapped
  methods.

  An unfortunate side effect of this change is that the argument count
  of methods must now match the implied argument count of the selector, that is
  a method with name ``someMethod_`` must now have exactly two arguments (``self``
  and the argument implied by the underscore at the end).

  Use ``objc.python_method`` as a decorator for python methods that don't use
  this convention and do no need to be registered with the Objective-C runtime
  as Objective-C selectors.

* The bridge now considers the default arguments for a function when determining
  if the Python signature of a function is compatible with the Objective-C
  signature, that is the following method definition is valid::

    class MyObject (NSObject):
       def someMethod_(self, a, b=2): pass

* The default selector calculated for Python methods with embedded underscores and
  without a closing underscore has changed, the embedded underscores are not translated
  to colons because the resulting Objective-C selector would not be valid.

  That is, in earlier versions the default selector for "some_method" would be
  "some:method", and from this version on the default for selector for this
  method is "some_method".

* (Python 3) Methods and functions with keyword-only arguments that don't have defaults
  cause a ``objc.BadPrototypeError`` exception when proxied to Objective-C
  because those can never be called from Objective-C without causing an
  exception.


Version 3.1.1
-------------

* Sigh... A number for sdists were incomplete due to missing MANIFEST.in files.

Version 3.1
-----------

* Fix value of ``FLT_MAX`` and ``FLT_MIN`` in framework bindings.

* Fix for the functions in ``PyObjCTools.AppHelper``: those functions didn't work
  correctly when the calling thread didn't have a runloop.

  Patch by Max Bélanger.

* :issue:`126`: Load the LaunchServices definitions through the CoreServices
  umbrella framework to avoid problems on OSX 10.11.

* :issue:`124`: Sporadic crash at program shutdown due to a race condition between
  Python interpreter shutdown and Cocoa cleanup.

  This is mostly a workaround, I don't have a full solution for this yet and
  I'm not sure if one is possible.

* Added ``objc.PyObjC_BUILD_RELEASE`` which contains the version of the SDK
  that was used to build PyObjC in the same format as the OSX availability
  macros.

* :issue:`117`: Added *maxTimeout* parameter to ``PyObjCTools.AppHelper.runConsoleEventLoop``.
  The default value is 3 seconds, which means that
  the console eventloop will stop within 3 seconds of calling ``stopEventLoop``.

* Re-enable faster method calls for simple method calls.

* Support OSX 10.10 in PyObjCTools.TestSupport (version comparison was too
  naive)

* Add bindings for ApplicationServices, currently only the HIServices sub
  framework is exposed.

* Add bindings for NetFS, introduced in OSX 10.7.

* Add bindings for ImageCaptureCore. Initial patch by Max Bélanger.

* Add bindings for IMServicePlugIn, introduced in OSX 10.7.

* Add bindings for SceneKit, introduced in OSX 10.8.

* Add bindings for CoreBluetooth, MapKit, AVKit, MediaLibrary,
  MediaAccessibility, GameController (all new in OSX 10.9)

* Add bindings for FinderSync, CloudKit, CryptoTokenKit,
  MultipeerConnectivity, NotificationCenter (all new in OSX 10.10)

* Add bindings for Contacts, ContactsUI, Photos, PhotosUI (new in OSX 10.11)

* Added function ``objc.callbackPointer``.

* Updated bindings for AppKit, CoreData, CoreFoundation, CoreGraphics,
  CoreLocation, CoreText, CoreVideo, CoreWLAN, EventKit, FSEvents,
  ImageIO, ImageKit, JavaScriptCore, LaunchServices, OpenDirectory,
  PDFKit, QuartzComposer, QuartzCore, QuartzFilters, QuickLookUI,
  ServiceManagement, Social, StoreKit and WebKit with the new APIs
  introduced in OSX 10.9, 10.10 and 10.11.

* Unchanged framework bindings: Collaboration, DictionaryServices,
  ExceptionHandling, InputMethodKit, InstallerPlugins, InstantMessage,
  InterfaceBuilderKit, LatentSemanticMapping, PreferencePanes, PubSub.

  .. note::

     InterfaceBuilderKit will likely be removed in a future version of PyObjC

* TODO: DiskArbitration, GameController, SpriteKit bindings are incomplete

* Fix hard crash with invalid type strings in metadata.

* Default value for struct wrappers was incorrect for fields that have
  a type encoding that's custom to PyObjC.

* Fix a type string validation error that could cause PyObjC to continue
  processing beyond the end of a type string (which can effectively hang
  the python interpreter with 100% CPU usage)

* Fix edge-case in NSCoding support that causes PyObjC to use proxy objects
  of the wrong type in some cases.

* Fix incompatibility with Python 3.6 (where ``inspect.getargspec`` no longer
  exists)

* Added (private) function ``objc._copyMetadataRegistry``. This function returns
  a copy of the internal registry that's used to find additional information
  about method signatures.

  Note that the data structure returned by this function is subject to change,
  that the data structure is undocumented and that modifying it does not affect
  the data used by PyObjC.

Version 3.0.5
-------------

* PyObjC now uses the system libffi when CPython itself was compiled to
  use that version of libffi.

  Patch by Max Bélanger.

* :issue:`111`: BridgeSupport code failed when there are unions in the bridgesupport
  file due to a bug in the code that parses Objective-C encoded types.

* BridgeSupport code didn't work properly with Python 3.x

* Add objc.MAC_OS_X_VERSION_10_10 and MAC_OS_X_VERSION_10_9.

* :issue:`107`: The code that checked for compliance to formal protocols didn't look
  at parent classes to determine if a class implements the protocol.

* Fix build issue for python 3.

Version 3.0.4
-------------

* :issue:`102`, :issue:`103`: Fix installation on OSX 10.10 when using "pip install pyobjc".

* :issue`:95`: Fix crash when ``sys.modules`` contains an object that is not a string.

* Fix crash on OSX 10.8 or later when using a 32-bit build and accessing
  an instance of "Object" (that is, pre-Nextstep classes).

* :issue:`106`: Fix a crash when using blocks without metadata, but with a block
  signature from the block runtime.

* :issue:`109`: ``PyObjCTools.MachSignals`` likely hasn't worked at all since PyObjC 2.0
  because it uses a C module that was never ported to PyObjC 2.0. This private
  module is reintroduced in this release (with a slightly changed API)

Version 3.0.3
-------------

* Fix a number of OSX 10.10 support issues.

Version 3.0.2
-------------

* :issue:`99`: Installation failed with recent versions of setuptools due to
  invalid assumptions in the PyObjC setup script.

* :issue:`93`: For a objc.PyObjCPointer object ``ptr.pointerAsInteger`` returned
  a 32-bit value on 64-bit systems.

* :issue:`92`: Removed dependency on pyobjc-framework-GameKit from the pyobjc
  package, GameKit isn't packaged yet.


Version 3.0.1
-------------

* :issue:`86`: Fix installation issue with setuptools 3.6.

* :issue:`85`: Remove debug output from the wrapper for ``NSApplicationMain``.

* :issue:`82`: NSArray.__iter__ was accedently removed in PyObjC 3.0

* PyObjCTools.Debugging didn't work properly on recent OSX versions (at least OSX 10.9)
  because ``/usr/bin/atos`` no longer worked.

Version 3.0
-----------

* :issue:`50`: Accessing Objective-C methods on "magic cookie" variables,
  like ``LaunchServices.kLSSharedFileListItemLast`` would crash the interpreter.

  This affected code like::

      from LaunchServices import kLSSharedFileListItemLast

      kLSSharedFileListItemLast == kLSSharedFileListItemLast
      dir(kLSSharedFileListItemLast)
      kLSSharedFileListItemLast.compare_

* Added a decorator "python_method" than can be used to decorate methods that should
  not be registered with the Objective-C runtime and should not be converted to a
  Objective-C selector.

  Usage::

      class MyClass (NSObject):

          @python_method
	  @classmethod
	  def fromkeys(self, keys):
	      pass

  This makes it easier to add a more "pythonic" API to Objective-C subclasses without
  being hindered by PyObjC's conventions for naming methods.

* :issue:`64`: Fix metadata for ``Quartz.CGEventKeyboardSetUnicodeString``
  and ``Quartz.CGEventKeyboardGetUnicodeString``.

* :issue:`77`: Passing a bound selector as a block argument failed when the block
  was actually called because the trampoline that calls back to Python accidentally
  ignored the bound ``self`` argument.

* :issue:`76`: It is now possible to pass ``None`` to a method expecting a block
  argument, as with normal object arguments the Objective-C method receives
  a ``nil`` value.

* Python integer values with values between 2 ** 63 and 2**64 are now proxied
  as plain NSNumber objects, not as using PyObjC specific subclass of NSNumber,
  to avoid a problem with writing them to binary plist files.

  This is a workaround and will likely be changed in some future version.

* ``inspect.signature`` works for all functions and methods implemented in C,
  when using Python 3.4 or later.

* The module ``PyObjCTools.NibClassBuilder`` is not longer available. It only worked
  with ancient versions of Interface Builder (pre-Xcode)

* The wrapper type for opaque pointers didn't have a "__module__" attribute,
  which breaks code that (correctly) assumes that all types have such an attribute.

* Archiving now supports nested definitions and method references, simular
  to the support of those added to pickle protocol 4 in Python 3.4.

  Encoding nested classes requires support for the ``__qualname__`` attribute,
  and hence requires Python 3.3. Decoding should work with earlier python
  versions as well.

* Add ``objc.autorelease_pool``, a context manager for managing an
  autorelease pool. Usage::

       with objc.autorelease_pool():
          pass


  This is equivalent to::

       _pool = NSAutoreleasePool.alloc().init()
       try:
           pass

       finally:
           del _pool

* Added ``objc.registerABCForClass`` to make it possible to register
  a class with a number of ABC classes when the class becomes available.

* ``NSDecimalNumber`` can now be instantatiated as a normal Python object::

     value = NSDecimalNumber(4)

* ``NSData`` and ``NSMutableData`` can now be instantiated as a normal
  Python object::

      value = NSData(someBytes)

   or::

      value = NSData()

* ``NSDecimal`` now coerces the other value to ``NSDecimal`` in coercions.
  Because of you can now order instances of ``NSDecimal`` and ``int``.

* ``PyObjCTools.KeyValueCoding.ArrayOperators`` and
  ``PyObjCTools.KeyValueCoding.arrayOperators`` were accidentally public
  names in previous releases, and are now removed. Use the array operators
  in the KVC protocol instead.

* Restructured the "convenience" method code. This shouldn't have user
  visible effects, but makes the code easier to maintain.

* ``objc.addConvienceForSelector`` no longer exists, it isn't possible
  to provide this functionality with the current implementation of the
  bridge.

* The build of pyobjc-core can now be configured by editing setup.cfg (or
  providing arguments to the build_ext command), instead of editing the
  setup.py file.

  Currently the following options are available for the build_ext command:

  * ``--use-system-libffi``: When this option is used the build will use
    /usr/lib/libffi.dylib instead of the embedded copy of libffi. The latter
    is the default is and is better tested.

  * ``--deployment-target=VAL``: The value of ``MACOSX_DEPLOYMENT_TARGET`` to use,
    defaults to the deployment target used for building Python itself

  * ``--sdk-root=VAL``: Path to the SDK root used to build PyObjC, or "python" to
    use the default SDK selected by distutils. The default is to use the
    most recent SDK available.

* The lazy importer has smarter calculation of the ``__all__`` attribute,
  which should speed up 'from Cocoa import \*'.

* BUGFIX: using a method definition with only ``*args`` and ``**kwds`` used
  to crash the interpreter, the now once again raise a TypeError exception.

* The metadata for pyobjc-framework-Accounts was incomplete, fixed that.

* :func:`objc.callbackFor` now also adds a *__metadata__* method to decorated
  functions. This is primarily to make it easier to test the metadata values.

* The *__typestr__* attribute of opaque pointer types is now a byte string,
  in previous versions this was an instance of :class:`str` (this only affects
  Python 3 support)

* The JavaScriptCore bindings (in pyobjc-framework-WebKit) are now more usable
  because types like "JSValueRef" are now exposed to Python (they were missing
  due to incomplete metadata).

* Exclude a number of keys from the metadata dictionary when they have the
  default value (in the result from the *__metadata__()* method on methods
  and functions)

* The "lazy" modules used by framework wrappers now always have a ``__loader__``
  attribute (as required by PEP 302). The value can be :data:`None` when there
  is no explicit loader (such as when importing from the filesystem in Python 3.2
  or earlier).

* Method (and function) metadata is stored in a more compact manner, reducing the
  memory use of PyObjC applications.

* Removed support for hiding "protected" methods, :func:`objc.setHideProtected` is gone,
  it complicated the code without real advantages.

  Reasons for this:

  * There were some conflicts because a class implemented two selectors that caused
    the same python method to be added to the class *__dict__*. Which one was added
    was basically random.

  * The functionality required PyObjC to maintain a full *__dict__* for classes, even
    when most Cocoa methods were never called. Ensuring that the contents of *__dict__*
    is correct in the face of Objective-C categories and class patches required some
    *very* expensive code.

  As a side effect of this some classes may no longer have the convenience methods they
  had in earlier releases (in particular classes that are not mentioned in Apple's
  documentation).

* :issue:`3`: The bridge now lazily looks for Objective-C methods as they are used from Python, instead
  of trying to maintain a class *__dict__* that mirrors the method list of the Objective-C
  class.

  Maintaining the *__dict__* was *very* expensive, on every method call the bridge would
  check if the method list had changed and there is no cheap way to perform that check.

  .. note::
     I haven't done performance tests at this time, it is not yet clear if this work will
     make the bridge more efficient or that there are other more important bottlenecks.

* The default translation from a python name to a selector was slightly changed:

  * double underscores inside the name are no translated to colons, that is 'foo__bar_' is translated to 'foo__bar:', not 'foo::bar:'

  * if the Python name start with two uppercase letters and an underscore, that first underscore is not translated into
    an colon. Two leading capitals are often used as a way to add some kind of namespacing
    to selector names (and avoid conflicts when a method with the same name is added later by the library provider)

* Added *__new__* method to NSString, it is now possible to explicitly convert a python string to a Cocoa
  string with ``NSString(someString)``

* Added *__eq__* and *__ne__* methods to native selector objects, which mean you can now
  check if two method objects are the same using 'sel1 == sel2'. This works both for bound
  and unbound selectors.

* NSData.bytes() could raise an exception on some version of Python 3 when the data object is empty.
  The function now returns an empty bytes object instead.

* NSMutableData.mutableBytes() raises an exception when the data object has a 0-sized buffer.
  (see also the previous bullet)

* Add attribute *__objclass__* to :class:`objc.selector` instances as an alias for *definingClass*. The name
  *__objclass__* is used by builtin method objects for the same purpose as *definingClass*.

  The new attribute is needed to ensure that ``help(NSObject)`` works (although all methods are shown as
  data descriptors, not methods)

* :class`objc.selector` no longer implements *__set__*, which means it is now classified as a method
  descriptor by the :mod:`inspec` module, which gives nicer output in :mod:`pydoc`.

  This doesn't change any functionality beyond that, it is still possible to overwrite methods and not
  possible to delete them.

* :class:`objc.native_selector` and :class:`objc.function` now have a (minimal) docstring with information
  object.  This makes :func:`help <pydoc.help>` for Cocoa classes and functions more useful.

  As a side-effect of this the docstring is no longer writeable.

  .. note::

     The docstring show the interface of a block with a function prototype instead of the proper
     C declaration, that makes the implementation slightly easier and the function prototype syntax
     is slightly easier to read for users that aren't C experts.

* :class:`objc.selector`, :class:`objc.function` and :class:`objc.IMP` now have an implementation for
  the "__signature__" property when using Python 3.3 or later. This makes it possible to use
  :func:`inspect.signature` with these objects.

* It should now be possible to write tuples with more than INT_MAX elements to an NSArchive. Those archives
  cannot be read back by older versions of PyObjC (or python running in 32-bit mode), but archives that
  contain only smaller tuples can be read back by earlier versions.

* :issue:`38`: Struct wrappers and opaque pointer types now implement support for :func:`sys.getsizeof`,
  as do :class:`objc.FSRef`, :class:`objc.FSSpec`, and Objective-C classes.

  The size of Objective-C instances is not entirely correct, and cannot be. The :func:`sizeof <sys.sizeof>` function
  only reports the size of the proxy object and the basic size of the Objective-C object. It does not
  report additional buffers used by the object, which for example means that a too low size is reported
  for Cocoa containers like NSArray.

* Opaque pointer objects now have a method "__c_void_p__" that returns a :class:`ctypes.void_p` for
  the same pointer.

* Added an API to "pyobjc-api.h" that makes it easier to explicitly load function references in
  manual function wrappers. This replaces the compiler support for weak linking, which was needed
  because weak linking did not work properly with clang (Xcode 4.5.1). This also makes it possible
  to compile in support for functions that aren't available on the build platform (in particular, when
  building on 10.8 the Quartz bindings now contain support for some functions that were dropped in 10.8
  and which will be available through pyobjc when deploying to 10.7)

* The framework wrappers no longer export a "protocols" submodule. Those submodules were deprecated in
  2.4 and did not contain information that is useful for users of PyObjC.

* Dropped the "objc.runtime" attribute (which was deprecated in PyObjC 2.0)

* Dropped depcreated APIs *objc.pluginBundle*, *objc.registerPlugin*. Py2app has used a
  different mechanism for years now.

* Dropped deprecatd APIs: *objc.splitStruct*,  *objc._loadFunctionList*. Both have
  been replaced by newer APIs in PyObjC 2.4.

* Foundation's *NSDecimal* type is exposed in the objc module as well.

  This was done to remove a dependency from the pyobjc-core package to pyobjc-framework-Cocoa.

* The type :class:`objc.NSDecimal` is now an immutable type, just like
  :class:`decimal.Decimal` and other Python value types.

  Because of this the interface of ``Foundation.NSScanner.scanDecimal_`` has changed, in
  previous versions it is used as::

      dec = Foundation.NSDecimal()
      ok = scanner.scanDecimal_(dec)

  In the current version it is called just like any other method with an output argument::

      ok, dec = scanner.scanDecimal_(None)

* The C code is more careful about updating Python reference counts, in earlier versions
  it was possible to trigger access to a field in a datastructure that was being deallocated
  because the calls to :c:macro:`Py_DECREF` for the field happened before setting the
  field to :c:data:`NULL` or a new value.  This could then result in a hard crash due to
  accessing freed memory.

* Bugfix: objc.NSDecimal(2.5) works with python 3 (caused a confusing
  exception due to buggy code before).

* Bugfix: the support for :func:`round <__builtin__.round>` for :class:`objc.NSDecimal`
  always rounded down, instead of using the normal rounding rules used by other
  methods.

* PybjC no longer supports the CoreFoundation bindings in the "Carbon.CF" module
  in the standard library for Python 2.  The "Carbon.CF" module is not present
  in Python 3, and is unmaintained in Python 2.

* The 'struct sockaddr' conversion code now understands the AF_UNIX address family.

* The function "objc.setSignatureForSelector" has been removed (and was deprecated
  in 2.3), use the metadata system instead."

* The 'returnTypes' and 'argumentTypes' parameters for 'objc.selector' have
  been removed (they were deprecated in version 2.5). These were an attempt
  to use type encodings as used in :c:func:`Py_BuildValue` and AFAIK were never
  used in real code.

* The header "pyobjc-api.h" has been cleaned up:

  .. note::

     "pyobjc-api.h" is used by extension modules in the PyObjC framework wrappers
     but is not intended to be a public API. Please let me (Ronald) know if you
     use this API, I'm trying to get the API as small as possible and that might
     lead to its complete removal in a future version of PyObjC.

  - Py_ARG_SIZE_T is no longer defined by pyobjc-api.h (use "n" instead)

  - Removed the following functions from the API (PYOBJC_API_VERSION is now 20)
    because they aren't used by PyObjC:

    - PyObjC_PerformWeaklinking (and struct PyObjC_WeakLink)

    - PyObjCRT_RemoveFieldNames

    - PyObjC_is_ascii_string

    - PyObjC_is_ascii_prefix

    - PyObjCObject_Check

    - PyObjCClass_Check

    - PyObjCSelector_Check

    - PyObjCObject_ClearObject

    - PyObjCClass_New

    - PyObjCErr_ToObjC

    - PyObjC_RegisterSignatureMapping

    - PyObjCRT_AlignOfType

    - PyObjCRT_SELName

    - PyObjCRT_SimplifySignature

    - PyObjC_RegisterStructType

    - PyObjCObject_IsUninitialized

    - PyObjCObject_New

    - PyObjCCreateOpaquePointerType

    .. note::

       There will be further cleanup of this API before the 3.0 release.

    Added a *name* argument to PyObjCPointerWrapper_Register.

* The KVO implementation for Cocoa subclasses used to ignore exceptions
  in the implementation of ``[obj willChangeValueForKey:]`` and
  ``[obj didChangeValueForKey:]`` and no longer does so.

  One side effect of this is that ``willChangeForForKey_`` and
  ``didChangeValueForKey_`` can now cause user visible exceptions
  when "__useKVO__" is true (the default) and these methods are implemented
  in Python.

* PyObjC 3 requires a compiler that supports Objective-C with C99 as the base
  language.

* PyObjC raises an exception instead of creating instances of
  :class:`objc.PyObjCPointer` when you set :data:`objc.options.unknown_pointer_raises`
  to :data:`True`.

  The default is currently :data:`False`, that will be changed in a future version
  and the entire `objc.ObjCPointer` class will likely be removed some releases
  after that.

* Configuration options are now attributes of special object :data:`objc.options`.

  The following functions are therefore now deprecated and will be removed
  in PyObjC 3.1:

  * :func:`objc.getVerbose`

  * :func:`objc.setVerbose`

  * :func:`objc.setUseKVOForSetAttr`

  * :func:`objc.setStrBridgeEnabled`

  * :func:`objc.getStrBridgeEnabled`

* Removed objc._setClassSetUpHook, an internal method that is not used
  anymore.

* Removed +[OC_PythonObject setVersion:encoder:decoder:],
  +[OC_PythonObject pythonifyStructTable], +[OC_PythonObject depythonifyTable].

 All were private methods used by the core bridge and are no longer necessary.

* Added :func:`objc.registerSetType` and :func:`objc.registerDateType`, with
  simular semantics as the already existing functions :func:`objc.registerMappingType`
  and :func:`objc.registerListType`.

* Moved the logic for creating Objective-C proxies for Python objects from
  class methods on OC_PythonObject, OC_PythonArray, OC_PythonDictionary,
  OC_PythonSet and OC_PythonDate to a C function to simplify this logic and
  make it easier to further optimize.

  Because of this a number of (private) class methods are no longer
  available. This shouldn't affect normal code because these methods aren't
  part of the public API for PyObjC.

* Added bindings to the CoreWLAN framework (macOS 10.6 or later) in
  package "pyobjc-framework-CoreWLAN"

* Added bindings to the AVFoundation framework (macOS 10.7 or later) in
  package "pyobjc-framework-AVFoundation"

* The *__dict__* for ``anObject.pyobjc_instanceMethods`` and
  ``AClass.pyobjc_classMethods`` is now read-only instead of read-write.

  Updates of *__dict__* already did not affect anything (the value is
  calculated on access).

* Removed workarounds for KVO bugs in macOS 10.3.9, which means KVO
  will likely not work properly anymore on that release of OS X.

* Earlier versions of PyObjC accidentally exposed ``-[NSObject respondsToSelector:]``
  as ``NSObject.respondsToSelector()`` as well as the expected
  ``NSObject.respondsToSelector_()``. The first incorrect binding no
  longer works.

* Python 3 only: NSKeyedArchives with a bytes object can now be read
  back by a pure Objective-C program (that program will decode it
  as an NSData object).

  Because of this the encoding for method for OC_PythonData was changed,
  archives created by PyObjC 3.0 can therefore not be read back
  by earlier PyObjC versions (but PyObjC 3.0 can read archives created
  by those older versions)

* NSKeyedArchives with a python list or tuple (but not subclasses) can
  now be read back as NSArrays in Objective-C programs.

* NSKeyedArchives with a python set or frozenset (but not subclasses)
  can now be read back as NSSets in Objective-C programs.

  This required a change in the format used to create the archive,
  which means that archives with a set or frozenset (but not subclasses)
  cannot be read back by earlier versions of PyObjC.

* When writing instances of list, tuple, dict, set and frozenset to
  an NSArchive, but not an NSKeyedArchiver, the objects are stored
  with the same encoding as the corresponding Cocoa class.

  This has two side effects: the archive can be read back by pure
  Objective-C code and when you read back the archive using PyObjC you'll
  get instances of Cocoa classes instead of the native python classes.

* ``-[OC_PythonEnumerator nextObject]`` now returns ``[NSNull null]`` instead
  of ``nil``, to be compatible with the behavior of item getters/setters
  and to avoid ending iteration premature when a Python sequence contains
  :data:`None`.

* Fixed a number of issues with :data:`None` as a member of a set-like
  object proxied by ``OC_PythonSet``. The easiest way to trigger the
  issue in earlier versions::

     assert {None} == NSSet.setWithArray([None])

  These expose sets with the same members to ObjC code, but those objects
  didn't compare equal.

* Python 2 only: NSDictionary instances now have the same internal
  other as dict instances with the same value, that is
  ``cmp(anNSDict1, anNSDict2) == ``cmp(dict(anNSDict1), dict(anNSDict2))``.

* In previous versions of PyObjC instances of ``Foundation.NSDecimal`` behaved
  as if they had the same methods as ``Foundation.NSDecimalNumber``. In 3.0
  PyObjC no longer exposes these methods.

* Python blocks (that is, Python callables passed to a method/function that
  expects an Objective-C block argument) now include an Objective-C
  signature string (introduced in "ABI.2010.3.16").

* PyObjC now supports blocks that have a large struct as the return value
  (for example a block that returns an NSRect structure).

* Reduced the number of unnecessary methods implemented by the various
  OC_Python* classes, this might affect some Objective-C code that directly
  uses these classes instead of just using the interface of their
  superclasses.

* ``del NSObject.__version__`` crashed the interpreter because the setter
  didn't guard against deletion attempts.

* ``del aSelector.isHidden`` crashed the interpreter (see above)

* Class :class:`objc.ObjCPointer` was not exposed in the :mod:`objc` module.

* The implementation of :class:`objc.ObjCPointer` didn't have a proper
  implementation of *__getattribute__* and that made objects of this
  class even more useless than they should have been.

* Values of :class:`objc.ObjCPointer` no longer have an unpack method
  (the method has been inaccisible for several releases and its implementation
  as unsafe)

* The *type* attribute of :class:`objc.ObjCPointer` now starts with
  :data:`objc._C_PTR` (that is, the *type* attribute is the encoded type
  of the pointer, instead of the encoded type of the pointed-to value).

* Framework wrappers no longer have a 'protocols' submodule, use
  :func:`objc.protocolNamed` to access a protocol.

* ``-[OC_PythonObject valueForKeyPath:]`` and ``-[OC_PythonObject setValue:forKeyPath:]``
  now call helper functions in :mod:`PyObjCTools.KeyValueCoding`, just
  like ``-[OC_PythonObject valueForKey:]`` and ``-[OC_PythonObject setValue:forKey:]``.

  This should give better results in some edge cases when dealing with
  complicated keypaths.


Version 2.5.2
-------------

- "easy_install pyobjc" always tried to install the FSEvents binding,
  even when running on OSX 10.4 (where that API is not available).

- ``objc.ObjCPointer`` didn't implement *__getattribute__*.

  (reported by private mail)

- Implementing a python method that has a block as one of its arguments
  didn't work. It now works when there is metadata that describes the
  method signature.

  (reported by private mail)

- BUGFIX: a method definition like this now once again raises TypeError
  instead of crashing the interpreter::

      def myMethod(*args):
         pass

  (reported by private mail)

Version 2.5.1
-------------

- PyObjC could crash when calling a method that is dynamically generated
  (that is, the selector is not present in the class according to the
  Objective-C runtime but the instance responds to it anyway).

  The cases that used to crash now raise :exc:`objc.error` instead.

  .. note::

     It is highly unlikely that real code would run into this, found
     while working on PyObjC 3.x.

- When writing a python unicode object to an NSArchiver or NSKeyedArchiver
  the object is now stored exactly the same as a normal NSString, and will
  be read back as such.

  This increases interoperability with code that expects to read back a
  non-keyed archive in a different process. An example of this is the use
  of Growl (see issue :issue:`31`)

  Instances of subclasses of unicode are not affected by this change, and
  can only be read back by other PyObjC programs.

- :issue:`43`: It was no longer possible to create instances of
  LaunchServices.LSLaunchURLSpec due to incomplete metadata.

- :issue:`41`: the 'install.py' script in the root of pyobjc repository
  failed to perform an install when running in a clean checkout of the tree.

- :issue:`44`: the various Cocoa frameworks only export @protocol definitions when
  they happen to be used by code in the framework. Added extensions to the
  various framework wrappers to ensure that all protocols are available to
  python code.

- Opaque pointer types now can be constructed with a "c_void_p" keyword
  argument that contains a :class:`ctypes.c_void_p` value for the pointer.

  This is the reverse of the *__c_void_p__()* method that was added
  earlier.

- :issue:`46`: It was not possible to use the Quartz.CoreGraphics module
  on OSX 10.5 when the binary was build on 10.8 (and using a 10.5 deployment
  target).

  Simular issues may be present in some of the other framework wrappers,
  there will be a more generic fix for this issue in a future release.

Version 2.5
-----------

- Add conversion to/from ctypes.c_void_p to proxies for Cocoa objects.

  To use::

     anObject = NSArray.array()
     void_p = anObject.__c_void_p__()
     # use void_p with ctypes

     otherObject = NSObject(c_void_p=voip_p)
     assert anObject is otherObject

  Note that it is save to construct the python proxy from NSObject,
  the class will return an instance of the correct proxy type (in this
  example an instance of NSArray)

- Fixed problem where the result of ``anObject.__cobject__()`` could not be converted
  back to a PyObjC object again.

- A number of framework wrappers have a "protocols" submodule containing
  protocol objects (for example the module 'Foundation.protocol'). Use
  of these modules is deprecated, they will be removed in PyObjC 3.0.

  Use :func:`objc.protocolNamed` to access protocols instead.

- Instances of :class:`objc.ivar` now have slots for introspection:

  - *__typestr__*: The type encoding

  - *__name__*: The Objective-C name

  - *__isOutlet__*: :data:`True` if the instance variable is an IBOutlet

  - *__isSlot__*: :data:`True` if the instance variable is a Python slot

- Added implementation of '==' and '!=' for selectors defined in Python
  that is slightly smarter than the default (identity based) implementation
  in Python.

  This is mostly done for the PyObjC unittests and shouldn't affect user
  code.

- :issue:`30`: Explicitly check if the compiler works, and try to
  fall back to clang if it doesn't. This uses a simular algorithm as
  the fix for <https://bugs.python.org/issue13590> in Python's tracker.

- :issue:`22`: Reimplement support for bridgesupport files

  This reintroduces ``objc.parseBridgeSupport`` and
  ``objc.initFrameworkWrapper``, both are reimplemented in Python
  (previous version used C code)

  .. note::

     The implementation is currently barely tested and therefore likely
     contains bugs.

- Struct types created by the framework wrappers once again create class
  methods on :class:`objc.ivar` to generate instance variables of that type::

     myLocation = objc.ivar.NSPoint()

  This has the same result as::

    myLocation = objc.ivar(typer=NSPoint.__typestr__)

- :func:`objc.IBAction` now raises TypeError when the argument is :data:`None`.

- :func:`objc.instancemethod` is now actually exported by the :mod:`objc` package.

- :func:`objc.accessor` and :func:`objc.typedAccessor` were not 64-bit safe.

- :func:`objc.accessor` and :func:`objc.typedAccessor` didn't support the entire
  set of KVC accessors.

- Add methods "_asdict" and "_replace" and field "_fields" to the struct wrapper
  types. These new attributes mirror the :class:`collections.namedtuple` interface.

  .. note::

     In the long run I'd like to make struct wrappers immutable to allow using
     them as dictionary keys. This is a first step in that direction and makes
     it possible to verify that immutable struct wrappers are usable.

- Added :func:`objc.createStructAlias`, and deprecated
  :func:`objc.registerStructAlias`. The new function has a "name" argument
  and can register types with the :class:`objc.ivar` type (see previous item)

- Add explicit deprecation warnings to ``objc.CFToObject`` and
  ``objc.ObjectToCF``. Both functions barely function at all and will
  be removed with PyObjC 3.0.

- ``objc.CFToObject`` and ``objc.ObjectToCF`` are no longer available
  when using Python 3.x, the APIs are used for MacPython support and
  that part of the standard library is not available with Python 3.x.

- ``objc.splitStruct`` is renamed to ``objc.splitStructSignature``
  and now actually works. The old name is temporarily available as
  an alias.

- Fix refcounting leak in ``objc.splitSignature``.

- ``objc._loadFunctionList`` is renamed to ``objc.loadFunctionList``
  and is fully documented. The old name is temporarily available as
  an alias.

- Move (deprecated) decorator "signature" from objc._functions to objc._descriptors,
  and remove the former module.

  .. note::
     The names op submodules of objc are implementation details, don't import
     them directly.

- The optional argument for the decorator :func:`objc.selectorFor` was broken

- The :class:`PyObjCTools.KeyValueCoding.kvc` wrapper `__setattr__` wrapper
  incorrectly set attributes on itself as well as on the wrapped object (the latter
  using Key-Value Coding)

- Renamed (private) function injectSuffixes to inject_suffixes to match the
  other code in objc._dyld.

- Slight restructuring of objc._pythonify to reduce code duplication between the
  python 2.x and python 3.x cases.

- Removed deprecated methods from PyObjCTools.TestSupport

- :class:`collections.Sequence` objects are now automatically proxied as NSArray
  instances

- :class:`collections.Mapping` objects are now automatically proxies as NSDictionary
  instances

- Removed some objects and functions from objc._bridges that weren't public
  and weren't used by PyObjC itself:

  - *BRIDGED_STRUCTURES*: mapping of python type to proxy class
  - *BRIDGED_STRUCTURES2*: mapping of python type to proxy class (not used at all)
  - *BRIDGED_TYPES*: mapping of python type to proxy class
  - *_bridgePythonTypes*: uses BRIDGED_STRUCTURES and BRIDGED_TYPES to update bridge data

  *_bridgePythonTypes* was called unconditionally, but never did anything because
  the data structures were empty and no code adds anything to them.

- Improved documentation

- For Objective-C blocks: try to extract the block signature from the (Objective-)C runtime
  when there is no metadata for the block. The block signature is available only when the
  code that creates the block is compiled using a recent enough compiler (although "recent
  enough" is fairly old by now)

- Fixes some issues with :class:`objc.object_property` which were found by
  improved unittests. In particular:

  - The selector names for boolean properties were wrong

  - Properties with a "depends_on" list didn't inherit properly

  - Properties that were used in subclasses didn't generate the correct KVO
    events when they were observed.

  - KVO issues with computed (read-only) properties

- Fixed some issues with :class:`objc.array_property` and :class:`objc.set_property`
  that were found by much improved unittests.

- Fixed issues with :mod:`PyObjCTools.KeyValueCoding` that were found by improved
  unittests:

  - ``getKey`` didn't work properly on dictionaries (dictionaries were treated as sequences)

  - ``getKeyPath(list, "@avg.field")`` didn't work when field wasn't a valid key for all
     items in the list, and likewise for the '@sum', '@min', '@max' special keys.

  - ``getKeyPath`` didn't raise the correct exception for empty key paths

  - ``@unionOfObjects`` and ``@distinctUnionOfObjects`` operators for Python sequences
    didn't raise an exception when the selected keypath didn't exist on an item of the sequence.

  - ``@unionOfArrays`` and ``@distinctUnionOfArrays`` operators for Python sequences
    didn't raise an exception when the selected keypath didn't exist on an item of the sequence.

  - ``@distinctUnionOfArrays`` and ``@distinctUnionOfObjects`` didn't work properly when
     the keypath pointed to objects that weren't hashable.

  - ``@distinctUnionOfSets`` operator was not present at all.

- 'PyObjCTools.KeyValueCoding.setKey' now sets keys in dictionaries, that is::

     >>> a = {}
     >>> setKey(a, 'foo', 42)
     >>> a
     {'foo': 42 }

- 'PyObjCTools.KeyValueCoding.setKey(object, 'key', value)' now sets attribute 'key' when
  the object already has that attribute, before looking at '_key'. This avoids that ``setKey``
  changes the underlying storage for a common Python property pattern::

      class Record (object):
         @property
	 def prop(self):
	     return self._prop

	 @prop.setter
	 def prop(self, value):
	     self._prop = calculate_using(value)

  Until PyObjC 2.5 the property setter for 'prop' would not be called when using KeyValueCoding.

- Removed macOS 10.2 (!) compatibility from :mod:`PyObjCTools.KeyValueCoding`.

- PyObjCTools.KeyValueCoding has undocumented attributes 'ArrayOperators' and 'arrayOperators',
  both will be removed in a future release.

- Using NSArchiver or NSKeyedArchiver to encode and then decode a python list or tuple could
  result in an unexpected value. In particular, if any element of the sequence was :data:`None`
  before archiving it would by ``NSNull.null()`` when read back.

- Using NSArchiver or NSKeyedArchiver to encode and decode (pure) python objects didn't always
  work correctly. Found by improved unittests.

- Using NSArchiver or NSKeyedArchiver to encode and decode bytes objects in Python 3 would
  result in an instance of NSData instead of bytes.

- The implementation of cmp() for NSSet instances now matches the behavior of regular python
  sets, that is calling ``cmp(anNSSet, aValue)`` will raise a TypeError exception unless
  both arguments are the same object (``anNSSet is aValue``).

- :issue:`36`: explicitly document that PyObjC does not support the Objective-C Garbage Collection
  system (introduced in OSX 10.5, deprecated in OSX 10.8), and also mention this in the
  documentation for the screen saver framework because the screen saver engine uses GC on
  OSX 10.6 and 10.7.

- :issue:`37`: Fix runtime link error with EPD (Enthought Python Distribution),
  which doesn't include the pymactoolbox functionality.

- Various improvements to the documentation

Version 2.4.1
-------------

.. note:: 2.41 was never released, all bugfixes are in the 2.4 branch as well as the 2.5 release.

- Cocoa wrappers: fix metadata for ``copy``, ``mutableCopy``,
  ``copyWithZone:`` and ``mutableCopyWithZone:``

- Fix for issue 3585235 on SourceForge: the threading helper category on
  NSObject didn't work due to a typo (defined in the Cocoa bindings)

  Fix is based on a patch by "Kentzo" with further updates and tests by
  Ronald.

- Rename ReadMe.txt to README.txt to work around misfeature in the
  sdist command in distutils.

- :issue:`28`: Avoid crash when using CGEventTabProxy values.

- :issue:`33`: "easy_install pyobjc" no longer tries to install the
  InterfaceBuilderKit bindings on OSX 10.7 or later.

Version 2.4
-----------

.. note::

   Sadly enough this changelog is incomplete.

- Fix crash when unarchiving a Python object.

- Add missing calls to ``[super init]`` in the implementation of
  OC_PythonUnicode and OC_PythonString (the ObjC proxies for python's
  unicode and str types)

- ``objc.addConvenienceForSelector`` is deprecated, primarily to make
  it possible to restructure the pyobjc internals.

- Workaround for bug in pip that resulted in pyobjc-core not being pip
  installable.  Patch by Marc Abramowitz.

- Creating new formal protocols now uses the new runtime API that was
  introduced in OSX 10.7. Because of this it is now possible to create
  new formal protocols in 64-bit code (when running on OSX 10.7 or later)

- Codebase should work again when Python using ``--enable-unicode=ucs4``.

- BUG: Avoid crashes in calculating with NSDecimal values in Python 3

- Implement '//' operator for NSDecimal and NSDecimalNumber.

- Implement support for the ``round`` builtin in NSDecimal and
  NSDecimalNumber

- There is now limited support for packed struct definitions. This
  requires that the struct is wrapped using ``objc.createStructType``.

  Struct packing is not described in the encoding string for a
  structure, which is why special support is needed.

- objc.registerStructAlias now returns the alias type instead of ``None``

- In Python 3.x there is a new way to explicitly specify which (informal)
  protocols a class conforms to::

     class MyClass (NSObject, protocols=[Protocol1, Protocol2]):
        pass

  Python 2.x does not support this syntax, you can still use the
  following code there::

     class MyClass (NSObject, Protocol1, Protocol2):
        pass

  Note: The Python 2.x style works up to Python 3.2. In Python 3.3 and later
  the Python 2.x style declaration no longer works due to changes in the
  language.

- It is also possible to specify the protocols that a class conforms to using
  a "__pyobjc_protocols__" attribute in the class body.  This has the same
  interface as the "protocols" keyword argument in Python 3.x.

  This is primarily meant to be used by code that needs to work in Python 2
  as well as Python 3.

- Updated Python support. With this release PyObjC supports Python 2.6 and later,
  including Python 3.3 (which has a completely new representation for unicode strings)

  NOTE: Support for 3.3 is very much work in progress right now, there have
  been changes for the new unicode representation, but more changes are required.

  Known issues:

  * metadata conflict error when explicitly implementing a prototype

  * one test failure w.r.t. unichar argument arrays

  Furthermore there are two refcounting test failures in both 3.2 and 3.3


- Add ``objc.setObjCPointerIsError`` and ``objc.getObjCPointerIsError``.

  By default PyObjC will create a ``PyObjCPointer`` object when it tries
  to convert a pointer it doesn't know about to Python. These values are
  fairly useless and obvious an indication that an API is wrapped improperly.

  With ``objc.setObjCPointerIsError(True)`` you can tell the bridge to
  raise an exception instead of creating these values.

- -[OC_PythonNumber compare:] calls super when the other value is
  an NSNumber and the Python value can be represented using a basic C
  type.

  This could slightly affect the results of comparing Python and
  Cocoa numbers, and avoids unbounded recursion when comparing
  Python numbers with NSDecimalNumbers on OSX 10.7 or later.

- Add implementations for methods from the NSComparisonMethods
  informal protocol to OC_PythonNumber

- Add '__cmp__' method when the Objective-C class implements the
  'compare:' selector.

- Introduced a way to compile bridgesupport data and lazily load wrappers.

  Avoid using "from Cocoa import \*" to get the most benefits from this,
  use either "import Cocoa" or "from Cocoa import NSObject".

- ``objc.initFrameworkWrapper`` is now deprecated, switch to the new
  compiled metadata code instead.

- ``objc.allocateBuffer`` now returns a bytearray on python >= 2.6,
  it used to return a buffer object in Python 2.

- ``objc.FSRef.from_pathname`` actually works instead of always raising
   a TypeError.

- ``objc.getAssociatedObject``, ``objc.setAssociatedObject`` and
  ``objc.removeAssociatedObjects`` are wrappers for the corresponding
  functions in the Objective-C runtime API.  These functions are only
  available when PyObjC was build on a system running OSX 10.6 or later,
  and the script is also running on such as system.

  The ``policy`` argument for ``objc.setAssociatedObject`` is optional and
  defaults to ``objc.OBJC_ASSOCIATION_RETAIN``.

Version 2.3
-----------

- Add some experimental code that slightly reduces the amount of
  memory used when loading bridgesupport files.

  Further work is needed to investigate what causes the memory
  usage to increase as much as it does, sadly enough Instruments
  doesn't play nice with ``--with-pymalloc`` and for some reason
  'import Foundation' crashes with ``--without-pymalloc``.

- "<struct>" definitions in the bridgesupport files can now have
  an alias attribute containing the name of Python type that should
  be used to proxy values of this type.

  This is used in the Quartz bindings to ensure that ``CGRect``
  and ``NSRect`` (from the Foundation framework) map onto the
  same Python type.

- Added ``objc.registerStructAlias``, a helper function to add
  a type encoding that should map on an already existing struct
  type.

- Use this to ensure that ``NSRect`` and ``CGRect`` are the same
  (in the Foundation and Quartz bindings).

- This version requires Python 2.6 or later, and also supports
  Python 3.1 or later.

- BUGFIX: The generic proxy for Python objects now implements
  ``-(CFTypeID)_cfTypeID``, which should result in less hard to
  understand Objective-C exceptions.

- BUGFIX: The metadata file support now checks if the metadata is
  compatible with information gathered from the Objective-C runtime.

  This ensures that when a native method signature is incompatible
  with the signature in a metadata file the bridge won't garble the
  correct information (and that in turn avoids hard crashes).

- PyObjC's support for ``NSCoding`` now also works with plain ``NSArchiver``
  instances, not just with ``NSKeyedArchiver``.

- (This item is currently only true for python3, need tests for python 2.x)

  NSDictionary now fully implements the dict API, except for the differences
  not below:

  * ``NSDictionary`` doesn't have the ``__missing__`` hook.

  * ``NSDictionary`` always copies keys, which gives slightly different
     semantics from Python.

  * ``NSDictionary.copy`` always returns an immutable dictionary, use
    ``NSDictionary.mutableCopy`` to get a mutable dictionary.

  * Instances of ``NSDictionary`` cannot be pickled

  ``NSDictionary`` implements one important feature that native Python
  dictionaries don't: full support for Key-Value Observations. Sadly enough
  it is not possible to support Key-Value Observation of native Python
  dictionaries without patching the interpreter.

- NSSet and NSMutableSet implement the same interface as ``frozenset`` and
  ``set``, except for the differences listed below:

  * ``NSSet.copy`` and ``NSMutableSet.copy`` always return an immutable
     object,  use the ``mutableCopy`` method to create a mutable copy.

  * Instances of ``NSSet`` cannot be pickled

  * In-place operators are not implemented, which means that ``aSet |= value``
    will assign a new object to ``aSet`` (as if you wrote ``aSet = aSet | value``.

    This is needed because the bridge cannot know if if ``aSet`` is mutable,
    let alone if ``aSet`` is a value that you are allowed to mutate by API
    contracts.

  * It is not possible to subclass ``NSSet`` and ``NSMutableSet`` in the same
    way as Python's ``set`` and ``frozenset`` classes because the Cocoa
    classes are class clusters (which means that all instances of ``NSSet``
    are actually instances of, non-necessarily public, subclasses.

  * Sadly enough ``set([1,2,3]) == NSSet([1, 2, 3])`` evaluates to False,
    even though the values are equivalent. Reversing the order of
    the test (``NSSet([1, 2, 3]) == set([1,2,3])``) results in the
    expected result.

    This is caused by the way equality tests for sets are implemented in
    CPython and is not something that can be fixed in PyObjC.

- BUGFIX: accessing methods through ``anObject.pyobjc_instancMethods`` is
  now safer, before this release this could cause unlimited recursion
  (although I'm not sure if it was possible to trigger this without
  other changes in this release).

- The PyObjC egg now includes the header files that should be used to
  compile to compile the extensions in the framework wrappers, which makes
  it a lot easier to access those headers.

- BUGFIX: The definition for Py_ARG_SIZE_T was incorrect, which causes
  problems in 64-bit code.

- Initial port to Python 3.x

  C-style 'char' characters and 'char*' strings are
  translated to/from byte strings ('str' in Python 2.x,
  'bytes' in Python 3.x). There is no automatic translation
  from Unicode strings.

  Objective-C selector names and encoded type strings are
  byte strings as well.

  NOTE: Python 3 support is pre-alpha at this time: the code compiles
  but does not pass tests yet. The code also needs to be reviewed to
  check for python3<->objc integration (dict.keys now returns a view,
  NSDictionary.keys still returns a basic iterator, ...)

  TODO:

  * Implement new style buffer support when depythonifying an array of
    C structures.

  * Documentation updates

- The Python 3.x port does not support transparent proxies for 'FILE*'
  "objects" because the ``file`` type in Python3 is not implemented on
  top of the C library stdio.

- The Python 2.x port has been enhanced to accept Unicode strings
  in more locations.

- Implement support for PEP-3118, for both Python 2.x and Python 3.x.

  This means that proxying arrays of basic C types to ObjC can now
  make use of the extended type information provided by the PEP-3118
  API.

  Furthermore it is possible to use ``memoryview`` objects with
  ``NSData`` instances, with the limitation that the memoryview *must*
  be cleaned up before the currently active autorelease pool is cleared,
  or the data instance is resized. That's a result of API restrictions
  in Apple's frameworks.

- The PyObjCTest testsuite now supports version-specific tests: for
  Python 2.x it will load modules whose name starts with 'test2\_' and for
  Python 3.x those starting with 'test3\_'. For both versions it will
  load test modules whose name starts with 'test\_' as well.

- Renamed the assertion functions in ``PyObjCTools.TestSupport``, added
  ``assertFoo`` methods and deprecated the ``failIfFoo`` and ``failUnlessFoo``
  methods (simularly to what's happening in the stdlib).

- Added ``objc.propertiesForClass``. This function returns information about
  properties for a class from the Objective-C runtime. The information does
  not include information about properties in superclasses.

- Added ``objc.object_property``. This is class behaves simularly to
  ``property``, but integrates better with Objective-C code and APIs like
  Key-Value Observation.

- Added ``objc.array_property``. This is simular to ``objc.object_property``,
  but models a list-like object and implements the right Objective-C interfaces
  for Key-Value Coding/Observations.

- Added ``objc.set_property``. This is simular to
  ``objc.object_property``, but models a set-like object and implements the
  right Objective-C interfaces for Key-Value Coding/Observations.

- Added ``objc.dict_property``. This is simular to
  ``objc.object_property``, but models a dict-like object and implements the
  right Objective-C interfaces for Key-Value Coding/Observations.

- NOTE: The interfaces of ``array_property``, ``set_property`` and ``dict_property``
  are minimal w.r.t. options for tweaking their behaviour. That will change in
  future versions of PyObjC.

  Please let us know which hooks would be useful.

- The documentation is now written using Sphinx.

  NOTE: This is an operation in progress, the documentation needs work to be
  truly useful.

- The (undocument) module ``PyObjCTools.DistUtilsSupport`` is no longer
  present.

- Converting a negative value to an unsigned integer now causes
  a deprecation warning, this will be a hard error once I update
  all framework wrapper metadata.


Version 2.2 (2009-11-24)
------------------------

- BUGFIX: Ensure PyObjC compiles cleanly with Python 2.6.4.

- BUGFIX: It is now possible to explicitly define ``__getitem__`` (and other
  special methods) if your class implements ``objectForKey:``::

      class MyObject (NSObject):
          def objectForKey_(self, k):
	     pass

	  def __getitem__(self, k):
	     pass

  In previous version of PyObjC the implementation of ``__getitem__`` would
  silently be replaced by a generic one.

- The default value for the ``__useKVO__`` attribute in class definitions
  can now be controlled by ``objc.setUseKVOForSetattr(b)``. The default
  is ``True``.

  Note: in previous versions the default was ``False``.

  Note2: the ``__useKVO__`` attribute is an implementation detail and should
  not be used in normal code.

  This change fixes an issue where KVO failed to detect some changes when
  those changes were done in Python using attribute access syntax.

- Wrappers for ``objc_sync_wait``, ``objc_sync_notify`` and
  ``objc_sync_notifyAll`` have been removed. These have never been part of
  the public API and this should therefore not affect existing code.

- BUGFIX: There was a refcount leak in the code that proxies native code to
  Python. This causes refcount leaks in user code when a Python class is
  instantiated from native code, when that class has an initializer written
  in Python.

  Thanks to Dirk Stoop of Made by Sofa for providing the bugreport that helped
  fix this issue.

- ``objc.recycleAutoreleasePool`` is now a no-op when a python bundle is loaded
  in an Objective-C program and the PyObjC's global release pool gets drained
  by an outer release pool. This should not affect user programs.

- BUGFIX: Storing pure python objects in a ``NSKeyedArchiver`` archive didn't
  full work for all tuples, especially self-recursive tuples.

  The current support for archiving Python objects passes all pickle unittests
  in Python 2.7.

- BUGFIX: ``+new`` is supposed to return an already retained object (that is,
  the caller owns a reference). Until now PyObjC has assumed that the return
  value of ``+new`` is an autoreleased value. The same is true for all class
  methods whose name starts with ``new``.

- There is initial support for Objective-C blocks, based on the implementation
  description in the `clang repository`__. Blocks are represented in Python
  as callable objects. This means you can pass an arbitrary callable when
  an Objective-C argument is a block, and that when your method accepts a block
  it will get passed a callable object.

  There are some limitations on the usage of blocks due to lack of introspection
  in the current implementation of blocks. This has two side-effects:

  * There must be metadata to describe the signature of blocks in PyObjC's
    metadata XML files.

  * Block metadata is not retained when a block is stored in an ObjC datastructure,
    such as an ``NSArray``, and there are no direct references to the block from
    Python.

.. __: https://clang.llvm.org/docs/Block-ABI-Apple.html

- ``objc.inject`` is no longer support. This was code that had no real relation
  to the rest of PyObjC and was only working in 32-bit mode with little reason
  to expect that it would ever be ported to 64-bit mode.

- Move the testsuite from ``objc.test`` to ``PyObjCTest`` and no longer
  install the tests.

  The tests are no longer installed because they aren't needed for
  day-to-day usage of PyObjC. Furthermore this change will make it possible
  to copy all of the pyobjc-core "egg" into an application bundle without
  adding unnecessary files to that bundle.

- BUGFIX: Storing pure python objects in a ``NSKeydArchiver`` archive didn't
  work 100% reliably for Python floats. I've changed the implementation on
  for encoding floats a little and now floats do get rounddtripped properly.

  The side effect of this is that archives written by PyObjC 2.2b2 or later
  cannot always be read by earlier versions (but PyObjC 2.2b2 can read archives
  created with earlier versions).

- BUGFIX: Enable building from source with the Python.org binary distribution.

- BUGFIX: Fix crash when using the animotor proxy feature of CoreAnimation.
  That is, the following code now works:

  .. sourcecode:: python
     :linenos:

      app = NSApplication.sharedApplication()
      window = NSWindow.alloc().init()
      anim = window.animator()
      anim.setAlphaValue_(1.0)


- Improve handling of non-methods in objc.Category:

  * The docstring of a category is now ignored

  * You'll get an explicit error exception when trying to add and ``ivar`` to
    a class

  * It's now possible to add class attributes in a category:

    .. sourcecode:: python
       :linenos:

          class NSObject (objc.Category(NSObject)):
              aClassDefault = [ 1, 2, 3 ]

              @classmethod
              def getDefault(cls):
                  return cls.aClassDefault



- Fixed support for ``FSRef`` and ``FSSpec`` structures.

  * Transparently convert ``Carbon.File.FSRef`` and ``Carbon.File.FSSpec``
    instances to C.

  * The types ``objc.FSRef`` and ``objc.FSSpec`` are the native
    PyObjC representation for ``FSRef`` and ``FSSpec`` structures.

- Added more magic signature heuristics: the delegate selector for
  sheets is now automatically recognized, removing the need for
  the decorator ``AppHelper.didEndSelector`` (which will stay present
  for backward compatibility).

  FIXME: Do the same thing for ``objc.accessor``. Both are a frequent
  source for errors.

- Added ``PyObjC.TestSupport``. This is an unsupported module containing
  useful functionality for testing PyObjC itself.

- Added ``free_result`` attribute to the ``retval`` element in metadata
  files. When this attribute has value ``'true'`` the return value of the
  C function (or ObjC-method) will be free-ed using the function ``free()``,
  otherwise the bridge assumes other code is responsible to free the result.

  This is to be used for low-level C API's that return a pointer to a
  dynamically allocated array that is to be free-ed by the caller. One example
  is the function ``DHCPClientPreferencesCopyApplicationOptions`` in the
  SystemConfiguration framework.

- Added ``objc.context``, which is helpful for dealing with "context"
  arguments as used by several Cocoa APIs. The context argument must be
  a number in Python, while you'd prefer to pass in an arbitrary object
  instead. The ``objc.context`` registry allows you to get a context
  integer for an arbitrary Python object, and retrieve that later on.

  To get the context integer for a Python object:

  .. sourcecode:: python

        ctx = objc.context.register(myValue)

  To unregister the object when you no longer need the context integer:

  .. sourcecode:: python

        objc.context.unregister(myValue)

  To retrieve the Python object given a context integer:

  .. sourcecode:: python

        myValue = objc.context.get(ctx)


  NOTE: This API is particularly handy when using Key-Value Observing, where
  the context number should be a unique value to make ensure that KVO usage
  by the superclass doesn't get confused with your own usage of KVO.

- PyObjC can now run in 64-bit mode.

  NOTE: 64-bit support is beta quality, that is: all unittests pass, but I
  haven't tried running real programs yet and hence there might be issues
  lurking below the surface.

  NOTE: 64-bit support does not yet work on PPC due to a bug in libffi which
  prevents catching Objective-C exceptions.

  This requires Leopard (OSX 10.5), earlier version of the OS don't have a
  64-bit Objective-C runtime at all.  This currently also requires a copy of
  python that was build with ``MACOSX_DEPLOYMENT_TARGET=10.5``.

  Note that class posing (the ``poseAsClass_`` class method) is not supported
  in 64-bit mode. It is also not possible to create new protocols in 64-bit
  code. Neither are supported by the 64-bit runtime APIs (that is, it is a
  restriction in Apple's Objective-C 2.0 runtime).

- There now is a custom proxy class for instances of ``datetime.date`` and
  ``datetime.datetime``, which takes away the need to manually convert these
  instances before using them from Objective-C (such as using an
  ``NSDateFormatter``)

- Objective-C classes that support the ``NSCopying`` protocol can now be
  copied using ``copy.copy`` as well.

..
   it would be nice to have the following, but that's not easy to achieve::
	- Objective-C classes that support the ``NSCoding`` protocol can now be
	  copied using ``copy.deepcopy``.

- ``OC_PythonArray`` and ``OC_PythonDictionary`` now explicitly implement
  ``copyWithZone:`` and ``mutableCopyWithZone:``, copies will now be
  Python objects instead of regular ``NSDictionary`` instances.

- Pure Python objects now support the ``NSCopying`` protocol.

- A new decorator: ``objc.namedselector`` for overriding the Objective-C
  selector. Usage:

  .. sourcecode:: python
     :linenos:

     class MyObject (NSObject):

         @objc.namedselector("foo:bar:")
         def foobar(self, foo, bar):
             pass

- A number of new type signature values were added. These are not present
  in the Objective-C runtime, but are used to more precisely describe the
  type of some arguments.

  The new values are:

  * ``_C_UNICHAR``:   A "UniChar" value in Objective-C

  * ``_C_NSBOOL``:    A "BOOL" value in Objective-C

  * ``_C_CHAR_AS_INT``: A "char" in Objective-C that is used as a number

  * ``_C_CHAR_AS_TEXT``: A "char" in Objective-C that is used as a character

  PyObjC will automatically translate these values into the correct Objective-C
  type encoding when communicating with the Objective-C runtime, making this
  change transparent to anyone but Python users.

  NOTE: ``_C_CHR`` is of course still supported, with the same semi-schizofrenic
  behaviour as always.

  NOTE2: The non-standard metadata extensions we used before to indicate
  that a C short is used as a unicode string are no longer supported.

- Output arguments are no longer optional. They must be specified both in
  method implementations and method calls. In PyObjC 2.0 they were optional,
  but raised a deprecation warning, for backward compatibility with PyObjC 1.x.

  The backward compatibility code was removed because it made code more
  complicated and actually caused some bugs.

- In PyObjC 1.x you could redefine an Objective-C class, as long as you
  redefined it in the same module (such as by reloading a module). That
  functionality didn't work in PyObjC 2.0 and is now completely removed
  because the functionality isn't supported by the Objective-C 2.0 runtime.

- Adds custom wrappers for some more Python types:

  * ``OC_PythonNumber``: wraps python numeric types

    This is used instead of ``NSNumber`` because we might loose information
    otherwise (such as when using custom subclasses of ``int``).

  * ``OC_PythonSet``: wraps a python set and is a subclass of ``NSMutableSet``

- BUGFIX: ``OC_PythonEnumerator`` now actually works.

- BUGFIX: using the ``@throw`` syntax one can raise arbitrary objects as
  exceptions (not just instances of NSException) in Objective-C. All
  instances of NSObject are now converted to Python exceptions, throwing
  some other object (such as a C++ exception) will still case a fatal
  error due to an uncaught exception.

  (SF Bug: 1741095)

- BUGFIX: ``repr(CoreFoundation.kCFAllocatorUseContext)`` now works

  (SF Bug: 1827746)

- BUGFIX: The wrappers for CoreFoundation types no longer create a new type
  in the Objective-C runtime, that type wasn't used anywhere and was an
  unwanted side-effect of how CoreFoundation types are wrapped.

- BUGFIX: The docstring for newly defined methods is no longer hidden
  by PyObjC. That is, given this code:

  .. sourcecode:: python
     :linenos:

  	class MyObject (NSObject):
	    def doit(self):
	        "do something"
		return 1 + 2

  ``MyObject.doit.__doc__`` now evaluates to ``"do something"``, in previous
  versions of PyObjC the docstring was ``None``.

- BUGFIX: Fixed calling and implementation methods where one or more
  of the arguments are defined as arrays, like this:

  .. sourcecode:: objective-c

  	-(void)fooCallback:(NSRect[4])rects;

  There were various issues that caused these to not work correctly in
  all earlier versions of PyObjC (which wasn't noticed earlier because
  Apple's frameworks don't use this construction).

- BUGFIX: correctly select the native implementation of the compatibility
  routines for the ObjC 2.0 runtime API when running on 10.5 (when compiled
  for OSX 10.3 or later).

- BUGFIX: fix a number of compatibility routines (ObjC 2.0 runtime API
  on OSX 10.4 or earlier).

Version 2.0.1 (included with OSX 10.5.2)
----------------------------------------

- BUGFIX: ``objc.inject`` works on Leopard (at least on Intel Macs, haven't
  tested on PPC).

- BUGFIX: don't crash when printing CF objects that are magic cookies.

- BUGFIX: It is now possible to override ``respondsToSelector:`` in Python.

- Add support for interacting with '@synchronized' blocks in Objective-C.

  The function ``object_lock(object)`` is a contextmanager that acquires and
  releases the '@synchronized' mutex for an object, and can also be used
  manually.

  That is (as context manager):

  .. sourcecode:: python
     :linenos:

  	from __future__ import with_statement

	obj = NSObject.new()

	with objc.object_lock(obj):
	   # Perform work while owning the @synchronize lock
	   pass

  or (manually):

  .. sourcecode:: python
     :linenos:

   	obj = NSObject.new()
	mutex = objc.object_lock(obj)
	mutex.lock()
	try:
	    # Perform work while owning the @synchronized lock
	    pass
	finally:
	    mutex.unlock()

  Note that the first version is slightly saver (see the documentation
  for with-statements for the details).

Version 2.0 (MacOS X 10.5.0)
----------------------------

- The basic infrastructure for playing nice in a GC host was added.

  This doesn't mean that PyObjC now actually plays nice with the ObjC
  garbage collector, some more development and much more testing is
  needed for that.

  Even so, the end result is about as good as we have without GC,
  programs won't make optimal use of GC because that would require
  surgery on the Python interpreter itself.

- The metadata returned by the ``__metadata__`` method is slightly changed
  to make it more compatible with the XML files.

- Some of the older metadata attributes, such as ``isAlloc`` and
  ``doesDonateRef`` were dropped. ``isAlloc`` isn't needed for anything but
  a number of now hardcoded methods (``+alloc`` and ``+allocWithZone:``),
  ``doesDonateRef`` is available through the new metadata mechanism.

- Fix a memory leak in the code that creates the python representation for
  method lists.

- Speed up framework loading due to three changes:

  1. Don't rescan the list of classes unless the framework actually defines
     new classes.

  2. The metadata loader now implemented in C.

  3. CF wrapper types (e.g. CGContextRef) no longer have methods
     corresponding to global functions, the speed-hit for calculating
     these is too large.

- It is now conveniently possible to create instance variables with
  a specific type (e.g. without manually making up a encoded type
  string):

  .. sourcecode:: python
     :linenos:

      class MyObject (NSObject):
          bounds = objc.ivar.NSRect()
          done = objc.ivar.bool()

- Objective-C metaclasses are modelled as Python metaclasses.  This brings
  a major improvement: class methods "just work"(TM):

  .. sourcecode:: python
     :linenos:

     o = NSObject.alloc().init()
     o.description()

     NSObject.description()

  In earlier versions of PyObjC the second call would fail because
  ``NSObject.description`` referred to an unbound instance-method instead of
  to the class method.

  This change should require little or change to existing code. There's only
  two types of code where the new behaviour is incompatible:

  1) Code that introspects the class dictionary to see what methods are
     available. These will no longer see class methods, but will have to look
     at the metaclass as well. This affects ``pydoc(1)`` as well.

  2) Code that uses unbound instance methods will no pick up class methods
     in some occasions. Use ``MyClass.instanceMethodForSelector_`` instead of
     unbound methods, or alternatively access instance methods through
     ``MyClass.pyobjc_instanceMethods``.

  3) Due to a limitation in the implementation of python's ``super`` class [#f1]_
     it is not possible to use the super machinery to resolve class methods.

     However, ``from Foundation import *`` will replace the builtin ``super``
     by a subclass that does work correctly for PyObjC programs, therefore
     this doesn't affect most PyObjC-using programs.


.. [#f1] It is not possible to override the way ``super`` looks for the "next"
   method to call. The class ``objc.super`` is a subclass of the builtin
   superclass with a ``__getattr__`` implementation that does the right thing
   for supercalls for Objective-C class methods.

- It is now easily possible to tell PyObjC that a Python type should be
  treated like a builtin sequence type:

  .. sourcecode:: python
     :linenos:

  	import UserList, objc

	class MyClass (UserList.UserList):
	    pass

	objc.registerListType(MyClass)

- And likewise for mapping types using ``objc.registerMappingType``.

- ``objc.enableThreading()`` is gone. It was introduced in ancient times to
  enable threading in the Python runtime but has been a no-op for ages because
  the PyObjC enables threading by default now.

- The unittests can now use the leaks(1) command to check for memory leaks. This
  slows testing down significantly and is therefore off by default. Enable by
  setting ``PYOBJC_WITH_LEAKS`` to a value in the shell environment before running
  the tests:

  .. sourcecode:: sh

       $ PYOBJC_WITH_LEAKS=1 python setup.py test

   NOTE: the actual value is ignored, as long as there is a value.

- (BUGFIX): PyObjC was leaking memory when doing scans of the Objective-C method tables

- (BUGFIX): The code below now raises an error, as it should have done in previous versions but never
  did:

  .. sourcecode:: python
     :linenos:

       class MyObject (object):
           def updateDescription(self):
               self.description = 42


- PyObjC has been split into several smaller packages: ``pyobjc-core`` contains
  the core bridge and frameworks are wrapped as separate setuptools packages.

- Objective-C objects now have an implicit attribute named ``_`` which can
  be used a shortcut for Key-Value-Coding.

  The code fragment below:

  .. sourcecode:: python
     :linenos:

  	o = <Some Objective-C Object>
	print o._.myKey
	o._.myKey = 44

  is equivalent to:

  .. sourcecode:: python
     :linenos:

	print o.valueForKey_('myKey')
	o.setValue_forKey_(44, 'myKey')

  The former is much nicer to use.

- Struct wrappers now have a ``copy`` method. This method tries to do the right
  thing when subfields are other struct wrappers (that is, deep-copy them).

- The metadata system has been revamped and mostly removes the need to write
  C-code when wrapping frameworks (that includes most of the AppKit and
  Foundation wrappers as well). The metadata is loaded at runtime from
  an XML file, whose format is shared between PyObjC and RubyCocoa.

  ``objc.initFrameworkWrapper`` can be used to load a framework using
  these XML metadata files.

  Note: because we now use an XML metadata file the scripts in
  ``Scripts/CodeGenerators`` have been removed: they are no longer needed. Have
  a look at the project ``pyobjc-metadata`` if you want to generate your own
  metadata.

  Note2: the metadata format is shared with RubyCocoa, although there are
  currently some slight differences (that is, the PyObjC metadata is slightly
  richer).

- PyObjC now has builtin support for CoreFoundation-based types, which is
  used by the new metadata file support.  Note that doesn't mean we support
  all of CoreFoundation and other CF-based frameworks, just that the machinery
  that's needed for that is present and working.

  This is a backward incompatible change: CF-based types will now be proxied
  using PyObjC-owned types instead of the ones in MacPython.  However, PyObjC
  will still convert MacPython CF-wrappers to the right native type.

  Another backward compatible change: ``registerCFSignature`` has a different
  signature:

  .. sourcecode:: python

      registerCFSignature(name, encoding, typeId [, tollfreeName]) -> type

  This is needed to capture all information about CF types.

- This version introduces generic support for callback functions. The metadata
  mentioned before contains information about the signature for callback
  functions, the decorator ``callbackFor`` converts a plain function to
  one that can be used as a callback:

  .. sourcecode:: python
     :linenos:

  	@objc.callbackFor(NSArray.sortedArrayUsingFunction_andContext_)
	def compare(left, right, context):
	    if left.key < right.key:
	        return NSOrderedAscending
	    elif left.key > right.key:
	        return NSOrderedDescending
   	    else:
	        return NSOrderedSame

  The ``makeCallbackFor`` callback should be used for callbacks where the
  callable is stored by the called function and is optional otherwise (such
  as the example above).

- The decorator ``selectorFor`` can be used to ensure that a method has the
  right signature to be used as the callback method for a specific method.

  Usage:

  .. sourcecode:: python

 	@objc.selectorFor(NSApplication.beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_)
	def sheetDidEnd_returnCode_contextInfo_(self, sheet, returnCode, info):
	    pass

- PyObjC compiled on Leopard uses the Objective-C 2.0 runtime.

  The compiler on 10.5 still gives warning about usage of deprecated APIs unless
  compiling for 10.5 or later because of a compatibility layer.

- GNUstep support has been removed because this has never worked properly,
  nobody seems interested in fixing that and the internal APIs of PyObjC have
  changed greatly.

- Output arguments are treated slightly different. In previous versions you
  were not allowed to pass values for output arguments.

  This is now deprecated behaviour, you should choose to supply values for all
  arguments including output arguments (mixing these two styles is not
  allowed, if you have two output argument you must either supply a value for
  both of them or neither).

  There are only two acceptable values for output argument:

  * ``None``: pass a non-NULL pointer to the objc function/method

  * ``objc.NULL``: pass a NULL pointer to the objc method.

  The already existing behaviour is the same as passing in ``None`` for all
  output arguments.

  This is most useful for suppressing an ``NSError`` value for methods that
  have an ``NSError**`` argument (when you don't want to look at that value),
  because generating that object might be expensive.

- ``objc.setSignature`` is deprecated, use the new metadata machinery instead.

- Opaque types (such as NSZonePointer) are now mutable, which is mostly present
  to allow framework wrappers to provide a nice OO interface to those types
  instead of forcing users to use the procedural API.

  None of the current framework wrappers use this feature.

- Several new methods were added to improve integration with a future version
  of MacPython: opaque pointer types and ``NSObject`` now have a method
  named ``__cobject__`` that returns a ``PyCObject`` which represents the
  proxied value. Furthermore both opaque pointer types and subclasses of
  ``NSObject`` are now callable and will create the proper proxy object when
  passed a ``PyCObject``. Note however than the caller is responsible to ensure
  that the ``PyCObject`` value represents a value of the right type.

- Archiving pure python objects using ``NSArchiver`` was already unsupported,
  we now explicitly raise an exception when users try to do this anyway. It
  is supported to archive and retrieve simple values: instances of ``int``,
  ``long``, ``float``, ``str`` and ``unicode``.

- A ``__del__`` or ``dealloc`` method can revive objects, which isn't really
  supported by Objective-C. We'll now warn about this, hopefully before the
  program crashes. The warning is ``objc.RevivedObjectiveCObjectWarning``.

- Some functions and methods return an instance of ``objc.varlist``. These
  objects behave a little like tuples, but don't have a defined length, you
  are responsible to not peak beyond the end of the actual array.

  The best way to deal with these objects is to convert them to real tuples
  as soon as possbible (using the ``as_tuple`` method). The number of elements
  in that tuple should be known to you and depends on the API.

  These objects are used in places where objects return an array but the
  size of that array cannot be described using the bridge metadata. These
  are mostly arrays whose size depends on the state of an object, or whose
  size is a function of one or more arguments of the method.

- There now is a public API for adding new "convenience methods", that is
  methods that emulate standard Python methods using Objective-C methods.

  There are two functions for adding new convenience methods:

  * ``addConvenienceForSelector`` adds a list of methods to a class when that
    class has the specified selector:

  .. sourcecode:: python

       addConvenienceForSelector('hash', [
       		('__hash__', lambda self: self.hash()),
	])

  * ``addConvenienceForClass`` adds a list of methods to the class with the
     specified name:

  .. sourcecode:: python

       addConvenienceForSelector('NSObject', [
       		('dummy', lambda self: 42 ),
	])

  In both cases the addition is done lazily, the class that will be changed
  need not be loaded at the time of the call.

- Fix a long-standing race condition where one could end up with a reference
  to an already deallocated Objective-C object when the last ObjC reference
  goes away on one thread and is just "recreated" on a second thread.

- The 'name' and 'reason' of an Objective-C exception are now represented as
  Unicode objects in the Python representation of the exception, instead of
  as a UTF-8 encoded string.

  The standard Python exception message is still a UTF-8 encoded string,
  that's needed to ensure that we can always print the value of the exception
  message (such as in tracebacks).

Version 1.4.1 (2006)
--------------------

- PyObjC now uses setuptools. Setuptools support is fairly minimal at the
  moment, we expect to move more of the build infrastructure to setuptools and
  to split PyObjC into smaller eggs.

- Fix an issue that made is possible to create weakref's to subclasses of
  subclasses of Objective-C classes. This was unintentional behaviour, the
  weakref is to the proxy (see the news for 1.0b1 for more details).

- Add RoundTransparentWindow and DragItemAround examples in ``Examples/AppKit``.

  Both are ports of Objective-C examples at ADC and were provided by
  ytrewq1.

- Fix issue where programs would crash with an badly aligned C-stack on
  some problems. This issue only affected Intel systems.

- Remove ``OC_PythonObject.pythonifyStructTable``. This method of wrapping
  structs was untested and not used in the core distribution. Use
  ``objc.createStructType`` instead.

- Binaries build on 10.4 also work on 10.3. This means it is no longer
  necessary to build PyObjC on the lowest version of the OS that you want
  to run your binaries on.  Doing this with python is somewhat of a black
  art, please test your applications on the lowest version of the OS that
  you want to support to make sure that this actually works.

Version 1.4 (2006-06-14)
--------------------------

- Classes whose name starts with and underscore are no longer imported when
  using ``objc.loadBundle``. They are still available using
  ``objc.lookUpClass``.

  Methods whose name starts with an underscore are no longer visible when
  introspecting using ``dir()``, but can still be called.

  These changes were done to make introspection slightly more user-friendly:
  anything that is now hidden from introspection is most likely not part of
  a public API.

- Most of the libffi testsuite is now run using a module that emulates
  dejagnu.

- Introduction of a GUI tool to manage custom method signatures
  (``Tools/Signatures``). This replaces the ``find-raw-pointers.py`` script.

- Fixed memory leak in ``OC_PythonObject``, this was due to bad reference
  counting.

- ``NSMutableArray.sort`` now has the same API as ``list.sort``. Due to
  implementation constraints the ``key`` argument results in slower sorting
  than you'd see with ``list.sort``.

- Selectors now have a read-only property 'native_signature' that contains
  the untampered signature for the method. This is for use by tools.

- 'void*' arguments are treated like unsigned integers, they are almost always
  opaque cookies.

- ``FILE*`` arguments are recognized and mostly work correctly. We can't
  reliably detect if the file was opened in append mode though.

- Make it possible to override the KVO methods, like ``setValue:forKey:`` and
  ``valueForKey:`` in Python for all levels in the inheritance hierarchy.

- Fix issues with reference counts for ``__slots__``.

- Experimental: use ``-autorelease`` instead of ``-release`` to release
  values in destructors. This seems to solve at least one memory management
  issue.

- A slight complication in the naming rule:

  1) Don't translate leading underscores in Python to colons in Objective-C,
     ``_doFoo_andBar_`` in Python will be ``_doFoo:andBar:`` in Objective-C.

  2) If a name starts and ends with double underscores don't modify the
     name at all when moving from Python to Objective-C,
     ``__foobar__`` in Python will stay that way in Objective-C.

  These changes fix some minor annoyances with the older scheme. Note that
  the translation from Objective-C to Python is unmodified and is entirely
  consistent with the modified rules for translating from Python to Objective-C.

- Fix for a memory leak in ``__pyobjc_object__`` handling.

Version 1.3.7 (2005-07-06)
--------------------------

- Added wrappers for embedded DiscRecording frameworks
  ([ 1224188 ] Fix for DiscRecording framework)

- Probably working Xcode 2.1 support (for converted Xcode 2.0 projects)

- Hide List, Object, and Protocol classes from objc.loadBundle
  to prevent confusion with Python code.  They can still be looked
  up with objc.lookUpClass.

- Fixed a regression where type signatures for pointers weren't
  normalized (fixes uses of NSModalSession, etc.)

- Fixed a bug with -[NSObject hash] to __hash__, there was a mismatch
  between integer types.

- Removed traces of the old Project Builder and Xcode templates in the
  examples and Foundation initialization code (PYOBJCFRAMEWORKS).

- Fixed a problem with reference counting in initializers.

- New TinyURLService example in AppKit that demonstrates how to write
  a service that transforms URLs into their tinyurl.com equivalents.

- Ported to macOS on Intel. This is an initial, experimental port. The
  Intel ABI has not been finalised yet. It is also possible to build fat
  binaries, that option should not be used in production builds.

- Support a number of new frameworks:

  * SenTestingKit

    TODO: this framework uses lots of macros (such as STAssertEquals), these
    have not yet been wrapped/converted.

  * SecurityFoundation


Version 1.3.6 (2005-05-19)
--------------------------

- Fixed bugs in the ProgressViewPalette example

- Fixed a bug in the class builder that caused most plugins to break

- Removed all references to Project Builder

- macOS 10.2 (Jaguar) no longer supported

Version 1.3.5 (2005-05-18)
--------------------------

- Importing objc now ensures that Foundation is multi-threaded, previously
  it only ensured that Python was.

- New ``objc.RegisterCFSignature`` used to register ``CFTypeRef``-like
  signatures with the runtime.

- ``PyObjCTools.Conversion`` functions now support all property list
  types with the following conversions:

  - NSData <-> buffer
  - NSDecimalNumber <-> decimal.Decimal (if present)
  - NSDate <-> datetime.datetime

  New ``toPythonDecimal``, ``fromPythonDecimal`` functions which convert
  between NSDecimalNumber and decimal.Decimal using an intermediate string.

  New ``serializePropertyList`` and ``deserializePropertyList`` functions
  which serialize (Objective-C) property lists to and from NSData.

- ``OC_PythonObject``, the proxy for Python objects that do not have
  an Objective-C superclass and are not otherwise special-cased, now
  act slightly more like typical Objective-C objects (supporting
  ``-isEqual:``, ``-hash``, and ``-compare:``).  This allows them
  to work with Key-Value Coding if they are contained by an Objective-C
  object, among other things.

- New objc.signature decorator that allows easier specification of
  objc.selector wrappers for functions when using Python 2.4:

  .. sourcecode:: python

     @objc.signature('i@:if')
     def methodWithX_andY_(self, x, y):
         return 0

- ``PyObjCTools.KeyValueCoding.getKeyPath`` now supports all of the
  Array Operators supported by macOS 10.4.

- Key-Value Coding of Python objects (whether or not using an Objective-C
  base class) should act like Objective-C now.  In previous versions
  there were inconsistencies with the use of capitalization, the
  underscore postfix in setters, and Key-Value Observing.

- The formal protocol list is now complete.  A new internal function,
  ``objc.protocolsForProcess()`` enumerates over all mach
  headers and returns all of the protocols defined in the expected
  place.  This fixes the scenario where an application uses a
  protocol but does not define any classes that
  conform to that protocol (i.e. to check plugin conformity).
  Previously it was not possible to reach these protocols simply by
  walking over all of the classes.

- A special value, ``objc.NULL``, may now be passed in the place
  of 'in' and 'inout' arguments.  This tells the bridge to pass
  a NULL pointer to the Objective-C method, instead of a pointer
  to the value.  The return value will still be a tuple of the
  expected size.

- Some of the new Tiger frameworks now have wrappers:

  - ``AppleScriptKit``
  - ``Automator``
  - ``CoreData``
  - ``DiscRecording``
  - ``DiscRecordingUI``
  - ``OSAKit``
  - ``Quartz``
  - ``QTKit``
  - ``SyncServices``
  - ``XgridFoundation``

  Documentation and tests not yet written.

- New ``OutlineEditor`` example in ``Examples/CoreData``,
  it is a Python version of the identically named Apple example.

- The last argument of selectors that end with ':error:' is now
  assumed to be 'out' if its type is an object pointer.

- More conveniences for ``list``-like and ``dict``-like
  objects: ``__reversed__``, ``reverse``, ``pop``,
  ``remove``, ``fromkeys``.

- ``OC_PythonDictionary`` and ``OC_PythonArray`` now return
  ``NSNull`` to Objective-C callers as appropriate.

- New ``WebKitInterpreter`` example in ``Examples/Plugins``.
  Uses the new WebKit Cocoa plugin API available in Safari 1.3
  and later to embed a PyInterpreter in the browser.

- Fixed a ``CFBundleRef`` reference counting bug in
  ``Foundation._Foundation``.  The symptom of this is usually
  a crashing application after having loaded a PyObjC-based
  plugin into an otherwise Objective-C app.

- New ``PyObjCTools.AppHelper`` functions: ``callAfter`` and
  ``callLater``, conveniences for calling Python functions on
  the main thread as soon as possible, or after a delay.

- Twisted examples changed to use ``threadedselectreactor``
  instead of ``cfreactor``.  ``cfreactor`` is deprecated.
  Needs Twisted newer than 2.0 (svn r13575 or later).

- ``objc.inject`` now injects on main thread by default,
  and takes an optional third ``useMainThread`` argument
  to change this behavior.  This is a complete rewrite
  which should be correct, stable, Tiger compatible,
  and synchronized with mach_* 1.1.

- Removed an ``NSAutoreleasePool`` category hack that has
  been deprecated for quite some time.

- New ``objc.removeAutoreleasePool`` function that will remove
  PyObjC's global ``NSAutoreleasePool``, which may be useful
  for plugins.

- Fixed bug in the ``NSBundle`` hack that caused a ``NULL``
  pointer dereference if looking up a non-existent class using
  ``NSBundle`` API.

- Added ``OC_PythonUnicode`` and ``OC_PythonString`` classes that
  preserve the identity of ``str`` and ``unicode`` objects across
  the bridge.  The bridge for ``str`` now uses the default
  encoding of ``NSString``, rather than ``sys.getdefaultencoding()``
  from Python.  For macOS, this is typically MacRoman.  The reason
  for this is that not all Python ``str`` instances could cross the
  bridge at all previously.  ``objc.setStrBridgeEnabled(False)`` will
  still trigger warnings, if you are attempting to track down an
  encoding bug.  However, the symptoms of the bug will be incorrectly
  encoded text, not an exception.

- New Xcode project template "PyObjC Mixed Application" that is
  a py2app based Python application that loads an Objective-C
  plug-in built as a separate target.

- New py2app based Xcode templates "PyObjC Application" and
  "PyObjC Document-based Application", these replace the
  older "Cocoa-Python Application" and
  "Cocoa-Python Document-based Application" respectively.

- New ``InjectBrowser`` example in ``Examples/Inject`` that demonstrates
  injection of the ``ClassBrowser`` example into another application using
  ``objc.inject``.

- ``NSData`` and ``NSMutableData`` instances now support the Python buffer
  protocol.

- ``NSData`` instances now support a convenience API that allow them to
  act like a ``buffer`` instance for ``str()`` and slicing.

- Objects that support the Python buffer protocol, such as ``buffer`` and
  ``array.array`` (but not ``str`` or ``unicode``) are now bridged as
  ``NSData`` subclasses.

Version 1.3 (2005-03-31)
------------------------

- New ``objc.pyobjc_id`` function that returns a the id of the underlying
  NSObject as an integer.  (Python wrapper objects are often made on the
  fly, meaning ``id(obj)`` is not constant during the lifetime of the
  object.)

- The bridge now maintains object identity across the bridge
  in both directions. Previous versions of the bridge only did this when
  bridging from Objective-C to Python.

  Exceptions: ``NSString`` and ``NSNumber`` do not have unique proxies.  These
  types are converted to subclasses of Python types as appropriate, so they
  can not have unique proxies.  The identity of the original Objective-C
  object is maintained by these subclasses, but there may be many Python
  "value proxies" for a single Objective-C object.

  Any Python object that is proxied using the ``__pyobjc_object__``
  interface will only get a unique proxy if the ``__pyobjc_object__``
  method implements that feature.

- New ``objc.protocolsForClass`` function that returns a list of protocols
  that the class directly claims to conform to.

- PyObjC classes can now declare that they implement formal protocols,
  for example:

  .. sourcecode:: python

     class MyLockingClass(NSObject, objc.protocolNamed('NSLocking')):
         # implementation
         pass

  It is also possible to define new protocols:

  .. sourcecode:: python

       MyProtocol = objc.formal_protocol("MyProtocol", None, [
       	selector(None, selector='mymethod', signature='v@:'),
       ])

  All formal protocols are instances of ``objc.formal_protocol``.

- PyObjCTools.KeyValueCoding has a new ``kvc`` class that allows
  Pythonic Key-Value Coding.

  - ``__getitem__`` is mapped to ``valueForKeyPath:``
  - ``__setitem__`` is mapped to ``setValue:forKeyPath:``
  - ``__getattr__`` is mapped to ``valueForKey:``
  - ``__setattr__`` is mapped to ``setValue:forKey:``

  The ``kvc`` class uses ``__pyobjc_object__``, so it may cross the bridge
  as the wrapped object.

- ``NSNumber`` instances are bridged to a ``float``, ``long``, or ``int``
  subclass that uses ``__pyobjc_object__``.
  ``NSDecimal`` is converted to ``NSDecimalNumber`` when used as an object,
  ``NSDecimalNumber`` is not bridged to ``NSDecimal`` because the latter is
  a mutable type.

- The Python to Objective-C bridge now looks for a ``__pyobjc_object__``
  attribute to get a PyObjC object from a Python object.

- New IDNSnitch example in Inject that demonstrates how to write an
  monitor for the launch of another application,
  use ``objc.inject`` to load code into a target process,
  and override the implementation of an existing method but still
  call back into the original implementation (method swizzling).

- ``objc.IMP`` should do the right thing now.  This type is returned
  by ``+[NSObject methodForSelector:]`` and
  ``+[NSObject instanceMethodForSelector:]``

- New ToDos example in CocoaBindings that demonstrates how to use
  two array controllers for the same data, and how to use value
  transformers to alter the color of text.  Originally from
  "Cocoa Bindings Examples and Hints", converted to PyObjC by u.fiedler.

- New Bookmarks example in CocoaBindings that demonstrates how to
  subclass ``NSArrayController`` to implement the ``NSTableView``
  delegate drag and drop protocol, including copying of objects between
  documents and accepting URL drops from other applications.  Also
  demonstrates re-ordering of the content array.  Originally from
  "Cocoa Bindings Examples and Hints", converted to PyObjC by u.fiedler.

- New FilteringController example in CocoaBindings that demonstrates
  how to subclass ``NSArrayController`` to implement filtering
  of a ``NSTableView``.  Also demonstrates the use of indexed accessors.
  Originally from "Cocoa Bindings Examples and Hints", converted to PyObjC
  by u.fiedler.

- New ControlledPreferences example in CocoaBindings that demonstrates
  how to use Cocoa Bindings to simplify storing and retrieving user
  preferences.  Originally from "Cocoa Bindings Examples and Hints",
  converted to PyObjC by u.fiedler.

- New TemperatureTransformer example in CocoaBindings that demonstrates
  how to use NSValueTransfomers with PyObjC.  Based on Apple's
  "Cocoa: Value Transformers" documentation, converted to PyObjC
  by u.fiedler.

- New CurrencyConvBindings example in CocoaBindings that demonstrates
  a Cocoa Bindings enabled version of the CurrencyConverter example.
  Converted to PyObjC by u.fiedler from the example in Apple's
  "Introduction to Developing Cocoa Applications Using Bindings".

- New ManualBindings example in CocoaBindings that demonstrates how
  to develop programmatic bindings from a PyObjC application.
  Converted to PyObjC by u.fiedler from the "Cocoa Bindings and Hints"
  example of the same name.

- New HotKeyPython example in AppKit that demonstrates how to use
  Carbon global hot keys from a PyObjC application.  Also demonstrates
  how to use a NSApplication subclass.

- Key-Value Observing support is now automatic in Python classes that
  descend from ``NSObject``, unless they implement a custom
  ``willChangeValueForKey:``, ``didChangeValueForKey:``, or
  ``__useKVO__`` is not True.  This allows ``self.foo = 1`` to
  automatically trigger notifications.  This works in all cases,
  whether ``foo`` is a ``property``, ``ivar``, or just in the
  ``__dict__``.

- New Inject folder in Examples, with an InjectInterpreter
  example that will inject a GUI Python interpreter into any process.

- New ``objc.inject()`` function for macOS 10.3 and later,
  allows an arbitrary bundle to be loaded into another process
  using mach_inject.

- ``objc.classAddMethods`` now recognizes and supports
  classmethods.

- GC is now correctly implemented for struct wrappers.

- The ``NSNumber`` bridge has been removed, now you will get
  ``NSNumber`` instances across the bridge instead of a
  Python representation.

- ``PyObjCTools.AppHelper.runEventLoop()`` will now bring your
  application to the front at startup when using pdb
  mode for convenience.

- ``objc.loadBundle()`` no longer filters the class list.  This
  solves a few potential issues and shaves off about 1/3rd of
  the overhead of ``python -c "import AppKit"``.

- ``PyObjCTools.AppHelper.runEventLoop()`` no longer breaks on
  pure Objective-C exceptions.  Most exceptions of this variety
  are more like warnings, and there is nothing that can be done
  them anyway.

- ``PyObjCTools.AppHelper.runEventLoop()`` now installs the
  interrupt handler and verbose exception logging when using pdb,
  either explicitly or by the USE_PDB environment variable.

- There is now a fast path for the ``NSString``/``unicode``
  bridge when ``Py_UNICODE_SIZE`` is 2.  This is the default
  setting for Python.

- The default selector signature will have a void return value
  unless a "return" statement with an argument is used in the
  bytecode.  In that case, it will default to an object return
  value.

- ``__bundle_hack__`` is no longer necessary, py2app now sets
  a different environment variable to the current plugin during
  execution, and a hack is installed to ``NSBundle`` so that classes
  may respond to requests for their bundle with the ``+bundleForClass``
  method.  The class builder adds a default implementation of this to
  Python classes if this environment variable is set.

- Added ``objc.currentBundle()``, which is equivalent to
  ``NSBundle.mainBundle()`` except after loading a plug-in.
  Makes it easier to load nib files.

- ``PyObjCTools.NibClassBuilder.extractClasses()`` now uses
  ``objc.currentBundle()`` instead of ``NSBundle.mainBundle()``.  This
  makes plugins less of a hassle to develop and allows identical code
  to be used for application or plugin development.

- ``objc.registerPlugin()`` and ``objc.pluginBundle()`` are now deprecated
  as they are no longer useful.

- It is now possible to subclass a class that implements ``copyWithZone:``
  without setting ``__slots__`` to ``()``.

- It is now possible to override ``dealloc``. It is still possible to
  define ``__del__``.

- As an experimental feature it is also possible to override ``retain`` and
  ``release``. Note it almost never a good idea to do this (even when you're
  programming in Objective-C and much more so in Python).

- ``poseAsClass:`` can be used, although it is not very useful in python, use
  categories instead.

  A major issue with ``poseAsClass:`` is that existing references to the old
  version of the class won't be changed to point to the new class.

- It is now possible to access all instance variables of a class using
  the functions ``objc.listInstanceVariables(aClassOrInstance)``,
  ``objc.getInstanceVariable(obj, name)`` and
  ``objc.setInstanceVariable(obj, name, value [, updateRefCount])``.

  The last argument of ``setInstanceVariable`` is required when the instance
  variable is an object. If it is true the bridge will update reference counts,
  otherwise it won't.

- All wrappers for opaque pointers (such as ``NSZone*``) now have the same
  interface and share a single implementation. This decreases code-size and
  makes it easier to add new wrappers.  A new feature is a ``__typestr__``
  attribute on the type object, this contains the encoded Objective-C type
  of the pointer.

  A function for creating new wrappers is exposed to python, as
  ``objc.createOpaquePointerType(name, typestr, doc)``.  The same function is
  also exposed in the C-API.

- Wrappers for C-structs how have a ``__typestr__`` attribute on their type.
  This attribute contains the encoded Objective-C type of the struct.

  The default ``__init__`` for struct-wrappers now initializes fields with an
  appropriate default value, instead of ``None``.

  New wrappers can now be created from Python using the function
  ``objc.createStructType(name, typestr, fieldnames, doc)``. The same
  function is also exposed in the C API (and has been for a while).

Version 1.2 (2004-12-29)
------------------------

- ``PyObjCTools.AppHelper.stopEventLoop`` will attempt to stop the current
  ``NSRunLoop`` (if started by ``runConsoleEventLoop``) or terminate the
  current ``NSApplication`` (which may or may not have been started by
  ``runEventLoop``).

- This version no longer support Python 2.2. Python 2.3 or later is
  required.

- It is now possible to use ``reload`` on modules containing Objective-C
  classes.

- ``objc.loadBundle`` now returns bundle we just loaded.

- Added ``objc.loadBundleVariables`` and ``objc.loadBundleFunctions``,
  two functions for reading global variables and functions from a bundle.

- objc.runtime will now raise AttributeError instead of objc.nosuchclass_error
  when a class is not found.

- objc.Category can be used to define categories on existing classes:

  .. sourcecode:: python

    class NSObject (objc.Category(NSObject)):
        def myMethod(self):
            pass

  This adds method ``myMethod`` to class NSObject.

- ``py2app`` is now used for all Example scripts and is the recommended method
  for creating PyObjC applications.

- Proxies of dict, list, and tuple now respect the invariant that you should
  get an identical instance if you ask for the same thing twice and the
  collection has not been mutated.  This fixes some problems with binary
  plist serialization, and potentially some edge cases elsewhere.

- There is now a ``__bundle_hack__`` class attribute that will cause the PyObjC
  class builder to use a statically allocated class wrapper if one is
  available via certain environment variables.  This functionality is used
  to enable +[NSBundle bundleForClass:] to work for exactly one class from
  a py2app-created plugin bundle.

- We now have a working Interface Builder palette example due to
  ``__bundle__hack__``.

- ``bool(NSNull.null())`` is now false.

- ``setup.py`` supports several new commands:

    build_libffi:

      builds libffi (used by build_ext)

    build_html:
      builds html documentation from ReST source

    bdist_dmg:
      creates a disk image with the binary installer

    bdist_mpkg:
      creates a binary installer

    test:
      runs unit test suite (replaces Scripts/runPyObjCTests
      and Scripts/runalltests)

- ``PyObjCStrBridgeWarning`` can now be generated when Python ``str`` objects
  cross the bridge by calling ``objc.setStrBridgeEnabled(False)``.  It is
  HIGHLY recommended that your application never send ``str`` objects over
  the bridge, as it is likely to cause problems due to the required
  coercion to unicode.

- The coercion bridge from Python to Objective-C instances can now be
  augmented from Python as it is exposed by ``OC_PythonObject``.  See
  ``objc._bridges``.  This is how the ``str`` -> ``unicode`` -> ``NSString``
  bridge with optional warnings is implemented.

- The coercion bridge between Python objects and Objective-C structures
  can now be augmented from Python as it is exposed by ``OC_PythonObject``.
  See ``objc._bridges``.  This is how the ``Carbon.File.FSRef``
  <-> ``'{FSRef=[80c]}'`` structure bridge is implemented.

- Extension modules such as ``_objc``, ``_AppKit``, etc. are now inside
  packages as ``objc._objc``, ``AppKit._AppKit``, etc.  They should never be
  used directly, so this should not break user code.

Version 1.1 (2004-05-30)
------------------------

- KVO now actually works from Python without using nasty hacks.

- Added Xcode template for document-based applications

Version 1.1b2 (2004-04-11)
--------------------------

- More fine-grained multi-threading support

- Xcode templates use a smarter embedded main program

- Add support for WebObjects 4.5 (a one-line patch!)

- Add a PackageManager clone to the Examples directory

- Add better support for NSProxy

  This makes it possible to use at Distributed Objects, although this
  feature has not received much testing

- Function 'objc.protocolNamed' is the Python equivalent of the @protocol
  expression in Objective-C.

- Add several new examples


Version 1.1b1 (2004-02-20)
---------------------------

- Fixes some regressions in 1.1 w.r.t. 1.0

- Add Xcode templates for python files

  You can now select a new python file in the 'add file...' dialog in Xcode

- Fix installer for Panther: the 1.1a0 version didn't behave correctly

- There is now an easier way to define methods that conform to the expectations
  of Cocoa bindings:

  .. sourcecode:: python

     class MyClass (NSObject):

	@objc.accessor
        def setSomething_(self, value):
            pass

	@objc.accessor
        def something(self):
            return "something!"


  It is not necessary to use ``objc.accessor`` when overriding an existing
  accessor method.

Version 1.1a0 (2004-02-02)
--------------------------

- Objective-C structs can now be wrapped using struct-like types. This has
  been used to implement wrapper types for NSPoint, NSSize, NSRange and NSRect
  in Foundation and NSAffineTransformStruct in AppKit.

  This means you can now access the x-coordinate of a point as ``aPoint.x``,
  accessing ``aPoint[0]`` is still supported for compatibility with older
  versions of PyObjC.

  It is still allowed to use tuples, or other sequences, to represent
  Objective-C structs.

  NOTE: This has two side-effects that may require changes in your programs:
  the values of the types mentioned above are no longer immutable and cannot
  be used as keys in dicts or elements in sets. Another side-effect is that
  a pickle containing these values created using this version of PyObjC cannot
  be unpickled on older versions of PyObjC.

- This version adds support for NSDecimal. This is a fixed-point type defined
  in Cocoa.

- NSDecimalNumbers are no longer converted to floats, that would loose
  information.

- If an Objective-C method name is a Python keyword you can now access it
  by appending two underscores to its name, e.g. someObject.class__().

  The same is true for defining methods, if you define a method ``raise__`` in
  a subclass of NSObject it will registered with the runtime as ``raise``.

  NOTE: Currently only ``class`` and ``raise`` are treated like this, because
  those are the only Python keywords that are actually used as Objective-C
  method names.

- Experimental support for ``instanceMethodForSelector:`` and
  ``methodForSelector:``.
  This support is not 100% stable, and might change in the future.

- Backward incompatible change: class methods are no longer callable through
  the instances.

- Integrates full support for MacOS X 10.3 (aka Panther)

- Adds a convenience/wrapper module for SecurityInterface

- It is now safe to call from Objective-C to Python in arbitrary threads, but
  only when using Python 2.3 or later.

- Fixes some issues with passing structs between Python and Objective-C.

- Uses the Panther version of ``NSKeyValueCoding``, the Jaguar version is still
  supported.

- method ``updateNSString`` of ``objc.pyobjc_unicode`` is deprecated, use
  create a new unicode object using ``unicode(mutableStringInstance)`` instead.

- NSAppleEventDescriptor bridged to Carbon.AE

- LibFFI is used more aggressivly, this should have no user-visible effects
  other than fixing a bug related to key-value observing.


- Adds a number of new Examples:

  * OpenGLDemo

    Shows how to use OpenGL with PyObjC

  * SillyBallsSaver

    Shows how to write a screensaver in Python. Requires a framework install
    of Python (that is, MacOS X 10.3 or MacPython 2.3 on MacOS X 10.2).

  * Twisted/WebServicesTool

    Shows how to integrate Twisted (1.1 or later) with Cocoa, it is a
    refactor of the WebServicesTool example that is made much simpler
    by using Twisted.

  * Twisted/WebServicesTool-ControllerLayer

    Shows how to integrate Twisted (1.1 or later) with Cocoa, it is a
    refactor of the WebServicesTool example that is made much simpler
    by using Twisted as it does not need threads. This one also uses
    NSController and therefore requires MacOS X 10.3.

Version 1.0 (2003-09-21)
------------------------

- This version includes a new version of libffi that properly deals with
  complex types on MacOS X.

Version 1.0rc3 (2003-09-14)
---------------------------

- 1.0rc2 didn't include the nibclassbuilder script

- Fix bug in NSRectFillList

Version 1.0rc2 (2003-09-10)
---------------------------

- Fix a number of bugs found in 1.0rc1.

Version 1.0rc1 (2003-08-10)
---------------------------

- Better support for the NSKeyValueCoding protocol.  The module
  ``PyObjCTools.KeyValueCoding`` provides a python interface that makes it
  possible to use key-value coding with python objects as well as
  Objective-C objects. Key-Value Coding also works as one would expect with
  Python objects when accessing them from Objective-C (both for plain Python
  objects and Python/Objective-C hybrid objects).

- objc.pyobjc_unicode objects are now pickled as unicode objects, previously
  the couldn't be pickled or were pickled as incomplete objects (protocol
  version 2).

- Pickling of ObjC objects never worked, we now explicitly throw an exception
  if you try to pickle one: pickle protocol version 2 silently wrote the
  incomplete state of objects to the pickle.

- The default repr() of ObjC objects is now the result of a call to the
  ``description`` method. This method is not called for uninitialized objects,
  because that might crash the interpreter; we use a default implementation
  in that case.

- A minor change to the conversion rule for methods with output arguments
  (pointers to values in ObjC, where the method will write through the pointer).
  If the method has 'void' as its return type, we used to return a tuple where
  the first value is always None. This first element is no longer included,
  furthermore if the method has only 1 output argument we no longer return
  a tuple but return the output value directly (again only if the method has
  'void' as its return type).

  This is a backward incompatible change, but there are not many of such
  methods.

- Another backward incompatible change is a minor cleanup of the names in
  the ``objc`` module. The most significant of these is the change from
  ``recycle_autorelease_pool`` to ``recycleAutoreleasePool``. The other
  changed names are internal to the bridge and should not be used in other
  code.

- The interface of Foundation.NSFillRects changed, it now has an interface
  that is consistent with the rest of the bridge.

Version 1.0b1 (2003-07-05)
--------------------------

- More tutorials

  Two new tutorials were added: 'Adding Python code to an existing ObjC
  application' and 'Understanding existing PyObjC examples'. The former
  explains how you can use Python to add new functionality to an already
  existing Objective-C application, the latter explains how to understand
  PyObjC programs written by other people.

- More examples

  Three examples were added: DotView, ClassBrowser and PythonBrowser,
  respectively showing the use of a custom NSView, NSBrowser and
  NSOutlineView.  PythonBrowser is reusable, making it trivial to add an
  object browser to your application.

- Support for MacOS X 10.1

  It is now possible to build PyObjC on MacOS X 10.1, with full access to
  the Cocoa API's on that platform.

  Note: The port to MacOS X 10.1 is not as well supported as the 10.2 port.
  The developers do not have full-time access to a MacOS X 10.1 system.

- Support for the WebKit framework, included with Safari 1.0.

  If you build PyObjC from source you will have to build on a system that has
  the WebKit SDK installed to make use of this. Note that the additional
  functionality will only be usable on systems that have Safari 1.0 installed,
  however as long as you don't use the additional functionality it is safe
  to run a 'WebKit-enabled' PyObjC on systems without Safari 1.0.

- It is no longer necessary to specify which protocols are implemented by

  a class, this information is automatically deduced from the list of implemented
  methods. You'll still a runtime error if you implement some methods of a
  protocol and one of the unimplemented methods is required.

- Support for "toll-free bridging" of Carbon.CF types to Objective-C objects.

  It is now possible to use instances of Carbon.CF types in places where
  Objective-C objects are expected. And to explicitly convert between the two.

  Note: this requires Python 2.3.

- Better integration with MacPython 2.3:

  * ``NSMovie.initWithMovie_`` and ``NSMovie.QTMovie`` now use ``QT.Movie``
    objects instead of generic pointer wrappers.

  * ``NSWindow.initWithWindowRef_`` and ``Window.windowRef`` now use
    ``Carbon.Window`` objects instead of generic pointer wrappers.

  * Methods returning CoreFoundation objects will return MacPython objects,
    and likewise, methods with CoreFoundation arguments will accept MacPython
    objects.

- It is now possible to write plugin bundles, such as preference panes for
  use in System Preferences, in Python. See Examples/PrefPanes for an example
  of this feature.

- The methods ``pyobjcPopPool`` and ``pyobjcPushPool`` of ``NSAutoreleasePool``
  are deprecated. These were introduced when PyObjC did not yet support the
  usual method for creating autorelease pools and are no longer necessary.

- Improved unittests, greatly increasing the confidence in the correctness
  of the bridge.

- All support for non-FFI builds has been removed.

- Object state is completely stored in the Objective-C object.  This has no
  user-visible effects, but makes the implementation a lot easier to
  comprehend and maintain.

- As part of the previous item we also fixed a bug that allowed addition of
  attributes to Objective-C objects. This was never the intention and had
  very odd semantics. Pure Objective-C objects not longer have a __dict__.

- Weakrefs are no longer used in the implementation of the bridge. Because
  the weakrefs to proxy objects isn't very useful the entire feature has
  been removed: It is no longer possible to create weakrefs to Objective-C
  objects.

  NOTE: You could create weakrefs in previous versions, but those would
  expire as soon as the last reference from Python died, *not* when the
  Objective-C object died, therefore code that uses weakrefs to Objective-C
  objects is almost certainly incorrect.

- Added support for custom conversion for pointer types. The end result is that
  we support more Cocoa APIs without special mappings.

- The generator scripts are automatically called when building PyObjC. This
  should make it easier to support multiple versions of MacOS X.


Version 0.9 (May-02-2003)
-------------------------

- This version includes numerous bugfixes and improvements.

- The module AppKit.NibClassBuilder has been moved to the package
  PyObjCTools.

- Usage of libFFI (https://sourceware.org/libffi/) is now mandatory. The
  setup.py gives the impression that it isn't, but we do *not* support
  non-FFI builds.

- We actually have some documentation, more will be added in future releases.

- There are more Project Builder templates (see 'Project Templates').

- The InterfaceBuilder, PreferencePanes and ScreenSaver frameworks have been
  wrapped.

- Management of reference counts is now completely automatic, it is no longer
  necessary to manually compensate for the higher reference count of objects
  returned by the alloc, copy and copyWithZone: class methods.

- Various function and keyword arguments have been renamed for a better
  integration with Cocoa. A partial list is of the changed names is::

    objc.lookup_class -> objc.lookUpClass
    objc.selector arguments/attributes:
        is_initializer -> isInitializer
        is_allocator -> isAlloc
        donates_ref -> doesDonateReference
        is_required -> isRequired
        class_method -> isClassMethod
        defining_class -> definingClass
        returns_self -> returnsSelf
        argument_types -> argumentTypes
        return_type -> returnType
    objc.get_class_list -> objc.getClassList

- On Python 2.2, objc.YES and objc.NO are instances of a private boolean type,
  on Python 2.3 these are instances of the builtin type bool.

- Because we now use libFFI a large amount of code could be disabled. The
  binaries are therefore much smaller, while we can now forward messages with
  arbitrary signatures (not limited to those we thought of while generating
  the static proxies that were used in 0.8)

- Better support for APIs that use byte arrays are arguments or return values.
  Specifically, the developer can now manipulate bitmaps directly via the
  NSBitmapImageRep class, work with binary data through the NSData class, and
  very quickly draw points and rects via NSRectFillList()

- We added a subclass of unicode that is used to proxy NSString values. This
  makes it easily possible to use NSString values with Python APIs, while at
  the same time allowing access to the full power of NSString.

Version 0.8 (Dec-10-2002)
-------------------------

- GNUStep support has been removed for lack of support.  Volunteers
  needed.

- Subclassing Objective-C classes from Python, including the addition
  of instance variables (like 'IBOutlet's)

- Generic support for pass-by-reference arguments

- More complete Cocoa package, including wrappers for a number of
  C functions, enumerated types, and globals.

- More example code

- Objective-C mappings and sequences can be accessed using the normal
  python methods for accessing mappings and sequences (e.g. subscripting
  works as expected)

- Documentation: See the directory 'docs'

- Can build standalone Cocoa applications based entirely on Python
  without requiring that user installs anything extra (requires 10.2).

- Better packaging and wrapper construction tools (borrowed from
  MacPython).

- An installer package.

- Support for Project Builder based Cocoa-Python projects.

- Unit tests.

Version 2002-01-30 (January 30, 2002)
-------------------------------------

- Version bumped to 0.6.1 ( __version__ is now a PyString )

- Will now build for Python 2.2

- added Cocoa package with Foundation.py and AppKit.py wrappers.

- HelloWorld.py in Examples

- builds with -g flag for debugging. -v option will dump log
  of message sends to /tmp file.

- Fixed one major runtime bug: added ISCLASS test before isKindOfClass -
  without check, it crashes on sends to abstract classes like NSProxy.

- There are still problems with Delegates and Notifications.

Version 2001-03-17 (March 17, 2001)
-----------------------------------

- moved to using distutils setup.py (requires small patch to distutils
  that has been submitted against python 2.1b1)

Version 2000-11-14 (November 14, 2000)
--------------------------------------

- GNU_RUNTIME is likely completely broken

- Compiles on macOS Server (python 2.0)

- Compiles on macOS (python 2.0)

- Works as either a dynamically loadable module or statically built
  into a python executable

- Requires a modified makesetup to work [patches have been sent to
  SourceForge.net's Python project].

- Supports NSAutoReleasepool.

- Some pre-OSX stuff removed;  references to old APIs, etc... (but
  nowhere near clean)

Version 0.55, 18 August 1998
----------------------------

- Here again, supporting GNU_RUNTIME and GNUstep Base! On my new Linux
  box I can finally test the module against them: I installed the
  latest snapshot of gstep-core, that contains the base library
  too. Given a sane GNUstep env (GNUSTEP_XXX env vars), you should be
  able to build a static ObjC-ized interpreter by::

    o Adjusting Setup, commenting out NeXT definition and enabling GNU
      ones;
    o make -f Makefile.pre.in boot
    o make static

Version 0.54, 24 March 1998
---------------------------

- OC_Pasteboard.[hm], OC_Stream.[mh] and ObjCStreams.m are definitively gone.

- OC_PythonObject derives from NSProxy.

Version 0.53, 4 January 1998
----------------------------

- Tons of changes, retargeting the core functionality around the
  OpenSTEP API. This release basically matches the previous one
  in terms of functionalities, but is should be closer to GNUstep.

- OC_Streams and OC_Pasteboard aren't supported, I've not yet decided
  if they are needed anymore.

- Updated LittleButtonedWindow demo.

Version 0.47, 29 October 1996
-----------------------------

- Misc/Makefile.pre.in automatically sets TARGET to ``pyobjc``.

- ObjC.m split to ObjCObject.m ObjCMethod.m ObjCPointer.m
  ObjCRuntime.m.

- New (almost invisible) types: ObjCSequenceObject and
  ObjCMappingObject; this to implement sequence and mapping syntax
  (several mapping methods have stub implementation).

- OC_Pasteboard class is gone. Its functionalities are now in a
  category of Pasteboard/NSPasteboard.

- Better methods doc.

- PyArg_ParseTuple format strings contain arguments names.

- OC_Streams are mapped to ObjCStreams by pythonify_c_value and its
  counterpart.

Version 0.46, 18 October 1996
-----------------------------

- OC_Stream is now a subclass of NSData under Foundation.

- New Objective-C class: OC_Pasteboard. Use it instead of Pasteboard/
  NSPasteboard.

- New Objective-C class: OC_PythonBundle. Use it instead of NXBundle/NSBundle.
  The ShellText demo has been upgraded to use it, and now you can run it
  directly from the WorkSpace.

- OC_Python.[hm] aren't in the package anymore.

- Setup.in directives changed again, due to OC_Python.m dropping.

Version 0.45, 14 October 1996
-----------------------------

- Double syntax: to make it easier for us to test and choose the
  better candidate, the only one that will be present in the final 1.0
  release. Keeping both would result in a speed penalty.
- Revisited streams, in particular GNUstep support.

Version 0.44, 9 October 1996
----------------------------

- Integers are now accepted too where floats or doubles are expected.

- New method: ObjC.make_pointer (1) returns an ObjCPointer containing
  ``((void *) 1)``.

Version 0.43, 7 October 1996
----------------------------

- Completed ObjCStream implementation. There is now a new module, ObjCStreams
  which is automatically loaded by ObjC. You can access it as ObjC.streams.

- Manual split in three parts: libPyObjC.tex with the chapter intro,
  libObjC.tex describing the main module, libObjCStreams.tex explains the
  stream facilities.

Version 0.42, 4 October 1996
----------------------------

- You can pass initialization arguments when using the ``Class()`` syntax. You
  select the right initializer selector with the ``init`` keyword parameter.

- First cut on ObjCStream objects. Thanx to Bill Bumgarner for motivations.

- New demo ShellText, to test above points.

Version 0.41, 2 October 1996
----------------------------

- Revised error messages: for arguments type mismatch they show the ObjC type
  expected.

- When a method returns a pointer to something, it gets translated as an
  ObjCPointer object, not the pythonified pointed value. When a method
  expects a pointer argument, it accepts such an object as well.

- New demo: Fred. To halt it, suspend the Python process with ^Z then kill
  it ;-).

- Setup.in directives changed. See the new file Modules/Setup.PyObjC.in

- Distributed as a standalone package. Special thanks to Bill Bumgarner.

Version 0.4, 27 September 1996
------------------------------

- Now handles methods returning doubles or floats.

- ObjCRuntime responds to .sel_is_mapped().

Version 0.31, 26 September 1996
-------------------------------

- It's now possible to use a different strategy to map ObjC method names to
  Python ones. Sooner or later we should decide the one to go, and drop the
  other. For details, see comments on PYTHONIFY_WITH_DOUBLE_UNDERSCORE in
  objc_support.h.
- Manual section.
- ObjC.runtime.__dict__ added.
- ObjC.runtime.kind added.

Version 0.3, 20 September 1996
------------------------------

- No user visible changes, just a little effort towards GNU_RUNTIME support.

Version 0.2, 16 September 1996
------------------------------

- Accepts a struct.pack() string for pointer arguments, but...

- ... New methods on ObjCMethod: .pack_argument and .unpack_argument:
  these should be used whenever an ObjC method expects a passed-by-reference
  argument; for example, on NeXTSTEP [View getFrame:] expects a pointer
  to an NXRect structure, that it will fill with the current frame of the
  view: in this case you should use something similar to::

        framep = aView.getFrame__.pack_argument (0)
        aView.getFrame__ (framep)
        frame = aView.getFrame__.unpack_argument (0, framep)

Version 0.1, 13 September 1996
------------------------------

- Correctly handle pointer arguments.

- New syntax to get a class: ObjC.runtime.NameOfClass

- New syntax aliasing .new(): SomeClass()

- New Demo: LittleButtonedWindow, that tests points above.

- What follow is the recipe to get PyObjC dynamically loadable on NeXTSTEP:

  * apply the patch in Misc/INSTALL.PyObjC to Python/importdl.c

  * modify Python/Makefile adding the switch ``-ObjC`` to the importdl.o
    build rule::

      importdl.o:   importdl.c
        $(CC) -ObjC -c $(CFLAGS) -I$(DLINCLDIR) $(srcdir)/importdl.c

  * modify Modules/Setup moving the PyObjC entry suggested above AFTER
    ``*shared*``, and remove ``-u libNeXT_s -lNeXT_s`` from it.

  * run ``make``: this will update various files, in particular
    Modules/Makefile.

  * modify Modules/Makefile adding ``-u libNeXT_s -lNeXT_s`` to SYSLIBS::

       SYSLIBS=      $(LIBM) $(LIBC) -u libNeXT_s -lNeXT_s

  * run ``make`` again
