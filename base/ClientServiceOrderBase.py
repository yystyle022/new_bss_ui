# -*- coding=utf-8 -*-
# @Time : 2024/4/22 9:58
# @Author : yangyang
# @File : new_bss_ui/ClientServiceOrderBase.py
class ClientServiceOrderBase():
    '''
    管理端服务订单页面
    '''

    def OrderListOrdinaryOrderTabXpath(self):
        '''
        订单列表的普通订单Tab
        @return:
        '''
        return "//div[text()='普通订单']"

    def OrderListRenewOrderTabXpath(self):
        '''
        订单列表续费订单Tab
        @return:
        '''
        return "//div[text()='续费订单']"

    def OrderListExpandOrderTabXpath(self):
        '''
        订单列表扩容订单Tab
        @return:
        '''
        return "//div[text()='扩容订单']"

    def OrderListTryUseToFormalOrderXpath(self):
        '''
        订单列表试用转正式订单Tab
        @return:
        '''
        return "//div[text()='试用转正式订单']"

    def OrderListFirstOrderDetailButtonXpath(self):
        '''
        列表第一条订单详情按钮
        @return:
        '''
        return "//table/tr[3]/td[7]//span[text()='详 情']"
