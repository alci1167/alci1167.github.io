class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        maxa = 0
        sta = []
        for i in range(N):
            start = i
            while sta and heights[i] < sta[-1][1]:
                cur = sta.pop()
                start = cur[0]
                maxa = max(maxa, (i - cur[0]) * cur[1])
            sta.append((start, heights[i]))
        while sta:
            cur = sta.pop()
            maxa = max(maxa, (N - cur[0]) * cur[1])
        return maxa
