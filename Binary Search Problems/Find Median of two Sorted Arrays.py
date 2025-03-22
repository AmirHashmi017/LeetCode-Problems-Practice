def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        half=(len(nums1)+len(nums2))//2
        if(len(nums2)<len(nums1)):
            nums1,nums2=nums2,nums1
        
        left=0
        right=len(nums1)-1
        while True:
            mid=(left+right)//2
            leftend=half-(mid+2)
            nums1left=nums1[mid] if mid>=0 else float("-infinity")
            nums1right=nums1[mid+1] if mid+1<len(nums1) else float("infinity")
            nums2left=nums2[leftend] if leftend>=0 else float("-infinity")
            nums2right=nums2[leftend+1] if leftend+1<len(nums2) else float("infinity")

            if(nums2left<=nums1right and nums1left<=nums2right):
                if((len(nums1)+len(nums2))%2==1):
                    return min(nums1right,nums2right)
                else:
                    return (float(max(nums1left,nums2left))+float(min(nums1right,nums2right)))/2
            elif(nums2left>nums1right):
                left=mid+1
            elif(nums1left>nums2right):
                right=mid-1

print(findMedianSortedArrays([1,2],[3,4]))