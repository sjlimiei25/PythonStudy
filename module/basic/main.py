# module/basic/main.py

# main.py : 시작점. 실행되는 모듈.

import calc
# 같은 경로에 있는 모듈 calc를 import!

result1 = calc.add(10, 5)
print(result1)

result2 = calc.subtract(20, 5)
print(result2)

# __pycache__
# : 파이썬이 모듈을 실행할 때 자동으로 생성하는 폴더
# : 바이트코드(.pyc) 파일이 있음
#   -> 자동으로 생성되는 캐시 파일로 삭제해도 문제 없음!
#      개발 시 속도 향상을 위해 존재 ( 자바에서 .class 파일과 유사 )