Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(L, x):
    
    if x in L:
        return list(filter(lambda e:L[e] == x, range(len(L))))
    else:
        return [-1]