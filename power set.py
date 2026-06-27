def generate_subsets(nums):
    subsets=[[]] #starts with empty subset
    for num in nums:
            new_subsets=[]
            for subset in subsets:
                  new_subsets.append(subset + [num])
            subsets.extend(new_subsets)
    return subsets  
nums=[1,2,3]
print(generate_subsets(nums))