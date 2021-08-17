Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(L, x):
    answer = []
    
    for i in L:
        if i > x:
            L.insert(L.index(i), x)
            break
    
    if L[len(L)-1] < x:
        L.append(x)
    
    return L