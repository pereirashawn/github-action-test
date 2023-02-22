import os

try:
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
except KeyError:
    CLIENT_SECRET = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

print("Hello World from main.py")
print(" Secret Value: {} ".format(CLIENT_SECRET))