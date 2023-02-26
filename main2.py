import json
import os

AOBResult = os.environ['INPUT_STORE']

AOBResultObj = json.loads(AOBResult)

print("isSucess: {}".format(AOBResultObj['isSuccess']))
print("jsonString: {}".format(AOBResultObj['jsonString']))
print("exceptionString: {}".format(AOBResultObj['exceptionString']))