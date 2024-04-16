class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top is len(cost)
        # dp[i] is the minimum cost to climb top starting from ith staircase
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1) :
            # starting at 15
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])

        
