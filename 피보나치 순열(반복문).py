Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(x):
    answer = 0
    i = 1
    temp = 0
    a = 1
    if (x >= 2):
        while (a < x):
            answer = i + temp
            temp = i
            i = answer
            a = a + 1
    elif (x == 0):
        answer = 0
    elif (x == 1):
        answer = 1
    
    return answer