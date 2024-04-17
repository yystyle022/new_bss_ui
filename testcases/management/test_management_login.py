# -*- coding=utf-8 -*-
# @Time : 2023/4/26 10:40
# @Author : yangyang
# @File : bss-ui/test_management_login.py


from page.ManagementLoginPage import *
from page.ManagementPage import go_to_login_page
from page.CommonPageFunction import assert_element_exist
from base.ManagementLeftNavicationBar import ManagementLeftNavicationBar


@allure.feature('管理端登录测试')
def test_login_management_success(browser):
    '''
    谷歌测试浏览器登录管理端-登录成功
    @param chromium_browser:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-登录成功')

    with allure.step('打开管理端进入登陆页面'):
        go_to_login_page(page)

    with allure.step('输入账号'):
        input_account_number(page)

    with allure.step('输入密码'):
        input_password(page)

    with allure.step('点击登录按钮'):
        click_login_button(page)

    with allure.step('验证是否登录成功'):
        assert_element_exist(page, ManagementLeftNavicationBar().serviceProductManagementXpath())


@allure.feature('管理端登录测试')
def test_login_management_account_no_exist_chromium_browser(browser):
    '''
    谷歌测试浏览器登录管理端-登录成功
    @param chromium_browser:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-登录账号不存在')

    with allure.step('打开管理端进入登陆页面'):
        go_to_login_page(page)

    with allure.step('输入账号'):
        input_account_number(page, AccountNumber=managementUsername1)

    with allure.step('输入密码'):
        input_password(page)

    with allure.step('点击登录按钮'):
        click_login_button(page)

    with allure.step('验证提示:账号不存在'):
        assert_element_exist(page, ManagementLoginBase().AccountNoExistToastXpath())
