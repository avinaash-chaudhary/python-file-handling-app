from pathlib import Path
import os # Curd Operation


def createfile():
    try:
        name=input("Please tell your file name:- ")
        path=Path(name)
    
        if not path.exists():
            with open(path,"w") as file:
                data=input("what you want to write:- ")
                file.write(data)
            print("File Created Successfully!")
        else:
            print("File name Already Exists")
    except Exception as err:
        print(f"an error occured as {err}")  


def readfile():
    try:
        name=input("Please tell your file name:- ")
        path=Path(name)
        if path.exists():
            with open(path,"r") as file:
                content=file.read()
            print(f"Your file content is {content}")
        else:
            print("Error no sach a file exists")
    except Exception as err:
        print(f"an a error occured as {err}")
    
         
def updatefile():
    try:
        name=input("Please tell your file name:- ")
        path=Path(name)
        if path.exists:
            print("Operations")
            print("1. Rename the file")
            print("2. Appending the content")
            print("3. Overwriting the file")
            
            choice=int(input("Enter your options:- "))
            if choice==1:
                newname=input("Enter the new name of the file:- ")
                new_path=Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("Renamed Successfully")
                else:print("file already exists")      

            elif choice==2:
                with open(path,"a") as file:
                    data=input("What do you want to append:- ")
                    file.write("\n"+data)
                print("Sucessfully Appended")

            elif choice==3:
                with open(path,"w") as file:
                    data=input("what do you want to overwrite:- ")
                    file.write("\n"+data)
                print("Successfully Overwritten")

    except Exception as err:
        print(f"An error occured as {err}")
        
        
        
        
        
        
def deletefile():
    try:
        name=input("Please tell your file name:- ")
        path=Path(name)
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("Error no such a file exists")
    except Exception as err:
        print(f"An error occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 1 for updating a file")
print("press 1 for deleting a file")



a=int(input("\nTell your response:- "))
if a==1:
    createfile()
elif a==2:
    readfile()

elif a==3:
    updatefile()

elif a==4:
    deletefile()

else:
    print("Invalid option!")