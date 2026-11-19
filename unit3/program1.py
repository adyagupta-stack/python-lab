num=[1,2,3,2,4,1,3,3,2]
d={}
for i in num:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
