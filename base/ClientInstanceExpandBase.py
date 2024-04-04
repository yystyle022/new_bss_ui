class ClientInstanceExpandBase:
    '''
    实例扩容页面
    '''

    def SumInputXpath(self):
        '''
        商品信息-扩容数量输入框
        @return:
        '''
        return "//input"

    def ActiveMethodXpath(self):
        '''
        商品信息-激活方式
        @return:
        '''
        return "//tr[@class]/td[2]"

    def BindMethodXpath(self):
        '''
        商品信息-绑定方式
        @return:
        '''
        return "//tr[@class]/td[3]"

    def LinkMethodXpath(self):
        '''
        商品信息-链接方式
        @return:
        '''
        return "//tr[@class]/td[4]"

    def DurationXpath(self):
        '''
        商品信息-购买时长
        @return:
        '''
        return "//tr[@class]/td[5]"

    def PriceXpath(self):
        '''
        商品信息-单价
        @return:
        '''
        return "//tr[@class]/td[7]/span"

    def PurchaseDurationIsDayXpath(self):
        '''
        购买时长-1天
        @return:
        '''
        return "//span[text()='天']"

    def PurchaseDurationIsMonthXpath(self):
        '''
        购买时长-1个月
        @return:
        '''
        return "//span[text()='个月']"

    def PurchaseDurationIsYearXpath(self):
        '''
        购买时长-1年
        @return:
        '''
        return "//span[text()='年']"

    def SubmitExpandButtonXpath(self):
        '''
        提交扩容按钮
        @return:
        '''
        return "//span[text()='提交扩容']"
