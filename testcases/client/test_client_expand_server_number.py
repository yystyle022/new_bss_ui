from page.ClientPage import *
from page.CommonPageFunction import *
from page.ClientSubmitOrderPage import *
from page.ClientPaymentOrderPage import *
from page.ClientInstanceExpandPage import *
from base.ClientCmInstanceListBase import ClientInstanceList
from common.allure_function import write_log_to_allure_report
from page.ClientInstanceExpandPage import expand_server_number


@allure.feature('官网厘清实例列表扩容差分账号,扩容成功')
def test_liqing_instance_list_expand_server_number(browser_login_client, get_expand_liqing_instanceId, get_random_number):
    '''
    厘清实例扩容差分账号
    @param browser_login_client:
    @param get_expand_liqing_instanceId:
    @param get_random_number:
    @return:
    '''
    expandNumber = get_random_number
    instanceId = get_expand_liqing_instanceId
    browser_name = browser_login_client['name']
    page = browser_login_client['page']
    allure.dynamic.title(f'{browser_name}浏览器-厘清实例列表扩容差分账号')

    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(page, '登录成功，进入首页')

    with allure.step('进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(page)

    with allure.step('查询扩容的实例'):
        client_instance_list_page_query_instance_id(page, instanceId)

    with allure.step('获取扩容前实例下的账号数量'):
        number1 = int(get_element_content(page, ClientInstanceList().InstanceFormalAccountNumberSumsXpath(instanceId), text=f'获取实例{instanceId}下的正式账号数量'))

    with allure.step('扩容实例'):
        expand_server_number(page, instanceId, sums=expandNumber)

    with allure.step('提交订单'):
        click_submit_order_button(page)

    with allure.step('余额支付订单'):
        click_pay_order_button(page)

    with allure.step('再次进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(page)

    with allure.step('查询扩容的实例'):
        client_instance_list_page_query_instance_id(page, instanceId)

    with allure.step('获取扩容后实例下的账号数量'):
        number2 = int(get_element_content(page, ClientInstanceList().InstanceFormalAccountNumberSumsXpath(instanceId), text=f'获取实例{instanceId}下的正式账号数量'))

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + expandNumber


@allure.feature('官网分明实例列表扩容差分账号,扩容成功')
def test_fenming_instance_list_expand_server_number(browser_login_client, get_expand_fenming_instanceId, get_random_number):
    '''
    分明实例扩容差分账号
    @param browser_login_client:
    @param get_expand_liqing_instanceId:
    @param get_random_number:
    @return:
    '''
    expandNumber = get_random_number
    instanceId = get_expand_fenming_instanceId
    browser_name = browser_login_client['name']
    page = browser_login_client['page']
    allure.dynamic.title(f'{browser_name}浏览器-分明实例列表扩容差分账号')

    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(page, '登录成功，进入首页')

    with allure.step('进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(page)

    with allure.step('查询扩容的实例'):
        client_instance_list_page_query_instance_id(page, instanceId)

    with allure.step('获取扩容前实例下的账号数量'):
        number1 = int(get_element_content(page, ClientInstanceList().InstanceFormalAccountNumberSumsXpath(instanceId), text=f'获取实例{instanceId}下的正式账号数量'))

    with allure.step('扩容实例'):
        expand_server_number(page, instanceId, sums=expandNumber)

    with allure.step('提交订单'):
        click_submit_order_button(page)

    with allure.step('余额支付订单'):
        click_pay_order_button(page)

    with allure.step('再次进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(page)

    with allure.step('查询扩容的实例'):
        client_instance_list_page_query_instance_id(page, instanceId)

    with allure.step('获取扩容后实例下的账号数量'):
        number2 = int(get_element_content(page, ClientInstanceList().InstanceFormalAccountNumberSumsXpath(instanceId), text=f'获取实例{instanceId}下的正式账号数量'))

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + expandNumber
