from page.ClientHomePage import *
from page.ClientSubmitOrderPage import *
from page.ClientPaymentOrderPage import *
from page.ClientProductDetailPage import *
from common.allure_function import write_log_to_allure_report


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买1天、自动激活、自动绑定方式的厘清账号')
def test_home_page_purchase_one_day_liqing_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买1个月、自动激活、自动绑定方式的厘清账号')
def test_home_page_purchase_one_month_liqing_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=2)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买1年、自动激活、自动绑定方式的厘清账号')
def test_home_page_purchase_one_year_liqing_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=3)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买1000个、1月、自动激活、自动绑定方式的厘清账号')
def test_home_page_purchase_1000_one_month_liqing_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=2, purchaseQuantity=1000)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买100个、1月、自动激活、手动绑定方式的厘清账号')
def test_home_page_purchase_100_one_month_liqing_auto_active_manual_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=2, bindMethod=2, purchaseQuantity=100)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买10个、1月、手动激活、自动绑定方式的厘清账号')
def test_home_page_purchase_10_one_month_liqing_manual_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=2, activeMethod=2, purchaseQuantity=10)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买10个、1月、手动激活、手动绑定方式的厘清账号')
def test_home_page_purchase_10_one_month_liqing_manual_active_manual_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
        click_purchase_button(chromium_client_login)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, duration=2, activeMethod=2, bindMethod=2, purchaseQuantity=10)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买10个、1天、自动激活、自动绑定方式的分明账号')
def test_home_page_purchase_10_one_day_fenming_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页分明购买按钮，进入分明详情页面'):
        click_purchase_button(chromium_client_login, product=2)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, purchaseQuantity=10)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买100个、1月、自动激活、自动绑定方式的分明账号')
def test_home_page_purchase_100_one_month_fenming_auto_active_auto_bind_server_number(chromium_client_login):
    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(chromium_client_login, '登录成功，进入首页')

    with allure.step('点击首页分明购买按钮，进入分明详情页面'):
        click_purchase_button(chromium_client_login, product=2)

    with allure.step('购买账号'):
        purchase_server_number(chromium_client_login, purchaseQuantity=100)

    with allure.step('提交订单'):
        click_submit_order_button(chromium_client_login)

    with allure.step('确认支付'):
        click_pay_order_button(chromium_client_login)
