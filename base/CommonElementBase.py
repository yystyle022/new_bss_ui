# -*- coding=utf-8 -*-
# @Time : 2024/4/26 11:05
# @Author : yangyang
# @File : new_bss_ui/CommonElementBase.py
class CommonElementBase:
    '''
    通用元素定位
    '''

    def SpanElementXpath(self, text):
        '''
        span
        @param text:
        @return:
        '''
        return f"//span[text()='{text}']"

    def SpanElementContainsTextXpath(self, text):
        '''
        span包括文本内容
        @param text:
        @return:
        '''
        return f"//span[contains(text(),'{text}')]"

    def DivElementContainsTextXpath(self, text):
        '''
        div包括文本内容
        @param text:
        @return:
        '''
        return f"//div[contains(text(),'{text}')]"

    def AlabelElementContainsTextXpath(self, text):
        '''
        a标签包括文本内容
        @param text:
        @return:
        '''
        return f"//a[contains(text(),'{text}')]"
