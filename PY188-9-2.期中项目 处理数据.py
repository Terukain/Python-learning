with open("C:/工作/软件/Python/excises/report.txt", 'r', encoding='UTF-8', errors='ignore') as f:
    f.seek(0)
    data1= [line.strip().split() for line in f.readlines()]
#读取文件，另存为删除回车，以空格分隔的字符串
    print(repr(data1))

scorelist = []
for datas in data1[1:]:
    score= []
    score.append(datas[0])
    l=[int(a) for a in datas[1:]]
    score=score+l #把每个人的各科目分数放到当行中
    person_average=sum(l)/len(datas[1:])
    score.append(sum(l))
    score.append(round(person_average,2))#round() 方法返回浮点数 x 的四舍五入值
    scorelist.append(score)
    #print("score: ", score)
    #print("scorelist",scorelist)
rank_scorelist=sorted(scorelist,key=lambda a:a[-2],reverse=True)#按照大小排序
print("rank_scorelist",rank_scorelist)#排名
#写入总分 averagescore和rank


totalscore=[]
for i in range(1,len(scorelist[0])):
    itemaverage=sum([j[i] for j in scorelist])/len(scorelist)
    totalscore.append(round(itemaverage,2))
totalscore.insert(0,"平均分")
#print("totalscore",totalscore)
rank_scorelist.insert(0,totalscore)
#print("rank_scorelist",rank_scorelist)
[rank_scorelist[i].insert(0,i) for i in range(len(rank_scorelist))]#插入排名
for i in rank_scorelist[1:]:
    for j in range(2,len(i)-2):
        if i[j]<60:
            i[j]='不及格'#替换不及格

print("rank_scorelist",rank_scorelist)

firstline=data1[0]
firstline.insert(0,'名次')
firstline.append('总分')
firstline.append('平均分')

print("firstline",firstline)

rank_scorelist.insert(0,firstline)
with open("lastreport.txt","w") as f:
    for lines in rank_scorelist:
        for line in lines:
            f.write(str(line)+" ")
print("Done!")
