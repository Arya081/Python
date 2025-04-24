import os
import shutil

source_dir = "source"
target_dir = "target"
file_name = "exam.txt"

os.makedirs(target_dir, exist_ok=True)
shutil.copy(os.path.join(source_dir, file_name), target_dir)
