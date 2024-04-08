# -*- coding=utf-8 -*-
# @Time : 2023/4/26 10:40
# @Author : yangyang
# @File : bss-ui/test_management_login.py


import pytest
from page.ManagementLoginPage import *
from page.ManagementPage import go_to_login_page


@allure.feature('管理端登录测试')
@allure.title('谷歌测试浏览器-登录成功')
def test_login_management_success_chromium_browser(chromium_browser):
    '''
    谷歌测试浏览器登录管理端-登录成功
    @param chromium_browser:
    @return:
    '''
    with allure.step('打开管理端进入登陆页面'):
        go_to_login_page(chromium_browser)

    with allure.step('输入账号'):
        input_account_number(chromium_browser)

    with allure.step('输入密码'):
        input_password(chromium_browser)

    with allure.step('点击登录按钮'):
        click_login_button(chromium_browser)

    with allure.step('验证是否登录成功'):
        assert_login_success(chromium_browser)


