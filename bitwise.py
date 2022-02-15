def out(k,tastevalue):
    l=len(tastevalue)
    count = 0
    for i in range(0,l):
        for j in range(i+1,l):
            if tastevalue[i]&tastevalue[j] > k:
                count+=1
    return count

n=int(input())
tastevalue=list(map(int,input().split())) 
k=int(input())
o = out(k,tastevalue)
print(o)