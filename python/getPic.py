import os
path = 'C:\\hackathon\\python\\resource\\heavyMetal';
for dir_entry in os.listdir(path):
    dir_entry_path = os.path.join(path,dir_entry)
    print dir_entry_path
