import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

url = "http://192.168.0.128/"
txt = "dirtop60000.txt"
url_list = []
# noinspection PyBroadException
try:
    with open(txt, 'r') as f:
        for a in f:
            a = a.replace('\n', '')
            url_list.append(a)
        f.close()

except Exception:
    print("file read error")

for li in url_list:
    conn = url + li
    try:
        result = requests.get(conn, headers=headers)
        print("%s---------------%s" % (conn, result))
    except Exception as e:
        print("%s---------------%s" % (conn, e))

# if __name__ == '__main__':
#     fscan("http://192.168.0.128/")
