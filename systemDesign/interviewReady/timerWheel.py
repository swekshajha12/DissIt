import time


class RateLimiter:
    def __init__(self):
        self.timeout = None
        self.capacity = None
        self.requests = {}

    def shouldAccept(self, requestId):
        # Remove expired requests
        currentTime = time.time()
        expired_requests = [requestId for requestId, timestamp in self.requests.items() if
                            currentTime - timestamp > self.timeout]
        for requestId in expired_requests:
            del self.requests[requestId]

        # Check if the request exceeds the capacity
        if len(self.requests) >= self.capacity:
            return False  # Request should not be accepted

        # Record the current request timestamp
        self.requests[requestId] = currentTime
        return True  # Request should be accepted

    def configure(self, timeoutInSeconds, capacityPerSecond):
        self.timeout = timeoutInSeconds
        self.capacity = capacityPerSecond
        self.requests = {}


ratelimiter = RateLimiter()

# Configure the rate limiter with a timeout of 6 seconds and a capacity of 3 requests per second
ratelimiter.configure(6, 3)

# Simulate requests
for i in range(1, 16):
    requestId = "Request" + str(i)
    accepted = ratelimiter.shouldAccept(requestId)
    print("Request {}: Accepted = {}".format(requestId, accepted))
    time.sleep(1)  # Sleep for 1 second
