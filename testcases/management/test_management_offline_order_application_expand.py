# -*- coding=utf-8 -*-
# @Time : 2023/10/12 9:40
# @Author : yangyang
# @File : bss-ui/test_management_offline_order_application_expand.py
from time import sleep

import allure
from common.allure_function import write_log_to_allure_report
from page.ManagementInstanceListPage import query_instance, get_formal_account_number
from page.ManagementPage import go_to_offline_order_page, go_to_order_review_page, go_to_instance_list_page
from page.ManagementOfflineOrderReviewPage import click_pending_review_tab, review_application_order
from page.ManagementOfflineOrderApplicationPage import go_to_pending_review_page, get_application_number, offline_order_application_expand


@allure.feature('管理端线下订单申请-实例扩容账号')
def test_offline_order_application_liqing_expand(browser_login_management, get_user_id, get_random_number, get_expand_liqing_instanceId):
    '''
    线下订单申请测试用例---厘清实例扩容
    @param browser_login_management:
    @param get_user_id: 用户编号
    @return:
    '''
    expandNumber = get_random_number
    instanceId = get_expand_liqing_instanceId
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-扩容厘清账号-申请成功，实例{instanceId}扩容{expandNumber}个账号')

    with allure.step('打开管理端网址，登陆成功'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容前的账号数量'):
        beforeExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('扩容订单申请'):
        offline_order_application_expand(page, get_user_id, instanceId, number=expandNumber)

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

    with allure.step('返回实例列表'):
        go_to_instance_list_page(page)

    with allure.step('再次查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容后的账号数量'):
        afterExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('判断扩容的数量是否正确'):
        assert afterExpandNumber == beforeExpandNumber + expandNumber


@allure.feature('管理端线下订单申请-实例扩容账号')
def test_offline_order_application_fenming_expand(browser_login_management, get_user_id, get_random_number, get_expand_fenming_instanceId):
    '''
    线下订单申请测试用例---分明实例扩容
    @param browser_login_management:
    @param get_user_id: 用户编号
    @return:
    '''
    expandNumber = get_random_number
    instanceId = get_expand_fenming_instanceId
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-扩容分明账号-申请成功，实例{instanceId}扩容{expandNumber}个账号')

    with allure.step('打开管理端网址，登陆成功'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容前的账号数量'):
        beforeExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('扩容订单申请'):
        offline_order_application_expand(page, get_user_id, instanceId, productName=2, number=expandNumber)

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

    with allure.step('返回实例列表'):
        go_to_instance_list_page(page)

    with allure.step('再次查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容后的账号数量'):
        afterExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('判断扩容的数量是否正确'):
        assert afterExpandNumber == beforeExpandNumber + expandNumber


@allure.feature('管理端线下订单申请-实例扩容账号')
def test_offline_order_application_orion_expand(browser_login_management, get_user_id, get_random_number, get_expand_orion_instanceId):
    '''
    线下订单申请测试用例---星璨实例扩容
    @param browser_login_management:
    @param get_user_id: 用户编号
    @return:
    '''
    expandNumber = get_random_number
    instanceId = get_expand_orion_instanceId
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-扩容星璨账号-申请成功，实例{instanceId}扩容{expandNumber}个账号')

    with allure.step('打开管理端网址，登陆成功'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容前的账号数量'):
        beforeExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('扩容订单申请'):
        offline_order_application_expand(page, get_user_id, instanceId, productName=3, number=expandNumber)

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

    with allure.step('返回实例列表'):
        go_to_instance_list_page(page)
        sleep(20)

    with allure.step('再次查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('获取扩容后的账号数量'):
        afterExpandNumber = get_formal_account_number(page, instanceId)

    with allure.step('判断扩容的数量是否正确'):
        assert afterExpandNumber == beforeExpandNumber + expandNumber
