def insertion(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertion([2,1,0,9,6,8,5]))