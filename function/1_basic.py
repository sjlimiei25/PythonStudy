# 1_basic.py
import random

# 매개변수가 없고, 반환 값도 없는 함수
def f1():
    print("나는 f1 함수야")
    print("전달받는 값도 없고, 돌려줄 값도 없어")

# f1()

# 매개변수가 있고, 반환값이 없는 함수
def f2(message):
    print("나는 f2 함수야")
    print("전달된 값을 가지고 어떠한 기능을 수행할 수 있어")
    print(f"*** {message}")

# f2("전달되는 값이야~~~")
# f2("Happy")

# 매개변수가 없고, 반환 값이 있는 함수
def f3():
    print("나는 f3 함수야")
    print("전달받는 값은 없고, 주기만 할거야!")
    return random.randint(1, 100)

# f3()  # => 전달된 값을 사용하지 않음!
# result = f3()
# print("f3 함수가 전달해준 값 ", result)

# 매개변수, 반환 값이 모두 있는 함수
def add(a, b):
    # 함수 첫 줄에 도움말 표시
    '''
        전달받은 두 수의 합을 구하는 함수

        Args:
            a : 첫번째 정수
            b : 두번째 정수
        
        Returns:
            a + b : 두 수의 합
    '''
    print("나는 add 함수야")
    print("전달 받은 두 수를 합해서 돌려줄게")
    return a + b

result2 = add(5, 10)
print("add 함수가 돌려준 값 ", result2)