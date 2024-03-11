# 최대공약수
# 유클리드 호제법


def get_gcd(num1,num2):
  while True:
    if num1 > num2:
      big_num = num1
      small_num = num2
    else:
      big_num = num2
      small_num = num1

    if big_num % small_num == 0:
      gcd = small_num 
      return gcd

    remainder = big_num % small_num
    num1 = small_num  # big_num로 설절 시 무한루프
    num2 = remainder  # small_num도 마찬가지

gcd = 0
user_input1 = int(input("첫번째 숫자를 입력해주세요"))
user_input2 = int(input("두번째 숫자를 입력해주세요"))

gcd = get_gcd(user_input1, user_input2)
print(f"최대공약수는 {gcd}입니다.")