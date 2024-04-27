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
        return f"//input[@placeholder='{input_placeholder}']"

    def submitButtonXpath(self):
        '''
        登录按钮xpath
        @return:
        '''
        return "//button[@type='submit']"

    def sliderVerificationIframeXpath(self):
        '''
        滑动验证窗口xpath
        @return:
        '''
        return "//iframe[@id='tcaptcha_iframe']"

    def sliderButtonXpath(self):
        '''
        滑动验证按钮xpath
        @return:
        '''
        return "//div[@id='tcaptcha_drag_thumb']"

    def sliderPicXpath(self):
        '''
        滑块图片xpath
        @return:
        '''
        return "//img[@id='slideBlock']"

    def sliderBackPicXpath(self):
        '''
        背景图片xpath
        @return:
        '''
        return "//img[@id='slideBg']"

    def refreshSliderBackPicButtonXpath(self):
        '''
        刷新滑块图片按钮xpath
        @return:
        '''
        return "//div[@aria-label='刷新']/div"

    def errorSliderWarning(self):
        '''
        滑动错误提示语Xpath
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

    def loginPageToastXpath(self, text):
        '''
        登陆页面toast提示
        @param text: 提示信息
        @return:
        '''
        return f"//span[contains(text(),'{text}')]"

    def accountOrPasswordNotBeNoneXpath(self):
        '''
        账号或密码不能为空
        @return:
        '''
        return "//div[text()='账号或密码不能为空']"

    def phoneNumberLoginTabXpath(self):
        '''
        手机号登录Tab
        @return:
        '''
        return "//div[text()='手机号登录']"

    def phoneNumberMistakeToastXpath(self):
        '''
        手机号输入错误提示
        @return:
        '''
        return "//div[text()='请输入正确的手机号']"

    def phoneNumberLoginPageSubmitButtonXpath(self):
        '''
        手机号登录页面的登录按钮
        @return:
        '''
        return "//div[@role='tabpanel'][2]//span[text()='登 录']"

    def getVerificationCodeButtonXpath(self):
        '''
        获取验证码按钮
        @return:
        '''
        return "//span[text()='获取验证码']"

    def regetVerificationCodeButtonXpath(self):
        '''
        重新获取验证码按钮
        @return:
        '''
        return "//span[contains(text(),'重新获取')]"

    def pleaseInputVerificationCodeToastXpath(self):
        '''
        请输入验证码提示
        @return:
        '''
        return "//div[text()='请输入验证码']"

    def vertificationCodeExpireToastXpath(self):
        '''
        验证码过期提示
        @return:
        '''
        return "//span[text()='验证码过期！']"

    def vertificationCodeMistakeToastXpath(self):
        '''
        验证码错误提示
        @return:
        '''
        return "//span[text()='验证码错误！']"

