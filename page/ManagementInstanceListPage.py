# -*- coding=utf-8 -*-
# @Time : 2024/4/16 11:07
# @Author : yangyang
# @File : new_bss_ui/ManagementInstanceListPage.py
from time import sleep

import allure

from page.CommonPageFunction import *
from common.allure_function import write_log_to_allure_report
from base.ManagementInstanceListBase import ManagementInstanceListBase


def input_user_id(page, useId):
    '''
    输入用户编号
    @param page:
    @param useId:
    @return:
    '''
    page.fill(ManagementInstanceListBase().UserIdInputFrameXpath(), f"{useId}")
    write_log_to_allure_report(page, text=f"输入的用户编号为：{useId}")


def input_instance_id(page, instanceId):
    '''
    输入实例ID
    @param page:
    @param instanceId:
    @return:
    '''
    page.fill(ManagementInstanceListBase().InstanceIdInputFrameXpath(), f"{instanceId}")
    write_log_to_allure_report(page, text=f"输入的实例ID为：{instanceId}")


def click_query_button(page):
    '''
    点击查询按钮
    @param page:
    @return:
    '''
    page.click(ManagementInstanceListBase().QueryButtonXpath())
    write_log_to_allure_report(page, text="点击查询按钮")


def click_list_instance_id(page, instanceId):
    '''
    点击实例ID
    @param page:
    @param instanceId:
    @return:
    '''
    page.click(ManagementInstanceListBase().InstanceIdXpath(instanceId))
    write_log_to_allure_report(page, text=f"点击实例ID:{instanceId}")


def query_instance(page, instanceId):
    '''
    查询实例ID
    @param page:
    @param instanceId:
    @return:
    '''
    with allure.step('输入实例ID'):
        input_instance_id(page, instanceId)

    with allure.step('点击查询按钮'):
        click_query_button(page)

    with allure.step('查看实例是否存在'):
        assert_element_exist(page, ManagementInstanceListBase().InstanceIdXpath(instanceId))


def query_userId(page, userId):
    '''
    按照用户编号查询
    @param page:
    @param userId:
    @return:
    '''
    with allure.step('输入用户编号'):
        input_user_id(page, userId)

    with allure.step('点击查询按钮'):
        click_query_button(page)


def get_formal_account_number(page, instanceId):
    '''
    获取实例下的正式账号数量
    @param page:
    @param instanceId:
    @return:
    '''
    accountNumber = int(get_element_content(page, ManagementInstanceListBase().FormalServerNumberXpath(instanceId), log=False))
    write_log_to_allure_report(page, text=f'{instanceId}实例下的正式账号个数为：{accountNumber}')
    return accountNumber


def get_try_account_number(page, instanceId):
    '''
    获取实例下的试用账号数量
    @param page:
    @param instanceId:
    @return:
    '''
    accountNumber = int(get_element_content(page, ManagementInstanceListBase().TryUseServerNumberXpath(instanceId)))
    write_log_to_allure_report(page, text=f'{instanceId}实例下的试用账号个数为：{accountNumber}')
    return accountNumber


def get_instance_list_rank_try_account_number(page, rank=1):
    '''
    获取实例列表第几行的试用账号数量
    @param page:
    @param rank:
    @return:
    '''
    instanceId = get_element_content(page, ManagementInstanceListBase().InstanceListRankInstanceIdXpath(rank), log=False)
    accountNumber = int(get_element_content(page, ManagementInstanceListBase().TryUseServerNumberXpath(instanceId), log=False))
    write_log_to_allure_report(page, text=f'{instanceId}实例下的试用账号个数为：{accountNumber}')
    return accountNumber
