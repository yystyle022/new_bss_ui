# -*- coding=utf-8 -*-
# @Time : 2023/10/20 15:58
# @Author : yangyang
# @File : bss-ui/test_process_five.py


import allure
import random
from common.userstestok import ntrip_send_gga
from common.client_playwright_function import get_server_number_password, auth_active_and_expire_time
from common.playwright_function import online_order_application_new_purchase_common_model, review_online_order_application, get_server_number, write_log_to_allure, screenshot_to_allure


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用---谷歌正式浏览器')
def test_process_five_chrome_browser(chrome_browser):
    '''
    测试新购账号后，可以鉴权和登录，ntrip正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,自动激活自动绑定
    OrderNumber = online_order_application_new_purchase_common_model(chrome_browser, ActiveTime='2', PurchaseSums=f'{random.randint(1, 2)}')
    # 财务审核申请订单
    ActiveTime = review_online_order_application(chrome_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chrome_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(chrome_browser, servernumber=ServerNumber)
    # 验证激活时间和到期时间是否正确
    assert auth_active_and_expire_time(chrome_browser, servernumber=ServerNumber, activetime=ActiveTime) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert ntrip_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用---谷歌测试浏览器')
def test_process_five_chromium_browser(chromium_browser):
    '''
    测试新购账号后，可以鉴权和登录，ntrip正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,自动激活自动绑定
    OrderNumber = online_order_application_new_purchase_common_model(chromium_browser, ActiveTime='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    ActiveTime = review_online_order_application(chromium_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chromium_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(chromium_browser, servernumber=ServerNumber)
    # 验证激活时间和到期时间是否正确
    assert auth_active_and_expire_time(chromium_browser, servernumber=ServerNumber, activetime=ActiveTime) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert ntrip_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用---微软Edge浏览器')
def test_process_five_edge_browser(edge_browser):
    '''
    测试新购账号后，可以鉴权和登录，ntrip正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,自动激活自动绑定
    OrderNumber = online_order_application_new_purchase_common_model(edge_browser, ActiveTime='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    ActiveTime = review_online_order_application(edge_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(edge_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(edge_browser, servernumber=ServerNumber)
    # 验证激活时间和到期时间是否正确
    assert auth_active_and_expire_time(edge_browser, servernumber=ServerNumber, activetime=ActiveTime) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert ntrip_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 实时激活 的正式账号 可以正常ntrip登录使用---火狐浏览器')
def test_process_five_firefox_browser(firefox_browser):
    '''
    测试新购账号后，可以鉴权和登录，ntrip正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,自动激活自动绑定
    OrderNumber = online_order_application_new_purchase_common_model(firefox_browser, ActiveTime='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    ActiveTime = review_online_order_application(firefox_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(firefox_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(firefox_browser, servernumber=ServerNumber)
    # 验证激活时间和到期时间是否正确
    assert auth_active_and_expire_time(firefox_browser, servernumber=ServerNumber, activetime=ActiveTime) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert ntrip_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'
