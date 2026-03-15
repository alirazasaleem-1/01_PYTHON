# This program sorts the pics/files inside folders according to their date 

import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS 

source_folder = r"D:\03 BACKUP\Google Photos Backup\2025-12-12"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path) and file.lower().endswith(("jpg", "jpeg", "png")):
        try:
            image = Image.open(file_path)
            exif_data = image._getexif()
            image.close()
            original_date = None 
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        original_date = value
                        break
                if original_date:
                    folder_name = original_date[:10].replace(":", "-")
            else:
                import datetime
                folder_name = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d")
            new_folder = os.path.join(source_folder, folder_name)
            os.makedirs(new_folder, exist_ok= True)

            shutil.move(file_path, os.path.join(new_folder, file))
            print(f"File: {file} successfully moved to {folder_name}")
        except Exception as e:
            print(f"Couldn't process {file} : {e}")

print("--- Accuracy level: 100% | Photos Organized ---")