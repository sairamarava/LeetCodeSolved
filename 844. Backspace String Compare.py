class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def result(s):
            stack=[]
            for i in s:
                if i!='#':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop(-1)
            return ''.join(stack)
        return result(t)==result(s)

                    

                
        
