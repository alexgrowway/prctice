def avgechengji(list):
    sumber = 0
    for i in list[1:]:
        sumber+=int(i)
    return sumber
#返回整个表平均分数
def qiuhe(list):
    pingjunfen = ['平均分',0,0,0,0,0,0,0,0,0,0,0]
    for i in list:
        x = 1
        for j in i[1:]:
            pingjunfen[x]+=float(j)
            x+=1
    n = 1
    for x in pingjunfen[1:]:
        pingjunfen2=x/len(list)
        pingjunfen[n] = round(pingjunfen2,2)
        n+=1
    return pingjunfen


with open('report.txt','r',encoding='utf-8') as f:
    cjlist = f.readlines()
zchengji = []
for i in cjlist[1:]:
    gerenchengji = i.split()
    c = avgechengji(gerenchengji)
    b = round(c/9,2)
    gerenchengji.extend((c,b))
    zchengji.append(gerenchengji)
qypj01 = qiuhe(zchengji)#平均成绩list
zchengji.sort(key=lambda x:x[11],reverse=True)#排序
zchengji.insert(0,qypj01)#插入平均分
mingci = 0
for z in zchengji:
    zchengji[mingci].insert(0,mingci)
    if mingci>0:
        grdkcj = 2
        for m in z[2:-2]:
            if int(m) < 60:
                zchengji[mingci][grdkcj]='不及格'
            grdkcj+=1
    mingci+=1

biaotou = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','个人平均']
zchengji.insert(0,biaotou)#添加表头
print(zchengji)
with open('result.txt','w',encoding='utf-8') as f:
    for line in zchengji:
        f.writelines(' '.join('%s'%id for id in line)+'\n')
