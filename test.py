


def main():
    str = input()
    lst = str.split (",")
    a=lst[0]
    b=lst[1]
    c1=0
    c2=0

    l=['a','e','i','o','u','A','E','I','O','U']

    for i in a:
        if i in l:
            c1+=1

    for i in b:
        if i in l:
            c2+=1
            
    if c1>c2:
        print(a)
        print(c1)
    elif c2>c1:
        print(b)
        print(c2)
    else:
        print("Both strings have same no. of vowels")
        print(c1)
    
        
if __name__=="__main__":
    main()