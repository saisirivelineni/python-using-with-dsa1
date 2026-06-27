def is_subset(A,B):
    for element in B:
        if element not in A:
                return False
        return True
A=[1,2,3,4,5]
B=[2,4]
print(is_subset(A,B))