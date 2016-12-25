class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
    
        """
        if not s or s == "0":
            return 0
        i = 0
        num = 0
        op = '+'
        stack = []
        for i in xrange(len(s)): #Mistake while should be for
            if s[i].isdigit():
                num = num*10 + ord(s[i])-ord('0')
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if op == '-':
                    stack.append(-num)
                elif op == '+':
                    stack.append(num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                else: #Mistake will miss last one if op == '/':
                    if num != 0:
                        #stack.append(stack.pop()//num)  #Mistake -3//2 = -2 
                        tmp = stack.pop()
                        if tmp//num < 0 and tmp%num != 0:
                            stack.append(tmp//num+1)
                        else:
                            stack.append(tmp//num)
                num = 0
                op = s[i]
        return sum(stack)
s = Solution() 
print s.calculate("14-3/2")
print s.calculate("1")  #"0"
        # while i < n:
        #     while i < n and s[i] == ' ':
        #         i += 1
        #     start = i
        #     num1 = 0
        #     while i < n and s[i].isdigit():
        #         i += 1
        #         num1 = num1*10 + s[i]
        #     if i >= n: break #TBD
        #     op = s[i]
        #     num2 = 0

        #     if op == '*' or op == '/':
        #         while i < n and s[i].isdigit():
        #             i += 1
        #             num2 = num2*10 + s[i]
        #         stack.push(num2 * num1)