#THIS IS STILL VERY BASIC, IMPROVEMENTS WILL BE SURELY MADE
#this gives access to os module functions
import os
import datetime

starting_folder = r"C:\\" #this is a scanning function in the os module

for dirpath,dirnames,filenames in os.walk(starting_folder): #starting from the root, this helps the program transverse using the function os.walk
    for file_name in filenames: #checks for files in filenames
        if file_name.lower().endswith(".pdf"): 
            filepath = os.path.join(dirpath,file_name)#helps in joining path and name of the file and then outputs it
            print(filepath)

#the next 3 lines interacts with the user and asks for user choice
print("Enter file extension to search: ")
print("I can only scan for(.pdf,.docx,.zip,.mp4,.csv,.txt) files")
target_ext = input("Your choice: ").lower().strip()

if not target_ext.startswith("."):#this adds dot(.) if uuser forgets to add as file extension
    target_ext = "." + target_ext
else:
    target_ext = target_ext

start_folder = r"C:\\" ##this serves as root folder of where to start the scanning
print(f"Scanning {start_folder}")

for dirpath,dirnames,filenames in os.walk(start_folder):#allows to visit every folder and subfolder
    for file_name in filenames:
        if file_name.lower().endswith(target_ext):
            full_path = os.path.join(dirpath,file_name)
            print(full_path)


#saving the user scan into a file

print("Enter file extension to search: ")
print("I can only scan for(.pdf,.docx,.zip,.mp4,.csv,.txt) files")
target_ext =("Enter choice: ").lower().strip()

if not target_ext.startswith("."):#this adds dot(.) if uuser forgets to add as file extension
    target_ext = "." + target_ext
else:
    target_ext = target_ext

start_folder = r"C:\\"#this is the root folder where scanning begins
print(f"Scanning {start_folder}")#prints a start scanning message

with open("found_files.txt", "w") as output_file:
    
        for dirpath, dirnames,filenames in os.walk(start_folder):
            for file_name in filenames:
                if file_name.lower().endswith(target_ext):#checks if filenme matches the extension
                    full_path = os.path.join(dirpath,file_name)#this helps to build the filr path
                    output_file.write(full_path +"\n")#this helps to write/save the filepsth to output_file


#xupports multiple extension scanning

print("This scanner supports(.pdf,.docx,.zip,.mp4,.csv,.txt) only")
ext_input = input("Enter extensions to search(separate with commas): ").strip().lower()

#the emprty list hols the file ext the user wants to scan
target_ext = []
for ext in ext_input.split(","):
    ext = ext.strip().title() #this helps to forma/clean the exts
    if not ext_input.lower().startswith("."):#checking if the exts startswith a dot(.)
        ext = "." + ext 
    else:
        ext = ext
    target_ext.append(ext) #this appends the exts to the empty list

start_folder = r"C:\\"#serves as root folder and starts scan from there
print(f"Scanning {start_folder}")#prints a start scanning message

with open("found_files.txt","w") as output_file:

    for dirpath,dirnames,filenames in os.walk(start_folder):#starts transversing from the root folder
        for file_name in filenames:
            if any(file_name.lower().endswith(ext) for ext in target_ext):
                full_path = os.path.join(dirpath,file_name)#creates a fullpath of the file ext
                output_file.write(full_path + "\n")#saves te file path in a file

#Step 5

start_folder = r"C:\\"#this is the root folder where scanning begins
print(f"Scanning {start_folder}")#prints a start scanning message

found_count = 0


with open("found_files.txt","w") as output_file:
    for dirpath,dirnames,filenames in os.walk(start_folder):#starts transversing from the root folder
        for file_name in filenames:
            if any(file_name.lower().endswith(ext) for ext in target_ext):
                full_path = os.path.join(dirpath,file_name)#creates a fullpath of the file ext
                output_file.write(full_path + "\n")#saves te file path in a file

                found_count +=1

print(f"Scan Complete: {found_count} files found")


#THIS IS STILL VERY BASIC, IMPROVEMENTS WILL BE SURELY MADE