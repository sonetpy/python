import os 
listing = os.walk('/home/abhinav/Python')
for root_path, directories, files in listing:
     print("root path =", root_path)
     print("directories =", directories)
     print("files =", files)
     print()
