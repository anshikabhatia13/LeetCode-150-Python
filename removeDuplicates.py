def removeDuplicates(nums: list[int]) -> int:
    r=1
    l=1
    for i in range(1,len(nums)):
        
        if nums[i]==nums[i-1]:
            r=r+1 
        else:
            nums[l]=nums[i]
            l=l+1
            r=r+1
    print(nums[:l])
    return l

    
#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
#nums=[1,1]
print(removeDuplicates(nums))