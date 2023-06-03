def majorityElement(nums: list[int])->int:
#   #O(n) space
#     count={}
#     result, maxCount=0,0
#     for n in nums:
#         count[n]= 1+ count.get(n,0)
#         #get(key, b) jere b is the value to be returned if key is not found
#         #count[n] means value of key n will be 1+ no of times val found
#         # 1 because at least onse it will be found
#         result=n if count[n]>maxCount else result
#         maxCount=max(count[n], maxCount)
#         #result will be n if count is greater yham maxCount
#         #maxCount is the max of count[n] and maxCount previously
#     return result

    #O(1) space BOYER MOORE ALGORITHM == works when we know there definitely is a majority element
    result=0
    count=0
    for n in nums:
        if count==0:
            result=n
        if n==result:
            count+=1
        else :
            count+=-1
    
    return result
        
    
nums = [3,2,3]
#nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))