class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L=[]
        for i in range(0,len(nums)):
            y=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==y:
                    L.append(i)
                    L.append(j)
                    break
                continue
        return L


        
