def solution(L, x, l, u):
    if l + 1 == u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L,x,l,mid)
    else:
        return solution(L,x,mid,u)
