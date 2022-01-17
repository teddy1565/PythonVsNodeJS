import multiprocessing

def count():
    for i in range(1000000000):
        continue

if __name__ == "__main__":
    for i in range(10):
        multiprocessing.Process(target=count).start()
