import threading


class SearchEngine:
    def __init__(self):
        # Initialize an empty dictionary to store signatures and their existence status
        self.signatures = {}
        # Create a reentrant lock to protect concurrent access to the dictionary
        self.lock = threading.RLock()

    def storeAsSignature(self, data):
        # Convert the data to a string as a unique hash signature (for simplicity)
        signature = str(data)
        # Acquire a lock for writing to the dictionary
        with self.lock:
            # Store the signature as a key with a value of True in the dictionary
            self.signatures[signature] = True

    def findMatch(self, data):
        # Convert the data to a string for comparison
        signature = str(data)
        # Acquire a read lock to safely search the dictionary
        with self.lock:
            # Check if the signature exists as a key in the dictionary
            return signature in self.signatures


# Create a new instance of the SearchEngine
search_engine = SearchEngine()

# Example usage with concurrent requests:
concurrent_requests = 100
threads = []


def worker(index):
    data = [index]  # Simulate some data
    search_engine.storeAsSignature(data)
    found = search_engine.findMatch(data)
    if found:
        print(f"Data {data} found.")
    else:
        print(f"Data {data} not found.")


# Create and start concurrent threads
for i in range(concurrent_requests):
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
