list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']
ss={}
for i in list_s:
    if i not in ss:
        ss[i]=1
    if i in ss:
        ss[i]+=1
print(ss)
