# 2_loop.py
import random

# 반복문
'''
    * 기본 구조

        # 반복 가능한 객체 : 리스트, 튜플, 세트, 딕셔너리, 문자열, range
        for 변수명 in 반복가능객체: 
            반복할 내용

    * range 함수
        range(stop) : 0부터 stop-1 까지 1씩 증가하는 숫자들을 생성 (시퀀스)
        range(start, stop) : start부터 stop-1까지 1씩 증가하는 시퀀스 생성
        range(start, stop, step) : start부터 stop-1까지 step씩 증가하는 시퀀스 생성
'''
'''
# * 1 ~ 10까지 출력
for i in range(1,11):
    print(i, end=" ")
print()

# * 리스트에 저장되어 있는 요소들을 출력
colors = ["red", "sky blue", "cyan"]
for c in colors:
    print(c, end=" ")
print()
'''
# while 문
'''
    * 기본 구조

        while 조건식:
            반복할 내용
'''
# * while문을 사용하여 1 ~ 10 출력
'''
n = 1
while n <= 10:
    print(n, end=" ")
    # n++ # SyntaxError 오류 발생!!
    # n = n + 1
    n += 1
'''
# * while문을 사용하여 
#       사용자 입력이 exit인 경우 종료
#               그렇지 않으면 입력값 출력
'''
while True:
    data = input("단어 입력하세요 (exit을 입력할 경우 종료) : ")

    if data.lower() == 'exit':  # 파이썬에서는 문자열의 값 비교 가능!
        print("프로그램 종료")
        break

    print(f"입력된 값 : {data}")
'''
# * 업앤다운 게임
# 1 ~ 100 사이의 숫자 맞추기 게임
'''
    ex) 정답 = 55
        사용자 : 20 Up!
        사용자 : 60 Down!
        ...
        사용자 : 55 정답!!
'''
'''
print("*======= Up & Down =======*")

answer = random.randint(1,100)

while True:
    # user = int(input("입력 : "))
    user = input("입력 : ")

    # isdigit() : 값이 정수로 되어있는지 아닌지 판별
    if not user.isdigit():
        print("숫자만 입력해주세요 --- ")
        continue

    user = int(user)

    if user == answer:
        print("정답입니다 *^^*")
        break
    elif user > answer:
        print("Down!!")
    else:   # user < answer
        print("Up!!")
'''
#---------------------------------------------------
# * 가위바위보 ---> 삼세판!        

# 3번 반복
# for i in range(1, 4):
#     print(f"round {i}")
# ----------------------
# n = 1
# while n <= 3:
#     print(f"round {n}")

#     n+=1

rps = ["가위", "바위", "보"]
# (사용자값, 컴퓨터값)
win_case = [("가위","보"), ("바위","가위"), ("보","바위")]

r = 1; win_count=0
# r, win_count = 1, 0
while r <= 3:
    print(f"* ======== ROUND {r} ========= *")
    user = input("가위, 바위, 보 중 하나만 선택 : ")

    if user in rps:
        computer = random.choice(rps)

        print(f"사용자 : {user} \t 컴퓨터 : {computer}")

        if user == computer:
            print("비겼습니다!")
        elif (user, computer) in win_case:
            print("이겼습니다!!")
            win_count+=1
        else:
            print("졌습니다 T.T")
        
        r+=1
    else:
        print("잘못 입력했습니다...")

print(f"{win_count}번 이겼습니다 ~~")