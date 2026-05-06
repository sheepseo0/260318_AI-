'''
student1 = {'name':'민수','score':85}
student2 = {'name':'지영','score':92}

def get_grade(student):
    if student['score'] >= 90:
        return 'A'
    elif student['score'] >= 80:
        return 'B'
    else:
        return 'C'

print(get_grade(student1))
print(get_grade(student2))
'''


class Student: #Student라는 클래스를 만들었다
    def __init__ (self, name, score):
        self.name = name
        self.score = score

    def get_grade(self): #인풋이 self
        if self.score >= 90:
            return"A"
        elif self.score >= 80:
            return"B"

민수 = Student('민수',85) #민수라는 변수가 __init__, get_grade 라는 변수를 가지게 됨
지영 = Student('지영',92) #이런 식으로 정보 저장 가능

print(민수.get_grade())
print(지영.get_grade())


'''#이게 의미하는 게 뭐냐?
민수.name = name
민수.score = score

이게 딕셔너리로 한 위에 보다 훨씬 간단하다
Class : 확장성이 높

여기서 지영이라는 student 클래스를 하나 더 만들려면?
'''
