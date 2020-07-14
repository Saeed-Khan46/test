class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        cnt,cnt2 = 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                cnt += 1
            elif cnt > 0 and S[i] == ')':
                cnt -= 1
        for i in range(len(S) - 1, -1, -1):
            if S[i] == ')':
                cnt2 += 1
            elif cnt2 > 0 and S[i] == '(':
                cnt2 -= 1
        return cnt + cnt2

s=Solution()       
print(s.minAddToMakeValid("((("))
