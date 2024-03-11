def write_file_out(path):
  try:
    with open(path, 'w') as f:  # 경로의 파일을 읽음
      print("모듈에 쓰기 함수")
      f.write("new contents")
  except FileNotFoundError:   # 파일찾을수 없을 때 
    print("파일을 읽을 수 없습니다!")



print("file_writer의 __name__입니다 :",__name__)
if __name__=='__main__':
  write_file_out()
