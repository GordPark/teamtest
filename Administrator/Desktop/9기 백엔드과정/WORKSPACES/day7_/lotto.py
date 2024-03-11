import requests


def main():
    result = {"drwNo":0,"winning_num":{},"bonus_num":0}
    while True:
        try:
            userinput = int(input("확인하고 싶은 회차정보를 입력해주세요: ")) # 회차정보를 입력받음
            if userinput <= 0:
                raise ValueError("0보다 큰 수를 입력해주세요!")
            break
        except ValueError:
            raise ValueError("숫자가 아닌 값을 입력하셨습니다!")
        
    lotto_url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={userinput}'
    print(lotto_url)    # 확인을 위해 url출력
    result["drwNo"] = userinput # 입력한 회차정보
    print(result)

    response = requests.get(lotto_url)
    print(response)
    output = response.json()
    print(output)

    # 당첨번호 
    result["winning_num"] = {f"drwtNo{i}":output[f"drwtNo{i}"] for i in range(1,7)}

    print(result)
    
    # 보너스번호
    result["bonus_num"] = output['bnusNo']
    print(result)

if __name__ == "__main__":
    main()