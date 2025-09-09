# 1_condition.py
import random

# 1. 조건문

'''
    * if 문 구조

        if 조건식:
            조건을 만족하는 경우 실행할 내용
        elif 조건식2:
            조건을 만족하지 않고, 조건2를 만족하는 경우 실행할 내용
        else:
            모든 조건을 만족하지 않는 경우 실행할 내용

'''
# * 숫자를 입력 받아 짝수/홀수 판별
#   짝수 판별 : 값 % 2 == 0
'''
num = int(input("숫자 입력 : "))

if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")
'''

# * 나이를 입력받아 성인 여부 출력 (19세 이상을 성인으로 판단)
'''
age = int(input("나이 : "))

if age >= 0:
    if age >= 19:
        print("성인입니다.")
    else:
        print("미성년자입니다.")
else:
    print("나이는 음수가 될 수 없습니다.")
'''

# * 가위바위보 게임 (단판)
'''
    사용자에게 가위, 바위, 보 중에 하나를 입력받고
    컴퓨터는 랜덤하게 하나를 선택한다.

    두 개의 값을 비교하여 승패를 결정.

    승 ) 사용자: 가위, 컴퓨터:보 / 사용자: 바위, 컴퓨터: 가위
        / 사용자: 보, 컴퓨터: 바위
    패 ) 승의 반대 상황!
    비김 ) 같은 경우
    --------------------------
    랜덤값 추출 : random 모듈 사용
                => 모듈: 미리 만들어져 있는 기능(파일)

    * import random 추가해야 함!

    random.random() : 0 이상 1 미만의 실수 (Math.random() 유사)
    random.randint(start, end) : start 이상 end 이하의 정수 (Random 유사)
    random.choice(시퀀스) : 시퀀스(리스트, 문자열 등)에서 임의의 요소(데이터) 선택
'''
'''
rps = ["가위", "바위", "보"]

user = input("가위, 바위, 보 중 하나만 선택 : ")

# if rps.index(user) >= 0:       # 존재하지 않는 경우 오류 발생 ValueError!
if user in rps: # 리스트(rps) 내에 데이터(user)가 있으면 True, 없으면 False
    # 가위, 바위, 보 중 선택한 경우
    computer = random.choice(rps)

    print(f"사용자 : {user}\t 컴퓨터 : {computer}")

    if user == computer:
        print("비겼습니다.")
    elif user == "가위" and computer == "보" or \
        user == "바위" and computer == "가위" or \
        user == "보" and computer == "바위":
        print("이겼습니다.")
    else:
        print("졌습니다.")
else:
    print("잘못 입력했습니다.")          
'''

rps = ["가위", "바위", "보"]
# (사용자값, 컴퓨터값)
win_case = [("가위","보"), ("바위","가위"), ("보","바위")]

user = input("가위, 바위, 보 중 하나만 선택 : ")

if user in rps:
    computer = random.choice(rps)

    print(f"사용자 : {user} \t 컴퓨터 : {computer}")

    if user == computer:
        print("비겼습니다!")
    elif (user, computer) in win_case:
        print("이겼습니다!!")
    else:
        print("졌습니다 T.T")
else:
    print("잘못 입력했습니다...")


# == if 문 한 줄로 표현 ==
'''
    자바에서의 삼항 연산자와 유사!

    참일 때 사용할 값 if 조건 else 거짓일 때 사용할 값
'''
x = 10, result = ''
if x % 2 == 0:
    result = '짝수'
else:
    result = '홀수'

x = 10
result = '짝수' if x % 2 == 0 else '홀수'