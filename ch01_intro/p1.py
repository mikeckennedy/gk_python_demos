print("About to import p2")
from p2 import get_user_name
print("Done importing p2")

print("Downloading data, we'll save it to your profile")
name = get_user_name()

print("Using /Users/{}/data".format(name))