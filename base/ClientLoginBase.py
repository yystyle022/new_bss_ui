# -*- coding: utf-8 -*-
# @Time : 2023/3/14 21:51
# @Author : yangyang
# @File : UI/ClientLoginBase.py
class ClientLoginBase:

    def loginInputXpath(self, input_placeholder):
        '''
        登录页面的用户名，密码输入框的Xpath
        @param input_placeholder: 输入框名称
               账号输入框：请输入账号或手机号码
               密码输入框：请输入密码
        @return: Xpath
        '''
        return "//input[@placeholder='{}']".format(input_placeholder)

    def submitButtonXpath(self):
        '''
        登录按钮xpath
        @return:
        '''
        return "//button[@type='submit']"

    def sliderVerificationIframeXpath(self):
        '''
        返回滑动验证窗口xpath
        @return:
        '''
        return "//iframe[@id='tcaptcha_iframe']"

    def sliderButtonXpath(self):
        '''
        返回滑动验证按钮xpath
        @return:
        '''
        return "//div[@id='tcaptcha_drag_thumb']"

    def sliderPicXpath(self):
        '''
        返回滑块图片xpath
        @return:
        '''
        return "//img[@id='slideBlock']"

    def sliderBackPicXpath(self):
        '''
        返回背景图片xpath
        @return:
        '''
        return "//img[@id='slideBg']"

    def errorSliderWarning(self):
        '''
        返回滑动错误提示语Xpath
        @return:
        '''
        return "//div[text()='请控制拼图块对齐缺口']"

    def loginSuccessXpath(self, username='18322369885'):
        '''
        登陆成功Xpath
        @return:
        '''
        return "//a[contains(text(),'{}')]".format(username)

    def managementLoginSuccessXpath(self):
        '''
        管理端登陆成功Xpath
        @return:
        '''
        return "//span[text()='财务管理']"

    def loginPasswordMistakeXpath(self, text):
        '''
        登录密码错误Xpath
        @return:
        '''
        return f"//span[text()='{text}']"
