def triplet_sum(nums, target):
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None  # No triplet found


# Example
arr = [1, 4, 45, 6, 10, 8]
target = 22
print(triplet_sum(arr, target))