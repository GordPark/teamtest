# 파일에서 데이터를 읽는 함수
def read_data(file_path):
    with open(file_path, 'r',encoding='cp949') as file:
        data = file.read()
    return data