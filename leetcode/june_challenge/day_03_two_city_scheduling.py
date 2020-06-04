class Solution:
    
    def cost_comparator(self, cost):
        return cost[0] - cost[1]

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=self.cost_comparator)
        n = len(costs)/2
        total_cost = 0
        for idx, item in enumerate(costs):
            if idx < n:
                total_cost += item[0]
            else:
                total_cost += item[1]
        return total_cost
