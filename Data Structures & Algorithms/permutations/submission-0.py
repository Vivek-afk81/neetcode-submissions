class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)

        def solve(subsets):
            if len(subsets)==len(nums):
                res.append(subsets.copy())
                return
            for i in range(len(nums)):
                if used[i]==False:
                    subsets.append(nums[i])
                    used[i]=True
                    solve(subsets)
                    subsets.pop()
                    used[i]=False
        solve([])
        return res