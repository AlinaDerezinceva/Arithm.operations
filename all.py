import math
a = float(input('Введите a: '))

z1 = (math.sin(2)*a+math.sin(5)*a-math.sin(3)*a)/(math.cos(a)+1-2*math.sin(2)**2*2*a)

print(f'z1={z1}')
