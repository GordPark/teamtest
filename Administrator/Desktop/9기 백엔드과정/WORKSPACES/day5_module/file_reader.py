def read_file_out(path):
  try:
    with open(path, 'r') as f:  # 경로의 파일을 읽음
      print("모듈에 있는 함수")
      print(f.read())
  except FileNotFoundError:   # 파일찾을수 없을 때 
    print("파일을 읽을 수 없습니다!")



print("file_reader의 __name__입니다 :",__name__)
if __name__=='__main__':
  read_file_out()
