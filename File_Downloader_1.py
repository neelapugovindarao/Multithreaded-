import time
import random
from concurrent.futures import ThreadPoolExecutor

FILES = [
    ("file1.zip", 10),
    ("file2.mp4", 20),
    ("file3.pdf", 5),
    ("file4.jpg", 2),
    ("file5.mp3", 8)
]


def download(file):
    name, size = file

    print(f"Starting download: {name}")

    time.sleep(size * random.uniform(0.2, 0.5))

    if random.random() < 0.2: # speed factor
        print(f"Failed: {name}")
        return (name, False)

    print(f"Completed: {name}")
    return (name, True)

