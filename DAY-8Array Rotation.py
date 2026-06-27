def left_rotate(arr,k):
        n=len(arr)
        k=k%n # important for larger k
        temp=arr[:k]
        arr=arr[k:]+temp
        return arr
arr=[1,2,3,4,5]
print(left_rotate(arr,7))
step1: [2,3,4,5,1]
step2: [3,4,5,1,2]
step3: [4,5,1,2,3]
step4: [5,1,2,3,4]
step5: [1,2,3,4,5]
step6: [2,3,4,5,1]
step7: [3,4,5,1,2]