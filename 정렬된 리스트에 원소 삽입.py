 def solution(L, x):
    answer = []
    
    for i in L:
        if i > x:
            L.insert(L.index(i), x)
            break
    
    if L[len(L)-1] < x:
        L.append(x)
    
    return L