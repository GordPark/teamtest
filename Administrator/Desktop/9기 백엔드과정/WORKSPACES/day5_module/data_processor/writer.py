# 파일에 데이터를 쓰는 함수
def write_data(data, file_path):
    with open(file_path, 'a') as file:
        file.write(data)