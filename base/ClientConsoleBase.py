class ClientConsoleBase():
    '''
    控制台概览页面
    '''

    def BuyNumCmXpath(self):
        '''
        厘米级总服务账号个数Xpath
        @return:
        '''
        return "//p[contains(text(),'厘米级')]/span[@class='buy-num']"

    def BuyNumDmXpath(self):
        '''
        亚米级总服务账号个数Xpath
        @return:
        '''
        return "//p[contains(text(),'亚米级')]/span[@class='buy-num']"

    def PurchaseCmAccountButtonXpath(self):
        '''
        购买厘米级服务账号按钮Xpath
        @return:
        '''
        return "//p[text()=' 厘米级 ']/../button"

    def PurchaseDmAccountButtonXpath(self):
        '''
        购买亚米级服务账号按钮Xpath 
        @return:
        '''
        return "//p[text()=' 亚米级 ']/../button"

    def AccountBalanceXpath(self):
        '''
        账户余额标识
        @return:
        '''
        return "//p[text()='账户余额']"

    def ServcieTotalXpath(self):
        '''
        服务统计标识
        @return:
        '''
        return "//div[text()='服务统计']"
