class ClientPaySuccessBase:
    '''
    支付成功页面
    '''

    def paySuccessIdentificationXpath(self):
        '''
        支付成功标识Xpath
        @return:
        '''
        return "//div[text()='订单支付成功']"

    def ReturnHomePageButtonXpath(self):
        '''
        返回首页Button的Xpath
        @return:
        '''
        return "//span[text()='返回首页']"

    def GoToConsoleButtonXpath(self):
        '''
        前往控制台Button的Xpath
        @return:
        '''
        return "//span[text()='前往控制台']"

    def CheckCurrentOrderButtonXpath(self):
        '''
        查看当前订单按钮的Xpath
        @return:
        '''
        return "//span[text()='查看当前订单']"
