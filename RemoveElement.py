def removeElement( nums: list[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k=k+1      
        print(nums[:k])
        return k

a=[3,2,2,3]#val=3
b=[0,1,2,2,3,0,4,2]#val = 2
print(removeElement(b,2))
