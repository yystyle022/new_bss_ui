# -*- coding=utf-8 -*-
# @Time : 2024/4/18 10:51
# @Author : yangyang
# @File : new_bss_ui/ClientCmFormalServerNumberBase.py
class ClientCmFormalServerNumberBase:
    '''
    官网厘米级服务正式账号页面
    '''

    def ClientCmFormalServerNumberPageBatchRenewButtonXpath(self):
        '''
        官网厘米级服务正式账号页面-批量续费按钮
        @return:
        '''
        return "//span[text()='批量续费']"

    def ClientCmFormalServerNumberPageRankServerNumberXpath(self, rank):
        '''
        官网厘米级服务正式账号页面-按照排名获取的差分账号
        @param rank:
        @return:
        '''
        return f"//tbody/tr[{rank}]/td[5]"

    def ClientCmFormalServerNumberPageServerNumberCheckButtonXpath(self, serverNumber):
        '''
        官网厘米级服务正式账号页面-账号查看按钮
        @param serverNumber:
        @return:
        '''
        return f"//td[text()='{serverNumber}']/..//a[text()='查看']"

    def ClientCmFormalServerNumberPageServerNumberPasswordXpath(self):
        '''
        官网厘米级服务正式账号页面-差分账号密码
        @return:
        '''
        return "//div[@role='tooltip']"
