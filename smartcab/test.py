import random

d = {'a': '7', 'e': '3', None: '9', 'g': '7', 'f': '1', 'j': '2', 'l': '9', 'w': '9'}

minvalue = min(d.items(), key=lambda x: x[1])[1]
maxvalue = max(d.items(), key = lambda x: x[1])[0]

intno = 100
assert isinstance(maxvalue, str)

maxQlist = []
for i in d:
    if d[i] == '7':
        maxQlist.append(i)
maxQ = random.choice(maxQlist)
print("maxQ:",maxQ)

print("max:",maxvalue,"min:",minvalue)


print("value for none:",d[None])
# assert isinstance(intno, str)