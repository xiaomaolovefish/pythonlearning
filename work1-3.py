#encoding='utf-8'
#作业一
#1
print 'name:ZhiPing Li'
#2
print 'h=a+b*c-d/e'
#3
print '..........\r',
print '555555555'
#4
print '..........\n 555555555'

#作业二
weight=input('please input weight(kg):' )
height=input('please input height(m):' )
BMI=weight/(height*height)
if BMI < 18.5:
    print '体重偏轻'
if 18.5<= BMI < 24:
        print '体重正常'
if BMI >=24:
    print '体重偏重'
    


#work3
import random
#生成扑克牌列表
items = [m+str(n)  for m in 'RBPD' for n in range(13)]
items.append('red Joker')
items.append('black Joker')
#洗牌
random.shuffle(items)

def poker(items):
    A=random.sample(items,17)
    print(A)
    ret = list(set(items) ^ set(A))
    return(ret)
if __name__ == '__main__':
    ret = poker(items)
    retb = poker(ret)
    retc = poker(retb)
    print(retc)

