from base.ClientHomeBase import ClientHomeBase
from common.userstestok import *
from base.ClientCmInstanceListBase import ClientInstanceList
from base.ClientLeftNavigationBar import ClientLeftNavigationBar
from page.ClientHomePage import click_purchase_button
from page.CommonPageFunction import *
from page.ClientSubmitOrderPage import *
from page.ClientPaymentOrderPage import *
from page.ClientProductDetailPage import *
from page.ClientPage import go_to_cm_service_instance_page, go_to_dm_service_instance_page
from common.allure_function import write_log_to_allure_report
from base.ClientCmFormalServerNumberBase import ClientCmFormalServerNumberBase


# @allure.feature('官网购买账号，登录成功')
# def test_purchase_liqing_auto_active_auto_bind_server_number_ntrip_login(browser_login_client, get_random_number, get_nrtk_broadcast_url, get_li_qing_mount_point, get_nrtk_port):
#     '''
#     官网购买-购买、自动激活、自动绑定方式的厘清账号,ntrip方式登录成功
#     @param browser_login_client:
#     @param get_random_number:
#     @return:
#     '''
#     purchaseNumber = get_random_number
#     browser_name = browser_login_client['name']
#     page = browser_login_client['page']
#     allure.dynamic.title(f'{browser_name}浏览器-官网购买自动激活、自动绑定方式的厘清账号,使用ntrip方式登录成功')
#
#     with allure.step('登录成功，进入首页'):
#         write_log_to_allure_report(page, '登录成功，进入首页')
#
#     with allure.step('点击六分图标进入首页'):
#         click_operation(page, ClientLeftNavigationBar().SixentsIconXpath(), text='点击六分图标进入首页')
#
#     with allure.step('点击首页厘清购买按钮，进入厘清详情页面'):
#         click_purchase_button(page)
#
#     with allure.step('购买账号'):
#         purchase_server_number(page, purchaseQuantity=purchaseNumber)
#
#     with allure.step('提交订单'):
#         click_submit_order_button(page)
#
#     with allure.step('确认支付'):
#         click_pay_order_button(page)
#
#     with allure.step('去厘米级实例页面'):
#         go_to_cm_service_instance_page(page)
#
#     with allure.step('点击实例列表第一个正式账号进入详情页面'):
#         click_operation(page, ClientInstanceList().CmInstanceListInstanceFormalAccountNumberButtonXpath(), text='点击实例列表页面，第一个实例的正式账号数量，进入账号页面')
#
#     with allure.step('获取页面的第一个差分账号'):
#         ServerNumber = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageRankServerNumberXpath(rank=1), log=False)
#         write_log_to_allure_report(page, text=f'获取的差分账号为{ServerNumber}')
#
#     with allure.step('点击差分账号的密码查看按钮'):
#         click_operation(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberCheckButtonXpath(ServerNumber), text='点击差分账号的密码查看按钮')
#
#     with allure.step('获取页面第一个差分账号的密码'):
#         severNumberPassword = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberPasswordXpath(), log=False)
#         write_log_to_allure_report(page, text=f'获取的差分账号密码为{severNumberPassword}')
#
#     with allure.step('使用NTtrip方式登录获取差分数据'):
#         loginResult = ntrip_send_gga(get_nrtk_broadcast_url, get_li_qing_mount_point, get_nrtk_port, ServerNumber, severNumberPassword)
#         assert loginResult == True, f'账号{ServerNumber}登录失败'
#         write_log_to_allure_report(page, text=f'账号{ServerNumber}，登录成功，结果为：{loginResult}')
#
#
# @allure.feature('官网购买账号，登录成功')
# def test_purchase_fenming_auto_active_auto_bind_server_number_ntrip_login(browser_login_client, get_random_number, get_nrtk_broadcast_url, get_fen_ming_mount_point, get_nrtk_port):
#     '''
#     官网购买-购买、自动激活、自动绑定方式的分明账号,ntrip方式登录成功
#     @param browser_login_client:
#     @param get_random_number:
#     @return:
#     '''
#     purchaseNumber = get_random_number
#     browser_name = browser_login_client['name']
#     page = browser_login_client['page']
#     allure.dynamic.title(f'{browser_name}浏览器-官网购买自动激活、自动绑定方式的分明账号,使用ntrip方式登录成功')
#
#     with allure.step('登录成功，进入首页'):
#         write_log_to_allure_report(page, '登录成功，进入首页')
#
#     with allure.step('点击六分图标进入首页'):
#         click_operation(page, ClientLeftNavigationBar().SixentsIconXpath(), text='点击六分图标进入首页')
#
#     with allure.step('点击首页分明购买按钮，进入分明详情页面'):
#         click_purchase_button(page, product=2)
#
#     with allure.step('购买账号'):
#         purchase_server_number(page, purchaseQuantity=purchaseNumber)
#
#     with allure.step('提交订单'):
#         click_submit_order_button(page)
#
#     with allure.step('确认支付'):
#         click_pay_order_button(page)
#
#     with allure.step('去亚米级实例页面'):
#         go_to_dm_service_instance_page(page)
#
#     with allure.step('点击实例列表第一个正式账号进入详情页面'):
#         click_operation(page, ClientInstanceList().CmInstanceListInstanceFormalAccountNumberButtonXpath(), text='点击实例列表页面，第一个实例的正式账号数量，进入账号页面')
#
#     with allure.step('获取页面的第一个差分账号'):
#         ServerNumber = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageRankServerNumberXpath(rank=1), log=False)
#         write_log_to_allure_report(page, text=f'获取的差分账号为{ServerNumber}')
#
#     with allure.step('点击差分账号的密码查看按钮'):
#         click_operation(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberCheckButtonXpath(ServerNumber), text='点击差分账号的密码查看按钮')
#
#     with allure.step('获取页面第一个差分账号的密码'):
#         severNumberPassword = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberPasswordXpath(), log=False)
#         write_log_to_allure_report(page, text=f'获取的差分账号密码为{severNumberPassword}')
#
#     with allure.step('使用NTtrip方式登录获取差分数据'):
#         loginResult = ntrip_send_gga(get_nrtk_broadcast_url, get_fen_ming_mount_point, get_nrtk_port, ServerNumber, severNumberPassword)
#         assert loginResult == True, f'账号{ServerNumber}登录失败'
#         write_log_to_allure_report(page, text=f'账号{ServerNumber}，登录成功，结果为：{loginResult}')


@allure.feature('官网购买账号，登录成功')
def test_purchase_orion_auto_active_auto_bind_server_number_ntrip_login(browser_login_client, get_random_number, get_ppp_rtk_broadcast_url, get_orion_mount_point, get_ppp_rtk_port):
    '''
    官网购买-购买、自动激活、自动绑定方式的星璨账号,ntrip方式登录成功
    @param browser_login_client:
    @param get_random_number:
    @return:
    '''
    purchaseNumber = get_random_number
    browser_name = browser_login_client['name']
    page = browser_login_client['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网购买自动激活、自动绑定方式的星璨账号,使用ntrip方式登录成功')

    with allure.step('登录成功，进入首页'):
        write_log_to_allure_report(page, '登录成功，进入首页')

    with allure.step('点击六分图标进入首页'):
        click_operation(page, ClientLeftNavigationBar().SixentsIconXpath(), text='点击六分图标进入首页')

    with allure.step('点击首页星璨购买按钮，进入星璨详情页面'):
        click_purchase_button(page, product=3)

    with allure.step('购买账号'):
        purchase_server_number(page, purchaseQuantity=purchaseNumber)

    with allure.step('提交订单'):
        click_submit_order_button(page)

    with allure.step('确认支付'):
        click_pay_order_button(page)

    with allure.step('去厘米级实例页面'):
        go_to_cm_service_instance_page(page)

    with allure.step('点击产品名称选择框，弹出选择列表'):
        click_operation(page, ClientInstanceList().ProductNameSelectXpath(), text='点击产品名称选择框，弹出选择列表')

    with allure.step('产品名称选择列表，选择星璨'):
        click_operation(page, ClientInstanceList().ProductNameSelectOrionXpath(), text='产品名称选择列表，选择星璨')

    sleep(15)

    with allure.step('点击查询按钮，查询出星璨实例'):
        click_operation(page, ClientInstanceList().QueryButtonXpath(), text='点击查询按钮，查询出星璨实例')

    with allure.step('点击星璨实例列表第一个正式账号进入详情页面'):
        click_operation(page, ClientInstanceList().CmInstanceListInstanceFormalAccountNumberButtonXpath(), text='点击实例列表页面，第一个实例的正式账号数量，进入账号页面')

    with allure.step('获取页面的第一个差分账号'):
        ServerNumber = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageRankServerNumberXpath(rank=1), log=False)
        write_log_to_allure_report(page, text=f'获取的差分账号为{ServerNumber}')

    with allure.step('点击差分账号的密码查看按钮'):
        click_operation(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberCheckButtonXpath(ServerNumber), text='点击差分账号的密码查看按钮')

    with allure.step('获取页面第一个差分账号的密码'):
        severNumberPassword = get_element_content(page, ClientCmFormalServerNumberBase().ClientCmFormalServerNumberPageServerNumberPasswordXpath(), log=False)
        write_log_to_allure_report(page, text=f'获取的差分账号密码为{severNumberPassword}')

    with allure.step('使用NTtrip方式登录获取差分数据'):
        loginResult = ntrip_send_gga(get_ppp_rtk_broadcast_url, get_orion_mount_point, get_ppp_rtk_port, ServerNumber, severNumberPassword)
        assert loginResult == True, f'账号{ServerNumber}登录失败'
        write_log_to_allure_report(page, text=f'账号{ServerNumber}，登录成功，结果为：{loginResult}')
