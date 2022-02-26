#coding:utf-8
import sys
from pathlib import Path

import whois,os,socket
"""
    外网--前期的信息收集
    通过域名
        判断是否存在CDN
            存在找出真实IP
        不存在通过 socket.gethostbyname 直接获取IP
        扫描端口
        子域名收集
            路径，敏感信息收集
            
    内网信息收集：
        存活主机
        协议探针
        端口扫描
    
"""
# 域名反查IP
def ip_check(domain):
    ip = socket.gethostbyname(domain)
    print(ip)


# 识别目标是否存在CDN
def cdn_check(domain):
    cdn_data = os.popen('nslookup ' + domain).read()
    print(cdn_data)

    # 通过cdn_data中小数点的个数判断cdn是否存在
    if cdn_data.count('.') > 10 :
        print('CDN存在')
    else:
        print('CDN不存在')

def whois_check(domain):
    da = whois.whois(domain)
    print(da)


# 子域名查询
def domain_check(domain):
    # 1.利用字典爆破
    now_path = sys.argv[0].replace(Path(__file__).name,'')
    for dm_list in open(now_path+"zym_dic.txt"):
        subdomain = domain.replace("www",dm_list)
        subdomain = subdomain.replace("\n",'')
        try:
            ip = socket.gethostbyname(subdomain)
            print(subdomain+" -----> "+ ip)
        except Exception as e:
            # 如果错误说明网站不存在该子域名
            pass
    # 2.利用bing或第三方接口进行查询


# 端口扫描
def port_check(ip):
    # 1.原生自写socket协议tcp udp扫描
    # ip = socket.gethostbyname(domain)
    print(ip)
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        for i in range(1,65535):
            data = server.connect_ex((ip,i))
            if data == 0:
                print(ip + ':' + str(i) +'------> open')
            else:
                # print(str(i) +'------> close')
                pass
    except Exception as e:
        print(e)
    # 2.调用三方模块等扫描
    # 3.调用系统工具脚本执行




if __name__ == '__main__':

    # port_check('192.168.131.133')
    domain_check('www.abc.cc')

