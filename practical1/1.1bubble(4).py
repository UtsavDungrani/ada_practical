def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr=[]

n=int(input("Enter the number of elements: "))
for i in range(n):
    value=int(input("Enter number: "))
    arr+=[value]

print(bubble(arr))
