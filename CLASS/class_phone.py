class phone:
    def __init__ (self, phone, brand, battery):
        self.phone = phone
        self.brand = brand
        self.battery = battery

    def __str__(self): #str? 민수를 프린트해라 하면 이 함수로 옴
        return "이름 : {}, 배터리 : {}".format(self__phone, self__battery)#__ 이거 하면 없다고 나옴?? 왜야        
    def use(self, minutes):
        self.battery -= 0.5*minutes
        print(f"{self.phone}사용 후 배터리:{self.battery}")

    def charge(self, minutes):
        self.battery += minutes
        print(f"{self.phone}사용 후 배터리:{self.battery}")

        if self.battery == 100:
            pass 

서영 = phone('아이폰15', 'Apple', 43)
다연 = phone('아이폰16pro', 'Apple',100)

print(다연.phone)
서영.use(30)
다연.charge(100)

print(서영)
print(서영.__phone) #이렇게 하면 밖에서 안 보이게 암호화 한 것 캡슐화!
#use, chare 함수 만들자!
#use 역할 : use(minutes) battery -= 0.5*minutes
#init는 뭐지?
#charge 역할 : charge(minutes) battery += minutes
#class안에선 무조건 self 사용해야함
#30분 사용하면 남은 배터리는 얼마인지 나오게

#9.6 문자열화 메소드
'''
메소드 = 클래스 함수다?
__init__: 클래스의 초기화 함수
'''
