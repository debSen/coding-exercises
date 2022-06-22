class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", '-', "*", "/"]
        
        stack = []
        
        for item in tokens:
            if item not in ops:
                stack.append(str(item))
            elif item in ops:
                ops1 = stack[-1]
                del stack[-1]
                ops2 = stack[-1]
                del stack[-1]
                val = int(eval(ops2+ item + ops1))
                stack.append(str(val))
            
        return stack[-1]
        