#202412705 양서영
#LAB 6-1
#(1)
capital_dic = {"Korea":"Soeul","China":"Beijing","USA":"Washington DC"}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

#(2)
fruits_dic={"apple":5000,"banana":4000,"grape":5300,"melon":6500}

for fruit in fruits_dic:
    print(f"{fruit}의 가격은 {fruits_dic[fruit]}원입니다.")


#LAB 6-2
#1~3
person = {"이름":"홍길동","나이":26,"몸무게":82}
person['특기']='분신술'
person['아버지']='홍판서'
del person['나이']
print(person)

#LAB 6-3
capital_dic = {"Korea":"Soeul","China":"Beijing","USA":"Washington DC"}
'Korea' in capital_dic
True
'China' in capital_dic
True
'Indonesia' in capital_dic
False
'Beijing' in capital_dic
False

#LAB 6-4
fruits_dic={"apple":6000,"banana":5000,"orange":7000,"melon":3000}
print(fruits_dic.keys())
print(fruits_dic.values())
print(fruits_dic.pop('apple')) #이러면 value 방출하고 삭제됨
print(fruits_dic.clear())

#LAB 6-5
fruits_dic={"apple":6000,"banana":5000,"orange":7000,"melon":3000}
fruits_list1 = list(fruits_dic.keys()) #딕셔너리의 키 -> 리스트
print(fruits_list1)

fruits_list2 = list(fruits_dic.values()) #딕셔너리의 키 -> 리스트
print(fruits_list2)

a = len(fruits_dic)
print(f"fruits_dic 딕셔너리 항목의 개수:{a}")

while True:
    test = input("확인하고자 하는 과일의 이름 입력:")

    if test in fruits_dic:
        print(f"{test} is in fruits_dic.")
        break
    elif test == "000":
        print("프로그램 종료")
        break
    else:
        print(f"{test} is not in fruits_dic.")
        print("다시 입력하세요!")

#LAB 6-6
#(1)
the_day = (1919,3,1) #이렇게 튜플을 만들었음
year = the_day[0]
month = the_day[1]
day = the_day[2]

print(f"{year}년 {month}월 {day}일은 삼일절입니다.")

#(2)
n_list = [10,20,30]
tuple1 = tuple(n_list)

a = tuple1[0]
b = tuple1[1]
c = tuple1[2]

print("a =",a)
print("b =",b)
print("c =",c)

#LAB 6-7
person = ('홍길동',2019001, 179) #튜플 형성
print("person = ", person)
#튜플 > 리스트 여기서 값 변경 후 다시 튜플로 돌아오기
p_list = list(person)
p_list[1] = 2020003
person = tuple(p_list)

print("학번 변경 후 person = ",person)

#LAB 6-8
#(1)
def square(x,y):
    return x**2, y**2 #이게 튜플로 반환

x = int(input("x 값을 입력하세요:"))
y = int(input("y 값을 입력하세요:"))

x_sq, y_sq = square(x,y)
print("{}제곱 = {}, {}제곱 = {}".format(x, x_sq, y, y_sq))

#(2)
>>>(10,20,30)+(40,50,60)
(10, 20, 30, 40, 50, 60)

#(3)
>>> print('hello'*3)
hellohellohello
>>> print(('hello',)*3)
('hello', 'hello', 'hello')

#LAB 6-9
#(1)
lst = ['apple','mango','banana']
s1 = set(lst)
print(s1)

#(2)
greet = 'Good afternoon'
s2 = set(greet)
print(s2)

#LAB 6-10
s1 = {10,20,30,40}
s2 = {30,40,50,60,70}

print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1^s2)
print(s1.issubset(s2)) #s1이 s2의 부분집합인가?
print(s1.issuperset(s2)) #s1이 s2의 상위집합인가?
print(s1.isdisjoint(s2)) #집합 s1이 s2와 서로소인가?

#LAB 6-11
def product_set(s1, s2):
    result = set()
    
    for a in s1:
        for b in s2:
            result.add((a, b)) 
    
    return result

A = {1, 2}
B = {'A', 'B', 'C'}

print("A×B =", product_set(A, B))
print("B×A =", product_set(B, A))
print("A×A =", product_set(A, A))
print("B×B =", product_set(B, B))










