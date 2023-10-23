#猜数字，成绩存文件，带姓名版本
f = open('game.txt',encoding='utf-8')
data = f.readlines()
f.close()
chengji = {}
for i in data:
    i = i.split()
    chengji[i[0]]=i[1:]
name = input('输入你的名字\n')
if chengji.get(name) == None:
    chengji[name] = ['0','0','0']
else:
    pass
print(chengji[name])
# try:
zongcs = int(chengji[name][0])
fasttime = int(chengji[name][1])
zongls = int(chengji[name][2])
# except:
#     zongcs = 0
#     fasttime = 0
#     zongls = 0
if zongcs == 0:
    age =0
else:
    age = zongls/zongcs
print('总共玩了%d次，最快%d轮猜出来，平均%.2f轮猜出答案'%(zongcs,fasttime,age))
def isEqual(num1, num2):
   if num1<num2:
       print('too small')
       return False;
   elif num1>num2:
       print ('too big')
       return False;
   else:
       print ('bingo')
       return True
from random import randint
num = randint(1, 100)
print('Guess what I think?')
bingo = False
lunci = 0
while bingo == False:
   answer = int(input())
   bingo = isEqual(answer, num)
   lunci+=1
if lunci<fasttime or fasttime==0:
    fasttime=lunci
else:
    pass
zongls = zongls + lunci
zongcs += 1
age = zongls/zongcs
print('总共玩了%d次，最快%d轮猜出来，平均%.2f轮猜出答案'%(zongcs,fasttime,age))
sorunm = [str(zongcs),str(fasttime),str(zongls)]
# sorunm=' '.join(sorunm)
chengji[name] = sorunm
data1 = []
for name in chengji:
    data1.append('%s %s\n'%(str(name),str(' '.join(chengji[name]))))
print(data1)
f=open('game.txt','w',encoding='utf-8')
f.writelines(data1)
f.close()
