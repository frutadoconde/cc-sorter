import os
import shutil
import yaml

with open("config.yml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

source_directory = config["source_directory"]
categories = config["categories"]

for category in categories.values():
    if not os.path.exists(category["folder_path"]):
        os.makedirs(category["folder_path"])

def move_files(source_dir, categories):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            for category, details in categories.items():
                for keyword in details["keywords"]:
                    if keyword.lower() in filename.lower():
                        destination_folder = details["folder_path"]
                        shutil.move(file_path, os.path.join(destination_folder, filename))
                        print(f"Moved '{filename}' to '{destination_folder}'")
                        break

move_files(source_directory, categories)

print("File moving completed.")