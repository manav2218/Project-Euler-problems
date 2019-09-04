#My code to Problem 1 of Project Euler
def SumofMul(n):
    list1=[]
    sum=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            list1.append(i)
    for i in list1:
        sum+=i
    return sum
print(SumofMul(1000))
