list = [] # 빈 리스트 선언

while(1):
    Input = input("Enter a number : ") # 숫자 입력
    try:
        ival = float(Input) # 실수인지 확인
        list.append(ival) # 리스트에 추가
    except:
        if (Input == 'done'): # 'done' 인지 확인
            print(max(list), min(list)) # 최대, 최소값 출력
        else:
            print("Invalid input") # 아니면 오류 출력