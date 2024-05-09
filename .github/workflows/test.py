import os

# Access environment variables
timestamp_seconds = os.environ.get('TIMESTAMP_SECONDS')
iso8601_timestamp = os.environ.get('ISO8601_TIMESTAMP')

# Print or use the values as needed
print("Timestamp seconds:", timestamp_seconds)
print("ISO8601 timestamp:", iso8601_timestamp)

