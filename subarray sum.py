def subarray_sum_bruteforce(arr,target):
    n=len(arr)
    for i in range(n):
        total=0
        for j in range(i,n):
            total+=arr[j]
            if total==target:
                return True
            return False