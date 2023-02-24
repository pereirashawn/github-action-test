import os
import sys

try:
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
except KeyError:
    CLIENT_SECRET = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

print(" --- HELLO WORLD ---")
num = (int)(sys.argv[1])
if(num%2 == 0):
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

