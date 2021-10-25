def mycount(str, mystr):
    count = 0
    substr = ''
    for i in str:
        substr += i
        if substr == mystr:
            count += 1
            substr = ''
    print(count)

def mystrip(mystr):
    reverse = mystr[::-1]
    for i in mystr:
        if i != ' ':
            first = mystr.index(i)
            break
    for i in reverse:
        if i != ' ':
            end = len(reverse[reverse.index(i):])
            break
            
    print('\'' + mystr[first:end] + '\'')

mycount('ababa', 'aba')
mystrip('    abcd ef   ')