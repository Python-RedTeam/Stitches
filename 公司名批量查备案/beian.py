# coding:utf-8
# author:herbagef

import requests
from urllib import parse
import json
import time


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        name = [i.strip("\n") for i in lines]
    return name


def req_url(qy_name):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    url = "http://icp.chinaz.com/Home/PageData"
    qy_name1 = parse.quote(qy_name)
    data = "pageNo=1&pageSize=10&Kw="+qy_name1
    req = requests.post(url=url, data=data, headers=header)
    host_all = json.loads(req.text).get("data")
    if len(host_all)>0:
        read_json(host_all)
    else:
        print("#"*40)
        print('{}不存在备案域名'.format(qy_name))


def read_json(host_all):
    for i in host_all:
        print('#'*40)
        print('网站网址:{}\n网站名称：{}\n网站负责人:{}\n网站备案/许可证号:{}\n网站类型:{}\n审核时间:{}'
              .format(i['host'], i['webName'], i['owner'], i['permit'], i['typ'], i['verifyTime']))
        with open("备案.txt", 'a+', encoding='utf-8') as f:
            f.write('{}\n'.format(i['host']))



def main():
    try:
        file_name = 'beian.txt'
        name = read_file(file_name)
        for i in name:
            time.sleep(2)
            req_url(i)

    except Exception as e:
        print("error:", e)


if __name__ == '__main__':
    main()


