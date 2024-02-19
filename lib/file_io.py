
from pathlib import Path

def write_file(file_name, file_content):
    try:
        
        file_name_with_extension = str(file_name) + ".txt"
        
        with open(file_name_with_extension, 'w') as file:
            
            file.write(file_content)
        print("Content successfully written to", file_name_with_extension)
    except Exception as e:
        print("An error occurred while writing to the file:", e)       

def append_file(file_name, append_content):
    try:
        file_name_with_extension = str(file_name) + ".txt"
        with open(file_name_with_extension, "a") as file:
            file.write(append_content)
    
        print("Content successfully appended to", file_name_with_extension)
    except Exception as e:
        print("An error occurred while appenidng to the file:", e)    
        

def read_file(file_name):
    try:
        file_name_with_extension = str(file_name) + ".txt"
        with open(file_name_with_extension, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
      print("File not found:", file_name_with_extension)    
    except Exception as e:
        print("An error occurre while reading the file:" ,e)      
