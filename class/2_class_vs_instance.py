# 2_class_vs_instance.py

# 클래스변수 : 모든 객체가 공유할 수 있는 변수
# 인스턴스변수 : 객체마다 다른 값을 가지는 변수

# Employee 클래스 정의
class Employee:
    # 클래스 변수. 모든 Employee 객체가 공유
    company = 'KH Company'

    def __init__(self, name, dept):
        # 인스턴스 변수. 각 객체마다 다른 값
        self.name = name
        self.dept = dept

# Employee 객체 생성
e1 = Employee("송치민", "게임개발팀")
e2 = Employee("김성빈", "개발1팀")

print(e1.company, e1.name, e1.dept) # 첫번째 직원 정보
print(e2.company, e2.name, e2.dept) # 두번째 직원 정보

# 클래스 변수 변경
Employee.company = 'KH Corp'
print(e1.company, e1.name)
print(e2.company, e2.name)