# Skeleton Python source for embedding Python into ObjC programs.
import os
import sys

DEBUG = 0

def main():
    # First find the Resource folder of the current application
    resource_folder, ourname = os.path.split(__file__)
    if DEBUG:
        print "PythonGlue: resource folder:", resource_folder
    
    # Add this folder and the PyObjC subfolder to sys.path
    sys.path.append(resource_folder)
    sys.path.append(os.path.join(resource_folder, "PyObjC"))
    
    # Now import all modules from the resource folder
    count = 0
    for filename in os.listdir(resource_folder):
        if filename[-3:] == ".py" and filename != ourname:
            module_name = filename[:-3]
            if DEBUG:
                print "PythonGlue: import", module_name
            __import__(filename[:-3])
            count = count + 1
    if count == 0:
        print "PythonGlue: Warning: no Python modules found"
            
if __name__ == '__main__':
    main()
    