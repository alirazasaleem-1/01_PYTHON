# Mini task is to rename 5 files with the suffix _day1
import os
folder = r"D:\01_PYTHON\automate\Mini Task"
for file_name in os.listdir(folder):
    if file_name.endswith(".txt"):
        name_only , extension_name = os.path.splitext(file_name)
        new_name = name_only + "_day1" + extension_name
        old_path = os.path.join(folder , file_name)
        new_path = os.path.join(folder , new_name)
        os.rename(old_path , new_path)
        print(f"✅ Renamed {file_name} to {new_name}")