#coding=gbk

import os
import datetime
import re
import shutil

dst ="E:\\ControlVersion\\SEAI\\control\\branches\\Branch_SIT\\Branch_NIS"
src="E:/ControlVersion/SvnNISjiaoben/SEAI/emp"
filename='E:\\ControlVersion\\SvnNISjiaoben\\SEAI\\code.log'
now=datetime.datetime.now()
#dr=now.strftime('%Y%m%d_%H%M')
dt=now.strftime('%Y%m%d')

def clean(fd):
       if os.path.exists(fd):
              if os.path.isdir(fd):
                     shutil.rmtree(fd)
                     print ("****删除文件夹%s 成功" %fd)
              elif os.path.isfile(fd):
                     os.remove(fd)
                     print ("****删除文件%s 成功" %fd)
              else:
                     pass
              
              
       else:
              pass
       
def get_version():
       cmd='svn info http://10.192.34.46/svn/SEAI/development/release/release_NIS > info.txt'
       os.system(cmd)
       f = open('info.txt','r')
       filelist = f.readlines()
       f.seek(0,0)
       for line in filelist:
              if 'Last Changed Rev' in line:
                     r = line
                     print r
       return r

def exportTmp():
    f = open('list.txt','r')
    filelist = f.readlines()
    f.seek(0,0)
    for line in filelist :
            if 'branch_NIS' in line:
                        str1 = 'emp/'+line[line.index('development/branches/branch_NIS')+len('development/branches/branch_NIS')+1:line.rfind("/")]
            else:
                        str1 = 'emp/'+line[line.index('development/branches')+len('development/branches')+1:line.rfind("/")]
            if(os.path.exists(str1)!=True):
                    os.makedirs(str1)
                                
            url,version = line.strip().split()
            print url,version
            cmd = 'svn export --force -r '+version+' '+url+' '+str1
        #cmd = 'svn export -r '+line.split(" ")[1].strip()+' '+line.split(" ")[0].strip()+' '+str1#+' --username '+svnUser+' --password '+svnPassword
            print cmd
            execSvn(cmd)
                        

def exportTmp_new():
       f = open('list.txt','r')
       filelist = f.readlines()
       f.seek(0,0)
       for line in filelist :
              if 'branch_NIS' in line:
                     str1 = 'emp/'+line[line.index('development/branches/branch_NIS')+len('development/branches/branch_NIS')+1:line.rfind("/")]
              else:
                     str1 = 'emp/'+line[line.index('development/branches')+len('development/branches')+1:line.rfind("/")]
              if(os.path.exists(str1)!=True):
                     os.makedirs(str1)
              if len(line.strip().split())==2:
                     url,version = line.strip().split()
                     cmd = 'svn export --force -r '+version+' '+url+' '+str1
                     execSvn(cmd)
              else:
                     url=line.strip()
                     cmd = 'svn export --force'+' '+url+' '+str1
                     print cmd
                     execSvn(cmd)
def exportTmp_new_2():
       f = open('list.txt','r')
       filelist = f.readlines()
       f.seek(0,0)
       for line in filelist :
              if 'branch_NIS' in line:
                     str1 = 'emp/'+line[line.index('development/branches/branch_NIS')+len('development/branches/branch_NIS')+1:line.rfind("/")]
              else:
                     str1 = 'emp/'+line[line.index('development/branches')+len('development/branches')+1:line.rfind("/")]
              if(os.path.exists(str1)!=True):
                     os.makedirs(str1)
              if len(line.strip().split())==2:
                     url,version = line.strip().split()
                     cmd = 'svn export --force -r '+version+' '+url+' '+str1
                     #execSvn(cmd)
                     REL=os.popen(cmd)
                     res=REL.read()
                     if 'export complete' in res:
                            print res
                     else:
                            print '***svn export fail**url %s' %url
                            print'\n'
                            with open('error.txt','a') as f:
                                   f.write(url)
                                   f.write('\n')
                     
              else:
                     url=line.strip()
                     cmd = 'svn export --force'+' '+url+' '+str1
                     print cmd
                     execSvn(cmd)     
        
def update():
       
       os.chdir(dst)
	#print(os.getcwd())
       cmd = 'svn update '+dst
       os.system(cmd)       
                
def copy_cmd():
       cmd ='xcopy /E /Y "%s" "%s\\*"' %(src,dst)
       #cmd='xcopy /E /Y' +' '+"E:\CCMS\temp\"  "E:\CCMS\SIT01"   
       print(cmd)
       os.system(cmd)
       #cmd_1 ='xcopy /E /Y  "E:/CCMS/svn_NIS/emp/branch_SIT" "E:\\SEAI\\control\\branches\\Branch_SIT\\Branch_NIS\\*"'
       #os.system(cmd_1)

def execSvn(cmd):
    flag = os.system(cmd)
    if flag!=0 :
        raise Exception("执行SVN命令失败,停止执行")
    else:
        print(" ******* 执行svn指令成功。 ******** ")


       
def svn_ci(r):
     os.chdir("E:\ControlVersion\SvnNISjiaoben\SEAI")
     with open("list.txt") as f:
                for line in f:
                       # totalpath=os.path.join(parent,path).strip("\n")
                       if 'branch_NIS' in line:
                              strl = line[line.index('development/branches/branch_NIS')+len('development/branches/branch_NIS')+1:line.rfind("/")]
                       else:
                              strl = line[line.index('development/branches')+len('development/branches')+1:line.rfind("/")]
                      
                       totalpath=os.path.join(dst,strl).strip("\n")
                       os.chdir(totalpath)
                       add='svn add --force *'
                       os.system(add)
   
    #os.getcwd()
     #dst1=dst+'database'
     #os.chdir(dst1)
     
     os.chdir(dst)
    #cmd_d='rmdir /s/q bin'
     #************************
     #add='svn add --force *'
     #print add
     #os.system(add)
     #*********************
   # add='svn add *'
   # os.system(add)
     cmd='svn ci -m " %s  Update SIT from dev/branch_NIS , %s   "' %(dt,r)
     print cmd
     execSvn(cmd)
   
def update_1():
       src ="E:/SEAI/control/branches/Branch_SIT/Branch_NIS"
       os.chdir(src)
	#print(os.getcwd())
       cmd = 'svn update '+src
       os.system(cmd)               

                        
if __name__ == "__main__":
       clean(filename)
       clean(src)
       r=get_version()
       #exportTmp()
       exportTmp_new()
       update()
       copy_cmd()
       svn_ci(r)
       os.system("pause")
        #update_1()

                        
             
                
		
		
		
		 
		
	       
	

		    
				
					
				
					
       
			
	   
				
			      
			
		 
			 
				
		       
			
    
			

					
					
					
					
					
				
				




















