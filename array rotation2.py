def left_rotate(arr,k):
        n=len(arr)
        k=k%n # important for larger k
        temp=arr[:k]
        arr=arr[k:]+temp
        return arr
arr=[6,7,8,9,10]
print(left_rotate(arr,7))
step1: [7,8,9,10,6]
step2: [8,9,10,6,7]
step3: [9,10,6,7,8]
step4: [10,6,7,8,9]
step5: [6,7,8,9,10]
step6: [7,8,9,10]