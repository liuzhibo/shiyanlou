import re
# from datetime import datetime
from collections import Counter

# 使用正则表达式解析日志文件，返回数据列表


def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (r''
                   '(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   '\[(.+)\]\s'  # 时间
                   '"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   '(\d+)\s'  # 状态码
                   '(\d+)\s'  # 数据大小
                   '"(.+)"\s'  # 请求头
                   '"(.+)"'  # 客户端信息
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers


def main():

    # 使用正则表达式解析日志文件
    logs = open_parser(
        '/Users/liuzhibo/Code/python/shiyanlou/week3/challenge11/nginx.log')

    '''
    1. 解析文件就是分离不同类型数据（IP，时间，状态码等）
    2. 从解析后的文件中统计挑战需要的信息
    '''
    _404list = []
    _iplist = []
    url_dict = {}
    ip_dict = {}

    for y in logs:
        if '11/Jan/2017' in y[1]:
            _iplist.append(y[0])
    ip_dict[Counter(_iplist).most_common(1)[0][0]] = Counter(
        _iplist).most_common(1)[0][1]
    for x in logs:
        if '404' in x[3]:
            _404list.append(x[2])
    url_dict[Counter(_404list).most_common(1)[0][0]] = Counter(
        _404list).most_common(1)[0][1]
    return ip_dict, url_dict


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
