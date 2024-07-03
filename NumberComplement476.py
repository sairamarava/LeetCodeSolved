class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Start From Here
        b=bin(int(num))[2:]
        s=""
        for i in str(b):
            if i=='0':
                s+='1'
            else:
                s+='0'
        s=s[::-1]
        sum=0
        for i in range(0,len(s)-1):
            sum+=int(s[i])*(2**i)
        return sum
