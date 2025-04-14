
import hashlib
import os

# Directory and file extension configurations
directories = [
    'c:\\Users\\wensal\\Downloads\\test',
    'c:\\Users\\wensal\\Downloads\\css\\virus\\test'
]
file_extension = ".py"

# Function to search for and remove injected code
def search_in_directories(directories, file_extension):
    virus_count = 0
    cleaned_count = 0
    for directory in directories:
        for root, dirs, files in os.walk(directory, topdown=True, onerror=lambda e: None):
            for file in files:
                if file.endswith(file_extension):
                    result = remove_injected_code(os.path.join(root, file))
                    if result["detected"]:
                        virus_count += 1
                    if result["cleaned"]:
                        cleaned_count += 1
    return virus_count, cleaned_count

def remove_injected_code(file):
    hash = hashlib.md5(file.split("\\")[-1].encode("utf-8")).hexdigest()
    detected = False
    cleaned = False
    try:
        with open(file, "r") as original_file:
            lines = original_file.readlines()

        clean_lines = []
        inside_injected_section = False
        for line in lines:
            if f"# begin-{hash}" in line:
                detected = True
                inside_injected_section = True
                continue
            elif f"# end-{hash}" in line:
                inside_injected_section = False
                cleaned = True
                continue

            if not inside_injected_section:
                clean_lines.append(line)

        with open(file, "w") as cleaned_file:
            cleaned_file.writelines(clean_lines)

    except Exception as e:
        print(f"An error occurred: {e}")

    return {"detected": detected, "cleaned": cleaned}
search_in_directories()
