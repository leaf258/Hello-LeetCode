

class Solution:
    def isValid(self, s:str) -> bool:
        if len(s)%2:
            return False
        
        mp = {'(':')','[':']','{':'}'}
        st = []

        for c in s:
            if c in mp:
                st.append(c)
            # elif not st:
            #     return False
            elif not st or c != mp[st.pop()]:
                return False
        return not st
    
s = "[(]"
a = Solution()
print(a.isValid(s))





