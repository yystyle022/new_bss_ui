import allure
from common.allure_function import write_log_to_allure_report
from page.ManagementInstanceListPage import query_instance, click_list_instance_id
from page.ManagementPage import go_to_offline_order_page, go_to_order_review_page, go_to_instance_list_page
from page.ManagementOfflineOrderReviewPage import click_pending_review_tab, review_application_order
from page.ManagementOfflineOrderApplicationPage import go_to_pending_review_page, get_application_number, offline_order_application_renew
from page.ManagementServerNumberPage import get_random_server_number_current_page, get_server_number_purchase_duration, query_server_number


@allure.feature('管理端线下订单申请-账号续费')
def test_offline_order_application_liqing_renew_month(browser_login_management, get_user_id, get_random_number, get_expand_liqing_instanceId):
    '''
    线下订单申请测试用例---厘清账号续费
    @param browser_login_management:
    @param get_user_id: 用户编号
    @return:
    '''
    renewNumber = get_random_number
    instanceId = get_expand_liqing_instanceId
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-续费厘清账号-申请成功，厘清账号续费{renewNumber}月')

    with allure.step('打开管理端，进入首页'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('点击实例id,进入实例详情页面，查看账号'):
        click_list_instance_id(page, instanceId)

    with allure.step('获取列表页面的需要续费的账号信息'):
        serverNumber = get_random_server_number_current_page(page, number=renewNumber)

    with allure.step('获取续费账号续费前的购买时长'):
        beforePurchaseDuration = get_server_number_purchase_duration(page, serverNumber=serverNumber)

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('续费订单申请'):
        offline_order_application_renew(page, get_user_id, serverNumber=serverNumber, duration=renewNumber)

    with allure.step('进入待审核列表'):
        go_to_pending_review_page(page)

    with allure.step('获取申请的订单号'):
        OrderApplicationNumber = get_application_number(page)

    with allure.step('进入订单审核页面'):
        go_to_order_review_page(page)

    with allure.step('点击待审核Tab,进入待审核列表页面'):
        click_pending_review_tab(page)

    with allure.step('审核订单'):
        review_application_order(page, OrderApplicationNumber)

    with allure.step('进入实例列表页面'):
        go_to_instance_list_page(page)

    with allure.step('查询扩容的实例'):
        query_instance(page, instanceId)

    with allure.step('点击实例id,进入实例详情页面，查看账号'):
        click_list_instance_id(page, instanceId)

    with allure.step('查询续费的账号'):
        query_server_number(page, serverNumber=serverNumber)

    with allure.step('获取续费后的账号购买时长'):
        afterPurchaseDuration = get_server_number_purchase_duration(page, serverNumber=serverNumber)

    with allure.step('判断续费后的购买时长是否正确'):
        assert afterPurchaseDuration['monthNumber'] == beforePurchaseDuration['monthNumber'] + renewNumber
        assert afterPurchaseDuration['dayNumber'] == beforePurchaseDuration['dayNumber']
