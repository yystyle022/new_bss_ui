# -*- coding=utf-8 -*-
# @Time : 2024/4/14 21:02
# @Author : yangyang
# @File : new_bss_ui/ManagementOfflineOrderReviewBase.py
import allure
from common.allure_function import write_log_to_allure_report
from base.ManagementOfflineOrderReviewBase import ManagementOfflineOrderReviewBase


def click_pending_review_tab(page):
    '''
    点击待审核TAB
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().PendingReviewTabXpath())
    write_log_to_allure_report(page, text='点击待审核TAB')


def click_user_id(page):
    '''
    点击用户编号查询条件
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().SearchConditionUserIdXpath())
    write_log_to_allure_report(page, text='点击用户编号查询条件')


def click_order_application_number(page):
    '''
    点击申请单编号查询
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().ChoiceOrderApplicationNumberXpath())
    write_log_to_allure_report(page, text='点击申请单编号查询')


def input_order_application_number(page, orderApplicationNumber):
    '''
    输入订单申请编号
    @param page:
    @return:
    '''
    page.fill(ManagementOfflineOrderReviewBase().InputOrderApplicationNumberXpath(), orderApplicationNumber)
    write_log_to_allure_report(page, text=f'输入订单申请编号为：{orderApplicationNumber}')


def click_in_to_detail_button(page, orderApplicationNumber):
    '''
    点击进入详情页面
    @param page:
    @param orderApplicationNumber:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().DetailsPageXpath(orderApplicationNumber))
    write_log_to_allure_report(page, text=f'进入订单{orderApplicationNumber}详情页面')


def click_review_pass(page):
    '''
    点击审核通过
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().DetailPageExaminationPasseXpath())
    write_log_to_allure_report(page, text='选择审核通过按钮')


def input_review_remark(page, remark):
    '''
    输入审核意见
    @param page:
    @param remark:
    @return:
    '''
    page.fill(ManagementOfflineOrderReviewBase().DetailPageReviewRemark(), remark)
    write_log_to_allure_report(page, text=f'输入订单审核意见为：{remark}')


def click_submit_button(page):
    '''
    点击提交按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderReviewBase().SubmitButton())
    write_log_to_allure_report(page, text='点击提交按钮')


def review_application_order(page, orderApplicationNumber, remark='UI测试用例-续费订单审核通过'):
    '''
    审核订单
    @param page:
    @param orderApplicationNumber:
    @return:
    '''
    with allure.step('点击订单详情按钮进入详情页面'):
        click_in_to_detail_button(page, orderApplicationNumber)

    with allure.step('选择审核通过'):
        click_review_pass(page)

    with allure.step('输入审核意见'):
        input_review_remark(page, remark)

    with allure.step('点击提交按钮'):
        click_submit_button(page)
