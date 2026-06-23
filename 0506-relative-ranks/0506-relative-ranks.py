class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sortedList = sorted(score, reverse=True)
        rank = {}
        for i in range(n):
            if i == 0:
                rank[sortedList[i]] = "Gold Medal"
            elif i == 1:
                rank[sortedList[i]] = "Silver Medal"
            elif i == 2:
                rank[sortedList[i]] = "Bronze Medal"
            else:
                rank[sortedList[i]] = str(i+1)
        ans = []
        for scr in score:
            ans.append(rank[scr])
        return ans