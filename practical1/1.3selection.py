def selection(arr):
    n=len(arr)
    
    for i in range(n):
        min_idx=i
        
        for j in range(i+1, n):
            if(arr[j]<arr[min_idx]):
                
                min_idx=j

                temp=arr[i]
                arr[i]=arr[min_idx]
                arr[min_idx]=temp
    return arr

print(selection([2,1,0,0,9,6,8,5]))