# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12306-config
   Description :
   Author :       XWH
   date：          2018/2/3
-------------------------------------------------
   Change Activity:
                   2018/2/3:
-------------------------------------------------
"""
__author__ = 'XWH'

# https://www.jianshu.com/p/6b1f94e32713

# python v2.7

import datetime

today = datetime.datetime.now()
tomorrow = today+datetime.timedelta(days=1)
tomorrow = tomorrow.strftime('%Y-%m-%d')
today = today.strftime('%Y-%m-%d')

# 登陆账号信息
username = '自己更新'
password = '自己更新'


# 购票用户信息
username_buy = '自己更新'
user_idcard_buy = '自己更新'
seat_name = '二等座' #'硬座'
ticket_type_zh = '成人票'
choose_seats = '1A'

# 邮箱
# 收件人
email_to = '自己更新@qq.com'

# 发件人
email_from = '自己更新@163.com'
email_passwd = '自己更新'
# 出发时间
train_date = '2018-02-22'#tomorrow
# 出发地点
from_city = '长沙'# '株洲'
# 目的地
to_city = '株洲' #'长沙'


# 高铁座位分布 选座 
# ---------------------------------------------------------------------------------
#              |               |              |               |                |
#  (窗)A       |       B       |        C     |               |        D       |       F(窗)
#              |               |              |               |                |
# -------------------------------------------------  过道  --------------------------
#              |               |              |               |                |
#      1A      |      1B       |       1C     |               |       1D       |      1F
#              |               |              |               |                |
# ---------------------------------------------------------------------------------
#      2A ....
#      3A ....
