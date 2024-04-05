from page.ClientPage import *
from page.ClientSubmitOrderPage import *
from page.ClientPaymentOrderPage import *
from page.ClientInstanceExpandPage import *
from common.allure_function import write_log_to_allure_report
from page.ClientInstanceExpandPage import expand_server_number

LiQing = LiQingExpandInstanceId
FenMing = FenMingExpandInstanceId


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---厘清实例列表扩容差分账号,扩容成功')
def test_liqing_instance_list_expand_server_number_chromium_browser(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number1 = search_instance(chromium_client_login, LiQing)

    with allure.step('扩容实例'):
        expand_server_number(chromium_client_login, LiQing)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('余额支付订单'):
        click_pay_order_button(chromium_client_login)

    with allure.step('再次进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number2 = search_instance(chromium_client_login, LiQing)

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + sums


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---厘清实例列表扩容差分账号,扩容1000个，扩容成功')
def test_liqing_instance_list_expand_1000_server_number_chromium_browser(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number1 = search_instance(chromium_client_login, LiQing)

    with allure.step('扩容实例'):
        expand_server_number(chromium_client_login, LiQing, sums=1000)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('余额支付订单'):
        click_pay_order_button(chromium_client_login)

    with allure.step('再次进入厘米级服务实例页面'):
        go_to_cm_service_instance_page(chromium_client_login)

    sleep(5)

    with allure.step('查询扩容的实例'):
        number2 = search_instance(chromium_client_login, LiQing)

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + 1000


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---实例列表扩容差分账号,扩容成功')
def test_fenming_instance_list_expand_server_number_chromium_browser(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number1 = search_instance(chromium_client_login, FenMing)

    with allure.step('扩容实例'):
        expand_server_number(chromium_client_login, FenMing)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('余额支付订单'):
        click_pay_order_button(chromium_client_login)

    with allure.step('再次进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number2 = search_instance(chromium_client_login, FenMing)

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + sums


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---实例列表扩容差分账号,扩容成功')
def test_fenming_instance_list_expand_1000_server_number_chromium_browser(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number1 = search_instance(chromium_client_login, FenMing)

    with allure.step('扩容实例'):
        expand_server_number(chromium_client_login, FenMing, sums=1000)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('余额支付订单'):
        click_pay_order_button(chromium_client_login)

    with allure.step('再次进入亚米级服务实例页面'):
        go_to_dm_service_instance_page(chromium_client_login)

    with allure.step('查询扩容的实例'):
        number2 = search_instance(chromium_client_login, FenMing)

    with allure.step('验证扩容后实例下的账号数量'):
        assert int(number2) == int(number1) + 1000
