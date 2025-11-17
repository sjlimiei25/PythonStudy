# adavenced/exception.py
def practice1():
  # 예외 처리 기본 구조
  try:
    x = int(input('숫자를 입력하세요 : '))
    result = 10 / x
  except ZeroDivisionError:   # 해당 예외 발생 시 실행할 내용
    print('0으로 나눌 수 없습니다.')
  except ValueError:
    print('숫자만 입력하세요')
  else:   # 예외가 발생되지 않았을 때 실행할 내용
    print(f'연산 결과... {result}')
  finally:
    print('practice1 완료 ----- *')

# practice1()

def practice2():
  numbers = [10, 20, 30]

  try:
    idx = int(input('조회할 인덱스 입력 (0~2):'))
    print(f'---> {numbers[idx]}')
  except IndexError:
    print('잘못된 인덱스 번호입니다.')
  except ValueError:
    print('숫자만 입력해야 합니다.')
  finally:
    print('practice2() 완료------*')

# practice2()

def practice3():
  user = {'name': '임수진', 'age': 20}

  key = input('조회할 데이터의 key 입력 (name/age) : ')
  #print(f'{key} --> {user.get(key)}')
  # => get 함수 이용 시 해당하는 key가 없는 경우 None 반환 -> 조건문 처리

  #    get(키값, 기본값) : 필수 항목(데이터)가 아닌 경우, 기본값으로 처리 가능한 경우
  #    get[키값]         : 필수 항목인 경우, 반드시 데이터가 존재해야 하는 경우, 예외 처리를 해야하는 경우
  try:
    print(f'{key} --> {user[key]}')
  except KeyError:
    print('존재하지 않는 키값입니다.')
  finally:
    print('practice3() ---- 종료 --- *')

# practice3()


# 사용자 정의 예외 => 내가 만든 예외 클래스!
class NegativeNumberError(Exception):
  """ 음수 입력 예외 """
  def __str__(self):
    return f'음수값이 입력되었습니다.'

def practice4():
  # 사용자로부터 숫자를 입력받아, 입력된 값을 출력
  # 단, 음수 입력 시 예외로 처리함.
  try:
    n = int(input('0 이상의 숫자를 입력하세요 : '))
    if n < 0:
      raise NegativeNumberError

    print(f'입력값 : {n}')
  except ValueError:
    print('숫자만 입력하세요')
  except NegativeNumberError as e:
    # print(e)
    print('음수가 입력되었습니다. 0 이상만 입력하세요.')
  finally:
    print('---- practice4() 완료 ----*')

practice4()