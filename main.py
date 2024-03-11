# 팀 브런치 사칙연산
from divide import divide
import subtraction
import add
import doble

# go calculator
sign = input("계산기 : [+, /, *, -]: ")
if sign == '+':
    add.add()
elif sign == '-':
    subtraction.subtraction()
elif sign == '*':
    doble.doble()
elif sign == '/':
    divide()


