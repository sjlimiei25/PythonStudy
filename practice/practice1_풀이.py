# practice1.py
'''
    입력 함수 => input(출력할내용):입력된값
        -> 기본적으로 입력된 값을 문자열 타입 리턴
        ex)  name = input("이름 입력 : ")
'''

# 1. 이름, 성별, 나이, 키 입력받아 출력
#  * 출력 형식 : 이름: xxx, 성별: xx, 나이: xx, 키: xx.xxcm
'''
name = input("이름 : ")
gender = input("성별 : ")
age = input("나이 : ")
height = input("키 : ")

#print(type(int(age)))

print(f"이름: {name}, 성별: {gender}, 나이: {age}, 키: {height}cm")
print()
'''
# 2. 두 정수 입력받아 합, 차, 곱, 몫, 나머지 계산 후 출력
'''
n1 = int(input("첫번째 숫자 : "))
n2 = int(input("두번째 숫자 : "))

print(type(n1))

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} * {n2} = {n1*n2}")
print(f"{n1} // {n2} = {n1//n2}")
print(f"{n1} % {n2} = {n1%n2}")

print()
'''
# 3. 영어 문자열 입력받아 앞 세 글자 출력
'''
data = input("영어 입력 : ")

print("앞 세글자 : ", data[0:3])
print("앞 세글자 : ", data[:3])
print()
'''
# 4. 실수 2개 입력받아 합, 차, 곱, 나누기 출력
'''
f1 = float(input("실수1 입력 : "))
f2 = float(input("실수2 입력 : "))

print(type(f1))

print(f"{f1} + {f2} = {f1+f2}")
print(f"{f1} - {f2} = {f1-f2}")
print(f"{f1} * {f2} = {f1*f2}")
print(f"{f1} / {f2} = {f1/f2}")
'''

# 5. 두 수 입력받아 제곱과 제곱근 계산
#    각각 제곱, 제곱근
'''
n1 = int(input("숫자1 입력 : "))
n2 = int(input("숫자2 입력 : "))

print(f"{n1} 의 제곱 : {n1**2}, 제곱근 : {n1**0.5}")
print(f"{n2} 의 제곱 : {n2**2}, 제곱근 : {n2**0.5}")
'''

# 6. 문자열 입력받아 대문자/소문자/글자 수 출력
'''
data = input("문자열 입력 : ")

print(f"대문자 : {data.upper()}")
print(f"소문자 : {data.lower()}")
print(f"글자수 : {len(data)}")
'''

# 7. 좋아하는 음식 3개 입력받아 리스트로 저장 후 출력
'''
foods = []  # 비어있는 리스트

food1 = input("좋아하는 음식1 : ")
food2 = input("좋아하는 음식2 : ")
food3 = input("좋아하는 음식3 : ")

# foods = [food1, food2, food3]
foods.append(food1)
foods.append(food2)
foods.append(food3)

print("좋아하는 음식 리스트:", foods)
print("첫 번째 음식:", foods[0])
print("마지막 음식:", foods[-1])
foods.sort()    # 기본: 오름차순 정렬
print("오름차순 정렬 : ", foods)
#foods.reverse()  # sort() 후 reverse() 할 경우 내림차순 정렬
foods.sort(reverse=True)    # 내림차순 정렬
print("내림차순 정렬 : ", foods)
print()
'''

# 8. 세 개의 숫자 입력받아 합과 평균 계산 후 출력
# 합 => 모두 더하기
# 평균 => 합 / 개수
'''
n1 = int(input("숫자 1 : "))
n2 = int(input("숫자 2 : "))
n3 = int(input("숫자 3 : "))

total = n1 + n2 + n3
print(f"{n1} + {n2} + {n3} = {total}")
print(f"평균 : {total / 3}")
print(f"평균 : {total // 3}")
'''

# 9. 문자열 입력받아 앞 3글자 + 뒤 2글자 합쳐서 출력
'''
data = input("문자열 입력 : ")

print(data[:3] + data[-2:])
print(data[0:3] + data[-2] + data[-1])
'''

# 10. 문자열 입력받아 대문자로 변환 후, 앞 5글자만 출력
'''
data = input("문자열 : ")

data = data.upper()
print(data[0:5])
print(data[:5])
'''