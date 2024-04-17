# -*- coding=utf-8 -*-
# @Time : 2024/4/15 17:29
# @Author : yangyang
# @File : new_bss_ui/ManagementServerNumberBase.py
class ManagementServerNumberBase:
    '''
    差分账号页面
    '''

    def SearchConditionUserIdInputXpath(self):
        '''
        查询条件，用户编号输入框
        @return:
        '''
        return "//label[@title='用户编号']/../..//input[@placeholder='请输入']"

    def SearchConditionServerNumberTypeChoiceXpath(self):
        '''
        查询条件，账号类型选择框
        @return:
        '''
        return "//label[@title='账号类型']/../following-sibling::div"

    def SearchConditionServerNumberTypeChoiceFormalXpath(self):
        '''
        查询条件，账号类型选择正式账号
        @return:
        '''
        return "//li[text()='正式账号']"

    def SearchConditionServerNumberTypeChoiceTryXpath(self):
        '''
        查询条件，账号类型选择试用账号
        @return:
        '''
        return "//li[text()='试用账号']"

    def SearchConditionInstanceIdInputXpath(self):
        '''
        查询条件，实例ID输入框
        @return:
        '''
        return "//label[@title='实例ID']/../..//input[@placeholder='请输入']"

    def SearchConditionServerNumberedInputXpath(self):
        '''
        查询条件，差分账号输入框
        @return:
        '''
        return "//label[@title='差分账号']/../..//input[@placeholder='请输入']"

    def SearchConditionProductNameChoiceXpath(self):
        '''
        查询条件，产品名称选择框
        @return:
        '''
        return "//label[@title='产品名称']/../following-sibling::div"

    def SearchConditionProductNameChoiceLiQingXpath(self):
        '''
        查询条件，产品名称选择厘清
        @return:
        '''
        return "//li[text()=' 厘清/Locate-CM ']"

    def SearchConditionProductNameChoiceFenMingXpath(self):
        '''
        查询条件，产品名称选择分明
        @return:
        '''
        return "//li[text()=' 分明/Locate-DM ']"

    def SearchConditionProductNameChoiceOrionXpath(self):
        '''
        查询条件，产品名称选择星璨
        @return:
        '''
        return "//li[text()=' 星璨/Orion ']"

    def SearchButtonXpath(self):
        '''
        查询按钮
        @return:
        '''
        return "//span[text()='查 询']"

    def ListServerNumberXpath(self, number):
        '''
        获取列表内随机的账号
        @param number:
        @return:
        '''
        return f"//tbody/tr[{number}]/td[6]"

    def ServerNumberListInstanceIdXpath(self, serverNumber):
        '''
        差分账号的实例ID
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/../td[5]"

    def PurchaseDurationXpath(self, serverNumber):
        '''
        购买时长
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[1]/span"

    def ServerNumberTypeXpath(self, serverNumber):
        '''
        账号类型
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/../td[9]/span"

    def HaveTestPeriodXpath(self, serverNumber):
        '''
        是否具备测试期
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[4]/span"

    def TestPeriodDurationXpath(self, serverNumber):
        '''
        测试期时长
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[5]"

    def YesOrNoActiveXpath(self, serverNumber):
        '''
        是否激活
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[6]"

    def ActiveTimeXpath(self, serverNumber):
        '''
        激活时间
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[7]"

    def ExpireTimeXpath(self, serverNumber):
        '''
        到期时间
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/following-sibling::td[8]/span"
