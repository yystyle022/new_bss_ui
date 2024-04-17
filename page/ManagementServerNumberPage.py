# -*- coding=utf-8 -*-
# @Time : 2024/4/15 21:53
# @Author : yangyang
# @File : new_bss_ui/ManagementServerNumberPage.py
import re

import allure
from page.CommonPageFunction import *
from common.allure_function import write_log_to_allure_report
from base.ManagementServerNumberBase import ManagementServerNumberBase


def choice_server_number_type(page, serverNumberType=1):
    '''
    选择账号类型
    @param page:
    @param serverNumberType:
    @return:
    '''
    click_operation(page, ManagementServerNumberBase().SearchConditionServerNumberTypeChoiceXpath(), text='点击账号类型选择框，弹出账号类型下拉选择列表')
    if serverNumberType == 1:
        click_operation(page, ManagementServerNumberBase().SearchConditionServerNumberTypeChoiceFormalXpath(), text='选择账号类型为：正式账号')
    elif serverNumberType == 2:
        click_operation(page, ManagementServerNumberBase().SearchConditionServerNumberTypeChoiceTryXpath(), text='选择账号类型为：试用账号')
    else:
        assert False, f'账号类型选择的是：{serverNumberType},此账号类型不正确'


def server_number_page_query_condition_choice_product_name(page, productName=1):
    '''
    选择账号类型
    @param page:
    @param serverNumberType:
    @return:
    '''
    click_operation(page, ManagementServerNumberBase().SearchConditionProductNameChoiceXpath(), text='点击产品名称选择框，弹出产品名称下拉选择列表')
    if productName == 1:
        click_operation(page, ManagementServerNumberBase().SearchConditionProductNameChoiceLiQingXpath(), text='选择产品名称为：厘清')
    elif productName == 2:
        click_operation(page, ManagementServerNumberBase().SearchConditionProductNameChoiceFenMingXpath(), text='选择产品名称为：分明')
    elif productName == 3:
        click_operation(page, ManagementServerNumberBase().SearchConditionProductNameChoiceOrionXpath(), text='选择产品名称为：星璨')
    else:
        assert False, f'产品名称选择的是：{productName},此产品名称不正确'


def search_condition_input_instance_id(page, instanceId):
    '''
    查询条件实例ID输入框输入实例ID
    @param page:
    @param instanceId:
    @return:
    '''
    page.fill(ManagementServerNumberBase().SearchConditionInstanceIdInputXpath(), f"{instanceId}")
    write_log_to_allure_report(page, text=f"输入的实例ID为：{instanceId}")


def search_condition_input_server_number(page, serverNumber):
    '''
    查询条件-输入差分账号
    @param page:
    @param serverNumber:
    @return:
    '''
    page.fill(ManagementServerNumberBase().SearchConditionServerNumberedInputXpath(), f"{serverNumber}")
    write_log_to_allure_report(page, text=f"输入的差分账号为：{serverNumber}")


def click_search_button(page):
    '''
    点击查询按钮
    @param page:
    @return:
    '''
    page.click(ManagementServerNumberBase().SearchButtonXpath())
    write_log_to_allure_report(page, text='点击查询按钮查询')


def get_random_server_number_current_page(page, number):
    '''
    获取当前页面的随机账号
    @param page:
    @param number:
    @return:
    '''
    serverNumber = get_element_content(page, ManagementServerNumberBase().ListServerNumberXpath(number), log=False)
    write_log_to_allure_report(page, text=f'获取的差分账号为：{serverNumber}')
    return serverNumber


def get_instance_id_from_server_number_page(page, serverNumber):
    '''
    获取当账号的实例ID
    @param page:
    @param number:
    @return:
    '''
    instanceId = get_element_content(page, ManagementServerNumberBase().ServerNumberListInstanceIdXpath(serverNumber), log=False)
    write_log_to_allure_report(page, text=f'获取差分账号的实例ID为：{instanceId}')
    return instanceId


def query_server_number(page, serverNumber):
    '''
    查询账号
    @param page:
    @param serverNumber:
    @return:
    '''
    with allure.step('输入差分账号'):
        search_condition_input_server_number(page, serverNumber)

    with allure.step('点击查询按钮'):
        click_search_button(page)


def get_server_number_purchase_duration(page, serverNumber):
    '''
    获取差分账号购买时长
    @param page:
    @param serverNumber:
    @return:
    '''
    element = page.query_selector(ManagementServerNumberBase().PurchaseDurationXpath(serverNumber))
    if element is None:
        # 处理element为None的情况
        write_log_to_allure_report(page, text=f'找不到账号{serverNumber}的购买时长的元素')
        assert False, f'找不到账号{serverNumber}的购买时长的元素'

    purchaseDuration = element.text_content()
    if purchaseDuration is None:
        # 处理text_content为None的情况
        write_log_to_allure_report(page, text=f'账号{serverNumber}的购买时长文本内容为空')
        assert False, f'账号{serverNumber}的购买时长文本内容为空'

    # 截取月和天的长度
    months = re.search(r'(\d+)月', purchaseDuration)
    days = re.search(r'(\d+)天', purchaseDuration)
    month_num = int(months.group(1)) if months else 0
    day_num = int(days.group(1)) if days else 0

    # 截图写入日志
    write_log_to_allure_report(page, text=f'账号{serverNumber}的购买时长为：{month_num}月{day_num}天')
    return {"monthNumber": month_num, "dayNumber": day_num}
