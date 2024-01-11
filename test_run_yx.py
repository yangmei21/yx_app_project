# 查看当前设备的包/activity命令:         adb shell dumpsys activity recents | find "intent={"
# cmp=top.youxian.app/io.dcloud.PandoraEntry
'''
package名称:top.youxian.app
启动Activity:io.dcloud.PandoraEntry
'''
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',  # 被测手机是安卓
            'platformVersion': '11',  # 手机安卓版本
            'deviceName': 'Mei 9',  # 设备名，安卓手机可以随意填写
            'appPackage': 'top.youxian.app',  # 启动APP Package名称
            'appActivity': 'io.dcloud.PandoraEntry',  # 启动Activity名称
            'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'noReset': False,  # 不要重置App
            'newCommandTimeout': 6000,
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)
        # 如果有弹框，则点击接受
        box = self.driver.find_element(By.ID, 'btn_custom_privacy_sure')
        if box:
            box.click()

    def test_login_err(self):
        """错误的登录；不输入登录账号、密码"""
        btn_login = self.driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View')
        btn_login.click()
        btn_login.click()
        btn_login.click()
        text = '请输入'
        # text模糊定位
        element = self.driver.find_element_by_xpath('//*[contains(@text, "%s")]' % text)
        print("toast内容：%s" % element.text)
        self.assertEqual(element.text, '请输入手机号')

    def test_login_right(self):
        """登录测试"""
        user = self.driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')
        user.send_keys('18890059003')

        pwd = self.driver.find_element(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText')
        pwd.send_keys('999999')
        # 勾选框
        option = self.driver.find_element(By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View')
        option.click()
        btn_login = self.driver.find_element(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[5]/android.view.View')
        btn_login.click()
        sleep(2)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
