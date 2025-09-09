# 2_data_type.py

# 변수 선언
name = '홍길동'
age = 20        # 정수형
height = 172.5  # 실수형
is_student = True       # java => isStudent

print("-- 변수의 타입 확인 --") # 변수에 담겨진 값의 타입
print(name, " : ", type(name))  # str
print(age, ":", type(age))      # int
print(height, ":", type(height))    # float
print(is_student, ":", type(is_student))    # bool

# * 여러 변수 동시 선언 *
x, y, z = 10, 5.5, "Hi"
print(x, y, z)
print(x, ":", type(x))
print(y, ":", type(y))
print(z, ":", type(z))
print()

# 타입 변환

# 문자열 -> 정수
str1 = "123"
i1 = int(str1)     # i1 = "123" => i1 = 123
print("str1->i1 : ", i1, type(i1))

# 문자열 -> 실수
str2 = "3.141592"
f1 = float(str2)    # f1 = "3.1415" => f1 = 3.1415
print("str2->f1 : ", f1, type(f1))

# 실수 -> 문자열
# f1 = 3.141592
str3 = str(f1)  # 3.141592 -> "3.141592"
print("f1->str3 : ", str3, type(str3))

# 정수 -> 실수
i2 = 55
f2 = float(i2)  # 55 -> 55.0
print("i2 -> f2 : ", f2, type(f2))

# 실수 -> 정수
f3 = 9.99
i3 = int(f3)
print("f3 -> i3 : ", i3, type(i3))  # 소숫점 버림 처리됨!

# 문자열 -> 불리언(논리)
str4 = "True"
b1 = bool(str4)
print("str4 -> b1 : ", b1, type(b1))

# 숫자 -> 불리언
i4 = 0
b2 = bool(i4)
print("i4 -> b2 : ", b2, type(b2))

print(bool(1))
print(bool(55))
# 정수 -> 불리언 변환 시 0인 경우 False 그 외에는 True
