class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(list(current))
                return
            if i >= len(candidates) or total > target:
                return

            # include current number
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()

            # move to next number
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result
