import json
import random
import time
from datetime import datetime
import sys

# Sample log data generator
def generate_log():
    # Sample application names
    apps = ["web-app", "api-service", "auth-service", "database", "cache"]
    # Log levels
    levels = ["INFO", "WARN", "ERROR", "DEBUG"]
    # Sample messages
    messages = [
        "Request processed successfully",
        "Connection timeout",
        "Authentication failed",
        "Database query completed",
        "Cache miss",
        "Memory usage high",
        "CPU spike detected",
        "Network latency increased"
    ]
    # Sample status codes
    status_codes = [200, 201, 400, 401, 403, 404, 500, 503]
    # Sample IP addresses
    ips = [f"192.168.1.{random.randint(1, 255)}" for _ in range(5)]
    
    log = {
        "@timestamp": datetime.utcnow().isoformat(),
        "app": random.choice(apps),
        "level": random.choice(levels),
        "message": random.choice(messages),
        "status_code": random.choice(status_codes),
        "response_time": round(random.uniform(0.1, 2.0), 3),
        "client_ip": random.choice(ips),
        "bytes": random.randint(500, 15000)
    }
    
    return json.dumps(log)

# Generate logs continuously
try:
    while True:
        print(generate_log())
        sys.stdout.flush()
        time.sleep(0.5)  # Generate a log every half second
except KeyboardInterrupt:
    sys.exit(0)