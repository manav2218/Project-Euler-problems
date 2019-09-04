# Solution to Longets Collatz Problem
maxx=0
maximum=[]
def Collatz(n):
    list1=[]
    x=n
    while x!=1:
        if x%2==0:
            x=x/2
            list1.append(x)
        else:
            x=3*x+1
            list1.append(x)

    for i in range(len(list1)):
        list1[i]=str(int(list1[i]))
    str1="->".join(list1)
    return len(list1)
   

for i in range(1,1000000):
    val=Collatz(i)
    if maxx<val:
        maxx=val
print("The number causing longest chain is ",i)
print("The size of longest chain is ",maxx)







