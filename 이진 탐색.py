Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(L, x):
    lower = 0
    upper = len(L) - 1 
    idx = -1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] > x:
            upper = middle - 1
        else:
            lower = middle + 1
    
    return idx