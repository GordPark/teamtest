import requests
import random

def get_lotto(userinput):
  result = {"drwNo":0,"winningnum":{},"bonusnum":0}

  lottourl = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={userinput}'
  result["drwNo"] = userinput # 입력한 회차정보
  response = requests.get(lottourl)
  output = response.json()  

  # 당첨번호 
  result["winningnum"] = {f"drwtNo{i}":output[f"drwtNo{i}"] for i in range(1,7)}

  # 보너스번호
  result["bonusnum"] = output['bnusNo']
  return result

# 랜덤로또 생성
def random_lotto(num):
  new_lotto = []
  while len(new_lotto)<7:
    new_num = random.randint(1, 46) 
    if new_num not in new_lotto:
      new_lotto.append(new_num)
  return new_lotto

# 로또내용저장
def save_file(write):
  with open("lottoinfo.txt",'a') as f:
    f.write(str(write) + '\n')
    


def main():
    while True:
      try:
          userinput = int(input("확인하고 싶은 회차정보를 입력해주세요: ")) # 회차정보를 입력받음
          if userinput <= 0 or userinput > 1109:
              raise ValueError("범위에 해당 하는 수를 입력해주세요!")
          break
      except ValueError:
          raise ValueError("숫자가 아닌 값을 입력하셨습니다!")
    # result = get_lotto(userinput)
    # print(result)
    # print("당첨 번호: ",result["winningnum"])
    # print("보너스 번호: ",result["bonusnum"])

    # 입력받은 회차까지 내용 파일에 저장
    for i in range(1,userinput+1):
      result = get_lotto(i)
      save_file(result)
    # 저장한 파일 확인
    with open("lottoinfo.txt", 'r') as f:
      contents = f.read()
      print(contents)


main()

