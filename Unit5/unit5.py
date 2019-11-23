import pexpect
child = pexpect.spawn('scp foo user@example.com: .')    #spawn启动scp程序
child = expect('Password:') #expect方法等待子程序产生的输出，判断是否匹配定义的字符串 #‘password:'
child.sendline(mypassword)  #匹配后则发送密码串进行回应
