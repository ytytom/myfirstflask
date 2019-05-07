# -*- coding: UTF-8 -*-
import urllib2, json, cookielib, urllib, datetime, os, threading
from urllib2 import Request, urlopen, URLError, HTTPError

global auth_code, zabbix_url, zabbix_header, login_url, graph_url, login_data, pic_save_path_dir, yesterday9, opener

zabbix_url = "http://172.20.13.209/zabbix/api_jsonrpc.php"
login_url = 'http://172.20.13.209/zabbix/index.php'
graph_url = 'http://172.20.13.209/zabbix/chart2.php'
zabbix_header = {"Content-Type": "application/json"}
zabbix_user = "yzq001"
zabbix_pass = "password"
auth_code = ""

auth_data = json.dumps({
    "jsonrpc": "2.0",
    "method": "user.login",
    "params":
        {
            "user": zabbix_user,
            "password": zabbix_pass
        },
    "id": 0
})

login_data = urllib.urlencode({
    "name": zabbix_user,
    "password": zabbix_pass,
    "autologin": 1,
    "enter": "Sign in"})

# today = datetime.datetime.now().date().strftime('%Y%m%d')
pic_save_path_dir = 'C:\\Users\\yangtingyao\\Desktop\\zabbix\\zabbix_API\\pic'

if not os.path.exists(pic_save_path_dir):
    os.makedirs(pic_save_path_dir)

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1))
yesterday9 = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 9).strftime('%Y%m%d%H%M%S')

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
opener.open(login_url, login_data)

request = urllib2.Request(zabbix_url, auth_data)

for key in zabbix_header:
    request.add_header(key, zabbix_header[key])
try:
    result = urllib2.urlopen(request)
except HTTPError, e:
    print 'The server couldn\'t fulfill the request, Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server.Reason: ', e.reason
else:
    response = json.loads(result.read())
    # print response
    result.close()

if 'result' in response:
    auth_code = response['result']
else:
    print  response['error']['data']


def Http_access(data):
    request = urllib2.Request(zabbix_url, data)
    for key in zabbix_header:
        request.add_header(key, zabbix_header[key])
    result = urllib2.urlopen(request)

    response = json.loads(result.read())
    # print result.read()
    # print response
    result.close()
    if len(response['result']) > 0:
        return response['result'][0]


def get_hostid(ip):
    get_host_data = ''
    if len(auth_code) <> 0:
        get_host_data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": [
                        ip,
                    ]
                }
            },
            "auth": auth_code,
            "id": 1
        })
    return get_host_data


def get_itemid(hostid, itemtype):
    get_item_data = ''
    if (len(auth_code) <> 0) and (hostid is not None):
        get_item_data = json.dumps({
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "search": {
                    "name": itemtype
                },
                "sortfield": "name"
            },
            "auth": auth_code,
            "id": 1
        })
    return get_item_data


def get_graphid(itemid):
    get_graph_data = ''
    if (len(auth_code) <> 0) and (itemid is not None):
        get_graph_data = json.dumps({
            "jsonrpc": "2.0",
            "method": "graphitem.get",
            "params": {
                "output": "extend",
                "expandData": 1,
                "itemids": itemid
            },
            "auth": auth_code,
            "id": 1
        })
    return get_graph_data


def pic_save(ip, name, graphid):
    graph_args = urllib.urlencode({
        "graphid": graphid,
        "width": '800',  # 定义图片宽度
        "height": '156',  # 定义图片高度
        "stime": yesterday9,  # 图形开始时间
        "period": '86400'})  # 定义时长，取1天的数据

    data = opener.open(graph_url, graph_args).read()
    # pic_save_path = pic_save_path_dir + ip + '-' + name +'.png'
    picname = ip + '-' + name + '.png'
    pic_save_path = os.path.join(pic_save_path_dir, picname)
    file = open(pic_save_path, 'wb')
    file.write(data)
    # file.flush()
    file.close()


def pic_save_th(ip):
    # 根据ip获取hostid
    host_data = get_hostid(ip)
    host_result = Http_access(host_data)
    if host_result is not None:  # 判断该IP是否在zabbix中存在
        hostid = host_result['hostid']


        # 根据监视器名称获取相应的itemid
        cpuname = 'CPU Busy'
        memoryname = 'Used memory in %'
        # diskname = 'Disk - Current Disk Queue Length'
        swap_use = 'Used swap space in %'
        item_cpu = get_itemid(hostid, cpuname)
        item_memory = get_itemid(hostid, memoryname)
        # item_disk = get_itemid(hostid,diskname)
        item_swap_use = get_itemid(hostid, swap_use)

        itemid_cpu = Http_access(item_cpu)['itemid']
        # itemid_memory = Http_access(item_memory)['itemid']
        # itemid_disk = Http_access(item_disk)['itemid']
        itemid_swap_use = Http_access(item_swap_use)['itemid']

        # 根据itemid获取相应的graphid
        graphdata_cpu = get_graphid(itemid_cpu)
        # graphdata_memory = get_graphid(itemid_memory)
        # graphdata_disk = get_graphid(itemid_disk)
        graphdata_swap_use = get_graphid(itemid_swap_use)

        graphid_cpu = Http_access(graphdata_cpu)['graphid']
        # graphid_memory = Http_access(graphdata_memory)['graphid']
        # graphid_disk = Http_access(graphdata_disk)['graphid']
        graphid_swap_use = Http_access(graphdata_swap_use)['graphid']

        print ip  # ,graphid_cpu,graphid_memory,graphid_disk,graphid_swap_use

        # 调用pic_save函数保存图片到本地
        pic_save(ip, cpuname, graphid_cpu)
        # pic_save(ip, memoryname, graphid_memory)
        # pic_save(ip,diskname,graphid_disk)
        pic_save(ip, swap_use, graphid_swap_use)

    else:
        print '%s doesnot exist in zabbix or key dose not exist' % ip


def lstg(num, lst):
    # 定义每段的个数num
    l = len(lst)
    g = l / num  # 取分成几组
    last = l % num  # 判断是否有剩余的数
    lstn = []
    if num >= l:
        lstn.append(lst)
    else:
        for i in range(g):
            i = i + 1
            n = i * num
            m = n - num
            lstn.append(lst[m:n])

        if last <> 0:
            lstn.append(lst[-last:])
    return lstn


if __name__ == '__main__':
    # 定义线程数量
    tnum = 5
    serverips = ['zabbix01']
    threads = []
    for ips in lstg(tnum, serverips):
        for ip in ips:
            # 创建并启动进程
            t = threading.Thread(target=pic_save_th, args=(ip,))
            # t.setName('th-'+ ip)
            t.setDaemon(True)
            t.start()
            threads.append(t)
        # 等待每个线程结束
        for t in threads:
            # print t.name,t.is_alive(),ctime()
            t.join()
