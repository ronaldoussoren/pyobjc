Assuming you have:

mkdir -p ~/Library/Application\ Support/Developer/Shared/Xcode/Project\ Templates/AA\ Testing

This will populate it with the templates in this directory, ready to be used from Xcode:

project-tool.py -k -v --template Cocoa-Python\ Application/CocoaApp.xcodeproj/TemplateInfo.plist \
    Cocoa-Python\ Application \
    ~/Library/Application\ Support/Developer/Shared/Xcode/Project\ Templates/AA\ Testing/Cocoa-Python\ Application

project-tool.py -k -v --template Cocoa-Python\ Document-based\ Application/CocoaDocApp.xcodeproj/TemplateInfo.plist \
    Cocoa-Python\ Document-based\ Application/ \
    ~/Library/Application\ Support/Developer/Shared/Xcode/Project\ Templates/AA\ Testing/Cocoa-Python\ Document-based\ Application

project-tool.py -k -v --template Cocoa-Python\ Core\ Data\ Application/CocoaApp.xcodeproj/TemplateInfo.plist \
    Cocoa-Python\ Core\ Data\ Application/ \
    ~/Library/Application\ Support/Developer/Shared/Xcode/Project\ Templates/AA\ Testing/Cocoa-Python\ Core\ Data\ Application

project-tool.py -k -v --template Cocoa-Python\ Core\ Data\ Document-based\ Application/CocoaDocApp.xcodeproj/TemplateInfo.plist \
    Cocoa-Python\ Core\ Data\ Document-based\ Application/ \
    ~/Library/Application\ Support/Developer/Shared/Xcode/Project\ Templates/AA\ Testing/Cocoa-Python\ Core\ Data\ Document-based\ Application

To copy a template from the Xcode distro and turn it into a working project:

project-tool.py -r -w -k /Developer/Library/Xcode/Project\ Templates/Application/Core\ Data\ Application \
    Cocoa-Python\ Core\ Data\ Application

(You will need to manually rename a handful of files after the copy, most likely.  Xcode will show the ones that need to be renamed in red -- rename the files to the name as shown in Xcode.)
