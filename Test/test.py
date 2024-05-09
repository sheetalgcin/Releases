import os
import datetime
annotations = {"events" : [{}],"v": 1}
event = [{"date": "", "component": "", "type": "", "tenant_id": "","version": ""}]
# Access environment variables
release = os.environ.get('RELEASE_TAG')
dateInfo = os.environ.get('RELEASE_DATE')

# Print or use the values as needed
print(f'Release Info: {release}')
print(f'dateInfo: {dateInfo}')

datetime_obj = datetime.datetime.fromisoformat(dateInfo)

# Convert datetime object to Unix epoch time
epoch_time = int(datetime_obj.timestamp())

events["date"] = int(epoch_time)
events["component"] = "zolagus"
events["type"]  = "release"
events["tenant_id"] = 1
events["version"] = str(release)

print(events)
print(annotations["events"].append(event))

# Print the result
print(epoch_time)
