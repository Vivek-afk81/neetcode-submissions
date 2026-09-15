class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        
        freq=dict(sorted(freq.items(), key=lambda x:x[1],reverse=True))
        for i in range(k):
            result.append(list(freq.items())[i][0])
        return result