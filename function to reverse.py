#function to reverse part of array:
def reverse (arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def left_rotate(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr
#Right rotate using left rotate
def right_rotate(arr, k):
     n=len(arr)
     k=k%n
     return left_rotate(arr,)
print("Original Array:",arr)
print("Right Rotate Array:', right_rotate(arr,k))