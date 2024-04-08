# -*- coding=utf-8 -*-
# @Time : 2024/4/8 18:15
# @Author : yangyang
# @File : new_bss_ui/ManagementLoginPage.py


from base.ManagementLoginBase import *
from common.playwrightFunction import *
from common.allure_function import write_log_to_allure_report
from base.ManagementLeftNavicationBar import ManagementLeftNavicationBar


def input_account_number(page, phoneNumber=managementUsername):
    '''
    输入账号
    @param page:
    @param phoneNumber:
    @return:
    '''
    page.fill(ManagementLoginBase().AccountNumberInputFrameXpath(), phoneNumber)
    write_log_to_allure_report(page, f"输入账号：{phoneNumber}")


def input_password(page, password=managementPassword):
    '''
    输入密码
    @param page:
    @param password:
    @return:
    '''
    page.fill(ManagementLoginBase().PasswordInputFrameXpath(), password)
    write_log_to_allure_report(page, f"输入密码：{password}")


def click_login_button(page):
    '''
    点击登录
    @param page:
    @return:
    '''
    page.click(ManagementLoginBase().LoginButtonXpath())
    write_log_to_allure_report(page, "点击登录按钮")


def assert_login_success(page):
    '''
    断言登录成功
    @param page:
    @return:
    '''
    try:
        assert page.wait_for_selector(ManagementLeftNavicationBar().serviceProductManagementXpath(), timeout=5000), '登录失败'
        write_log_to_allure_report(page, '登录成功')
    except Exception as error:
        write_log_to_allure_report(page, f'登录失败：{error}')
