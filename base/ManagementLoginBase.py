# -*- coding=utf-8 -*-
# @Time : 2024/4/8 17:55
# @Author : yangyang
# @File : new_bss_ui/ManagementLoginBase.py
class ManagementLoginBase:
    '''
    管理端登录页面元素
    '''

    def AccountNumberInputFrameXpath(self):
        '''
        手机号输入框Xpath
        @return:
        '''
        return "//input[@placeholder='账号或手机号']"

    def PasswordInputFrameXpath(self):
        '''
        密码输入框Xpath
        @return:
        '''
        return "//input[@placeholder='密码']"

    def LoginButtonXpath(self):
        '''
        登录按钮Xpath
        @return:
        '''
        return "//span[text()='登 录']"

    def AccountNoExistToastXpath(self):
        '''
        账号不存在toast提示
        @return:
        '''
        return "//span[text()='该账号不存在 ']"
