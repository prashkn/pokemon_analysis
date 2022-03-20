from call import *

test = make_call("pokemon", "35")["moves"]
for obj in test:
    print(obj["move"]["name"])
