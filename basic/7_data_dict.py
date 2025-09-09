# 7_data_dict.py

# 딕셔너리 => Map 과 유사
#  특징 => 키-밸류 한 쌍으로 관리. 키값은 중복 허용 x

user = { "name":"홍길동", "age":20, "phone":"010-0000-0000" }
print(user)

print("사용자 이름 : ", user["name"])
print("나이 : ", user.get("age"))

# 데이터 추가
user["hobby"] = "야구보기"
print(user)

print("키값들만 조회 : ", user.keys())
print("밸류값들만 조회 : ", user.values())

# 데이터 삭제
user.pop("phone")
print(user)