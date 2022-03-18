import numpy as np
def file_read(title):
    a=[]
    b=open(title,'r').readlines()
    for line in b:
        a.append([int(x) for x in line.split()])
    return a


def fas(w, v):
    i1=len(v)  #строки
    j1=len(v[1])  #cтолбцы
    for i in range(i1):
      for j in range(j1):
          if v[i][j] != w:
              v[i][j]=0
    for i in v:
        for i2 in i:
            print(i2, end=' ')
        print()
    return v

a = np.array(file_read("island.txt"))
a = np.arange(a)
print (a)

#for w in range (1, 10):
#    print ("Нахождение всех", w, ":")
#    fas(w, file_read("island.txt"))
    
