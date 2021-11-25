#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Excercise 7.2

# 파일명을 입력받습니다
name = input("Enter the file name")

# 컴퓨터로컬 주소와 이름을 합친 후 읽어들입니다. 줄마다 읽어들이기 위해 readlines()를 사용하였습니다.
uri = 'C:/Users/PH/Desktop/' + name
with open(uri, 'r') as f:
    lanList = f.readlines()
# print(f"lanList : {lanList}")

arr = []
# 만약 X-DSPAM-Confidence: 를 포함하는 라인을 만나면 arr리스트에 저장합니다. 
for lan in lanList:
    if "X-DSPAM-Confidence" in lan:
        arr.append(lan)
# 스팸의 총계를 저장하기 위한 리스트 입니다.        
total_spam = 0

# 해당라인에 소수가 들어있는 부분을 짜르고 소수로 변환 후 저장해 합칩니다
for i in range(len(arr)):
    total_spam += float(arr[i][20:-1])
print("Average spam confidence : ", total_spam / len(arr))

