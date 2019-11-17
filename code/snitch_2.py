import os

path = "/Users/gtalarico/dev/repos/others"

def b_to_mb(num_bytes):
    return round(num_bytes / (1024 * 1024), 2)


for root, _, files in os.walk(path):
    for filename in files:
        filepath = os.path.join(root, filename)
        stats = os.stat(filepath)
        size_in_bytes = stats.st_size
        size_mbs = b_to_mb(size_in_bytes)
        if size_mbs < 5:
            continue
        print(filepath)
        print(f"{size_mbs}MiB")

breakpoint()
