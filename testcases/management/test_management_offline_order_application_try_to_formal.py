import allure

from base.ManagementInstanceListBase import ManagementInstanceListBase
from page.CommonPageFunction import *
from base.ManagementServerNumberBase import ManagementServerNumberBase
from page.ManagementInstanceListPage import query_instance, click_list_instance_id, input_instance_id
from page.ManagementPage import go_to_offline_order_page, go_to_order_review_page, go_to_instance_list_page, go_to_server_number_list_page
from page.ManagementOfflineOrderReviewPage import click_pending_review_tab, review_application_order
from page.ManagementOfflineOrderApplicationPage import go_to_pending_review_page, get_application_number, offline_order_application_renew, offline_order_application_try_to_formal
from page.ManagementServerNumberPage import get_random_server_number_current_page, get_server_number_purchase_duration, query_server_number, choice_server_number_type, click_search_button, \
    server_number_page_query_condition_choice_product_name, get_instance_id_from_server_number_page, search_condition_input_server_number


@allure.feature('管理端线下订单申请-账号试用转正式')
def test_offline_order_application_try_to_formal_liqing(browser_login_management, get_user_id, get_random_number, get_expand_liqing_instanceId):
    '''
    线下订单申请测试用例---试用转正式申请
    @param browser_login_management:
    @param get_user_id: 用户编号
    @return:
    '''
    randomNumber = get_random_number
    instanceId = get_expand_liqing_instanceId
    browser_name = browser_login_management['name']
    page = browser_login_management['page']
    allure.dynamic.title(f'{browser_name}浏览器-厘清账号试用转正式-申请成功')

    with allure.step('打开管理端，进入首页'):
        write_log_to_allure_report(page, text='登录管理端成功')

    with allure.step('进入差分账号页面'):
        go_to_server_number_list_page(page)

    with allure.step('输入用户编号'):
        input_operation(page, ManagementServerNumberBase().SearchConditionUserIdInputXpath(), get_user_id, f'输入的用户编号为：{get_user_id}')

    with allure.step('选择账号类型为试用账号'):
        choice_server_number_type(page, serverNumberType=2)

    with allure.step('选择产品名称为厘清'):
        server_number_page_query_condition_choice_product_name(page)

    with allure.step('点击查询按钮进行查询'):
        click_search_button(page)

    with allure.step('获取页面内的试用账号'):
        tryServerNumber = get_random_server_number_current_page(page, randomNumber)

    with allure.step('获取试用账号的实例'):
        instanceId = get_instance_id_from_server_number_page(page, tryServerNumber)

    with allure.step('进入订单申请页面'):
        go_to_offline_order_page(page)

    with allure.step('试用转正式订单申请'):
        offline_order_application_try_to_formal(page, get_user_id, serverNumber=tryServerNumber, duration=randomNumber)

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

    with allure.step('输入实例ID'):
        input_operation(page, ManagementInstanceListBase().InstanceIdInputFrameXpath(), instanceId, text=f'输入实例ID为：{instanceId}')

    with allure.step('点击查询按钮'):
        click_operation(page, ManagementInstanceListBase().QueryButtonXpath(), text='点击查询按钮，查询实例')

    with allure.step('点击列表的实例ID，进入实例的账号页面'):
        click_operation(page, ManagementInstanceListBase().InstanceIdXpath(instanceId), text=f'点击实例ID:{instanceId}，进入实例的账号页面')

    with allure.step('账号列表页面输入差分账号'):
        search_condition_input_server_number(page, tryServerNumber)

    with allure.step('点击查询按钮，查询该账号'):
        click_operation(page, ManagementServerNumberBase().SearchButtonXpath(), text='点击查询按钮')

    with allure.step('获取账号的账号类型'):
        serverType = get_element_content(page, ManagementServerNumberBase().ServerNumberTypeXpath(tryServerNumber), '获取账号类型')

    with allure.step('验证账号类型为正式账号'):
        assert serverType == '正式账号'
