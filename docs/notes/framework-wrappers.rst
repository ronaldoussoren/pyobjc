Overview of macOS frameworks and their wrappers
===============================================

The table below lists all frameworks found within ``/System/Library/Frameworks`` on macOS and what the
name of the Python packages are for their wrappers. The table lists "-" as the name of the Python package when
the framework is not wrapped, see the column with notes for more information.

The framework name links to API notes for that framework, the python packages link to their PyPI page.

.. list-table::
   :class: sphinx-datatable
   :header-rows: 1

   * - Framework name
     - :iconify:`devicon:pypi` Python Package
     - Notes

   * - :doc:`dispatch </apinotes/libdispatch>`
     -  :pypi:`pyobjc-framework-libdispatch`
     -

   * - :doc:`AccessoryAccess </apinotes/AccessoryAccess>`
     - :pypi:`pyobjc-framework-AccessoryAccess`
     -

   * - :doc:`Accessibility </apinotes/Accessibility>`
     - :pypi:`pyobjc-framework-Accessibility`
     -

   * - AccessorySetupKit
     -
     - No public API on macOS.

   * - Accelerate
     -
     - Will not be wrapped.

   * - :doc:`Accounts </apinotes/Accounts>`
     - :pypi:`pyobjc-framework-Accounts`
     -

   * - ActivityKit
     -
     - No public API on macOS, :iconify:`devicon:swift` Swift-only.

   * - :doc:`AddressBook </apinotes/AddressBook>`
     - :pypi:`pyobjc-framework-AddressBook`
     -

   * - :doc:`AdServices </apinotes/AdServices>`
     - :pypi:`pyobjc-framework-AdServices`
     -

   * - :doc:`AdSupport </apinotes/AdSupport>`
     - :pypi:`pyobjc-framework-AdSupport`
     -

   * - AGL
     -
     - Will not be wrapped.

       .. macosdeprecated::  macOS 10.14.

   * - AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - AppIntentsTypeSupport
     -
     - No public API.

   * - :doc:`AppKit </apinotes/AppKit>`
     -  :pypi:`pyobjc-framework-Cocoa`
     -

   * - AppleShareClientCore
     -
     -  No public API

   * - :doc:`AppTrackingTransparency </apinotes/AppTrackingTransparency>`
     - :pypi:`pyobjc-framework-AppTrackingTransparency`
     -

   * - AppKitScripting
     -
     - Not wrapped, all definitions are available through the AppKit bindings.

       .. macosremoved: 10.15

   * - :doc:`AppleScriptKit </apinotes/AppleScriptKit>`
     - :pypi:`pyobjc-framework-AppleScriptKit`
     -

   * - :doc:`AppleScriptObjC </apinotes/AppleScriptObjC>`
     - :pypi:`pyobjc-framework-AppleScriptObjC`
     -

   * - :doc:`ApplicationServices </apinotes/ApplicationServices>`
     - :pypi:`pyobjc-framework-ApplicationServices`
     -

   * - AppSSO
     -
     - No public API.

   * - :doc:`ARKit </apinotes/ARKit>`
     - :pypi:`pyobjc-framework-ARKit`
     -

   * - AudioAccessoryKit
     -
     - :iconify:`devicon:swift` Swift-only framework

   * - AudioToolbox
     -
     -

   * - AudioUnit
     -
     -

   * - :doc:`AudioVideoBridging </apinotes/AudioVideoBridging>`
     - :pypi:`pyobjc-framework-AudioVideoBridging`
     -

   * - :doc:`AuthenticationServices </apinotes/AuthenticationServices>`
     - :pypi:`pyobjc-framework-AuthenticationServices`
     -

   * - :doc:`Automator </apinotes/Automator>`
     - :pypi:`pyobjc-framework-Automator`
     -

   * - :doc:`AutomaticAssessmentConfiguration </apinotes/AutomaticAssessmentConfiguration>`
     - :pypi:`pyobjc-framework-AutomaticAssessmentConfiguration`
     -

   * - :doc:`AVFoundation </apinotes/AVFoundation>`
     - :pypi:`pyobjc-framework-AVFoundation`
     -

   * - AVFAudio
     - :pypi:`pyobjc-framework-AVFoundation`
     - Use ``import AVFoundation`` to use these APIs.

       .. macosadded:: 11.3

   * - :doc:`AVKit </apinotes/AVKit>`
     - :pypi:`pyobjc-framework-AVKit`
     -

   * - :doc:`AVRouting </apinotes/AVRouting>`
     - :pypi:`pyobjc-framework-AVRouting`
     -

   * - :doc:`BackgroundAssets </apinotes/BackgroundAssets>`
     - :pypi:`pyobjc-framework-BackgroundAssets`
     -

   * - BackgroundTasks
     -
     - No public API on macOS

   * - BrowserEngineCore
     -
     - Very low-level API, will not be wrapped

   * - :doc:`BrowserEngineKit  </apinotes/BrowserEngineKit>`
     - :pypi:'pyobjc-framework-BrowserEgineKit`
     -

   * - :doc:`BusinessChat </apinotes/BusinessChat>`
     - :pypi:`pyobjc-framework-BusinessChat`
     -

   * - ByteMatrixVerification
     -
     - No public API on macOS

   * - :doc:`CalendarStore </apinotes/CalendarStore>`
     - :pypi:`pyobjc-framework-CalendarStore`
     -

   * - :doc:`CallKit </apinotes/CallKit>`
     - :pypi:`pyobjc-framework-CallKit`
     -

   * - CarKey
     -
     - No public API on macOS

   * - :doc:`Carbon </apinotes/Carbon>`
     - :pypi:`pyobjc-framework-Carbon`
     -

   * - :doc:`CFNetwork </apinotes/CFNetwork>`
     - :pypi:`pyobjc-framework-CFNetwork`
     -

   * - CrashReportExtension
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - Charts
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - CHIP
     -
     - Will not be wrapped.

       .. macosremoved:: 14

   * - :doc:`Cinematic </apinotes/Cinematic>`
     - :pypi:`pyobjc-framework-Cinematic`
     -

   * - :doc:`ClassKit </apinotes/ClassKit>`
     - :pypi:`pyobjc-framework-ClassKit`
     -

   * - ClassKitUI
     -
     - :iconify:`devicon:swift` Swift-only framework

   * - ClockKit
     -
     - No public API on macOS

   * - CLLogEntry
     -
     - No public API on macOS

   * - :doc:`CloudKit </apinotes/CloudKit>`
     - :pypi:`pyobjc-framework-CloudKit`
     -

   * - :doc:`Cocoa </apinotes/Cocoa>`
     - :pypi:`pyobjc-framework-Cocoa`
     -

   * - :doc:`Collaboration </apinotes/Collaboration>`
     - :pypi:`pyobjc-framework-Collaboration`
     -

   * - :doc:`ColorSync </apinotes/ColorSync>`
     - :pypi:`pyobjc-framework-ColorSync`
     -

   * - Combine
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`CompositorServices </apinotes/CompositorServices>`
     - :pypi:`pyobjc-framework-CompositorServices`
     -

   * - ComputeGraph
     -
     - No usable API.

   * - ContactProvider
     -
     - No public API

   * - :doc:`Contacts </apinotes/Contacts>`  `
     - :pypi:`pyobjc-framework-Contacts`
     -

   * - :doc:`ContactsUI </apinotes/ContactsUI>`
     - :pypi:`pyobjc-framework-ContactsUI`
     -

   * - ContextualActionsClient
     -
     - No functionality exposed.

   * - CoreAI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`CoreAudio </apinotes/CoreAudio>`
     - :pypi:`pyobjc-framework-CoreAudio`
     -

   * - :doc:`CoreAudioKit </apinotes/CoreAudioKit>`
     - :pypi:`pyobjc-framework-CoreAudioKit`
     -

   * - CoreAudioTypes
     - :pypi:`pyobjc-framework-CoreAudio`
     - These constants and types are exposed in the CoreAudio bindings. Use ``import CoreAudio``.

   * - CoreAuthentication
     -
     - No public API.

       .. macosremoved:: 10.13

   * - :doc:`CoreBluetooth </apinotes/CoreBluetooth>`
     - :pypi:`pyobjc-framework-CoreBluetooth`
     -

   * - :doc:`CoreData </apinotes/CoreData>`
     - :pypi:`pyobjc-framework-CoreData`
     -

   * - CoreDisplay
     -
     - No public API.

   * - :doc:`CoreFoundation </apinotes/CoreFoundation>`
     - :pypi:`pyobjc-framework-Cocoa`
     -

   * - :doc:`CoreGraphics </apinotes/CoreGraphics>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`CoreHaptics </apinotes/CoreHaptics>`
     - :pypi:`pyobjc-framework-CoreHaptics`
     -

   * - CoreHID
     -
     - No public API.

       .. macosremoved:: 14

   * - :doc:`CoreImage </apinotes/CoreImage>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`CoreLocation </apinotes/CoreLocation>`
     - :pypi:`pyobjc-framework-CoreLocation`
     -

   * - :doc:`CoreMedia </apinotes/CoreMedia>`
     - :pypi:`pyobjc-framework-CoreMedia`
     -

   * - :doc:`CoreMediaIO </apinotes/CoreMediaIO>`
     - :pypi:`pyobjc-framework-CoreMediaIO`
     -

   * - :doc:`CoreMIDI </apinotes/CoreMIDI>`
     - :pypi:`pyobjc-framework-CoreMIDI`
     -

   * - CoreMIDIServer
     -
     - No public API.

   * - :doc:`CoreML </apinotes/CoreML>`
     - :pypi:`pyobjc-framework-CoreML`
     -

   * - :doc:`CoreMotion </apinotes/CoreMotion>`
     - :pypi:`pyobjc-framework-CoreMotion`
     -

   * - :doc:`CoreServices </apinotes/CoreServices>`
     - :pypi:`pyobjc-framework-CoreServices`
     - Various subframeworks are wrapped

   * - :doc:`CoreServices/LauchServices </apinotes/LaunchServices>`
     - :pypi:`pyobjc-framework-LaunchServices`
     -

   * - :doc:`CoreServices/SharedFileList </apinotes/LaunchServices>`
     - :pypi:`pyobjc-framework-CoreServices`
     - Use ``import CoreServices``.

       ``import LaunchServices`` can be used when :pypi:`pyobjc-framework-LaunchServices`,
       is installed, but that's for backward compatibility only.

   * - :doc:`CoreServices/FSEvents </apinotes/FSEvents>`
     - :pypi:`pyobjc-framework-FSEvents`
     -

   * - CoreServices/AE
     -
     - Not wrapped, use the `appscript <https://appscript.sourceforge.io/>`_ package.

   * - :doc:`CoreServices/CarbonCore </apinotes/CarbonCore>`
     - :pypi:`pyobjc-framework-CoreServices`
     - Use ``import CoreServices``

   * - CoreServices/Metadata
     - :pypi:`pyobjc-framework-CoreServices`
     - Use ``import CoreServices``

   * - :doc:`CoreServices/OSServices </apinotes/OSServices>`
     - :pypi:`pyobjc-framework-CoreServices`
     - Use ``import CoreServices``

   * - :doc:`CoreSpotlight </apinotes/CoreSpotlight>`
     - :pypi:`pyobjc-framework-CoreSpotlight`
     -

   * - CoreTelephony
     -
     - Framework has no public API on macOS

   * - CoreTransferable
     -
     - Framework has no public API on macOS

   * - :doc:`CoreText </apinotes/CoreText>`
     - :pypi:`pyobjc-framework-CoreText`
     -

   * - :doc:`CoreVideo </apinotes/CoreVideo>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - CoreWiFi
     -
     - Framework has no public API

   * - :doc:`CoreWLAN </apinotes/CoreWLAN>`
     - :pypi:`pyobjc-framework-CoreWLAN`
     -

   * - CoreXR
     -
     - No public API.

   * - CreateML
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - CreateMLComponents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - CryptoKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`CryptoTokenKit </apinotes/CryptoTokenKit>`
     - :pypi:`pyobjc-framework-CryptoTokenKit`
     -

   * - :doc:`DataDetection </apinotes/DataDetection>`
     - :pypi:`pyobjc-framework-DataDetection`
     -

   * - DeclaredAgeRange
     -
     -

   * - DeveloperToolsSupport
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - DeviceActivity
     -
     - No public API.

   * - DeviceAccess
     -
     - No public API.

   * - :doc:`DeviceCheck </apinotes/DeviceCheck>`
     - :pypi:`pyobjc-framework-DeviceCheck`
     -

   * - :doc:`DeviceDiscoveryExtension </apinotes/DeviceDiscoveryExtension>`
     - :pypi:`pyobjc-framework-DeviceDiscoveryExtension`
     -

   * - DirectoryService
     -
     - Will not be wrapped, deprecated framework.

   * - :doc:`DiscRecording </apinotes/DiscRecording>`
     - :pypi:`pyobjc-framework-DiscRecording`
     -

   * - :doc:`DiscRecordingUI </apinotes/DiscRecording>`
     - :pypi:`pyobjc-framework-DiscRecording`
     -

   * - :doc:`DiskArbitration </apinotes/DiskArbitration>`
     - :pypi:`pyobjc-framework-DiskArbitration`
     -
   * - DiskImageKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - DockKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - DriverKit
     -
     - Will not be wrapped, too low level.

   * - DVComponentGlue
     -
     - No public API.

       .. macosremoved:: 10.15

   * - :doc:`DVDPlayback </apinotes/DVDPlayback>`
     - :pypi:`pyobjc-framework-DVDPlayback`
     -

   * - DrawSprocket
     -
     - Will not be wrapped.

       .. macosremoved:: 10.15

   * - :doc:`EventKit </apinotes/EventKit>`
     - :pypi:`pyobjc-framework-EventKit`
     -

   * - :doc:`ExceptionHandling </apinotes/ExceptionHandling>`
     - :pypi:`pyobjc-framework-ExceptionHandling`
     -

   * - ExposureNotification
     -
     - No public API on macOS.

   * - ExtensionFoundation
     -
     - No public API on macOS.

   * - :doc:`ExecutionPolicy </apinotes/ExecutionPolicy>`
     - :pypi:`pyobjc-framework-ExecutionPolicy`
     -

   * - :doc:`ExtensionKit </apinotes/ExtensionKit>`
     - :pypi:`pyobjc-framework-ExtensionKit`
     -

   * - :doc:`ExternalAccessory </apinotes/ExternalAccessory>`
     - :pypi:`pyobjc-framework-ExternalAccessory`
     -

   * - FamilyControls
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`FileProvider </apinotes/FileProvider>`
     - :pypi:`pyobjc-framework-FileProvider`
     -

   * - :doc:`FileProviderUI </apinotes/FileProviderUI>`
     - :pypi:`pyobjc-framework-FileProviderUI`
     -

   * - FinanceKit
     -
     - No public API.

   * - FinanceKitUI
     -
     - No public API.

   * - :doc:`FinderSync </apinotes/FinderSync>`
     - :pypi:`pyobjc-framework-FinderSync`
     -

   * - ForceFeedback
     -
     - Will not be wrapped, low-level API

   * - :doc:`Foundation </apinotes/Foundation>`
     - :pypi:`pyobjc-framework-Cocoa`
     -

   * - FoundationModels
     -
     -

   * - :doc:`FSKit </apinotes/FSKit>`
     - :pypi:`pyobjc-framework-FSKit`
     -

   * - FWAUserLib
     -
     - Will not be wrapped.

       .. macosdeprecated:: 10.12

       .. macosremoved:: 13

   * - :doc:`GameController </apinotes/GameController>`
     - :pypi:`pyobjc-framework-GameController`
     -

   * - :doc:`GameCenter </apinotes/GameCenter>`
     - :pypi:`pyobjc-framework-GameCenter`
     -

       .. macosremoved:: 10.13

   * - :doc:`GameKit </apinotes/GameKit>`
     - :pypi:`pyobjc-framework-GameKit`
     -

   * - :doc:`GameplayKit </apinotes/GameplayKit>`
     - :pypi:`pyobjc-framework-GameplayKit`
     -

   * - GameSave
     - :pypi:`pyobjc-framework-GameSave`
     -
        .. macosadded:: 25

   * - GeoToolbox
     -
     -

   * - GLKit
     -
     - Will not be wrapped.

       .. macosdeprecated:: 10.14

   * - GLUT
     -
     - Will not be wrapped. Use :pypi:`PyOpenGL` instead.

   * - GroupActivities
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - GSS
     -
     - Will not be wrapped. Use :pypi:`gssapi` instead.

   * - :doc:`HealthKit </apinotes/HealthKit>`
     - :pypi:`pyobjc-framework-HealthKit`
     -

   * - HIDDriverKit
     -
     - Will not be wrapped, too low level.

   * - :doc:`HomeKit </apinotes/HomeKit>`
     -
     - Framework can only be used in Catalist (iOS-on-mac) applications.

   * - Hypervisor
     -
     - Will not be wrapped, too low level. The framework :doc:`Virtualization </apinotes/Virtualization>`
       is a high-level interface for using virtual machines.

   * - ICADevices
     -
     - Will not be wrapped.

   * - IdentityDocumentServices
     -
     -

   * - IdentityDocumentServicesUI
     -
     -

   * - IdentityLookup
     -
     - No public API on macOS.

   * - :doc:`ImageCaptureCore </apinotes/ImageCaptureCore>`
     - :pypi:`pyobjc-framework-ImageCaptureCore`
     -

   * - :doc:`ImageIO </apinotes/ImageIO>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - ImagePlayground
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - IMCore
     -
     - No public API.

       .. macosremoved:: 10.13

   * - ImmersiveMediaSupport
     -
     -

   * - IMServicePlugIn
     -
     - Will not be wrapped.

       .. version-removed:: 10

       .. macosremoved: 14

   * - IncomingCallNotifications
     -
     - No public API on macOS.

       .. macosremoved:: 10.15

   * - :doc:`InputMethodKit </apinotes/InputMethodKit>`
     - :pypi:`pyobjc-framework-InputMethodKit`
     -

   * - :doc:`InstallerPlugins </apinotes/InstallerPlugins>`
     - :pypi:`pyobjc-framework-InstallerPlugins`
     -

   * - :doc:`InstantMessage </apinotes/InstantMessage>`
     - :pypi:`pyobjc-framework-InstantMessage`
     -

   * - :doc:`Intents </apinotes/Intents>`
     - :pypi:`pyobjc-framework-Intents`
     -

   * - :doc:`IntentsUI </apinotes/IntentsUI>`
     - :pypi:`pyobjc-framework-IntentsUI`
     -

   * - :doc:`IOBluetooth </apinotes/IOBluetooth>`
     - :pypi:`pyobjc-framework-IOBluetooth`
     -

   * - :doc:`IOBluetoothUI </apinotes/IOBluetoothUI>`
     - :pypi:`pyobjc-framework-IOBluetoothUI`
     -

   * - IOKit
     -
     - Will not be wrapped.

   * - :doc:`IOSurface </apinotes/IOSurface>`
     - :pypi:`pyobjc-framework-IOSurface`
     -

   * - IOUSBHost
     -
     - Will not be wrapped.

   * - :doc:`iTunesLibrary </apinotes/iTunesLibrary>`
     - :pypi:`pyobjc-framework-iTunesLibrary`
     -

   * - :doc:`JavaScriptCore </apinotes/JavaScriptCore>`
     - :pypi:`pyobjc-framework-WebKit`
     -

   * - JavaFrameEmbedding
     -
     - Will not be wrapped.

   * - JavaNativeFoundation
     -
     - Will not be wrapped.

   * - JavaRuntimeSupport
     -
     - Will not be wrapped.

   * - JavaVM
     -
     - Will not be wrapped.

   * - Kerberos
     -
     - Will not be wrapped.

   * - Kernel
     -
     - Will not be wrapped.

   * - :doc:`KernelManagement </apinotes/KernelManagement>`
     - :pypi:`pyobjc-framework-KernelManagement`
     -

   * - :doc:`LatentSemanticMapping </apinotes/LatentSemanticMapping>`
     - :pypi:`pyobjc-framework-LatentSemanticMapping`
     -

   * - LDAP
     -
     - Will not be wrapped.  Use :pypi:`python-ldap` instead.

   * - LightweightCodeRequirements
     -
     - No public API.

   * - :doc:`LinkPresentation </apinotes/LinkPresentation>`
     - :pypi:`pyobjc-framework-LinkPresentation`
     -

   * - :doc:`LinkSecurity </apinotes/LinkSecurity>`
     - :pypi:`pyobjc-framework-LinkSecurity`
     -

   * - LiveCommunicationKit
     -
     -

   * - :doc:`LocalAuthentication </apinotes/LocalAuthentication>`
     - :pypi:`pyobjc-framework-LocalAuthentication`
     -

   * - :doc:`LocalAuthenticationEmbeddedUI </apinotes/LocalAuthenticationEmbeddedUI>`
     - :pypi:`pyobjc-framework-LocalAuthenticationEmbeddedUI`
     -

   * - ManagedSettings
     -
     - No public API on macOS.

   * - ManagedAppDistribution
     -
     - No public API on macOS.

   * - :doc:`MapKit </apinotes/MapKit>`
     - :pypi:`pyobjc-framework-MapKit`
     -

   * - :doc:`MailKit </apinotes/MailKit>`
     - :pypi:`pyobjc-framework-MailKit`
     -

   * - ManagedApp
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - Matter
     -
     - Not wrapped yet.

   * - MatterSupport
     -
     - No public API.

   * - :doc:`MediaAccessibility </apinotes/MediaAccessibility>`
     - :pypi:`pyobjc-framework-MediaAccessibility`
     -

   * - :doc:`MediaExtension </apinotes/MediaExtension>`
     - :pypi:`pyobjc-framework-MediaExtension`
     -

   * - MediaIntelligence
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - MediaIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`MediaLibrary </apinotes/MediaLibrary>`
     - :pypi:`pyobjc-framework-MediaLibrary`
     -

   * - :doc:`MediaPlayer </apinotes/MediaPlayer>`
     - :pypi:`pyobjc-framework-MediaPlayer`
     -

   * - :doc:`MediaToolbox </apinotes/MediaToolbox>`
     - :pypi:`pyobjc-framework-MediaToolbox`
     -

   * - MeshNetFramework
     -
     -

   * - Message
     -
     - No longer available.

   * - :doc:`Metal </apinotes/Metal>`
     - :pypi:`pyobjc-framework-Metal`
     -

   * - :doc:`MetalFX </apinotes/MetalFX>`
     - :pypi:`pyobjc-framework-MetalFX`
     -

   * - :doc:`MetalKit </apinotes/MetalKit>`
     - :pypi:`pyobjc-framework-MetalKit`
     -

   * - MetalPerformancePrimitives
     -
     - Low-level C++ API

   * - :doc:`MetalPerformanceShaders </apinotes/MetalPerformanceShaders>`
     - :pypi:`pyobjc-framework-MetalPerformanceShaders`
     -

   * - :doc:`MetalPerformanceShadersGraph </apinotes/MetalPerformanceShadersGraph>`
     - :pypi:`pyobjc-framework-MetalPerformanceShadersGraph`
     -

   * - :doc:`MetricKit </apinotes/MetricKit>`
     - :pypi:`pyobjc-framework-MetricKit`
     -

   * - :doc:`MLCompute </apinotes/MLCompute>`
     - :pypi:`pyobjc-framework-MLCompute`
     -

   * - :doc:`ModelIO </apinotes/ModelIO>`
     - :pypi:`pyobjc-framework-ModelIO`
     -

   * - MorphunAssetsUpdater
     -
     - No public API.

   * - :doc:`MultipeerConnectivity </apinotes/MultipeerConnectivity>`
     - :pypi:`pyobjc-framework-MultipeerConnectivity`
     -

   * - MusicKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - MusicUnderstanding
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`NaturalLanguage </apinotes/NaturalLanguage>`
     - :pypi:`pyobjc-framework-NaturalLanguage`
     -

   * - :doc:`NetFS </apinotes/NetFS>`
     - :pypi:`pyobjc-framework-NetFS`
     -

   * - :doc:`Network </apinotes/Network>`
     - :pypi:`pyobjc-framework-Network`
     -

   * - :doc:`NetworkExtension </apinotes/NetworkExtension>`
     - :pypi:`pyobjc-framework-NetworkExtension`
     -

   * - NearbyInteraction
     -
     - No public API on macOS

   * - NetworkingDriverKit
     -
     - Will not be wrapped, too low level.

   * - :doc:`NotificationCenter </apinotes/NotificationCenter>`
     - :pypi:`pyobjc-framework-NotificationCenter`
     -

   * - NowPlaying
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - OpenAL
     -
     - Will not be wrapped,  use :pypi:`PyAL` instead.

        .. macosdeprecated:: 10.15

   * - OpenCL
     -
     - Will not be wrapped.  Use :pypi:`pyopencl` instead.

   * - :doc:`OpenDirectory </apinotes/OpenDirectory>`
     - :pypi:`pyobjc-framework-OpenDirectory`
     -

   * - OpenGL
     -
     - Will not be wrapped.  Use :pypi:`PyOpenGL` instead.

   * - :doc:`OSAKit </apinotes/OSAKit>`
     - :pypi:`pyobjc-framework-OSAKit`
     -

   * - OSAnalytics
     -
     - No public API on macOS

   * - :doc:`OSLog </apinotes/OSLog>`
     - :pypi:`pyobjc-framework-OSLog`
     -

   * - PaperKit
     -
     -

   * - ParavirtualizedGraphics
     -
     - Will not be wrapped.

   * - :doc:`PassKit </apinotes/PassKit>`
     - :pypi:`pyobjc-framework-PassKit`
     -

   * - PCIDriverKit
     -
     - Will not be wrapped.

   * - PCSC
     -
     - Use :pypi:`pyscard` instead.

   * - :doc:`PDFKit </apinotes/PDFKit>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`PencilKit </apinotes/PencilKit>`
     - :pypi:`pyobjc-framework-PencilKit`
     -

   * - PermissionKit
     -
     -

   * - :doc:`PHASE </apinotes/PHASE>`
     - :pypi:`pyobjc-framework-PHASE`
     -

   * - :doc:`Photos </apinotes/Photos>`
     - :pypi:`pyobjc-framework-Photos`
     -

   * - :doc:`PhotosUI </apinotes/PhotosUI>`
     - :pypi:`pyobjc-framework-PhotosUI`
     -

   * - :doc:`PreferencePanes </apinotes/PreferencePanes>`
     - :pypi:`pyobjc-framework-PreferencePanes`
     -

   * - ProximityReaderStub
     -
     - No public API on macOS.

   * - :doc:`PubSub </apinotes/PubSub>`
     - :pypi:`pyobjc-framework-PubSub`
     - .. macosremoved:: 10.15

   * - :doc:`PushKit </apinotes/PushKit>`
     - :pypi:`pyobjc-framework-PushKit`
     -

   * - PushToTalk
     -
     - No public API on macOS.

   * - Python
     -
     - Will not be wrapped.

   * - QTKit
     -
     - .. version-removed:: 7

       .. macosremoved:: 10.15

   * - :doc:`Quartz </apinotes/Quartz>`
     - :pypi:`pyobjc-framework-Quartz`
     -

   * - Quartz / :doc:`ImageKit </apinotes/ImageKit>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - Quartz / :doc:`QuartzComposer </apinotes/QuartzComposer>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - Quartz / :doc:`QuartzFilters </apinotes/QuartzFilters>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - Quartz / :doc:`QuickLookUI </apinotes/QuickLookUI>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`QuartzCore </apinotes/QuartzCore>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`QuickLook </apinotes/QuickLook>`
     - :pypi:`pyobjc-framework-Quartz`
     - Use ``import Quartz`` to access these APIs.

   * - :doc:`QuickLookThumbnailing </apinotes/QuickLookThumbnailing>`
     - :pypi:`pyobjc-framework-QuickLookThumbnailing`
     -

   * - QuickTime
     -
     - Will not be wrapped.

       .. macosremoved:: 10.15

   * - RealityFoundation
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - RealityKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - RelevanceKit
     -
     - No public API on macOS

   * - :doc:`ReplayKit </apinotes/ReplayKit>`
     - :pypi:`pyobjc-framework-ReplayKit`
     -

   * - Ruby
     -
     - Will not be wrapped, use Python

   * - RubyCocoa
     -
     - Will not be wrapped, use Python

   * - :doc:`SafetyKit </apinotes/SafetyKit>`
     - :pypi:`pyobjc-framework-SafetyKit`
     -

   * - :doc:`SafariServices </apinotes/SafariServices>`
     - :pypi:`pyobjc-framework-SafariServices`
     -

   * - :doc:`SceneKit </apinotes/SceneKit>`
     - :pypi:`pyobjc-framework-SceneKit`
     -

   * - :doc:`ScreenCaptureKit </apinotes/ScreenCaptureKit>`
     - :pypi:`pyobjc-framework-ScreenCaptureKit`
     -

   * - :doc:`ScreenSaver </apinotes/ScreenSaver>`
     - :pypi:`pyobjc-framework-ScreenSaver`
     -

   * - :doc:`ScreenTime </apinotes/ScreenTime>`
     - :pypi:`pyobjc-framework-ScreenTime`
     -

   * - Scripting
     -
     - This framework is (long) deprecated, use ``import Foundation`` instead.

       .. macosremoved:: 10.15

   * - :doc:`ScriptingBridge </apinotes/ScriptingBridge>`
     - :pypi:`pyobjc-framework-ScriptingBridge`
     -

   * - SecureConfigDB
     -
     - No public API on macOS. Use ``import Foundation`` instead.

   * - :doc:`Security </apinotes/Security>`
     - :pypi:`pyobjc-framework-Security`
     -

   * - :doc:`SecurityFoundation </apinotes/SecurityFoundation>`
     - :pypi:`pyobjc-framework-SecurityFoundation`
     -

   * - :doc:`SecurityInterface </apinotes/SecurityInterface>`
     - :pypi:`pyobjc-framework-SecurityInterface`
     -

   * - :doc:`SecurityUI </apinotes/SecurityUI>`
     - :pypi:`pyobjc-framework-SecurityUI`
     -

   * - :doc:`SensitiveContentAnalysis </apinotes/SensitiveContentAnalysis>`
     - :pypi:`pyobjc-framework-SensitiveContentAnalysis`
     -

   * - SiriAudioIntentUtils
     -
     - No public API on macOS.

   * - SensorKit
     -
     - No public API on macOS.

   * - ServiceExtensions
     -
     - No public API on macOS.

   * - ServiceExtensionsCore
     -
     - No public API on macOS.

   * - :doc:`ServiceManagement </apinotes/ServiceManagement>`
     - :pypi:`pyobjc-framework-ServiceManagement`
     -

   * - :doc:`SharedWithYouCore </apinotes/SharedWithYouCore>`
     - :pypi:`pyobjc-framework-SharedWithYouCore`
     -

   * - :doc:`SharedWithYou </apinotes/SharedWithYou>`
     - :pypi:`pyobjc-framework-SharedWithYou`
     -

   * - :doc:`ShazamKit </apinotes/ShazamKit>`
     - :pypi:`pyobjc-framework-ShazamKit`
     -

   * - :doc:`Social </apinotes/Social>`
     - :pypi:`pyobjc-framework-Social`
     -

   * - :doc:`SoundAnalysis </apinotes/SoundAnalysis>`
     - :pypi:`pyobjc-framework-SoundAnalysis`
     -

   * - SpatialPreview
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`Speech </apinotes/Speech>`
     - :pypi:`pyobjc-framework-Speech`
     -

   * - :doc:`SpriteKit </apinotes/SpriteKit>`
     - :pypi:`pyobjc-framework-SpriteKit`
     -

   * - :doc:`StateReporting </apinotes/StateReporting>`
     - :pypi:`pyobjc-framework-StateReporting`
     -

   * - StickerFoundation
     -
     - No public API on macOS.

   * - StickerKit
     -
     - No public API on macOS.

   * - :doc:`StoreKit </apinotes/StoreKit>`
     - :pypi:`pyobjc-framework-StoreKit`
     -

   * - SuggestedActions
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - SwiftData
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - SwiftUICore
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`SyncServices </apinotes/SyncServices>`
     - :pypi:`pyobjc-framework-SyncServices`
     -

   * - :doc:`Symbols </apinotes/Symbols>`
     - :pypi:`pyobjc-framework-Symbols`
     -

   * - System
     -
     - No public API.

   * - :doc:`SystemConfiguration </apinotes/SystemConfiguration>`
     - :pypi:`pyobjc-framework-SystemConfiguration`
     -

   * - :doc:`SystemExtensions </apinotes/SystemExtensions>`
     - :pypi:`pyobjc-framework-SystemExtensions`
     -

   * - TabularData
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - Tcl
     -
     - Will not be wrapped, use Python

   * - TelephonyMessagingKit
     -
     -

   * - TipKit
     -
     - No public API.

   * - Tk
     -
     - Will not be wrapped, use :mod:`tkinter`.

   * - :doc:`ThreadNetwork </apinotes/ThreadNetwork>`
     - :pypi:`pyobjc-framework-ThreadNetwork`
     -

   * - TipsNext
     -
     - No public API.

   * - Translation
     -
     - No public API.

   * - TWAIN
     -
     - Will not be wrapped. Use :doc:`ImageCaptureCore </apinotes/ImageCaptureCore>` instead.

   * - USBDriverKit
     -
     - Will not be wrapped, too low level.

   * - USDKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`UserNotifications </apinotes/UserNotifications>`
     - :pypi:`pyobjc-framework-UserNotifications`
     -

   * - :doc:`UserNotificationsUI </apinotes/UserNotificationsUI>`
     - :pypi:`pyobjc-framework-UserNotificationsUI`
     -

   * - :doc:`UniformTypeIdentifiers </apinotes/UniformTypeIdentifiers>`
     - :pypi:`pyobjc-framework-UniformTypeIdentifiers`
     -

   * - vecLib
     -
     - Will not be wrapped.

   * - VideoDecodeAcceleration
     -
     - Will not be wrapped.

       .. macosdeprecated:: 10.11

   * - :doc:`VideoSubscriberAccount </apinotes/VideoSubscriberAccount>`
     - :pypi:`pyobjc-framework-VideoSubscriberAccount`
     -

   * - :doc:`VideoToolbox </apinotes/VideoToolbox>`
     - :pypi:`pyobjc-framework-VideoToolbox`
     -

   * - :doc:`Virtualization </apinotes/Virtualization>`
     - :pypi:`pyobjc-framework-Virtualization`
     -

   * - VisualIntelligence
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`Vision </apinotes/Vision>`
     - :pypi:`pyobjc-framework-Vision`
     -

   * - VisionKit
     -
     - Only available in Catalist.       .

   * - vmnet
     -
     - Will not be wrapped, too low level.

   * - :doc:`WebKit </apinotes/WebKit>`
     - :pypi:`pyobjc-framework-WebKit`
     -

   * - WidgetKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - UIKit
     -
     - Not wrapped yet.

   * - WiFiAware
     -
     -

   * - WeatherKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - WorkoutKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - :doc:`xpc </apinotes/xpc>`
     - :pypi:`pyobjc-framework-libxpc`
     -

   * - _AppIntents_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _AppIntents_AppKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _AppIntents_HealthKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _ARKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _AuthenticationServices_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _AVKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _CompositorServices_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _Contacts_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _CoreData_CloudKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _CoreSpotlight_FoundationModels
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _DeviceActivity_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _FinanceKit_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _FoundationModels_AppKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _FoundationModels_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _GeoToolbox_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _GroupActivities_AppKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _Intents_TipKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _LinkPresentation_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _LocalAuthentication_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _LocationEssentials
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _ManagedAppDistribution_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.
   * - _MediaIntents_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _MediaPlayer_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _NowPlaying_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _PassKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _PermissionKit_AppKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _PermissionKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _PhotosUI_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _Photos_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _PhotosUI_WidgetKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _RealityKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _RealityKit_ComputeGraph
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _ScreenCaptureKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SharedWithYou_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SpatialPreview_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SpatialPreview_USDKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SpriteKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _StoreKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SceneKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SwiftData_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _QuickLook_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _MapKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _MusicKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SwiftData_CoreData
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _SwiftUICore
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _Translation_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _USDKit_RealityKit
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _UserNotifications_AppIntents
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _Vision_FoundationModels
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _WebKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.

   * - _WorkoutKit_SwiftUI
     -
     - :iconify:`devicon:swift` Swift-only framework.


Frameworks that are marked as "Will not be wrapped" will not be wrapped, mostly because these frameworks are not
useful for Python programmers. Frameworks that are marked with "Not wrapped yet" will be wrapped in some future
version of PyObjC although there is no explicit roadmap for this.

Frameworks that are marked as ":iconify:`devicon:swift` Swift-only framework" have a public API for Swift, but not for other languages. These
frameworks cannot be wrapped by PyObjC.

Please file an issue if you have a usecase for accessing one of the unwrapped frameworks from Python, this helps
prioritizing work.
