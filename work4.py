#encoding='utf-8'
#python 2.7.12
#作业4
import random
n = input('please input people:' )
total = input('please input total:' )
money=total*100
length=money-n+1

#产生随机数
def get_num(length,n):
  redpack=[random.randint(1, length) for i in range(n)]
  #print redpack
  return(redpack)


if __name__ == '__main__':
  
  redpack = get_num(length,n)
  act_money = sum(redpack)
  #比较随机数之和与总金额是否相等
  while act_money != money :
    #不相等，执行循环
    redpack = get_num(length,n)
    act_money = sum(redpack)
    if act_money == money :
      #相等打印随机数
      print(redpack)
      print(sum(redpack))
      for item in redpack :
        #浮点数处理
        pack = item/float(100)
        pack='%.2f' %pack
        print pack
        #打印随机产生的每人所得红包金额
  




