import os
from send_email import send_email

def b_to_mb(num_bytes):
    return round(num_bytes / (1024 * 1024), 2)

def find_large_files(path):
    large_files = []
    for root, _, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            stats = os.stat(filepath)
            size_in_bytes = stats.st_size
            size_mbs = b_to_mb(size_in_bytes)
            if size_mbs < 5:
                continue

            large_file = { "filepath": filepath, "size": size_mbs}
            large_files.append(large_file)
    return large_files

# Send Email
path = "/Users/gtalarico/dev/repos/others"
large_files = find_large_files(path)
large_files_text = str(large_files)
send_email(large_files_text)


