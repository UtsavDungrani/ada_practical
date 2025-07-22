def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# Take user input for array size
n = int(input("Enter the number of elements: "))
arr = []

# Take user input for array elements
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Sorted array:", bubble(arr))