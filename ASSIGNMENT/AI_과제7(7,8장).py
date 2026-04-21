#7-1
'''
import datetime
now = datetime.datetime.now()

print("오늘의 날짜:{}년 {}월 {}일".format(now.year, now.month, now.day))

if now.hour <12:
    ampm = "오전"
    hour_12 = now.hour
    if hour_12 == 0:
        hour_12 = 12
else:
    ampm = "오후"
    hour_12 = now.hour - 12
    if hour_12 == 0:
        hour_12 = 12
print("현재시간 : {} {}시 {}분 {}초".format(ampm, hour_12, now.minute, now.second))

#7-2
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2028, 12, 25)
time_gap = xMas - dt.datetime.now()
print('2028년 크리스마스까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))


import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2036, 1, 1)
time_gap = xMas - dt.datetime.now()
print('2036년 새해까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))


import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 10, 19)
time_gap = xMas - dt.datetime.now()
print('2026년 생일까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))

#7-3
import datetime as dt
print('오늘 =', dt.datetime.now())
hundred = dt.timedelta(days = 1000)
plus100day = dt.datetime.now() + hundred
print('1000일 후 =', plus100day)

from datetime import datetime, timedelta
year, month, day = map(int, input("처음으로 사귄 연도와 월, 일을 입력하시오: ").split())
start_date = datetime(year, month, day)
day_100 = start_date + timedelta(days=100)
print(f"100일 기념일은 : {day_100.year}년 {day_100.month}월 {day_100.day}일입니다.")


#7-4
import math

for i in range(2,11):
    print(f"4**{i} = {math.pow(4,i)}") # pow(4,i) : 4의 i

    
import math

for degree in range(0, 181, 10):
    radian = math.radians(degree) #math.radians() : 라디안 : 각도 * (파이/180) 이거 계
    print(f"{degree} degree = {radian:.3f} radian")

import math
for degree in range(0,181,10):
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    print(f"sin({degree:3d}) = {sin_value:.2f}")

#7-5
import random
result = []
for _ in range(3):
    num = random.randrange(0, 101, 5)
    result.append(num)
print("0에서 100 이하의 정수 중에서 5의 배수")
print(result)
    
import random
numbers = range(1, 11)
result = random.sample(numbers, 3)
print(f"1에서 10 사이의 임의의 정수 : {result}")

#7-7
import turtle

t = turtle.Turtle()
t.shape("turtle")

for _ in range(3):
    t.forward(100) 
    t.left(120)  

for _ in range(3):
    t.forward(200)
    t.left(120)    

turtle.done()
#???
import turtle

t = turtle.Turtle()
t.shape("turtle")

lengths = [100, 200, 300]

for l in lengths:
    for _ in range(3):
        t.forward(l)
        t.left(120)

turtle.done()
'''
#8-1
#1. IndexError
#2. ValueError
#3. TypeError
try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print(f"1번 결과: {e}")

# 2. ValueError 확인
try:
    n = int('20%')
except Exception as e:
    print(f"2번 결과: {e}")

# 3. TypeError 확인
try:
    a = 100 + '200'
except Exception as e:
    print(f"3번 결과: {e}")

    
#8-2
try:
    result = 10 * (30 / 0)
except ZeroDivisionError:
    print("오류: 0으로 나눌 수 없습니다.")

try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print("오류: 유효한 정수를 입력해야 합니다.")

    import sys

try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print("오류: 해당 파일을 찾을 수 없습니다.")


#8-3 
a = [1, 2, 3, 4, 5]
order_names = ["첫", "두", "세", "네", "다섯"]

try:
    choice = int(input("a의 요소를 하나 선택하시오 : "))
    idx = a.index(choice)
    print(f"{choice} 은(는) {order_names[idx]} 번째 요소입니다.")
except:
    print("오류 : 입력 값이 정수나 실수가 아님")
