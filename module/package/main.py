# module/package/main.py

# from 패키지명 import 모듈명, ...
'''
from calculator import calc, utils
# import calculator.calc

result = calc.add(10, 5)
utils.show_result(result)
'''

# init 파일 설정 후
from calculator import add, subtract, show_result

result = add(10, 30)
show_result(result)

# 변경
