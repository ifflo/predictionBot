# utils/rate_limiter.py
import time


class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def wait(self):
        now = time.time()
        while len(self.requests) >= self.max_requests:
            if now - self.requests[0] > self.time_window:
                self.requests.pop(0)
            else:
                time.sleep(self.time_window - (now - self.requests[0]))
            now = time.time()
        self.requests.append(now)


binance_limiter = RateLimiter(max_requests=1200, time_window=60)  # Example: 1200 requests per minute
cyptocompare_limiter = RateLimiter(max_requests=1200, time_window=60)  # Example: 1200 requests per minute
