import os
import shutil
import pytest

# 公司电脑的allure路径
allure_path = r'D:\python3.10.10\Scripts\allure-2.13.2\bin\allure.bat'
# allure_path = r'D:\python3.8\Scripts\allure-2.13.2\bin\allure.bat'
# 家里的台式机电脑allure路径
# allure_path = r'E:\allure-2.13.2\bin\allure.bat'
# 家里的笔记本电脑allure路径
# allure_path = r'D:\Software\allure-2.27.0\bin\allure.bat'
# 执行结果路径
result_path = os.path.join(os.getcwd(), 'result')

# 删除老的测试结果
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if os.path.exists('./result/'):
    shutil.rmtree('./result/')
if os.path.exists('./logs/log'):
    shutil.rmtree('./logs/log')

# pytest主函数
pytest.main(['-s', '-vs', './testcases', '--capture=sys', '--alluredir=./result/', '--html=./result/report.html', '--self-contained-html'])
# 直接执行allure服务
# os.system('allure serve ./result/')

# 生成report报告文件
os.system(f'{allure_path} generate {result_path} -o ./report/ --clean')