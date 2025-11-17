# advanced/file_io.py
file_name = 'my_songs.txt'

# 파일 쓰기 (output)
with open(file_name, 'w', encoding='utf-8') as f:
  f.write('Happy\n')
  f.write('Welcome to the black parade\n')
  f.write('take cover\n')

# 파일 읽기 (input)
with open(file_name, 'r', encoding='utf-8') as f:
  # print(f.read())
  
  '''
  print(f.readline())
  print(f.readline())
  print(f.readline())

  print(f.readline() == '') # 없는 데이터...
  '''
  while True:
    data = f.readline()

    # if data == '': break
    if not data: break

    print(data.strip())
  print('*--- 파일 읽기 완료 ---*')


# origin.txt 파일 내용을 copy.txt 파일에 복사하기
# contents = ''   # 한번에 읽어서 저장한 경우
contents = []
with open('origin.txt', 'r', encoding='utf-8') as f:
  # contents = f.read()
  while True:
    data = f.readline()
    if not data: break

    contents.append(data)

with open('copy2.txt', 'w', encoding='utf-8') as f:
  # f.write(contents)
  f.writelines(contents)