import os
import shutil
import datetime

source_dir = r"D:\New folder"# always use "r" as raw or (\\) while using \ for naming a folder in the code
destination_dir = r"D:\Backup"

def copy_folder_to(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exist in: {dest}")

copy_folder_to(source_dir,destination_dir)




