f=open("xr.txt", "r", encoding="utf-8")
f=f.readlines()
c={}
for l in f:
    letter=l[:1]
    q=list(c.get(letter, []))
    q.append(l.rstrip())
    print(letter)
    c.update({letter: q})


