# -*- coding=utf-8 -*-
# @Time : 2023/5/5 9:27
# @Author : yangyang
# @File : bss-ui/ClientCmInstanceListBase.py
class ClientInstanceList:
    '''
    厘米级服务实例页面
    '''

    def InstanceIdInputXpath(self):
        '''
        查询条件-实例Id输入框
        @return:
        '''
        return "//input[@placeholder='请输入']"

    def ProductNameSelectXpath(self):
        '''
        查询条件-产品名称选择框
        @return:
        '''
        return "//div[@title='厘清/Locate-CM']"

    def ProductNameSelectLiQingXpath(self):
        '''
        查询条件-产品名称选项-厘清
        @return:
        '''
        return "//li[text()=' 厘清/Locate-CM ']"

    def ProductNameSelectOrionXpath(self):
        '''
        查询条件-产品名称选择-星璨
        @return:
        '''
        return "//li[text()=' 星璨/Orion ']"

    def QueryButtonXpath(self):
        '''
        查询按钮
        @return:
        '''
        return "//span[text()='查 询']"

    def CmListTitleXpath(self):
        '''
        厘米级实例列表标题
        @return:
        '''
        return "//div[text()='厘米级实例列表']"

    def DmListTitleXpath(self):
        '''
        亚米级实例列表标题
        @return:
        '''
        return "//div[text()='亚米级实例列表']"

    def ListExpandButtonXpath(self, InstanceId):
        '''
        实例列表-实例展开按钮
        @param instance:
        @return:
        '''
        return f"//td[text()='{InstanceId}']/..//span[@class='expand-icon']"

    def ServiceModeXpath(self, InstanceId):
        '''
        实例列表-实例服务模式
        @param InstanceId:
        @return:
        '''
        return f"//td[text()='{InstanceId}']/../td[2]/span"

    def InstanceIdXpath(self, InstanceId):
        '''
        实例列表-实例ID
        @param InstanceId:
        @return:
        '''
        return f"//td[text()='{InstanceId}']"

    def InstanceFormalAccountNumberSumsXpath(self, InstanceId):
        '''
        实例列表-实例下正式账号数量
        @param InstanceId:
        @return:
        '''
        return f"//td[text()='{InstanceId}']/following-sibling::td[7]/a"

    def InstanceExpandAccountNumberButtonXpath(self, InstanceId):
        '''
        实例列表-实例下扩容账号按钮
        @return:
        '''
        return f"//td[text()='{InstanceId}']/..//a[text()='扩容']"

    def ListAsXpath(self, InstanceId):
        '''
        实例列表-实例AS
        @param instance:
        @return:
        '''
        return f"//td[text()='{InstanceId}']/../following-sibling::tr[1]//span[contains(text(),'AppSecret')]/following-sibling::span"
