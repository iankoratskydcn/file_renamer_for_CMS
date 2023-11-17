import os
import re
from pathlib import Path

    
def replace_characters(current_string):
    #replaces any " " or _ with -, lowercases, and eliminates special chars
    result = re.sub('[^0-9a-zA-Z-]+', '', current_string.replace(" ","-").replace("_","-").lower())
    return result

def get_dir(trydir,asktype):
    asktype=str(asktype)
    try:
        if (os.path.isfile(trydir)):
            trydir = Path(trydir).parent
        
        for _name in os.listdir(trydir):
            
            f = os.path.join(trydir, _name)

            if asktype=="1":
            
                # checking if it is a file
                if os.path.isfile(f):
                    #split the name
                    name_parts = _name.__str__().split(".",-1)
                    
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

            if asktype=="2":
                    # checking if it is a folder
                    if os.path.isdir(f):

                        # split name by periods and reconstitute
                        initialName = replace_characters("".join(_name.__str__().split(".",-1))+"_")
                        count = 0
                        #here we iterate the subfolders
                        for _name2 in os.listdir(f):


                            f2 = os.path.join(f, _name2)

                            

                            # checking if it is a file
                            if os.path.isfile(f2):

                                #split the name
                                name_parts = _name2.__str__().split(".",-1)
                                
                                #get the extension
                                extension_type = name_parts.pop()
                                
                                #create the new name
                                newname = initialName+count.__str__()+"."+extension_type
                                f3 = os.path.join(f, newname)
                                
                                #rename
                                os.rename(f2, f3)
                                count+=1
                            

    except:
        print("That didn't work, please retry")
        request_dir()

def request_dir():
    trydir = input("What's the directory? ")
    ask_type= input("Type? \n1. rename all in dir \n2. go to each subfolder and rename by folder and iterator\n")
    get_dir(trydir,ask_type)


        
def main():
    request_dir()

main()