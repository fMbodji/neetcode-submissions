class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        for c in s:
            # if its an open element, add to stack
            if c not in closedToOpen:
                stack.append(c)
            # if its a closed elem, check if match is found
            else: 
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else: # stack is empty, or no match found
                    return False
        
        # at the end if stack is empty= all matches found -> True
        if not stack:
            return True
        return False 
                      


        