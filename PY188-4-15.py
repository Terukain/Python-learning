#1. if条件判断
money = 88

# 当 money 的值大于 100 时，输出 "rich"
# 否则，输出 "poor"

if money>100:
    print("rich")
else:
    print("poor")




#3. BMI 计算器

print('BMI Calculaion:')
hight=float(input('plese input your hight(m):'))
weight=float(input('plese input your weight(kg):'))
BMI=weight/(hight*hight)
print('Your BMI:%.2f'%(BMI))
if BMI<18.5:
    print('体重偏轻')
elif BMI >= 24:
    print('体重偏重')
else:
    print('体重正常')

