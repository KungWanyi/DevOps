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
child.expect(pexpect.EOF)


shell_cmd = 'ls -l | grep LOG > logs.txt'
child = pexpect.spawn('/bin/bash',['-c',shell_cmd])
child.expect(pexpect.EOF)


#写到日志文件的方法
child = pexpect.spawn('some_command')
fout = file('mylog.txt','w')
child.logfile = fout


#输出到标准输出的方法如下
child = pexpect.spawn('some_command')
child.logfile = sys.stdout


#如下为一个完整的实例，实现远程SSH登录，登录成功后显示/home目录文件清单，并通过日志文件记录所有的输入与输出
import pexpect
import sys

child = pexpect.spawn('ssh root@192.168.1.15')
child.logfile = fout
#chid.logfile = sys.stdout
child.expect("password:")
child.sendline("1qaz@WSX")
child.expect('#')
child.sendline('ls /home')
child.expect('#')


#以下为mylog.txt日志内容，可以看到pexpect产生的全部输入与输出信息
#cat mylog.txt
root@192.168.1.15's password:1qaz@WSX




#expect(pattern,timeout=-1,searchwindowsize=-1)

