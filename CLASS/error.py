while(True):
    try:
        a, b = input('두 수를 입력하시오: ').split()
        result = int(a) / int(b)
        print('{}/{} = {}'.format(a, b, result))
        break
    except:
        print('수가 정확한지 확인하세요.')

str3 = input("3개의 숫자를 입력하세요~").split() #하나의 문자를 쪼개줌
istr3 = list(map(int,str3))
print(str3)
     
#리스트? map?

str3 = map(int(input("3개의 숫자를 입력하세요~").split())) #하나의 문자를 쪼개줌
print(str3)
