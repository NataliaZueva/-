rn = [[8,3,5], [4,9,3], [6,2,4], [3,9,1]]
rn2 = []
#rn = [2,4,6,8,1,5]
print ('1= ', rn)
def stroka(x):
    maxx=0
    m=0
    for i in range(len(x)):
        maxx=0
        for q in range(i, len(x)):
            if x[q]>maxx:
                maxx=x[q]
                m=q
        x[i],x[m]=x[m],x[i]
    return (x[::-1])


for i in rn:
    rn2.append(stroka(i))
print('2= ',rn2)


a=1
while a != 0:
    a=0
    for i in range(len(rn2)-1):
        k=0
        for j in range(len(rn2)-i-1):
            if rn2[i][k] == rn2[i+1][k]:
                while rn2[i][k] == rn2[i+1][k]:
                    k+=1
            if rn2[i][k]>rn2[i+1][k]:
                rn2[i],rn2[i+1]= rn2[i+1],rn2[i]
                a+=1
print('3= ',rn2)
    


    
        
