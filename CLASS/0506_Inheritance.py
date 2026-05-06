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

class Sedan(Car):
    def speedUp(self, value):
        self.speed += value
        if self.speed > 150:#속도 제한
            self.speed = 150
    def speedDown(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

myCar = Sedan("K5", 50)
print(myCar)

#이게 어떻게 작동하는 지 이해하기
