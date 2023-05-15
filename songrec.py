# Function to search the specified array `nums` for key `target`
# using the binary search algorithm
def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
 
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid      # key found
 
    return low              # key not found
 
 
# Function to find the `k` closest elements to `target` in a sorted integer array `nums`
def findKClosestElements(nums, target, k):
 
    # find the insertion point using the binary search algorithm
    i = binarySearch(nums, target)
 
    left = i - 1
    right = i
 
    # run `k` times
    while k > 0:
 
        # compare the elements on both sides of the insertion point `i`
        # to get the first `k` closest elements
 
        if left < 0 or (right < len(nums) and abs(nums[left] - target) > abs(nums[right] - target)):
            right = right + 1
        else:
            left = left - 1
 
        k = k - 1
 
    # return `k` closest elements
    return nums[left+1: right]
 
 
if __name__ == '__main__':
 
    nums = [10, 12, 15, 17, 18, 20, 25]
    target = 16
    k = 4
 
    print(findKClosestElements(nums, target, k))