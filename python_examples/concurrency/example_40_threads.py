import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"Thread {self.name} starting")
        time.sleep(2)  # Simulate a time-consuming task
        print(f"Thread {self.name} finished")

# Create and start multiple threads
threads = [WorkerThread(name=f"Worker-{i}") for i in range(3)]
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads completed.")
