# -*- coding=utf-8 -*-
# @Time : 2024/4/17 9:39
# @Author : yangyang
# @File : new_bss_ui/ManagementServiceOrderBase.py
class ManagementServiceOrderBase:
    '''
    服务订单页面
    '''

    def QueryConitionOrderNumberInputFrameXpath(self):
        '''
        查询条件-订单号输入框
        @return:
        '''
        return "//input[@placeholder='订单号']"

    def QueryConitionUserIdInputFrameXpath(self):
        '''
        查询条件-用户编号输入框
        @return:
        '''
        return "//input[@placeholder='请输入']"

    def QueryButtonXpath(self):
        '''
        查询按钮
        @return:
        '''
        return "//span[text()='查 询']"

    def AddTryOrderButtonXpath(self):
        '''
        添加试用订单按钮
        @return:
        '''
        return "//span[text()='添加试用订单']"

    def AddTryOrderPageUserIdInputFrameXpath(self):
        '''
        添加试用订单页面-客户编号输入框
        @return:
        '''
        return "//label[@title='客户编号']/../following-sibling::div//input"

    def AddTryOrderPageServiceProductChoiceFrameXpath(self):
        '''
        添加试用订单页面-服务产品选择框
        @return:
        '''
        return "//label[@title='服务产品']/../following-sibling::div//div[text()='请选择']"

    def AddTryOrderPageServiceProductChoiceLiQingXpath(self):
        '''
        添加试用订单页面-服务产品选择厘清
        @return:
        '''
        return "//li[text()=' 厘清/Locate-CM ']"

    def AddTryOrderPageServiceProductChoiceFenMingXpath(self):
        '''
        添加试用订单页面-服务产品选择分明
        @return:
        '''
        return "//li[text()=' 分明/Locate-DM ']"

    def AddTryOrderPageServiceProductChoiceOrionXpath(self):
        '''
        添加试用订单页面-服务产品选择星璨
        @return:
        '''
        return "//li[text()=' 星璨/Orion ']"

    def AddTryOrderPageLinkMethodChoiceNtripOrSdkXpath(self):
        '''
        添加试用订单页面-链接方式选择Ntrip或Sdk
        @return:
        '''
        return "//label[@title='链接方式']/../following-sibling::div//span[text()=' ntrip或SDK ']"

    def AddTryOrderPageLinkMethodChoiceNtripXpath(self):
        '''
        添加试用订单页面-链接方式选择Ntrip
        @return:
        '''
        return "//label[@title='链接方式']/../following-sibling::div//span[text()=' ntrip ']"

    def AddTryOrderPageLinkMethodChoiceSdkXpath(self):
        '''
        添加试用订单页面-链接方式选择Sdk
        @return:
        '''
        return "//label[@title='链接方式']/../following-sibling::div//span[text()=' SDK ']"

    def AddTryOrderPageActiveMethodChoiceAutoActiveXpath(self):
        '''
        添加试用订单页面-激活方式选择自动激活
        @return:
        '''
        return "//label[@title='激活方式']/../following-sibling::div//span[text()=' 自动激活 ']"

    def AddTryOrderPageActiveMethodChoiceManaulActiveXpath(self):
        '''
        添加试用订单页面-激活方式选择手动激活
        @return:
        '''
        return "//label[@title='激活方式']/../following-sibling::div//span[text()=' 手动激活 ']"

    def AddTryOrderPageBindMethodChoiceAutoBindXpath(self):
        '''
        添加试用订单页面-绑定方式选择自动绑定
        @return:
        '''
        return "//label[@title='绑定方式']/../following-sibling::div//span[text()=' 自动绑定 ']"

    def AddTryOrderPageBindMethodChoiceManaulBindXpath(self):
        '''
        添加试用订单页面-绑定方式选择手动绑定
        @return:
        '''
        return "//label[@title='绑定方式']/../following-sibling::div//span[text()=' 手动绑定 ']"

    def AddTryOrderPagePurchaseNumberInputFrameXpath(self):
        '''
        添加试用订单页面-购买数量输入框
        @return:
        '''
        return "//label[@title='购买数量']/../following-sibling::div//input"

    def AddTryOrderPagePurchaseDurationInputFrameXpath(self):
        '''
        添加试用订单页面-购买时长输入框
        @return:
        '''
        return "//label[@title='购买时长（天）']/../following-sibling::div//input"

    def AddTryOrderPagePurchasePriceInputFrameXpath(self):
        '''
        添加试用订单页面-购买价格输入框
        @return:
        '''
        return "//label[@title='购买价格']/../following-sibling::div//input"

    def AddTryOrderPageSalePeopleInputFrameXpath(self):
        '''
        添加试用订单页面-销售人员输入框
        @return:
        '''
        return "//label[@title='销售人员']/../following-sibling::div//input"

    def AddTryOrderPageRemarkInputFrameXpath(self):
        '''
        添加试用订单页面-备注输入框
        @return:
        '''
        return "//textarea"

    def AddTryOrderPageOrderUseChoiceCustomerUseXpath(self):
        '''
        添加试用订单页面-用途选择客户使用
        @return:
        '''
        return "//label[@title='用途']/../following-sibling::div//span[text()=' 客户使用账号 ']"

    def AddTryOrderPageOrderUseChoiceInternalTestUseXpath(self):
        '''
        添加试用订单页面-用途选择内部测试使用
        @return:
        '''
        return "//label[@title='用途']/../following-sibling::div//span[text()=' 内部测试账号 ']"

    def AddTryOrderPageCancelButtonXpath(self):
        '''
        添加试用订单页面-取消按钮
        @return:
        '''
        return "//span[text()='取 消']"

    def AddTryOrderPageSureButtonXpath(self):
        '''
        添加试用订单页面-确定按钮
        @return:
        '''
        return "//span[text()='确 定']"

    def AddTryOrderPageSecondSureButtonXpath(self):
        '''
        二次确认弹窗-确定按钮
        @return:
        '''
        return "//p[text()=' 请确认是否提交该表单？ ']/../following-sibling::div//span[text()='确 定']"

    def ServiceOrderListTryOrderTabXpath(self):
        '''
        服务订单列表，试用订单Tab
        @return:
        '''
        return "//div[text()='试用订单']"

    def ServiceOrderListTryOrderNumberXpath(self):
        '''
        服务订单列表-订单号
        @return:
        '''
        return "//table/tr[2]//span[contains(text(),'订单号')]"
