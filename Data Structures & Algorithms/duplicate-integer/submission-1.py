class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited={}
        i=0
        while i<len(nums):
            if nums[i] not in visited:
                visited[nums[i]]=i
            else:
                return True
            i+=1
        return False