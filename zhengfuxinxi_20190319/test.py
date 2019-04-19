'''
项目文件上传：scrapyd-deploy <服务器名> -p <项目名> --version <版本号>

可用服务器列表： scrapyd-deploy -l

服务器中未上传项目是，会有默认项目：scrapyd-deploy -L server-douban

启动爬虫：curl http://localhost:6800/schedule.json -d project=myproject -d spider=spider2

 curl http://localhost:6800/schedule.json -d project=myproject -d spider=somespider -d setting=DOWNLOAD_DELAY=2 -d arg1=val1

一个项目部署到所有服务器：scrapyd-deploy -a -p <project>



服务器运行状态：http://127.0.0.1:6800/daemonstatus.json

关闭爬虫：curl http://localhost:6800/cancel.json -d project=myproject -d job=6487ec79947edab326d6db28a2d86511e8247444

项目下，各爬虫版本：http://localhost:6800/listversions.json?project=myproject

项目下，爬虫列表：http://127.0.0.1:6800/listspiders.json?project=myproject

服务器下，工程列表：http://127.0.0.1:6800/listprojects.json

服务器下，所有任务列表：http://127.0.0.1:6800/listjobs.json?project=myproject

启动指定爬虫，post请求： http://localhost:6800/schedule.json      （post方式，data={"project":myproject,"spider":myspider}）

删除指定工程，post请求： http://127.0.0.1:6800/delversion.json    （post方式，data={"project":myproject,"version":myversion}）

删除工程，post请求： http://127.0.0.1:6800/delproject.json      （post方式，data={"project":myproject}）



'''

'''
response.status_code    状态码
response.json()         数据转为json（根据情况使用）
response.headers        响应头信息
response.request        请求方式
response.url            请求的url
response.cookies        返回的cookie数据（空）
response.elapsed        请求响应时间（空）
response.history        返回的历史信息（空）
'''

import requests
from scrapy import cmdline


def get_requests(tag, p_name='null', p_spider='', p_version='null', jobid = 'null'):  # pn工程名  pv工程版本号
    '''
    指令离别： fwzt状态  fwlb服务器列表  pcbb爬虫版本  gbpc关闭爬虫  pclb爬虫列表
             gclb工程列表  rwlb任务列表  gbpc关闭爬虫  scpc删除爬虫  scgc删除工程
    :param tag: 指令名称
    :param p_name: 项目名称
    :param p_version: 项目版本
    :return: 从scrapyd的反馈数据
    '''
    url = {
        'fwzt': 'http://127.0.0.1:6800/daemonstatus.json',

        # 'fwlb': 'http://127.0.0.1:6800/listspiders.json?project=myproject',
        'pcbb': 'http://localhost:6800/listversions.json?project=myproject',
        'gbpc': 'curl http://localhost:6800/cancel.json -d project=myproject -d job=jobid',

        'pclb': 'http://127.0.0.1:6800/listspiders.json?project=myproject',
        'gclb': 'http://127.0.0.1:6800/listprojects.json',
        'rwlb': 'http://127.0.0.1:6800/listjobs.json?project=myproject',

        'scpc': 'http://127.0.0.1:6800/delversion.json',
        'scgc': 'http://127.0.0.1:6800/delproject.json',
        'qdpc': 'http//localhost:6800/schedule.json -d project=myproject -d spider=somespider',
    }

    if not type(tag) == type(p_name) == type(p_version) == str:
        raise Exception('参数类型错误！')

    if tag in ['fwzt', 'gclb']:
        response = requests.get(url=url[tag])

    elif tag in ['fwlb', 'pcbb', 'pclb', 'rwlb']:
        url = url[tag].replace('myproject', p_name)
        response = requests.get(url=url)

    elif tag in ['gbpc']:
        url = url[tag].replace('myproject', p_name).replace('jobid',jobid)
        response = requests.get(url=url)

    elif tag in ['qdpc', 'scpc', 'scgc']:
        if tag == 'qdpc':
            data = {"project": p_name, "spider": p_spider}
        if tag == 'scpc':
            data = {"project": p_name, "version": p_version}
        if tag == 'scgc':
            data = {"project": p_name}

        response = requests.post(url=url[tag], data=data)
    else:
        raise Exception('参数错误！')
    # print(response.status_code, response.json())
    ret = {'status': response.status_code, 'msg': response.json()}
    return ret


# 命令列表
# up = ['python','scrapyd-deploy','sone','-p','zhengfuxinxi_20190319','--version','1.0v']
# c1 = cmdline.execute(up)
# # c1 = cmdline.execute(['scrapyd-deploy sone -p zhengfuxinxi_20190319 --version 1.0v'])
# print(c1)

# # 服务器状态
print(get_requests('fwzt'))
# # 可用服务器列表
# # print(get_requests('fwlb'))
#
# # 启动爬虫
# print(get_requests('qdpc', 'zhengfuxinxi_20190319', 'zhengfu'))
# # 爬虫版本
# print(get_requests('pcbb', 'zhengfuxinxi_20190319'))
# # 爬虫列表
# print(get_requests('pclb', 'zhengfuxinxi_20190319'))
# 任务列表(包括：待处理、正运行、已完成三种状态)
print(get_requests('rwlb', 'zhengfuxinxi_20190319'))
# # 关闭爬虫
# print(get_requests('gbpc','zhengfuxinxi_20190319',jobid='323d961061d311e99416107b44269657'))
# # 删除爬虫
# print(get_requests('scpc'))
# # 删除工程
print(get_requests('scgc'))
