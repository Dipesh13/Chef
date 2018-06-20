import os

def file_path(filepath):
    filepath = filepath.split("/")[-1]
    #to extract filename from filepath
    print(os.path.basename(filepath))
    # to etract extenstion and name from filename
    name, ext = os.path.splitext(filepath)
    print(name)
    print(ext)

# files = ['/home/mohit/abc 12.pdf','/home/mohit/  h:ey_there.pdf','home/mohit//he#llo.pdf','hey..pdf','home/mohit/hey/there.pdf']
folder = './data'
files = os.listdir(folder)

for f in files:
    file_path(f)
