# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login.py


import pytest
from common.playwrightFunction import *
from page.ClientLoginPage import ClientLoginPage


@allure.feature('测试登录官网')
@allure.title('测试登录官网-登录成功')
@pytest.mark.regression
def test_login_client_success(chromium_browser):
    ClientLoginPage().client_login_success(chromium_browser)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-密码错误')
@pytest.mark.regression
def test_login_client_password_mistake(chromium_browser):
    ClientLoginPage().client_login_fail(chromium_browser, text='密码错误！', username=clientUsername, password=clientMistakePassword)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-账号不存在')
@pytest.mark.regression
def test_login_client_username_no_exist(chromium_browser):
    ClientLoginPage().client_login_fail(chromium_browser, text='账号不存在！', username=clientNoExistUsername, password=clientPassword)
