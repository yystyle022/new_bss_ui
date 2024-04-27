# -*- coding=utf-8 -*-
# @Time : 2023/3/17 16:50
# @Author : yangyang
# @File : UI/ClientHomeBase.py


class ClientHomeBase:
    '''
    官网首页元素Xpath
    '''

    # 首页右上角登录按钮
    def loginButtonXpath(self):
        return "//a[contains(text(),'登录')]"

    # 首页右上角注册按钮
    def registerButtonXpath(self):
        return "//a[contains(text(),'注册')]"

    # 首页右上角控制台按钮
    def consoleXpath(self):
        return "//a[contains(text(),'控制台')]"

    def HomePageTopTitleProductTabXpath(self):
        '''
        顶部产品tab
        @return:
        '''
        return "//a[contains(text(),'六分商城')]/../..//a[contains(text(),'产品')]"

    # 首页厘清标题
    def liqingHomePageTitleXpath(self):
        return "//h5[text()='厘清/Locate-CM']"

    # 首页厘清立即购买按钮
    def liqingHomePagePurchaseButtonXpath(self):
        return "//h5[text()='厘清/Locate-CM']/..//span[text()='立即购买']"

    # 首页分明标题
    def fenmingHomePageTitleXpath(self):
        return "//h5[text()='分明/Locate-DM']"

    # 首页分明立即购买按钮
    def fenmingHomePagePurchaseButtonXpath(self):
        '''
        首页分明立即购买按钮
        @return:
        '''
        return "//h5[text()='分明/Locate-DM']/..//span[text()='立即购买']"

    def OrionHomePageTitleXpath(self):
        '''
        首页星璨标题
        @return:
        '''
        return "//h5[text()='分明/Locate-DM']/../../../following-sibling::li//h5"

    def OrionHomePagePurchaseButtonXpath(self):
        '''
        首页星璨立即购买按钮
        @return:
        '''
        return "//h5[text()='星璨/Orion']/..//span[text()='立即购买']"
