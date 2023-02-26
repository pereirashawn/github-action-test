import json
import os

env_file = os.environ['GITHUB_OUTPUT']
print("value = {}".format(env_file))

with open(env_file,"r") as file:
    print(file.read())


# AOBResultObj = json.loads(AOBResult)

# print("isSucess: {}".format(AOBResultObj['isSuccess']))
# print("jsonString: {}".format(AOBResultObj['jsonString']))
# print("exceptionString: {}".format(AOBResultObj['exceptionString']))