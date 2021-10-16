def computegrade(Score): # 함수 선언
    # 점수에 따른 리턴값
    if 1 >= Score and Score >= 0.9:
	    return print("A")
    elif 0.9 > Score and Score >= 0.8:
	    return print("B")
    elif 0.8 > Score and Score >= 0.7:
	    return print("C")
    elif 0.7 > Score and Score >= 0.6:
	    return print("D")
    elif 0.6 > Score and Score >= 0:
	    return print("F")
    else: # 점수 이외에 값을 입력 시
	    return print("Bad score")

while(1): # 무한 루프 생성
	computegrade(float(input("Enter score : "))) # 스코어 입력