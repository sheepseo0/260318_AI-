import json

'''
# 주소록 데이터
addressbook = { 
    "양서영" : "01074432538", 
    "민다영" : "01022532236"
} #딕셔너리 변수로 정보 저장

#1. 파일로 저장 
with open("addressbook.json", "w", encoding = "utf-8") as f: #하드디스크에 방을 하나 만들어서
    json.dump(addressbook, f, ensure_ascii = False, indent = 4) #파일에다가 저 정보를 저장한다.

print("주소록이 저장되었습니다.")
'''

#2. 파일에서 다시 불러오기
with open("addressbook.json", "r", encoding = "utf-8") as f: 
    addressbook = json.load(f) 

print("불러온 주소록:", addressbook) 
print("양서영 번호:", addressbook["양서영"])

