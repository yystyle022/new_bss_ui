# -*- coding=utf-8 -*-
# @Time : 2024/4/17 9:34
# @Author : yangyang
# @File : new_bss_ui/ManagementServiceOrderPage.py
import allure
from page.CommonPageFunction import *
from common.allure_function import write_log_to_allure_report
from base.ManagementServiceOrderBase import ManagementServiceOrderBase
from page.ManagementPage import go_to_server_order_page, go_to_instance_list_page


def management_service_order_page_input_order_number(page, orderNumber):
    '''
    输入订单号码
    @param page:
    @param orderNumber:
    @return:
    '''
    page.fill(ManagementServiceOrderBase().QueryConitionOrderNumberInputFrameXpath(), f'{orderNumber}')
    write_log_to_allure_report(page, text=f'输入订单号：{orderNumber}')


def management_service_order_page_input_user_id(page, userId):
    '''
    输入用户编号
    @param page:
    @param userId:
    @return:
    '''
    page.fill(ManagementServiceOrderBase().QueryConitionUserIdInputFrameXpath(), f'{userId}')
    write_log_to_allure_report(page, text=f'输入用户编号：{userId}')


def management_service_order_page_click_query_button(page):
    '''
    点击查询按钮
    @param page:
    @return:
    '''
    page.click(ManagementServiceOrderBase().QueryButtonXpath())
    write_log_to_allure_report(page, text='点击查询按钮')


def click_add_try_order_button(page):
    '''
    点击添加试用订单按钮
    @param page:
    @return:
    '''
    page.click(ManagementServiceOrderBase().AddTryOrderButtonXpath())
    write_log_to_allure_report(page, text='点击添加试用订单按钮')


def add_try_order_page_choice_product_name(page, productName):
    '''
    选择产品名称
    @param page:
    @param productName: 1-厘清；2-分明；3-星璨
    @return:
    '''
    # 点击产品名称选择框，弹出产品名称选择列表
    page.click(ManagementServiceOrderBase().AddTryOrderPageServiceProductChoiceFrameXpath())
    write_log_to_allure_report(page, text="点击产品名称选择框，弹出产品名称选择列表")
    if productName == 1:
        page.click(ManagementServiceOrderBase().AddTryOrderPageServiceProductChoiceLiQingXpath())
        write_log_to_allure_report(page, text="选择的产品名称为厘清")
    elif productName == 2:
        page.click(ManagementServiceOrderBase().AddTryOrderPageServiceProductChoiceFenMingXpath())
        write_log_to_allure_report(page, text="选择的产品名称为分明")
    elif productName == 3:
        page.click(ManagementServiceOrderBase().AddTryOrderPageServiceProductChoiceOrionXpath())
        write_log_to_allure_report(page, text="选择的产品名称为星璨")
    else:
        assert False, f"选择的产品名称为：{productName},产品名称选择不正确"


def add_try_order_page_choice_link_method(page, linkMethod):
    '''
    选择链接方式
    @param page:
    @param linkMethod: 1-Ntrip或Sdk；2-Ntrip；3-Sdk
    @return:
    '''
    if linkMethod == 1:
        page.click(ManagementServiceOrderBase().AddTryOrderPageLinkMethodChoiceNtripOrSdkXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Ntrip或Sdk")
    elif linkMethod == 2:
        page.click(ManagementServiceOrderBase().AddTryOrderPageLinkMethodChoiceNtripXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Ntrip")
    elif linkMethod == 3:
        page.click(ManagementServiceOrderBase().AddTryOrderPageLinkMethodChoiceSdkXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Sdk")
    else:
        assert False, f"选择的链接方式为：{linkMethod},链接方式选择不正确"


def add_try_order_page_choice_active_method(page, activeMethod):
    '''
    选择激活方式
    @param page:
    @param activeMethod: 1-自动激活；2-手动激活
    @return:
    '''
    if activeMethod == 1:
        page.click(ManagementServiceOrderBase().AddTryOrderPageActiveMethodChoiceAutoActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活方式为：自动激活")
    elif activeMethod == 2:
        page.click(ManagementServiceOrderBase().AddTryOrderPageActiveMethodChoiceManaulActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活方式为：手动激活")
    else:
        assert False, f"选择的激活方式为：{activeMethod},激活方式选择不正确"


def add_try_order_page_choice_bind_method(page, bindMethod):
    '''
    选择绑定方式
    @param page:
    @param bindMethod: 1-自动绑定；2-手动绑定
    @return:
    '''
    if bindMethod == 1:
        page.click(ManagementServiceOrderBase().AddTryOrderPageBindMethodChoiceAutoBindXpath())
        write_log_to_allure_report(page, text=f"选择的绑定方式为：自动绑定")
    elif bindMethod == 2:
        page.click(ManagementServiceOrderBase().AddTryOrderPageBindMethodChoiceManaulBindXpath())
        write_log_to_allure_report(page, text=f"选择的绑定方式为：手动绑定")
    else:
        assert False, f"选择的绑定方式为：{bindMethod},绑定方式选择不正确"


def add_try_order_page_choice_order_use(page, use):
    '''
    选择订单用途
    @param page:
    @param use: 1-客户使用账号；2-内部测试账号
    @return:
    '''
    if use == 1:
        page.click(ManagementServiceOrderBase().AddTryOrderPageOrderUseChoiceCustomerUseXpath())
        write_log_to_allure_report(page, text='选择的订单用途为：客户使用账号')
    elif use == 2:
        page.click(ManagementServiceOrderBase().AddTryOrderPageOrderUseChoiceInternalTestUseXpath())
        write_log_to_allure_report(page, text='选择的订单用途为：内部测试账号')
    else:
        assert False, f"选择的订单用途为：{use},订单用途选择不正确"


def add_try_order_application(page, userId, productName=1, linkMethod=1, activeMethod=1, bindMethod=1, number=1, duration=1,
                              price=1.21, salePersonName='UI测试扩容订单', orderRemark='UI测试扩容订单审核', orderUse=2):
    '''
    试用订单申请
    @param page:
    @param userId:
    @param productName:
    @param linkMethod:
    @param activeMethod:
    @param bindMethod:
    @param number:
    @param duration:
    @param price:
    @param salePersonName:
    @param orderRemark:
    @param orderUse:
    @return:
    '''

    with allure.step('点击服务订单列表的添加试用订单按钮'):
        click_add_try_order_button(page)

    with allure.step('输入客户编号'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPageUserIdInputFrameXpath(), userId, f'输入客户编号{userId}')

    with allure.step('选择服务产品'):
        add_try_order_page_choice_product_name(page, productName)

    with allure.step('选择链接方式'):
        add_try_order_page_choice_link_method(page, linkMethod)

    with allure.step('选择激活方式'):
        add_try_order_page_choice_active_method(page, activeMethod)

    with allure.step('选择绑定方式'):
        add_try_order_page_choice_bind_method(page, bindMethod)

    with allure.step('填写购买数量'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPagePurchaseNumberInputFrameXpath(), number, f'填写购买账号的数量为：{number}')

    with allure.step('填写购买时长'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPagePurchaseDurationInputFrameXpath(), duration, f'账号的购买时长为：{duration}天')

    with allure.step('填写购买价格'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPagePurchasePriceInputFrameXpath(), price, f'账号的购买价格为：{price}')

    with allure.step('填写销售人员'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPageSalePeopleInputFrameXpath(), salePersonName, f'销售人员为：{salePersonName}')

    with allure.step('填写备注信息'):
        input_operation(page, ManagementServiceOrderBase().AddTryOrderPageRemarkInputFrameXpath(), orderRemark, f'备注信息为：{orderRemark}')

    with allure.step('选择账号的用途'):
        add_try_order_page_choice_order_use(page, orderUse)

    with allure.step('点击确定按钮提交'):
        click_operation(page, ManagementServiceOrderBase().AddTryOrderPageSureButtonXpath(), '点击确定按钮')

    with allure.step('二次确认弹窗，点击确定按钮'):
        click_operation(page, ManagementServiceOrderBase().AddTryOrderPageSecondSureButtonXpath(), '二次确认弹窗，点击确定按钮')
