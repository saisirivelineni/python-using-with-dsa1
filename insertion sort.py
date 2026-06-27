def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i] #Element to be inserted
        j=i-1 #compare with previous element
        #shift element greater than key
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1

            #place key at correct position
            arr[j+1]=key
        return arr
#Example
numbers=[101,102,103,107,105,106,108,109]
sorted_numbers=insertion_sort(numbers)
print(sorted_numbers)