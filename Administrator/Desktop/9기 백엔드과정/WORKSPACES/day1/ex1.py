n = int(input("Enter a number: "))  # 사용자로부터 숫자를 입력 받음
for i in range(1, n+1):
    if i % 3 != 0:
        print(i, end=' ')

