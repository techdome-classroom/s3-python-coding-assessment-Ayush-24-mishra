class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():  # Check for opening brackets
            stack.append(char)
        elif char in parentheses_map.keys():  # Check for closing brackets
            if not stack or stack.pop() != parentheses_map[char]:
                return False  # Mismatched or unbalanced brackets

    return len(stack) == 0 
        pass







    



  

