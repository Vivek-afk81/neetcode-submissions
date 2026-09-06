class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (2 * n)
        result = []

        def solve(idx, total):
            if idx == len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            # Add '('
            if total < n:
                brackets[idx] = "("
                solve(idx + 1, total + 1)

            # Add ')'
            if total > 0:
                brackets[idx] = ")"
                solve(idx + 1, total - 1)

        solve(0, 0)
        return result

