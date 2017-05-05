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
items = ['red-1', 'red-2', 'red-3', 'red-4', 'red-5', 'red-6','red-7','red-8','red-9','red-Q','red-J','red-K','red-A','black-1', 'black-2', 'black-3', 'black-4', 'black-5', 'black-6','black-7','black-8','black-9','black-Q','black-J','black-K','black-A','plum-1', 'plum-2', 'plum-3', 'plum-4', 'plum-5', 'plum-6','plum-7','plum-8','plum-9','plum-Q','plum-J','plum-K','plum-A','diamond-1', 'diamond-2', 'diamond-3', 'diamond-4', 'diamond-5', 'diamond-6','diamond-7','diamond-8','diamond-9','diamond-Q','diamond-J','diamond-K','diamond-A','red Joker','black Joker']
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

