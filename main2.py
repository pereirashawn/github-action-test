import json
import os

AOBResult = os.environ['GITHUB_OUTPUT']
print("value = {}".format(AOBResult))

# AOBResultObj = json.loads(AOBResult)

# print("isSucess: {}".format(AOBResultObj['isSuccess']))
# print("jsonString: {}".format(AOBResultObj['jsonString']))
# print("exceptionString: {}".format(AOBResultObj['exceptionString']))