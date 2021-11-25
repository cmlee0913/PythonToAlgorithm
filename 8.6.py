# Eercise 8.6
# 처음 입력을 받는다
command = input("Eonter a number : ")
# 입력받은 값을 저장할 리스트를 생성한다
arr = []
# "done"이라는 입력을 받을 때 까지 숫자를 입력한다
while command != "done":
    # 리스트에 숫자들을 저장한다
    arr.append(int(command))
    command = input("Eonter a number : ")
# "done"이 입력되면 반복문이 종료되고 최대, 최소 값이 출력된다     
print("Maximum : ",max(arr), "Minimum :", min(arr))

