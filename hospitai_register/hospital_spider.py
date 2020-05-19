#coding:utf8
import requests
from tools import send_email,get_all_conf
import time
import json


#  获取首页每家医院的简单信息
def get_index_list(i):
    cookies = {
        'hyde_session': 'L8nwIlyvoyZnFFvghlQYQgpE332nsrCX_5299018',
        'pgv_pvi': '5689594880',
        'pgv_si': 's5625565184',
        'cmi-user-ticket': '-UOl_3PfEKlp2CzEzPsEHUZuaHbMv_P0yrTX3A..',
        'secure-key': '85e0726d-c3b3-4111-973f-aa3234d9317e',
        'hyde_session_tm': '1589705737699',
    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Request-Source': 'PC',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.114yygh.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('_time', '1589705832732'),
        ('keywords', ''),
        ('levelId', '0'),
        ('areaId', '0'),
        # ('pageNo', '1'),
        ('pageNo', '{}'.format(i)),
        ('pageSize', '20'),
    )

    response = requests.get('https://www.114yygh.com/web/hospital/list', headers=headers, params=params,
                            cookies=cookies)

    time.sleep(2)
    # write_csv(response.json())
    return response.json()

# 获取每家医院科室的简单信息
def get_deatil_list(hosCode):
    cookies = {
        'hyde_session_tm': '1589713259036',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.114yygh.com/hospital/1/home',
        'Connection': 'keep-alive',
        'Request-Source': 'PC',
    }

    params = (
        ('_time', '1589713330063'),
        ('hosCode', '{}'.format(hosCode)),
    )
    response = requests.get('https://www.114yygh.com/web/department/hos/list', headers=headers, params=params,
                            cookies=cookies)
    # write_json(hosCode,response.json())
    time.sleep(2)
    return response.json()


# 获取具体每个门诊科室的详细信息
def get_detail(firstDeptCode,secondDeptCode,hosCode):
    cookies = {
        'cmi-user-ticket': 'Ls--YccbVBql_aOX1MSY2MhILQDzVwFDxaN5Ag..',
    }
    headers = {
        'Origin': 'https://www.114yygh.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        # 'Referer': 'https://www.114yygh.com/hospital/1/2feb85b952a4dcd6dbf832100f6ef595/200004097/source',
        'Referer': 'https://www.114yygh.com/hospital/1/{}/{}/source'.format(firstDeptCode,secondDeptCode),
        'Connection': 'keep-alive',
        'Request-Source': 'PC',
    }
    params = (
        ('_time', '1589717746005'),
    )
    # data = '{"firstDeptCode":"2feb85b952a4dcd6dbf832100f6ef595","secondDeptCode":"200004097","hosCode":"1","week":1}'
    data = {"firstDeptCode":"{}".format(firstDeptCode),"secondDeptCode":"{}".format(secondDeptCode),"hosCode":"{}".format(hosCode),"week":1}
    data = json.dumps(data)
    response = requests.post('https://www.114yygh.com/web/product/list', headers=headers, params=params,
                             cookies=cookies, data=data)
    time.sleep(2)
    return response.json()

def main():
    for i in range(1,15):
        try:
            json_data = get_index_list(i)
            print('访问114首页ajax接口：{}'.format(json_data))
            for item in json_data['data']['list']:
                print('每个医院的大致简介:{}'.format(item))
                if item['name'] in filter_hospital:
                    print('要过滤的医院{}'.format(item))
                    break
                if '一级' in item['levelText'] or '二级' in item['levelText']:
                    print('要过滤的医院{}'.format(item))
                    break
                try:
                    detail_json = get_deatil_list(item['code'])
                    for item2 in detail_json['data']['list']:
                        print('医院科室分类的情况:{}'.format(item2))
                        for item3 in item2['subList']:
                            print('具体到某个医院某个门诊的某个小门诊：{}'.format(item3))
                            if '口腔' not in item3['name']: continue
                            try:
                                final_json = get_detail(item3['dept1Code'], item3['code'], item['code'])
                                print('我想要得到的具体信息：{}'.format(final_json))
                                for item4 in final_json['data']['calendars']:
                                    info = '医院：{},levelText：{},一级科室：{},二级科室：{},时间：{}-->{}，挂号情况：{}'.format(item['name'],item['levelText'] ,item2['name'],
                                                                                           item3['name'], item4['dutyDate'],
                                                                                           item4['weekDesc'], item4['status'])
                                    print(info)
                                    if item4['status'] == 'AVAILABLE': send_email(info)
                            except Exception as e:
                                print(e)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    filter_hospital = ['中国医学科学院整形外科医院',
                       '北京中诺第二口腔医院',
                       '北京中诺口腔医院',
                       '北京海德堡联合口腔医院',
                       '北京市红十字会和平骨科医院',
                       '北京维乐口腔医院',
                       '北京汉琨中医医院',
                       '北京新华卓越康复医院',
                       '北京优联眼耳鼻喉医院',
                       '北京德尔康尼骨科医院',
                       '北京北亚骨科医院',
                       '北京市怀柔区第二医院',
                       '首都医科大学附属北京潞河医院'
                       ]
    filter_small_dempartment = []
    main()
    '''
    ls -l | grep "^-" | wc -l

    '''