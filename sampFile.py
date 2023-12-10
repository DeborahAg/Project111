import os
import shutil

from_dir="C:/Users/owoad/Downloads"
print(os.listdir(from_dir))
source="c:/users/owoad/Downloads/CA.png"
destination="C:/Users/owoad/Downloads/Sample/sampFile.py/test1.png"
shutil.copy(source,destination)
print("File Copied")