def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
nums=list(map(int, input("Enter the list of elements").split()))
print (nums)
print(linear_search(nums, 70))
