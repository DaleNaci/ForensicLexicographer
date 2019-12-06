import json
import statistics



# this is just for now im sure we will change it later
filename = "author.json"

try:
    with open(filename, 'r') as source:
        author_profile = json.loads(source.read())
except:
    # error stuff here
    exit()


# here is where u check all the stuff

print(author_profile) # just for now


print(f"print the author % match result")
