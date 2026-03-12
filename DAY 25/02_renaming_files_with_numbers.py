import os
folder = r"D:\01_PYTHON\automate"
counter = 1
for file_name in os.listdir(folder):
    if file_name.endswith(".txt"):
        new_name = str(counter) + "_" + file_name
        old_path = os.path.join(folder , file_name)
        new_path = os.path.join(folder , new_name)
        os.rename = (old_path, new_path)
        counter += 1
        print(f"Renamed {file_name} to {new_name}")

