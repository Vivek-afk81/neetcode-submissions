class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        j=n-1
        i=0
        while i<n and j>0:

            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]

            if numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1

        