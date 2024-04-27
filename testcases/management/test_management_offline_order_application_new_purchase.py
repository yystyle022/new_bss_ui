# -*- coding=utf-8 -*-
# @Time : 2023/10/7 17:25
# @Author : yangyang
# @File : bss-ui/test_management_offline_order_application_new_purchase.py
import allure

from page.ClientPage import go_to_cm_service_instance_page
from page.CommonPageFunction import *
from common.allure_function import write_log_to_allure_report
from base.ClientCmInstanceListBase import ClientInstanceList
from base.ManagementServiceOrderBase import ManagementServiceOrderBase
from page.ManagementPage import go_to_offline_order_page, go_to_order_review_page, go_to_server_order_page
from page.ManagementOfflineOrderReviewPage import click_pending_review_tab, review_application_order
from page.ManagementOfflineOrderApplicationPage import go_to_pending_review_page, get_application_number, offline_order_application_new_purchase
from page.ManagementServiceOrderPage import management_service_order_page_input_user_id, management_service_order_page_click_query_button


@allure.feature('管理端线下订单申请-新购')
def test_offline_order_application_new_purchase_liqing_login(browser_login_management, get_user_id, get_random_number):
    '''
    线下订单申请测试用例---新购厘清账号，登录成功
    @param chromium_browser:
    @return:
    '''
    number = get_random_number
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-新购订单申请成功，购买{number}个厘清账号，账号类别：通用模式，自动激活，自动绑定，ntrip或SDK，无测试期，非实时激活')

    with allure.step('打开管理端网址，登陆成功'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('新购订单申请'):
        offline_order_application_new_purchase(page, userId=get_user_id, number=number)

    with allure.step('进入待审核列表'):
        go_to_pending_review_page(page)

    with allure.step('获取申请的订单号'):
        OrderApplicationNumber = get_application_number(page)

    with allure.step('进入订单审核页面'):
        go_to_order_review_page(page)

    with allure.step('点击待审核Tab,进入待审核列表页面'):
        click_pending_review_tab(page)

    with allure.step('审核订单'):
        review_application_order(page, OrderApplicationNumber)

    with allure.step('进入服务订单页面'):
        go_to_server_order_page(page)

    with allure.step('查询条件输入用户编号'):
        management_service_order_page_input_user_id(page, userId=get_user_id)

    with allure.step('点击查询按钮查询订单'):
        management_service_order_page_click_query_button(page)

    with allure.step('点击查询出的第一条订单的详情按钮，进入详情页面'):
        click_operation(page, ManagementServiceOrderBase().ServiceOrderListFirstOrderDetailButtonXpath(), text='点击订单详情进入详情页面')

    with allure.step('获取差分账号'):
        serverNumber = get_element_content(page, ManagementServiceOrderBase().ServiceOrderDetailFirstServerNumberXpath(), text='获取差分账号')

# @allure.feature('管理端线下订单申请-新购')
# def test_offline_order_application_new_purchase_liqing_two(browser_login_management, get_user_id, get_random_number):
#     '''
#     线下订单申请测试用例---新购厘清
#     @param chromium_browser:
#     @return:
#     '''
#     number = get_random_number
#     browser_name = browser_login_management['name']
#     page = browser_login_management['page']
#     allure.dynamic.title(f'{browser_name}浏览器-新购订单申请成功，购买{number}个厘清账号，账号类别：通用模式，自动激活，手动绑定，ntrip或SDK，无测试期，非实时激活')
#
#     with allure.step('打开管理端网址，登陆成功'):
#         write_log_to_allure_report(page, text='登录管理端成功')
#
#     with allure.step('进入订单申请页面'):
#         go_to_offline_order_page(page)
#
#     with allure.step('新购订单申请'):
#         offline_order_application_new_purchase(page, userId=get_user_id, bindMethod=2, number=number)
#
#     with allure.step('进入待审核列表'):
#         go_to_pending_review_page(page)
#
#     with allure.step('获取申请的订单号'):
#         OrderApplicationNumber = get_application_number(page)
#
#     with allure.step('进入订单审核页面'):
#         go_to_order_review_page(page)
#
#     with allure.step('点击待审核Tab,进入待审核列表页面'):
#         click_pending_review_tab(page)
#
#     with allure.step(f'审核订单'):
#         review_application_order(page, OrderApplicationNumber)
#
#
# @allure.feature('管理端线下订单申请-新购')
# def test_offline_order_application_new_purchase_fenming_one(browser_login_management, get_user_id, get_random_number):
#     '''
#     线下订单申请测试用例---新购分明
#     @param chromium_browser:
#     @return:
#     '''
#     number = get_random_number
#     browser_name = browser_login_management['name']
#     page = browser_login_management['page']
#     allure.dynamic.title(f'{browser_name}浏览器-新购订单申请成功，购买{number}个分明账号，账号类别：通用模式，自动激活，手动绑定，ntrip或SDK，无测试期，非实时激活')
#
#     with allure.step('打开管理端网址，登陆成功'):
#         write_log_to_allure_report(page, text='登录管理端成功')
#
#     with allure.step('进入订单申请页面'):
#         go_to_offline_order_page(page)
#
#     with allure.step('新购订单申请'):
#         offline_order_application_new_purchase(page, userId=get_user_id, bindMethod=2, number=number)
#
#     with allure.step('进入待审核列表'):
#         go_to_pending_review_page(page)
#
#     with allure.step('获取申请的订单号'):
#         OrderApplicationNumber = get_application_number(page)
#
#     with allure.step('进入订单审核页面'):
#         go_to_order_review_page(page)
#
#     with allure.step('点击待审核Tab,进入待审核列表页面'):
#         click_pending_review_tab(page)
#
#     with allure.step(f'审核订单'):
#         review_application_order(page, OrderApplicationNumber)
