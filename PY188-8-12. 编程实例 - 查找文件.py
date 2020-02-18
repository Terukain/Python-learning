import os,sys

def findfiles(t,path):
    foundlist=[]
    allfiles=os.listdir(path)
    for name in allfiles:
        fullname=path+'/'+name
        if t in name:
            foundlist.append(fullname)
        else:
            try:
                with open(fullname)as f:
                    for l in f.readlines:
                        if t in l:
                            foundlist.append(fullname+':'+l.strip())
                            break
            except:
                pass
    return foundlist
t=input('请输入搜索关键词：')

path=input("搜索目录为：（默认为C:\工作\软件\Python\excises）\n")
if not path.strip():
    path='.'
result=findfiles(t,path)


print("搜索结果：")

for a in result:
    print(a)
