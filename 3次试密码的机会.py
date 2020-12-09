# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:53:31 2019

@author: Administrator
"""

#count=0                         #break语句终止所有循环，跳出循环姐，执行循环后面的语句；往下跳不往上跳。
#while count < 10:               #continue语句终止当前循环，开始下一次循环，往上跳往下跳。
#    if count==7:
#        count=count+1
#        break
#    print(count)
#    count=count+1

#提供3次试密码的机会

#n=1
#i=1
##while n<3:
#password=input("请输入密码：")
#if int(password)==123:
#    print("验证通过")
##    else:
##            n=3-i
##            print('密码错误，''你还有')
##            i=i+1

#老师版本
#count=0
#while count<3:
#    user=input("请输入用户名：")
#    psd=input("请输入密码：")
#    if user =="Bven" and psd=="mm123123":
#        print("验证通过")
#        break
#    else:
#        print('账号或者密码有误，请检查后重新输入')
#        count=count+1
#print('您的账号已锁定，请15分钟后重新登陆')


#实验版本1 over
#count=0
#while count<3:
#    user=input("请输入用户名：")
#        if user=='Bven':
#            print('账号验证通过，请输入密码')
#        else：
#            print('账号输入有误，请检查')
#        
#        psd=input("请输入密码：")
#        if psd=="mm123123":
#            print("密码验证通过，欢迎使用")
#        else：
#            print('')
#        break
#    else:
#        print('账号或者密码有误，请检查后重新输入')
#        count=count+1
#print('您的账号已锁定，请15分钟后重新登陆')

#实验终版本，用多重if嵌套实现需求
user=input("请输入用户名：")
if user =="1" :
    print("验证通过")
else:
    print('用户名有误，请检查')
count=0
while count<3:
    psd=input("请输入密码：")
    if psd=="111":
        print("验证通过")
        break
    else:
        count=count+1
        n=3-count
        if n==0:
            break
        else:
            print('密码有误，'+'你还有'+str(n)+'次机会，'+'请检查后重试')        
    
# print('您的账号已锁定，请15分钟后重新登陆')




#    else:
#        print('账号或者密码有误，请检查后重新输入')
#        count=count+1
#        n=3-count
#        if n==0:
#            break
#        else:
#            print('你还有'+str(n)+'次机会')
#        
#print('您的账号已锁定，请15分钟后重新登陆')
