import os
import math

path = r"/Users/gtalarico/dev/repos/others"

byte = 1
kb = 1024
mb = 1024 * 1024

def bytes_to_mb(size_in_bytes):
    return round(size_in_bytes / mb, 3)


for root, dirs, files in os.walk(path):
    pass
    # print(root)
    # print(dirs)
    # print(files)

for root, dirs, files in os.walk(path):
    # pass
    # print(root)
    # print(dirs)
    for filename in files:
        filepath = os.path.join(root, filename)
        # print(filepath)


for root, dirs, files in os.walk(path):
    # pass
    # print(root)
    # print(dirs)
    for filename in files:
        filepath = os.path.join(root, filename)
        file_stats = os.stat(filepath)
        size_in_bytes = file_stats.st_size

        size_in_mb = bytes_to_mb(size_in_bytes)
        if size_in_mb > 1:
            pass
            # print(filepath)
            # print(size_in_mb)
            # print(f"File: {filename} Size: {size_in_mb}MB")


large_files = []

for root, dirs, files in os.walk(path):
    # pass
    # print(root)
    # print(dirs)
    for filename in files:
        filepath = os.path.join(root, filename)
        file_stats = os.stat(filepath)
        size_in_bytes = file_stats.st_size

        size_in_mb = bytes_to_mb(size_in_bytes)
        if size_in_mb > 1:
            # print(filepath)
            # print(size_in_mb)
            file_info = f"File: {filename} Size: {size_in_mb}MB"
            large_files.append(file_info)

print(large_files)
