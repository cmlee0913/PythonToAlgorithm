while(1):
	Score = float(input("Enter score : "))
	
	if 1 >= Score and Score >= 0.9:
		print("A")
	elif 0.9 > Score and Score >= 0.8:
		print("B")
	elif 0.8 > Score and Score >= 0.7:
		print("C")
	elif 0.7 > Score and Score >= 0.6:
		print("D")
	elif 0.6 > Score and Score >= 0:
		print("F")
	else:
		print("Bad score")
