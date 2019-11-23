import pexpect
child = pexpect.spawn('scp foo user@example.com: .')    #spawn启动scp程序
child = expect('Password:') #expect方法等待子程序产生的输出，判断是否匹配定义的字符串 #‘password:'
child.sendline(mypassword)  #匹配后则发送密码串进行回应



class pexpect.spawn(command,agrs=[],timeout=30,maxread=2000,searchwindowsize=None,logfile=None,cwd=None,env=None,ignore_sighup=True)


#其中command参数可以是任意已知的系统命令，比如
child = pexpect.spawn('/usr/bin/ftp')       #启动ftp客户端命令
child = pexpect.spawn('/usr/bin/ssh user@example.com')  #启动ssh远程连接命令
child = pexpect.spawn('ls -latr /tmp') #运行ls显示 /tmp目录内容命令


#当子程序需要参数时，还可以使用Python列表来代替参数项，如：
child = pexpect.spawn('/usr/bin/ftp',[])
child = pexpect.spawn('/usr/bin/ssh',['usr@example.com'])
child = pexpect.spawn('ls',['-lstr','/tmp'])

child = pexpect.spawn('/bin/bash -c "ls -l | grep LOG > logs.txt"')
