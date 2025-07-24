

def omg():
    x=["aaaa","aaa1223"]
    for ci in x:
        yield ci

for c in omg():
    print(c)