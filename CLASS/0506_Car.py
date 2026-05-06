class Car:
    name = ''
    speed = 0

    def __init__(self, name, speed): #기본값이 있으면..
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
    
    def speedUp(self, value): #speed up 기능 추가
        self.speed += value

    def speedDown(self, value):
        self.speed -= value


    def __str__(self):
        return '{}의 속도는 {}입니다'.format(self.name, self.speed)

car1 = Car('민다영',180) #여기서 car1 : 인스턴스 변
car2 = Car('벤츠', 30)
car1.speedDown(40)
car2.speedUp(10)

#이게 어떻게 작동하는 지 이해하기
print("%s의 현재 속도는 %d입니다." % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." % (car2.getName(), car2.getSpeed()))

