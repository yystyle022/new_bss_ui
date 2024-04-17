# -*- coding=utf-8 -*-
# @Time : 2024/4/17 9:33
# @Author : yangyang
# @File : new_bss_ui/test_management_try_order_application.py
import allure
from page.ManagementInstanceListPage import query_userId, get_instance_list_rank_try_account_number
from page.ManagementPage import go_to_server_order_page, go_to_instance_list_page
from page.ManagementServiceOrderPage import add_try_order_application


@allure.feature('管理端试用订单申请')
def test_try_order_application_liqing_one(browser_login_management, get_user_id, get_random_number):
    '''
    管理端添加试用订单申请-厘清试用账号申请
    @param browser_login_management:
    @param get_user_id:
    @param get_random_number:
    @return:
    '''
    number = get_random_number
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-试用账号申请成功，购买{number}个厘清试用账号，账号类别：自动激活，自动绑定，ntrip或SDK')

    with allure.step('打开管理端进入服务订单页面'):
        go_to_server_order_page(page)

    with allure.step('开始添加试用订单'):
        add_try_order_application(page, userId=get_user_id, number=number)

    with allure.step('去实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询用户下的实例'):
        query_userId(page, userId=get_user_id)

    with allure.step('获取实例列表的第一个实例下的试用账号数量'):
        tryServerNum = get_instance_list_rank_try_account_number(page)

    with allure.step('判断试用数量是否与申请的一致'):
        assert tryServerNum == number, f'试用账号个数不正确，申请的数量为：{number}，实际获取的数量为：{tryServerNum}'
