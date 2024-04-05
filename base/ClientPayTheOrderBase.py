class ClientPayTheOrderBase:
    '''
    支付订单页面
    '''

    def ConfirmPaymentButtonXpath(self):
        '''
        确认支付按钮
        @return:
        '''
        return "//button"

    def InOrderPaymentPageXpath(self):
        '''
        进入订单支付页面标识
        @return:
        '''
        return "//div[text()='订单提交成功，请尽快付款！']"
