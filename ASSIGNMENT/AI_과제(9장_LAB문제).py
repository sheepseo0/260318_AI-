#LAB 9-1
#1번 답 : 100, 20000, 2.0
    # 1번 확인
print((200).__sub__(100))
print((200).__mul__(100))
print((200).__truediv__(100))


#2번 답 : 40
    # 2번 확인
print([10, 20, 30, 40].pop())

#3번 답 : keys(), get() - 이 둘은 딕셔너리 객체에서 사용하는 메소드.

#4번 답 : ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
#5번 결과 : ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    # 4, 5번 확인
print(dir(int))
print(dir(list))

#LAB 9-2
    #1-a. 객체 지향 프로그래밍 : OPP, 잘 설계된 클래스를 이용해 객체를 생성하는 것, 실제로 상호작용하는 객체를 만들어 프로그램에 적용시키는 방법
    #1-b. 절차적 프로그래밍 : 데이터와 함수가 분리된 것, 코드의 규모가 커지면 어려워짐
    #1-c. 그래픽 사용자 인터페이스 : 명령어를 직접 치는 대신, 화면의 아이콘과 버튼을 마우스로 클릭하며 컴퓨터와 소통하는 방식
    #2. 데이터를 중심으로 묶는 것 (객체 지향), 순서대로 처리하는 것 (절차적)

#LAB 9-3
    #1. 클래스 : 프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체, 객체의 설계도/틀/청사진
    #2. 객체 : 클래스라는 틀을 통해 구현된 실제 데이
    #3. 인스턴스 : 클래스로부터 만들어지는 각각의 개별적인 객체, 서로 다른 인스턴스는 서로 다른 속성 값 가질 수 있음
    #4. 클래스의 속성 : 클래스 내부에 선언된 변수
    #5. 클래스의 동작 : 클래스 내부에 정의된 함수

#LAB 9-4
class Dog:
    def bark(self):
        print("멍멍~~")
my_dog = Dog()
my_dog.bark()

#LAB 9-5
class Dog:
    def __init__(self, name): 
        self.name = name
    def bark(self):
        print("멍멍~~")
my_dog = Dog('Jindo')
my_dog.bark()

#LAB 9-6
class Dog:
    def __init__(self, name): 
        self.name = name

    def __str__(self):
        return f"Dog(name = {self.name})"
        
        
my_dog = Dog('Jindo')

print('my Dog의 정보 :', my_dog)

#LAB 9-7
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is nit m')
# 결과 : n is m

#LAB 9-8
#1.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print(f'v1 * v2 = {v1 * v2}')
print(f'v1 / v2 = {v1 / v2}')

#2.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(10, 20)
print(f'-v1 = {-v1}')

#LAB 9-9
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude_sq(self):
        return self.x**2 + self.y**2

    def __gt__(self, other):
        return self.magnitude_sq() > other.magnitude_sq()

    def __ge__(self, other):
        return self.magnitude_sq() >= other.magnitude_sq()

    def __lt__(self, other):
        return self.magnitude_sq() < other.magnitude_sq()

    def __le__(self, other):
        return self.magnitude_sq() <= other.magnitude_sq()

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print(f'v1 > v2 = {v1 > v2}')
print(f'v1 >= v2 = {v1 >= v2}')
print(f'v1 < v2 = {v1 < v2}')
print(f'v1 <= v2 = {v1 <= v2}')

#LAB 9-10
#1.
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])
#1. 결과 값
#>>> {'width': 100, 'height': 200}
#>>> 100

#2.
class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
#2. 결과값
#>>> {'_Rect__width': 100, '_Rect__height': 200}
#>>> 100
