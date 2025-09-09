# 4_inheritance.py

# 상속 : 부모 클래스의 속성,메소드들을 새로 정의하지 않고 사용할 수 있는 기술

# Animal 클래스 정의
class Animal:
    def eat(self):
        print("간식을 먹습니다.")
    
    def speak(self):
        print("소리를 냅니다.")

# Dog 클래스 정의
# class Dog:
class Dog(Animal):
    '''
    def speak(self):
        print("멍멍~!!")

    def eat(self):
        print("간식을 먹습니다.")
    '''
    def speak(self):        # 오버라이딩(재정의)
        print("멍!!멍!!")

    def play_ball(self):
        print("공을 가지고 놀기!")

# Dog 클래스 생성
d = Dog()
d.play_ball()
d.eat()
d.speak()