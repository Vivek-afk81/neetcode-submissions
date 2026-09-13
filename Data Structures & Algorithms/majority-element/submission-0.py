class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for x in freq:
            if freq[x]>(len(nums))//2:
                return x