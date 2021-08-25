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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for element in tokenList:
        if type(element) is int:
            postfixList.append(element)
        if element == '(':
            opStack.push(element)
        if element == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        if element in ['*','+','-','/','(',')']:
            if opStack.isEmpty():
                opStack.push(element)
            else:
                while prec[opStack.peek()] >= prec[element]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
                opStack.push(element)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return postfixList


def postfixEval(tokenList):
    
    opStack = ArrayStack()

    for element in tokenList:
        if element not in ['*','+','-','/']:
            opStack.push(element)
        if element in ['*','+','-','/']:
            value = opStack.pop() * opStack.pop()
            opStack.push(value)
            
    return opStack.pop()
        
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val