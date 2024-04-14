# -*- coding=utf-8 -*-
# @Time : 2024/4/14 21:07
# @Author : yangyang
# @File : new_bss_ui/ManagementOfflineOrderReviewBase.py
class ManagementOfflineOrderReviewBase:
    '''
    线下订单审核页面
    '''

    def SearchConditionUserIdXpath(self):
        '''
        查询条件-用户编号
        @return:
        '''
        return "//div[text()=' 用户编号 ']"

    def ChoiceOrderApplicationNumberXpath(self):
        '''
        选择用户申请编号
        @return:
        '''
        return "//li[text()=' 申请单编号 ']"

    def InputOrderApplicationNumberXpath(self):
        '''
        申请单编号输入框
        @return:
        '''
        return "//input[@placeholder='请输入']"

    def AllTabXpath(self):
        '''
        全部Tab
        @return:
        '''
        return "//div[text()='全部']"

    def PendingReviewTabXpath(self):
        '''
        待审核Tab
        @return:
        '''
        return "//div[text()='待审核']"

    def DetailsPageXpath(self, applicationNumber):
        '''
        进入详情页操作
        @return:
        '''
        return f"//td[text()='{applicationNumber}']/../td[15]"

    def DetailPageExaminationPasseXpath(self):
        '''
        审核通过
        @return:
        '''
        return "//span[text()=' 审核通过 ']"

    def DetailPageExaminationNoPasseXpath(self):
        '''
        审核不通过
        @return:
        '''
        return "//span[text()=' 审核驳回 ']"

    def DetailPageReviewRemark(self):
        '''
        审核备注输入
        @return:
        '''
        return "//textarea"

    def SubmitButton(self):
        '''
        提交按钮
        @return:
        '''
        return "//span[text()='提 交']"
