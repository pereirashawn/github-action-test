import json
import os
import sys

AOBResult = (int)(sys.argv[0])

AOBResultObj = json.loads(AOBResult)

print("isSucess: {}".format(AOBResultObj['isSuccess']))
print("jsonString: {}".format(AOBResultObj['jsonString']))
print("exceptionString: {}".format(AOBResultObj['exceptionString']))