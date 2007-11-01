import os
import sys
import wxglade
import common
import webbrowser
import main
common.wxglade_path = os.getcwd()

# fix bug in show_tutorial
def show_tutorial(self, event):
    webbrowser.open_new('file://'+os.path.join(common.wxglade_path, 'docs', 'index.html'))

main.wxGladeFrame.show_tutorial = show_tutorial

if len(sys.argv) == 1:
    main.main()
else:
    options, args = wxglade.parse_command_line()
    if not options:
        filename = wxglade._fix_path(args[0])
        main.main(filename)
    else:
        wxglade.command_line_code_generation(options, args)
