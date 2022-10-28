import platform
import os
import sys
import re
from os import walk
from pathlib import Path

ostype = "Darwin"
f = []

def checkplatform():
    #so the switch case will work
    ostype = platform.system()
    print(ostype)
    
def replace_characters(current_string):
    #replaces any " " or _ with -, lowercases, and eliminates special chars
    result = re.sub('[^0-9a-zA-Z]+', '', current_string.replace(" ","-").replace("_","-").lower())
    return result

def get_dir(trydir):
    try:
        if ostype=="Darwin":
            if (os.path.isfile(trydir)):
                trydir = Path(trydir).parent
            
            for filename in os.listdir(trydir):
                print("inside")
                
                f = os.path.join(trydir, filename)
                print("inside")
                
                # checking if it is a file
                if os.path.isfile(f):
                    print("inside")
                    
                    
                    print("\n")
                    
                    #split the name
                    name_parts = filename.__str__().split(".",-1)
                    print(name_parts)
                    
                    #get the extension
                    extension_type = name_parts.pop()
                    
                    #reconsittute name, if there were any periods
                    name = "".join(name_parts)
                    
                    #replace the characters
                    newname = replace_characters(name)
                    
                    #print what the result is
                    print(trydir.__str__()+"/"+newname+"."+extension_type)
                    
                    #rename
                    os.rename(f, trydir.__str__()+"/"+newname+"."+extension_type)
    except:
        print("That didn't work, please retry")
        request_dir()

def request_dir():
    trydir = input("What's the directory? ")
    get_dir(trydir)
    
def testcase():
    get_dir("/Users/iankoratsky/Desktop")
        
def main():
    checkplatform()
    request_dir()

#main()
testcase()