class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        print(self.length, "길이의 선이 생성되었습니다.")

    def __del__(self):
        print(self.length, "길이의 선이 삭제되었습니다.")

    def __repr__(self):
        return '선의 길이:'+str(self.length)

    def __add__(self, other):
        return self.length + other.length

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.length == other.length


myline1 = Line(100)
myline2 = Line(200)

print(myline1)
