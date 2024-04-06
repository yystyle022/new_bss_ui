class ClientRegisterBase:
    '''
    用户注册页面
    '''

    def UserRegisterNodeXpath(self):
        '''
        用户注册节点标识
        @return:
        '''
        return "//div[text()='用户注册']"

    def PhoneNumberInputFrameXpath(self):
        '''
        手机号输入框
        @return:
        '''
        return "//input[@placeholder='11位手机号']"

    def VerificationCodeInputFrameXpath(self):
        '''
        验证码输入框
        @return:
        '''
        return "//input[@placeholder='输入验证码']"

    def GetVerificationCodeButtonXpath(self):
        '''
        获取验证码按钮
        @return:
        '''
        return "//span[text()='获取验证码']"

    def PleaseInputRightPhoneNumberWarningXpath(self):
        '''
        请输入正确的手机号提示语
        @return:
        '''
        return "//div[text()='请输入正确的手机号']"
