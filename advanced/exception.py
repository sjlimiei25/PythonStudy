# adavenced/exception.py
def practice1():
  # 예외 처리 기본 구조

  x = int(input('숫자를 입력하세요 : '))
  try:
    result = 10 / x
  except ZeroDivisionError:   # 해당 예외 발생 시 실행할 내용
    print('0으로 나눌 수 없습니다.')
  else:   # 예외가 발생되지 않았을 때 실행할 내용
    print(f'연산 결과... {result}')
  finally:
    print('practice1 완료 ----- *')

practice1()