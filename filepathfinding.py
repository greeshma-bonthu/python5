
import sys
import os
file_path = input("File_path:")
does_file_exist = os.path.exists(file_path)
print(does_file_exist)
if(does_file_exist==0):
    print("alert")
    sys.exit(0)
