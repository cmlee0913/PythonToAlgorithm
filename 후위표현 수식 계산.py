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
    for c in tokenList:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            if c in prec:
                if opStack.isEmpty():
                    opStack.push(c)
                elif prec[opStack.peek()] >= prec[c]:
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                        postfixList.append(opStack.pop())
                    opStack.push(c)
                else:
                    opStack.push(c)
            else:
                postfixList.append(c)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    
    opStack = ArrayStack()

    for element in tokenList:
        if element not in ['*','+','-','/']:
            opStack.push(element)
        if element in ['*','+','-','/']:
            if element == '+':
                first_popdata = opStack.pop()
                second_popdata = opStack.pop()
                temp = first_popdata + second_popdata
                opStack.push(temp)
            elif element == '-':
                first_popdata = opStack.pop()
                second_popdata = opStack.pop()
                temp = second_popdata - first_popdata
                opStack.push(temp)
            elif element == '*':
                first_popdata = opStack.pop()
                second_popdata = opStack.pop()
                temp = first_popdata * second_popdata
                opStack.push(temp)
            elif element == '/':
                first_popdata = opStack.pop()
                second_popdata = opStack.pop()
                temp = second_popdata / first_popdata
                opStack.push(temp)
            
    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val