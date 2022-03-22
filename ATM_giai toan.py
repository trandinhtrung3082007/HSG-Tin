def main(N, S, nums):
    visited = set()
    def dfs(i, target, sofar=[]):
        if (i, target) in visited:
            return None
        visited.add((i, target))
        if target == 0:
            return sofar
        if i == N - 1 or target < 0:
            return None
        return dfs(i + 1, target, sofar) or dfs(i + 1, target - nums[i], sofar + [nums[i]])
    return dfs(0, S)

def main2(N, S, nums):
    dp = [[[] for _ in range(N + 1)] for _ in range(S + 1)]
    for i, num in enumerate(nums, 1):
        for s in range(S + 1):
            if s >= num and (dp[s][i - 1] or s == S):
                dp[s - num][i] = dp[s][i - 1] + [num]
            dp[s][i] = dp[s][i - 1] + []
    for res in dp[0]:
        if res:
            return res

print(main(10, 390, [200, 10, 20, 20, 50, 50, 50, 50,100, 100]))
print(main2(10, 390, [200, 10, 20, 20, 50, 50, 50, 50,100, 100]))