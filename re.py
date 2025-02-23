import re

p = re.compile(r"^[0-9]+$", re.S)

num = "123"
snum = "s123"

if p.search(num):
    print("number")
else:
    print("string")

if p.search(snum):
    print("number")
else:
    print("string")