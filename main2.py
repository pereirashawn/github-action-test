import json
import os
import sys

AOBResult = sys.argv[1]

print("argument: {}".format(AOBResult))

AOBResultObj = json.loads(AOBResult)

print("isSucess: {}".format(AOBResultObj['isSuccess']))
print("jsonString: {}".format(AOBResultObj['jsonString']))
print("exceptionString: {}".format(AOBResultObj['exceptionString']))