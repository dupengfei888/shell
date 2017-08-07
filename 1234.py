Sum=0
Li=list(range(1,5))
for i in Li:
    for j in Li:
        if i != j:
            for k in Li:
                if k != j and k != i:
                    print("%s%s%s"%(i,j,k))
                    Sum+=1
print('all have %s'%Sum)
