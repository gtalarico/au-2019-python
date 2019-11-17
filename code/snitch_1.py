import os

path = "/Users/gtalarico/dev/repos/others"


for root, _, files in os.walk(path):
    for filename in files:
        filepath = os.path.join(root, filename)
        stats = os.stat(filepath)
        size_in_bytes = stats.st_size

breakpoint()
