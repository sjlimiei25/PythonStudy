# practice2.py

# 1. 연도를 입력 받아 윤년인지 아닌지 출력
'''
    * 윤년 판별 기준
      - 연도가 4의 배수이면 윤년
        이때, 100의 배수이면 윤년이 아님
        하지만, 400의 배수이면 윤년

                    4의 배수     100의 배수     400의 배수      윤년 여부
      ex) 2020  =>     O           X             X              O
          1900  =>     O           O             X              X
          2000  =>     O           O             O              O
          2023  =>     X           X             X              X
'''
year = int(input("연도 입력 : "))
'''
if year % 4 == 0:
    # pass
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}년은 윤년입니다.")
        else:
            print(f"{year}년은 평년입니다")
    else:
        print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")
'''
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}년은 윤년입니다")
else:
    print(f"{year}년은 평년입니다")

# 2. 1 ~ 100 까지의 3의 배수 합 출력
total = 0
for n in range(1, 101):
  if n % 3 == 0:  # 배수 판별 : A % B == 0 A가 B의 배수인 경우
    total += n    #total = total + n

print("1부터 100까지 값 중 3의 배수 총 합 : ", total)

# 3. 구구단 출력 (2단 ~ 9단)
'''  **** 출력 형식 ****
    2 x 1 = 2   3 x 1 = 3   4 x 1 = 4   ...  9 x 1 = 9
    2 x 2 = 4   3 x 2 = 6   4 x 2 = 8   ...  9 x 2 = 18
    2 x 3 = 6   3 x 3 = 9   4 x 3 = 12   ...  9 x 3 = 27
    ...
    2 x 9 = 18   3 x 9 = 27   4 x 9 = 36   ...  9 x 9 = 81
'''
# 세로로 출력하기
for i in range(2, 10):      # 단
    for j in range(1, 10):  # 곱해지는 값
      print(f"{i} * {j} = {i*j}")
    print()

# 가로로 출력하기
for j in range(1, 10):      # 곱해지는 값
    for i in range(2, 10):  # 단
      print(f"{i} * {j} = {i*j}", end="\t")
    print()



# 4. 문자열을 입력 받아 길이가 5 이상이면 "길어요" 출력. 
#     그렇지 않으면 입력된 값 출력
data = input("문자열 입력 : ")

length = len(data)
if length >= 5:
  print("길어요")
else:
  print(data)



# 5. 1 ~ 31까지 숫자를 모두 출력하되, 값에 3 또는 6 또는 9가 포함된 경우 "짝👏" 출력
clab_number = [3, 6, 9]
for i in range(1, 32):
  if i < 10:
    # 1,2,"3",4,5,"6",7,8,"9"
    if i in clab_number:
      print("👏", end=" ")
    else:
      print(i, end=" ")
  else:
    # i => 10 ~ 31
    if i % 10 in clab_number or\
        i // 10 in clab_number:
      print("👏", end=" ")
    else:
      print(i, end=" ") 
