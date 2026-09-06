class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (2 * n)
        result = []

        def solve(idx, total,brackets,result):
            if idx == len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
            if total>len(brackets)//2:
                return
            if total<0:
                return
            
            brackets[idx]="("
            summation=total+1
            solve(idx+1,summation,brackets,result)
            brackets[idx]=")"
            summation=total-1
            solve(idx+1,summation,brackets,result)
        solve(0,0,brackets,result)
        return result
            


