from common.playwrightFunction import write_log_to_allure, screenshot_to_allure


def write_log_to_allure_report(page, text, screenshot=True, log=False):
    try:
        if screenshot:
            screenshot_to_allure(page, text)
        if log:
            write_log_to_allure(text)
    except Exception:
        raise '日志写入异常...'
