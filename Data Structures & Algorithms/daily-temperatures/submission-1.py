class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                n = stack.pop()
                sol[n] = i - n
            stack.append(i)
        return sol