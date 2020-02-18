def readblocklist():
    with open("blocklist.txt",encoding='utf-8')as f:
        global words
        #words=[h.strip()for h in f.readlines()if h]
        words=[]
        lines=f.readlines()
        for h in lines:
            if h:
                h=h.strip()# strip()方法默认去掉字符串两端的 \t \n \r 空格,等符号
                words.append(h)

def filter(text,symbol="*"):
    for w in words:
        text=text.replace(w,symbol)#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
    return text

readblocklist()
while True:
    g=input('输入待屏蔽文字：\n')
    if not g:
        break
    print("优化后的文字：\n",filter(g))
