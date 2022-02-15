from math import ceil,log2
def buildSegmentTree(A,tree,curr_index,tl,tr):
    if tl==tr:
        tree[curr_index]=A[tl]
    else:
        mid=(tl+tr)//2
        buildSegmentTree(A,tree,2*curr_index+1,tl,mid)
        buildSegmentTree(A,tree,2*curr_index+2,mid+1,tr)
        tree[curr_index]=-1
 
def update(tree,curr_index,tl,tr,l,r,andVal):
    if l>r:
        return
    if l==tl and r==tr:
        if tree[curr_index]==-1:
            tree[curr_index]=andVal
        else:
            tree[curr_index]&=andVal
    else:
        mid=(tl+tr)//2
        update(tree,2*curr_index+1,tl,mid,l,min(r,mid),andVal)
        update(tree,2*curr_index+2,mid+1,tr,max(mid+1,l),r,andVal)
 
def get(tree,curr_index,tl,tr,i):
    if tl==tr:
        return tree[curr_index]
    else:
        mid=(tl+tr)//2
        if i<=mid:
            if tree[curr_index]==-1:
                return get(tree,2*curr_index+1,tl,mid,i)
            else:
                return tree[curr_index] & get(tree,2*curr_index+1,tl,mid,i)
        else:
            if tree[curr_index]==-1: 
                return get(tree,2*curr_index+2,mid+1,tr,i)
            else:
                return tree[curr_index] & get(tree,2*curr_index+2,mid+1,tr,i)
 
def main():
    N,Q=map(int,input().split())
    A=list(map(int,input().split()))
    tree=[-1]*(2*pow(2,int(ceil(log2(N))))-1)
    buildSegmentTree(A,tree,0,0,N-1)
    for _ in range(Q):
        L,R,V=map(int,input().split())
        update(tree,0,0,N-1,L-1,R-1,V)
    for i in range(N):
        print(get(tree,0,0,N-1,i),end=" ")

main()