#리스트 자료형
'''
#LAB 5-1 리스트 생성
#(1)
even_list = [2,4,6,8,10]
print(even_list)

#(2)
list1 = list(range(2,12,2))
print(list1)

#(3)
nations = ['Korea','China','India','Nepal']
print("nations = ",nations)

#(4)
friends = ['철수','길동','영수','지민']
print("friends = ",friends)

#(5)
string = list('XYZ') 
print(string)


#LAB 5-2
#(1)
prime_list = [2,3,5,7]
print("prime_list의 첫 원소:", prime_list[0])

#(2)
print("prime_list의 마지막 원소:", prime_list[3])

#(3)
print("prime_list의 마지막 원소:", prime_list[-1])

#(4)
nations = ['Korea','China','India','Nepal']
print("nations의 첫 원소:", nations[0])

#(5)
print("nations의 마지막 원소:", nations[-1])

#(6)
print("nations의 마지막 원소:", nations[len(nations)-1])

#LAB 5-3
#(1)
prime_list = [2,3,5,7]
prime_list.append(11)
print(prime_list)

#(2)
prime_list = [2,3,5,7,11]
prime_list.remove(3)
print(prime_list)

#(3)
nations = ['Korea','China','India','Nepal']
nations.append('Russia')
print("추가 후 국가 목록:", nations)

#(4)
if 'Korea' in nations:
    print('Korea 는(은) 국가 목록에 있습니다.')
else:
    print('Korea 는(은) 국가 목록에 없습니다.')

if 'Malaysia' in nations:
    print('Malaysia 는(은) 국가 목록에 있습니다.')
else:
    print('Malaysia 는(은) 국가 목록에 없습니다.')
'''

#LAB 5-4 : 리스트의 내장(min(), max(), sum(), len()) 함수
#(1)
prime_list = [2,3,5,7]
print("1에서 10까지의 소수 :", prime_list)
print("최솟값:", min(prime_list))
print("최댓값:", max(prime_list))
print("합계:", sum(prime_list))
print("평균", len(prime_list))

#(2)
nations = ['Korea','China','Russia','Malaysia']
print("국가 목록 :", nations)
print("사전에 가장 먼저 나오는 나라:", min(nations))
print("사전에 가장 뒤에 나오는 나라:", max(nations))


#LAB 5-5
#(1)
a = [1,2,3]
b = [10,20,30]
a.append(b)
a
#>>> [1, 2, 3, [10, 20, 30]]
#>>> [1, 2, 3, 10, 20, 30]

#(2)
nlist = [1,2,3,4,5,6,7,8,9,10]
print("nlist=", nlist)
#>>> nlist= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#(3)
nlist.insert(0, 0)
print(f"3번 결과: nlist = {nlist}")

#(4)
nlist.reverse()
print(f"4번 결과: nlist = {nlist}")

#(5)
last_element = nlist.pop()
print(f"5번 결과: 마지막 원소 = {last_element}")
print(f"nlist = {nlist}")

#LAB 5-6
n = int(input("반복할 정수를 입력하시오 : "))
base_list = [1, 2, 3]
result_list = base_list * n
print(result_list)

#LAB 5-7
#(1)
n_list = list(range(15))
print("n_list =", n_list)

#(2)
s_list1 = n_list[0:5]
s_list2 = n_list[5:11]
s_list3 = n_list[11:15]
s_list4 = n_list[2:11:2]
s_list5 = n_list[10:5:-1]
s_list6 = n_list[10:1:-2]

print("s_list1 =", s_list1)
print("s_list2 =", s_list2)
print("s_list3 =", s_list3)
print("s_list4 =", s_list4)
print("s_list5 =", s_list5)
print("s_list6 =", s_list6)
