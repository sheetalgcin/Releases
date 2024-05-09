import os
import datetime

# Access environment variables
release = os.environ.get('RELEASE_TAG')
dateInfo = os.environ.get('RELEASE_DATE')

# Print or use the values as needed
print(f'Release Info: {release}')
print(f'dateInfo: {dateInfo}')

datetime_obj = datetime.datetime.fromisoformat(dateInfo)

# Convert datetime object to Unix epoch time
epoch_time = int(datetime_obj.timestamp())

# Print the result
print(epoch_time)
