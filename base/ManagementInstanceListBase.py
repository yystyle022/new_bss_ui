# -*- coding=utf-8 -*-
# @Time : 2024/4/16 10:51
# @Author : yangyang
# @File : new_bss_ui/ManagementInstanceListBase.py

class ManagementInstanceListBase:
    '''
    实例列表页面
    '''

    def UserIdInputFrameXpath(self):
        '''
        用户编号输入框
        @return:
        '''
        return "//label[@title='用户编号']/../following-sibling::div//input"

    def InstanceIdInputFrameXpath(self):
        '''
        实例ID输入框
        @return:
        '''
        return "//label[@title='实例ID']/../following-sibling::div//input"

    def QueryButtonXpath(self):
        '''
        查询按钮
        @return:
        '''
        return "//span[text()='查 询']"

    def InstanceIdXpath(self, instanceId):
        '''
        实例ID
        @return:
        '''
        return f"//span[text()='{instanceId}']"

    def ActiveMethodXpath(self):
        '''
        激活方式
        @return:
        '''
        return "//span[text()='{instanceId}']/../following-sibling::td[5]"

    def BindMethodXpath(self):
        '''
        绑定方式
        @return:
        '''
        return "//span[text()='{instanceId}']/../following-sibling::td[6]"

    def LinkMethodXpath(self):
        '''
        链接方式
        @return:
        '''
        return "//span[text()='{instanceId}']/../following-sibling::td[7]"

    def FormalServerNumberXpath(self, instanceId):
        '''
        正式账号个数
        @return:
        '''
        return f"//span[text()='{instanceId}']/../following-sibling::td[9]"

    def TryUseServerNumberXpath(self, instanceId):
        '''
        试用账号个数
        @param instanceId:
        @return:
        '''
        return f"//span[text()='{instanceId}']/../following-sibling::td[10]"

    def InstanceListRankInstanceIdXpath(self, rank):
        '''
        实例列表的实例ID
        @param rank: 列表第几个
        @return:
        '''
        return f"//tbody/tr[{rank}]/td[2]/span"
