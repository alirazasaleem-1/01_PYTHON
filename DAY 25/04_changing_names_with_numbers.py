# this program changes random file names to proper numbering 
import os
import logging
logging.basicConfig(
    filename = 'rename.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
folder = r"D:\03 BACKUP\01 OPPO BACKUP 2 Feb, 2026\DCIM\Camera"
counter = 1

for file_name in os.listdir(folder):
    old_path = os.path.join(folder, file_name)
    if os.path.isfile(old_path):
        name_only , extension = os.path.splitext(file_name)
        new_name = str(counter) + extension
        new_path = os.path.join(folder , new_name)
        os.rename(old_path , new_path)
        logging.info(f"Renamed {file_name} -> {new_name}")
        counter += 1
        print(f"✅ Renamed {file_name} to {new_name}")

print("\n✅ Done! Your folder is now completely ordered")