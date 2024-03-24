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

    # 首页厘清标题
    def liqingHomePageTitleXpath(self):
        return "//h5[text()='厘清/Locate-CM']"

    # 首页厘清立即购买按钮
    def liqingHomePagePurchaseButtonXpath(self):
        return "//h5[text()='厘清/Locate-CM']/..//span[text()='立即购买']"

    # 首页右上角控制台按钮
    def consoleXpath(self):
        return "//a[contains(text(),'控制台')]"
