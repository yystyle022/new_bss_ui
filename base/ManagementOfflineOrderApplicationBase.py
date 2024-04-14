class ManagementOfflineOrderApplicationBase:
    '''
    线下订单申
    '''

    def PendingReviewTabXpath(self):
        '''
        待审核Tab
        @return:
        '''
        return "//div[text()='待审核']"

    def ApplicationNumberXpath(self):
        '''
        列表申请单编号
        @return:
        '''
        return "//tbody/tr[1]/td[1]"

    def NewApplicationButtonXpath(self):
        '''
        新增申请按钮
        @return:
        '''
        return "//span[text()='新增申请']"

    def CommonModeTitleXpath(self):
        '''
        通用模式标题
        @return:
        '''
        return "//div[text()='通用模式']"

    def AccumulationModeTitleXpath(self):
        '''
        累计模式标题
        @return:
        '''
        return "//div[text()='累计模式']"

    def OrderTypeNewPurchaseXpath(self):
        '''
        订单类型选择-新购
        @return:
        '''
        return "//span[text()=' 新购 ']"

    def OrderTypeExpandXpath(self):
        '''
        订单类型选择-扩容
        @return:
        '''
        return "//span[text()=' 扩容 ']"

    def OrderTypeRenewXpath(self):
        '''
        订单类型选择-续费
        @return:
        '''
        return "//span[text()=' 续费 ']"

    def OrderTypeTryToFormalXpath(self):
        '''
        订单类型选择-试用转正式
        @return:
        '''
        return "//span[text()=' 试用转正式 ']"

    def CustomerNumberInputXpath(self):
        '''
        客户编号输入框
        @return:
        '''
        return "//input[@id='userId']"

    def ServiceProductChoiceXpath(self):
        '''
        服务产品选择框
        @return:
        '''
        return "//div[text()='请选择']"

    def ServiceProductChoiceLiQingXpath(self):
        '''
        服务产品选择-厘清
        @return:
        '''
        return "//li[text()=' 厘清/Locate-CM ']"

    def ServiceProductChoiceFenMingXpath(self):
        '''
        服务产品选择-分明
        @return:
        '''
        return "//li[text()=' 分明/Locate-DM ']"

    def ServiceProductChoiceOrionXpath(self):
        '''
        服务产品选择-星璨
        @return:
        '''
        return "//li[text()=' 星璨/Orion ']"

    def ChoiceServerNumberXpath(self):
        '''
        选择账号
        @return:
        '''
        return "//a[text()='选择账号']"

    def ServerNumberSearchPageServerNumberInputXpath(self):
        '''
        账号搜索页面搜索条件-差分账号
        @return:
        '''
        return "//label[@title='差分账号']/../..//input[@placeholder='请输入']"

    def ServerNumberSearchPageInstanceIdInputXpath(self):
        '''
        账号搜索页面搜索条件-实例ID
        @return:
        '''
        return "//label[@title='实例ID']/../..//input[@placeholder='请输入']"

    def ServerNumberSearchPageSearchButtonXpath(self):
        '''
        账号搜索页面-查询按钮
        @return:
        '''
        return "//span[text()='查 询']"

    def ServerNumberSearchPageSureButtonXpath(self):
        '''
        账号搜索页面-确定按钮
        @return:
        '''
        return "//span[text()='确 定']"

    def ServerNumberSearchPageServerNumberXpath(self, serverNumber):
        '''
        账号查询页面-账号列表xpath
        @return:
        '''
        return f"//td[text()='{serverNumber}']"

    def ServerNumberSearchPageClickChoiceFrameXpath(self, serverNumber):
        '''
        差分账号点击选择框
        @return:
        '''
        return f"//td[text()='{serverNumber}']/../td[1]"

    def TestActiveYesXpath(self):
        '''
        测试激活-是
        @return:
        '''
        return "//span[text()=' 是 ']"

    def TestActiveNoXpath(self):
        '''
        测试激活-否
        @return:
        '''
        return "//span[text()=' 否 ']"

    def TestPeriodDurationInputXpath(self):
        '''
        测试期时长输入框
        @return:
        '''
        return "//span[text()='天']/..//input"

    def LinkMethodNrtipOrSdkXpath(self):
        '''
        链接方式-Nrtip或Sdk
        @return:
        '''
        return "//span[text()=' ntrip或SDK ']"

    def LinkMethodNrtipXpath(self):
        '''
        链接方式-Nrtip
        @return:
        '''
        return "//span[text()=' ntrip ']"

    def LinkMethodSdkXpath(self):
        '''
        链接方式-Sdk
        @return:
        '''
        return "//span[text()=' SDK ']"

    def ActiveMethodAutoActiveXpath(self):
        '''
        激活方式-自动激活
        @return:
        '''
        return "//span[text()=' 自动激活 ']"

    def ActiveMethodManualActiveXpath(self):
        '''
        激活方式-手动激活
        @return:
        '''
        return "//span[text()=' 手动激活 ']"

    def BindMethodAutoBindXpath(self):
        '''
        绑定方式-自动绑定
        @return:
        '''
        return "//span[text()=' 自动绑定 ']"

    def BindMethodManualBindXpath(self):
        '''
        绑定方式-手动绑定
        @return:
        '''
        return "//span[text()=' 手动绑定 ']"

    def ActiveTimePointRealTimeActiveXpath(self):
        '''
        激活时间点-实时激活
        @return:
        '''
        return "//span[text()=' 实时激活 ']"

    def ActiveTimePointNoRealTimeActiveXpath(self):
        '''
        激活时间点-非实时激活
        @return:
        '''
        return "//span[text()=' 非实时激活 ']"

    def ActiveTimePointBeforeExpirationDateActiveXpath(self):
        '''
        激活时间点-截止日期前激活
        @return:
        '''
        return "//span[text()=' 在截止日期前激活 ']"

    def ExpirationDateInputXpath(self):
        '''
        截止日期输入框
        @return:
        '''
        return "//span[text()=' 在截止日期前激活 ']//input"

    def ExpirationDateTodayXpath(self):
        '''
        截止日期-今天
        @return:
        '''
        return "//a[text()='今天']"

    def InstanceIdInputXpath(self):
        '''
        实例ID输入框
        @return:
        '''
        return "//input[@placeholder='请输入扩容的实例ID']"

    def PurchaseNumberInputXpath(self):
        '''
        购买个数输入框
        @return:
        '''
        return "//label[text()='购买数量']/../following-sibling::div//input"

    def PurchaseDurationUnitChoiceXpath(self):
        '''
        购买时长单位选择
        @return:
        '''
        return "//div[text()=' 年 ']"

    def PurchaseDurationUnitYearXpath(self):
        '''
        购买时长单位-年
        @return:
        '''
        return "//li[text()=' 年 ']"

    def PurchaseDurationUnitMonthXpath(self):
        '''
        购买时长单位-月
        @return:
        '''
        return "//li[text()=' 月 ']"

    def PurchaseDurationUnitDayXpath(self):
        '''
        购买时长单位-天
        @return:
        '''
        return "//li[text()=' 天 ']"

    def PurchaseDurationInputXpath(self):
        '''
        购买时长输入框
        @return:
        '''
        return "//label[text()='购买时长']/../following-sibling::div//input"

    def PurchasePriceInputXpath(self):
        '''
        购买价格输入框
        @return:
        '''
        return "//label[text()='购买价格']/../following-sibling::div//input"

    def OfflineContractTimeChoiceXpath(self):
        '''
        线下合同时间选择框
        @return:
        '''
        return "//label[text()='线下合同时间']/../following-sibling::div//input"

    def OfflineContractTimeChoiceTodayXpath(self):
        '''
        线下合同时间选择-今天
        @return:
        '''
        return "//a[text()='今天']"

    def SalesPersonInputXpath(self):
        '''
        销售人员输入框
        @return:
        '''
        return "//label[text()='销售人员']/../following-sibling::div//input"

    def SalesPersonPhoneNumberInputXpath(self):
        '''
        销售人员电话输入框
        @return:
        '''
        return "//label[text()='销售人员电话']/../following-sibling::div//input"

    def OrderApplicationRemarkInputXpath(self):
        '''
        线下订单申请备注输入框
        @return:
        '''
        return "//textarea"

    def OrderUseCustomerUseAccountXpath(self):
        '''
        线下订单申请用途选择-客户使用账号
        @return:
        '''
        return "//span[text()=' 客户使用账号 ']"

    def OrderUseInternalTestAccountXpath(self):
        '''
        线下订单申请用途选择-内部测试账号
        @return:
        '''
        return "//span[text()=' 内部测试账号 ']"

    def SubmitButtonXpath(self):
        '''
        订单提交按钮
        @return:
        '''
        return "//span[text()='提 交']"

    def SaveButtonXpath(self):
        '''
        保存按钮
        @return:
        '''
        return "//span[text()='保 存']"

    def CancelButtonXpath(self):
        '''
        取消按钮
        @return:
        '''
        return "//span[text()='取 消']"

    def SureButtonXpath(self):
        '''
        弹窗确定按钮
        @return:
        '''
        return "//span[text()='确 定']"
