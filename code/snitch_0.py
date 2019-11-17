import os

path = "/Users/gtalarico/dev/repos/others"

for thing in os.walk(path):
    print(thing)
    break
