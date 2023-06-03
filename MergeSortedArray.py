# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

def merge(nums1: list[int], m: int, nums2: list[int], n: int) :
        """
        Do not return anything, modify nums1 in-place instead.
        Here we have nums1 as first array, nums2 as second arrray and m is the index of last value of 
        nums1 , n is the index of last value of nums2
        """
        #get the last value of nums 1
        l=m+n-1
        # start merging in reverse order
        while n>0 and m>0:
            if nums1[m-1]> nums2[n-1]:
                nums1[l]=nums1[m-1]
                m=-1
                
            else:
                nums1[l]=nums2[n-1]
                n=-1
                l=-1
            
        
        while n>0:
            nums1[l]=nums2[n-1]
            l,n=l-1,n-1


a=[1,2,5,0,0,0] #m=3
b=[2,5,6] #n=3
# a=[] #m=0
# b=[1] #n=1

merge(a,3,b,3)
print(a)