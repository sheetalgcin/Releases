import os

# Access environment variables
timestamp_seconds = os.environ.get('RELEASE_TAG')
iso8601_timestamp = os.environ.get('RELEASE_DATE')

# Print or use the values as needed
print("Timestamp seconds:", timestamp_seconds)
print("ISO8601 timestamp:", iso8601_timestamp)

