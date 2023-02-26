import os
import sys
import json

try:
    CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    input_variable = (int)(os.environ['INPUT_STORE'])
    print("val: {}".format(input_variable))
except KeyError:
    CLIENT_SECRET = "Token not available!"
    # or raise an error if it's not available so that the workflow fails


AOBResult = "AOBResult"
AOBResultObj = {
     "isSuccess": True,
     "jsonString": "Library Success",
     "exceptionString": ""
}

if(input_variable % 2 == 0):
    print("{} is an EVEN number".format(input_variable))
else:
    print("{} is an ODD number".format(input_variable))

if "GITHUB_OUTPUT" in os.environ :
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            f.write("AOBResult={}".format(AOBResultObj))



