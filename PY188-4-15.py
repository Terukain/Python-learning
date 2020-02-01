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

