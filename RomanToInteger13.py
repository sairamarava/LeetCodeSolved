class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D': 500,'M': 1000}
        for a, b in zip(s,s[1:]):
            if dic[a]<dic[b]:
                ans-=dic[a]
            else:
                ans+=dic[a]
        return ans+dic[s[-1]]
