filename = input("File name: ")
start_ext = filename[::-1].find('.')
ext_type = filename[(-start_ext):].lower()

ext_dict = {
    "gif": "image/gif",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
    }

if ext_type in ext_dict:
    print(ext_dict[ext_type])
else:
    print("application/octet-stream")