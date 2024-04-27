# -*- coding=utf-8 -*-
# @Time : 2024/4/8 18:15
# @Author : yangyang
# @File : new_bss_ui/ManagementLoginPage.py
import allure
from page.CommonPageFunction import *
from base.ManagementLoginBase import *
from common.playwright_function import *
from common.allure_function import write_log_to_allure_report
from page.ManagementPage import go_to_home_page


def input_account_number(page, AccountNumber):
    '''
    输入账号
    @param page:
    @param phoneNumber:
    @return:
    '''
    input_operation(page, ManagementLoginBase().AccountNumberInputFrameXpath(), AccountNumber, f"输入账号：{AccountNumber}")


def input_password(page, password):
    '''
    输入密码
    @param page:
    @param password:
    @return:
    '''
    input_operation(page, ManagementLoginBase().PasswordInputFrameXpath(), password, f"输入登录密码：{password}")


def click_login_button(page):
    '''
    点击登录
    @param page:
    @return:
    '''
    click_operation(page, ManagementLoginBase().LoginButtonXpath(), "点击登录按钮")


def management_login(page, managementUsername, managementPassword, element):
    '''
    管理端登录
    @param page:
    @param managementUsername:
    @param managementPassword:
    @param element:
    @return:
    '''
    with allure.step('打开管理端进入首页'):
        go_to_home_page(page)

    with allure.step(f'输入账号：{managementUsername}'):
        input_account_number(page, managementUsername)

    with allure.step(f'输入密码：{managementPassword}'):
        input_password(page, managementPassword)

    with allure.step('点击登录按钮'):
        click_login_button(page)

    with allure.step('验证页面元素是否存在'):
        assert_element_exist(page, element)
