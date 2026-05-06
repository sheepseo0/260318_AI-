class Cat: 
    # 생성자 혹은 초기화 메소드라 한다
    def __init__(self, name, color='흰색'):
        self.name = name # name이라는 인스턴스 변수를 생성
        self.color = color # color라는 인스턴스 변수를 생성
    # 고양이의 정보를 출력하는 메소드
    def meow(self):
        print('내이름은 {}, 색깔은 {}, 야옹 야옹~~'.format(self.name, self.color))
        
nabi = Cat('나비', '검정색') # nabi 인스턴스 생성
nero = Cat('네로', '흰색') # nero 인스턴스 생성
mimi = Cat('미미', '갈색') # mini 인스턴스 생성

nabi.meow()
nero.meow()
mimi.meow()
