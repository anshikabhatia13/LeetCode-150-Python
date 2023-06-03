def removeDuplicates(nums: list[int]) -> int:
    if len(nums)<3 :
        return len(nums)
    l=2
    for i in range(2,len(nums)):
        if nums[i]!=nums[l-2]:
            nums[l]=nums[i]
            l=l+1
                 
    print(nums[:l])
    return l

    
nums = [1,1,1,2,2,2,3]
#nums = [0,0,1,1,1,1,2,3,3]
#nums=[1,1]
print(removeDuplicates(nums))