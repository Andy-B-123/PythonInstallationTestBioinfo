# Hello.py

from tqdm import tqdm
import time

def hello():
    for _ in tqdm(range(10)):
        print("Hello, world!")
        time.sleep(0.5)

if __name__ == "__main__":
    hello()
