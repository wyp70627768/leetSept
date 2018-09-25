# 354. Russian Doll Envelopes
'''
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        env_sort = [x[1] for x in sorted(envelopes, key = lambda x: (x[0], -x[1]))]
        dp = [0]*len(envelopes)
        ans = 0
        for env in env_sort:
            i = bisect.bisect_left(dp, env, 0, ans)
            dp[i] = env
            if ans == i:
                ans += 1
        return ans

