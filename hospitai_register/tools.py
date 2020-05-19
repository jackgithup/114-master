# coding:utf8
import os
from configparser import ConfigParser
import smtplib
from email.message import EmailMessage
import datetime
import csv
import json


def get_all_conf():
    cfg = ConfigParser()
    if os.path.exists('/Users/zgff/Desktop/work_space/hospitai_register/'):
        cfg.read('/Users/zgff/Desktop/work_space/hospitai_register/conf/local.ini')
    return cfg


def send_email(content):
    # 定义SMTP邮件服务器地址
    smtp_server = 'smtp.qq.com'
    # 邮件发送人邮箱
    from_addr = get_all_conf().get('email','from_addr')  # 自己的邮想
    to_addr = get_all_conf().get('email','to_addr')  # 测试接收邮件地址邮箱
    # 创建SMTP连接
    conn = smtplib.SMTP_SSL(smtp_server, 465)
    # 设计调试级别
    conn.set_debuglevel(1)
    # 登录邮箱
    # conn.login(from_addr, password)
    conn.login(from_addr, "hbnmwfjhpvvybiag")
    # 创建邮件内容对象
    msg = EmailMessage()
    msg['Subject'] = '{}中奖了，有可以医院可以预约挂号了！'.format(get_now_time())
    # 设置邮件内容
    msg.set_content(content, 'plain', 'utf-8')
    # 发送邮件
    conn.sendmail(from_addr, [to_addr], msg.as_string())
    # 退出连接
    conn.quit()

def get_now_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def write_csv(json_data):
    list_file_path = '{}file/list.csv'.format(get_all_conf().get('path','curr_dir'))
    if not os.path.exists(list_file_path):
        with open(list_file_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            item = ['code','name','levelText','openTimeText']
            writer.writerow(item)
    for item in json_data['data']['list']:
        print(item)
        with open(list_file_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            item = [item['code'],item['name'],item['levelText'],item['openTimeText']]
            writer.writerow(item)

def write_json(hosCode=162,json_data=''):
    json_data = {'resCode': 0, 'msg': None, 'data': {'count': 12, 'list': [{'code': '44f162029abb45f9ff0a5f743da0650d', 'name': '全部科室', 'subList': [{'code': '200050923', 'name': '门诊部核酸检测门诊(东院)', 'dept1Code': '44f162029abb45f9ff0a5f743da0650d', 'hotDept': False}, {'code': '200050924', 'name': '国际医疗部门诊', 'dept1Code': '44f162029abb45f9ff0a5f743da0650d', 'hotDept': False}, {'code': '200050931', 'name': '临床营养科(西院国际医疗)', 'dept1Code': '44f162029abb45f9ff0a5f743da0650d', 'hotDept': False}, {'code': '200050964', 'name': '内分泌科互联网诊疗', 'dept1Code': '44f162029abb45f9ff0a5f743da0650d', 'hotDept': False}]}, {'code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'name': '内科', 'subList': [{'code': '200041542', 'name': '特需心内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200042374', 'name': '特需消化内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200040886', 'name': '特需内分泌科门诊(西院)1', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200041246', 'name': '特需呼吸内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200041038', 'name': '特需肾内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200041244', 'name': '特需血液内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200044248', 'name': '特需老年医学科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200040166', 'name': '特需普通内科门诊1', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200041666', 'name': '内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200043118', 'name': '普通内科全科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200045974', 'name': '普通内科疑难病症门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200048285', 'name': '特需肿瘤内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200048369', 'name': '特需普通内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200048378', 'name': '卫干门诊(内科)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200048380', 'name': '特需免疫内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200048440', 'name': '特需感染内科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004002', 'name': '内分泌科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004004', 'name': '特需内分泌科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004020', 'name': '特需普通内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004014', 'name': '肿瘤内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003975', 'name': '心内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003976', 'name': '心内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003977', 'name': '心内科高血压专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003978', 'name': '特需心内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004005', 'name': '神经科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004006', 'name': '神经科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004007', 'name': '神经内科癫痫门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004010', 'name': '特需神经科门诊2', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003997', 'name': '消化内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003998', 'name': '消化内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003999', 'name': '早期胃癌专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004000', 'name': '特需消化内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004001', 'name': '内分泌科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004003', 'name': '特需内分泌科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003989', 'name': '免疫内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003990', 'name': '免疫内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003991', 'name': '特需免疫内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003992', 'name': '特需免疫内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003993', 'name': '呼吸内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003994', 'name': '呼吸内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003995', 'name': '戒烟门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003996', 'name': '特需呼吸内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003979', 'name': '肾内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003980', 'name': '肾内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003981', 'name': '特需肾内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003982', 'name': '血液科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003983', 'name': '血友病门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003984', 'name': '特需血液内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003985', 'name': '感染内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003986', 'name': '感染内科热病门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003987', 'name': '感染内科免疫功能低下门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003988', 'name': '特需感染内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003973', 'name': '老年综合门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003974', 'name': '特需老年综合门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200003972', 'name': '内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004018', 'name': '普通内科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004019', 'name': '普通内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004015', 'name': '肿瘤内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004016', 'name': '特需肿瘤内科门诊1', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004017', 'name': '特需肿瘤内科门诊(西院)', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004012', 'name': '重症肌无力专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004008', 'name': '头疼专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004009', 'name': '脑血管病专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004011', 'name': '痴呆与脑白质病专科门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}, {'code': '200004134', 'name': '肝炎门诊', 'dept1Code': '1c87253ca8aa8fc966a2443eeaac0fc1', 'hotDept': False}]}, {'code': 'cbc348c817edeffab9599ad12205fa78', 'name': '外科', 'subList': [{'code': '200045976', 'name': '特需血管外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200040164', 'name': '特需胸外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200048287', 'name': '乳腺外科乳癌化疗门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200048331', 'name': '乳腺外科乳癌随访门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200048412', 'name': '特需整形外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200048490', 'name': '泌尿外科专项诊疗门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200048586', 'name': '胸外科化疗专病门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004041', 'name': '特需神经外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004051', 'name': '心外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004052', 'name': '心外科成人门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004053', 'name': '特需心外科门诊1', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004054', 'name': '特需心外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004049', 'name': '特需泌尿外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004072', 'name': '特需肝脏外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004027', 'name': '特需基本外科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004031', 'name': '特需骨科门诊2', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004046', 'name': '肾积水专科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004034', 'name': '神经外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004035', 'name': '神经外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004040', 'name': '特需神经外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004059', 'name': '血管外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004060', 'name': '血管外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004061', 'name': '动脉疾病专科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004062', 'name': '特需血管外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004063', 'name': '特需血管外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004032', 'name': '胸外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004033', 'name': '特需胸外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004066', 'name': '特需整形外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004067', 'name': '乳腺外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004068', 'name': '乳腺外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004069', 'name': '特需乳腺外科门诊(西院)1', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004042', 'name': '泌尿外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004043', 'name': '泌尿外科男科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004044', 'name': '泌尿外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004045', 'name': '泌尿外科男科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004047', 'name': '特需泌尿外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004070', 'name': '肝脏外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004071', 'name': '特需肝外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004022', 'name': '外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004023', 'name': '基本外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004025', 'name': '基本外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004026', 'name': '特需基本外科门诊1', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004028', 'name': '骨科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004029', 'name': '骨科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004030', 'name': '特需骨科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004064', 'name': '整形美容外科门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004116', 'name': '急诊科', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200004065', 'name': '整形美容外科门诊(西院)', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}, {'code': '200039788', 'name': '泌尿外科肾癌靶向治疗专病门诊', 'dept1Code': 'cbc348c817edeffab9599ad12205fa78', 'hotDept': False}]}, {'code': '17be7b5423b1782612f4a50608246fb4', 'name': '妇产科', 'subList': [{'code': '200046682', 'name': '特需综合妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200046684', 'name': '特需妇科内分泌门诊2', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048276', 'name': '妇泌中心(西院)', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048413', 'name': '特需普通妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048441', 'name': '特需肿瘤妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048447', 'name': '特需妇科计划生育门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048487', 'name': '特需产科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048521', 'name': '妇科计划生育门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048522', 'name': '综合妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200048523', 'name': '妇科肿瘤门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004078', 'name': '妇产科辅助生育中心', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004073', 'name': '妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004074', 'name': '妇科门诊(西院)', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004075', 'name': '特需妇科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004076', 'name': '特需妇科门诊(西院)1', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004080', 'name': '妇科内分泌门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004081', 'name': '特需妇科内分泌门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004082', 'name': '特需妇科内分泌门诊(西院)', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}, {'code': '200004077', 'name': '产科门诊', 'dept1Code': '17be7b5423b1782612f4a50608246fb4', 'hotDept': False}]}, {'code': '2543ade3aecd3f5a3e2329d068c1d367', 'name': '儿科', 'subList': [{'code': '200004084', 'name': '儿科门诊', 'dept1Code': '2543ade3aecd3f5a3e2329d068c1d367', 'hotDept': False}, {'code': '200004085', 'name': '特需儿科门诊', 'dept1Code': '2543ade3aecd3f5a3e2329d068c1d367', 'hotDept': False}]}, {'code': 'e7391935e2070acf94e87b5b6f104f68', 'name': '变态反应科', 'subList': [{'code': '200004094', 'name': '变态反应科门诊', 'dept1Code': 'e7391935e2070acf94e87b5b6f104f68', 'hotDept': False}, {'code': '200004095', 'name': '特需变态反应科门诊', 'dept1Code': 'e7391935e2070acf94e87b5b6f104f68', 'hotDept': False}]}, {'code': '2feb85b952a4dcd6dbf832100f6ef595', 'name': '五官', 'subList': [{'code': '200048325', 'name': '特需皮肤科门诊2', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200048377', 'name': '皮科激光中心', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200048468', 'name': '普通皮科复诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200048529', 'name': '特需口腔科门诊2', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004107', 'name': '皮肤科白癜风副教授门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004108', 'name': '皮肤科普通皮科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004119', 'name': '美容皮肤科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004086', 'name': '眼科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004087', 'name': '眼科门诊(西院)', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004088', 'name': '特需眼科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004089', 'name': '眼科糖尿病视网膜病专科', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004096', 'name': '口腔科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004097', 'name': '口腔科门诊(西院)', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004101', 'name': '口腔科住院医门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004098', 'name': '口腔科洁牙门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004099', 'name': '特需口腔外科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004100', 'name': '口腔科特需门诊(西院)', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004090', 'name': '耳鼻喉科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004091', 'name': '耳鼻喉科门诊(西院)', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004093', 'name': '特需耳鼻喉科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004102', 'name': '皮科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004103', 'name': '皮科门诊(西院)', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004104', 'name': '皮肤科性病门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}, {'code': '200004106', 'name': '特需皮肤科门诊', 'dept1Code': '2feb85b952a4dcd6dbf832100f6ef595', 'hotDept': False}]}, {'code': '7dafa91626a45481feefb3d1a84c7984', 'name': '中医科', 'subList': [{'code': '200041040', 'name': '特需中医科门诊2', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200048480', 'name': '卫干门诊(中医科)', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200004112', 'name': '中医科针灸室(西院)', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200004110', 'name': '中医科针灸室', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200004109', 'name': '中医科门诊', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200004111', 'name': '中医科门诊(西院)', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}, {'code': '200004113', 'name': '特需中医科门诊1', 'dept1Code': '7dafa91626a45481feefb3d1a84c7984', 'hotDept': False}]}, {'code': '4dcb42d3a6ca39589f20bcd160903ae9', 'name': '营养科', 'subList': [{'code': '200048262', 'name': '临床营养科西院门诊', 'dept1Code': '4dcb42d3a6ca39589f20bcd160903ae9', 'hotDept': False}, {'code': '200047302', 'name': '特需营养科门诊1', 'dept1Code': '4dcb42d3a6ca39589f20bcd160903ae9', 'hotDept': False}, {'code': '200004133', 'name': '营养科咨询门诊', 'dept1Code': '4dcb42d3a6ca39589f20bcd160903ae9', 'hotDept': False}]}, {'code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'name': '专科', 'subList': [{'code': '200040878', 'name': '多发性硬化专科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200040182', 'name': '运动障碍病专科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200048482', 'name': '特需病理科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200048483', 'name': '病理科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004057', 'name': '麻醉科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004124', 'name': '放疗科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004125', 'name': '放疗科门诊(西院)', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004126', 'name': '特需放疗科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004117', 'name': '心理医学科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004118', 'name': '特需心理医学科门诊1', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004123', 'name': '介入治疗门诊(放射科)', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004130', 'name': '超声介入门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004129', 'name': '物理医学康复科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004127', 'name': '物理医学康复科门诊(西院)', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004120', 'name': '肠外肠内营养科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004122', 'name': '特需肠外肠内营养科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004131', 'name': '核医学科门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004132', 'name': '特需核医学门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004055', 'name': '麻醉科', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}, {'code': '200004056', 'name': '麻醉科疼痛门诊', 'dept1Code': 'a4e171f4cf9b6816acdfb9ae62c414d7', 'hotDept': False}]}, {'code': '0551a547cc19d3d09f2e57bd2931b7d0', 'name': '其它', 'subList': [{'code': '200040142', 'name': '肾内科IGA肾病专病门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200048338', 'name': '检验科门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200048491', 'name': '门诊部疑难病会诊中心(东院)', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200048571', 'name': '加速器治疗室(放疗科)(西院)', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200048575', 'name': '生殖中心门诊(西院)', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004013', 'name': '帕金森专病门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004037', 'name': '癫痫门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004021', 'name': '老年医学科门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004038', 'name': '神经外科垂体专病门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004039', 'name': '神经外科脊髓疾病专科门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004048', 'name': '泌尿外科泌尿结石门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004050', 'name': '泌尿外科膀胱癌专科门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004024', 'name': '基本外科肠造口门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004092', 'name': '耳聋基因筛查遗传门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004128', 'name': '特需康复理疗门诊2', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004036', 'name': '疼痛门诊', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004058', 'name': '特需麻醉科门诊2', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004135', 'name': '针灸按摩室(西院)', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200004121', 'name': '肠外肠内营养科门诊(西院)', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}, {'code': '200041160', 'name': '特需放射科门诊1', 'dept1Code': '0551a547cc19d3d09f2e57bd2931b7d0', 'hotDept': False}]}, {'code': '1e452d84823e025229c72c23d100a464', 'name': '国际医疗部', 'subList': [{'code': '200048271', 'name': '国际医疗(儿科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048272', 'name': '国际医疗(预防接种)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048273', 'name': '国际医疗(神经科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048274', 'name': '国际医疗(胸外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048278', 'name': '国际医疗(内分泌科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048279', 'name': '基本外科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048280', 'name': '内分泌科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048281', 'name': '国际医疗(消化内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048282', 'name': '国际医疗(普通内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048283', 'name': '国际医疗(皮肤科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048286', 'name': '消化内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048288', 'name': '国际医疗(感染内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048289', 'name': '国际医疗(变态反应科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048290', 'name': '国际医疗(免疫内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048293', 'name': '国际医疗(中医科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048294', 'name': '国际医疗(呼吸内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048297', 'name': '国际医疗(美容外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048298', 'name': '国际医疗(产科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048299', 'name': '医学美容中心外科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048300', 'name': '国际医疗(血管外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048301', 'name': '核医学科(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048304', 'name': '国际医疗(妇科内分泌)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048308', 'name': '变态（过敏）反应科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048309', 'name': '免疫内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048310', 'name': '国际医疗(骨科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048311', 'name': '口腔科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048312', 'name': '国际医疗(泌尿外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048313', 'name': '国际医疗(核医学科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048314', 'name': '内分泌与生殖妇科中心门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048315', 'name': '国际医疗(血液科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048316', 'name': '国际医疗(美容皮肤科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048317', 'name': '国际医疗(耳鼻喉科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048318', 'name': '国际医疗(神经外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048319', 'name': '肿瘤内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048320', 'name': '耳鼻喉科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048326', 'name': '国际医疗(针灸按摩室)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048327', 'name': '国际医疗(心内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048328', 'name': '国际医疗(口腔科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048329', 'name': '国际医疗(麻醉科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048330', 'name': '神经科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048332', 'name': '呼吸内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048333', 'name': '国际医疗(物理医学康复科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048334', 'name': '心内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048335', 'name': '肾内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048346', 'name': '国际医疗(基本外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048347', 'name': '乳腺外科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048348', 'name': '国际医疗(肾内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048349', 'name': '皮肤科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048350', 'name': '国际医疗(眼科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048352', 'name': '国际医疗(肝脏外科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048353', 'name': '眼科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048355', 'name': '麻醉科(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048356', 'name': '国际医疗(肿瘤内科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048366', 'name': '国际医疗(营养科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048368', 'name': '国际医疗(放射治疗科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048379', 'name': '国际医疗部特约门诊', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048465', 'name': '物理医学康复科(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048467', 'name': '泌尿外科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048470', 'name': '国际医疗(肠外肠内营养科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048485', 'name': '国际医疗(老年医学科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048486', 'name': '普通内科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048513', 'name': '医学美容中心门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048524', 'name': '国际医疗(妇科肿瘤)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048525', 'name': '国际医疗(综合妇科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048526', 'name': '国际医疗(妇科计划生育)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048536', 'name': '骨科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048559', 'name': '国际医疗(放射科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048585', 'name': '老年医学门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200048644', 'name': '儿科门诊(西院国际医疗)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200004114', 'name': '国际医疗(妇科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}, {'code': '200004115', 'name': '国际医疗(心理医学科)', 'dept1Code': '1e452d84823e025229c72c23d100a464', 'hotDept': False}]}]}}
    curr_path = get_all_conf().get('path','curr_dir')
    with open('{}file/{}.json'.format(curr_path,hosCode),'w') as f:
        json.dump(json_data,f,ensure_ascii=False,indent=4)


if __name__ == '__main__':
    pass
