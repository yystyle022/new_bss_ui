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


def assert_element_exist(page, element):
    '''
    断言元素存在
    @param page:
    @return:
    '''
    try:
        page.wait_for_selector(element, timeout=2000)
        write_log_to_allure_report(page, '登录成功')
    except Exception:
        write_log_to_allure_report(page, f'登录失败')
        assert False, f"登陆失败，未找到元素{element}"
