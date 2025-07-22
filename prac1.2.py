def selection(arr):
    n=len(arr)
    for i in range(n):
        flag=i
        for j in range(i+1,n):
            if(arr[flag]>arr[j]):
                flag=j
        temp=arr[i]
        arr[i]=arr[flag]
        arr[flag]=temp
    return arr

arr=[]

n=int(input("Enter the number of elements: "))
for i in range(n):
    value=int(input("Enter number: "))
    arr+=[value]

print(selection(arr))