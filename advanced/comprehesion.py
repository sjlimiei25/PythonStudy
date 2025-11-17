# advanced/comprehension.py

# 컴프리헨션 : 반복문을 한 줄로 간결하게 표현하는 문법
def practice1():
  numbers = [1, 2, 3, 3, 4, 5]

  # 리스트
  squares = [n**2 for n in numbers]
  print(squares)

  # 셋
  squares_set = {n**2 for n in numbers}
  print(squares_set)

  # 딕셔너리
  words = ['emotion', 'happy', 'gloomy']
  # ==> {'emotion': 7, 'happy': 5, 'gloomy': 6}
  words_len = {w:len(w) for w in words }
  print(words_len)

# practice1()

def practice2():
  #  조건을 추가하여 컴프리헨션 적용
  numbers = [1,2,3,3,4,5]

  # 리스트에 짝수에 해당하는 값의 제곱으로 저장
  even_squares = [n**2 for n in numbers if n % 2 == 0]
  print(even_squares)
  
  # 홀수의 값은 원래 값 그대로,,
  data = [n**2 if n % 2 == 0 else n for n in numbers]
  print(data)

  words = ['animals', 'foods', 'tools', 'happy', 'sad']
  # 위 단어들 중 글자수가 5자인 항목만 대문자로 변경, 
  #    조건에 해당되지 않는 경우 원래 값 그대로 사용
  # trans_words = [w for w in words]
  # trans_words = [w.upper() for w in words]
  # trans_words = [w.upper() for w in words if len(w) == 5]
  
  trans_words = [w.upper() if len(w) == 5 else w for w in words]
  print(trans_words)

# practice2()

def practice3():
  '''
      *  텍스트 데이터 전처리
        : 사용자가 입력한 문장 목록에서 
              양쪽 공백 제거, -> strip()
              소문자로 통일,  -> lower()
              빈 문자열 제거
  '''
  sentences = []
  while True:
    stc = input('문장을 입력하세요..(종료:-1) : ')
    if stc.strip() == '-1': 
      break
    sentences.append(stc)

  print(f'처리 전 데이터 ... {sentences}')

  # 조건에 맞게 리스트 재구성(전처리)
  trans_stc = [s.strip().lower() for s in sentences if s.strip() != '']

  print(f'처리 후 데이터 ... {trans_stc}')

# practice3()

def practice4():
  # 파일명 목록에서 확장자 필터링
  # : 이미지 파일만 추출
  files = ['flower.png', 'sample.txt', 'cat.jpg', 'manual.pdf', 'coffee.jpeg']

  # 이미지 파일명만 저장 => .png, .jpg, .jpeg, ....
  # images = [f for f in files if '.png' in f or '.jpg' in f or '.jpeg' in f]
  images = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
  print(images)

# practice4()

def practice5():
  # 딕셔너리로 데이터 변환
  # : (상품, 가격) 리스트에서 {상품명: 가격+VAT(부가가치세, 10%)} 딕셔너리 생성
  products = [
    ('keyboard', 40000),
    ('mouse', 20000),
    ('monitor', 100000)
  ]

  price_with_vat = {n: int(p*1.1) for n, p in products}
  print(price_with_vat)

# practice5()