# 3_encapsulation.py

# 캡슐화
# : 객체의 속성을 외부에서 직접 접근하지 못하도록 보호하고 (정보은닉)
#   getter/setter 등과 같이 메소드를 통해 간접적으로 접근하도록 하는 것

# Person 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name        # public(공개)   : 어디서든 접근 가능
        self.__age = age        # private(비공개) : 클래스 내에서만 접근 가능

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

# Person 객체 생성
p1 = Person("아이유", 33)
print(p1.name)
# print(p1.__age)     # 오류 발생! AttributeError
print( p1.get_age() )

p1.set_age(20)
print( p1.get_age() )