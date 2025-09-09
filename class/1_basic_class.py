# 1_basic_class.py

'''
[클래스 정의]

class 클래스명:
    # 생성자
    def __init__(self, 매개변수):
        # 초기 작업 (초기화)

    # 메소드 (클래스 내의 함수)
    def 메소드명(self, 매개변수):
        # 동작할 내용
'''

# Person 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요 저는 {self.name}입니다.")
        print(f"나이는 {self.age}살입니다.")

# Person 객체 생성
p1 = Person("어머니", 20)
p1.introduce()

p2 = Person("아이유", 33)
p2.introduce()