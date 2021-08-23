Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for element in S:
        if element not in "*+-/()":
            answer += element
        if element == "(":
            opStack.push(element)
        if element == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        if element in "*+-/":
            if opStack.isEmpty():
                opStack.push(element)
            else:
                while prec[opStack.peek()] >= prec[element]:
                    answer += opStack.pop()
                    if opStack.isEmpty():
                        break
                opStack.push(element)
    while not opStack.isEmpty():
        answer += opStack.pop()
            
    return answer