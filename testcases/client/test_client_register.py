from base.ClientHomeBase import ClientHomeBase
from base.CommonElementBase import CommonElementBase
from page.ClientRegisterPage import *
from page.ManagementLoginPage import *
from base.ClientLoginBase import ClientLoginBase
from page.ClientPage import go_to_home_page_no_login
from page.ClientHomePage import click_register_button
from common.playwright_function import save_directory


@allure.feature('首页注册跳转')
def test_register_button_jump(browser):
    '''
    测试点击首页注册按钮，成功跳转到注册页面
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-点击首页注册按钮，成功跳转到注册页面')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_alphabet(browser):
    '''
    测试手机号输入字母，提示:手机号不正确
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-手机号输入字母，提示:手机号不正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)

    with allure.step('输入字母'):
        input_phone_number(page, 'ahagsgtQw')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_10_number(browser):
    '''
    输入10位数字，提示:手机号不正确
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-手机号输入10位数字，提示:手机号不正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)

    with allure.step('输入10位数字'):
        input_phone_number(page, '1332541124')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_12_number(browser):
    '''
    输入12位数字，提示:手机号不正确
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-手机号输入12位数字，提示:手机号不正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)

    with allure.step('输入12位数字'):
        input_phone_number(page, '133254112436')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_chinese(browser):
    '''
    手机号输入汉字，提示:手机号不正确
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-手机号输入汉字，提示:手机号不正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)

    with allure.step('输入汉字'):
        input_phone_number(page, '测试文案汉字')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_none(browser):
    '''
    手机号输入为空，提示:手机号不正确
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-手机号输入为空，提示:手机号不正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮'):
        click_register_button(page)

    with allure.step('验证是否进入注册页面'):
        assert_into_register_page_success(page)

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('提示:请输入正确的手机号'):
        assert_input_phone_number_incorrect(page)


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_registered_phone_number(browser, get_client_login_information):
    '''
    输入已注册的手机号，提示:该手机号已注册
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    username, password = get_client_login_information
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-输入已注册的手机号，提示:该手机号已注册')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('输入已注册的手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), username, text=f'输入已注册的手机号:{username}')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('滑动滑块验证'):
        while True:
            frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
            download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
            download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
            write_log_to_allure_report(page, '下载滑块图片成功')
            position = dragbox_location(page)
            x = position['x'] + position['width'] / 2
            y = position['y'] + position['height'] / 2
            distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
            write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
            page.mouse.move(x, y)
            page.mouse.down()
            for i in distance:
                x = x + i
                page.mouse.move(x, y)
            page.mouse.up()
            write_log_to_allure_report(page, '滑块滑动完成')
            if check_element_with_timeout(page, CommonElementBase().SpanElementXpath('该手机号已注册')):
                break
            page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
            write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')

    with allure.step('提示:该手机号已注册'):
        assert_element_exist(page, CommonElementBase().SpanElementXpath('该手机号已注册'))


@allure.feature('注册手机号验证')
def test_client_register_phone_number_input_unregistered_phone_number(browser):
    '''
    输入未注册的手机号，短信验证码发送成功
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-输入未注册的手机号，短信验证码发送成功')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('输入未注册的手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), '18888886666', text='输入未注册的手机号:18888886666')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('滑动滑块验证'):
        while True:
            frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
            download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
            download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
            write_log_to_allure_report(page, '下载滑块图片成功')
            position = dragbox_location(page)
            x = position['x'] + position['width'] / 2
            y = position['y'] + position['height'] / 2
            distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
            write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
            page.mouse.move(x, y)
            page.mouse.down()
            for i in distance:
                x = x + i
                page.mouse.move(x, y)
            page.mouse.up()
            write_log_to_allure_report(page, '滑块滑动完成')
            if check_element_with_timeout(page, ClientLoginBase().regetVerificationCodeButtonXpath()):
                break
            page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
            write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')

    with allure.step('验证码发送成功'):
        assert_element_exist(page, CommonElementBase().SpanElementContainsTextXpath('重新获取'))


@allure.feature('注册验证码验证')
def test_client_register_input_none_vertification_code(browser):
    '''
    验证码不输入，提示：请输入验证码
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-验证码不输入，提示：请输入验证码')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('输入未注册的手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), '18888886666', text='输入未注册的手机号:18888886666')

    with allure.step('勾选协议'):
        click_operation(page, ClientRegisterBase().UserServiceAgreementChoiceInputFrameXpath(), text='勾选协议')

    with allure.step('点击立即绑定按钮'):
        click_operation(page, CommonElementBase().SpanElementXpath('立即绑定'), text='点击立即绑定按钮')

    with allure.step('提示：请输入验证码'):
        assert_element_exist(page, CommonElementBase().DivElementContainsTextXpath('请输入验证码'))


@allure.feature('注册验证码验证')
def test_client_register_input_expire_vertification_code(browser):
    '''
    验证码大于6位，提示：验证码错误！
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-验证码大于6位，提示：验证码错误！')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('输入手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), '18888886666', text='输入未注册的手机号:18888886666')

    with allure.step('输入过期的验证码'):
        input_operation(page, ClientRegisterBase().VerificationCodeInputFrameXpath(), '00000000', text='输入错误的验证码:000000')

    with allure.step('勾选协议'):
        click_operation(page, ClientRegisterBase().UserServiceAgreementChoiceInputFrameXpath(), text='勾选协议')

    with allure.step('点击立即绑定按钮'):
        click_operation(page, CommonElementBase().SpanElementXpath('立即绑定'), text='点击立即绑定按钮')

    with allure.step('提示：验证码错误'):
        assert_element_exist(page, CommonElementBase().SpanElementContainsTextXpath('验证码错误'))


@allure.feature('注册验证码验证')
def test_client_register_input_mistake_vertification_code(browser):
    '''
    输入错误的验证码，提示：验证码错误！
    @param page:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册- 输入错误的验证码，提示：验证码错误！')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('输入未注册的手机号'):
        input_operation(page, ClientLoginBase().loginInputXpath('11位手机号'), '18888886666', text='输入未注册的手机号:18888886666')

    with allure.step('点击获取验证码'):
        click_get_verification_code(page)

    with allure.step('滑动滑块验证'):
        while True:
            frame_xpath = ClientLoginBase().sliderVerificationIframeXpath()
            download_images(page, image_name="slider", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderPicXpath(), save_directory=save_directory)
            download_images(page, image_name="background", frame_xpath=frame_xpath, image_xpath=ClientLoginBase().sliderBackPicXpath(), save_directory=save_directory)
            write_log_to_allure_report(page, '下载滑块图片成功')
            position = dragbox_location(page)
            x = position['x'] + position['width'] / 2
            y = position['y'] + position['height'] / 2
            distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
            write_log_to_allure_report(page, f'计算滑块的滑动距离成功，滑动距离为：{distance}')
            page.mouse.move(x, y)
            page.mouse.down()
            for i in distance:
                x = x + i
                page.mouse.move(x, y)
            page.mouse.up()
            write_log_to_allure_report(page, '滑块滑动完成')
            if check_element_with_timeout(page, ClientLoginBase().regetVerificationCodeButtonXpath()):
                break
            page.wait_for_selector(frame_xpath).content_frame().click(ClientLoginBase().refreshSliderBackPicButtonXpath())
            write_log_to_allure_report(page, '滑动验证失败，再次点击刷新滑块图片')

    with allure.step('验证码发送成功'):
        assert_element_exist(page, CommonElementBase().SpanElementContainsTextXpath('重新获取'))

    with allure.step('输入错误的验证码'):
        input_operation(page, ClientRegisterBase().VerificationCodeInputFrameXpath(), '888888', text='输入错误的验证码:888888')

    with allure.step('勾选协议'):
        click_operation(page, ClientRegisterBase().UserServiceAgreementChoiceInputFrameXpath(), text='勾选协议')

    with allure.step('点击立即绑定按钮'):
        click_operation(page, CommonElementBase().SpanElementXpath('立即绑定'), text='点击立即绑定按钮')

    with allure.step('提示：验证码错误！'):
        assert_element_exist(page, CommonElementBase().SpanElementContainsTextXpath('验证码错误'))


@allure.feature('注册服务协议验证')
def test_client_register_click_user_service_entrance(browser):
    '''
    点击用户服务协议，跳转到协议查看页面，协议内容正确
    @param browser:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-协议查看：点击用户服务协议，跳转到协议查看页面，协议内容正确')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('点击用户服务协议查看入口'):
        click_operation(page, ClientRegisterBase().UserServiceAgreementEntranceXpath(), text='点击用户服务协议查看入口')

    with allure.step('验证是否进入服务协议页面'):
        assert_element_exist(page, ClientRegisterBase().UserServiceAgreementDetailPageTitleXpath())


@allure.feature('测试官网注册')
def test_client_register_click_back_to_home_page(browser):
    '''
    点击注册页面返回首页，返回首页成功
    @param browser:
    @return:
    '''
    browser_name = browser['name']
    page = browser['page']
    allure.dynamic.title(f'{browser_name}浏览器-官网注册-点击注册页面返回首页，返回首页成功')

    with allure.step('打开网址进入首页'):
        go_to_home_page_no_login(page)

    with allure.step('点击注册按钮,进入注册页面'):
        click_register_button(page)

    with allure.step('点击注册页面返回首页'):
        click_operation(page, CommonElementBase().AlabelElementContainsTextXpath('返回首页'), text='点击注册页面返回首页')

    with allure.step('验证是否进入服务协议页面'):
        assert_element_exist(page, ClientHomeBase().liqingHomePageTitleXpath())
