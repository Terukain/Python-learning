#1:想一下以下变量分别是什么。输出结果，看看是否符合你的判断。
a = 'hello,world'
b = 1.4145
c = (1 != 2)
d = (True and False)
e = (True or False)
print(a,b,c,d,e)

#2:通过字符串格式化在同一行输出 a，b，c，d，e，其中浮点数要求只保留两位小数。输出示例：
#a:hello,word; b:1.41; c:True; d:False; e:True
print('a:%s;b:%.2f;c:%s;d:%s;e:%s'%(a,b,c,d,e))
#3:定义一个字符串，使其输出结果如下图所示
print(''''hello,world'\n\\"hello,world"''')
