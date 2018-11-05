import os
from string import digits
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"ENTER THE PATH TO ALPHABET FILE, ex /Users/Downloads/rename_file/alphabet")
    print(file_list)
    saved_path = os.getcwd()
    #print("Current Working Directory is " + saved_path)
    os.chdir(r"ENTER THE PATH TO ALPHABET FILE, ex /Users/Downloads/rename_file/alphabet")
    #(2) for each file, rename filename(without numbers)
    for file_name in file_list:
        print("Old Name - " + file_name)
        remove_digits = file_name.maketrans('', '', digits)
        os.rename(file_name, file_name.translate(remove_digits))
        print("New Name - " + file_name.translate(remove_digits))

    os.chdir(saved_path)

rename_files()

