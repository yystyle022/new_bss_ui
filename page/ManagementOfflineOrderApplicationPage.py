import allure
from common.playwrightFunction import assert_element_exist
from common.allure_function import write_log_to_allure_report
from base.ManagementOfflineOrderApplicationBase import ManagementOfflineOrderApplicationBase


def click_add_application_button(page):
    '''
    点击新增申请按钮
    @return:
    '''
    # 点击新增申请按钮
    page.click(ManagementOfflineOrderApplicationBase().NewApplicationButtonXpath())
    write_log_to_allure_report(page, text='点击新增申请按钮')


def choice_order_mode(page, orderMode):
    '''
    选择订单模式
    @param page:
    @param orderMode: 1-通用模式；2-累计模式
    @return:
    '''
    if orderMode == 1:
        page.click(ManagementOfflineOrderApplicationBase().CommonModeTitleXpath())
        write_log_to_allure_report(page, text='选择订单模式为通用模式')
    elif orderMode == 2:
        page.click(ManagementOfflineOrderApplicationBase().AccumulationModeTitleXpath())
        write_log_to_allure_report(page, text='选择订单模式为累计模式')
    else:
        assert False, f"输入的订单模式值为：{orderMode},订单模式输入值不正确，请重新输入"


def choice_order_type(page, orderType):
    '''
    选择订单类型
    @param page:
    @param orderType: 1-新购；2-扩容；3-续费；4-试用转正式
    @return:
    '''
    if orderType == 1:
        page.click(ManagementOfflineOrderApplicationBase().OrderTypeNewPurchaseXpath())
        write_log_to_allure_report(page, text='新购订单')
    elif orderType == 2:
        page.click(ManagementOfflineOrderApplicationBase().OrderTypeExpandXpath())
        write_log_to_allure_report(page, text='扩容订单')
    elif orderType == 3:
        page.click(ManagementOfflineOrderApplicationBase().OrderTypeRenewXpath())
        write_log_to_allure_report(page, text='续费订单')
    elif orderType == 4:
        page.click(ManagementOfflineOrderApplicationBase().OrderTypeTryToFormalXpath())
        write_log_to_allure_report(page, text='试用转正式订单')
    else:
        assert False, f"选择的订单类型为：{orderType},订单类型选择错误，请重新选择"


def input_user_id(page, userId):
    '''
    输入用户编号
    @param page:
    @param userId: 用户编号
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().CustomerNumberInputXpath(), f"{userId}")
    write_log_to_allure_report(page, text=f"输入的客户编号为：{userId}")


def choice_product_name(page, productName):
    '''
    选择产品名称
    @param page:
    @param productName: 1-厘清；2-分明；3-星璨
    @return:
    '''
    # 点击产品名称选择框，弹出产品名称选择列表
    page.click(ManagementOfflineOrderApplicationBase().ServiceProductChoiceXpath())
    write_log_to_allure_report(page, text="点击产品名称选择框，弹出产品名称选择列表")
    if productName == 1:
        page.click(ManagementOfflineOrderApplicationBase().ServiceProductChoiceLiQingXpath())
        write_log_to_allure_report(page, text="选择的产品名称为厘清")
    elif productName == 2:
        page.click(ManagementOfflineOrderApplicationBase().ServiceProductChoiceFenMingXpath())
        write_log_to_allure_report(page, text="选择的产品名称为分明")
    elif productName == 3:
        page.click(ManagementOfflineOrderApplicationBase().ServiceProductChoiceOrionXpath())
        write_log_to_allure_report(page, text="选择的产品名称为星璨")
    else:
        assert False, f"选择的产品名称为：{productName},产品名称选择不正确"


def choice_test_active(page, testActive, testActiveDuration):
    '''
    选择是否需要测试激活
    @param page:
    @param testActive: True-需要测试激活；False-不需要测试激活
    @return:
    '''
    if testActive:
        page.click(ManagementOfflineOrderApplicationBase().TestActiveYesXpath())
        write_log_to_allure_report(page, text="需要测试激活")
        page.fill(ManagementOfflineOrderApplicationBase().TestPeriodDurationInputXpath(), f"{testActiveDuration}")
        write_log_to_allure_report(page, text=f"测试激活时长为：{testActiveDuration}天")
    else:
        page.click(ManagementOfflineOrderApplicationBase().TestActiveNoXpath())
        write_log_to_allure_report(page, text="不需要测试激活")


def click_choice_server_number(page):
    '''
    点击选择账号
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().ChoiceServerNumberXpath())
    write_log_to_allure_report(page, text="点击选择账号")


def server_number_search_input_server_number(page, serverNumber):
    '''
    账号查询页面输入差分账号查询
    @param page:
    @param serverNumber:差分账号
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().ServerNumberSearchPageServerNumberInputXpath(), serverNumber)
    write_log_to_allure_report(page, text=f"输入的差分账号为：{serverNumber}")


def click_server_number_search_button(page):
    '''
    账号查询页面，点击账号查询按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().ServerNumberSearchPageSearchButtonXpath())
    write_log_to_allure_report(page, text="点击账号查询按钮")


def assert_server_number_exist(page, serverNumber):
    '''
    断言页面账号存在
    @param page:
    @param serverNumber:
    @return:
    '''
    assert_element_exist(page, ManagementOfflineOrderApplicationBase().ServerNumberSearchPageServerNumberXpath(serverNumber))


def choice_server_number(page, serverNumber):
    '''
    选择差分账号
    @param page:
    @param serverNumber:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().ServerNumberSearchPageClickChoiceFrameXpath(serverNumber))
    write_log_to_allure_report(page, text=f"点击账号选择按钮，选择账号{serverNumber}")


def click_sure_button(page):
    '''
    点击确定按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().ServerNumberSearchPageSureButtonXpath())
    write_log_to_allure_report(page, text=f"点击确定按钮成功")


def choice_link_method(page, linkMethod):
    '''
    选择链接方式
    @param page:
    @param linkMethod: 1-Ntrip或Sdk；2-Ntrip；3-Sdk
    @return:
    '''
    if linkMethod == 1:
        page.click(ManagementOfflineOrderApplicationBase().LinkMethodNrtipOrSdkXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Ntrip或Sdk")
    elif linkMethod == 2:
        page.click(ManagementOfflineOrderApplicationBase().LinkMethodNrtipXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Ntrip")
    elif linkMethod == 3:
        page.click(ManagementOfflineOrderApplicationBase().LinkMethodSdkXpath())
        write_log_to_allure_report(page, text=f"选择的链接方式为：Sdk")
    else:
        assert False, f"选择的链接方式为：{linkMethod},链接方式选择不正确"


def choice_active_method(page, activeMethod):
    '''
    选择激活方式
    @param page:
    @param activeMethod: 1-自动激活；2-手动激活
    @return:
    '''
    if activeMethod == 1:
        page.click(ManagementOfflineOrderApplicationBase().ActiveMethodAutoActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活方式为：自动激活")
    elif activeMethod == 2:
        page.click(ManagementOfflineOrderApplicationBase().ActiveMethodManualActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活方式为：手动激活")
    else:
        assert False, f"选择的激活方式为：{activeMethod},激活方式选择不正确"


def choice_bind_method(page, bindMethod):
    '''
    选择绑定方式
    @param page:
    @param bindMethod: 1-自动绑定；2-手动绑定
    @return:
    '''
    if bindMethod == 1:
        page.click(ManagementOfflineOrderApplicationBase().BindMethodAutoBindXpath())
        write_log_to_allure_report(page, text=f"选择的绑定方式为：自动绑定")
    elif bindMethod == 2:
        page.click(ManagementOfflineOrderApplicationBase().BindMethodManualBindXpath())
        write_log_to_allure_report(page, text=f"选择的绑定方式为：手动绑定")
    else:
        assert False, f"选择的绑定方式为：{bindMethod},绑定方式选择不正确"


def input_instance_id(page, instanceId):
    '''
    输入实例ID
    @param page:
    @param instanceId:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().InstanceIdInputXpath(), f"{instanceId}")
    write_log_to_allure_report(page, text=f"输入的扩容实例为：{instanceId}")


def choice_active_time_point(page, activeTimePoint):
    '''
    选择激活时间点
    @param page:
    @param activeTimePoint: 1-非实时激活；2-实时激活；3-截止日期前激活
    @return:
    '''
    if activeTimePoint == 1:
        page.click(ManagementOfflineOrderApplicationBase().ActiveTimePointNoRealTimeActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活时间点为：非实时激活")
    elif activeTimePoint == 2:
        page.click(ManagementOfflineOrderApplicationBase().ActiveTimePointRealTimeActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活时间点为：实时激活")
    elif activeTimePoint == 3:
        page.click(ManagementOfflineOrderApplicationBase().ActiveTimePointBeforeExpirationDateActiveXpath())
        write_log_to_allure_report(page, text=f"选择的激活时间点为：在截止日期前激活")
        page.click(ManagementOfflineOrderApplicationBase().ExpirationDateInputXpath())
        write_log_to_allure_report(page, text=f"点击截止日期输入框")
        page.click(ManagementOfflineOrderApplicationBase().ExpirationDateTodayXpath())
        write_log_to_allure_report(page, text=f"选择截止日期为今天")
    else:
        assert False, f"选择的激活时间点为：{activeTimePoint},激活时间点选择不正确"


def input_purchase_number(page, number):
    '''
    输入购买数量
    @param page:
    @param number:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().InstanceIdInputXpath(), f"{number}")
    write_log_to_allure_report(page, text=f"输入的购买数量为：{number}")


def choice_purchase_duration_unit(page, unit):
    '''
    选择购买时长单位
    @param page:
    @param unit: 1-年；2-月；3-日
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().PurchaseDurationUnitChoiceXpath())
    write_log_to_allure_report(page, text=f"点击选择购买时长单位")

    if unit == 1:
        page.click(ManagementOfflineOrderApplicationBase().PurchaseDurationUnitYearXpath())
        write_log_to_allure_report(page, text=f"选择单位为年")
    elif unit == 2:
        page.click(ManagementOfflineOrderApplicationBase().PurchaseDurationUnitMonthXpath())
        write_log_to_allure_report(page, text=f"选择单位为月")
    elif unit == 3:
        page.click(ManagementOfflineOrderApplicationBase().PurchaseDurationUnitDayXpath())
        write_log_to_allure_report(page, text=f"选择单位为日")
    else:
        assert False, f"选择的单位为：{unit},购买时长单位选择不正确"


def input_purchase_duration(page, duration):
    '''
    输入购买时长
    @param page:
    @param duration:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().PurchaseDurationInputXpath(), f"{duration}")
    write_log_to_allure_report(page, text=f"输入的购买时长为：{duration}")


def input_purchase_price(page, price):
    '''
    输入购买价格
    @param page:
    @param price:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().PurchasePriceInputXpath(), f"{price}")
    write_log_to_allure_report(page, text=f"输入的购买时长为：{price}")


def choice_offline_contract_date(page):
    '''
    选择线下合同日期
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().OfflineContractTimeChoiceXpath())
    write_log_to_allure_report(page, text='点击线下合同时间选择框')
    page.click(ManagementOfflineOrderApplicationBase().OfflineContractTimeChoiceTodayXpath())
    write_log_to_allure_report(page, text='线下合同选择时间为今天')


def input_sales_person_name(page, salePersonName):
    '''
    填写销售人员名称
    @param page:
    @param salePersonName:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().SalesPersonInputXpath(), salePersonName)
    write_log_to_allure_report(page, text=f"输入的销售人员名称为：{salePersonName}")


def input_sales_person_phone_number(page, salePersonPhoneNumber):
    '''
    填写销售人员电话
    @param page:
    @param salePersonPhoneNumber:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().SalesPersonPhoneNumberInputXpath(), salePersonPhoneNumber)
    write_log_to_allure_report(page, text=f"输入的销售人员电话为：{salePersonPhoneNumber}")


def input_order_remark(page, orderRemark):
    '''
    填写订单备注
    @param page:
    @param orderRemark:
    @return:
    '''
    page.fill(ManagementOfflineOrderApplicationBase().OrderApplicationRemarkInputXpath(), orderRemark)
    write_log_to_allure_report(page, text=f"输入的订单备注为：{orderRemark}")


def choice_order_use(page, use):
    '''
    选择订单用途
    @param page:
    @param use: 1-客户使用账号；2-内部测试账号
    @return:
    '''
    if use == 1:
        page.click(ManagementOfflineOrderApplicationBase().OrderUseCustomerUseAccountXpath())
        write_log_to_allure_report(page, text='选择的订单用途为：客户使用账号')
    elif use == 2:
        page.click(ManagementOfflineOrderApplicationBase().OrderUseInternalTestAccountXpath())
        write_log_to_allure_report(page, text='选择的订单用途为：内部测试账号')
    else:
        assert False, f"选择的订单用途为：{use},订单用途选择不正确"


def click_submit_button(page):
    '''
    点击订单提交按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().SubmitButtonXpath())
    write_log_to_allure_report(page, text='点击订单提交按钮')


def click_save_button(page):
    '''
    点击订单保存按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().SaveButtonXpath())
    write_log_to_allure_report(page, text='点击订单保存按钮')


def click_cancel_button(page):
    '''
    点击订单取消按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().CancelButtonXpath())
    write_log_to_allure_report(page, text='点击订单取消按钮')


def click_ok_button(page):
    '''
    提交订单弹窗确定按钮
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().SureButtonXpath())
    write_log_to_allure_report(page, text='点击弹窗确定按钮')


def go_to_pending_review_page(page):
    '''
    进度待审核页面
    @param page:
    @return:
    '''
    page.click(ManagementOfflineOrderApplicationBase().PendingReviewTabXpath())
    write_log_to_allure_report(page, text='点击待审核Tab进入待审核页面')


def get_application_number(page):
    '''
    获取申请单编号
    @param page:
    @return:
    '''
    OrderApplicationNumber = page.query_selector(ManagementOfflineOrderApplicationBase().ApplicationNumberXpath()).text_content()
    write_log_to_allure_report(page, text=f'订单申请编号为：{OrderApplicationNumber}', screenshot=False, log=True)
    return OrderApplicationNumber


def offline_order_application_new_purchase(page, userId, salePersonName, salePersonPhoneNumber, orderMode=1, orderType=1, productName=1, testActive=False,
                                           testActiveDuration=5, linkMethod=1, activeMethod=1, bindMethod=1, activeTimePoint=1, number=1, unit=2, duration=1,
                                           price=1.21, orderRemark='UI测试', use=2):
    '''
    线下订单购买，新购账号
    @param page:
    @param userId:用户id
    @param salePersonName:销售人员名称
    @param salePersonPhoneNumber:销售人员手机号
    @param orderMode:订单模式
    @param orderType:订单类型
    @param productName:商品名称
    @param testActive:测试激活
    @param testActiveDuration:测试时长
    @param linkMethod:链接方法
    @param activeMethod:激活方式
    @param bindMethod:绑定方式
    @param activeTimePoint:激活时间点
    @param number:数量
    @param price:价格
    @param orderRemark:备注
    @param use:用途
    @return:
    '''
    with allure.step('点击订单申请按钮'):
        click_add_application_button(page)

    with allure.step('选择订单模式'):
        choice_order_mode(page, orderMode)

    with allure.step('选择订单类型'):
        choice_order_type(page, orderType)

    with allure.step('输入客户编号'):
        input_user_id(page, userId)

    with allure.step('选择产品名称'):
        choice_product_name(page, productName)

    with allure.step('选择是否测试激活和测试时长'):
        choice_test_active(page, testActive, testActiveDuration)

    with allure.step('选择链接方式'):
        choice_link_method(page, linkMethod)

    with allure.step('选择激活方式'):
        choice_active_method(page, activeMethod)

    with allure.step('选择绑定方式'):
        choice_bind_method(page, bindMethod)

    with allure.step('选择激活时间点'):
        choice_active_time_point(page, activeTimePoint)

    with allure.step('填写购买数量'):
        input_purchase_number(page, number)

    with allure.step('选择购买时长单位'):
        choice_purchase_duration_unit(page, unit)

    with allure.step('填写购买时长'):
        input_purchase_duration(page, duration)

    with allure.step('填写购买价格'):
        input_purchase_price(page, price)

    with allure.step('填写线下合同时间,时间为今天'):
        choice_offline_contract_date(page)

    with allure.step('填写销售人员名称'):
        input_sales_person_name(page, salePersonName)

    with allure.step('填写销售人员手机号码'):
        input_sales_person_phone_number(page, salePersonPhoneNumber)

    with allure.step('填写订单备注'):
        input_order_remark(page, orderRemark)

    with allure.step('选择订单用途'):
        choice_order_use(page, use)

    with allure.step('点击提交按钮'):
        click_submit_button(page)

    with allure.step('点击确定按钮'):
        click_sure_button(page)
