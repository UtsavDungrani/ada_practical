def bubble(arr):
    for i in range(len(arr),0,-1):
        for j in range(0, i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble([6,1,5,0,4,3,1,9]))